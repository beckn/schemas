#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import yaml  # type: ignore
except Exception as exc:
    raise SystemExit(f"PyYAML is required: {exc}")


RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
RDFS_NS = "http://www.w3.org/2000/01/rdf-schema#"
SCHEMA_NS = "https://schema.org/version/latest/schemaorg-current-https.jsonld"


def _extract_version_from_dir(path: Path) -> Optional[str]:
    for parent in [path.parent, path.parent.parent]:
        if parent is None:
            continue
        m = re.fullmatch(r"v(\d+\.\d+)(?:\.\d+)?", parent.name)
        if m:
            return m.group(1)
    return None


def _extract_version_from_id(schema_id: str) -> Optional[str]:
    match = re.search(r"/v(\d+\.\d+)(?:\.\d+)?(?:/|$)", schema_id)
    if match:
        return match.group(1)
    return None


def _normalize_version(version: str) -> str:
    parts = [p for p in version.strip().split(".") if p != ""]
    if not parts:
        return "2.1"
    if len(parts) == 1:
        return f"{parts[0]}.0"
    return f"{parts[0]}.{parts[1]}"


def _to_plain_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def _collect_properties(node: Any, out: Dict[str, str], seen_nodes: Set[int]) -> None:
    if isinstance(node, (dict, list)):
        node_id = id(node)
        if node_id in seen_nodes:
            return
        seen_nodes.add(node_id)

    if isinstance(node, dict):
        props = node.get("properties")
        if isinstance(props, dict):
            for key, value in props.items():
                if not isinstance(key, str) or not key:
                    continue
                desc = ""
                if isinstance(value, dict):
                    desc = _to_plain_text(value.get("description"))
                if key not in out:
                    out[key] = desc
                elif not out[key] and desc:
                    out[key] = desc
                _collect_properties(value, out, seen_nodes)

        for value in node.values():
            _collect_properties(value, out, seen_nodes)
    elif isinstance(node, list):
        for value in node:
            _collect_properties(value, out, seen_nodes)


def _pick_openapi_schema_name(doc: Dict[str, Any], fallback_name: str) -> str:
    schemas = doc.get("components", {}).get("schemas", {})
    if not isinstance(schemas, dict) or not schemas:
        raise ValueError("OpenAPI input must include components.schemas")

    if len(schemas) == 1:
        only_key = next(iter(schemas.keys()))
        if isinstance(only_key, str) and only_key:
            return only_key

    info_title = _to_plain_text(doc.get("info", {}).get("title"))
    if info_title and info_title in schemas:
        return info_title

    if fallback_name in schemas:
        return fallback_name

    for key in schemas.keys():
        if isinstance(key, str) and key:
            return key

    raise ValueError("Unable to determine schema name from components.schemas")


def load_schema_source(input_path: Path) -> Dict[str, Any]:
    path = input_path.resolve()
    if not path.exists():
        raise FileNotFoundError(f"Input not found: {path}")

    fallback_name = path.parent.parent.name if path.parent.parent else path.stem

    if path.suffix.lower() in {".yaml", ".yml"}:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError("OpenAPI file must parse to an object")

        schema_name = _pick_openapi_schema_name(doc, fallback_name)
        schema_obj = doc.get("components", {}).get("schemas", {}).get(schema_name)
        if not isinstance(schema_obj, dict):
            raise ValueError(f"Schema '{schema_name}' not found in components.schemas")

        version_raw = _to_plain_text(doc.get("info", {}).get("version"))
        version = _normalize_version(version_raw if version_raw else (_extract_version_from_dir(path) or "2.1"))

        description = _to_plain_text(schema_obj.get("description"))
        if not description:
            description = _to_plain_text(doc.get("info", {}).get("description"))

        properties: Dict[str, str] = {}
        _collect_properties(schema_obj, properties, set())

        return {
            "schema_name": schema_name,
            "version": version,
            "description": description,
            "properties": properties,
        }

    doc = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError("JSON Schema file must parse to an object")

    schema_id = _to_plain_text(doc.get("$id"))
    schema_name = fallback_name
    if schema_id:
        match = re.search(r"schema\.beckn\.io/([^/]+)/v", schema_id)
        if match:
            schema_name = match.group(1)

    version = _extract_version_from_dir(path) or _extract_version_from_id(schema_id) or "2.1"
    version = _normalize_version(version)

    description = _to_plain_text(doc.get("description"))
    properties = {}
    _collect_properties(doc, properties, set())

    return {
        "schema_name": schema_name,
        "version": version,
        "description": description,
        "properties": properties,
    }


def build_context_document(source: Dict[str, Any]) -> Dict[str, Any]:
    schema_name = source["schema_name"]
    version = source["version"]
    properties: Dict[str, str] = source["properties"]
    beckn_context_url = f"https://schema.beckn.io/LinkedData/v{version}/context.jsonld"

    context: Dict[str, Any] = {
        "@version": 1.1,
        "@protected": True,
        "beckn": beckn_context_url,
        schema_name: f"beckn:{schema_name}",
    }
    for prop in sorted(properties.keys()):
        context[prop] = f"beckn:{prop}"

    return {"@context": context}


def build_vocab_document(source: Dict[str, Any]) -> Dict[str, Any]:
    schema_name = source["schema_name"]
    version = source["version"]
    description = source["description"]
    properties: Dict[str, str] = source["properties"]
    beckn_context_url = f"https://schema.beckn.io/LinkedData/v{version}/context.jsonld"

    context: Dict[str, Any] = {
        "beckn": beckn_context_url,
        "rdf": RDF_NS,
        "rdfs": RDFS_NS,
        "schema": SCHEMA_NS,
        schema_name: f"beckn:{schema_name}",
    }
    for prop in sorted(properties.keys()):
        context[prop] = f"beckn:{prop}"

    graph: List[Dict[str, Any]] = [
        {
            "@id": f"beckn:{schema_name}",
            "@type": "rdfs:Class",
            "rdfs:label": schema_name,
            "rdfs:comment": description if description else f"Class {schema_name}",
        }
    ]

    for prop in sorted(properties.keys()):
        graph.append(
            {
                "@id": f"beckn:{prop}",
                "@type": "rdf:Property",
                "rdfs:label": prop,
                "rdfs:comment": properties[prop] if properties[prop] else f"Property {prop}",
            }
        )

    return {"@context": context, "@graph": graph}


def write_json_document(path: Path, document: Dict[str, Any]) -> None:
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
