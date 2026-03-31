# CandidateProfileResourceAttributes — v2.1

Discoverable profile attributes of a candidate Resource. Captures what the candidate brings (skills, experience, availability) and what they seek (location preference, work mode, job type). Designed for privacy: no name, contact, or identity data. Credentials are referenced via SkillEntry with optional VC attestation URLs.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CandidateProfileResourceAttributes/attributes.yaml](https://schema.beckn.io/CandidateProfileResourceAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/attributes.yaml](https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/CandidateProfileResourceAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/context.jsonld](https://schema.beckn.io/CandidateProfileResourceAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/context.jsonld](https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/vocab.jsonld](https://schema.beckn.io/CandidateProfileResourceAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/CandidateProfileResourceAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `skills` | no | array | List of skills, qualifications, and credentials held by the candidate. Each entry supports graceful degradation: self-declared (attested=false) or VC-backed (attested=true, proof_request_url present).  |
| `experience_level` | no | string | Overall seniority level of the candidate. |
| `experience_years` | no | integer | Approximate total years of relevant work experience. |
| `location_preference` | no | object | Geographic and work-mode preferences of the candidate. |
| `availability` | no | string | How soon the candidate is available to start. |
| `open_to_relocation` | no | boolean | Whether the candidate is open to relocating. |
| `industry_preference` | no | array | Industries the candidate prefers to work in, expressed as authority-governed codes for international neutrality.  |
| `job_type_preference` | no | array | Types of employment the candidate is interested in. |
| `overall_verification_status` | no | string | Aggregate verification status derived from the candidate's DeDi verification_index. Indicates how many of their declared skills have been VC-attested. Not PII — derived from public registry data.  |
