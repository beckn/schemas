# SkillEntry — Shared Type

**Type:** Shared sub-schema
**Protocol Version:** 2.1
**Semantic Model:** generalised
**Version:** 1.0.0
**Used By:** `CandidateProfileResourceAttributes`

## Overview

`SkillEntry` represents a single skill, qualification, or credential held by a candidate
and published as part of their discoverable profile. It is the supply-side counterpart to
`CredentialRequirement` — where `CredentialRequirement` specifies what is needed,
`SkillEntry` specifies what is held.

## Graceful Degradation Design

The type is intentionally designed to support early-stage ecosystems where VC infrastructure
is not yet universal:

- **Self-declared** (`attested: false`, no `proof_request_url`): The candidate declares the
  skill. It is discoverable but marked as unverified. Employers can still see it.
- **VC-backed** (`attested: true`, `proof_request_url` present): The skill is backed by a
  verifiable credential. Employers can trigger VP verification via the proof_request_url.

As more skills get VC-backed over time, individual entries enrich progressively. No schema
version bump is required — the same `SkillEntry` structure handles both phases.

## Privacy Model

The `proof_request_url` points to the DeDi proof-request endpoint for this specific
credential. It does NOT expose the VC payload or any PII. The VC payload remains in the
holder's wallet. Only a signed verification summary is returned to the verifier by the
orchestrating platform.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `category` | enum | Yes | Broad credential class |
| `subtype` | string | Yes | Specific skill or credential name |
| `level` | string | No | Proficiency or qualification level |
| `attested` | boolean | Yes | Whether VC-backed (true) or self-declared (false) |
| `proof_request_url` | uri | No | DeDi VP request endpoint; only when attested = true |

## Upstream Candidate

The `attested` + `proof_request_url` pattern is generalisable beyond hiring — it applies
wherever credentials need to be discoverable before verification. Candidate for Beckn core.
