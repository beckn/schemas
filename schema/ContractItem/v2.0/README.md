# ContractItem — v2.0

A line item within a Contract, linking an accepted Offer and ordered Item with quantity and price.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ContractItem/attributes.yaml](https://schema.beckn.io/ContractItem/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ContractItem/v2.0/attributes.yaml](https://schema.beckn.io/ContractItem/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ContractItem/attributes.jsonschema.yaml](https://schema.beckn.io/ContractItem/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ContractItem/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ContractItem/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ContractItem/context.jsonld](https://schema.beckn.io/ContractItem/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ContractItem/v2.0/context.jsonld](https://schema.beckn.io/ContractItem/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ContractItem/vocab.jsonld](https://schema.beckn.io/ContractItem/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ContractItem/v2.0/vocab.jsonld](https://schema.beckn.io/ContractItem/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `acceptedOffer` | no | $ref: https://schema.beckn.io/Offer/v2.1/attributes.yaml#/components/schemas/Offer | Offer applied to this line (if different from contract-level) |
| `itemId` | yes | $ref: https://schema.beckn.io/Item/v2.1/attributes.yaml#/components/schemas/Item | - |
| `lineId` | no | string | Unique line id within contract |
| `contractItemAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Line-level Attribute Pack (options, substitutions, ESG, etc.) |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Line price composition (unit/tax/delivery/discount) |
| `quantity` | no | $ref: https://schema.beckn.io/Quantity/v2.0/attributes.yaml#/components/schemas/Quantity | - |
