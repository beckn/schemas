# Spatial Constraint

> **Canonical IRI:** [`https://schema.beckn.io/SpatialConstraint`](https://schema.beckn.io/SpatialConstraint)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

**Spatial predicate** using **OGC CQL2 (JSON semantics)** applied to one or more geometry targets in an item. This is where clients express spatial intent. Key ideas: - `targets`: one or more **JSONPath-like** pointers that locate geometry fields within each item document (e.g., `$['availableAt'][*]['geo']`). - `op`: spatial operator (CQL2). Common ones: • `S_WITHIN` (A is completely inside B) • `S_INTERSECTS` (A intersects B) • `S_CONTAINS` (A contains B) • `S_DWITHIN` (A within distance of B) - `geometry`: **GeoJSON** literal used as the predicate reference geometry. - `distanceMeters`: required for `S_DWITHIN` when using a GeoJSON Point/shape. - `quantifier`: if a target resolves to an array, choose whether **ANY** (default), **ALL**, or **NONE** of elements must satisfy the predicate. CRS: unless otherwise stated, all coordinates are **EPSG:4326**.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `op` | `string` | ✅ | OGC CQL2 spatial operator. |
| `targets` | `string` \| `array` | ✅ | 'One or more JSONPath-like pointers to geometry fields within the item. Example pointers: - `$[''availableAt''][*][''geo'']` (array of site Points)… |
| `geometry` | object | — | — |
| `distanceMeters` | `number` | — | For `S_DWITHIN`: maximum distance in meters from the target geometry to `geometry` (e.g., "within 5000 m of this Point"). Ignored for other ops. |
| `quantifier` | `string` | — | 'How to evaluate when `targets` resolves to an array - - **any**: at least one element matches (default) - **all**: every element must match - **no… |
| `srid` | `string` | — | Coordinate Reference System identifier for `geometry`. Default is `"EPSG:4326"`. If provided, servers MAY reproject to EPSG:4326 internally. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/SpatialConstraint` |
| JSON Schema (latest) | `https://schema.beckn.io/SpatialConstraint/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/SpatialConstraint/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/SpatialConstraint/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
