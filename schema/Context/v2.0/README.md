# Context — v2.0

The transaction context object carried in every API request.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Context](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Context` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `action` | Action |  |
| `bapId` | string | A globally unique identifier of the BAP, Typically it is the fully qualified domain name (FQDN) of the BAP |
| `bapUri` | string | API URL of the BAP for accepting callbacks from BPPs. |
| `bppId` | string | A globally unique identifier of the BAP, Typically it is the fully qualified domain name (FQDN) of the BAP |
| `bppUri` | string | API URL of the BPP for accepting calls from BAPs. |
| `messageId` | string | This is a unique value which persists during a request / callback cycle. Since beckn protocol APIs are asynchronous, BAPs need a common value to match an incoming callback from a BPP to an earlier call. This value can also be used to ignore duplicate messages coming from the BPP. It is recommended to generate a fresh message_id for every new interaction. When sending unsolicited callbacks, BPPs must generate a new message_id. |
| `networkId` | string | A unique identifier representing a group of platforms. By default, it is the url of the network registry on the Beckn network |
| `timestamp` | string | Time of request generation in RFC3339 format |
| `transactionId` | string | This is a unique value which persists across all API calls from `search` through `confirm`. This is done to indicate an active user session across multiple requests. The BPPs can use this value to push personalized recommendations, and dynamic offerings related to an ongoing transaction despite being unaware of the user active on the BAP. |
| `try` | boolean | A flag to indicate that this request is intended to 'try' an operation. Typically set to `false` by default, but set to `true` when negotiating terms, updating or cancelling an active order. When set to `true`, the receiver must respond with the expected consequences as per the terms of service initially agreed between the BAP and the BPP during the `init/on_init` cycle. For example, A BAP will set this flag to `true` when requesting the BPP to cancel the order. Upon receiving this the BPP could respond with updated cost, cancellation fees, reasons for cancellation, a cancellation form, payment links, and any additional notifications or prompts informing the BAP about future consequences if continued (like an account ban, or reduced rating). When both participants are ready to continue the transaction, this flag MUST be set back to `false`. |
| `ttl` | string | The duration in ISO8601 format after timestamp for which this message holds valid |
| `version` | string | Version of beckn protocol being used by the sender |
