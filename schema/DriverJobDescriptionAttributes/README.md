# DriverJobDescriptionAttributes Schema

**Container:** `Item.itemAttributes`
**Category:** `driver-job`
**Version:** 1.0.0
**Use Cases:** UC1 (Driver/Aggregator Initiated Job Application), UC2 (Operator publishes jobs)
**Tag:** mobility driver-network

---

## Overview

`DriverJobDescriptionAttributes` describes a driver job listing published by an operator or hiring entity on the Driver Network. It is attached to a Beckn `Item` as `itemAttributes` when the item's catalogue category is `driver-job`.

This schema covers the **intrinsic job description only** — role, location, requirements, working conditions, and operator trust signals. Commercial offer terms (salary, benefits confirmation, joining date) are modelled separately in `DriverJobOfferAttributes`.

---

## Attachment Point

```
Item
└── itemAttributes  →  DriverJobDescriptionAttributes
```

---

## Key Properties

| Property | Type | Required | Notes |
|---|---|---|---|
| `roleType` | string (vocab) | ✓ | DriverRoleType enum |
| `vehicleCategoriesRequired` | string[] (vocab) | | DriverVehicleCategory enum |
| `jobLocation` | NetworkLocation | ✓ | schema:jobLocation |
| `employmentType` | string (vocab) | ✓ | EmploymentType enum |
| `shiftType` | string (vocab) | | ShiftType enum |
| `workingHours` | string | | Human-readable hours description |
| `contractDuration` | string | | ISO 8601 duration; omit for permanent roles |
| `minExperienceYears` | number | | Minimum years required |
| `requiredCredentials` | string[] (vocab) | | CredentialType enum |
| `requiredTraining` | string[] | | Training labels |
| `benefitsSummary` | string[] | | Catalogue-visible summary; full terms in offer |
| `operatorReputation` | ReputationSummary | | Attestation-based rating |
| `applicationInstructions` | string | | Revealed at on_select only |

---

## Design Rationale

**Why is salary not here?** Salary is a commercial term that varies per offer context (negotiation, location premium, urgency). It belongs in `DriverJobOfferAttributes`, which is communicated at the `OFFER_ISSUED` fulfillment stage.

**Why is `applicationInstructions` in this schema but hidden at discovery?** It is intrinsic to the job (set by the operator), but only relevant once a candidate has selected the job. It is returned in `on_select`, not in `on_discover`.

**Why are `requiredCredentials` vocab terms and not free text?** Interoperability requires that credential types be consistently identified across platforms. The `CredentialType` vocab provides the standard set; jurisdiction-specific licence classes are a network-layer validation concern.

---

## Non-Goals

- Salary, joining date, shift confirmation → `DriverJobOfferAttributes`
- Interview scheduling, driving tests → `DriverHiringFulfillmentAttributes`
- Application IDs, submitted documents → `DriverApplicationOrderAttributes`
- Driver training programmes → separate `driver-training` catalogue category
