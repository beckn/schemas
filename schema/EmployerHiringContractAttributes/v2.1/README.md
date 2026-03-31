# EmployerHiringContractAttributes — v2.1

Contract-level metadata for an employer-to-candidate hiring offer. Captures the specific role details being offered, compensation amount (as distinct from the candidate's desired range), proposed joining date, offer expiry, and candidate response state.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/EmployerHiringContractAttributes/attributes.yaml](https://schema.beckn.io/EmployerHiringContractAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/attributes.yaml](https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/EmployerHiringContractAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/context.jsonld](https://schema.beckn.io/EmployerHiringContractAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/context.jsonld](https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/vocab.jsonld](https://schema.beckn.io/EmployerHiringContractAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/EmployerHiringContractAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `role_title` | yes | string | Title of the role being formally offered. |
| `role_location` | no | object | Location where the role will be performed. |
| `role_work_mode` | no | string | Work arrangement for the offered role. |
| `proposed_joining_date` | no | string | Date the employer proposes the candidate joins. |
| `offer_expiry` | yes | string | Datetime after which the offer lapses if not accepted. |
| `offered_compensation_currency` | no | string | ISO 4217 currency code for the offered compensation. |
| `offered_compensation_amount` | no | number | Specific compensation amount offered (not a range). |
| `offered_compensation_period` | no | string | Period for the offered compensation. |
| `candidate_response` | no | string | Candidate's response to the hiring offer. |
