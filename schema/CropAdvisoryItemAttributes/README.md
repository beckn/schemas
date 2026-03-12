# CropAdvisoryItemAttributes Schema

**Container:** `Item.beckn:itemAttributes`
**Version:** 1.0.0
**Use Cases:** Crop Disease Control, Spray Schedule Advisory, Pest Forecast
**Tag:** agri-crop-advisory agri-disease-control agri-spray-schedule

---

## Overview

`CropAdvisoryItemAttributes` is the item-level extension schema for the **Agri Advisory**
vertical on the Beckn v2 generalized network (domain: `advisory:agri`, formerly `advisory:uki`
in v1). It describes the intrinsic attributes of a knowledge advisory item — an atomic,
digital content asset such as an article, video, PDF, or spray schedule recommendation
addressing crop disease control, pest forecasts, or spray schedules.

This schema serves Use Case 1 of the UAI (Universal Agri Informatics) network.

---

## Attachment Points

- **Primary container:** `beckn:Item.beckn:itemAttributes`
- **Sub-schemas (same folder):** `CropContext`, `ExpertCredentials`, `CropGrowthStage`

This schema does NOT extend `offerAttributes` (pricing lives in `AgriAdvisoryOfferAttributes`)
or `fulfillmentAttributes` (delivery mode and location live in `AgriAdvisoryFulfillmentAttributes`).

---

## Design Rationale

### Advisory category as top-level enum
The v1 network encoded advisory type inside `category.descriptor.code` (e.g.,
`"disease-control"`, `"spray-schedule"`, `"pest-forecast"`). In v2 this moves into
`itemAttributes.advisoryCategory` as a typed enum, enabling typed filtering without
relying on free-text category code matching. The `beckn:category` field on core `Item`
is retained for broader domain categorisation.

### CropContext as a sub-schema
In v1, crop context (crop name, growth stage, soil type, irrigation type, disease name)
was encoded as intent-only tags in the `search` message. In v2, these same attributes
are promoted to first-class structured fields in `CropContext`, which can appear:
- In the **search intent** (to personalise results)
- On the **item** itself (indicating which crop/context the advisory was generated for)

This dual use avoids information loss when catalogues store pre-generated advisories.

### Content format as itemAttributes, not fulfillmentAttributes
The content type (PDF, VIDEO, TEXT) is an intrinsic property of the advisory item —
it describes what the item IS, not how it gets delivered. In contrast,
`AgriAdvisoryFulfillmentAttributes.deliveryMode` describes HOW the item is made
accessible (via download link, API, SMS, etc.). A single item may be available in
multiple delivery modes.

### Languages in itemAttributes
Languages denote what content exists, not user preference. A BAP can filter items
by available language at discovery time. This is item-intrinsic metadata, not offer
or fulfillment metadata.

### No price in itemAttributes
In v1, disease control advisories were typically free (no `price` field on item).
Pricing (FREE vs PAID, cancellation policy, access type) lives exclusively in
`AgriAdvisoryOfferAttributes`, respecting the core v2 rule that Item = intrinsic
description, Offer = commercial terms.

### No location in itemAttributes
Advisory items themselves are location-agnostic; they are knowledge content.
Location specificity is relevant only for pest forecast queries (where a farm GPS
is the search parameter). That location is expressed in
`AgriAdvisoryFulfillmentAttributes.targetLocation` — the place for which the
forecast applies — not on the item.

---

## Non-Goals

- **Does not model the farmer's identity or farm profile.** User/farm profiles are
  outside the scope of Beckn schema packs.
- **Does not model payment terms.** Payment and access model live in
  `AgriAdvisoryOfferAttributes`.
- **Does not model delivery logistics.** Content delivery details live in
  `AgriAdvisoryFulfillmentAttributes`.
- **Does not model market prices.** Price listing for commodities is in
  `CommodityPriceItemAttributes`.
- **Does not model weather forecasts.** Weather data is in
  `WeatherForecastItemAttributes`.

---

## Upstream Candidates

The following attributes are generic enough to be promoted to Beckn core or a
cross-domain "knowledge/media" extension:

| Attribute | Rationale |
|-----------|-----------|
| `contentMimeType` | Any digital-content domain (e-learning, health docs) needs MIME type |
| `contentUrl` | Universal for any digital item |
| `languages` | Already partially covered in core via `beckn:inLanguage`; candidate for promotion |
| `contentDurationSeconds` | Relevant to all media items (video, audio, podcasts) |

---

## v1 → v2 Field Migration

| v1 Field | v2 Location | Notes |
|----------|-------------|-------|
| `context.domain` = `advisory:uki` | `beckn:networkId` | Domain becomes network context |
| `category.descriptor.code` | `itemAttributes.advisoryCategory` | Typed enum replaces free-text code |
| `item.tags[languages].list[].value` | `itemAttributes.languages` | First-class array, ISO 639-1 |
| `item.descriptor.media[].mimetype` | `itemAttributes.contentMimeType` | Per-item MIME type |
| `item.descriptor.media[].url` | `itemAttributes.contentUrl` | Per-item content URL |
| `intent.tags[crop-details]` | `itemAttributes.cropContext` | Structured sub-schema |
| `intent.tags[health-information].disease-name` | `itemAttributes.cropContext.diseaseName` | Part of CropContext |
| `item.rating` | `beckn:rating.beckn:ratingValue` | Core Item rating |
