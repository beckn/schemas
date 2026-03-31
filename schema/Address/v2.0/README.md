# Address — v2.0

**Postal address** aligned with schema.org `PostalAddress`. Use for human-readable addresses. Geometry lives in `Location.geo` as GeoJSON.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Address/attributes.yaml](https://schema.beckn.io/Address/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Address/v2.0/attributes.yaml](https://schema.beckn.io/Address/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Address/attributes.jsonschema.yaml](https://schema.beckn.io/Address/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Address/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Address/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Address/context.jsonld](https://schema.beckn.io/Address/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Address/v2.0/context.jsonld](https://schema.beckn.io/Address/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Address/vocab.jsonld](https://schema.beckn.io/Address/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Address/v2.0/vocab.jsonld](https://schema.beckn.io/Address/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `addressCountry` | no | string | Country name or ISO-3166-1 alpha-2 code. |
| `addressLocality` | no | string | City/locality. |
| `addressRegion` | no | string | State/region/province. |
| `extendedAddress` | no | string | Address extension (apt/suite/floor, C/O). |
| `postalCode` | no | string | Postal/ZIP code. |
| `streetAddress` | no | string | Street address (building name/number and street). |
