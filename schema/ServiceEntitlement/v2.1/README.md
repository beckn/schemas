# ServiceEntitlement — v2.1

**Schema Pack Version:** 2.1.0
**Released:** April 2026
**Status:** Initial release

## Notes

New schema introduced in v2.1 of the generic-service schema pack. Represents a durable service-credit artifact issued when a Seeker NP (implementing agency, payer organisation) pre-purchases service capacity from a Provider NP in a procurement engagement.

Consuming engagements draw down against the entitlement by referencing its `entitlementId` in their consideration attributes (see ServiceConsideration v2.1 `entitlementRef` field).

### Container

- **Contract.contractAttributes**

### Key features

- Full lifecycle state machine: DRAFT → ACTIVE → LOW → EXPIRED → REVOKED → CLOSED
- Capacity tracking: totalCapacity, usedCapacity, remainingCapacity
- Geography and counterparty scoping for multi-provider networks
- Redemption rules: min/max per redemption, cooldown periods
- Locked terms snapshot for dispute resolution
- Grievance reference linking to NFO arbitration records
