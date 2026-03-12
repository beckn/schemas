# SchemeOrderAttributes Schema

**Container:** `Order.orderAttributes`
**Version:** 1.0.0
**Use Cases:** Agriculture scheme application tracking, DBT disbursement record, government reference management, applicant consent capture
**Tag:** agri-schemes government-welfare dbt disbursement application-tracking consent

---

## Overview

`SchemeOrderAttributes` holds the **transaction-level metadata** for a confirmed scheme
application order. Once a beneficiary has confirmed a scheme application (via the Beckn
`confirm` → `on_confirm` flow), this schema captures:

- The official government application ID assigned by the scheme authority
- The application outcome (approved / rejected) with reason
- The disbursement record (date, amount, government transaction reference)
- The applicant's consent record

This is the record-keeping layer — the provenance trail that allows BAP applications to
show beneficiaries the status of their application and disbursement history.

---

## Attachment Points

| Container | Schema | Rationale |
|-----------|--------|-----------|
| `Order.orderAttributes` | `SchemeOrderAttributes` | Government application IDs, disbursement references, consent timestamps, and rejection reasons are transactional metadata. They are created as a result of the Order lifecycle and do not belong in the scheme description (Item), access policy (Offer), or execution mechanics (Fulfillment). |

---

## Design Rationale

### 1. Two distinct status fields — fulfillment vs. order
There are two status tracking fields in this pack:
- `SchemeFulfillmentAttributes.sfa:applicationStatus` — tracks the **process** status
  from the BPP platform's perspective (agent assignment, document collection, portal submission)
- `SchemeOrderAttributes.sor:schemeApplicationStatus` — tracks the **outcome** status
  from the government scheme authority's perspective (submitted, approved, rejected, disbursed)

These are separate because the BPP may have completed its process (APPLICATION_SUBMITTED)
while the government authority's status is still UNDER_REVIEW. Mixing them into a single
field would lose this important distinction.

### 2. DisbursementRecord as sub-schema (not array)
Scheme disbursements can be installment-based (e.g., PM-KISAN: 3 installments of ₹2,000).
However, modelling this as an array of DisbursementRecord objects was rejected in favour
of a single record with `disbursementInstallment` and `totalInstallments` fields. The
rationale: a Beckn order represents a single confirmed application transaction. Each
installment could generate a new status update event rather than requiring the schema
to manage a list. BAP applications needing full disbursement history should maintain
their own history log from status callbacks.

### 3. Consent capture at Order layer
The DPDP Act (India) and similar regulations require explicit consent before submitting
applicant data to government authorities. The `sor:applicantConsentGiven` and
`sor:consentTimestamp` fields provide a machine-readable consent record. This is order-layer
metadata because consent is given at the point of transaction confirmation.

### 4. Government Application ID vs. BPP Portal Reference
- `SchemeFulfillmentAttributes.sfa:applicationPortalReference` — BPP-internal reference
  generated when the application slot is created on the BPP's own portal.
- `SchemeOrderAttributes.sor:governmentApplicationId` — Official ID assigned by the
  government scheme authority after formal submission. This field is only populated
  after `APPLICATION_SUBMITTED` status is reached.

### 5. Billing and payment in core Order
Core `Order.billing` and core `Payment` are used for any applicant payment records
(e.g., crop insurance premium). These are not redefined here — they are standard Beckn
core constructs. `SchemeOrderAttributes` only adds the domain-specific extension that
core does not cover.

---

## Non-Goals

- **No scheme content.** Descriptions, languages, documents belong in `SchemeItemAttributes`.
- **No eligibility.** Who can apply belongs in `SchemeOfferAttributes`.
- **No process status.** BPP-side process lifecycle belongs in `SchemeFulfillmentAttributes`.
- **No payment mechanics.** Premium collection and payment method are handled by core `Payment`.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `sor:governmentApplicationId` (generalized as `externalReferenceId`) | Any scheme, permit, or approval workflow needs an external authority reference ID; broadly applicable |
| `sor:applicantConsentGiven` + `sor:consentTimestamp` | A generic consent capture pattern is needed for any regulated data-sharing flow; should be a Beckn core concept |
| `sor:rejectionReason` | Generic outcome reason field applicable to any approval/rejection flow |

---

## v1 → v2 Field Migration

| v1 Field | v1 Location | v2 Location |
|----------|-------------|-------------|
| `order.id` | `message.order.id` | Core `Order.beckn:id` (unchanged) |
| `order.fulfillments[].state.descriptor.code` (final status) | `on_status.message.order` | `orderAttributes.sor:schemeApplicationStatus` (government-side) |
| (no explicit field in v1) | Implicit in flow | `orderAttributes.sor:governmentApplicationId` |
| (no explicit field in v1) | Implicit in flow | `orderAttributes.sor:disbursementRecord` |
| (no explicit field in v1) | Implicit in flow | `orderAttributes.sor:applicantConsentGiven` + `sor:consentTimestamp` |
