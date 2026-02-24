# Contract — v2.0

A formalised agreement between consumer and provider.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Contract](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Contract` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | A URL to the reference vocabulary where this schema has been defined. If missing, this field defaults to `https://schema.beckn.io/`. It allows applications to fetch the mapping between the simple JSON keys of this class and absolute Beckn IRIs (Internationalized Resource Identifiers), allowing conversion of standard Beckn JSON payload into linked data. |
| `@type` | string | A Beckn IRI on the vocabulary defined in the @context. Must start with "beckn:" followed by URL-safe identifier characters. |
| `id` | string | A UUID string generated at the BPP endpoint at any stage before the confirmation of the order i.e before `/on_confirm` callback. This value is intended typically for indexing or filtering. While the chances of a UUID collision are rare, it is recommended to use a combination of `bppId`, `providerId` and `id` to allow for global uniqueness. |
| `displayId` | string | A human-readable / Agent-readable identifier of the contract intended for display or printing. This value may or may not be different from `id` which is intended purely for machine-readability. Typically, this value is generated after the confirmation of the order at the BPP's end. |
| `items` | [ContractItem](../../ContractItem/README.md)[] | The items of value i.e resources, specified in this contract. Depending upon the context, these resources could be a combination physical objects, virtual objects, services, time slots, distance travelled, alloted space, and many more. |
| `status` |  | The current state of the contract. Depending on the context, it could be just a code or a detailed description of state. |
| `contractValue` |  | An object that captures the total value of the contract including a breakup of the items, discounts, fulfillment charges, and any other additional charges relevant to that context. |
| `participants` | [Participant](../../Participant/README.md)[] | The participants involved in the contract. Contracts are not always between two individuals. Several entities may play a specific role in the creation, fulfillment, and post-fulfillment of the contract. |
| `entitlements` | [Entitlement](../../Entitlement/README.md)[] |  |
| `fulfillments` | [Fulfillment](../../Fulfillment/README.md)[] | Describes the acts performed by each participant to fulfill the contract |
