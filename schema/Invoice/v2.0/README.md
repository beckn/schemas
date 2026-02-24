# Invoice — v2.0

An invoice issued for a transaction.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Invoice](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Invoice` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | CPD |
| `@type` | string | TPD |
| `dueDate` | string |  |
| `id` | string | Stable invoice identifier (system id) |
| `invoiceAttributes` | [Attributes](../../Attributes/README.md) | Attribute Pack for tax regime (e.g., GST/VAT), e-invoice refs, legal boilerplate, etc. |
| `issueDate` | string |  |
| `number` | string | Human-visible invoice number |
| `payee` | [Provider](../../Provider/README.md) | Seller / issuer of the invoice |
| `payer` | [Consumer](../../Consumer/README.md) | consumer being invoiced |
| `costBreakup` | [PriceSpecification](../../PriceSpecification/README.md)[] |  |
