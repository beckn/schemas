# HiringJobOfferAttributes — v2.1

Commercial and availability terms under which a job opportunity is offered. The proposedConsideration on the core Offer object carries the midpoint or headline compensation figure; this extension provides the full range and period breakdown for display and filtering.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/HiringJobOfferAttributes/attributes.yaml](https://schema.beckn.io/HiringJobOfferAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/v2.1/attributes.yaml](https://schema.beckn.io/HiringJobOfferAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/HiringJobOfferAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/HiringJobOfferAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/context.jsonld](https://schema.beckn.io/HiringJobOfferAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/v2.1/context.jsonld](https://schema.beckn.io/HiringJobOfferAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/vocab.jsonld](https://schema.beckn.io/HiringJobOfferAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/HiringJobOfferAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/HiringJobOfferAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `compensation_currency` | no | string | ISO 4217 currency code for the compensation. |
| `compensation_min` | no | number | Lower bound of the compensation range. |
| `compensation_max` | no | number | Upper bound of the compensation range. |
| `compensation_period` | no | string | Pay period for the stated compensation figures. |
| `openings_count` | no | integer | Number of positions available under this offer. |
| `application_deadline` | no | string | Latest datetime by which applications will be accepted. |
| `posting_validity` | no | object | Publication window for this offer (start and end datetimes). |
| `probation_period_months` | no | integer | Optional probation period in months applicable to this offer. Absence implies no formal probation.  |
