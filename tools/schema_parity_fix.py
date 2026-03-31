#!/usr/bin/env python3
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

try:
    import yaml  # type: ignore
except Exception as e:
    raise SystemExit(f"PyYAML is required: {e}")


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "schema_parity_audit_report.json"
BECKN_PATH = (ROOT / "../protocol-specifications-v2/api/v2.0.0/beckn.yaml").resolve()
SCHEMA_ROOT = ROOT / "schema"
LOG_PATH = ROOT / "schema_parity_fix.log"
SUMMARY_PATH = ROOT / "schema_parity_fix_summary.json"


def semver_key(ver_dir: str) -> Tuple[int, ...]:
    m = re.fullmatch(r"v(\d+)(?:\.(\d+))?(?:\.(\d+))?", ver_dir)
    if not m:
        return (-1,)
    return tuple(int(x) if x is not None else 0 for x in m.groups())


def latest_version_dir(schema_name: str) -> Path:
    schema_dir = SCHEMA_ROOT / schema_name
    if not schema_dir.exists() or not schema_dir.is_dir():
        raise FileNotFoundError(f"schema dir not found: {schema_dir}")

    versions: List[Tuple[Tuple[int, ...], Path]] = []
    for child in schema_dir.iterdir():
        if child.is_dir() and semver_key(child.name) != (-1,):
            versions.append((semver_key(child.name), child))

    if not versions:
        raise FileNotFoundError(f"no semantic version dirs found under: {schema_dir}")

    versions.sort(key=lambda x: x[0], reverse=True)
    return versions[0][1]


def pointer_get(doc: Any, pointer: str) -> Any:
    if pointer in ("", "/"):
        return doc
    if not pointer.startswith("/"):
        raise KeyError(f"invalid JSON pointer: {pointer}")
    cur = doc
    for part in pointer[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def resolve_local_refs(node: Any, root_doc: Any, stack: Tuple[str, ...] = ()) -> Any:
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith("#"):
            if ref in stack:
                return node
            pointer = ref[1:]
            try:
                target = pointer_get(root_doc, pointer)
                resolved = resolve_local_refs(target, root_doc, stack + (ref,))
                sibling = {k: v for k, v in node.items() if k != "$ref"}
                if sibling:
                    merged: Dict[str, Any] = {}
                    if isinstance(resolved, dict):
                        merged.update(resolved)
                    else:
                        merged["__resolved_ref_value__"] = resolved
                    for k, v in sibling.items():
                        merged[k] = resolve_local_refs(v, root_doc, stack)
                    return merged
                return resolved
            except Exception:
                pass
        return {k: resolve_local_refs(v, root_doc, stack) for k, v in node.items()}
    if isinstance(node, list):
        return [resolve_local_refs(v, root_doc, stack) for v in node]
    return node


def load_targets(report: Dict[str, Any]) -> List[str]:
    if isinstance(report.get("mismatched_schemas"), list):
        out = [x for x in report["mismatched_schemas"] if isinstance(x, str)]
        return sorted(set(out))

    mismatches = report.get("mismatches")
    if isinstance(mismatches, dict):
        return sorted(mismatches.keys())

    if isinstance(mismatches, list):
        out = []
        for item in mismatches:
            if isinstance(item, dict) and isinstance(item.get("schema"), str):
                out.append(item["schema"])
        return sorted(set(out))

    raise ValueError(
        "Could not determine mismatch targets from schema_parity_audit_report.json"
    )


def main() -> int:
    if not REPORT_PATH.exists():
        raise SystemExit(f"report not found: {REPORT_PATH}")
    if not BECKN_PATH.exists():
        raise SystemExit(f"beckn.yaml not found: {BECKN_PATH}")
    if not SCHEMA_ROOT.exists():
        raise SystemExit(f"schema root not found: {SCHEMA_ROOT}")

    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    targets = load_targets(report)

    beckn_doc = yaml.safe_load(BECKN_PATH.read_text(encoding="utf-8"))
    beckn_schemas: Dict[str, Any] = beckn_doc.get("components", {}).get("schemas", {})

    run_started = datetime.now(timezone.utc).isoformat()
    summary: Dict[str, Any] = {
        "run_started": run_started,
        "report_source": str(REPORT_PATH),
        "beckn_source": str(BECKN_PATH),
        "target_count": len(targets),
        "targets": targets,
        "updated": {},
        "skipped": [],
    }

    for schema_name in targets:
        if schema_name not in beckn_schemas:
            summary["skipped"].append({
                "schema": schema_name,
                "reason": "missing_in_beckn_components",
            })
            continue

        latest_dir = latest_version_dir(schema_name)
        allowed_files = {
            "schema.json": latest_dir / "schema.json",
            "attributes.yaml": latest_dir / "attributes.yaml",
            "context.jsonld": latest_dir / "context.jsonld",
            "vocab.jsonld": latest_dir / "vocab.jsonld",
        }

        changed_files: List[str] = []
        details: Dict[str, Any] = {
            "latest_version_dir": str(latest_dir.relative_to(ROOT)),
            "changes": {
                "schema.json": None,
                "attributes.yaml": None,
                "context.jsonld": None,
                "vocab.jsonld": None,
            },
        }

        schema_json_path = allowed_files["schema.json"]
        if not schema_json_path.exists():
            raise FileNotFoundError(f"missing schema.json for {schema_name}: {schema_json_path}")

        current_schema_text = schema_json_path.read_text(encoding="utf-8")
        canonical_obj = resolve_local_refs(
            beckn_schemas[schema_name],
            {"components": {"schemas": beckn_schemas}},
        )
        canonical_text = json.dumps(canonical_obj, indent=2, ensure_ascii=False) + "\n"
        if current_schema_text != canonical_text:
            schema_json_path.write_text(canonical_text, encoding="utf-8")
            changed_files.append("schema.json")
            details["changes"]["schema.json"] = "replaced with canonical components.schemas definition"

        if changed_files:
            ts = datetime.now(timezone.utc).isoformat()
            log_line = (
                f"{ts}\tschema={schema_name}\tversion_dir={latest_dir.relative_to(ROOT)}"
                f"\tchanged_files={','.join(changed_files)}\n"
            )
            with LOG_PATH.open("a", encoding="utf-8") as lf:
                lf.write(log_line)
            summary["updated"][schema_name] = details

    summary["updated_count"] = len(summary["updated"])
    summary["log_file"] = str(LOG_PATH.relative_to(ROOT))
    summary["run_finished"] = datetime.now(timezone.utc).isoformat()

    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "target_count": len(targets),
        "updated_count": len(summary["updated"]),
        "skipped_count": len(summary["skipped"]),
        "summary_file": str(SUMMARY_PATH.relative_to(ROOT)),
        "log_file": str(LOG_PATH.relative_to(ROOT)),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
