# GeoJSONGeometry

**GeoJSON geometry** per RFC 7946. Coordinates are in **EPSG:4326 (WGS-84)** and MUST follow **[longitude, latitude, (altitude?)]** order.
Supported types: - Point, LineString, Polygon - MultiPoint, MultiLineString, MultiPolygon - GeometryCollection (uses `geometries` instead of `coordinates`)
Notes: - For rectangles, use a Polygon with a single linear ring where the first
  and last positions are identical.
- Circles are **not native** to GeoJSON. For circular searches, use
  `SpatialConstraint` with `op: s_dwithin` and a Point + `distanceMeters`,
  or approximate the circle as a Polygon.
- Optional `bbox` is `[west, south, east, north]` in degrees.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml](https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.yaml) | [https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/GeoJSONGeometry/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/GeoJSONGeometry/v2.0/context.jsonld](https://schema.beckn.io/GeoJSONGeometry/v2.0/context.jsonld) | [https://schema.beckn.io/GeoJSONGeometry/v2.0/vocab.jsonld](https://schema.beckn.io/GeoJSONGeometry/v2.0/vocab.jsonld) | [https://schema.beckn.io/GeoJSONGeometry/v2.0/README.md](https://schema.beckn.io/GeoJSONGeometry/v2.0/README.md) |
