# Context — v2.0

Every API call in Beckn protocol has a context. It provides a high-level overview to the receiver about the nature of the intended transaction. Typically, it is the BAP that sets the transaction context based on the consumer's location and action on their UI. The context object contains four types of fields: (1) demographic information about the transaction using fields like domain, country, and region; (2) addressing details like the sending and receiving platform's ID and API URL; (3) interoperability information like the protocol version implemented by the sender; and (4) transaction details like the method being called at the receiver's endpoint, the transaction_id that represents an end-to-end user session at the BAP, a message ID to pair requests with callbacks, a timestamp to capture sending times, a ttl to specify the validity of the request, and a key to encrypt information if necessary.

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
| `action` | yes | $ref: https://schema.beckn.io/BecknEndpoint/attributes.yaml#/components/schemas/BecknEndpoint | The Beckn endpoint being called. Must conform to BecknEndpoint format. |
| `bapId` | yes | string | A globally unique identifier of the BAP. Typically the fully qualified domain name (FQDN) of the BAP. |
| `bapUri` | yes | string | API URL of the BAP for accepting callbacks from BPPs. |
| `bppId` | no | string | A globally unique identifier of the BPP. Typically the fully qualified domain name (FQDN) of the BPP. |
| `bppUri` | no | string | API URL of the BPP for accepting calls from BAPs. |
| `messageId` | yes | string | A unique value which persists during a request/callback cycle. BAPs use this value to match an incoming callback from a BPP to an earlier call. Generate a fresh message_id for every new interaction. |
| `networkId` | no | string | A unique identifier representing a group of platforms. By default, the URL of the network registry on the Beckn network. |
| `timestamp` | yes | string | Time of request generation in RFC3339 format. |
| `transactionId` | yes | string | A unique value which persists across all API calls from discover through confirm. Used to indicate an active user session across multiple requests. |
| `try` | no | boolean | A flag to indicate that this request is intended to try an operation. Set to false by default. Set to true when negotiating terms, updating, or cancelling an active contract. When true, the receiver responds with the expected consequences per the terms of service agreed during init/on_init. |
| `ttl` | no | string | The duration in ISO8601 format after timestamp for which this message holds valid. |
| `version` | yes | string | Version of Beckn protocol being used by the sender. |
| `lineage` | no | array | An optional array of causal attribution records asserting that this Beckn transaction was triggered by one or more upstream Beckn interactions. Present only at transaction boundaries. MUST NOT be populated within subsequent steps of the same transaction. Per current Beckn profiles, this array MUST contain at most one entry when present. |
