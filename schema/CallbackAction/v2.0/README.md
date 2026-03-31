# CallbackAction — v2.0

DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. The $id also lacked a version segment.
Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). Callback actions are those with on_ prefixed endpoints (e.g. beckn/on_discover, beckn/on_confirm) and are validated by the same BecknAction schema via if/then dispatch on context.action.
This schema will be removed in a future major version.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CallbackAction/attributes.yaml](https://schema.beckn.io/CallbackAction/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CallbackAction/v2.0/attributes.yaml](https://schema.beckn.io/CallbackAction/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CallbackAction/attributes.jsonschema.yaml](https://schema.beckn.io/CallbackAction/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CallbackAction/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CallbackAction/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CallbackAction/context.jsonld](https://schema.beckn.io/CallbackAction/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CallbackAction/v2.0/context.jsonld](https://schema.beckn.io/CallbackAction/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CallbackAction/vocab.jsonld](https://schema.beckn.io/CallbackAction/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CallbackAction/v2.0/vocab.jsonld](https://schema.beckn.io/CallbackAction/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| _none_ | - | - | - |
