# MonitoredCall — v2.0

A real-time arrival or departure prediction for a specific vehicle at a specific stop within a monitored journey.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/MonitoredCall/attributes.yaml](https://schema.beckn.io/MonitoredCall/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/MonitoredCall/v2.0/attributes.yaml](https://schema.beckn.io/MonitoredCall/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/MonitoredCall/attributes.jsonschema.yaml](https://schema.beckn.io/MonitoredCall/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/MonitoredCall/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/MonitoredCall/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/MonitoredCall/context.jsonld](https://schema.beckn.io/MonitoredCall/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/MonitoredCall/v2.0/context.jsonld](https://schema.beckn.io/MonitoredCall/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/MonitoredCall/vocab.jsonld](https://schema.beckn.io/MonitoredCall/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/MonitoredCall/v2.0/vocab.jsonld](https://schema.beckn.io/MonitoredCall/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `stopPointRef` | no | $ref: https://schema.beckn.io/StopPoint/v2.0/attributes.yaml#/components/schemas/StopPoint | Reference to the stop point for this call |
| `visitNumber` | no | number | Visit sequence number for loop services |
| `vehicleAtStop` | no | boolean | Whether the vehicle is currently at the stop |
| `expectedArrivalTime` | no | string | Predicted arrival time at this stop |
| `expectedDepartureTime` | no | string | Predicted departure time from this stop |
| `aimedArrivalTime` | no | string | Scheduled arrival time from the timetable |
| `aimedDepartureTime` | no | string | Scheduled departure time from the timetable |
| `arrivalStatus` | no | string | Arrival status (e.g. onTime, delayed, early) |
| `departureStatus` | no | string | Departure status (e.g. onTime, delayed, early) |
| `id` | no | string | Unique identifier for the tracking record |
| `url` | no | string | URL endpoint for real-time tracking information |
| `status` | no | $ref: https://schema.beckn.io/State/v2.0/attributes.yaml#/components/schemas/State | Current tracking status |
| `validity` | no | $ref: https://schema.beckn.io/TimePeriod/v2.0/attributes.yaml#/components/schemas/TimePeriod | Validity period for this tracking record |
