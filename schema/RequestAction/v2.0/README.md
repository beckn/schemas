# Request Action — v2.0

DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). The request/callback distinction is encoded in context.action (e.g. beckn/discover for requests, beckn/on_discover for callbacks). This schema will be removed in a future major version.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [RequestAction](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | JSON Schema 2020-12 definition for `RequestAction` |
| [context.jsonld](./context.jsonld) | JSON-LD context for `RequestAction` v2.0 |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary for `RequestAction` v2.0 |
