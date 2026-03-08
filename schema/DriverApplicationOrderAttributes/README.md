# DriverApplicationOrderAttributes Schema

**Container:** `Order.orderAttributes`
**Version:** 1.0.0
**Use Cases:** UC1 and UC2 — established at `init`, updated through `confirm`
**Tag:** mobility driver-network

---

## Overview

`DriverApplicationOrderAttributes` captures **transaction-level metadata** for a driver hiring application. It is attached to a Beckn `Order` as `orderAttributes` from the `init` stage onwards.

This schema holds the identifiers, submitted credential documents, Driver Passport reference, offer outcome, and onboarding status. The execution stage data (interview scheduling, driving tests, hiring state machine) belongs in `DriverHiringFulfillmentAttributes`.

---

## Attachment Point

```
Order
└── orderAttributes  →  DriverApplicationOrderAttributes
```

---

## Key Properties

| Property | Type | PII | Disclosure Stage | Notes |
|---|---|---|---|---|
| `applicationId` | string | No | init | Network-assigned transaction ID |
| `jobId` | string | No | init | Job listing being applied to |
| `driverPassportReference` | string (URI) | **Yes** | **init+** | Driver consent required |
| `submittedDocuments` | DriverCredential[] | **Yes** | **update+** | Credential docs submitted |
| `offerReference` | string | No | update | Links to DriverJobOfferAttributes |
| `offerStatus` | string (vocab) | No | update | OfferStatus vocab term |
| `acceptanceTimestamp` | date-time | No | confirm | When driver accepted |
| `onboardingStatus` | string (vocab) | No | confirm | OnboardingStatus vocab term |

---

## DriverCredential Sub-Schema

| Field | PII | Notes |
|---|---|---|
| `credentialType` | No | CredentialType vocab term |
| `issuer` | No | Issuing authority name |
| `credentialRef` | **Yes** | Licence number, verification ID — never index |
| `issuedOn` | No | ISO 8601 date |
| `validUntil` | No | ISO 8601 date |
| `documentURL` | **Yes** | Signed URL — access-controlled, short-lived |

---

## Design Rationale

**Why is this separate from DriverHiringFulfillmentAttributes?**
Beckn v2 requires that `Order` = transaction record and `Fulfillment` = execution model. Application identifiers, submitted documents, and offer outcomes are transaction record fields. Interview schedules, driving test results, and hiring stage transitions are execution fields. Merging them (as the original draft did in `DriverApplicationLifecycleAttributes`) creates an oversized schema that cannot evolve independently.

**Why are credential documents flagged with disclosure stages?**
Submitting a driving licence or police verification document is a sensitive act. The `x-pii-disclosure-stage` annotation signals to platforms that these fields must be omitted from `init` payloads in some configurations, and shared only when the operator has progressed the application to the evaluation stage (`update`).

---

## Non-Goals

- Interview scheduling, hiring stage state machine → `DriverHiringFulfillmentAttributes`
- Salary and offer commercial terms → `DriverJobOfferAttributes`
- Job description and role requirements → `DriverJobDescriptionAttributes`
- Driver identity (name, date of birth) → Driver Passport (shared via `driverPassportReference`)
