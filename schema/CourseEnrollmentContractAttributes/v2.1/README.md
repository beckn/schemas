# CourseEnrollmentContractAttributes — v2.1

Beckn v2.1 extension schema for the contractAttributes container. Represents the transaction-level state of a course enrollment: enrollment reference, cohort assignment, prerequisite verification outcome, and credential issuance tracking. Parties: SKILL_SEEKER and SKILL_PROVIDER.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/attributes.yaml](https://schema.beckn.io/CourseEnrollmentContractAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/attributes.yaml](https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/CourseEnrollmentContractAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/context.jsonld](https://schema.beckn.io/CourseEnrollmentContractAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/context.jsonld](https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/vocab.jsonld](https://schema.beckn.io/CourseEnrollmentContractAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/CourseEnrollmentContractAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `enrollment_reference` | yes | string | BAP-generated unique reference for this enrollment. |
| `cohort_id` | no | string | Identifier of the cohort or batch the learner is assigned to. |
| `prerequisite_verification_summary` | no | $ref: ../../../VerificationSummary/attributes.jsonschema.yaml#/components/schemas/VerificationSummary | - |
| `credential_issuance_pending` | no | boolean | Whether the outcome credential VC is pending issuance upon course completion. True after enrollment; false once the VC has been issued.  |
| `enrolled_at` | yes | string | Timestamp when enrollment was confirmed. |
