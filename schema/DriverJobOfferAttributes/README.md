# DriverJobOfferAttributes Schema

**Container:** `Offer.offerAttributes`
**Version:** 1.0.0
**Trigger Stage:** `HiringStage: OFFER_ISSUED`
**Use Cases:** UC1 and UC2 — communicated via `update`/`on_update` when the operator issues a formal offer
**Tag:** mobility driver-network

---

## Overview

`DriverJobOfferAttributes` carries the commercial and contractual terms of a job offer issued by an operator to a driver. It is attached to a Beckn `Offer` as `offerAttributes` and is communicated once the hiring lifecycle reaches the `OFFER_ISSUED` stage.

This schema is explicitly separated from the job description (`DriverJobDescriptionAttributes`) because offer terms are **context-dependent** — they may vary per candidate, negotiation round, or operator policy, even for the same job listing.

---

## Attachment Point

```
Offer
└── offerAttributes  →  DriverJobOfferAttributes
```

---

## Key Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `salarySpecification` | SalarySpecification | | value + ISO 4217 currency + SalaryFrequency |
| `joiningDate` | date | | ISO 8601 date |
| `shiftAssignment` | string (vocab) | | ShiftType enum (confirmed assignment) |
| `assignedDepot` | string | | Depot / base name |
| `routeType` | string | | CITY, INTERCITY, HIGHWAY, LOCAL |
| `insuranceProvided` | boolean | | |
| `accommodationProvided` | boolean | | |
| `otherBenefits` | string[] | | Free-text additional benefits |
| `probationPeriod` | string | | ISO 8601 duration |
| `contractDuration` | string | | ISO 8601 duration; omit for permanent |
| `offerIssuedAt` | date-time | | |
| `offerValidity` | date-time | | Offer acceptance deadline |
| `remarks` | string | | Additional conditions |

---

## Design Rationale

**Why is salary here and not in DriverJobDescriptionAttributes?**
Salary is a commercial term tied to an offer, not an intrinsic property of the job listing. An operator may advertise a salary range at discovery but specify the confirmed amount only in the formal offer — which may vary by candidate or negotiation. Separating it into `offerAttributes` follows the Beckn v2 principle of commercial isolation.

**Why is SalarySpecification a structured object and not three flat fields?**
The draft schema used `salaryAmount`, `salaryCurrency`, `salaryFrequency` as separate flat fields. The structured `SalarySpecification` (extending `schema:MonetaryAmount`) provides IRI alignment, validation constraints (ISO 4217 pattern for currency), and international reusability across any country or currency.

---

## Non-Goals

- Job requirements, location, role type → `DriverJobDescriptionAttributes`
- Interview scheduling, hiring stage → `DriverHiringFulfillmentAttributes`
- Application IDs, submitted documents → `DriverApplicationOrderAttributes`
