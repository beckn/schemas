# ServiceCoordinationResource Schema

**Container:** `Resource.resourceAttributes`
**Extends:** `ServiceResource/v2.1`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Coordinator discovery (Discover 2), referral routing
**Tags:** generic-service, coordination, resource

## Overview

ServiceCoordinationResource is the discoverable catalogue entry for a care
coordinator. It describes the coordinator's *standing capability* — the referral
categories it handles, the downstream service types it books toward, its
programme and geographic catchment, its acceptance mode, and the urgency tiers it
supports. Seekers filter coordinators against this scope when addressing the
coordination transaction (T1).

## Attachment points

- **Primary:** `Resource.resourceAttributes` in `on_search` / catalogue responses.

## Design rationale

The coordinator's standing scope (`coordinationScope`) is distinct from the
per-referral `targetCriteria` carried on the `ServiceCoordination` contract. The
former is what the coordinator advertises; the latter is what an individual
referral asks the coordinator to discover against downstream.

`referralCategories` and `targetServiceTypes` are self-owned CodedValues whose
default coding authority is this schema's own context; networks may override the
`@context` to extend the value sets. `programmeScope` and `geographyScope` are
externally governed CodedValues.

## Non-goals

This schema does NOT define:
- Per-referral target requirements (belongs in `ServiceCoordination.targetCriteria`)
- Coordination acceptance terms / SLAs (belongs in `ServiceCoordinationOffer`)
- The coordination contract itself (belongs in `ServiceCoordination`)

## Upstream candidates

- ServiceResource (generic Beckn service resource)
