# BecknAction

Unified Beckn action envelope. All Beckn API requests and callbacks conform to this schema. The context identifies the action being performed; the message carries the action-specific payload. Message content is validated via if/then dispatch based on context.action. For unknown or extension endpoints, no if/then branch applies and message remains unconstrained.
This schema supersedes RequestAction and CallbackAction, both of which were structurally invalid. The request/callback distinction is encoded in the context.action value (e.g. beckn/discover vs beckn/on_discover), not in a separate schema type.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/BecknAction/v2.0/attributes.yaml](https://schema.beckn.io/BecknAction/v2.0/attributes.yaml) | [https://schema.beckn.io/BecknAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/BecknAction/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/BecknAction/v2.0/context.jsonld](https://schema.beckn.io/BecknAction/v2.0/context.jsonld) | [https://schema.beckn.io/BecknAction/v2.0/vocab.jsonld](https://schema.beckn.io/BecknAction/v2.0/vocab.jsonld) | [https://schema.beckn.io/BecknAction/v2.0/README.md](https://schema.beckn.io/BecknAction/v2.0/README.md) |
