# Form Submission — v2.0

A user's submitted response to a Beckn form. Captures the filled-in field values keyed by form field names. Typically attached to a RatingInput to convey feedback form answers alongside a rating.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [FormSubmission](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | JSON Schema 2020-12 definition for `FormSubmission` |
| [context.jsonld](./context.jsonld) | JSON-LD context for `FormSubmission` v2.0 |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary for `FormSubmission` v2.0 |

## Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string (uri) | — | Identifier of the form that was submitted. Typically the form's URL or the value of the form's url field. |
| `submissionId` | string (uuid) | — | Unique identifier for this form submission instance. |
| `data` | object | ✅ | Key-value map of form field names to submitted values. Keys correspond to the field identifiers defined in the form; … |
| `submittedAt` | string (date-time) | — | Timestamp at which the form was submitted, in RFC 3339 / ISO 8601 format. |
