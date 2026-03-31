# RatingForm — v2.0

A form designed to capture rating and feedback from a user. This can be used by both BAP and BPP to fetch ratings and feedback of their respective users.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RatingForm/attributes.yaml](https://schema.beckn.io/RatingForm/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RatingForm/v2.0/attributes.yaml](https://schema.beckn.io/RatingForm/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RatingForm/attributes.jsonschema.yaml](https://schema.beckn.io/RatingForm/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RatingForm/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RatingForm/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RatingForm/context.jsonld](https://schema.beckn.io/RatingForm/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RatingForm/v2.0/context.jsonld](https://schema.beckn.io/RatingForm/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RatingForm/vocab.jsonld](https://schema.beckn.io/RatingForm/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RatingForm/v2.0/vocab.jsonld](https://schema.beckn.io/RatingForm/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `target` | yes | object | The entity being rated |
| `range` | no | any | - |
| `feedbackForm` | no | $ref: https://schema.beckn.io/Form/attributes.yaml#/components/schemas/Form | A feedback form sent along with a rating request |
| `feedbackRequired` | yes | boolean | Specifies whether feedback after rating is required for acceptance of rating |
