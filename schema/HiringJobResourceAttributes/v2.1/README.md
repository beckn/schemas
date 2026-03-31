# HiringJobResourceAttributes — v2.1

Intrinsic attributes of a job opportunity Resource. Domain-generic: applicable to any hiring vertical (tech, construction, logistics, healthcare, gig economy, etc.).

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/HiringJobResourceAttributes/attributes.yaml](https://schema.beckn.io/HiringJobResourceAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/v2.1/attributes.yaml](https://schema.beckn.io/HiringJobResourceAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/HiringJobResourceAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/HiringJobResourceAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/context.jsonld](https://schema.beckn.io/HiringJobResourceAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/v2.1/context.jsonld](https://schema.beckn.io/HiringJobResourceAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/vocab.jsonld](https://schema.beckn.io/HiringJobResourceAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/HiringJobResourceAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/HiringJobResourceAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `job_type` | no | string | Nature of the employment engagement. |
| `work_mode` | no | string | Physical arrangement for the role. |
| `industry_type` | no | $ref: ../../../CodedValue/attributes.jsonschema.yaml#/components/schemas/CodedValue | Industry classification using an authority-governed code system (e.g. ISIC, NIC). Provides international neutrality.  |
| `location` | no | object | Primary location of the role. |
| `service_area` | no | string | Free-text description of the geographic service area for roles not tied to a single location (e.g. field sales, delivery routes).  |
| `requirements` | no | array | Ordered list of credential requirements an applicant must satisfy. Mandatory requirements block the application; non-mandatory are advisory.  |
| `tags` | no | array | Free-text tags for discovery and search indexing. |
