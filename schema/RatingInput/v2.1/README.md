# RatingInput — v2.0

Input for a rating submission.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [RatingInput](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `RatingInput` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string |  |
| `@type` | string |  |
| `target` | object | The entity being rated |
| `range` |  |  |
| `feedbackFormSubmission` | FormSubmission | The submission to the feedback form sent along with a rating request |
