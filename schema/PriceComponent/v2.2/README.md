# PriceComponent — v2.1

A single line item within a `PriceSpecification` breakup, such as a base charge, tax, delivery cost, discount, fee, or surcharge. Beyond the monetary amount, a `PriceComponent` MAY carry a JSON-LD `componentAttributes` bag that richly describes why the component applies, how it is calculated, and any governing terms — enabling a receiving node to render or act on the line (for example, highlight a surge charge or notify the user) without performing any price computation of its own.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/PriceComponent/v2.2/attributes.yaml](https://schema.beckn.io/PriceComponent/v2.2/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/PriceComponent/v2.2/schema.json](https://schema.beckn.io/PriceComponent/v2.2/schema.json) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/PriceComponent/v2.2/context.jsonld](https://schema.beckn.io/PriceComponent/v2.2/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/PriceComponent/v2.2/vocab.jsonld](https://schema.beckn.io/PriceComponent/v2.2/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `type` | no | string (enum) | The nature of this price component: `UNIT`, `TAX`, `DELIVERY`, `DISCOUNT`, `FEE`, `SURCHARGE`, `DEPOSIT_REFUNDABLE`, `DEPOSIT`, `ADVANCE`, `TIP`, `CARRY_FORWARD`, `PENALTY`, `DONATION`, `TRANCHE`, `CASHBACK`, `SERVICE_FEE`, `PROCESSING_FEE`, `CONVENIENCE_FEE`, `REFUND`, `TOTAL`, `OTHER` |
| `value` | no | number | Monetary amount of this component, expressed in `currency` |
| `currency` | no | string | ISO 4217 currency code for `value` |
| `description` | no | string | Human-readable label for this component |
| `componentAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/schema.json | JSON-LD aware container describing the rationale, calculation, and terms of this component. MUST include `@context` and `@type` |

## Examples

A surged base fare, with the SurgeMultiplier carried in `componentAttributes`:

```json
{
  "type": "UNIT",
  "value": 14.40,
  "currency": "EUR",
  "description": "(Base fare + distance) X 1.2x surge pricing",
  "componentAttributes": {
    "@context": "https://schema.beckn.io/SurgeMultiplier/2.0/context.jsonld",
    "@type": "SurgeMultiplier",
    "multiplierValue": 1.2,
    "reason": "HIGH_DEMAND",
    "validUntil": "2026-07-06T10:00:00Z",
    "appliedTo": { "@type": "PriceSpecification", "currency": "EUR", "value": 12.00 }
  }
}
```

A refundable deposit, with its settlement terms carried in `componentAttributes`:

```json
{
  "type": "DEPOSIT_REFUNDABLE",
  "value": 150.00,
  "currency": "EUR",
  "description": "Refundable security deposit (hold; refunded after return of the vehicle undamaged)",
  "componentAttributes": {
    "@context": "https://schema.beckn.io/SettlementTerm/2.0/context.jsonld",
    "@type": "SettlementTerm",
    "amount": { "currency": "EUR", "value": 150.00 },
    "paymentTrigger": "POST_FULFILLMENT",
    "settlementStatus": "PENDING",
    "payTo": { "vpa": "rider-refund-account@bank" },
    "acceptedPaymentMethods": ["BANK_TRANSFER"]
  }
}
```
