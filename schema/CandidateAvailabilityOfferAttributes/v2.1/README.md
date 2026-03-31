# CandidateAvailabilityOfferAttributes — v2.1

Availability and compensation expectation terms under which a candidate profile is offered to employers. The proposedConsideration on the core Offer carries the candidate's headline desired salary; this extension provides the full range, notice period, and contract type preferences.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/attributes.yaml](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/attributes.yaml](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/context.jsonld](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/context.jsonld](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/vocab.jsonld](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `desired_compensation_currency` | no | string | ISO 4217 currency code for the desired compensation. |
| `desired_compensation_min` | no | number | Lower bound of the candidate's desired compensation range. |
| `desired_compensation_max` | no | number | Upper bound of the candidate's desired compensation range. |
| `desired_compensation_period` | no | string | Period against which the desired compensation is stated. |
| `notice_period_days` | no | integer | Current notice period the candidate must serve before joining. |
| `availability_window` | no | object | Period during which the candidate is available to start. |
| `preferred_contract_types` | no | array | Employment types the candidate is willing to accept. |
