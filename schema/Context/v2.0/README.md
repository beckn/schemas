# Context — v2.0

Base context schema for all Beckn API calls. Contains addressing information
(BAP/BPP identifiers and API URLs), protocol version, the action being called,
transaction and message IDs, timestamp, TTL, and optional encryption key.
This schema defines all possible properties but imposes NO required-field
constraints. Endpoint-specific validation is defined inline in operation request schemas.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Context/attributes.yaml](https://schema.beckn.io/Context/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Context/v2.0/attributes.yaml](https://schema.beckn.io/Context/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Context/attributes.jsonschema.yaml](https://schema.beckn.io/Context/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Context/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Context/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Context/context.jsonld](https://schema.beckn.io/Context/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Context/v2.0/context.jsonld](https://schema.beckn.io/Context/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Context/vocab.jsonld](https://schema.beckn.io/Context/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Context/v2.0/vocab.jsonld](https://schema.beckn.io/Context/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `domain` | no | string | Domain code that is relevant to this transaction context |
| `location` | no | object | The location where the transaction is intended to be fulfilled. |
| `action` | no | string | The Beckn protocol method being called by the sender and executed at the receiver. |
| `version` | no | string | Version of transaction protocol being used by the sender. |
| `bapId` | no | string | Subscriber ID of the BAP as registered on dedi.global |
| `bapUri` | no | string | The callback URL of the BAP.  REQUIRED: This should necessarily contain the same domain name as verified in its namespace under dedi.global, and MUST have the same URL as registered in its subscriber registry on dedi.global |
| `bppId` | no | string | Subscriber ID of the BPP as registered on dedi.global |
| `bppUri` | no | string | The request URL of the BPP.  REQUIRED: This MUST contain the same domain name as verified in its namespace under dedi.global, and MUST have the same URL as registered in its subscriber registry on dedi.global |
| `transactionId` | no | string | This is a unique value which persists across all API calls from `search` through `confirm`. This is done to indicate an active user session across multiple requests. The BPPs can use this value to push personalized recommendations, and dynamic offerings related to an ongoing transaction despite being unaware of the user active on the BAP. |
| `messageId` | no | string | This is a unique value which persists during a request / callback cycle. Since beckn protocol APIs are asynchronous, BAPs need a common value to match an incoming callback from a BPP to an earlier call. This value can also be used to ignore duplicate messages coming from the BPP. It is recommended to generate a fresh message_id for every new interaction. When sending unsolicited callbacks, BPPs must generate a new message_id. |
| `networkId` | no | string | Unique identifier of a network. This identifier ALWAYS represents a specific beckn registry in a specific namespace on dedi.global. Format : `{namespace_id}/{registry_id}@{dedi-host}`. The `@{dedi-host}` suffix is optional. If it is not present, the network is assumed to be registered on dedi.glounique Example: Assuming acmenet.org is the namespace, and registry_name = charge-net, so networkId should be `acmenet.org/charge-net` |
| `timestamp` | no | string | Time of request generation in RFC3339 format |
| `key` | no | string | The encryption public key of the sender |
| `ttl` | no | string | The duration in ISO8601 format after timestamp for which this message holds valid |
| `schemaContext` | no | array | Array of JSON-LD context urls representing the schemas relevant to the request in which this context object is transported. |
| `requestDigest` | no | $ref: https://schema.beckn.io/RequestDigest/v2.0/attributes.yaml#/components/schemas/RequestDigest | - |
