# JobApplicationPerformanceAttributes — v2.1

Execution metadata for the verification and routing service performed during a job application. Includes the verification method used, per-requirement results, proof integrity reference, and routing outcome. No VC or VP payloads are stored.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/attributes.yaml](https://schema.beckn.io/JobApplicationPerformanceAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/attributes.yaml](https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/JobApplicationPerformanceAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/context.jsonld](https://schema.beckn.io/JobApplicationPerformanceAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/context.jsonld](https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/vocab.jsonld](https://schema.beckn.io/JobApplicationPerformanceAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/JobApplicationPerformanceAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `verification_method` | no | string | Primary method used to verify credentials in this performance unit. |
| `per_requirement_results` | no | array | Granular verification outcome per requirement. Mandatory requirements that FAIL block routing to the employer.  |
| `proof_hash` | no | string | SHA-256 hash of the Verifiable Presentation (VP) used during verification. Provides integrity reference; no VP payload stored.  |
| `issuer_dids_verified` | no | array | DIDs of credential issuers validated during this performance. |
| `routed_to_provider` | no | boolean | Whether the application was successfully forwarded to the employer after verification. False if mandatory requirements failed.  |
| `routing_timestamp` | no | string | Timestamp when the application was routed to the employer. |
