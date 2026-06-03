# CallbackSignature

A digitally signed authentication credential transmitted in the HTTP Authorization header of PN solicited callbacks to CN `/on_*` endpoints. Extends the standard Signature by chaining the PN's signature to the CN's original request signature, allowing the CN to verify that the callback is a genuine response to a request it sent.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/CallbackSignature/v2.0/attributes.yaml](https://schema.beckn.io/CallbackSignature/v2.0/attributes.yaml) | [https://schema.beckn.io/CallbackSignature/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/CallbackSignature/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/CallbackSignature/v2.0/context.jsonld](https://schema.beckn.io/CallbackSignature/v2.0/context.jsonld) | [https://schema.beckn.io/CallbackSignature/v2.0/vocab.jsonld](https://schema.beckn.io/CallbackSignature/v2.0/vocab.jsonld) | [https://schema.beckn.io/CallbackSignature/v2.0/README.md](https://schema.beckn.io/CallbackSignature/v2.0/README.md) |
