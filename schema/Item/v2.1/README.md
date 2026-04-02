# Item — v2.1

Schema definition for Item in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Item/attributes.yaml](https://schema.beckn.io/Item/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Item/v2.1/attributes.yaml](https://schema.beckn.io/Item/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Item/attributes.jsonschema.yaml](https://schema.beckn.io/Item/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Item/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Item/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Item/context.jsonld](https://schema.beckn.io/Item/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Item/v2.1/context.jsonld](https://schema.beckn.io/Item/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Item/vocab.jsonld](https://schema.beckn.io/Item/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Item/v2.1/vocab.jsonld](https://schema.beckn.io/Item/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context URI for the core Item schema |
| `@type` | yes | string | Type of the core item |
| `availabilityWindow` | no | array | Time periods when the item is available |
| `availableAt` | no | array | Physical locations where the item is available |
| `category` | no | $ref: https://schema.beckn.io/CategoryCode/v2.1/attributes.yaml#/components/schemas/CategoryCode | - |
| `constraints` | no | array | - |
| `descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | - |
| `id` | yes | string | Unique identifier for the item |
| `isActive` | no | boolean | Whether the item is active |
| `itemAttributes` | yes | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | - |
| `networkId` | no | array | Array of network identifiers for the BAP (Beckn App Provider) that offers this item |
| `policies` | no | array | - |
| `provider` | yes | $ref: https://schema.beckn.io/Provider/v2.1/attributes.yaml#/components/schemas/Provider | - |
| `rateable` | no | boolean | Whether the item can be rated by customers |
| `rating` | no | $ref: https://schema.beckn.io/Rating/v2.1/attributes.yaml#/components/schemas/Rating | - |
