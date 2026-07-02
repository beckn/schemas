# SalarySpecification — v2.1

**Schema Pack Version:** 2.1.0
**Released:** July 2026
**Status:** Initial release

## Notes

Initial release of the SalarySpecification shared utility type for the hiring domain. Replaces
the flat `salary_min` / `salary_max` / `salary_currency` / `salary_period` fields that were
previously scattered across Offer and candidate schemas, consolidating them into a single
structured sub-object.

Introduces the `PER_GIG` salary period variant to accommodate gig and platform hiring networks
where pay is per completed unit rather than a recurring time period.
