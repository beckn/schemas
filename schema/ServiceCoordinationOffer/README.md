# ServiceCoordinationOffer Schema

**Container:** `Offer.offerAttributes`
**Extends:** `ServiceOffer/v2.1`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Coordinator terms publishing, SLA commitment
**Tags:** generic-service, coordination, offer

## Overview

ServiceCoordinationOffer defines a care coordinator's terms for accepting a
coordination engagement: per-urgency SLA windows, its retry policy on downstream
refusal, whether it supports transferring an in-flight coordination to another
coordinator, and an optional capacity signal.

## Attachment points

- **Primary:** `Offer.offerAttributes` in `on_search` / catalogue responses.

## Design rationale

SLA windows are expressed per urgency tier so the same coordinator can commit to
tighter turnaround for URGENT/EMERGENCY referrals than for ROUTINE ones.
`retryPolicy` and `handoffSupported` are operational, protocol-invariant plain
enums/booleans rather than CodedValues.

## Non-goals

- Coordinator standing capability (belongs in `ServiceCoordinationResource`)
- The coordination contract (belongs in `ServiceCoordination`)

## Upstream candidates

- ServiceOffer (generic Beckn service offer)
