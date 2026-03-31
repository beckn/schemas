# Quantity — v2.0

Schema definition for Quantity in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Quantity/attributes.yaml](https://schema.beckn.io/Quantity/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Quantity/v2.0/attributes.yaml](https://schema.beckn.io/Quantity/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Quantity/attributes.jsonschema.yaml](https://schema.beckn.io/Quantity/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Quantity/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Quantity/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Quantity/context.jsonld](https://schema.beckn.io/Quantity/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Quantity/v2.0/context.jsonld](https://schema.beckn.io/Quantity/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Quantity/vocab.jsonld](https://schema.beckn.io/Quantity/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Quantity/v2.0/vocab.jsonld](https://schema.beckn.io/Quantity/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `maxQuantity` | no | number | Maximum quantity for this price |
| `minQuantity` | no | number | Minimum quantity for this price |
| `unitCode` | no | string | Unit code for the quoted price (e.g., KWH, MIN, H, MON) |
| `unitQuantity` | no | number | Quantity of the unit |
| `unitText` | no | string | Unit for the quoted price (e.g., kWh, minute, hour, month) |
