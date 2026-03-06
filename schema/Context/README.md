# Context

> **Canonical IRI:** [`https://schema.beckn.io/Context`](https://schema.beckn.io/Context)
> **Tags:** `common`
> **Namespace:** `https://schema.beckn.io/`
> Part of the [Beckn Protocol Core Schema](../../README.md)

---

Every API call in Beckn protocol has a context. It provides a high-level overview to the receiver about the nature of the intended transaction. Typically, it is the BAP that sets the transaction context based on the consumer's location and action on their UI. The context object contains four types of fields: (1) demographic information about the transaction using fields like domain, country, and region; (2) addressing details like the sending and receiving platform's ID and API URL; (3) interoperability information like the protocol version implemented by the sender; and (4) transaction details like the method being called at the receiver's endpoint, the transaction_id that represents an end-to-end user session at the BAP, a message ID to pair requests with callbacks, a timestamp to capture sending times, a ttl to specify the validity of the request, and a key to encrypt information if necessary.

## Versions

| Version | attributes.yaml | context.jsonld | vocab.jsonld | README |
|---------|----------------|----------------|--------------|--------|
| **v2.0** | [attributes.yaml](./v2.0/attributes.yaml) | [context.jsonld](./v2.0/context.jsonld) | [vocab.jsonld](./v2.0/vocab.jsonld) | [README](./v2.0/README.md) |

## Properties (latest: v2.0)

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `action` | object | ✅ | The Beckn endpoint being called. Must conform to BecknEndpoint format. |
| `bapId` | `string` | ✅ | A globally unique identifier of the BAP. Typically the fully qualified domain name (FQDN) of the BAP. |
| `bapUri` | `string` (uri) | ✅ | API URL of the BAP for accepting callbacks from BPPs. |
| `bppId` | `string` | — | A globally unique identifier of the BPP. Typically the fully qualified domain name (FQDN) of the BPP. |
| `bppUri` | `string` (uri) | — | API URL of the BPP for accepting calls from BAPs. |
| `messageId` | `string` (uuid) | ✅ | A unique value which persists during a request/callback cycle. BAPs use this value to match an incoming callback from a BPP to an earlier call. Gen… |
| `networkId` | `string` | — | A unique identifier representing a group of platforms. By default, the URL of the network registry on the Beckn network. |
| `timestamp` | `string` (date-time) | ✅ | Time of request generation in RFC3339 format. |
| `transactionId` | `string` (uuid) | ✅ | A unique value which persists across all API calls from discover through confirm. Used to indicate an active user session across multiple requests. |
| `try` | `boolean` | — | A flag to indicate that this request is intended to try an operation. Set to false by default. Set to true when negotiating terms, updating, or can… |
| `ttl` | `string` | — | The duration in ISO8601 format after timestamp for which this message holds valid. |
| `version` | `string` | ✅ | Version of Beckn protocol being used by the sender. |
| `lineage` | any[] | — | An optional array of causal attribution records asserting that this Beckn transaction was triggered by one or more upstream Beckn interactions. Pre… |

## Linked Data

| Resource | URL |
|----------|-----|
| Canonical IRI | `https://schema.beckn.io/Context` |
| JSON Schema (latest) | `https://schema.beckn.io/Context/2.0` |
| context.jsonld (latest) | `https://schema.beckn.io/Context/2.0/context.jsonld` |
| vocab.jsonld (latest) | `https://schema.beckn.io/Context/2.0/vocab.jsonld` |
| Root context.jsonld | `https://schema.beckn.io/context.jsonld` |
| Root vocab.jsonld | `https://schema.beckn.io/vocab.jsonld` |
