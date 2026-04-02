# SpatialConstraint

**Spatial predicate** using **OGC CQL2 (JSON semantics)** applied to one or more geometry targets in an item. This is where clients express spatial intent. Key ideas: - `targets`: one or more **JSONPath-like** pointers that locate geometry    fields within each item document (e.g., `$['availableAt'][*]['geo']`). - `op`: spatial operator (CQL2). Common ones:      • `S_WITHIN`     (A is completely inside B)     • `S_INTERSECTS` (A intersects B)     • `S_CONTAINS`   (A contains B)     • `S_DWITHIN`    (A within distance of B) - `geometry`: **GeoJSON** literal used as the predicate reference geometry. - `distanceMeters`: required for `S_DWITHIN` when using a GeoJSON Point/shape. - `quantifier`: if a target resolves to an array, choose whether **ANY** (default),    **ALL**, or **NONE** of elements must satisfy the predicate.  CRS: unless otherwise stated, all coordinates are **EPSG:4326**.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/SpatialConstraint/v2.0/attributes.yaml](https://schema.beckn.io/SpatialConstraint/v2.0/attributes.yaml) | [https://schema.beckn.io/SpatialConstraint/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/SpatialConstraint/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/SpatialConstraint/v2.0/context.jsonld](https://schema.beckn.io/SpatialConstraint/v2.0/context.jsonld) | [https://schema.beckn.io/SpatialConstraint/v2.0/vocab.jsonld](https://schema.beckn.io/SpatialConstraint/v2.0/vocab.jsonld) | [https://schema.beckn.io/SpatialConstraint/v2.0/README.md](https://schema.beckn.io/SpatialConstraint/v2.0/README.md) |
