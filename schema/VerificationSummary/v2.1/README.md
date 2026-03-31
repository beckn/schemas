# VerificationSummary — v2.1

Summary of a credential verification check. Contains the overall result, reason codes for any failures, and which credential categories were successfully verified. No VC or VP payloads are included.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/VerificationSummary/attributes.yaml](https://schema.beckn.io/VerificationSummary/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/VerificationSummary/v2.1/attributes.yaml](https://schema.beckn.io/VerificationSummary/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/VerificationSummary/attributes.jsonschema.yaml](https://schema.beckn.io/VerificationSummary/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/VerificationSummary/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/VerificationSummary/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/VerificationSummary/context.jsonld](https://schema.beckn.io/VerificationSummary/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/VerificationSummary/v2.1/context.jsonld](https://schema.beckn.io/VerificationSummary/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/VerificationSummary/vocab.jsonld](https://schema.beckn.io/VerificationSummary/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/VerificationSummary/v2.1/vocab.jsonld](https://schema.beckn.io/VerificationSummary/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `overall_result` | yes | string | Aggregate outcome of the verification check. |
| `reason_codes` | no | array | Reason codes for failures or partial results. Empty if overall_result is PASS. Examples: "MANDATORY_REQUIREMENT_MISSING", "EXPIRED_CREDENTIAL", "ISSUER_NOT_TRUSTED", "SIGNATURE_INVALID".  |
| `verified_categories` | no | array | Credential categories that were successfully verified in this check.  |
| `verified_subtypes` | no | array | Specific credential subtypes that were successfully verified.  |
| `checked_at` | yes | string | Timestamp when verification was performed. |
| `proof_metadata_hash` | no | string | Optional hash of the VP used in verification. Provides integrity reference without storing the VP payload.  |
