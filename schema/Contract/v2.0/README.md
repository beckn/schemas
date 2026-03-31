# Contract — v2.0

This is a JSON-LD compliant, linked-data schema that specifies a generic multi-party, digitally signed Contract between a set of participants. based on the vocabulary defined in the @context. By default, it is the most generic form of contract i.e beckn:Contract. However, based on the mapping being used in @context, it could take values like retail:Order, mobility:Reservation, healthcare:Appointment, and so on, which will be defined as sub-classes of beckn:Contract.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Contract/attributes.yaml](https://schema.beckn.io/Contract/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Contract/v2.0/attributes.yaml](https://schema.beckn.io/Contract/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Contract/attributes.jsonschema.yaml](https://schema.beckn.io/Contract/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Contract/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Contract/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Contract/context.jsonld](https://schema.beckn.io/Contract/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Contract/v2.0/context.jsonld](https://schema.beckn.io/Contract/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Contract/vocab.jsonld](https://schema.beckn.io/Contract/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Contract/v2.0/vocab.jsonld](https://schema.beckn.io/Contract/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | no | string | A URL to the reference vocabulary where this schema has been defined. If missing, this field defaults to `https://schema.beckn.io/`. It allows applications to fetch the mapping between the simple JSON keys of this class and absolute Beckn IRIs (Internationalized Resource Identifiers), allowing conversion of standard Beckn JSON payload into linked data. |
| `@type` | yes | string | A Beckn IRI on the vocabulary defined in the @context. Must start with "beckn:" followed by URL-safe identifier characters. |
| `id` | no | string | A UUID string generated at the BPP endpoint at any stage before the confirmation of the order i.e before `/on_confirm` callback. This value is intended typically for indexing or filtering. While the chances of a UUID collision are rare, it is recommended to use a combination of `bppId`, `providerId` and `id` to allow for global uniqueness. |
| `displayId` | no | string | A human-readable / Agent-readable identifier of the contract intended for display or printing. This value may or may not be different from `id` which is intended purely for machine-readability. Typically, this value is generated after the confirmation of the order at the BPP's end. |
| `items` | yes | array | The items of value i.e resources, specified in this contract. Depending upon the context, these resources could be a combination physical objects, virtual objects, services, time slots, distance travelled, alloted space, and many more. |
| `status` | no | any | The current state of the contract. Depending on the context, it could be just a code or a detailed description of state. |
| `contractValue` | no | any | An object that captures the total value of the contract including a breakup of the items, discounts, fulfillment charges, and any other additional charges relevant to that context. |
| `participants` | yes | array | The participants involved in the contract. Contracts are not always between two individuals. Several entities may play a specific role in the creation, fulfillment, and post-fulfillment of the contract. |
| `entitlements` | no | array | - |
| `fulfillments` | no | array | Describes the acts performed by each participant to fulfill the contract |
