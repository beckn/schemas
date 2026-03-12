# SchemeOfferAttributes Schema

**Container:** `Offer.offerAttributes`
**Version:** 1.0.0
**Use Cases:** Agriculture scheme eligibility matching, benefit comparison, welfare scheme discovery
**Tag:** agri-schemes government-welfare eligibility benefit-discovery

---

## Overview

`SchemeOfferAttributes` models the **commercial and access policy** of a scheme offer —
who is eligible to apply, what they receive, and over what time window.

This is the most complex schema in the pack, reflecting the domain reality that government
schemes have highly varied eligibility rules across demographic, economic, professional,
identity, educational, and residency dimensions. The v1 implementation encoded all of these
as flat tag lists. The v2 schema structures them into typed sub-objects for machine-readable
matching and filtering.

---

## Attachment Points

| Container | Schema | Rationale |
|-----------|--------|-----------|
| `Offer.offerAttributes` | `SchemeOfferAttributes` | Eligibility is commercial policy — it determines access. Benefit quantum is the price of the offer to society. Application window is offer validity. All are offer-layer concerns. |

---

## Design Rationale

### 1. Eligibility is Offer-layer, not Item-layer
In Beckn v2, the `Item` represents the intrinsic thing (the scheme). The `Offer` wraps it
with commercial terms. Eligibility rules are access conditions — analogous to "eligible
customer segment" in retail, or "eligibility for a tariff" in energy. They belong in Offer.

A single scheme Item can theoretically have multiple Offer wrappers with different eligibility
tiers (e.g., general vs. priority households getting different benefit amounts) — this is the
power of separating Item from Offer.

### 2. Structured eligibility sub-objects instead of flat tags
The v1 used a flat key-value tag list under `demographic-details`, `personal-details`,
`economic-details`, `employment-details` tags. In v2, these are modelled as typed sub-schemas
(`DemographicCriteria`, `EconomicCriteria`, etc.) so that BAP applications can:
- Build structured eligibility questionnaires
- Perform machine-readable eligibility pre-screening
- Apply typed filters on the discovery index

### 3. AdditionalCriteria escape hatch for rare rules
Not all eligibility rules can be structured. The `soa:additionalCriteria` array provides a
typed key-value escape hatch (matching v1 tag codes like `CT0001TU`) for rare
scheme-specific conditions without polluting the structured sub-schemas.

### 4. Benefit quantum at Offer, not Item
The monetary amount (₹5 lakhs for PM-JAY) is an offer parameter, not an intrinsic property
of the scheme. Different states may offer different premium rates or coverage limits for the
same central scheme. Keeping quantum in Offer allows this variation.

### 5. Eligibility form (xInput equivalent)
The v1 `xinput` mechanism — where BPP returns a form URL for detailed eligibility collection
— is preserved as `soa:eligibilityForm` in the offer attributes. This enables the same
progressive disclosure pattern in v2.

### 6. Country-specificity
Caste categories (SC/ST/OBC), ration card types (BPL/AAY/PHH), and identity documents
(Aadhaar, SECC) are India-specific. They are namespaced under the `soa:` prefix and
documented clearly. For international deployments, these sub-schemas should be replaced
with jurisdiction-appropriate constructs.

---

## Non-Goals

- **No scheme content.** Scheme descriptions, documents, and languages belong in `SchemeItemAttributes`.
- **No fulfillment logistics.** Agent assignment, DBT/fulfillment modes belong in `SchemeFulfillmentAttributes`.
- **No order lifecycle.** Application reference IDs and disbursement belong in `SchemeOrderAttributes`.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `soa:maxBeneficiaries` | Any quota-limited scheme or allocation-based offer could use this |
| `soa:eligibilityForm` | A generic "contextual form collection" pattern could be a core composability feature |
| `soa:benefitQuantum.soa:benefitPeriod` | A temporal scope for benefits (per-episode, per-annum) is a broadly applicable Offer concept |

---

## v1 → v2 Field Migration

| v1 Field | v1 Location | v2 Location |
|----------|-------------|-------------|
| `tags[code=demographic-details][code=gender]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:demographicCriteria.soa:gender` |
| `tags[code=demographic-details][code=caste-category]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:demographicCriteria.soa:casteCategory` |
| `tags[code=personal-details][code=differently-abled]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:demographicCriteria.soa:differentlyAbled` |
| `tags[code=personal-details][code=land-owner]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:economicCriteria.soa:landOwnership` |
| `tags[code=personal-details][code=girl-children]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:demographicCriteria.soa:minGirlChildren` |
| `tags[code=economic-details][code=ration-card-type]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:economicCriteria.soa:rationCardType` |
| `tags[code=economic-details][code=business-support-required]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:professionalCriteria.soa:businessSupportType` |
| `tags[code=employment-details][code=job-type]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:professionalCriteria.soa:occupationType` |
| `tags[code=employment-details][code=enterprise-category]` | `message.intent.tags` | `offerAttributes.soa:eligibilityCriteria.soa:professionalCriteria.soa:enterpriseCategory` |
| `tags[code=demographic-eligibility]` | `item.tags` | `offerAttributes.soa:eligibilityCriteria.soa:residencyCriteria.soa:statesOfResidence` |
| `tags[code=additional-eligibility]` | `item.tags` | `offerAttributes.soa:eligibilityCriteria.soa:additionalCriteria[]` |
| `item.xinput` | `item.xinput` | `offerAttributes.soa:eligibilityForm` |
| (benefit amount — not in v1 schema, was in descriptive text) | `item.descriptor.long_desc` | `offerAttributes.soa:benefitQuantum.soa:monetaryAmount` |
