# ServiceResource Schema

**Container:** `Resource.resourceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Professional services discovery, service booking, teleconsultation, maintenance, repair
**Tags:** generic-service, on-demand, professional-services

## Overview

ServiceResource defines the core attributes for a professional service offering, including its unit of measurement, geographic coverage, capacity constraints, and availability schedule. It serves as the foundation for representing any on-demand professional service in the Beckn network.

## Attachment points

- **Primary:** `Catalog.resources[].resourceAttributes` in on_discover messages
- **Secondary:** Referenced in `Offer.resourceIds` for binding offers to resources

## Design rationale

The schema is designed to be protocol-agnostic and applicable across multiple service verticals (healthcare, agriculture, cleaning, consulting, etc.). It captures the essential business logic needed for service discovery and matching without imposing domain-specific constraints.

Key design decisions:
- Service unit is flexible (hour, session, visit, unit, kg, day, piece)
- Coverage area supports both geographic regions and radius-based coverage
- Availability is defined at the weekly level to support recurring schedules
- Capacity is tracked both daily and weekly for resource planning

## Non-goals

This schema does NOT define:
- Pricing information (belongs in Consideration)
- Actual booking/fulfillment details (belongs in Performance)
- Contract terms (belongs in Contract)
- Service quality metrics (belongs in custom extension schemas)

## Upstream candidates

Related upstream schemas in Beckn Core:
- Resource (generic Beckn resource)
- Descriptor (shared by all resources for name/description)
