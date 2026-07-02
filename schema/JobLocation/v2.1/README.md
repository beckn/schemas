# JobLocation — v2.1

**Schema Pack Version:** 2.1.0
**Released:** July 2026
**Status:** Initial release

## Notes

Initial release of the JobLocation shared utility type for the hiring domain. Introduces the
flexible anyOf location model combining GeoJSON geometry (`geo`) and postal address fields
(`address_locality`, `address_region`, `address_country`), supporting both text-based
discovery filtering and geo-spatial radius queries via Beckn SpatialConstraint operators.

Privacy constraint introduced at this version: `geo` MUST be locality-level precision at
`on_discover` — precise GPS coordinates MUST NOT be disclosed until a later contract stage.
