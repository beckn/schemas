# ServiceEntitlement Schema

**Container:** `Contract.contractAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Bulk procurement engagements, government/NGO/institutional service purchase, entitlement-funded service consumption, camp-based service delivery
**Tag:** service generic-service contract

## Overview

ServiceEntitlement models a durable service-credit artifact issued when a Seeker NP (implementing agency, payer organisation) pre-purchases service capacity from a Provider NP in a procurement engagement. The entitlement records the committed capacity, validity window, geographic and counterparty scope, and redemption rules. Consuming engagements draw down against it by referencing `entitlementId` in their `ServiceConsideration.entitlementRef`.

This schema enables the two-contract procurement model: a procurement Contract (funded by milestone payments) issues an entitlement; subsequent per-patient or per-session Contracts are funded by drawing down against that entitlement rather than by fresh payment authorisation.

## Attachment Points

Attaches to `Contract.contractAttributes` on the procurement Contract. The entitlement is created when the procurement Contract reaches ACTIVE state (on_confirm) and persists until EXPIRED, REVOKED, or CLOSED.

## Design Rationale

- **Separation from ServiceContract** — ServiceContract captures booking-time metadata applicable to all service contracts. ServiceEntitlement is specific to the procurement sub-type where capacity is pre-committed, and its lifecycle (DRAFT → ACTIVE → LOW → EXPIRED → REVOKED → CLOSED) is independent of the per-patient contract lifecycle. Keeping them separate avoids conflating two distinct contract roles.
- **Mutual exclusivity with paymentAuthorisation** — `ServiceConsideration` enforces a `oneOf` constraint: either `paymentAuthorisation` (fresh payment) or `entitlementRef` (drawdown) is present — never both. This makes the funding model explicit and unambiguous at the contract level.
- **Capacity counters** — `totalCapacity`, `usedCapacity`, and `remainingCapacity` are maintained by the Provider NP and updated via `update`/`on_update` messages as each consuming engagement is confirmed. The `LOW` state signals that the seeker should initiate a top-up procurement before capacity runs out.
- **Locked terms snapshot** — `lockedTermsSnapshot` carries a JSON snapshot of the procurement offer terms at commit time, providing a tamper-evident reference for dispute resolution without requiring the Provider NP to retain offer history indefinitely.

## Non-Goals

- Does not model per-patient or per-session contract metadata — that is ServiceContract's role.
- Does not model payment settlement for the procurement Contract itself — that is ServiceSettlement's role.
- Does not model the scheduling or logistics of individual consuming engagements — that is ServicePerformance's role.
- Does not enforce or validate entitlement drawdown cryptographically — authentication and integrity are the responsibility of the network's trust infrastructure.

## Upstream Candidates

- `entitlementId` / `issuerId` / `holderId` / `state` — generic enough to belong in a core `Entitlement` type if the Beckn core ever introduces a first-class capacity-credit primitive.
- `redemptionRules` (min/max per redemption, cooldown) — applicable to any network where pre-purchased capacity is drawn down in bounded increments.
