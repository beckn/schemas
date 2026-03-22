# HiringJobResourceAttributes Schema

**Container:** `Resource.resourceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Job discovery in any hiring marketplace (tech, construction, logistics, healthcare, gig economy, campus hiring)
**Tag:** hiring employment jobs workforce

## Overview

`HiringJobResourceAttributes` extends the v2.1 `Resource` container with intrinsic metadata
about a job opportunity. It is intentionally domain-generic — usable by any BAP/BPP pair
in a hiring vertical without modification.

The schema captures what a job *is*: its type, work arrangement, location, industry context,
and the credential requirements an applicant must satisfy. Commercial terms (compensation,
openings, application deadline) belong in `HiringJobOfferAttributes`.

## Attachment Points

| Container | Schema | Reason |
|-----------|--------|--------|
| `beckn:resourceAttributes` | `HiringJobResourceAttributes` | Intrinsic job metadata; needed at discovery time |

## Design Rationale

**Requirements as first-class fields.** Job requirements (`requirements[]`) are placed in
`resourceAttributes` rather than `offerAttributes` because they are intrinsic to the role,
not to a commercial offer. A job's credential requirements do not change with compensation —
they define the role itself. This also enables BAP-side filtering at discovery time without
resolving the Offer.

**CodedValue for industry.** `industry_type` uses the `CodedValue` pattern (ISIC, NIC, or
any authority) rather than a hardcoded enum. This makes the schema valid in any country
without modification.

**No PII.** The schema contains no personal data. The employer's identity is managed by the
BPP and masked by the BAP platform in federated discovery. The `provider` field on the core
`Resource` object handles provider attribution without exposing it in the extension schema.

**No pricing.** Compensation is absent from this schema by design. It belongs in
`HiringJobOfferAttributes.proposedConsideration` and the offer's compensation range fields.

## Non-Goals

- Does not capture pricing, compensation, or openings count (→ `HiringJobOfferAttributes`)
- Does not capture application state or verification outcome (→ `JobApplicationContractAttributes`)
- Does not capture verification execution details (→ `JobApplicationPerformanceAttributes`)
- Does not store employer identity or internal platform routing IDs

## Upstream Candidates

- `requirements[]` using `CredentialRequirement` — generic enough for Beckn core
- `CodedValue` pattern for authority-governed enumerations — generic enough for Beckn core
- `work_mode` enum (ONSITE/REMOTE/HYBRID) — applicable across multiple verticals
