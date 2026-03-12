# SupportResponse — v2.0

Support response payload returned by a BPP to a BAP in the `/beckn/on_support`
callback. Contains the support ticket reference, available contact channels,
SLA commitment, and optional consumer acknowledgement details.

Part of the [Beckn Protocol Core Schema](../../../README.md) · [SupportResponse](../README.md)

## Files

| File | Description |
|------|-------------|
| [attributes.yaml](./attributes.yaml) | OpenAPI 3.1.1 component definition for `SupportResponse` |
| [context.jsonld](./context.jsonld) | JSON-LD context mapping properties to beckn IRIs |
| [vocab.jsonld](./vocab.jsonld) | RDF vocabulary declaration for this schema |

## Properties

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `@context` | `string` (uri) | ✅ | JSON-LD context URI. |
| `@type` | `string` | ✅ | Must be `beckn:SupportResponse`. |
| `refId` | `string` | — | Reference identifier against which support was requested. |
| `ticketId` | `string` | — | Support ticket identifier assigned by the BPP. |
| `descriptor` | `Descriptor` | — | Human-readable label for this support response. |
| `channels` | `array` | — | Available support channels with contact details. |
| `sla` | `object` | — | Service level agreement for this support response. |
| `consumer` | `Consumer` | — | The consumer the support response is addressed to. |
