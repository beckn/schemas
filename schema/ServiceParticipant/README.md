# ServiceParticipant Schema

**Container:** `Participant.participantAttributes`
**Extends:** *(standalone — domain-neutral base)*
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Tag:** service generic-service participant

## Overview

ServiceParticipant is the domain-neutral base for participant attribute schemas in the Beckn generalised model. It defines a single field — `credentialRefs` — an array of Beckn Credential/2.0 objects that participant schemas in any domain can inherit via `allOf` to provide runtime proof of credentials.

The schema is intentionally minimal. It does not model role, identity, or domain-specific attributes — those belong in the domain extension schema. Its sole purpose is to make `credentialRefs` a portable, reusable, consistently typed field across all Beckn networks.

## Attachment Points

Attaches to `Participant.participantAttributes` within `Contract.participants[]`. Domain-specific participant schemas extend ServiceParticipant and add role, identity, and domain-specific sub-objects alongside the inherited `credentialRefs`.

## Design Rationale

- **`credentialRefs` referencing Beckn Credential/2.0** — Rather than defining a custom credential structure, ServiceParticipant delegates entirely to the Beckn core Credential/2.0 type (`https://schema.beckn.io/Credential/v2.0/attributes.yaml`). This keeps the definition authoritative and in sync with the broader Beckn trust infrastructure.

- **Credential/2.0 is a `oneOf` of two branches:**
  - *W3C Verifiable Credential* — an opaque JSON object (`additionalProperties: true`) conforming to the W3C VC Data Model. Machine-verifiable via the issuer's DID. Beckn intentionally does not validate the internal VC structure at the schema layer — the W3C VC spec governs that.
  - *Document Credential* — a Beckn Document/2.0 object (`label`, `url`, `mimeType` required; `standard`, `security` optional). For manual/offline verification of PDFs, images, or other document-based credentials. Use the `standard` field to convey credential type (e.g. `MedicalLicence`, `FacilityAccreditation`, `NGORegistration`).

- **Separation from domain-specific credential metadata** — `credentialRefs` is the runtime proof link, not a place to model credential attributes. Any domain-specific structured credential metadata (e.g. specialty, accreditation body, registration number for query and filtering purposes) belongs in a domain-specific sub-object in the extending schema (e.g. `specialistAccreditation` in HealthParticipant).

- **No role or identity fields at base level** — Role and identity are domain-specific enough that generalising them here would produce an unusable schema. Domain extensions add those fields on top.

## Non-Goals

- Does not model participant role — that belongs in the domain-specific extension.
- Does not model national or sector-specific identity identifiers — those belong in the domain extension (e.g. `healthIds` in HealthParticipant).
- Does not model consent, authorisation, or access control — those belong in the Contract schema.
- Does not validate credential content — credential verification is a network trust layer concern, not a schema concern.

## Upstream Candidates

- `credentialRefs` (Credential/2.0 array) — if Beckn core defines a `Participant.credentials` field at the protocol level in a future version, this field could be upstreamed and ServiceParticipant retired. Until then, it serves as the generalised layer between Beckn core types and domain participant schemas.
