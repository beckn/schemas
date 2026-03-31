# LineageEntry

A causal attribution record asserting that the Beckn transaction in which this entry appears was triggered by a specific upstream Beckn interaction. Used in Context.lineage at transaction boundaries — when a new transaction is initiated as a direct consequence of an upstream interaction. MUST NOT be included within subsequent steps of the same transaction, and MUST NOT be propagated by downstream responses.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/LineageEntry/v2.0/attributes.yaml](https://schema.beckn.io/LineageEntry/v2.0/attributes.yaml) | [https://schema.beckn.io/LineageEntry/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LineageEntry/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/LineageEntry/v2.0/context.jsonld](https://schema.beckn.io/LineageEntry/v2.0/context.jsonld) | [https://schema.beckn.io/LineageEntry/v2.0/vocab.jsonld](https://schema.beckn.io/LineageEntry/v2.0/vocab.jsonld) | [https://schema.beckn.io/LineageEntry/v2.0/README.md](https://schema.beckn.io/LineageEntry/v2.0/README.md) |
