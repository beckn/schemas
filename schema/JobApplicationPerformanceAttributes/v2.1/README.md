# JobApplicationPerformanceAttributes Schema

**Container:** `Performance.performanceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Credential verification execution tracking in job application workflows
**Tag:** hiring employment verification performance service

## Overview

`JobApplicationPerformanceAttributes` extends the v2.1 `Performance` container with
execution metadata for the credential verification and application routing service.

In the hiring-jobs use case, the Beckn transaction's "performance" is the service of
verifying an applicant's credentials and routing the application to the employer. This
schema captures how that service was executed: which method was used, what the per-
requirement outcomes were, and whether the application was forwarded.

## Performance Mode: SERVICE

The performance mode is `SERVICE` — the BPP-side platform (e.g. SkillNet) performs a
verification and routing service on behalf of both parties. There is no physical delivery
and no digital access grant — it is a pure service execution.

## Attachment Points

| Container | Schema | Reason |
|-----------|--------|--------|
| `beckn:performanceAttributes` | `JobApplicationPerformanceAttributes` | Execution details of the verification service |

## Design Rationale

**Granular per-requirement results.** Rather than just an aggregate PASS/FAIL, this schema
captures outcomes at the individual requirement level. This is essential for the employer to
understand which specific credentials were verified and which were not — enabling informed
reverification decisions.

**Privacy-preserving.** The `proof_hash` is a SHA-256 hash of the VP — not the VP itself.
`issuer_dids_verified` contains issuer DIDs only — not the subject's DID or any credential
content.

## Non-Goals

- Does not store VC, VP, or any credential payload
- Does not model the employment contract outcome (outside Beckn boundary)
- Does not model physical delivery or digital access
