# Resource — v2.0

A minimal, domain-neutral abstraction representing any discoverable, referenceable, or committable unit of value, capability, service, entitlement, or asset within the network.  Examples: - A retail product SKU, a mobility ride, a job role, a carbon credit unit,  a dataset/API entitlement, a training course, a clinic service slot.  Designed for composability through `resourceAttributes` where domain packs can plug in their specific fields without changing the core.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Resource/attributes.yaml](https://schema.beckn.io/Resource/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Resource/v2.0/attributes.yaml](https://schema.beckn.io/Resource/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Resource/attributes.jsonschema.yaml](https://schema.beckn.io/Resource/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Resource/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Resource/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Resource/context.jsonld](https://schema.beckn.io/Resource/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Resource/v2.0/context.jsonld](https://schema.beckn.io/Resource/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Resource/vocab.jsonld](https://schema.beckn.io/Resource/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Resource/v2.0/vocab.jsonld](https://schema.beckn.io/Resource/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Globally unique identifier of the resource. |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
| `resourceAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | All the properties of a resource that describe its value, its terms of usage, fulfillment, and consideration |
