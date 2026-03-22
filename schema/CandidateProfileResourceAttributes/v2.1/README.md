# CandidateProfileResourceAttributes Schema

**Container:** `Resource.resourceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Talent marketplace — employer discovers candidate profiles; reverse hiring discovery
**Tag:** hiring candidates talent workforce skills profile

## Overview

`CandidateProfileResourceAttributes` extends the v2.1 `Resource` container with the
attributes of a discoverable candidate profile. In this topology, the candidate (or their
representing platform) is the **BPP**, and the employer is the **BAP**. The Resource is
the candidate's profile — their skills, experience, availability, and work preferences.

This inverts the classical hiring topology (employer as BPP) and enables a talent catalogue
that employers can search — making previously invisible or informal workers discoverable
across a federated network.

## Attachment Points

| Container | Schema | Reason |
|-----------|--------|--------|
| `beckn:resourceAttributes` | `CandidateProfileResourceAttributes` | Candidate profile metadata needed at discovery time |

## The SkillEntry Design (Graceful Degradation)

The `skills[]` array uses the shared `SkillEntry` type, designed for progressive enrichment:

| Phase | `attested` | `proof_request_url` | Employer sees |
|-------|-----------|---------------------|---------------|
| Early ecosystem | `false` | absent | Skill visible, labelled "self-declared" |
| VC ecosystem growing | `true` | present | Skill visible, VC verification available |

Employers can discover and filter on self-declared skills. As the VC ecosystem matures,
the same profiles enrich automatically — no schema migration required.

## Privacy Design

- **No PII.** No name, contact, address, date of birth, or government ID.
- The candidate's identity and DID are managed at the core `Resource.provider` level.
- `proof_request_url` is a DeDi endpoint — employers trigger a VP request through the
  platform; the VC payload never leaves the holder's wallet.
- `overall_verification_status` is derived from the public DeDi `verification_index`.

## Design Rationale

**Topology inversion.** In the classical hiring-jobs topology, employers are BPPs and
candidates are BAPs. Here, the candidate's platform is the BPP, publishing their profile
as a Resource. An employer BAP searches across BPPs for matching candidates. This enables
a federated talent network where no single platform owns all candidates.

**No compensation in resourceAttributes.** The candidate's desired compensation terms
belong in `CandidateAvailabilityOfferAttributes`, not here. This keeps Resource neutral
and allows different offers (e.g., different notice periods or contract types) to cover
the same profile Resource.

## Non-Goals

- Does not store VC or VP payloads
- Does not carry employer preferences or job requirements (→ hiring-jobs pack)
- Does not model the hiring contract itself (→ `EmployerHiringContractAttributes`)
