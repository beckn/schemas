# ServiceOffer Schema

**Container:** `Offer.offerAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Service booking terms, quantity constraints, cancellation policies
**Tags:** generic-service, on-demand, professional-services

## Overview

ServiceOffer defines the commercial and operational terms for a service offering, including quantity constraints, advance booking requirements, and cancellation policies. Offers bind resources to the terms under which they are available for booking.

## Attachment points

- **Primary:** `Catalog.offers[].offerAttributes` in on_discover messages
- **Relationship:** Offers reference resources via `Offer.resourceIds`

## Design rationale

ServiceOffer complements ServiceResource by defining the "if you want to book this resource, here are the terms" information. This separation of concerns keeps resource metadata (capabilities, schedule) separate from commercial terms (quantities, policies).

## Non-goals

This schema does NOT define:
- Pricing (belongs in Consideration)
- Service details (belongs in ServiceResource)
- Actual fulfillment terms (belongs in Contract/Performance)

## Upstream candidates

Related upstream schemas in Beckn Core:
- Offer (generic Beckn offer)
