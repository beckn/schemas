# ServiceCoordinationResource — v2.1

**Schema Pack Version:** 2.1.0
**Released:** June 2026
**Status:** under-review

## Notes

Resource-level attributes for a care coordinator. Extends `ServiceResource/v2.1`
with the standing coordination capability advertised at Discover 2.

### Container

- **Resource.resourceAttributes**

### Key fields

- `coordinationScope` — referralCategories, targetServiceTypes, programmeScope, geographyScope (CodedValue arrays)
- `acceptanceMode` — AUTO_ACCEPT / MANUAL_REVIEW (plain enum)
- `supportedUrgencyTiers` — ROUTINE / URGENT / EMERGENCY (plain enum array)

### Filterable at Discover 2

`coordinationScope.referralCategories`, `coordinationScope.programmeScope`,
`coordinationScope.geographyScope`.
