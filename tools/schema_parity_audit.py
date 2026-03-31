#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple, Set

try:
    import yaml  # type: ignore
except Exception as e:
    raise SystemExit(f"PyYAML is required: {e}")


ROOT = Path(__file__).resolve().parents[1]
BECKN_PATH = (ROOT / "../protocol-specifications-v2/api/v2.0.0/beckn.yaml").resolve()
SCHEMA_ROOT = ROOT / "schema"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def semver_key(ver_dir: str) -> Tuple[int, ...]:
    m = re.fullmatch(r"v(\d+)(?:\.(\d+))?(?:\.(\d+))?", ver_dir)
    if not m:
        return (-1,)
    return tuple(int(x) if x is not None else 0 for x in m.groups())


def pointer_get(doc: Any, pointer: str) -> Any:
    if pointer == "" or pointer == "/":
        return doc
    if not pointer.startswith("/"):
        raise KeyError(f"Invalid JSON pointer: {pointer}")
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
        if "$ref" in node and isinstance(node["$ref"], str) and node["$ref"].startswith("#"):
            ref = node["$ref"]
            pointer = ref[1:]
            if ref in stack:
                return node
            try:
                target = pointer_get(root_doc, pointer)
                resolved_target = resolve_local_refs(target, root_doc, stack + (ref,))
                sibling = {k: v for k, v in node.items() if k != "$ref"}
                if sibling:
                    merged = {}
                    if isinstance(resolved_target, dict):
                        merged.update(resolved_target)
                    else:
                        merged = {"__resolved_ref_value__": resolved_target}
                    for k, v in sibling.items():
                        merged[k] = resolve_local_refs(v, root_doc, stack)
                    return merged
                return resolved_target
            except Exception:
                pass
        return {k: resolve_local_refs(v, root_doc, stack) for k, v in node.items()}
    if isinstance(node, list):
        return [resolve_local_refs(v, root_doc, stack) for v in node]
    return node


def collect_local_schema_refs(obj: Any, out: Set[str]) -> None:
    if isinstance(obj, dict):
        ref = obj.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
            tail = ref.split("#/components/schemas/", 1)[1]
            name = tail.split("/", 1)[0]
            if name:
                out.add(name)
        for v in obj.values():
            collect_local_schema_refs(v, out)
    elif isinstance(obj, list):
        for v in obj:
            collect_local_schema_refs(v, out)


def deep_diff(a: Any, b: Any, path: str = "$") -> List[Dict[str, Any]]:
    diffs: List[Dict[str, Any]] = []
    if type(a) != type(b):
        diffs.append({"path": path, "beckn": a, "schema": b, "reason": "type_mismatch"})
        return diffs

    if isinstance(a, dict):
        a_keys = set(a.keys())
        b_keys = set(b.keys())
        for k in sorted(a_keys - b_keys):
            diffs.append({"path": f"{path}.{k}", "beckn": a[k], "schema": "<missing>", "reason": "missing_in_schema"})
        for k in sorted(b_keys - a_keys):
            diffs.append({"path": f"{path}.{k}", "beckn": "<missing>", "schema": b[k], "reason": "missing_in_beckn"})
        for k in sorted(a_keys & b_keys):
            diffs.extend(deep_diff(a[k], b[k], f"{path}.{k}"))
        return diffs

    if isinstance(a, list):
        if len(a) != len(b):
            diffs.append({"path": path, "beckn": f"len={len(a)}", "schema": f"len={len(b)}", "reason": "list_length_mismatch"})
        for i, (av, bv) in enumerate(zip(a, b)):
            diffs.extend(deep_diff(av, bv, f"{path}[{i}]"))
        return diffs

    if a != b:
        diffs.append({"path": path, "beckn": a, "schema": b, "reason": "value_mismatch"})
    return diffs


def schema_name_to_latest_file(schema_root: Path) -> Dict[str, Path]:
    result: Dict[str, Path] = {}
    for child in sorted(schema_root.iterdir()):
        if not child.is_dir():
            continue
        versions = []
        for v in child.iterdir():
            if v.is_dir() and semver_key(v.name) != (-1,):
                schema_json = v / "schema.json"
                if schema_json.exists():
                    versions.append((semver_key(v.name), schema_json))
        if versions:
            versions.sort(key=lambda x: x[0], reverse=True)
            result[child.name] = versions[0][1]
    return result


def main() -> int:
    if not BECKN_PATH.exists():
        raise SystemExit(f"beckn.yaml not found: {BECKN_PATH}")
    if not SCHEMA_ROOT.exists():
        raise SystemExit(f"schema dir not found: {SCHEMA_ROOT}")

    beckn_doc = load_yaml(BECKN_PATH)
    components = beckn_doc.get("components", {})
    beckn_schemas: Dict[str, Any] = components.get("schemas", {})

    names_from_defs = set(beckn_schemas.keys())
    names_from_refs: Set[str] = set()
    collect_local_schema_refs(beckn_doc, names_from_refs)
    beckn_all_names = sorted(names_from_defs | names_from_refs)

    latest_schema_files = schema_name_to_latest_file(SCHEMA_ROOT)
    schema_all_names = sorted(latest_schema_files.keys())

    matched = [n for n in beckn_all_names if n in latest_schema_files]
    missing_in_schema = [n for n in beckn_all_names if n not in latest_schema_files]
    missing_in_beckn = [n for n in schema_all_names if n not in beckn_all_names]

    mismatches: Dict[str, Dict[str, Any]] = {}
    for name in matched:
        if name not in beckn_schemas:
            continue

        beckn_schema_raw = beckn_schemas[name]
        beckn_root = {"components": {"schemas": beckn_schemas}}
        beckn_schema = resolve_local_refs(beckn_schema_raw, beckn_root)

        schema_file = latest_schema_files[name]
        schema_doc = load_json(schema_file)
        schema_resolved = resolve_local_refs(schema_doc, schema_doc)

        diffs = deep_diff(beckn_schema, schema_resolved)
        if diffs:
            mismatches[name] = {
                "schema_file": str(schema_file.relative_to(ROOT)),
                "diff_count": len(diffs),
                "diffs": diffs,
            }

    report = {
        "inputs": {
            "beckn_yaml": str(BECKN_PATH),
            "schema_root": str(SCHEMA_ROOT),
        },
        "counts": {
            "total_schemas_in_beckn": len(beckn_all_names),
            "matched_schemas": len(matched),
            "missing_in_schema": len(missing_in_schema),
            "missing_in_beckn_yaml": len(missing_in_beckn),
            "mismatched_schemas": len(mismatches),
        },
        "matched": {
            n: str(latest_schema_files[n].relative_to(ROOT)) for n in matched
        },
        "missing_in_schema": missing_in_schema,
        "missing_in_beckn_yaml": missing_in_beckn,
        "mismatches": mismatches,
        "verdict": "PASS" if (not missing_in_schema and not mismatches) else "FAIL",
        "notes": [
            "Comparison resolves local/internal $ref references (starting with '#').",
            "External refs are left as-is.",
            "Key order and formatting differences are ignored by structural comparison.",
        ],
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

