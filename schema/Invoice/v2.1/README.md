# Invoice — v2.1

Schema definition for Invoice in the Beckn Protocol v2.0.1

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Invoice/attributes.yaml](https://schema.beckn.io/Invoice/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Invoice/v2.1/attributes.yaml](https://schema.beckn.io/Invoice/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Invoice/attributes.jsonschema.yaml](https://schema.beckn.io/Invoice/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Invoice/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Invoice/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Invoice/context.jsonld](https://schema.beckn.io/Invoice/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Invoice/v2.1/context.jsonld](https://schema.beckn.io/Invoice/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Invoice/vocab.jsonld](https://schema.beckn.io/Invoice/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Invoice/v2.1/vocab.jsonld](https://schema.beckn.io/Invoice/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | CPD |
| `@type` | yes | string | TPD |
| `dueDate` | no | ['string', 'null'] | - |
| `id` | yes | string | Stable invoice identifier (system id) |
| `invoiceAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Attribute Pack for tax regime (e.g., GST/VAT), e-invoice refs, legal boilerplate, etc. |
| `issueDate` | yes | string | - |
| `number` | yes | string | Human-visible invoice number |
| `payee` | yes | $ref: https://schema.beckn.io/Provider/v2.1/attributes.yaml#/components/schemas/Provider | Seller / issuer of the invoice |
| `payer` | yes | $ref: https://schema.beckn.io/Consumer/v2.0/attributes.yaml#/components/schemas/Consumer | consumer being invoiced |
| `costBreakup` | no | array | - |
