# GeoJSONGeometry — v2.0

A GeoJSON geometry object (Point, Polygon, etc.).

Part of the [Beckn Protocol Core Schema](../../../README.md) · [GeoJSONGeometry](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `GeoJSONGeometry` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `bbox` | array | Optional bounding box `[west, south, east, north]` in degrees. |
| `coordinates` | array | Coordinates per RFC 7946 for all types **except** GeometryCollection. Order is **[lon, lat, (alt)]**. For Polygons, this is an array of linear rings; each ring is an array of positions. |
| `geometries` | [GeoJSONGeometry](../../GeoJSONGeometry/README.md)[] | Member geometries when `type` is **GeometryCollection**. |
| `type` | string |  |
