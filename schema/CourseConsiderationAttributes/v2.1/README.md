# CourseConsiderationAttributes Schema

**Container:** `Consideration.considerationAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Course fee structure; government-funded scheme payment; income-share agreements
**Tag:** skilling education consideration fee payment

## Overview

`CourseConsiderationAttributes` extends the v2.1 `Consideration` container with value-
exchange specifics for a course enrollment. The core `Consideration` object carries the
monetary amount; this extension provides the fee structure context — how it's categorised,
when it's due, whether it's subsidised, and what the refund terms are.

This schema is what makes the difference between a course that says "₹4,999" and one
that says "₹4,999 — government-funded, no upfront payment, refundable if cancelled 7 days
before start". That context is essential for a trustworthy skilling marketplace.

## Non-Goals
- Does not carry the monetary amount itself (→ core `Consideration.beckn:amount`)
- Does not carry payment gateway transaction details (→ `settlementAttributes` if needed)
