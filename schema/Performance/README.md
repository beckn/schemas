# Performance

Generalized execution/performance unit. This is where downstream objects bind:
- Fulfillment-like details (where/when/how)
- Tracking handles
- Support touchpoints
- Status updates

A minimal envelope that carries identity, status, and a performanceAttributes
bag that holds the concrete domain-specific delivery schema.

Domain specification authors can attach rich context and types via `performanceAttributes`.

For example, Hyperlocal delivery details (pickup/delivery locations, items shipped, agent, etc.)
are placed inside performanceAttributes using a well-known domain schema such as
HyperlocalDelivery. Use the generic Attributes schema when no well-known
domain schema exists.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/Performance/v2.0/attributes.yaml](https://schema.beckn.io/Performance/v2.0/attributes.yaml) | [https://schema.beckn.io/Performance/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Performance/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/Performance/v2.0/context.jsonld](https://schema.beckn.io/Performance/v2.0/context.jsonld) | [https://schema.beckn.io/Performance/v2.0/vocab.jsonld](https://schema.beckn.io/Performance/v2.0/vocab.jsonld) | [https://schema.beckn.io/Performance/v2.0/README.md](https://schema.beckn.io/Performance/v2.0/README.md) |
