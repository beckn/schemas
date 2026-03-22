# CourseOfferAttributes Schema

**Container:** `Offer.offerAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Course fee display and filtering; enrollment window management; government-funded scheme discovery
**Tag:** skilling education courses offer pricing enrollment

## Overview

`CourseOfferAttributes` extends the v2.1 `Offer` container with commercial and availability
terms for a training course. Captures whether a course is free, subsidised, government-funded
or paid; how many seats remain; and when enrollment closes.

## Non-Goals
- Does not capture course content or prerequisites (→ `CourseResourceAttributes`)
- Does not capture payment schedule or fee structure details (→ `CourseConsiderationAttributes`)
- Does not capture enrollment status (→ `CourseEnrollmentContractAttributes`)
