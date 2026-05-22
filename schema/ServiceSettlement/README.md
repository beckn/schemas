# ServiceSettlement Schema

**Container:** `Settlement.settlementAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Payment confirmation, settlement tracking, receipt management
**Tags:** generic-service, on-demand, professional-services

## Overview

ServiceSettlement records payment settlement details for a confirmed service contract, tracking whether the provider has received payment, when it was recorded, and the receipt reference.

## Attachment points

- **Primary:** `Contract.settlements[].settlementAttributes` in on_status messages

## Design rationale

ServiceSettlement is separate from the pricing terms (ServiceConsideration) because settlement happens at a different time in the transaction lifecycle. Consideration is agreed at confirmation time, but settlement is updated in status messages as payments are processed.

## Non-goals

This schema does NOT define:
- Pricing or payment methods (belongs in ServiceConsideration)
- Bank or payment processor details (implementation-specific)
- Refund processing (domain-specific)

## Upstream candidates

Related upstream schemas in Beckn Core:
- Settlement (generic Beckn settlement)
