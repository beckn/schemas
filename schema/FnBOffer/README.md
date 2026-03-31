# FnBOffer

A Beckn schema for food and beverage offer attributes.

FnBOffer extends beckn:RetailCoreOfferAttributes with F&B-specific offer
customization groups — the structured mechanism by which a food item's
configurable options (size, crust, toppings, add-ons) are declared and
priced within an offer.

A CustomizationGroup represents one dimension of configurability (e.g.
pizza size, crust type, topping selection). Each group has one or more
options with optional price deltas.

Inheritance: beckn:RetailCoreOfferAttributes ← beckn:FnBOffer
Use in: beckn:Offer.offerAttributes for F&B catalog items

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/FnBOffer/v2.0/attributes.yaml](https://schema.beckn.io/FnBOffer/v2.0/attributes.yaml) | [https://schema.beckn.io/FnBOffer/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FnBOffer/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/FnBOffer/v2.0/context.jsonld](https://schema.beckn.io/FnBOffer/v2.0/context.jsonld) | [https://schema.beckn.io/FnBOffer/v2.0/vocab.jsonld](https://schema.beckn.io/FnBOffer/v2.0/vocab.jsonld) | [https://schema.beckn.io/FnBOffer/v2.0/README.md](https://schema.beckn.io/FnBOffer/v2.0/README.md) |
