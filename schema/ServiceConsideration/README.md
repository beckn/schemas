# ServiceConsideration Schema

**Container:** `Consideration.considerationAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Service pricing, payment terms, multi-currency billing
**Tags:** generic-service, on-demand, professional-services

## Overview

ServiceConsideration defines the financial terms of a service contract, including pricing per unit, total amount, accepted payment methods, and payment method selection.

## Attachment points

- **Primary:** `Contract.consideration[].considerationAttributes` in on_confirm messages

## Design rationale

ServiceConsideration is where financial details live - price per unit, total cost, which payment methods are accepted, and which one was chosen. This is separate from the service itself (ServiceResource), the booking terms (ServiceOffer), and the execution details (ServicePerformance).

## Non-goals

This schema does NOT define:
- Refund policies (belongs in ServiceOffer or domain-specific extensions)
- Discounts (belongs in domain-specific extensions)
- Payment processor details (implementation-specific)

## Upstream candidates

Related upstream schemas in Beckn Core:
- Consideration (generic Beckn consideration)
