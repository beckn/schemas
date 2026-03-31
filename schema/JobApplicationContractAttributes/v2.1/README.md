# JobApplicationContractAttributes — v2.1

Transaction-level metadata for a job application contract. Captures the application reference, aggregate verification outcome, and reverification state. No credential payloads are stored here.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/JobApplicationContractAttributes/attributes.yaml](https://schema.beckn.io/JobApplicationContractAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/v2.1/attributes.yaml](https://schema.beckn.io/JobApplicationContractAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/JobApplicationContractAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/JobApplicationContractAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/context.jsonld](https://schema.beckn.io/JobApplicationContractAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/v2.1/context.jsonld](https://schema.beckn.io/JobApplicationContractAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/vocab.jsonld](https://schema.beckn.io/JobApplicationContractAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/JobApplicationContractAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/JobApplicationContractAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `application_reference` | yes | string | BAP-generated unique reference for this application. Used for tracking, status queries, and audit. Not a platform routing ID.  |
| `verification_summary` | no | $ref: ../../../VerificationSummary/attributes.jsonschema.yaml#/components/schemas/VerificationSummary | Aggregate outcome of credential verification performed during the application submission. Populated after verification completes.  |
| `reverification_requested` | no | boolean | Whether the employer (EMPLOYER party) has requested re-verification of some or all credentials after the initial application submission.  |
| `reverification_requirements` | no | array | Additional or revised requirements for which reverification has been requested. Only populated when reverification_requested = true.  |
| `submitted_at` | yes | string | Timestamp when the application was submitted. |
