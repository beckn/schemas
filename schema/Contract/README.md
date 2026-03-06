# Contract

> **Canonical IRI:** [`https://schema.beckn.io/Contract`](https://schema.beckn.io/Contract)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

This is a JSON-LD compliant, linked-data schema that specifies a generic multi-party, digitally signed Contract between a set of participants. based on the vocabulary defined in the @context. By default, it is the most generic form of contract i.e beckn:Contract. However, based on the mapping being used in @context, it could take values like retail:Order, mobility:Reservation, healthcare:Appointment, and so on, which will be defined as sub-classes of beckn:Contract.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | — | A URL to the reference vocabulary where this schema has been defined. If missing, this field defaults to `https://schema.beckn.io/`. It allows appl… |
| `@type` | `string` | ✅ | A Beckn IRI on the vocabulary defined in the @context. Must start with "beckn:" followed by URL-safe identifier characters. |
| `id` | `string` (uuid) | — | A UUID string generated at the BPP endpoint at any stage before the confirmation of the order i.e before `/on_confirm` callback. This value is inte… |
| `displayId` | `string` | — | A human-readable / Agent-readable identifier of the contract intended for display or printing. This value may or may not be different from `id` whi… |
| `items` | any[] | ✅ | The items of value i.e resources, specified in this contract. Depending upon the context, these resources could be a combination physical objects, … |
| `status` | `string` \| `object` | — | The current state of the contract. Depending on the context, it could be just a code or a detailed description of state. |
| `contractValue` | `object` | — | An object that captures the total value of the contract including a breakup of the items, discounts, fulfillment charges, and any other additional … |
| `participants` | any[] | ✅ | The participants involved in the contract. Contracts are not always between two individuals. Several entities may play a specific role in the creat… |
| `entitlements` | any[] | — | — |
| `fulfillments` | any[] | — | Describes the acts performed by each participant to fulfill the contract |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Contract` |
| JSON Schema (latest) | `https://schema.beckn.io/Contract/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Contract/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Contract/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
