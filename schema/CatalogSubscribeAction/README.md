# CatalogSubscribeAction

Message payload for catalog/subscription.
At least one of `networkIds` or `schemaTypes` must be non-empty.
An empty `schemaTypes` array is treated as the wildcard sentinel `"*"`,
matching all schema types for the specified networks.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.yaml](https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.yaml) | [https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CatalogSubscribeAction/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/CatalogSubscribeAction/v2.0/context.jsonld](https://schema.beckn.io/CatalogSubscribeAction/v2.0/context.jsonld) | [https://schema.beckn.io/CatalogSubscribeAction/v2.0/vocab.jsonld](https://schema.beckn.io/CatalogSubscribeAction/v2.0/vocab.jsonld) | [https://schema.beckn.io/CatalogSubscribeAction/v2.0/README.md](https://schema.beckn.io/CatalogSubscribeAction/v2.0/README.md) |
