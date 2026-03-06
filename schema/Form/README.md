# Form

> **Canonical IRI:** [`https://schema.beckn.io/Form`](https://schema.beckn.io/Form)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Describes a form

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | CPD |
| `@type` | `string` | ✅ | — |
| `data` | object | — | The form submission data |
| `mimeType` | `string` | — | This field indicates the nature and format of the form received by querying the url. MIME types are defined and standardized in IETF's RFC 6838. |
| `submissionId` | `string` (uuid) | — | — |
| `url` | `string` (uri) | — | The URL from where the form can be fetched. The content fetched from the url must be processed as per the mimeType specified in this object. Once f… |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Form` |
| JSON Schema (latest) | `https://schema.beckn.io/Form/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Form/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Form/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
