# Offer — v2.1

A generalized, cross-domain Offer that captures the terms under which one or more Resources may be committed.  Core intent: - Support multiple terms/eligibility/constraints/price points for the same Resource(s) - Support dynamic / on-the-fly offers (e.g., bundling, combinational discounts,  eligibility changes, capacity-aware pricing)  This mirrors the role of Offer in current Beckn (and schema.org patterns), but keeps the shape minimal and composable via `beckn:offerAttributes`.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Offer/attributes.yaml](https://schema.beckn.io/Offer/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Offer/v2.1/attributes.yaml](https://schema.beckn.io/Offer/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Offer/attributes.jsonschema.yaml](https://schema.beckn.io/Offer/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Offer/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Offer/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Offer/context.jsonld](https://schema.beckn.io/Offer/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Offer/v2.1/context.jsonld](https://schema.beckn.io/Offer/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Offer/vocab.jsonld](https://schema.beckn.io/Offer/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Offer/v2.1/vocab.jsonld](https://schema.beckn.io/Offer/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Unique identifier of the offer. |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | Human / agent-readable description of this offer. |
| `provider` | no | $ref: https://schema.beckn.io/Provider/v2.1/attributes.yaml#/components/schemas/Provider | - |
| `resourceIds` | no | array | References (IDs) to resources covered by this offer. |
| `addOns` | no | array | IDs of optional extra Offers or Resources that can be attached. |
| `considerationIds` | no | array | - |
| `fulfillmentIds` | no | $ref: https://schema.beckn.io/Consideration/v2.0/attributes.yaml#/components/schemas/Consideration | Details regarding the fulfillment of this offer |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.1/attributes.yaml#/components/schemas/TimePeriod | - |
| `availableTo` | no | array | Optional visibility constraint indicating which network participants (by participantId / networkId / role) are allowed to discover or transact on this entity.  If omitted, the entity is assumed to be visible to all participants in the addressed network(s). |
| `offerAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | - |
