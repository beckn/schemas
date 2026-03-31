# Package — v2.0

A Package is a physical unit of goods prepared for transport within a shipment. Maps to beckn:Item.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Package/attributes.yaml](https://schema.beckn.io/Package/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Package/v2.0/attributes.yaml](https://schema.beckn.io/Package/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Package/attributes.jsonschema.yaml](https://schema.beckn.io/Package/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Package/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Package/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Package/context.jsonld](https://schema.beckn.io/Package/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Package/v2.0/context.jsonld](https://schema.beckn.io/Package/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Package/vocab.jsonld](https://schema.beckn.io/Package/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Package/v2.0/vocab.jsonld](https://schema.beckn.io/Package/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Unique identifier for the package |
| `description` | no | string | Description of package contents |
| `weight` | yes | object | Weight of the package |
| `dimensions` | no | object | Physical dimensions of the package |
| `volumetricWeight` | no | number | Calculated volumetric weight in kg |
| `fragile` | no | boolean | Whether the package requires fragile handling |
| `hazardous` | no | boolean | Whether the package contains hazardous materials |
| `declaredValue` | no | object | Declared monetary value of contents |
| `packageType` | no | string | Type of packaging |
| `barcode` | no | string | Package-level barcode or QR code |
| `temperatureControl` | no | object | Temperature control requirements for cold chain |
| `insuranceRequired` | no | boolean | Whether insurance is required for this package |
