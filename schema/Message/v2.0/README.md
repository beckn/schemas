# Message — v2.0

Open payload container for Beckn action messages. The specific content of the message object is determined by the action value in the accompanying Context. BecknAction constrains message content based on context.action via if/then dispatch rules. Direct use of this schema provides no payload constraints — use BecknAction for validated action payloads.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Message](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | JSON Schema 2020-12 definition for `Message` |
| [context.jsonld](./context.jsonld) | JSON-LD context for `Message` v2.0 |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary for `Message` v2.0 |
