# LogisticsReceipt — v2.0

Digital acknowledgment of payment and delivery for a logistics service.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LogisticsReceipt/attributes.yaml](https://schema.beckn.io/LogisticsReceipt/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LogisticsReceipt/v2.0/attributes.yaml](https://schema.beckn.io/LogisticsReceipt/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LogisticsReceipt/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsReceipt/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LogisticsReceipt/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsReceipt/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LogisticsReceipt/context.jsonld](https://schema.beckn.io/LogisticsReceipt/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LogisticsReceipt/v2.0/context.jsonld](https://schema.beckn.io/LogisticsReceipt/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LogisticsReceipt/vocab.jsonld](https://schema.beckn.io/LogisticsReceipt/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LogisticsReceipt/v2.0/vocab.jsonld](https://schema.beckn.io/LogisticsReceipt/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | - |
| `shipmentId` | yes | string | - |
| `invoiceNumber` | no | string | - |
| `issuedAt` | no | string | - |
| `fare` | yes | $ref: https://schema.beckn.io/Fare/v2.0/attributes.yaml#/components/schemas/Fare | - |
| `paymentMode` | no | string | - |
| `paymentTransactionId` | no | string | - |
| `paidAt` | no | string | - |
| `shipper` | no | $ref: https://schema.beckn.io/Contact/v2.0/attributes.yaml#/components/schemas/Contact | - |
| `consignee` | no | $ref: https://schema.beckn.io/Contact/v2.0/attributes.yaml#/components/schemas/Contact | - |
| `carrier` | no | $ref: https://schema.beckn.io/Carrier/v2.0/attributes.yaml#/components/schemas/Carrier | - |
| `deliveryProof` | no | $ref: https://schema.beckn.io/Proof/v2.0/attributes.yaml#/components/schemas/Proof | - |
| `downloadUrl` | no | string | URL to download PDF receipt |
