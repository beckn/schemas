# DriverCandidateAttributes Schema

**Container:** `Item.itemAttributes`
**Category:** `driver-candidate`
**Version:** 1.0.0
**Use Case:** UC2 — Operator Initiated Driver Recruitment
**Tag:** mobility driver-network

---

## Overview

`DriverCandidateAttributes` represents an identity-lite driver profile published by a driver platform or aggregator for discovery by operators. It is attached to a Beckn `Item` as `itemAttributes` when the catalogue category is `driver-candidate`.

The schema is designed for **progressive disclosure**: only non-PII fields are exposed in `on_discover`. The Driver Passport reference is shared only after explicit driver consent, from the `init` stage onwards.

---

## Attachment Point

```
Item
└── itemAttributes  →  DriverCandidateAttributes
```

---

## Key Properties

| Property | Type | Required | PII | Disclosure Stage |
|---|---|---|---|---|
| `driverId` | string | ✓ | No | on_discover |
| `homeLocation` | NetworkLocation | | Partial (locality only) | on_discover (locality) |
| `availabilityStatus` | string (vocab) | ✓ | No | on_discover |
| `vehicleCategories` | string[] (vocab) | ✓ | No | on_discover |
| `experienceYears` | number | | No | on_discover |
| `trainingSummary` | string[] | | No | on_discover |
| `credentialSummary` | string[] (vocab) | | No | on_discover |
| `reputationSummary` | ReputationSummary | | No | on_discover |
| `passportReference` | string (URI) | | **Yes** | **init+** |
| `lastUpdated` | date-time | | No | on_discover |

---

## Design Rationale

**Why is `passportReference` in itemAttributes but flagged as hidden at discovery?**
The passport reference is a property of the driver's Item (it describes the driver), but exposing it at discovery would let any operator retrieve the full passport without driver consent. The `x-pii-disclosure-stage: init` annotation signals that implementations must omit this field from `on_discover` and `on_select` responses by default.

**Why is `homeLocation` capped at locality resolution at discovery?**
A driver's precise home address is PII. Publishing it in a discovery catalogue would expose it to all operators who run discovery queries. The `homeLocation` at discovery must resolve to city/locality level only; more precise data is available after the driver consents at `init` stage.

**Why credential type labels only (no credential documents)?**
Credential documents (licence number, document URL) are PII. `credentialSummary` is a signal for operator discovery filtering ("does this driver hold a HAZMAT certification?") without exposing the underlying document. Full credential documents are submitted in `DriverApplicationOrderAttributes.submittedDocuments`.

**Why is reputation described as non-centralised?**
Driver Network governance prohibits centralised reputation scoring. `reputationSummary` aggregates signals from verifiable attestations by operators and training institutes; the `ratingAgency` field names the attesting entity.

---

## Non-Goals

- Driving licence number, police verification ID → `DriverApplicationOrderAttributes.submittedDocuments`
- Driver's full name, date of birth, address → Driver Passport (shared via `passportReference`)
- Salary expectations → not modelled (driver-initiated; communicated outside the catalogue)
- Interview scheduling → `DriverHiringFulfillmentAttributes`
