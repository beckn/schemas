# ServiceContract Schema

**Container:** `Contract.contractAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Service booking confirmation, multi-channel booking tracking
**Tags:** generic-service, on-demand, professional-services

## Overview

ServiceContract defines the contract-time metadata for a confirmed service booking, capturing how the booking was made, what the client requested, and important operational timestamps like when reminders were sent.

## Attachment points

- **Primary:** `Contract.contractAttributes` in on_confirm messages

## Design rationale

ServiceContract records the "metadata of the booking transaction" - which channel was used, what the client said, whether a reminder was sent. This is distinct from the performance (actual execution) and financial (pricing) aspects of the contract.

## Non-goals

This schema does NOT define:
- Financial terms (belongs in Consideration)
- Appointment details (belongs in Performance)
- Resource specifications (belongs in ServiceResource)

## Upstream candidates

Related upstream schemas in Beckn Core:
- Contract (generic Beckn contract)
