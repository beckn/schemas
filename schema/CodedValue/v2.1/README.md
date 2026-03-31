# CodedValue — v2.1

An authority-governed code value. The @context URI identifies the code system authority (e.g. UN ISIC, UNESCO ISCED, India NSQF). The @type identifies the class of code within that system. The code is the actual value. This pattern avoids hardcoding country-specific enumerations into the schema.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CodedValue/attributes.yaml](https://schema.beckn.io/CodedValue/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CodedValue/v2.1/attributes.yaml](https://schema.beckn.io/CodedValue/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CodedValue/attributes.jsonschema.yaml](https://schema.beckn.io/CodedValue/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CodedValue/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CodedValue/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CodedValue/context.jsonld](https://schema.beckn.io/CodedValue/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CodedValue/v2.1/context.jsonld](https://schema.beckn.io/CodedValue/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CodedValue/vocab.jsonld](https://schema.beckn.io/CodedValue/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CodedValue/v2.1/vocab.jsonld](https://schema.beckn.io/CodedValue/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | URI of the canonical code system authority. Examples: "https://unstats.un.org/unsd/classifications/Econ/isic" (ISIC), "https://uis.unesco.org/en/topic/international-standard-classification-education-isced" (ISCED), "https://www.nqfindia.org/" (India NSQF).  |
| `@type` | yes | string | Code class within the identified context. Examples: "IndustryCode", "FieldOfEducationCode", "QualificationLevel".  |
| `code` | yes | string | The actual code value as defined by the authority. Examples: "8299" (ISIC: other business support), "0613" (ISCED: software), "4" (NSQF Level 4).  |
| `label` | no | string | Human-readable label for the code (optional, for display). |
