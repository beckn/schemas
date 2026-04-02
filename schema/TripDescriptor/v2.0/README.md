# TripDescriptor — v2.0

An identifier that uniquely references a specific vehicle journey in a real-time transit feed.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/TripDescriptor/attributes.yaml](https://schema.beckn.io/TripDescriptor/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/TripDescriptor/v2.0/attributes.yaml](https://schema.beckn.io/TripDescriptor/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/TripDescriptor/attributes.jsonschema.yaml](https://schema.beckn.io/TripDescriptor/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/TripDescriptor/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/TripDescriptor/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/TripDescriptor/context.jsonld](https://schema.beckn.io/TripDescriptor/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/TripDescriptor/v2.0/context.jsonld](https://schema.beckn.io/TripDescriptor/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/TripDescriptor/vocab.jsonld](https://schema.beckn.io/TripDescriptor/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/TripDescriptor/v2.0/vocab.jsonld](https://schema.beckn.io/TripDescriptor/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `tripId` | no | string | GTFS trip_id of the trip being referenced |
| `routeId` | no | string | GTFS route_id associated with the trip |
| `directionId` | no | string | Direction of travel (0 or 1) |
| `startTime` | no | string | Scheduled start time of the trip in HH:MM:SS |
| `startDate` | no | string | Start date of the trip in YYYYMMDD format |
| `scheduleRelationship` | no | string | Relationship to the GTFS schedule (SCHEDULED, ADDED, UNSCHEDULED, CANCELED) |
| `name` | no | string | Short display name of the entity |
| `short_desc` | no | string | Brief textual description |
| `long_desc` | no | string | Detailed or long-form description |
| `media` | no | string | Media resource URLs (images, audio, video) |
| `images` | no | string | Image URLs for visual display |
