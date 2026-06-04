# Dispute — v2.0

A Dispute is a formal disagreement raised by one node (the **claimant**) against another (the **respondent**) over any piece of information published on the network. **Anything can be disputed** — a `Contract`, an `Invoice`, a `Settlement`, a `Performance`, a `Consideration`, contract terms, or any other published object. A dispute itemises one or more **cases**, each backed by a **reason** and **supporting evidence**, and tracks its lifecycle from unresolved through to resolved or withdrawn. It is exchanged over the `dispute` / `on_dispute` endpoints, wrapped in a [`DisputeAction`](../../DisputeAction/v2.0/).

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Dispute/attributes.yaml](https://schema.beckn.io/Dispute/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Dispute/v2.0/attributes.yaml](https://schema.beckn.io/Dispute/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Dispute/context.jsonld](https://schema.beckn.io/Dispute/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Dispute/v2.0/context.jsonld](https://schema.beckn.io/Dispute/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Dispute/vocab.jsonld](https://schema.beckn.io/Dispute/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Dispute/v2.0/vocab.jsonld](https://schema.beckn.io/Dispute/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Model

Dispute is a **generic** object: it is not tied to invoicing. Any published artifact can be disputed by another node. It deliberately mirrors the `Invoice` shape — a two-party pair plus an itemised, individually-status-tracked list.

- **Parties** — `claimant` (raises the dispute) and `respondent` (the dispute is against), each a `Participant`.
- **ODR provider** — `odrProvider` (a `Participant`) is the neutral third party. Dispute resolution is a **tri-party** arrangement; claimant and respondent must agree on this provider (which may happen after the dispute is raised, so it is optional). Its `descriptor.code` carries the resolution role: `MEDIATOR`, `ARBITRATOR`, `CONCILIATOR`, `ADJUDICATOR`, `OMBUDSMAN`, `NEUTRAL_EVALUATOR`, `EXPERT`.
- **Support precondition** — `supportCases` is a **required** array of [`SupportCase`](../../SupportCase/v2.0/) with `minItems: 1` and a `contains` rule requiring **at least one ticket whose `status.code` is `UNRESOLVED`**. A dispute therefore cannot be raised until the parties have an open, unresolved support case — escalation must follow an attempted support resolution.
- **Cases** — `cases` is an array of `{ case, status }`. Each `case` is `{ subject, reason, evidence }`:
  - `subject` → an `Attributes` JSON-LD bag whose `@type` identifies what is disputed (`Contract`, `Invoice`, `Settlement`, `Performance`, `Consideration`, `ContractTerms`, …); the object may be embedded or referenced by URL.
  - `reason` → a `Descriptor` (**required**).
  - `evidence` → an array of `Document` (**required, minItems 1**). `Document` carries `url` + `mimeType` + `label` + `security`, so it holds both machine-readable proofs (e.g. verifiable credentials) and human-readable ones — images, audio, video, chat logs, emails, off-network artifacts. A case without any attached proof, even circumstantial, may be **rejected at the respondent's discretion**.
- **Lifecycle** — `status.code` ∈ `UNRESOLVED`, `RESOLVED`, `WITHDRAWN` (default `UNRESOLVED`); `WITHDRAWN` is a claimant cancellation. Each case's `status.code` ∈ `UNRESOLVED`, `RESOLVED` (default `UNRESOLVED`).

### History / audit

Disputes can be created, updated, status-tracked, and cancelled. **Both nodes are expected to persist their own history of each dispute** (who changed what, and when) for audit and reconciliation. This change log is **node-local** and is intentionally **not** part of the wire schema — only the current state of the dispute travels between nodes.

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context reference |
| `@type` | yes | string | JSON-LD type |
| `id` | yes | string (uuid) | Stable dispute identifier (system id). |
| `raisedAt` | no | string (date-time) | Timestamp at which the dispute was raised. |
| `descriptor` | no | $ref: Descriptor/v2.1 | Describes the nature of the dispute. |
| `status` | no | allOf: Descriptor (code ∈ UNRESOLVED, RESOLVED, WITHDRAWN; default UNRESOLVED) | Lifecycle state of the dispute. |
| `claimant` | yes | $ref: Participant/v2.0 | The party that raises the dispute. |
| `respondent` | yes | $ref: Participant/v2.0 | The party against whom the dispute is raised. |
| `odrProvider` | no | allOf: Participant (descriptor.code ∈ MEDIATOR, ARBITRATOR, CONCILIATOR, ADJUDICATOR, OMBUDSMAN, NEUTRAL_EVALUATOR, EXPERT) | The agreed neutral ODR provider. |
| `supportCases` | yes | array of SupportCase/v2.0 (minItems 1, contains ≥1 UNRESOLVED) | The support tickets underpinning the dispute. At least one must be UNRESOLVED — a dispute cannot be raised without it. |
| `cases` | yes | array of `{ case, status }` | The disputed matters. `case` = { subject (Attributes @type), reason (Descriptor), evidence (Document[]) }; `status` ∈ UNRESOLVED, RESOLVED. |
| `disputeAttributes` | no | $ref: Attributes/v2.0 | Domain-specific extension attributes. |
