#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA_ROOT = ROOT / "schema"
GEN_CONTEXT = ROOT / "tools" / "generate-context-jsonld.py"
GEN_VOCAB = ROOT / "tools" / "generate-vocab-jsonld.py"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find missing context/vocab files and generate them"
    )
    parser.add_argument(
        "--schema-root",
        default=str(DEFAULT_SCHEMA_ROOT),
        help="Path to schema root (default: ./schema)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Regenerate context/vocab even if files already exist",
    )
    return parser.parse_args()


def version_dirs(schema_root: Path) -> List[Path]:
    out: List[Path] = []
    for schema_dir in sorted(schema_root.iterdir()):
        if not schema_dir.is_dir():
            continue
        for ver_dir in sorted(schema_dir.iterdir()):
            if ver_dir.is_dir() and ver_dir.name.startswith("v"):
                out.append(ver_dir)
    return out


def pick_input_file(ver_dir: Path) -> Path:
    attributes = ver_dir / "attributes.yaml"
    if attributes.exists():
        return attributes
    attributes_yml = ver_dir / "attributes.yml"
    if attributes_yml.exists():
        return attributes_yml
    schema_json = ver_dir / "schema.json"
    if schema_json.exists():
        return schema_json
    raise FileNotFoundError(f"No attributes.yaml/.yml or schema.json in {ver_dir}")


def run_generator(script: Path, input_file: Path, output_file: Path) -> None:
    cmd = [
        sys.executable,
        str(script),
        "--input",
        str(input_file),
        "--output",
        str(output_file),
    ]
    subprocess.run(cmd, check=True)


def main() -> int:
    args = parse_args()
    schema_root = Path(args.schema_root).resolve()
    if not schema_root.exists() or not schema_root.is_dir():
        raise SystemExit(f"schema root not found: {schema_root}")
    if not GEN_CONTEXT.exists() or not GEN_VOCAB.exists():
        raise SystemExit("generator scripts are missing under tools/")

    fixed: List[Tuple[Path, str]] = []
    skipped: List[Path] = []

    for ver_dir in version_dirs(schema_root):
        try:
            input_file = pick_input_file(ver_dir)
        except FileNotFoundError:
            skipped.append(ver_dir)
            continue

        context_path = ver_dir / "context.jsonld"
        vocab_path = ver_dir / "vocab.jsonld"

        needs_context = args.overwrite or not context_path.exists()
        needs_vocab = args.overwrite or not vocab_path.exists()

        if not needs_context and not needs_vocab:
            continue

        if needs_context:
            run_generator(GEN_CONTEXT, input_file, context_path)
            fixed.append((ver_dir, "context.jsonld"))
        if needs_vocab:
            run_generator(GEN_VOCAB, input_file, vocab_path)
            fixed.append((ver_dir, "vocab.jsonld"))

    print(f"schema_root={schema_root}")
    print(f"generated_count={len(fixed)}")
    print(f"skipped_count={len(skipped)}")
    for ver_dir, file_name in fixed:
        print(f"generated {ver_dir / file_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
