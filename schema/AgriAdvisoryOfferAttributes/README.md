# AgriAdvisoryOfferAttributes Schema

**Container:** `Offer.beckn:offerAttributes`
**Version:** 1.0.0
**Use Cases:** Crop Disease Advisory (UC1 paid variant), Weather Forecast Data (UC3)
**Tag:** agri-advisory agri-offer agri-digital-content

---

## Overview

`AgriAdvisoryOfferAttributes` is the offer-level extension schema for digital agri
advisory services on the Beckn v2 network. It extends `beckn:Offer.beckn:offerAttributes`
with commercial policy metadata specific to knowledge and weather advisory products:
access model, content license, access validity, and cancellation/refund policy.

This schema is shared by UC1 (disease/crop advisory — paid variant) and UC3 (weather
data/forecast). Free UC1 advisories (open knowledge) use `pricingModel: FREE` and
`accessType: OPEN_ACCESS`. Paid services set pricing via core `beckn:price` (PriceSpecification).

---

## Attachment Points

- **Primary container:** `beckn:Offer.beckn:offerAttributes`
- **Sub-schemas (same folder):** `CancellationPolicy`
- **Does NOT apply to UC2** (commodity price listing). That use case uses
  `CommodityMarketOfferAttributes` instead.

---

## Design Rationale

### pricingModel vs core beckn:price
Core `beckn:price` carries the monetary value (e.g., INR 30). `pricingModel` is a
categorical label (FREE / PAID / FREEMIUM) that enables filtering without needing to
parse the price — a BAP can filter "show free items" with a single enum comparison.

### accessType clarifies post-purchase entitlement
Without `accessType`, a buyer cannot determine whether paying grants perpetual access,
time-limited access, or API credentials. In the v1 weather data guide, the order flow
grants download access to a PDF report — this maps to `ONE_TIME_PURCHASE`. Future
subscription models can use `SUBSCRIPTION_ACCESS`.

### contentLicense for redistribution control
Advisory content from academic/government sources often has specific redistribution
terms (e.g., "for personal use only", "CC BY-SA"). The `contentLicense` attribute
enables data providers to declare these terms in machine-readable form for
compliance checking by BAP platforms.

### CancellationPolicy as a sub-schema
In the v1 weather data guide, the flow explicitly includes cancellation and refund
policy presentation to the buyer. This is modeled as a structured sub-schema rather
than free text, enabling automated policy display and rule-based enforcement.

### No tax or regulatory declarations
In the v1 guide, no GST or VAT declarations appear for advisory services. If a future
network mandate requires invoice-level tax attributes, those would go in
`beckn:Invoice.beckn:invoiceAttributes`, not in Offer.

---

## Non-Goals

- **Does not model commodity price ranges** — those are in `CommodityMarketOfferAttributes`.
- **Does not model subscription billing cycles** — recurring schedules are out of scope per clarifications.
- **Does not model platform/operator fees** — those are order-level concerns in core `Payment`.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `pricingModel` | Universal for any digital content domain (e-learning, media, API services) |
| `accessType` | Universal for knowledge/data/media offers; candidate for a cross-domain "digital offer" extension |
| `contentLicense` | Reusable in any digital content vertical |
| `CancellationPolicy` | Useful across healthcare consultations, e-learning, media subscriptions |

---

## v1 → v2 Field Migration

| v1 Field | v2 Location | Notes |
|----------|-------------|-------|
| (no explicit pricing model in v1 free advisory) | `offerAttributes.pricingModel` = `FREE` | Implicit in v1, explicit in v2 |
| `item.price` (weather guide) | `beckn:price.value` + `beckn:price.currency` | Core PriceSpecification |
| (cancellation/refund terms in UI copy) | `offerAttributes.cancellationPolicy` | Structured, machine-readable |
| (access validity implied by delivery) | `offerAttributes.accessValidityPeriod` | Explicit duration |
