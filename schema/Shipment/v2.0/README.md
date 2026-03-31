# Shipment — v2.0

A Shipment represents the movement of one or more packages from an origin to a destination. It is the top-level fulfillment entity in a logistics transaction and maps to beckn:Fulfillment.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Shipment/attributes.yaml](https://schema.beckn.io/Shipment/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Shipment/v2.0/attributes.yaml](https://schema.beckn.io/Shipment/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Shipment/attributes.jsonschema.yaml](https://schema.beckn.io/Shipment/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Shipment/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Shipment/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Shipment/context.jsonld](https://schema.beckn.io/Shipment/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Shipment/v2.0/context.jsonld](https://schema.beckn.io/Shipment/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Shipment/vocab.jsonld](https://schema.beckn.io/Shipment/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Shipment/v2.0/vocab.jsonld](https://schema.beckn.io/Shipment/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Unique identifier for the shipment |
| `trackingId` | no | string | Public tracking identifier shared with sender/receiver |
| `status` | yes | string | Current status of the shipment |
| `origin` | yes | $ref: https://schema.beckn.io/Place/attributes.yaml#/components/schemas/Place | - |
| `destination` | yes | $ref: https://schema.beckn.io/Place/attributes.yaml#/components/schemas/Place | - |
| `packages` | no | array | List of packages in this shipment |
| `carrier` | no | $ref: https://schema.beckn.io/Carrier/attributes.yaml#/components/schemas/Carrier | - |
| `driver` | no | $ref: https://schema.beckn.io/Driver/attributes.yaml#/components/schemas/Driver | - |
| `vehicle` | no | $ref: https://schema.beckn.io/Vehicle/attributes.yaml#/components/schemas/Vehicle | - |
| `route` | no | $ref: https://schema.beckn.io/Route/attributes.yaml#/components/schemas/Route | - |
| `scheduledPickup` | no | string | Scheduled pickup time |
| `estimatedDelivery` | no | string | Estimated delivery date and time |
| `actualDelivery` | no | string | Actual delivery date and time |
| `deliverySlot` | no | $ref: https://schema.beckn.io/DeliverySlot/attributes.yaml#/components/schemas/DeliverySlot | - |
| `serviceType` | no | string | Type of logistics service |
| `specialInstructions` | no | string | Special handling instructions for the shipment |
| `proof` | no | $ref: https://schema.beckn.io/Proof/attributes.yaml#/components/schemas/Proof | - |
| `fare` | no | $ref: https://schema.beckn.io/Fare/attributes.yaml#/components/schemas/Fare | - |
| `receipt` | no | $ref: https://schema.beckn.io/Receipt/attributes.yaml#/components/schemas/Receipt | - |
| `cancellationPolicy` | no | $ref: https://schema.beckn.io/CancellationPolicy/attributes.yaml#/components/schemas/CancellationPolicy | - |
| `returnPolicy` | no | $ref: https://schema.beckn.io/ReturnPolicy/attributes.yaml#/components/schemas/ReturnPolicy | - |
| `alerts` | no | array | Alerts raised for this shipment |
| `trackingUpdates` | no | array | History of tracking updates |
| `createdAt` | no | string | Timestamp when shipment was created |
| `updatedAt` | no | string | Timestamp of last update |
