# CourseDeliveryPerformanceAttributes Schema

**Container:** `Performance.performanceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Course delivery tracking; completion status; VC issuance reference
**Tag:** skilling education delivery performance completion

## Overview

`CourseDeliveryPerformanceAttributes` extends the v2.1 `Performance` container with the
execution state of course delivery. For online/self-paced courses, mode is `ACCESS`; for
instructor-led courses, mode is `SERVICE`.

Captures the delivery URL, session schedule, completion criteria, current completion status,
and the reference to the VC issued upon successful completion.

## Non-Goals
- Does not capture learner-specific attendance records (PII concern; application layer)
- Does not capture assessment scores (PII concern)
- Does not capture the credential payload itself (→ learner wallet)
