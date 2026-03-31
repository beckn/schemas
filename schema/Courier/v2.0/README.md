# Courier — v2.0

A Courier is an individual delivery agent responsible for last-mile pickup and delivery of packages, typically in hyperlocal or urban delivery contexts. Maps to beckn:Agent.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Courier/attributes.yaml](https://schema.beckn.io/Courier/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Courier/v2.0/attributes.yaml](https://schema.beckn.io/Courier/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Courier/attributes.jsonschema.yaml](https://schema.beckn.io/Courier/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/Courier/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/Courier/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/Courier/context.jsonld](https://schema.beckn.io/Courier/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Courier/v2.0/context.jsonld](https://schema.beckn.io/Courier/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Courier/vocab.jsonld](https://schema.beckn.io/Courier/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Courier/v2.0/vocab.jsonld](https://schema.beckn.io/Courier/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Unique courier identifier |
| `name` | yes | string | Full name of the courier |
| `phone` | no | string | Contact phone number |
| `email` | no | string | Email address |
| `profilePhoto` | no | string | URL to courier's profile photo |
| `rating` | no | number | Average rating (1-5) |
| `vehicleType` | no | string | Type of vehicle used |
| `vehicleNumber` | no | string | Vehicle registration number |
| `currentLocation` | no | $ref: https://schema.beckn.io/Place/attributes.yaml#/components/schemas/Place | - |
| `status` | no | string | - |
| `activeShipments` | no | array | Currently assigned shipments |
| `kycVerified` | no | boolean | Whether courier has completed KYC verification |
| `joiningDate` | no | string | Date the courier joined the network |
