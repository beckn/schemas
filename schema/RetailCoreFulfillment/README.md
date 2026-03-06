# Retail Core Fulfillment

> **Canonical IRI:** [`https://schema.beckn.io/RetailCoreFulfillment`](https://schema.beckn.io/RetailCoreFulfillment)
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Retail-specific fulfillment attributes extending Beckn core Fulfillment. Covers delivery endpoint, operating schedule, SLA semantics and handling constraints.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `supportedFulfillmentTypes` | string[] | — | — |
| `deliveryDetails` | object | — | Delivery endpoint details for DELIVERY fulfillment type. |
| `operatingHours` | [RecurringSchedule](../RecurringSchedule/README.md)[] | — | Recurring store operating schedule. |
| `closures` | [TimePeriod](../TimePeriod/README.md)[] | — | Explicit closure periods overriding operatingHours. |
| `sla` | object | — | Service level agreement for fulfillment. Indicates expected time bounds from defined lifecycle event. |
| `handling` | string[] | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/RetailCoreFulfillment` |
| JSON Schema (latest) | `https://schema.beckn.io/RetailCoreFulfillment/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/RetailCoreFulfillment/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/RetailCoreFulfillment/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |

## Related Schemas

| Schema | Referenced via |
|--------|----------------|
| [`RecurringSchedule`](../RecurringSchedule/README.md) | `operatingHours` |
| [`TimePeriod`](../TimePeriod/README.md) | `closures` |
