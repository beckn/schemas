# FnBPriceSpecification — v2.0

A price specification for food and beverage (F&B) delivery orders.

FnBPriceSpecification specializes beckn:PriceSpecification for the specific price
calculation structure of a food ordering and delivery transaction. It is derived
from extensive research into how food delivery platforms (Domino's, Zomato, Swiggy,
UberEats) model itemised bills, including:

- Size-dependent item and topping pricing (a topping on a Regular pizza costs less
  than on a Large pizza; add-on price = f(size, topping_type))
- Crust upcharges (premium crusts like Cheese Burst or Pan cost more)
- Combo discount mechanics (bundle savings expressed as negative values)
- Delivery and packaging fees distinct from item charges
- Platform convenience charges

**Component type codes:**

Item-level charges (may appear multiple times — once per line item):
- BASE_ITEM         — Base price of a food or beverage item at its selected size
- SIZE_UPCHARGE     — Premium for selecting a larger size over the base size (e.g. Regular → Medium)
- TOPPING           — Individual topping or ingredient add-on; price varies by item size
- ADDON             — Optional add-on item (dip, sauce, condiment packet)
- CUSTOMIZATION     — Surcharge for a special preparation request
- SIDE              — A side dish added to the order

Combo and offer adjustments (typically negative):
- COMBO_SAVINGS     — Discount from applying a bundle/meal combo deal (negative)
- COMBO_UPCHARGE    — Premium for upgrading within a combo (e.g. regular to medium pizza)
- OFFER_DISCOUNT    — Time-limited promotional discount applied at order level (negative)
- COUPON_DISCOUNT   — Discount from a promo/coupon code (negative)
- LOYALTY_DISCOUNT  — Discount from loyalty points redemption (negative)

Order-level charges:
- DELIVERY_FEE      — Delivery charge (flat, distance-based, or surge-adjusted)
- PACKAGING_FEE     — Restaurant packaging charge (boxes, insulated bags, eco-packaging)
- SMALL_ORDER_FEE   — Surcharge applied when order value is below the minimum
- PLATFORM_FEE      — App/platform convenience service charge

Gratuity:
- TIP               — Customer gratuity (added voluntarily by the consumer)

Notes:
- Tax components (GST, VAT, etc.) are jurisdiction-specific and MUST be modelled
  using PriceSpecificationComponent variants, not as codes in this schema.
- For TOPPING components, referenceItemId SHOULD be set to the ID of the base
  item to which the topping belongs, since topping price varies by item size.
- Negative values MUST be used for COMBO_SAVINGS, OFFER_DISCOUNT, COUPON_DISCOUNT,
  and LOYALTY_DISCOUNT.

Inheritance: beckn:PriceSpecification ← beckn:FnBPriceSpecification
schema.org alignment: schema:PriceSpecification (via inheritance)
Use in: beckn:Consideration.considerationAttributes for F&B orders

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FnBPriceSpecification/attributes.yaml](https://schema.beckn.io/FnBPriceSpecification/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FnBPriceSpecification/v2.0/attributes.yaml](https://schema.beckn.io/FnBPriceSpecification/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FnBPriceSpecification/attributes.jsonschema.yaml](https://schema.beckn.io/FnBPriceSpecification/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FnBPriceSpecification/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FnBPriceSpecification/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FnBPriceSpecification/context.jsonld](https://schema.beckn.io/FnBPriceSpecification/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FnBPriceSpecification/v2.0/context.jsonld](https://schema.beckn.io/FnBPriceSpecification/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FnBPriceSpecification/vocab.jsonld](https://schema.beckn.io/FnBPriceSpecification/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FnBPriceSpecification/v2.0/vocab.jsonld](https://schema.beckn.io/FnBPriceSpecification/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| _none_ | - | - | - |
