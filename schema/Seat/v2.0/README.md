# Seat — v2.0

A specific seat position reserved or assigned to a passenger on a flight, train, or other transport service.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Seat/attributes.yaml](https://schema.beckn.io/Seat/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Seat/v2.0/attributes.yaml](https://schema.beckn.io/Seat/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Seat/attributes.jsonschema.yaml](https://schema.beckn.io/Seat/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Seat/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Seat/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Seat/context.jsonld](https://schema.beckn.io/Seat/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Seat/v2.0/context.jsonld](https://schema.beckn.io/Seat/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Seat/vocab.jsonld](https://schema.beckn.io/Seat/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Seat/v2.0/vocab.jsonld](https://schema.beckn.io/Seat/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `seatId` | no | string | Unique identifier or label for the seat |
| `row` | no | string | Row designation (number or letter) |
| `column` | no | string | Column or seat letter within the row |
| `seatType` | no | string | Type of seat (e.g. WINDOW, AISLE, MIDDLE, UPPER_BERTH) |
| `seatCharacteristics` | no | string | Additional characteristics (e.g. EXTRA_LEGROOM, QUIET_ZONE, ACCESSIBLE) |
| `deckLevel` | no | string | Deck or level (UPPER, LOWER, MAIN) |
| `id` | no | string | Unique identifier for the entitlement |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable information about the entitlement |
| `resource` | no | $ref: https://schema.beckn.io/ContractItem/v2.0/attributes.yaml#/components/schemas/ContractItem | The resource being accessed against this entitlement |
| `credentials` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Credential descriptors for the entitlement |
