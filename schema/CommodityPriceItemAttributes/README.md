# CommodityPriceItemAttributes Schema

**Container:** `Item.beckn:itemAttributes`
**Version:** 1.0.0
**Use Cases:** Commodity Price Listing, Market Price Discovery
**Tag:** agri-price-listing agri-commodity agri-mandi

---

## Overview

`CommodityPriceItemAttributes` is the item-level extension schema for the **commodity
price listing** use case on the Beckn v2 agri-advisory network. Each item instance
represents the price data for a specific commodity at a specific agricultural market
(mandi/APMC) during a given observation period.

In v1, multiple mandi price observations for the same commodity were returned as
separate `items[]` entries in the catalog, each associated with a `location_id`. In v2,
this same pattern is retained: each item = one mandi's price record. The price ranges
(min/max/average) are modeled in the companion `CommodityMarketOfferAttributes` schema
on the `Offer`, preserving the v2 principle that pricing is commercial and belongs in
Offer, not Item.

---

## Attachment Points

- **Primary container:** `beckn:Item.beckn:itemAttributes`
- **Companion offer schema:** `CommodityMarketOfferAttributes` (on `beckn:Offer.beckn:offerAttributes`)
- **Companion fulfillment schema:** `AgriAdvisoryFulfillmentAttributes` (search location and date range)

---

## Design Rationale

### Why price ranges are NOT in itemAttributes
In v1, price (`minimum_value`, `maximum_value`, `estimated_value`) was embedded directly
in `item.price`. In v2, the core rule is that pricing is **commercial metadata** and must
live in `Offer.offerAttributes`. This enforces a clean separation: `itemAttributes`
describes the commodity and mandi (the "what" and "where"), while `offerAttributes`
describes the price range observed (the commercial observation).

This separation also allows a single item (one commodity/mandi pair) to carry multiple
offers covering different time windows — useful when historical price data is queried.

### One item per mandi
The v1 pattern of using `location_ids` to associate an item with multiple provider
locations is simplified in v2. Each item represents exactly one mandi. This keeps
item attributes lean and makes location-based filtering straightforward using
`beckn:availableAt` (GeoJSON) on the core Item.

### mandiName and mandiCode as item attributes
The mandi is intrinsic to the price observation. Different mandi observations of the
same commodity have fundamentally different identities (e.g., Grapes at Nashik APMC ≠
Grapes at Pune APMC). Therefore mandi identification belongs in `itemAttributes`, not
in `offerAttributes`.

### Commodity variety, grade, size as item attributes
These are intrinsic properties of the agricultural lot being priced. They describe
"which grapes" rather than "at what price". They remain stable regardless of which
offer (time window, data source) is applied. Thus they belong in `itemAttributes`.

### priceObservationPeriod in itemAttributes
The observation period is a property of the data item itself (it defines what the
item IS — a price snapshot for a specific date range). It is not a commercial policy
decision. Contrast with `beckn:availability` on core Item, which is about item
availability for ordering.

---

## Non-Goals

- **Does not model price ranges** (min/max/average) — those live in `CommodityMarketOfferAttributes`.
- **Does not model the farmer's search location radius** — that's a fulfillment attribute.
- **Does not model commodity forecasts** — only observed/reported market prices.
- **Does not model futures or forward contracts** — only spot market prices.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `commodityVariety` | Useful in any agri-commodity domain (livestock, fisheries, horticulture) |
| `commodityGrade` | Applicable to any graded commodity (minerals, textiles, agri) |
| `priceObservationPeriod` | Any time-series data item could use a structured observation period |

---

## v1 → v2 Field Migration

| v1 Field | v2 Location | Notes |
|----------|-------------|-------|
| `item.descriptor.name` | `beckn:descriptor.schema:name` | Unchanged |
| `item.price.minimum_value` | `Offer.offerAttributes.minPrice` | Moves to CommodityMarketOfferAttributes |
| `item.price.maximum_value` | `Offer.offerAttributes.maxPrice` | Moves to CommodityMarketOfferAttributes |
| `item.price.estimated_value` | `Offer.offerAttributes.averagePrice` | Moves to CommodityMarketOfferAttributes |
| `item.location_ids[]` | `beckn:availableAt[].geo` | GeoJSON location on core Item |
| `provider.locations[id].city` | `beckn:availableAt[].address.addressLocality` | Core Location address |
| `intent.item.tags[item-details].variety` | `itemAttributes.commodityVariety` | First-class attribute |
| `intent.item.tags[item-details].grade` | `itemAttributes.commodityGrade` | First-class attribute |
| `intent.item.tags[item-details].size` | `itemAttributes.commoditySize` | First-class attribute |
| `intent.fulfillment.stops[price-location].time.range` | `itemAttributes.priceObservationPeriod` | Structured TimePeriod |
