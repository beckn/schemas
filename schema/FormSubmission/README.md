# Form Submission

> **Canonical IRI:** [`https://schema.beckn.io/FormSubmission`](https://schema.beckn.io/FormSubmission)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A user's submitted response to a Beckn form. Captures the filled-in field values keyed by form field names. Typically attached to a RatingInput to convey feedback form answers alongside a rating.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | `string` (uri) | — | Identifier of the form that was submitted. Typically the form's URL or the value of the form's url field. |
| `submissionId` | `string` (uuid) | — | Unique identifier for this form submission instance. |
| `data` | object | ✅ | Key-value map of form field names to submitted values. Keys correspond to the field identifiers defined in the form; values are the user's response… |
| `submittedAt` | `string` (date-time) | — | Timestamp at which the form was submitted, in RFC 3339 / ISO 8601 format. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/FormSubmission` |
| JSON Schema (latest) | `https://schema.beckn.io/FormSubmission/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/FormSubmission/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/FormSubmission/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
