# ServiceCoordination — v2.1

**Schema Pack Version:** 2.1.0
**Released:** June 2026
**Status:** under-review

## Notes

The coordination contract (T1). Extends `ServiceContract/v2.1`. Specialised by
`HealthReferral` in the OHSN pack.

### Container

- **Contract.contractAttributes**

### lifecycleState (state machine)

`DRAFT, ACTIVE, TARGET_SELECTED, BOOKING_CONFIRMED, TARGET_NOTIFIED, ATTENDED,
NO_SHOW, CANCELLED, PROVIDER_CANCELLED, OUTCOME_RECEIVED, SLA_BREACHED, LAPSED,
REVOKED, WITHDRAWN, CLOSED`

Conditional requireds (each a separate `allOf[]` if/then):

| When lifecycleState == | then required |
|---|---|
| ACTIVE | coordinationId, targetCriteria |
| TARGET_SELECTED | targetCriteria |
| BOOKING_CONFIRMED | targetBookingRef |

### Key fields

- `coordinationId` (uuid, required) — persistent coordination id (Referral ID for health)
- `targetCriteria` (object, required) — what the coordinator discovers against
- `recommendedTargetRef` (object, optional) — advisory named-provider snapshot
- `handoverDocument` (object) — credential-scoped handover reference
- `notificationRoster` (object[]) — parties to notify
- `deviation` (object) — in-band deviation signal (self-owned CodedValue reasonCode)
- `handoff` (object) — T1 transfer to another coordinator
