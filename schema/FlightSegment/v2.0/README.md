# FlightSegment — v2.0

A single non-stop flight operated between two airports, forming a unit of an air travel itinerary.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FlightSegment/attributes.yaml](https://schema.beckn.io/FlightSegment/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FlightSegment/v2.0/attributes.yaml](https://schema.beckn.io/FlightSegment/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FlightSegment/attributes.jsonschema.yaml](https://schema.beckn.io/FlightSegment/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FlightSegment/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FlightSegment/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FlightSegment/context.jsonld](https://schema.beckn.io/FlightSegment/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FlightSegment/v2.0/context.jsonld](https://schema.beckn.io/FlightSegment/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FlightSegment/vocab.jsonld](https://schema.beckn.io/FlightSegment/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FlightSegment/v2.0/vocab.jsonld](https://schema.beckn.io/FlightSegment/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `flightNumber` | no | string | IATA/ICAO flight number (e.g. AI101) |
| `departureAirport` | no | string | IATA airport code of the departure airport |
| `arrivalAirport` | no | string | IATA airport code of the arrival airport |
| `departureTime` | no | string | Scheduled local departure date and time |
| `arrivalTime` | no | string | Scheduled local arrival date and time |
| `airline` | no | string | IATA airline code of the operating carrier |
| `aircraftType` | no | string | IATA aircraft type code |
| `mode` | no | string | Transport mode for this leg (e.g. BUS, RAIL, WALK, BICYCLE) |
| `origin` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | Start location of the leg |
| `destination` | no | $ref: https://schema.beckn.io/Location/v2.0/attributes.yaml#/components/schemas/Location | End location of the leg |
| `startTime` | no | string | Scheduled or actual start time of the leg |
| `endTime` | no | string | Scheduled or actual end time of the leg |
| `distance` | no | number | Distance of this leg in metres |
| `headsign` | no | string | Destination sign text displayed on the vehicle |
| `routeRef` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Reference to the route served on this leg |
