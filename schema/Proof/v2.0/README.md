# Proof — v2.0

Proof of delivery or pickup evidence, including photos, signatures, OTP confirmations, or digital receipts. Maps to beckn:Document.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Proof/attributes.yaml](https://schema.beckn.io/Proof/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Proof/v2.0/attributes.yaml](https://schema.beckn.io/Proof/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Proof/attributes.jsonschema.yaml](https://schema.beckn.io/Proof/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Proof/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Proof/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Proof/context.jsonld](https://schema.beckn.io/Proof/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Proof/v2.0/context.jsonld](https://schema.beckn.io/Proof/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Proof/vocab.jsonld](https://schema.beckn.io/Proof/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Proof/v2.0/vocab.jsonld](https://schema.beckn.io/Proof/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `shipmentId` | no | string | - |
| `type` | yes | string | - |
| `subType` | no | string | What was captured |
| `mediaUrl` | no | string | URL to proof media (photo/signature image) |
| `signatureData` | no | string | Base64-encoded signature data |
| `otpVerified` | no | boolean | Whether OTP was verified for delivery |
| `recipientName` | no | string | Name of person who received the package |
| `recipientRelation` | no | string | Relation to consignee if not consignee |
| `location` | no | object | - |
| `timestamp` | yes | string | - |
| `driverSignoff` | no | boolean | Driver confirmed successful delivery |
