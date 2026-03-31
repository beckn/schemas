# Context

Every API call in Beckn protocol has a context. It provides a high-level overview to the receiver about the nature of the intended transaction. Typically, it is the BAP that sets the transaction context based on the consumer's location and action on their UI. The context object contains four types of fields: (1) demographic information about the transaction using fields like domain, country, and region; (2) addressing details like the sending and receiving platform's ID and API URL; (3) interoperability information like the protocol version implemented by the sender; and (4) transaction details like the method being called at the receiver's endpoint, the transaction_id that represents an end-to-end user session at the BAP, a message ID to pair requests with callbacks, a timestamp to capture sending times, a ttl to specify the validity of the request, and a key to encrypt information if necessary.

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.0** | [https://schema.beckn.io/Context/v2.0/attributes.yaml](https://schema.beckn.io/Context/v2.0/attributes.yaml) | [https://schema.beckn.io/Context/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Context/v2.0/attributes.jsonschema.yaml) | [https://schema.beckn.io/Context/v2.0/context.jsonld](https://schema.beckn.io/Context/v2.0/context.jsonld) | [https://schema.beckn.io/Context/v2.0/vocab.jsonld](https://schema.beckn.io/Context/v2.0/vocab.jsonld) | [https://schema.beckn.io/Context/v2.0/README.md](https://schema.beckn.io/Context/v2.0/README.md) |
