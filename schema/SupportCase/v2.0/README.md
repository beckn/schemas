# SupportCase — v2.0

A domain-agnostic customer support ticket used to record an issue raised between parties — its category, priority, lifecycle status, supporting attachments, and support interaction sessions. It is independent of any particular domain; domain-specific values are carried via the `category` descriptor and the extensible attribute bags.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/SupportCase/v2.0/attributes.yaml](https://schema.beckn.io/SupportCase/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/SupportCase/v2.0/context.jsonld](https://schema.beckn.io/SupportCase/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/SupportCase/v2.0/vocab.jsonld](https://schema.beckn.io/SupportCase/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Design notes

- **`category`** (Descriptor) classifies the issue — the domain defines the code.
- **`priority`** is an open-enum string — suggested values `P1`, `P2`, `P3`, with custom values allowed.
- **`status`** is a Descriptor with `code` ∈ `UNRESOLVED`, `RESOLVED` (default `UNRESOLVED`).
- **`attachments`** reuse `Document/v2.0`; **`sessions`** capture support interactions over a `CommunicationChannel` with associated `MediaFile` data.

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context reference |
| `@type` | yes | string | JSON-LD type |
| `id` | yes | string | Stable support case identifier. |
| `category` | yes | $ref: Descriptor/v2.1 | Issue category; `code` defined by the domain. |
| `description` | no | string | Human-readable description of the issue. |
| `priority` | no | string (open enum) | Priority; suggested `P1`/`P2`/`P3`, custom values allowed. |
| `status` | no | allOf: Descriptor (code ∈ UNRESOLVED, RESOLVED; default UNRESOLVED) | Lifecycle state of the case. |
| `raisedBy` | no | string | Party who raised the case. |
| `assignedAgent` | no | string | Support agent the case is assigned to. |
| `attachments` | no | array of Document/v2.0 | Supporting attachments / evidence. |
| `sessions` | no | array of `{ id, supportChannel, data }` | Support interaction sessions. `supportChannel` is a CommunicationChannel/v2.0; `data` is a MediaFile/v2.0. |
| `claimAmount` | no | number | Amount claimed, if any. |
| `resolution` | no | string | Resolution details, once resolved. |
| `createdAt` | no | string (date-time) | When the case was created. |
| `resolvedAt` | no | string (date-time) | When the case was resolved. |
