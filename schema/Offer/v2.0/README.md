# Offer — v2.0

Schema definition for Offer in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Offer/attributes.yaml](https://schema.beckn.io/Offer/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Offer/v2.0/attributes.yaml](https://schema.beckn.io/Offer/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Offer/attributes.jsonschema.yaml](https://schema.beckn.io/Offer/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Offer/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Offer/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Offer/context.jsonld](https://schema.beckn.io/Offer/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Offer/v2.0/context.jsonld](https://schema.beckn.io/Offer/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Offer/vocab.jsonld](https://schema.beckn.io/Offer/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Offer/v2.0/vocab.jsonld](https://schema.beckn.io/Offer/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `beckn:id` | yes | string | Unique id for this offer |
| `beckn:descriptor` | yes | $ref: https://schema.beckn.io/Descriptor/attributes.yaml#/components/schemas/Descriptor | - |
| `beckn:provider` | yes | $ref: https://schema.beckn.io/Provider/attributes.yaml#/components/schemas/Provider | Seller / provider of this offer |
| `beckn:items` | yes | array | Base item(s) the offer applies to (single or bundle) |
| `beckn:addOns` | no | array | Optional extra Offers that can be attached (e.g., warranty, gift wrap) |
| `beckn:addOnItems` | no | array | Optional extras modeled as items (e.g., toppings, accessories) |
| `beckn:isActive` | no | boolean | Whether the offer is active |
| `beckn:validity` | no | $ref: https://schema.beckn.io/TimePeriod/attributes.yaml#/components/schemas/TimePeriod | Offer validity window |
| `beckn:price` | no | $ref: https://schema.beckn.io/PriceSpecification/attributes.yaml#/components/schemas/PriceSpecification | Price snapshot; detailed models can live in offerAttributes |
| `beckn:eligibleRegion` | no | array | Regions where the offer is eligible |
| `beckn:acceptedPaymentMethod` | no | $ref: https://schema.beckn.io/AcceptedPaymentMethod/attributes.yaml#/components/schemas/AcceptedPaymentMethod | - |
| `beckn:offerAttributes` | no | $ref: https://schema.beckn.io/Attributes/attributes.yaml#/components/schemas/Attributes | Attribute Pack attachment (pricing models, discounts, rail terms, etc.) |
