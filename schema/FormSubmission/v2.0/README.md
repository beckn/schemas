# FormSubmission — v2.0

A user's submitted response to a Beckn form. Captures the filled-in field values keyed by form field names. Typically attached to a RatingInput to convey feedback form answers alongside a rating.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/FormSubmission/attributes.yaml](https://schema.beckn.io/FormSubmission/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/FormSubmission/v2.0/attributes.yaml](https://schema.beckn.io/FormSubmission/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/FormSubmission/attributes.jsonschema.yaml](https://schema.beckn.io/FormSubmission/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/FormSubmission/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/FormSubmission/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/FormSubmission/context.jsonld](https://schema.beckn.io/FormSubmission/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/FormSubmission/v2.0/context.jsonld](https://schema.beckn.io/FormSubmission/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/FormSubmission/vocab.jsonld](https://schema.beckn.io/FormSubmission/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/FormSubmission/v2.0/vocab.jsonld](https://schema.beckn.io/FormSubmission/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | Identifier of the form that was submitted. Typically the form's URL or the value of the form's url field. |
| `submissionId` | no | string | Unique identifier for this form submission instance. |
| `data` | yes | object | Key-value map of form field names to submitted values. Keys correspond to the field identifiers defined in the form; values are the user's responses as strings. |
| `submittedAt` | no | string | Timestamp at which the form was submitted, in RFC 3339 / ISO 8601 format. |
