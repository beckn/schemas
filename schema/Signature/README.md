# Signature

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

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/Signature/v2.0/attributes.yaml](https://schema.beckn.io/Signature/v2.0/attributes.yaml) | [https://schema.beckn.io/Signature/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Signature/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/Signature/v2.0/context.jsonld](https://schema.beckn.io/Signature/v2.0/context.jsonld) | [https://schema.beckn.io/Signature/v2.0/vocab.jsonld](https://schema.beckn.io/Signature/v2.0/vocab.jsonld) | [https://schema.beckn.io/Signature/v2.0/README.md](https://schema.beckn.io/Signature/v2.0/README.md) |
