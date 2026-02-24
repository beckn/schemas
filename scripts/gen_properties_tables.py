#!/usr/bin/env python3
"""
Generate ## Properties table in each schema/*/v2.0/README.md from attributes.yaml.

Usage:
    python3 scripts/gen_properties_tables.py
"""

import glob
import os
import re
import sys

import yaml

# All 91 known schemas — used to determine if a $ref target gets a hyperlink
KNOWN_SCHEMAS = {
    'AcceptedPaymentMethod', 'Address', 'Alert', 'Attributes', 'CancelAction',
    'CancellationOutcome', 'CancellationPolicy', 'CancellationReason', 'Catalog',
    'CatalogProcessingResult', 'CategoryCode', 'CheckoutTerminal', 'ConfirmAction',
    'Constraint', 'Consumer', 'Context', 'Contract', 'ContractItem', 'Credential',
    'Descriptor', 'DiscoverAction', 'DisplayedRating', 'Document', 'Eligibility',
    'Entitlement', 'Error', 'ErrorResponse', 'Feedback', 'Form', 'Fulfillment',
    'FulfillmentAgent', 'FulfillmentMode', 'FulfillmentStage', 'FulfillmentStageAuthorization',
    'FulfillmentStageEndpoint', 'GeoJSONGeometry', 'InitAction', 'Instruction', 'Intent',
    'Invoice', 'Item', 'Location', 'MediaFile', 'MediaInput', 'MediaSearch',
    'MediaSearchOptions', 'Offer', 'OnCancelAction', 'OnConfirmAction', 'OnDiscoverAction',
    'OnInitAction', 'OnRateAction', 'OnSelectAction', 'OnStatusAction', 'OnSupportAction',
    'OnTrackAction', 'OnUpdateAction', 'Organization', 'Participant', 'PaymentAction',
    'PaymentTerms', 'PaymentTrigger', 'Person', 'Policy', 'PriceSpecification',
    'ProcessingNotice', 'Provider', 'Quantity', 'RateAction', 'Rating', 'RatingForm',
    'RatingInput', 'RefundTerms', 'SelectAction', 'SettlementSchedule', 'SettlementTerm',
    'Skill', 'SpatialConstraint', 'State', 'StatusAction', 'SupportAction', 'SupportInfo',
    'SupportRequest', 'SupportTicket', 'Time', 'TimePeriod', 'TrackAction', 'Tracking',
    'TrackingRequest', 'TransactionEndpoint', 'UpdateAction',
}


def extract_schema_name_from_ref(ref_str):
    """Extract schema name from a $ref string.

    Handles:
      - URL refs:   'https://schema.beckn.io/Alert.yaml'  → 'Alert'
      - Local refs: '#/components/schemas/Alert'           → 'Alert'
    """
    if not ref_str:
        return ''
    if ref_str.startswith('#/'):
        return ref_str.split('/')[-1]
    # URL-style ref
    name = ref_str.split('/')[-1]
    if name.endswith('.yaml'):
        name = name[:-5]
    return name


def schema_link(schema_name):
    """Return a markdown link if schema_name is a known schema, else just the name."""
    if schema_name in KNOWN_SCHEMAS:
        return f'[{schema_name}](../../{schema_name}/README.md)'
    return schema_name


def resolve_ref_from_allof(allof_value):
    """
    Resolve a $ref from an allOf value which may be:
      - a list:  [{'$ref': '...'}, ...]
      - a dict:  {'$ref': '...'}    (non-standard but occurs in some files)
    Returns the schema name string, or None if not found.
    """
    if isinstance(allof_value, list):
        for item in allof_value:
            if isinstance(item, dict) and '$ref' in item:
                return extract_schema_name_from_ref(item['$ref'])
    elif isinstance(allof_value, dict) and '$ref' in allof_value:
        return extract_schema_name_from_ref(allof_value['$ref'])
    return None


def get_type_str(prop_def):
    """
    Given a property definition dict, return the markdown type string.

    Priority:
      1. Direct $ref                    → SchemaName (linked if known)
      2. allOf with $ref                → SchemaName (linked if known)
      3. type: array + items.$ref       → SchemaName[] (linked if known)
      4. type: array + items.type       → primitiveType[]
      5. type: array (no items info)    → array
      6. Other type                     → the type string
      7. Fallback                       → '' (empty)
    """
    if not isinstance(prop_def, dict):
        return ''

    # 1. Direct $ref
    if '$ref' in prop_def:
        sname = extract_schema_name_from_ref(prop_def['$ref'])
        return schema_link(sname)

    # 2. allOf with $ref
    if 'allOf' in prop_def:
        sname = resolve_ref_from_allof(prop_def['allOf'])
        if sname:
            return schema_link(sname)
        return 'object'

    # 3–5. type: array
    if prop_def.get('type') == 'array':
        items = prop_def.get('items', {})
        if isinstance(items, dict):
            if '$ref' in items:
                sname = extract_schema_name_from_ref(items['$ref'])
                return f'{schema_link(sname)}[]'
            item_type = items.get('type', '')
            if item_type:
                return f'{item_type}[]'
        return 'array'

    # 6. Any other type
    if 'type' in prop_def:
        return str(prop_def['type'])

    return ''


def clean_description(desc):
    """Sanitise a description string for use inside a Markdown table cell."""
    if not desc:
        return ''
    # Convert to str (some YAML values may be multiline strings)
    text = str(desc)
    # Collapse newlines to a space
    text = text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
    # Escape pipe characters (would break the table)
    text = text.replace('|', '\\|')
    # Collapse runs of spaces
    text = re.sub(r'  +', ' ', text)
    return text.strip()


def build_properties_section(yaml_path, schema_name):
    """
    Parse attributes.yaml and return the full ## Properties markdown section
    (including leading newline) as a string.
    """
    with open(yaml_path, 'r', encoding='utf-8') as fh:
        data = yaml.safe_load(fh)

    schemas_node = data.get('components', {}).get('schemas', {})
    schema_def = schemas_node.get(schema_name, {})

    properties = schema_def.get('properties')

    # ── Schema has no properties (e.g. allOf-only like TransactionEndpoint) ──
    if not properties:
        if 'allOf' in schema_def:
            sname = resolve_ref_from_allof(schema_def['allOf'])
            if sname:
                link = schema_link(sname)
                return (
                    '\n## Properties\n\n'
                    f'This schema extends {link} and does not define additional '
                    'top-level properties.\n'
                )
        return '\n## Properties\n\nThis schema has no defined top-level properties.\n'

    # ── Build the table ──────────────────────────────────────────────────────
    rows = []
    for prop_name, prop_def in properties.items():
        # Guard: skip list entries (e.g. 'required' list mis-indented into properties)
        if isinstance(prop_def, list):
            continue
        # Guard: handle plain-string values (e.g. property: "description text")
        if isinstance(prop_def, str):
            rows.append(f'| `{prop_name}` | | {clean_description(prop_def)} |')
            continue
        if prop_def is None:
            prop_def = {}
        type_str = get_type_str(prop_def)
        desc = clean_description(prop_def.get('description', ''))
        rows.append(f'| `{prop_name}` | {type_str} | {desc} |')

    header = [
        '\n## Properties\n',
        '| Property | Type | Description |',
        '|----------|------|-------------|',
    ]
    return '\n'.join(header + rows) + '\n'


def update_readme(readme_path, properties_section):
    """
    Append (or replace) the ## Properties section in a README.md file.
    Idempotent: strips any existing ## Properties section first.
    """
    with open(readme_path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # Remove any existing ## Properties section (from previous runs)
    content = re.sub(r'\n## Properties\b.*', '', content, flags=re.DOTALL)
    content = content.rstrip() + '\n'

    new_content = content + properties_section

    with open(readme_path, 'w', encoding='utf-8') as fh:
        fh.write(new_content)


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_glob = os.path.join(repo_root, 'schema', '*', 'v2.0', 'attributes.yaml')
    yaml_files = sorted(glob.glob(schema_glob))

    if not yaml_files:
        print('No attributes.yaml files found. Check the path.', file=sys.stderr)
        sys.exit(1)

    updated = 0
    errors = []

    for yaml_path in yaml_files:
        # Derive schema name from directory structure
        # …/schema/<SchemaName>/v2.0/attributes.yaml
        parts = yaml_path.replace('\\', '/').split('/')
        schema_name = parts[-3]

        readme_path = os.path.join(os.path.dirname(yaml_path), 'README.md')
        if not os.path.exists(readme_path):
            errors.append(f'SKIP (no README.md): {schema_name}')
            continue

        try:
            section = build_properties_section(yaml_path, schema_name)
        except Exception as exc:
            errors.append(f'ERROR parsing {schema_name}: {exc}')
            continue

        try:
            update_readme(readme_path, section)
        except Exception as exc:
            errors.append(f'ERROR writing {schema_name}: {exc}')
            continue

        print(f'  ✓  {schema_name}')
        updated += 1

    print(f'\nDone — updated {updated} / {len(yaml_files)} README files.')

    if errors:
        print('\nIssues:')
        for msg in errors:
            print(f'  {msg}')
        sys.exit(1)


if __name__ == '__main__':
    main()
