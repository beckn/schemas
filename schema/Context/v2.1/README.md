# Context — v2.1

The message envelope header that accompanies every Beckn API call, carrying network addressing, protocol version, action identification, transaction correlation identifiers, timing constraints, and optional cryptographic metadata required to route, authenticate, and correlate messages across the asynchronous Beckn communication pattern.

This version is aligned with the `Context` schema in `beckn.yaml`.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Context/v2.1/attributes.yaml](https://schema.beckn.io/Context/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Context/v2.1/context.jsonld](https://schema.beckn.io/Context/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Context/v2.1/vocab.jsonld](https://schema.beckn.io/Context/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Changes from v2.0

- **Removed:** `domain`, `location`.
- **Added:** `senderId` / `receiverId` (identities of the message sender / receiver — node identity on dedi.global by default, DIDs also supported), `senderUrl` / `receiverUrl` (their network addresses), and `try` (boolean two-phase preview flag for `update` / `cancel`).
- **Rewritten:** all property descriptions and the top-level description, aligned to `beckn.yaml`.

## Properties

| Property | Type | Description |
|---|---|---|
| `@context` | string | JSON-LD context reference |
| `@type` | string | JSON-LD type |
| `action` | string | The Beckn protocol method being invoked; MUST match the endpoint's path action. |
| `version` | string (const `2.0.0`) | Beckn protocol version for this transaction. |
| `bapId` | string | Verified namespace identifier of the CN on dedi.global. |
| `senderId` | string | Identity of the message sender — by default its node identity on dedi.global (`namespace_id/registry_id/record_id`); DIDs supported for ecosystems anchored elsewhere. |
| `senderUrl` | string (uri) | Network address (base URL) of the message sender. |
| `bapUri` | string (uri) | Callback base URL of the CN. |
| `bppId` | string | Verified namespace identifier of the PN on dedi.global. |
| `bppUri` | string (uri) | Request base URL of the PN. |
| `receiverId` | string | Identity of the message receiver — by default its node identity on dedi.global (`namespace_id/registry_id/record_id`); DIDs supported for ecosystems anchored elsewhere. |
| `receiverUrl` | string (uri) | Network address (base URL) of the message receiver. |
| `transactionId` | string (uuid) | Persists across all calls within a transaction session. |
| `messageId` | string (uuid) | Persists across a request and its callback. |
| `networkId` | string | Identifier of the Beckn subnet (e.g. `acmenet.org/charge-net`). |
| `timestamp` | string (date-time) | RFC 3339 message generation time. |
| `key` | string | Encryption public key of the sender. |
| `try` | boolean | Two-phase preview flag; applies to `update` / `cancel` only. |
| `ttl` | string | ISO 8601 validity duration after `timestamp`. |
| `schemaContext` | array of string (uri) | JSON-LD context URLs relevant to the request. |
| `requestDigest` | $ref: RequestDigest/v2.0 | BLAKE2b-512 hash of the originating request body. |

This schema defines all possible properties but imposes **no** required-field constraints; endpoint-specific validation is defined inline in operation request schemas.
