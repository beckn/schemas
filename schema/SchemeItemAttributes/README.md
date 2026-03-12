# SchemeItemAttributes Schema

**Container:** `Item.itemAttributes`
**Version:** 1.0.0
**Use Cases:** Agriculture scheme discovery, government welfare scheme search, NGO programme cataloguing
**Tag:** agri-schemes government-welfare scheme-discovery

---

## Overview

`SchemeItemAttributes` is the extension schema that adds domain-specific intrinsic metadata
to a Beckn v2 `Item` representing a government or NGO scheme. It describes **what the scheme is**
rather than who can apply (→ `SchemeOfferAttributes`) or how it is delivered (→ `SchemeFulfillmentAttributes`).

This schema supports the UAI / UKI network use case where farmers and rural beneficiaries
discover applicable welfare schemes across multiple providers — central government, state
governments, district bodies, and NGOs — through a single Beckn-enabled application.

---

## Attachment Points

| Container | Schema | Rationale |
|-----------|--------|-----------|
| `Item.itemAttributes` | `SchemeItemAttributes` | Intrinsic identity, type, documentation, and application modes of the scheme as a discoverable catalogue item |

Sub-schemas (`RequiredDocument`, `SchemeBenefitSummary`) are co-located in this folder's
`attributes.yaml` and do not get separate folders — they are only referenced from
within `SchemeItemAttributes`.

---

## Design Rationale

### 1. Eligibility lives in Offer, not Item
Eligibility criteria (age, gender, caste, income, land ownership, etc.) are commercial policy —
they determine who gets access to the offer. In Beckn v2 terms, eligibility is an
`offerAttributes` concern, not an `itemAttributes` concern. The scheme as an item is neutral;
the offer wrapping it carries the access conditions.

### 2. Benefit quantum lives in Offer, not Item
The monetary or coverage amount (₹5 lakhs, 100 days of guaranteed employment) is an offer
parameter that may vary by geography, time period, or eligibility tier. It belongs in
`SchemeOfferAttributes.benefitQuantum`. The item schema carries only a descriptive benefit
summary (`schemeBenefits`) without amounts.

### 3. Languages as Item attribute
The available languages for scheme information and forms are intrinsic to the scheme's
accessibility as a content item, not a commercial policy. They are correctly modelled
here in `itemAttributes` to support language-filtered discovery.

### 4. Scheme type and funding model as required fields
These two fields drive the primary discovery filters in this domain.
A seeker cannot meaningfully compare schemes without knowing whether a scheme is
insurance vs. DBT vs. employment, or whether it is central vs. state vs. NGO-funded.
They are therefore `required` in the schema.

### 5. Official scheme code for cross-referencing
Government schemes often have official codes (e.g., `PM000024` for Central Sector Schemes).
These codes enable interoperability with external government databases, DigiLocker,
and scheme aggregator portals. The field is optional but recommended.

### 6. Application modes support multi-channel discovery
Rural India has diverse digital literacy levels. Surfacing the application modes (online,
offline, agent, CSC) at the item level helps BAP applications filter and present options
appropriate to the beneficiary's capability.

---

## Non-Goals

- **No applicant PII here.** Applicant profile data (name, Aadhaar, income) is collected via
  the `Form` (xinput) mechanism at the offer/fulfillment stage.
- **No monetary amounts.** Benefit coverage amounts belong in `SchemeOfferAttributes`.
- **No eligibility rules.** Who can apply is modelled in `SchemeOfferAttributes.eligibilityCriteria`.
- **No fulfillment state machine.** Application status tracking is in `SchemeFulfillmentAttributes`.
- **No customizations.** Schemes are atomic items with no variants or bundles.

---

## Upstream Candidates

The following attributes are generic enough to consider for promotion to Beckn core:

| Attribute | Rationale |
|-----------|-----------|
| `sia:availableLanguages` | Any content item could declare its language availability; applicable to education, health, advisory verticals |
| `sia:applicationModes` | A generalized "access channel" concept applicable to any service or entitlement vertical |
| `sia:officialPortalUrl` | A generic "canonical reference URL" could be useful for many institutional product types |

---

## v1 → v2 Field Migration

| v1 Field | v1 Location | v2 Location |
|----------|-------------|-------------|
| `tags[code=target-beneficiary-type]` | `item.tags` | `itemAttributes.sia:targetBeneficiaryType` |
| `tags[code=funding-model]` | `item.tags` | `itemAttributes.sia:fundingModel` |
| `tags[code=required-docs]` | `item.tags` | `itemAttributes.sia:requiredDocuments` |
| `tags[code=languages]` | `item.tags` | `itemAttributes.sia:availableLanguages` |
| `descriptor.name` | `item.descriptor.name` | Core `Item.beckn:descriptor.schema:name` (unchanged) |
| `descriptor.short_desc` | `item.descriptor.short_desc` | Core `Item.beckn:descriptor.beckn:shortDesc` |
| `descriptor.long_desc` | `item.descriptor.long_desc` | Core `Item.beckn:descriptor.beckn:longDesc` |
| `category_ids[]` | `item.category_ids` | Core `Item.beckn:category.schema:codeValue` |
| `xinput` | `item.xinput` | Core `Form` object (referenced from `Offer.offerAttributes`) |
