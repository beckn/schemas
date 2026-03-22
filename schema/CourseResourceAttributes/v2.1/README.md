# CourseResourceAttributes Schema

**Container:** `Resource.resourceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Course discovery in any skilling ecosystem (vocational, professional, academic, government schemes)
**Tag:** skilling education training courses credentials

## Overview

`CourseResourceAttributes` extends the v2.1 `Resource` container with intrinsic metadata
about a training course or program. It is domain-generic — applicable to any skilling
vertical without modification.

The schema captures what a course *is*: its level, delivery mode, duration, domain,
location, capacity, prerequisites, schedule, and the credential issued on completion.
Pricing and enrollment terms belong in `CourseOfferAttributes`.

## Key Design Decision: `outcome_credential` in resourceAttributes

The credential issued on course completion (`outcome_credential`) is placed in
`resourceAttributes` — not in `contractAttributes` — because learners search by intended
outcome ("find courses that give me an AWS SAA cert"). This is discovery-time data.
The actual issuance tracking (`credential_issuance_pending`, `issued_credential_ref`)
belongs in the contract and performance schemas.

## Non-Goals

- Does not capture pricing, seats availability, or enrollment deadlines (→ `CourseOfferAttributes`)
- Does not capture enrollment tracking or prerequisite verification outcome (→ `CourseEnrollmentContractAttributes`)
- Does not capture delivery execution, completion status, or actual VC issuance ref (→ `CourseDeliveryPerformanceAttributes`)
