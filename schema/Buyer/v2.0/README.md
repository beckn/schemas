# Buyer — v2.0

Schema definition for Buyer in the Beckn Protocol

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Buyer/attributes.yaml](https://schema.beckn.io/Buyer/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Buyer/v2.0/attributes.yaml](https://schema.beckn.io/Buyer/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Buyer/attributes.jsonschema.yaml](https://schema.beckn.io/Buyer/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Buyer/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Buyer/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Buyer/context.jsonld](https://schema.beckn.io/Buyer/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Buyer/v2.0/context.jsonld](https://schema.beckn.io/Buyer/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Buyer/vocab.jsonld](https://schema.beckn.io/Buyer/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Buyer/v2.0/vocab.jsonld](https://schema.beckn.io/Buyer/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | - |
| `@type` | yes | string | - |
| `beckn:id` | yes | string | Unique identifier for the buyer (personId or orgId in legacy schema) |
| `beckn:role` | no | string | The functional role of the buyer in the transaction. |
| `beckn:displayName` | no | string | Human-readable display name |
| `beckn:telephone` | no | string | Telephone number |
| `beckn:email` | no | string | Email Address |
| `beckn:taxID` | no | string | Tax identifier for the buyer. |
| `beckn:buyerAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Attribute Pack reference for richer identity: # buyer/identity.v1 (contact details: email, phone, address) # buyer/org-ids.v1 (LEI, GSTIN, ISIN, CUSIP…) # buyer/kyc.v1 (jurisdictional compliance fields) # buyer/preferences.v1 (delivery preferences, accessibility needs, etc.)  |
