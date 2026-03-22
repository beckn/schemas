# JobApplicationContractAttributes Schema

**Container:** `Contract.contractAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Job application transaction tracking; credential verification outcome recording
**Tag:** hiring employment application contract verification

## Overview

`JobApplicationContractAttributes` extends the v2.1 `Contract` container with metadata
specific to a job application transaction. The contract binds two parties — the job seeker
(`CANDIDATE`) and the job provider (`EMPLOYER`) — in an application commitment.

This schema captures the application reference, the aggregate credential verification
outcome, and the reverification state. It deliberately excludes VC and VP payloads to
preserve privacy.

## Attachment Points

| Container | Schema | Reason |
|-----------|--------|--------|
| `beckn:contractAttributes` | `JobApplicationContractAttributes` | Application tracking and verification outcome at transaction level |

## Contract Structure

```
Contract {
  parties:     [ { role: "CANDIDATE" }, { role: "EMPLOYER" } ]
  commitments: [ { refType: "RESOURCE", ref: "<job-resource-id>" } ]
  performance: [ { mode: "SERVICE", performanceAttributes: {...} } ]
  contractAttributes: { application_reference, verification_summary, ... }
}
```

## Design Rationale

**No platform routing IDs.** Fields like `cds_listing_id` or internal platform mapping
identifiers are intentionally absent. Platform routing is application-layer plumbing,
not a Beckn protocol concern.

**Reverification as a first-class state.** The employer's right to request re-verification
(documented in the SkillNet design) is modelled as `reverification_requested` +
`reverification_requirements[]`. This enables the Contract status to remain CONFIRMED while
a reverification cycle is in progress, rather than regressing to PENDING.

**No consideration.** There is no monetary transaction within the application contract.
Compensation agreed between the parties is outside the Beckn protocol boundary.

## Non-Goals

- Does not store VC or VP payloads
- Does not model the employment contract itself (that is a post-Beckn relationship)
- Does not carry platform-internal routing identifiers
