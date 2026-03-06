# Message

> **Canonical IRI:** [`https://schema.beckn.io/Message`](https://schema.beckn.io/Message)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Open payload container for Beckn action messages. The specific content of the message object is determined by the action value in the accompanying Context. BecknAction constrains message content based on context.action via if/then dispatch rules. Direct use of this schema provides no payload constraints — use BecknAction for validated action payloads.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Message` |
| JSON Schema (latest) | `https://schema.beckn.io/Message/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Message/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Message/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
