# RetailItem

A minimal retail item schema for use in Contract.commitments[].commitmentAttributes.

RetailItem is the foundational schema for items in retail transactions.
It extends beckn:Resource with the core retail item properties: price, quantity,
and verifiable credentials. Domain-specific schemas (e.g. FoodAndBeverageItem)
extend RetailItem with additional domain-specific attributes.

Inheritance: beckn:Resource ← beckn:RetailItem
Use in: beckn:Commitment.commitmentAttributes for retail orders

## Versions

| Version | attributes.yaml | attributes.jsonschema.yaml | context.jsonld | vocab.jsonld | README |
|---|---|---|---|---|---|
| **v2.1** | [https://schema.beckn.io/RetailItem/v2.1/attributes.yaml](https://schema.beckn.io/RetailItem/v2.1/attributes.yaml) | [https://schema.beckn.io/RetailItem/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/RetailItem/v2.1/attributes.jsonschema.yaml) | [https://schema.beckn.io/RetailItem/v2.1/context.jsonld](https://schema.beckn.io/RetailItem/v2.1/context.jsonld) | [https://schema.beckn.io/RetailItem/v2.1/vocab.jsonld](https://schema.beckn.io/RetailItem/v2.1/vocab.jsonld) | [https://schema.beckn.io/RetailItem/v2.1/README.md](https://schema.beckn.io/RetailItem/v2.1/README.md) |
