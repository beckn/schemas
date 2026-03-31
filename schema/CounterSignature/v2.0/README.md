# CounterSignature — v2.0

A signed receipt transmitted in the synchronous `Ack` response body, proving that the
receiver authenticated, received, and processed the inbound request.

`CounterSignature` shares the same wire format as `Signature` but differs:
- **Signer**: the response receiver (not the request sender)
- **Location**: transmitted in the `Ack` response body (not in the `Authorization` header)
- **`digest`**: covers the Ack response body (not the inbound request body)
- **`(request-digest)`** and **`(message-id)`** MUST be included in the signing string

Signing string format:
```
(created): {unixTimestamp}
(expires): {unixTimestamp}
digest: BLAKE-512={base64DigestOfAckBody}
(request-digest): BLAKE-512={base64DigestOfInboundRequestBody}
(message-id): {messageId}
```

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CounterSignature/attributes.yaml](https://schema.beckn.io/CounterSignature/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CounterSignature/v2.0/attributes.yaml](https://schema.beckn.io/CounterSignature/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CounterSignature/attributes.jsonschema.yaml](https://schema.beckn.io/CounterSignature/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CounterSignature/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CounterSignature/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CounterSignature/context.jsonld](https://schema.beckn.io/CounterSignature/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CounterSignature/v2.0/context.jsonld](https://schema.beckn.io/CounterSignature/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CounterSignature/vocab.jsonld](https://schema.beckn.io/CounterSignature/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CounterSignature/v2.0/vocab.jsonld](https://schema.beckn.io/CounterSignature/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| _none_ | - | - | - |
