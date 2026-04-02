# Context

Base context schema for all Beckn API calls. Contains addressing information
(BAP/BPP identifiers and API URLs), protocol version, the action being called,
transaction and message IDs, timestamp, TTL, and optional encryption key.
This schema defines all possible properties but imposes NO required-field
constraints. Endpoint-specific validation is defined inline in operation request schemas.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/Context/v2.0/attributes.yaml](https://schema.beckn.io/Context/v2.0/attributes.yaml) | [https://schema.beckn.io/Context/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Context/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/Context/v2.0/context.jsonld](https://schema.beckn.io/Context/v2.0/context.jsonld) | [https://schema.beckn.io/Context/v2.0/vocab.jsonld](https://schema.beckn.io/Context/v2.0/vocab.jsonld) | [https://schema.beckn.io/Context/v2.0/README.md](https://schema.beckn.io/Context/v2.0/README.md) |
