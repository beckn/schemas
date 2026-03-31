# BecknAction — v2.0

Unified Beckn action envelope. All Beckn API requests and callbacks conform to this schema. The context identifies the action being performed; the message carries the action-specific payload. Message content is validated via if/then dispatch based on context.action. For unknown or extension endpoints, no if/then branch applies and message remains unconstrained.
This schema supersedes RequestAction and CallbackAction, both of which were structurally invalid. The request/callback distinction is encoded in the context.action value (e.g. beckn/discover vs beckn/on_discover), not in a separate schema type.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/BecknAction/attributes.yaml](https://schema.beckn.io/BecknAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/BecknAction/v2.0/attributes.yaml](https://schema.beckn.io/BecknAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/BecknAction/attributes.jsonschema.yaml](https://schema.beckn.io/BecknAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/BecknAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/BecknAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/BecknAction/context.jsonld](https://schema.beckn.io/BecknAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/BecknAction/v2.0/context.jsonld](https://schema.beckn.io/BecknAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/BecknAction/vocab.jsonld](https://schema.beckn.io/BecknAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/BecknAction/v2.0/vocab.jsonld](https://schema.beckn.io/BecknAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `context` | yes | $ref: https://schema.beckn.io/Context/attributes.yaml#/components/schemas/Context | Transaction context identifying the action, sender, receiver, and correlation IDs. |
| `message` | yes | $ref: https://schema.beckn.io/Message/attributes.yaml#/components/schemas/Message | Action-specific payload. Content constraints applied via if/then dispatch below. |
