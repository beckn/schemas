# LogisticsVehicle — v2.0

A Vehicle is a transport asset used for logistics operations. Vehicle types range from bicycles for hyperlocal delivery to heavy trucks for long haul freight. Maps to beckn:Asset.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/LogisticsVehicle/attributes.yaml](https://schema.beckn.io/LogisticsVehicle/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/LogisticsVehicle/v2.0/attributes.yaml](https://schema.beckn.io/LogisticsVehicle/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/LogisticsVehicle/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsVehicle/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/LogisticsVehicle/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/LogisticsVehicle/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/LogisticsVehicle/context.jsonld](https://schema.beckn.io/LogisticsVehicle/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/LogisticsVehicle/v2.0/context.jsonld](https://schema.beckn.io/LogisticsVehicle/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/LogisticsVehicle/vocab.jsonld](https://schema.beckn.io/LogisticsVehicle/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/LogisticsVehicle/v2.0/vocab.jsonld](https://schema.beckn.io/LogisticsVehicle/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `id` | yes | string | Unique vehicle identifier |
| `registrationNumber` | yes | string | Vehicle registration/license plate number |
| `type` | yes | string | Type of vehicle |
| `make` | no | string | Vehicle manufacturer |
| `model` | no | string | Vehicle model |
| `year` | no | integer | Year of manufacture |
| `color` | no | string | - |
| `fuelType` | no | string | - |
| `payloadCapacity` | no | object | Maximum cargo capacity |
| `volumeCapacity` | no | object | Cargo volume capacity |
| `hasRefrigeration` | no | boolean | Whether vehicle has refrigeration (cold chain) |
| `gpsEnabled` | no | boolean | Whether vehicle has GPS tracking |
| `insuranceExpiry` | no | string | - |
| `pollutionCertExpiry` | no | string | - |
| `fitnessExpiry` | no | string | - |
| `currentLocation` | no | object | - |
| `status` | no | string | - |
