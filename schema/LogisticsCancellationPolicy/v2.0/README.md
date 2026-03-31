# LogisticsCancellationPolicy — v2.0

Defines terms under which a shipment booking can be cancelled.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LogisticsCancellationPolicy/attributes.yaml](https://schema.beckn.io/LogisticsCancellationPolicy/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/attributes.yaml](https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsCancellationPolicy/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/context.jsonld](https://schema.beckn.io/LogisticsCancellationPolicy/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/context.jsonld](https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/vocab.jsonld](https://schema.beckn.io/LogisticsCancellationPolicy/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/vocab.jsonld](https://schema.beckn.io/LogisticsCancellationPolicy/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | no | string | - |
| `cancellableUntil` | no | string | Cancellation allowed until this lifecycle stage |
| `cancellationFee` | no | object | - |
| `refundPolicy` | no | object | - |
| `conditions` | no | array | - |
| `applicableServiceTypes` | no | array | - |
