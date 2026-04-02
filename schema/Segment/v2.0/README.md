# Segment — v2.0

A portion of a rail journey operated continuously by a single carrier between two consecutive stops or stations.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Segment/attributes.yaml](https://schema.beckn.io/Segment/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Segment/v2.0/attributes.yaml](https://schema.beckn.io/Segment/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Segment/attributes.jsonschema.yaml](https://schema.beckn.io/Segment/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Segment/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Segment/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Segment/context.jsonld](https://schema.beckn.io/Segment/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Segment/v2.0/context.jsonld](https://schema.beckn.io/Segment/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Segment/vocab.jsonld](https://schema.beckn.io/Segment/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Segment/v2.0/vocab.jsonld](https://schema.beckn.io/Segment/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `carrierCode` | no | string | Code of the carrier operating this segment |
| `segmentNumber` | no | number | Sequence number of this segment within the journey |
| `trainNumber` | no | string | Train or service number for this segment |
| `coachNumber` | no | string | Coach or carriage number |
| `mode` | no | string | Transport mode for this leg (e.g. BUS, RAIL, WALK, BICYCLE) |
| `origin` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Start location of the leg |
| `destination` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | End location of the leg |
| `startTime` | no | string | Scheduled or actual start time of the leg |
| `endTime` | no | string | Scheduled or actual end time of the leg |
| `distance` | no | number | Distance of this leg in metres |
| `headsign` | no | string | Destination sign text displayed on the vehicle |
| `routeRef` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Reference to the route served on this leg |
