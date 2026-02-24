# SpatialConstraint — v2.0

A spatial constraint using GeoJSON geometry.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [SpatialConstraint](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `SpatialConstraint` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `op` | string | OGC CQL2 spatial operator. |
| `targets` |  | 'One or more JSONPath-like pointers to geometry fields within the item. Example pointers: - `$[''availableAt''][*][''geo'']` (array of site Points) - `$[''itemAttributes''][''ride:dropOff''][''geo'']` (drop zone Polygon)' |
| `geometry` | [GeoJSONGeometry](../../GeoJSONGeometry/README.md) |  |
| `distanceMeters` | number | For `S_DWITHIN`: maximum distance in meters from the target geometry to `geometry` (e.g., "within 5000 m of this Point"). Ignored for other ops. |
| `quantifier` | string | 'How to evaluate when `targets` resolves to an array - - **any**: at least one element matches (default) - **all**: every element must match - **none**: no element may match' |
| `srid` | string | Coordinate Reference System identifier for `geometry`. Default is `"EPSG:4326"`. If provided, servers MAY reproject to EPSG:4326 internally. |
