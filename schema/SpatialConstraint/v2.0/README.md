# SpatialConstraint — v2.0

**Spatial predicate** using **OGC CQL2 (JSON semantics)** applied to one or more geometry targets in an item. This is where clients express spatial intent. Key ideas: - `targets`: one or more **JSONPath-like** pointers that locate geometry    fields within each item document (e.g., `$['availableAt'][*]['geo']`). - `op`: spatial operator (CQL2). Common ones:      • `S_WITHIN`     (A is completely inside B)     • `S_INTERSECTS` (A intersects B)     • `S_CONTAINS`   (A contains B)     • `S_DWITHIN`    (A within distance of B) - `geometry`: **GeoJSON** literal used as the predicate reference geometry. - `distanceMeters`: required for `S_DWITHIN` when using a GeoJSON Point/shape. - `quantifier`: if a target resolves to an array, choose whether **ANY** (default),    **ALL**, or **NONE** of elements must satisfy the predicate.  CRS: unless otherwise stated, all coordinates are **EPSG:4326**.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SpatialConstraint/attributes.yaml](https://schema.beckn.io/SpatialConstraint/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SpatialConstraint/v2.0/attributes.yaml](https://schema.beckn.io/SpatialConstraint/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SpatialConstraint/attributes.jsonschema.yaml](https://schema.beckn.io/SpatialConstraint/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SpatialConstraint/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SpatialConstraint/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SpatialConstraint/context.jsonld](https://schema.beckn.io/SpatialConstraint/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SpatialConstraint/v2.0/context.jsonld](https://schema.beckn.io/SpatialConstraint/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SpatialConstraint/vocab.jsonld](https://schema.beckn.io/SpatialConstraint/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SpatialConstraint/v2.0/vocab.jsonld](https://schema.beckn.io/SpatialConstraint/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `op` | yes | string | OGC CQL2 spatial operator. |
| `targets` | yes | any | 'One or more JSONPath-like pointers to geometry fields within the item.  Example pointers:  - `$[''availableAt''][*][''geo'']` (array of site Points)  - `$[''itemAttributes''][''ride:dropOff''][''geo'']` (drop zone Polygon)'  |
| `geometry` | no | object | - |
| `distanceMeters` | no | number | For `S_DWITHIN`: maximum distance in meters from the target geometry to `geometry` (e.g., "within 5000 m of this Point"). Ignored for other ops. |
| `quantifier` | no | string | 'How to evaluate when `targets` resolves to an array - - **any**: at least one element matches (default) - **all**: every element must match  - **none**: no element may match'  |
| `srid` | no | string | Coordinate Reference System identifier for `geometry`. Default is `"EPSG:4326"`. If provided, servers MAY reproject to EPSG:4326 internally. |
