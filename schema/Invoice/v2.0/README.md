# Invoice — v2.0

Schema definition for Invoice in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Invoice/attributes.yaml](https://schema.beckn.io/Invoice/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Invoice/v2.0/attributes.yaml](https://schema.beckn.io/Invoice/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Invoice/attributes.jsonschema.yaml](https://schema.beckn.io/Invoice/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Invoice/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Invoice/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Invoice/context.jsonld](https://schema.beckn.io/Invoice/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Invoice/v2.0/context.jsonld](https://schema.beckn.io/Invoice/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Invoice/vocab.jsonld](https://schema.beckn.io/Invoice/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Invoice/v2.0/vocab.jsonld](https://schema.beckn.io/Invoice/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `beckn:id` | yes | string | Stable invoice identifier (system id) |
| `beckn:number` | yes | string | Human-visible invoice number |
| `beckn:issueDate` | yes | string | - |
| `beckn:dueDate` | no | string | - |
| `beckn:payee` | yes | $ref: https://schema.beckn.io/Provider/v2.1/attributes.yaml#/components/schemas/Provider | Seller / issuer of the invoice |
| `beckn:payer` | yes | $ref: https://schema.beckn.io/Buyer/v2.0/attributes.yaml#/components/schemas/Buyer | Buyer being invoiced |
| `beckn:totals` | yes | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Invoice grand totals (tax/shipping/discount components inside) |
| `beckn:invoiceAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Attribute Pack for tax regime (e.g., GST/VAT), e-invoice refs, legal boilerplate, etc. |
