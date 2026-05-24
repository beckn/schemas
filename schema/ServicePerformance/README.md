# ServicePerformance Schema

**Container:** `Performance.performanceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Appointment confirmation, service fulfillment tracking, location management
**Tags:** generic-service, on-demand, professional-services

## Overview

ServicePerformance defines the execution-time details for a service contract, capturing when the appointment is confirmed, where it will happen, who has confirmed completion, and whether follow-up is needed.

## Attachment points

- **Primary:** `Contract.performance[].performanceAttributes` in on_confirm messages
- **Relationship:** Each Performance is bound to commitments via `Performance.commitmentIds`

## Design rationale

ServicePerformance is where the "actual execution details" live - confirmed time, location, completion status. This is distinct from the booking metadata (ServiceContract) and financial terms (ServiceConsideration).

## Non-goals

This schema does NOT define:
- Financial terms (belongs in Consideration)
- Booking metadata (belongs in ServiceContract)
- Resource specifications (belongs in ServiceResource)

## Upstream candidates

Related upstream schemas in Beckn Core:
- Performance (generic Beckn performance)
