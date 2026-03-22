# HiringJobOfferAttributes Schema

**Container:** `Offer.offerAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Compensation display and filtering in job discovery; application deadline management
**Tag:** hiring employment compensation offer

## Overview

`HiringJobOfferAttributes` extends the v2.1 `Offer` container with commercial terms specific
to a job opportunity. It captures the compensation range, pay period, available openings count,
application deadline, and offer validity window.

The core `Offer` object's `beckn:proposedConsideration` carries the headline compensation figure
(used in search rankings and generic display). This extension provides the full min/max range
and period breakdown required for filtering and detailed display.

## Attachment Points

| Container | Schema | Reason |
|-----------|--------|--------|
| `beckn:offerAttributes` | `HiringJobOfferAttributes` | Commercial terms; needed at selection time |

## Design Rationale

**Range over single figure.** Compensation is expressed as a min/max range rather than a
single value, reflecting the reality of hiring. The core `proposedConsideration` carries the
midpoint or maximum for generic discovery display.

**No eligibility constraints here.** Eligibility (credential requirements) belongs in
`HiringJobResourceAttributes.requirements[]` because it is intrinsic to the role, not to
a commercial offer. This keeps Offer focused on terms and Resource focused on what the role
requires.

## Non-Goals

- Does not capture eligibility or credential requirements (→ `HiringJobResourceAttributes`)
- Does not capture application state (→ `JobApplicationContractAttributes`)
- Does not capture employment benefits beyond base compensation
