# Itinerary — v2.0

A complete planned trip containing an ordered sequence of legs, including transfer points, durations, and timing.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Itinerary/attributes.yaml](https://schema.beckn.io/Itinerary/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Itinerary/v2.0/attributes.yaml](https://schema.beckn.io/Itinerary/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Itinerary/attributes.jsonschema.yaml](https://schema.beckn.io/Itinerary/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Itinerary/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Itinerary/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Itinerary/context.jsonld](https://schema.beckn.io/Itinerary/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Itinerary/v2.0/context.jsonld](https://schema.beckn.io/Itinerary/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Itinerary/vocab.jsonld](https://schema.beckn.io/Itinerary/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Itinerary/v2.0/vocab.jsonld](https://schema.beckn.io/Itinerary/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `legs` | no | $ref: https://schema.beckn.io/Leg/v2.0/attributes.yaml#/components/schemas/Leg | Ordered list of legs making up this itinerary |
| `totalDuration` | no | string | Total travel duration for the itinerary |
| `totalDistance` | no | number | Total distance in metres for the itinerary |
| `transferCount` | no | number | Number of transfers in the itinerary |
| `departureTime` | no | string | Departure time of the first leg |
| `arrivalTime` | no | string | Arrival time of the last leg |
| `id` | no | string | Unique identifier for the contract |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the contract |
| `items` | no | $ref: https://schema.beckn.io/ContractItem/v2.0/attributes.yaml#/components/schemas/ContractItem | Line items within the contract |
| `fulfillments` | no | $ref: https://schema.beckn.io/Fulfillment/v2.1/attributes.yaml#/components/schemas/Fulfillment | Fulfillments associated with this contract |
| `state` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current state of the contract |
