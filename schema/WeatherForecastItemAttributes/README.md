# WeatherForecastItemAttributes Schema

**Container:** `Item.beckn:itemAttributes`
**Version:** 1.0.0
**Use Cases:** Weather Forecast Data, Agro-Advisory, Seasonal Outlook, Historical Weather Data
**Tag:** agri-weather-forecast agri-forecast-data agri-advisory

---

## Overview

`WeatherForecastItemAttributes` is the item-level extension schema for the **weather data
and forecast** use case on the Beckn v2 agri-advisory network. Each item represents a
distinct weather intelligence product — a purchasable or discoverable weather data service
deliverable (e.g., a 14-day hyperlocal forecast, a seasonal outlook, or historical data
access).

This schema covers Use Case 3 of the UAI (Universal Agri Informatics) network.

---

## Attachment Points

- **Primary container:** `beckn:Item.beckn:itemAttributes`
- **Sub-schemas (same folder):** `WeatherDataPoint` (enum), `WeatherOutputFormat` (enum)
- **Companion offer schema:** `AgriAdvisoryOfferAttributes` (pricing, access type, cancellation)
- **Companion fulfillment schema:** `AgriAdvisoryFulfillmentAttributes` (delivery location, mode)

---

## Design Rationale

### forecastType as a top-level item discriminator
In v1, the forecast type was encoded in `category.descriptor.code` (`"Weather-Forecast"`).
In v2, this becomes a typed enum in `itemAttributes.forecastType`. This enables precise
type-based filtering during discovery without relying on free-text category matching.

### Weather data points as item attributes
The set of meteorological parameters included in a product (temperature, humidity,
evapotranspiration, etc.) is intrinsic to the item — it describes what data IS provided.
This is discovery metadata: a farmer searching for "temperature + evapotranspiration for
irrigation planning" needs to filter by data points at catalog time.

### forecastDurationDays vs forecastDurationISO
Two duration representations are provided for different consumer needs:
- `forecastDurationDays` (integer): optimised for UI display and range filtering ("show me products with ≥14 days")
- `forecastDurationISO` (ISO 8601): optimised for machine processing and API interoperability

Both can coexist; only one is required.

### Output formats in itemAttributes
The list of available output formats (PDF, JSON API, SMS, etc.) describes what the item
CAN provide — it is intrinsic to the item. The actual delivery format selected by the
buyer at transaction time is captured in `AgriAdvisoryFulfillmentAttributes.deliveryMode`.

### Provider license as a search filter
In v1, provider license (`"Proprietary"`) was encoded as a tag in provider-level intent.
In v2, this is promoted to a typed item attribute. This allows BAPs to filter catalog items
by license type (e.g., "show only open-data providers" for a government platform).

### No price or cancellation policy in itemAttributes
Per v2 core rules, all commercial terms live in `AgriAdvisoryOfferAttributes`. The
INR 30 price for a 14-day forecast from the v1 guide maps to `Offer.beckn:price`.

---

## Non-Goals

- **Does not model the forecast delivery location.** The farm GPS coordinates for which
  the forecast is requested are in `AgriAdvisoryFulfillmentAttributes.targetLocation`.
- **Does not model forecast pricing.** Price lives in `AgriAdvisoryOfferAttributes`.
- **Does not model the actual forecast data payload.** The forecast data itself (temperatures,
  rainfall values) is the delivered content, not a schema attribute. Only the product metadata
  is modeled here.
- **Does not model crop disease risk** — that is in `CropAdvisoryItemAttributes`.

---

## Upstream Candidates

| Attribute | Rationale |
|-----------|-----------|
| `providerLicense` | Any data/content domain (satellite imagery, geospatial data, scientific datasets) needs a license classification |
| `outputFormats` | Any digital data product could use a standard set of output format enums |
| `updateFrequency` | Any real-time or periodic data product (traffic, satellite, air quality) needs refresh frequency |
| `modelSource` | Relevant to any data product derived from a computational model |

---

## v1 → v2 Field Migration

| v1 Field | v2 Location | Notes |
|----------|-------------|-------|
| `category.descriptor.code` = `"Weather-Forecast"` | `itemAttributes.forecastType` | Typed enum replaces code string |
| `item.time.range.start / end` | `beckn:availabilityWindow` | Core Item availability window |
| `item.time.duration` = `"P7D"` | `itemAttributes.forecastDurationISO` | ISO duration in itemAttributes |
| `intent.tags[Weather datapoints].list[].value` | `itemAttributes.weatherDataPoints` | Typed enum array |
| `intent.tags[languages].list[].value` | `itemAttributes.languages` | First-class array |
| `provider.tags[License].value` | `itemAttributes.providerLicense` | Moved from provider-level to item |
| `item.price` | `Offer.beckn:price` via `AgriAdvisoryOfferAttributes` | Price to Offer |
| `fulfillment.stops[].location.gps` | `AgriAdvisoryFulfillmentAttributes.targetLocation` | GeoJSON in fulfillmentAttributes |
