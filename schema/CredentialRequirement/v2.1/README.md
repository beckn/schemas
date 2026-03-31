# CredentialRequirement — v2.1

A single credential requirement or prerequisite. Specifies what a candidate or enrollee must hold. Category is a broad class; subtype is the specific credential within that class.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CredentialRequirement/attributes.yaml](https://schema.beckn.io/CredentialRequirement/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CredentialRequirement/v2.1/attributes.yaml](https://schema.beckn.io/CredentialRequirement/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CredentialRequirement/attributes.jsonschema.yaml](https://schema.beckn.io/CredentialRequirement/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CredentialRequirement/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CredentialRequirement/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CredentialRequirement/context.jsonld](https://schema.beckn.io/CredentialRequirement/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CredentialRequirement/v2.1/context.jsonld](https://schema.beckn.io/CredentialRequirement/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CredentialRequirement/vocab.jsonld](https://schema.beckn.io/CredentialRequirement/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CredentialRequirement/v2.1/vocab.jsonld](https://schema.beckn.io/CredentialRequirement/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `category` | yes | string | Broad class of the required credential. |
| `subtype` | yes | string | Specific credential within the category. Examples: "AWS_SAA", "BTECH_CS", "LMV_LICENSE", "Aadhaar", "Java_SE_11".  |
| `mandatory` | yes | boolean | Whether this requirement is mandatory. If true, failure to satisfy it blocks the transaction. If false, it is advisory / preferred.  |
