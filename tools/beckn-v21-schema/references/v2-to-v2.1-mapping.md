# Beckn v2 → v2.1 Migration Mapping

Use this when the user provides a v2 schema pack and wants to migrate to v2.1 generalised.

## Container Renaming

| v2 Container | v2.1 Container | Applies To |
|-------------|---------------|-----------|
| `beckn:itemAttributes` | `beckn:resourceAttributes` | Resource (formerly Item) |
| `beckn:offerAttributes` | `beckn:offerAttributes` | Offer (name unchanged, semantics broadened) |
| `beckn:fulfillmentAttributes` | `beckn:performanceAttributes` | Performance (formerly Fulfillment) |
| `beckn:orderAttributes` | `beckn:contractAttributes` | Contract (formerly Order) |
| (n/a) | `beckn:commitmentAttributes` | New — per-commitment detail |
| (n/a) | `beckn:considerationAttributes` | New — value-exchange specifics |
| (n/a) | `beckn:settlementAttributes` | New — settlement discharge details |

## Object Field Renaming

### Item → Resource

| v2 Field | v2.1 Field | Notes |
|---------|-----------|-------|
| `beckn:isActive` | `beckn:isAvailable` | Boolean availability flag |
| `beckn:itemAttributes` | `beckn:resourceAttributes` | Extension container |
| (n/a) | `beckn:availableTo[]` | New visibility constraint |

### Offer (legacy) → Offer (generalised)

| v2 Field | v2.1 Field | Notes |
|---------|-----------|-------|
| Item refs (inline) | `beckn:resourceRefs[]` | Array of Resource IDs |
| (n/a) | `beckn:status` | New lifecycle state |
| (n/a) | `beckn:proposer` | Provider making the offer |
| (n/a) | `beckn:addOnRefs[]` | Optional add-on references |
| (n/a) | `beckn:proposedConsideration` | Replaces inline pricing |
| `beckn:offerAttributes` | `beckn:offerAttributes` | Unchanged name |

### Order → Contract

| v2 Field | v2.1 Field | Notes |
|---------|-----------|-------|
| `beckn:provider` | `beckn:parties[{role: "SELLER"}]` | Seller becomes a party |
| `beckn:buyer` / billing | `beckn:parties[{role: "BUYER"}]` | Buyer becomes a party |
| `beckn:items[]` | `beckn:commitments[{refType: "RESOURCE"}]` | Order items → Resource commitments |
| `beckn:fulfillments[]` | `beckn:performance[]` | Array of Performance units |
| `beckn:payments[]` | `beckn:consideration[] + beckn:settlements[]` | Split into promise + discharge |
| `beckn:orderAttributes` | `beckn:contractAttributes` | Extension container |

### Fulfillment → Performance

| v2 Field | v2.1 Field | Notes |
|---------|-----------|-------|
| `beckn:type` (DELIVERY, etc.) | `beckn:mode` | DELIVERY / SERVICE / ACCESS / TRANSFER / EXECUTION / OTHER |
| `beckn:state` | `beckn:status` | PLANNED / IN_PROGRESS / COMPLETED / FAILED / CANCELLED |
| `beckn:tracking` | `beckn:tracking` | Core `Tracking` object — unchanged |
| `beckn:support` | `beckn:support` | Core `SupportInfo` — unchanged |
| `beckn:fulfillmentAttributes` | `beckn:performanceAttributes` | Extension container |

### Payment → Consideration + Settlement

| v2 Field | v2.1 Consideration | v2.1 Settlement | Notes |
|---------|-------------------|----------------|-------|
| Payment status: REQUESTED | `Consideration.beckn:status: PROPOSED` | — | Promise requested |
| Payment status: CONFIRMED | `Consideration.beckn:status: AGREED` | — | Promise agreed |
| Payment status: PAID | `Consideration.beckn:status: SETTLED` | `Settlement.beckn:status: COMPLETED` | Discharged |
| `beckn:amount` | `beckn:amount` | `beckn:amount` | Copied to both |
| Transaction ref | — | `beckn:settlementRef` | External reference |

## context.jsonld Changes

| v2 | v2.1 | Notes |
|----|------|-------|
| `"@import": "https://schema.beckn.io/core/v2/context.jsonld"` | `"@import": "https://schema.beckn.io/core/v2/context.jsonld#generalised"` | Fragment discriminator added |

## profile.json Changes

Add these two mandatory new fields:
```json
"protocol_version": "2.1",
"semantic_model": "generalised"
```

## Folder Structure Changes

In v2.1, schema folders live under a `v2.1/` version level:
```
domain-usecase/          domain-usecase/
  ItemAttributes/    →     v2.1/
  OrderAttributes/           ResourceAttributes/
  ...                        ContractAttributes/
                             ...
```

## renderer.json Changes

Add `html` and `html_detail` Handlebars HTML template properties alongside existing
`card_template` and `detail_template` (which remain valid).

Update any templates referencing v2 paths:
- `beckn:itemAttributes.*` → `beckn:resourceAttributes.*`
- `beckn:orderAttributes.*` → `beckn:contractAttributes.*`
- `beckn:fulfillmentAttributes.*` → `beckn:performanceAttributes.*`
- `beckn:offers[0].beckn:price.*` → `beckn:offers[0].beckn:proposedConsideration.amount.*`
