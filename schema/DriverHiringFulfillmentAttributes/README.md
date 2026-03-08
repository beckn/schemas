# DriverHiringFulfillmentAttributes Schema

**Container:** `Fulfillment.fulfillmentAttributes`
**Version:** 1.0.0
**Use Cases:** UC1 and UC2 — updated progressively via `update`/`on_update` interactions
**Tag:** mobility driver-network

---

## Overview

`DriverHiringFulfillmentAttributes` models the **execution stages** of the driver hiring process. It tracks the multi-stage hiring lifecycle state machine and carries scheduling details for evaluation activities (interviews, driving tests).

This schema was added during the v2 migration. The original draft merged execution stage data into `DriverApplicationOrderAttributes`, which violated the Beckn v2 principle that `Fulfillment` = execution model and `Order` = transaction record.

---

## Attachment Point

```
Fulfillment
└── fulfillmentAttributes  →  DriverHiringFulfillmentAttributes
```

---

## Hiring State Machine

```
APPLICATION_SUBMITTED
  → UNDER_REVIEW
    → INTERVIEW_SCHEDULED
      → EVALUATION_COMPLETE
        → OFFER_ISSUED
          → OFFER_ACCEPTED → HIRING_CONFIRMED → ONBOARDING_COMPLETE
          → OFFER_REJECTED
```

Each stage transition is communicated via an `update`/`on_update` interaction with the updated `hiringStage` value.

---

## Key Properties

| Property | Type | Notes |
|---|---|---|
| `hiringStage` | string (vocab) | Current stage — HiringStage vocab term |
| `screeningNotes` | string | Outcome notes from initial screening |
| `interviewSchedule` | InterviewDetails[] | Populated at INTERVIEW_SCHEDULED; updated as rounds complete |
| `drivingTestSchedule` | DrivingTestDetails[] | Populated when driving assessment is scheduled |

### InterviewDetails

| Field | Type | Notes |
|---|---|---|
| `interviewType` | string | IN_PERSON, VIDEO, TELEPHONIC |
| `scheduledAt` | date-time | ISO 8601 |
| `locationOrLink` | string | Physical address or call URL |
| `interviewer` | string | Interviewing officer name or ID |
| `status` | string | SCHEDULED, COMPLETED, CANCELLED, NO_SHOW |
| `remarks` | string | Interview outcome notes |

### DrivingTestDetails

| Field | Type | Notes |
|---|---|---|
| `scheduledAt` | date-time | ISO 8601 |
| `location` | string | Test venue address |
| `vehicleCategory` | string | DriverVehicleCategory vocab |
| `evaluator` | string | Evaluating officer name or ID |
| `result` | string | PASS, FAIL, PENDING |
| `remarks` | string | Evaluator remarks |

---

## Design Rationale

**Why is this a separate schema and not part of Order?**
The hiring lifecycle (interview scheduling, driving tests, screening status) is an execution process — it maps to the `Fulfillment` entity in Beckn v2, which carries state and execution metadata. `Order` should only hold transaction identifiers and outcomes. Mixing them creates a schema that cannot be evolved independently.

**Why are multiple interview rounds supported?**
Many operators conduct multiple interview rounds (initial screening, managerial interview, HR round). The `interviewSchedule` is an array and each `update` may add new rounds or update the status of existing ones.

---

## Non-Goals

- Application identifiers, submitted documents → `DriverApplicationOrderAttributes`
- Salary and offer terms → `DriverJobOfferAttributes`
- Job role and requirements → `DriverJobDescriptionAttributes`
