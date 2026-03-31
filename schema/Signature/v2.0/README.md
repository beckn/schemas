# Signature — v2.0

A digitally signed authentication credential in the HTTP `Authorization` header.
Follows draft-cavage-http-signatures-12 as profiled by BECKN-006.

Format:
```
Signature keyId="{subscriberId}|{uniqueKeyId}|{algorithm}",algorithm="{algorithm}",created="{unixTimestamp}",expires="{unixTimestamp}",headers="{signedHeaders}",signature="{base64Signature}"
```

| Attribute | Description |
|-----------|-------------|
| `keyId` | `{subscriberId}\|{uniqueKeyId}\|{algorithm}` — FQDN, registry UUID, signing algorithm |
| `algorithm` | MUST be `ed25519` |
| `created` | Unix timestamp when the signature was created |
| `expires` | Unix timestamp when the signature expires |
| `headers` | Space-separated signed headers. MUST include `(created)`, `(expires)`, `digest` |
| `signature` | Base64-encoded Ed25519 signature over the signing string |

Signing string:
`(created): {value}\n(expires): {value}\ndigest: BLAKE-512={digest}`
where `digest` is a BLAKE2b-512 hash of the request body, Base64-encoded.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Signature/attributes.yaml](https://schema.beckn.io/Signature/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Signature/v2.0/attributes.yaml](https://schema.beckn.io/Signature/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Signature/attributes.jsonschema.yaml](https://schema.beckn.io/Signature/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Signature/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Signature/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Signature/context.jsonld](https://schema.beckn.io/Signature/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Signature/v2.0/context.jsonld](https://schema.beckn.io/Signature/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Signature/vocab.jsonld](https://schema.beckn.io/Signature/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Signature/v2.0/vocab.jsonld](https://schema.beckn.io/Signature/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| _none_ | - | - | - |
