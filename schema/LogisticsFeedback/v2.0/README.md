# LogisticsFeedback — v2.0

Qualitative feedback from sender or receiver about a logistics experience.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LogisticsFeedback/attributes.yaml](https://schema.beckn.io/LogisticsFeedback/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LogisticsFeedback/v2.0/attributes.yaml](https://schema.beckn.io/LogisticsFeedback/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LogisticsFeedback/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsFeedback/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LogisticsFeedback/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsFeedback/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LogisticsFeedback/context.jsonld](https://schema.beckn.io/LogisticsFeedback/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LogisticsFeedback/v2.0/context.jsonld](https://schema.beckn.io/LogisticsFeedback/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LogisticsFeedback/vocab.jsonld](https://schema.beckn.io/LogisticsFeedback/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LogisticsFeedback/v2.0/vocab.jsonld](https://schema.beckn.io/LogisticsFeedback/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | - |
| `shipmentId` | no | string | - |
| `rating` | no | $ref: https://schema.beckn.io/Rating/v2.1/attributes.yaml#/components/schemas/Rating | - |
| `review` | no | string | Free text review |
| `tags` | no | array | Structured feedback tags |
| `wouldRecommend` | no | boolean | - |
| `submittedBy` | no | string | User ID of feedback submitter |
| `submittedAt` | no | string | - |
| `isPublic` | no | boolean | Whether feedback is publicly visible |
