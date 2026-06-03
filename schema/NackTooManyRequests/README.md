# NackTooManyRequests

The synchronous rejection body returned when the responding NP has exceeded a request rate limit (AUT_RATE_LIMITED) or a policy-governed engagement capacity limit (POL_NP_CAPACITY_EXCEEDED). The caller MUST apply back-off before retrying. Implementations SHOULD include a Retry-After header on 429 responses.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.yaml](https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.yaml) | [https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/NackTooManyRequests/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/NackTooManyRequests/v2.0/context.jsonld](https://schema.beckn.io/NackTooManyRequests/v2.0/context.jsonld) | [https://schema.beckn.io/NackTooManyRequests/v2.0/vocab.jsonld](https://schema.beckn.io/NackTooManyRequests/v2.0/vocab.jsonld) | [https://schema.beckn.io/NackTooManyRequests/v2.0/README.md](https://schema.beckn.io/NackTooManyRequests/v2.0/README.md) |
