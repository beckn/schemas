# ServiceCoordination Schema

**Container:** `Contract.contractAttributes`
**Extends:** `ServiceContract/v2.1`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Coordination contract (T1), referral lifecycle, handover, deviation signalling
**Tags:** generic-service, coordination, contract

## Overview

ServiceCoordination is the coordination contract (T1) — the core of the generic
coordination layer. It carries the persistent coordination identity, a lifecycle
state machine, the `targetCriteria` the coordinator discovers against, an optional
named-target snapshot (`recommendedTargetRef`), a credential-scoped
`handoverDocument`, a `notificationRoster`, an in-band `deviation` signal, and
transfer (`handoff`) support. Chain: `ServiceContract <- ServiceCoordination <- HealthReferral`.

## Attachment points

- **Primary:** `Contract.contractAttributes` in `on_confirm` / `on_status` of the T1 transaction.

## Design rationale

- **`targetCriteria` vs `recommendedTargetRef`** — `targetCriteria` is mandatory and is
  the substance of the referral (what the coordinator re-discovers against on
  TARGET_REFUSED / retry). `recommendedTargetRef` is an optional, non-binding named
  overlay captured at Discover 1; its presence selects named vs scoped discovery mode.
- **`lifecycleState` state machine** — mirrors the `ServiceEntitlement.state` pattern:
  a plain enum with conditional `required` rules expressed as separate `allOf[]`
  if/then entries (ACTIVE requires coordinationId + targetCriteria; BOOKING_CONFIRMED
  requires targetBookingRef).
- **`handoverDocument`** — a generic, credential-scoped reference: `artifactRef` is a
  label resolving to a Document in the contract's `Descriptor.docs[]`; the URL lives in
  the core Document, never in this field. `credentialScope` is a plain credential id / DID.
- **`deviation`** — the in-band, protocol-carried deviation signal; its `reasonCode` is a
  self-owned CodedValue. The out-of-band registry record is a separate concern (IG).

## Non-goals

- Coordinator standing capability (belongs in `ServiceCoordinationResource`)
- Coordinator acceptance terms / SLAs (belongs in `ServiceCoordinationOffer`)
- The downstream booking (T2) itself (belongs in the domain contract, e.g. HealthContract)

## Upstream candidates

- ServiceContract (generic Beckn service contract)

## Coded values

Self-owned coded fields (`deviation.reasonCode`, `targetCriteria.serviceCategory`) use the pinned typed-`CodedValue` pattern (`const @type`, open/defaulted `@context`). Resolution of a `code` to its value set, and value-set extension by another network, follow **the CodedValue resolution & extension convention (RFC-001, draft)**.
