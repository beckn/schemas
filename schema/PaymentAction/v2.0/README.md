# PaymentAction — v2.0

A payment action record.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [PaymentAction](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `PaymentAction` |

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
| `amount` | object | Amount associated with this payment action |
| `paymentStatus` | string | Payment lifecycle status (Pending \| Authorized \| Captured \| Failed \| Refunded \| PartialRefund …) |
| `paymentMethod` | object |  |
| `paymentUrl` | string | URL for payment processing/redirection |
| `state` | [State](../../State/README.md) |  |
| `txnRef` | string | PSP/gateway/bank transaction reference |
| `checkoutAt` | [CheckoutTerminal](../../CheckoutTerminal/README.md) |  |
| `paidAt` | string | The time at which the payment was made |
| `paymentActionAttributes` | [Attributes](../../Attributes/README.md) | Extensible set of attributes containing payment actions specific to each ecosystem. |
