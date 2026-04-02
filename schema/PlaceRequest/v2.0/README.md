# PlaceRequest — v2.0

A request for a specific accommodation or seat assignment within a transport service during the booking process.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PlaceRequest/attributes.yaml](https://schema.beckn.io/PlaceRequest/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/PlaceRequest/v2.0/attributes.yaml](https://schema.beckn.io/PlaceRequest/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PlaceRequest/attributes.jsonschema.yaml](https://schema.beckn.io/PlaceRequest/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/PlaceRequest/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/PlaceRequest/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PlaceRequest/context.jsonld](https://schema.beckn.io/PlaceRequest/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/PlaceRequest/v2.0/context.jsonld](https://schema.beckn.io/PlaceRequest/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PlaceRequest/vocab.jsonld](https://schema.beckn.io/PlaceRequest/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/PlaceRequest/v2.0/vocab.jsonld](https://schema.beckn.io/PlaceRequest/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `accommodationType` | no | string | Type of accommodation requested (e.g. SEAT, BERTH, COMPARTMENT) |
| `preferences` | no | string | Passenger preferences (e.g. window, aisle, quiet zone) |
| `seatRef` | no | $ref: https://schema.beckn.io/Seat/v2.0/attributes.yaml#/components/schemas/Seat | Specific seat requested, if applicable |
| `id` | no | string | Unique identifier for the contract item |
| `descriptor` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Human-readable description of the item |
| `price` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | Price for this contract item |
| `quantity` | no | $ref: https://schema.beckn.io/Quantity/v2.0/attributes.yaml#/components/schemas/Quantity | Quantity of this contract item |
