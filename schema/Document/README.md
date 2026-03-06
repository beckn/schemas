# Document

> **Canonical IRI:** [`https://schema.beckn.io/Document`](https://schema.beckn.io/Document)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

A document, that can be parsed, printed, download or displayed. This has intentionally been kept separate from MediaFile as they may contain additional attributes like signature, schema etc.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `label` | `string` | — | The display name of the media file |
| `mimeType` | `string` | — | MIME type if 'data' is provided (application/pdf, image/png, application/json). |
| `standard` | `string` | — | Describes the schema type in case the document follows a standard schema like a verifiableCredential |
| `url` | `string` (uri) | — | URL to the document |
| `security` | object | — | — |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Document` |
| JSON Schema (latest) | `https://schema.beckn.io/Document/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Document/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Document/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
