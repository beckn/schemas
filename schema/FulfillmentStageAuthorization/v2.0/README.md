# FulfillmentStageAuthorization — v2.0

Authorization required at a fulfillment stage.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [FulfillmentStageAuthorization](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `FulfillmentStageAuthorization` |

## Root linked-data files

The JSON-LD context and RDF vocabulary for this schema are consolidated at the schema root:

| File | Description |
|------|-------------|
| [schema/context.jsonld](../../context.jsonld) | Root JSON-LD context (all schemas, namespace: `https://schema.beckn.io/core/v2.0/`) |
| [schema/vocab.jsonld](../../vocab.jsonld) | Root RDF vocabulary (all schemas) |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `@context` | string | CPD |
| `@type` | string |  |
| `mediaFiles` | [MediaFile](../../MediaFile/README.md)[] | Media files required to enter or exit this fulfillment stage. The could be images of delivered packages, recorded video proof of installation, etc |
| `docs` | array | Documents required to enter or exit this fulfillment stage. The could be entry tickets, boarding passes, waybill, permits, certificates, credentials, etc |
| `authToken` | string | A human readable string that needs to be provided to enter or exit this fulfillment stage. Like an OTP |
