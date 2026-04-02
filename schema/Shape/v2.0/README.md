# Shape — v2.0

The geographic path traced by a vehicle along a route, represented as an ordered sequence of geographic coordinates.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Shape/attributes.yaml](https://schema.beckn.io/Shape/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Shape/v2.0/attributes.yaml](https://schema.beckn.io/Shape/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Shape/attributes.jsonschema.yaml](https://schema.beckn.io/Shape/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Shape/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Shape/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Shape/context.jsonld](https://schema.beckn.io/Shape/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Shape/v2.0/context.jsonld](https://schema.beckn.io/Shape/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Shape/vocab.jsonld](https://schema.beckn.io/Shape/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Shape/v2.0/vocab.jsonld](https://schema.beckn.io/Shape/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `shapeId` | no | string | Unique identifier for the shape |
| `distanceTraveled` | no | number | Distance along the shape in metres up to this point |
| `type` | no | string | GeoJSON geometry type (Point, Polygon, LineString, etc.) |
| `coordinates` | no | array | Coordinate array per RFC 7946 |
