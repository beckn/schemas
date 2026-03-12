# SchemeFulfillmentAttributes Schema

**Container:** `Fulfillment.deliveryAttributes`
**Version:** 1.0.0
**Use Cases:** Agriculture scheme application lifecycle, agent-assisted enrollment, DBT benefit delivery, crop insurance claim tracking
**Tag:** agri-schemes government-welfare dbt agent-assisted fulfillment-status

---

## Overview

`SchemeFulfillmentAttributes` models **how** a scheme benefit reaches the beneficiary —
the delivery mechanism, the application submission process, the assigned agent, and
the domain-specific lifecycle status codes for the application.

This is the execution layer. It does not describe what the scheme is (→ `SchemeItemAttributes`),
who is eligible (→ `SchemeOfferAttributes`), or what government reference IDs are assigned
post-disbursement (→ `SchemeOrderAttributes`).

---

## Attachment Points

| Container | Schema | Rationale |
|-----------|--------|-----------|
| `Fulfillment.deliveryAttributes` | `SchemeFulfillmentAttributes` | The delivery type (DBT, subsidized service, employment), submission mode, agent assignment, and application status codes are all execution-model properties belonging in Fulfillment. |

---

## Design Rationale

### 1. Single-stage fulfillment model
Per the domain clarifications, scheme fulfillment is modelled as single-stage. The lifecycle
(booking → agent assignment → documents → application → disbursement) is tracked via the
`sfa:applicationStatus` enum rather than as separate Fulfillment stages. This keeps the
model simple while still providing rich status visibility.

### 2. Agent-assisted fulfillment as first-class delivery type
The v1 guide shows a pattern where a beneficiary books a field agent who then submits the
scheme application on their behalf. This is modelled as `sfa:schemeDeliveryType = AGENT_ASSISTED_APPLICATION`.
The `sfa:agentDetails` sub-schema captures the assigned agent's details, mirroring the v1
`fulfillment.agent` object.

### 3. Status codes derived from v1 state machine
The v1 guide shows the following status codes in `fulfillment.state.descriptor.code`:
`Booking-Confirmed`, `Agent-Assigned`, `Application-Initiated`. The v2 schema expands this
into a complete lifecycle enum (`sfa:ApplicationStatus`) covering the full arc from booking
through disbursement and failure recovery, making the state machine explicit and indexable.

### 4. Disbursement mode vs. delivery type
`sfa:schemeDeliveryType` describes the *category* of benefit delivery (DBT, subsidized service,
employment, etc.). `sfa:disbursementMode` describes the *channel* for the monetary transfer
(NEFT, RTGS, cheque). These are separated because a DBT scheme can disburse via multiple
channel types, and not all delivery types have a monetary disbursement channel.

### 5. Customer details remain in core Fulfillment
The v1 `fulfillment.customer.person.name` and `fulfillment.customer.contact.phone` fields
are modelled in the **core** `Fulfillment` container (as `beckn:customer`). They are not
duplicated here. The schema extension only adds domain-specific attributes that core does
not cover.

---

## Non-Goals

- **No monetary transaction records.** Government application IDs and disbursement reference
  numbers belong in `SchemeOrderAttributes`.
- **No eligibility rules.** Who can apply is `SchemeOfferAttributes`.
- **No scheme content.** Documents required and scheme descriptions are `SchemeItemAttributes`.
- **No multi-stage logistics.** Scheme fulfillment is single-stage; complex multi-hop logistics
  are out of scope for this vertical.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `sfa:applicationStatus` (generic form) | A generic "service application lifecycle status" enum (submitted, under-review, approved, rejected, closed) could be useful for any entitlement-based service — healthcare authorization, permit applications, etc. |
| `sfa:agentDetails` | A generic "assigned service agent" sub-schema is broadly applicable to any B2B2C service vertical |
| `sfa:applicationPortalReference` | A generic "third-party portal reference ID" field could be a standard Beckn core concept for any cross-system application tracking |

---

## v1 → v2 Field Migration

| v1 Field | v1 Location | v2 Location |
|----------|-------------|-------------|
| `fulfillment.type` | `provider.fulfillments[].type` / `order.fulfillments[].type` | `fulfillmentAttributes.sfa:schemeDeliveryType` |
| `fulfillment.state.descriptor.code` | `order.fulfillments[].state.descriptor.code` | `fulfillmentAttributes.sfa:applicationStatus` |
| `fulfillment.customer.person.name` | `order.fulfillments[].customer.person.name` | Core `Fulfillment.beckn:customer.person.schema:name` |
| `fulfillment.customer.contact.phone` | `order.fulfillments[].customer.contact.phone` | Core `Fulfillment.beckn:customer.contact.schema:telephone` |
| `fulfillment.agent.organization.descriptor.name` | `order.fulfillments[].agent.organization.descriptor.name` | `fulfillmentAttributes.sfa:agentDetails.sfa:agentOrganization` |
| `fulfillment.agent.organization.descriptor.code` | `order.fulfillments[].agent.organization.descriptor.code` | `fulfillmentAttributes.sfa:agentDetails.sfa:agentOrganizationCode` |
| `fulfillment.agent.person.name` | `order.fulfillments[].agent.person.name` | `fulfillmentAttributes.sfa:agentDetails.sfa:agentName` |
| `fulfillment.agent.contact.phone` | `order.fulfillments[].agent.contact.phone` | `fulfillmentAttributes.sfa:agentDetails.sfa:agentContact` |
