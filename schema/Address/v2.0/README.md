# Address — v2.0

Physical or postal address.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Address](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Address` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `addressCountry` | string | Country name or ISO-3166-1 alpha-2 code. |
| `addressLocality` | string | City/locality. |
| `addressRegion` | string | State/region/province. |
| `extendedAddress` | string | Address extension (apt/suite/floor, C/O). |
| `postalCode` | string | Postal/ZIP code. |
| `streetAddress` | string | Street address (building name/number and street). |
