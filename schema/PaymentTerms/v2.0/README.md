# PaymentTerms — v2.0

Terms governing payment.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [PaymentTerms](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `PaymentTerms` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string |  |
| `@type` | string |  |
| `collectedBy` | string | Describes the entity that first collects the payment from the consumer. This is the actor who is responsible to initiate the settlement process as per the terms described in the settlementTerms property. |
| `checkoutAt` | [CheckoutTerminal](../../CheckoutTerminal/README.md) |  |
| `settlementTerms` | [SettlementTerm](../../SettlementTerm/README.md)[] |  |
| `checkoutTrigger` | [PaymentTrigger](../../PaymentTrigger/README.md) | The stage in the order lifecycle when the checkout should be triggered |
| `paymentTermsAttributes` | [Attributes](../../Attributes/README.md) | Rail-specific attribute pack (e.g., UPI: VPA/UTR; CARD: token/3DS; BNPL: plan/schedule) |
