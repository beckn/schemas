# Tracking — v2.1

Information regarding live tracking of the fufillment of a contract

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Tracking/attributes.yaml](https://schema.beckn.io/Tracking/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Tracking/v2.1/attributes.yaml](https://schema.beckn.io/Tracking/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Tracking/attributes.jsonschema.yaml](https://schema.beckn.io/Tracking/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Tracking/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/Tracking/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Tracking/context.jsonld](https://schema.beckn.io/Tracking/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Tracking/v2.1/context.jsonld](https://schema.beckn.io/Tracking/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Tracking/vocab.jsonld](https://schema.beckn.io/Tracking/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Tracking/v2.1/vocab.jsonld](https://schema.beckn.io/Tracking/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `refId` | no | string | Tracking reference ID for the tracking session. Could be the Order ID, Fulfillment ID, Fulfillment Stage ID, or any other unique tracking identifier |
| `status` | yes | string | - |
| `url` | yes | string | Link/handle to off-network tracking UI or endpoint. |
