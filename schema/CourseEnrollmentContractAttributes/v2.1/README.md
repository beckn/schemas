# CourseEnrollmentContractAttributes Schema

**Container:** `Contract.contractAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Course enrollment tracking; prerequisite verification; credential issuance pipeline
**Tag:** skilling education enrollment contract verification

## Overview

`CourseEnrollmentContractAttributes` extends the v2.1 `Contract` container with metadata
for a course enrollment transaction. Parties: SKILL_SEEKER (learner) and SKILL_PROVIDER
(training institution). Tracks enrollment reference, cohort assignment, prerequisite
verification outcome, and whether the outcome credential VC is pending issuance.

## Contract Structure
```
Contract {
  parties:     [ { role: "SKILL_SEEKER" }, { role: "SKILL_PROVIDER" } ]
  commitments: [ { refType: "RESOURCE", ref: "<course-resource-id>" } ]
  consideration: [ { type: "MONETARY", status: "AGREED", ... } ]  (if paid course)
  performance: [ { mode: "SERVICE"|"ACCESS", performanceAttributes: {...} } ]
  contractAttributes: { enrollment_reference, cohort_id, prereq_verification, ... }
}
```

## Non-Goals
- Does not capture delivery execution or completion status (→ `CourseDeliveryPerformanceAttributes`)
- Does not capture fee payment structure (→ `CourseConsiderationAttributes`)
