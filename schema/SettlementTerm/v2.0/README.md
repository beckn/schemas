# SettlementTerm — v2.0

A term within a settlement schedule.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [SettlementTerm](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `SettlementTerm` |

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
| `amount` | object | Amount associated with this settlement action |
| `paymentTrigger` | [PaymentTrigger](../../PaymentTrigger/README.md) | Describes the event which triggers the payment against this settlement term |
| `settlementStatus` | string |  |
| `settlementSchedule` | [SettlementSchedule](../../SettlementSchedule/README.md) |  |
| `payTo` |  | Describes the details of the account where the money must be remited. It could be a bank account, a payment gateway, or a virtual payment address (like a UPI ID) |
| `acceptedPaymentMethods` | string[] | Describes the methods or mechanisms accepted by the payee (described in the payTo property) for the purpose of this settlement. |
| `settlementTermAttributes` | [Attributes](../../Attributes/README.md) | Additional use case specific settlement terms that must be adhered to |
