# VehicleJourney — v2.0

A specific operational instance of a vehicle traveling a defined route at a scheduled time on a given service day.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VehicleJourney/attributes.yaml](https://schema.beckn.io/VehicleJourney/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VehicleJourney/v2.0/attributes.yaml](https://schema.beckn.io/VehicleJourney/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VehicleJourney/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleJourney/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VehicleJourney/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/VehicleJourney/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VehicleJourney/context.jsonld](https://schema.beckn.io/VehicleJourney/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VehicleJourney/v2.0/context.jsonld](https://schema.beckn.io/VehicleJourney/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VehicleJourney/vocab.jsonld](https://schema.beckn.io/VehicleJourney/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VehicleJourney/v2.0/vocab.jsonld](https://schema.beckn.io/VehicleJourney/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `vehicleJourneyCode` | no | string | Unique code for this vehicle journey |
| `routeRef` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Reference to the route being served |
| `serviceCalendarRef` | no | $ref: https://schema.beckn.io/ServiceCalendar/v2.0/attributes.yaml#/components/schemas/ServiceCalendar | Calendar defining when this journey operates |
| `vehicleRef` | no | $ref: https://schema.beckn.io/Vehicle/v2.0/attributes.yaml#/components/schemas/Vehicle | Vehicle assigned to this journey |
| `patternRef` | no | $ref: https://schema.beckn.io/Pattern/v2.0/attributes.yaml#/components/schemas/Pattern | Journey pattern being followed |
| `stopTimes` | no | $ref: https://schema.beckn.io/StopTime/v2.0/attributes.yaml#/components/schemas/StopTime | Scheduled stop times for each stop on this journey |
| `id` | no | string | Unique identifier for the fulfillment |
| `type` | no | string | Type of fulfillment (extensible term) |
| `agent` | no | $ref: https://schema.beckn.io/FulfillmentAgent/v2.0/attributes.yaml#/components/schemas/FulfillmentAgent | The entity responsible for performing the fulfillment |
| `mode` | no | $ref: https://schema.beckn.io/FulfillmentMode/v2.0/attributes.yaml#/components/schemas/FulfillmentMode | Mode of fulfillment |
| `state` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current state of the fulfillment |
| `participants` | no | $ref: https://schema.beckn.io/Participant/v2.0/attributes.yaml#/components/schemas/Participant | Participants entitled to receive this fulfillment |
| `stages` | no | $ref: https://schema.beckn.io/FulfillmentStage/v2.0/attributes.yaml#/components/schemas/FulfillmentStage | Stages in the fulfillment lifecycle |
| `instructions` | no | $ref: https://schema.beckn.io/core/v2.0/Descriptor/attributes.yaml#components/schemas/Descriptor | Instructions for fulfillment |
