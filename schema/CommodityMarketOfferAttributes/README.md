# CommodityMarketOfferAttributes Schema

**Container:** `Offer.beckn:offerAttributes`
**Version:** 1.0.0
**Use Cases:** Commodity Price Listing, Agricultural Market Price Discovery
**Tag:** agri-commodity-market agri-price-listing agri-offer

---

## Overview

`CommodityMarketOfferAttributes` is the offer-level extension schema for the
**commodity price listing** use case on the Beckn v2 agri-advisory network. It extends
`beckn:Offer.beckn:offerAttributes` with the price range statistics (min/max/average)
observed for a commodity at a specific agricultural market during a given period.

In v1, these prices appeared directly on `item.price.minimum_value`,
`item.price.maximum_value`, and `item.price.estimated_value`. In v2, they move to
the Offer, respecting the core rule that all pricing is commercial metadata.

---

## Attachment Points

- **Primary container:** `beckn:Offer.beckn:offerAttributes`
- **Companion item schema:** `CommodityPriceItemAttributes` (on `beckn:Item.beckn:itemAttributes`)

---

## Design Rationale

### Three price fields (min/max/average) as offer attributes
Agricultural market prices are inherently statistical: a single commodity at a mandi
has a range of prices across different lots, grades, and buyers in a day. This is
fundamentally different from a fixed retail price. The three fields (min, max, average)
together represent this distribution and are necessary for meaningful market intelligence.

The core `beckn:price` on the Offer carries the representative value (average/modal
price) for general compatibility. The extended `minPrice`/`maxPrice`/`averagePrice`
attributes provide the full statistical context.

### Price fields in Offer, NOT Item
In v1, these prices were on `item.price`. This violates the v2 principle that Item
describes the intrinsic commodity (what it is), while Offer describes commercial
terms (what it costs). A single item (Grapes at Nashik APMC) could theoretically
have offers for different date windows at different price levels. Keeping prices in
Offer enables this multi-offer pattern.

### Currency-neutral
All price fields reference `currency` (ISO 4217). The v1 implementation assumed INR
throughout. The v2 schema abstracts this so the same schema works for any agricultural
market worldwide.

### arrivals as offer context
Market arrival volumes provide supply-side context that explains price levels.
This is offer metadata (it relates to the commercial observation) rather than item
metadata (the commodity itself). Including it in offerAttributes allows buyers to
contextualize prices without requiring separate API calls.

### priceVolatilityIndicator as derived enum
The ratio of (maxPrice - minPrice) / minPrice gives a volatility signal. Rather than
forcing all BAPs to compute this, the BPP can supply a pre-computed categorical
indicator (LOW/MODERATE/HIGH/VERY_HIGH), enabling simple UI-level risk signals
for farmers without requiring mathematical literacy.

---

## Non-Goals

- **Does not model forward/futures prices** — only spot market observations.
- **Does not model price trends over time** — trend analysis requires multiple offers
  over time windows, which can be composed by the BAP.
- **Does not model quality certification of the lot** — that is in `itemAttributes.commodityGrade`.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `minPrice` / `maxPrice` / `averagePrice` | Useful in any market/auction domain (livestock, fisheries, commodities exchanges, real estate) as a standard statistical price extension for core `PriceSpecification` |
| `priceVolatilityIndicator` | Could be a generalised `PriceSpecification` extension for any volatile-price domain |

---

## v1 → v2 Field Migration

| v1 Field | v2 Location | Notes |
|----------|-------------|-------|
| `item.price.minimum_value` | `Offer.offerAttributes.minPrice` | Moves from Item to Offer |
| `item.price.maximum_value` | `Offer.offerAttributes.maxPrice` | Moves from Item to Offer |
| `item.price.estimated_value` | `Offer.offerAttributes.averagePrice` + `beckn:price.value` | Dual representation |
| (implied INR) | `Offer.offerAttributes.currency` | Explicit ISO 4217 |
