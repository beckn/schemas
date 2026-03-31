# CounterSignature

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

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/CounterSignature/v2.0/attributes.yaml](https://schema.beckn.io/CounterSignature/v2.0/attributes.yaml) | [https://schema.beckn.io/CounterSignature/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CounterSignature/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/CounterSignature/v2.0/context.jsonld](https://schema.beckn.io/CounterSignature/v2.0/context.jsonld) | [https://schema.beckn.io/CounterSignature/v2.0/vocab.jsonld](https://schema.beckn.io/CounterSignature/v2.0/vocab.jsonld) | [https://schema.beckn.io/CounterSignature/v2.0/README.md](https://schema.beckn.io/CounterSignature/v2.0/README.md) |
