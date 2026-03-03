#!/usr/bin/env python3
"""
Convert attributes.yaml files from OpenAPI 3.1.1 format to JSON Schema 2020-12 format.

Before:
  openapi: 3.1.1
  info: ...
  components:
    schemas:
      SchemaName:
        description: ...
        type: object
        properties: ...

After:
  $id: "https://schema.beckn.io/SchemaName/v2.0"
  $schema: "https://json-schema.org/draft/2020-12/schema"
  description: ...
  title: SchemaName
  type: object
  properties: ...
"""

import os
import sys
import glob

import yaml


# Custom representer to preserve key order and handle special keys like $id
class OrderedDumper(yaml.Dumper):
    pass


def _represent_str(dumper, data):
    # Use double-quoted style for $id and $schema values that are URIs
    if data.startswith('http') or data.startswith('https://json-schema'):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


OrderedDumper.add_representer(str, _represent_str)


def convert_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    try:
        doc = yaml.safe_load(content)
    except yaml.YAMLError as e:
        print(f"  ERROR parsing YAML: {e}")
        return False

    if doc is None:
        print(f"  SKIP: empty file")
        return False

    # Check if already in JSON Schema format (has $id or $schema at top)
    if '$id' in doc or '$schema' in doc:
        print(f"  SKIP: already in JSON Schema format")
        return False

    # Check if it's in OpenAPI format
    if 'openapi' not in doc and 'components' not in doc:
        print(f"  SKIP: not in OpenAPI format (unknown format)")
        return False

    # Extract schema name and content from components.schemas
    components = doc.get('components', {})
    schemas = components.get('schemas', {})

    if not schemas:
        print(f"  ERROR: no schemas found in components.schemas")
        return False

    if len(schemas) != 1:
        print(f"  WARNING: multiple schemas found: {list(schemas.keys())}, using first")

    schema_name = list(schemas.keys())[0]
    schema_body = schemas[schema_name]

    if schema_body is None:
        schema_body = {}

    # Build the new top-level document with $id and $schema first
    new_doc = {}
    new_doc['$id'] = f"https://schema.beckn.io/{schema_name}/v2.0"
    new_doc['$schema'] = "https://json-schema.org/draft/2020-12/schema"

    # Add description from schema body if present, else from info
    if 'description' in schema_body:
        new_doc['description'] = schema_body.pop('description')
    elif doc.get('info', {}).get('description'):
        new_doc['description'] = doc['info']['description']

    # Add title - use schema name, overriding any existing title
    new_doc['title'] = schema_name

    # Add all remaining fields from schema body (type, properties, required, etc.)
    # Skip 'title' from schema body since we already set it
    for key, value in schema_body.items():
        if key != 'title':
            new_doc[key] = value

    # Serialize to YAML
    yaml_str = yaml.dump(
        new_doc,
        Dumper=OrderedDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2,
        width=120,
    )

    with open(filepath, 'w') as f:
        f.write(yaml_str)

    print(f"  OK: converted {schema_name}")
    return True


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pattern = os.path.join(base_dir, 'schema', '*', 'v2.0', 'attributes.yaml')
    files = sorted(glob.glob(pattern))

    # Exclude RequestAction and CallbackAction (already converted)
    exclude = {'RequestAction', 'CallbackAction'}
    files = [f for f in files if os.path.basename(os.path.dirname(os.path.dirname(f))) not in exclude]

    print(f"Found {len(files)} files to convert\n")

    converted = 0
    skipped = 0
    errors = 0

    for filepath in files:
        schema_dir = os.path.basename(os.path.dirname(os.path.dirname(filepath)))
        print(f"Processing: {schema_dir}")
        try:
            result = convert_file(filepath)
            if result:
                converted += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1

    print(f"\nDone: {converted} converted, {skipped} skipped, {errors} errors")


if __name__ == '__main__':
    main()
