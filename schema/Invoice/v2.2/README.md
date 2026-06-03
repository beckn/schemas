# Invoice — v2.2

An Invoice is a financial statement issued by a creditor to a debtor that itemises the amounts owed and records how they are settled. Each statement entry is a billed financial entry — an order, refund, commission, finder fee, or adjustment — rather than a product or service. The invoice tracks its lifecycle status, the agreed settlement terms, and the proofs of settlement (payment actions) that discharge the amount due. It is exchanged over the `invoice` / `on_invoice` endpoints, where one node invoices another.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/Invoice/attributes.yaml](https://schema.beckn.io/Invoice/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/Invoice/v2.2/attributes.yaml](https://schema.beckn.io/Invoice/v2.2/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/Invoice/context.jsonld](https://schema.beckn.io/Invoice/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/Invoice/v2.2/context.jsonld](https://schema.beckn.io/Invoice/v2.2/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/Invoice/vocab.jsonld](https://schema.beckn.io/Invoice/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/Invoice/v2.2/vocab.jsonld](https://schema.beckn.io/Invoice/v2.2/vocab.jsonld) | RDF vocabulary (versioned path) |

## Model

Invoice is an **independent** schema (not a specialisation of `Contract`). It borrows the useful ideas — a creditor/debtor pair, an itemised statement, and explicit settlement — without inheriting Contract's commerce-shaped `commitments` / `offer` / `resources`.

- **Parties** — `creditor` (owed the net amount) and `debtor` (owes it), each a `Participant`. The issuer is not modelled as a field; it is the node that invokes the `invoice` / `on_invoice` endpoint.
- **Line items** — `statement` is an array of `{ consideration, amount }` entries. The `consideration` (a `Consideration`) carries the billed item polymorphically through its `considerationAttributes` JSON-LD bag (by `@type`: `Contract`, `RetailOrder`, `DeliveryService`, `Commission`, `FinderFee`, `Adjustment`, `Refund`, …); `amount` is the money owed for that entry.
- **Settlement** — `settlementTerms` (a `SettlementTerm`) carries the agreed terms; `settlementAction` is an array of `PaymentAction` proofs of discharge (supporting installments / partial payments).
- **Lifecycle** — `status.code` is one of `DRAFT`, `PENDING`, `COMMITTED`, `SETTLED`, `CANCELLED`, `DISPUTED` (default `PENDING`). Each statement entry's `consideration.status.code` is one of `PENDING`, `COMMITTED`, `DISPUTED`, `SETTLED` (default `PENDING`), updatable by the creditor or debtor.

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context reference |
| `@type` | yes | string | JSON-LD type |
| `id` | yes | string (uuid) | Stable invoice identifier (system id). |
| `number` | yes | string | Human-visible invoice number. |
| `issuedAt` | yes | string (date-time) | Timestamp at which the invoice was issued. |
| `dueDate` | no | string (date) | Date by which the invoice amount is due for settlement. |
| `descriptor` | no | $ref: https://schema.beckn.io/Descriptor/v2.1/attributes.yaml#/components/schemas/Descriptor | Describes the nature of the invoice in human / agent readable terms. |
| `status` | no | allOf: Descriptor (code ∈ DRAFT, PENDING, COMMITTED, SETTLED, CANCELLED, DISPUTED; default PENDING) | The lifecycle state of the invoice. |
| `creditor` | yes | $ref: https://schema.beckn.io/Participant/v2.0/attributes.yaml#/components/schemas/Participant | The party that is owed the net amount — the seller / provider. |
| `debtor` | yes | $ref: https://schema.beckn.io/Participant/v2.0/attributes.yaml#/components/schemas/Participant | The party the invoice is issued to and who owes the net amount — the consumer being billed. |
| `statement` | yes | array of `{ consideration, amount }` | The itemised statement of charges. Each entry pairs a `Consideration` (billed item, by `@type` in `considerationAttributes`) with its monetary `amount` (`PriceSpecification`). |
| `total` | no | $ref: https://schema.beckn.io/PriceSpecification/v2.1/attributes.yaml#/components/schemas/PriceSpecification | The net amount payable for this invoice across all statement entries. |
| `settlementTerms` | no | $ref: https://schema.beckn.io/SettlementTerm/v2.0/attributes.yaml#/components/schemas/SettlementTerm | The agreed terms under which the invoice is to be settled. |
| `settlementAction` | no | array of $ref: https://schema.beckn.io/PaymentAction/v2.0/attributes.yaml#/components/schemas/PaymentAction | Proofs of settlement that discharge the invoice — one entry per payment event. |
| `invoiceAttributes` | no | $ref: https://schema.beckn.io/Attributes/v2.0/attributes.yaml#/components/schemas/Attributes | Domain-specific extension attributes — tax regime (e.g. GST/VAT), e-invoice refs, legal boilerplate, etc. |
