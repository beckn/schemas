# Geo JSON Geometry

> **Canonical IRI:** [`https://schema.beckn.io/GeoJSONGeometry`](https://schema.beckn.io/GeoJSONGeometry)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

**GeoJSON geometry** per RFC 7946. Coordinates are in **EPSG:4326 (WGS-84)** and MUST follow **[longitude, latitude, (altitude?)]** order. Supported types: - Point, LineString, Polygon - MultiPoint, MultiLineString, MultiPolygon - GeometryCollection (uses `geometries` instead of `coordinates`) Notes: - For rectangles, use a Polygon with a single linear ring where the first and last positions are identical. - Circles are **not native** to GeoJSON. For circular searches, use `SpatialConstraint` with `op: s_dwithin` and a Point + `distanceMeters`, or approximate the circle as a Polygon. - Optional `bbox` is `[west, south, east, north]` in degrees.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `bbox` | any[] | — | Optional bounding box `[west, south, east, north]` in degrees. |
| `coordinates` | any[] | — | Coordinates per RFC 7946 for all types **except** GeometryCollection. Order is **[lon, lat, (alt)]**. For Polygons, this is an array of linear ring… |
| `geometries` | any[] | — | Member geometries when `type` is **GeometryCollection**. |
| `type` | `string` | ✅ | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/GeoJSONGeometry` |
| JSON Schema (latest) | `https://schema.beckn.io/GeoJSONGeometry/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/GeoJSONGeometry/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/GeoJSONGeometry/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
