# GeoJSONGeometry — v2.0

**GeoJSON geometry** per RFC 7946. Coordinates are in **EPSG:4326 (WGS-84)** and MUST follow **[longitude, latitude, (altitude?)]** order. Supported types: - Point, LineString, Polygon - MultiPoint, MultiLineString, MultiPolygon - GeometryCollection (uses `geometries` instead of `coordinates`) Notes: - For rectangles, use a Polygon with a single linear ring where the first  and last positions are identical. - Circles are **not native** to GeoJSON. For circular searches, use  `SpatialConstraint` with `op: s_dwithin` and a Point + `distanceMeters`,  or approximate the circle as a Polygon. - Optional `bbox` is `[west, south, east, north]` in degrees.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/GeoJSONGeometry/attributes.yaml](https://schema.beckn.io/GeoJSONGeometry/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml](https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/GeoJSONGeometry/attributes.jsonschema.yaml](https://schema.beckn.io/GeoJSONGeometry/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/GeoJSONGeometry/context.jsonld](https://schema.beckn.io/GeoJSONGeometry/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/GeoJSONGeometry/v2.0/context.jsonld](https://schema.beckn.io/GeoJSONGeometry/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/GeoJSONGeometry/vocab.jsonld](https://schema.beckn.io/GeoJSONGeometry/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/GeoJSONGeometry/v2.0/vocab.jsonld](https://schema.beckn.io/GeoJSONGeometry/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `bbox` | no | array | Optional bounding box `[west, south, east, north]` in degrees. |
| `coordinates` | no | array | Coordinates per RFC 7946 for all types **except** GeometryCollection. Order is **[lon, lat, (alt)]**. For Polygons, this is an array of linear rings; each ring is an array of positions. |
| `geometries` | no | array | Member geometries when `type` is **GeometryCollection**. |
| `type` | yes | string | - |
