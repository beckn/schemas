# JobLocation

**Container:** inline sub-schema (shared utility type)
**Tag:** hiring hiring-common shared-type
**Pack:** hiring-common
**Use Cases:** Any hiring-domain network requiring location filtering on job listings or candidate profiles

Flexible location type combining optional GeoJSON geometry and optional postal address fields. At least one must be present (anyOf constraint).

Two modes:
- **Text filtering** — `address_locality`, `address_region`, `address_country` for city/region-based discovery ("jobs in Bengaluru")
- **Geo-spatial** — `geo` (GeoJSONGeometry) for radius-based queries via Beckn SpatialConstraint operators ("jobs within 50 km")

Both modes may coexist on the same object for richer indexing.

Used by:
- `HiringJobResource.location` — work location of a job vacancy
- `CandidateProfileResource.preferred_location` / `current_location` — candidate location preferences
- `DriverCandidateProfileResource.home_location` — driver home location (locality-level only at discovery)

Note: `geo` MUST be locality-level precision at on_discover — precise GPS coordinates MUST NOT be disclosed until a later stage.
