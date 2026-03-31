# SkillEntry — v2.1

A single skill, qualification, or credential held by a candidate. The attested flag and proof_request_url are optional — allowing the schema to function in early-stage ecosystems where VC infrastructure is not yet universal. As VCs become available for specific skills, the proof_request_url can be populated without any schema change.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SkillEntry/attributes.yaml](https://schema.beckn.io/SkillEntry/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/SkillEntry/v2.1/attributes.yaml](https://schema.beckn.io/SkillEntry/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SkillEntry/attributes.jsonschema.yaml](https://schema.beckn.io/SkillEntry/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/SkillEntry/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/SkillEntry/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/SkillEntry/context.jsonld](https://schema.beckn.io/SkillEntry/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/SkillEntry/v2.1/context.jsonld](https://schema.beckn.io/SkillEntry/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SkillEntry/vocab.jsonld](https://schema.beckn.io/SkillEntry/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/SkillEntry/v2.1/vocab.jsonld](https://schema.beckn.io/SkillEntry/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `category` | yes | string | Broad class of the credential or skill held. |
| `subtype` | yes | string | Specific skill or credential. Examples: "AWS_SAA", "BTECH_CS", "LMV_LICENSE", "Java_SE_11", "CNC_Operator_Level2".  |
| `level` | no | string | Optional proficiency or qualification level. Examples: "BEGINNER", "PROFESSIONAL", "ADVANCED", "3_YEARS_EXP", "NQF_Level_4".  |
| `attested` | yes | boolean | Whether this skill entry is backed by a verifiable credential (VC). false = self-declared (no VC yet); true = VC exists and is resolvable via proof_request_url. Employers can discover self-declared skills but know they are unverified.  |
| `proof_request_url` | no | string | URL of the DeDi proof-request endpoint scoped to this specific credential. Only present when attested = true. An employer BAP can call this endpoint to trigger a Verifiable Presentation (VP) request. The VC payload itself never leaves the holder's wallet — only a signed verification response is returned by the orchestrator. Example: "https://dedi.example.net/proof-request/did:ex:123/skill/AWS_SAA"  |
