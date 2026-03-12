# Support — v2.0

Support request payload sent by a BAP to a BPP in the `/beckn/support` call.
Used to request support contact information, report an issue, or open a
support ticket for an existing order.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [Support](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `Support` |
| [context.jsonld](./context.jsonld) | JSON-LD context mapping properties to beckn IRIs |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary declaration for this schema |

## Properties

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI. |
| `@type` | `string` | ✅ | Must be `Support`. |
| `orderId` | `string` | — | The order against which support is required. |
| `ticketIds` | `array` | — | IDs of existing support tickets for this order. |
| `callbackPhone` | `string` | — | Telephone number of the user for a support callback. |
| `issue` | `string` | — | Free-text description of the issue requiring support. |
| `issueCode` | `string` | — | Structured issue category code (domain-defined). |
