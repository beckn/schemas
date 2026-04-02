#!/usr/bin/env python3
import argparse
from pathlib import Path

from jsonld_generation_utils import build_context_document, load_schema_source, write_json_document


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate context.jsonld from attributes.yaml or schema.json"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to attributes.yaml/.yml or schema.json",
    )
    parser.add_argument(
        "--output",
        help="Output path for context.jsonld (defaults next to input)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve() if args.output else (input_path.parent / "context.jsonld")

    source = load_schema_source(input_path)
    doc = build_context_document(source)
    write_json_document(output_path, doc)

    print(f"generated {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
