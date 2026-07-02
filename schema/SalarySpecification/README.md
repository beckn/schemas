# SalarySpecification

**Container:** inline sub-schema (shared utility type)
**Tag:** hiring hiring-common shared-type
**Pack:** hiring-common
**Use Cases:** Any hiring-domain network carrying salary data on job offers or candidate expectations

Structured salary range (or fixed value) with currency and payment period. Replaces flat `salary_min` / `salary_max` / `salary_currency` / `salary_period` fields that were previously scattered across Offer and candidate schemas.

Properties:
- `salary_min` — minimum (or fixed) value
- `salary_max` — maximum value for a range; omit for fixed salary
- `salary_currency` — ISO 4217 code (e.g. INR, USD)
- `salary_period` — ANNUAL, MONTHLY, WEEKLY, HOURLY, or PER_GIG

The `PER_GIG` period variant accommodates gig and platform hiring networks where pay is per completed unit rather than a time period.

Used by:
- `HiringJobOffer.salary_specification` — compensation offered by the employer
- `CandidateProfileResource.expected_salary` — salary expectation declared by the candidate
