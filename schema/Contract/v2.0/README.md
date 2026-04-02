# Contract — v2.0

This is a JSON-LD compliant, linked-data schema that specifies a generic multi-party, digitally signed Contract between a set of participants. based on the vocabulary defined in the @context. By default, it is the most generic form of contract i.e beckn:Contract. However, based on the mapping being used in @context, it could take values like retail:Order, mobility:Reservation, healthcare:Appointment, and so on, which will be defined as sub-classes of beckn:Contract. Alternate description A digitally agreed commitment between two or more participants governing the exchange of economic or non-economic value.  Contract is the canonical contract object in the generalized Beckn v2.1 protocol. It replaces the commerce-specific Order construct as the canonical transaction object at the API layer.  A Contract binds:  - Commitments (what is agreed)  - Consideration (value promised)  - Performance (how execution occurs)  - Settlements (how consideration is discharged)  The model is domain-neutral and supports commerce, hiring, energy markets, carbon exchanges, data access, mobility, subscriptions, and other use cases.

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
| `id` | no | string | A UUID string generated at the BPP endpoint at any stage before the confirmation of the order i.e before `/on_confirm` callback. This value is intended typically for indexing or filtering. While the chances of a UUID collision are rare, it is recommended to use a combination of `bppId`, `providerId` and `id` to allow for global uniqueness. |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | Describes the nature of the contract in human / agent readable terms |
| `commitments` | yes | array | Structured commitments governed by this contract. |
| `consideration` | no | array | Value agreed to be exchanged under this contract. |
| `participants` | no | array | The participants involved in the contract. Contracts are not always between two individuals.  Several entities may play a specific role in the creation, fulfillment, and post-fulfillment of the contract. |
| `performance` | no | array | Execution units of the contract.  Performance is the generalized fulfillment abstraction. Each Performance instance represents a structured execution plan or delivery mechanism, including:   - Physical delivery  - Service provisioning  - API access  - Subscription activation  - Carbon credit transfer  - Capacity allocation  - Workforce onboarding Tracking and Support interactions may be linked to individual Performance units. |
| `settlements` | no | array | Records representing discharge of agreed consideration. |
| `status` | no | allOf | The current state of the contract expressed as a Descriptor whose code MUST be one of the standard contract state values. |
| `contractAttributes` | no | allOf | Domain-specific extension attributes for this contract. |
