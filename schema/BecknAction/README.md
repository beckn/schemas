# Beckn Action

> **Canonical IRI:** [`https://schema.beckn.io/BecknAction`](https://schema.beckn.io/BecknAction)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Unified Beckn action envelope. All Beckn API requests and callbacks conform to this schema. The context identifies the action being performed; the message carries the action-specific payload. Message content is validated via if/then dispatch based on context.action. For unknown or extension endpoints, no if/then branch applies and message remains unconstrained. This schema supersedes RequestAction and CallbackAction, both of which were structurally invalid. The request/callback distinction is encoded in the context.action value (e.g. beckn/discover vs beckn/on_discover), not in a separate schema type.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `context` | any | ✅ | Transaction context identifying the action, sender, receiver, and correlation IDs. |
| `message` | any | ✅ | Action-specific payload. Content constraints applied via if/then dispatch below. |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/BecknAction` |
| JSON Schema (latest) | `https://schema.beckn.io/BecknAction/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/BecknAction/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/BecknAction/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
