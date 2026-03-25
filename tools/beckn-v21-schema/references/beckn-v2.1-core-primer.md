# Beckn v2.1 Generalised Core Primer

## What Changed from v2 (Commerce-Centric) to v2.1 (Generalised)

Beckn v2 introduced a composable extension model using `Item → Offer → Order` as the
core transaction triad. v2.1 replaces this with a **domain-neutral** triad that works
for any value exchange — commerce, hiring, energy, carbon credits, data access, and more.

## The Seven Extension Containers

```
Resource      → beckn:resourceAttributes      (what is being offered / discoverable)
Offer         → beckn:offerAttributes         (terms under which a resource is offered)
Contract      → beckn:contractAttributes      (transaction-level metadata)
Commitment    → beckn:commitmentAttributes    (per-commitment detail inside a contract)
Performance   → beckn:performanceAttributes   (how execution occurs)
Consideration → beckn:considerationAttributes (value-exchange specifics)
Settlement    → beckn:settlementAttributes    (how consideration is discharged)
```

## The v2 → v2.1 Concept Map

| v2 Concept | v2.1 Equivalent | Notes |
|-----------|----------------|-------|
| `Item` | `Resource` | Domain-neutral; no "sellable unit" assumption |
| `itemAttributes` | `resourceAttributes` | Same extension pattern |
| `Offer` (legacy) | `Offer` (generalised) | Status lifecycle added; `resourceRefs` replaces item refs |
| `offerAttributes` | `offerAttributes` | Name unchanged; semantics broadened |
| `Order` | `Contract` | Binding multi-party agreement |
| `orderAttributes` | `contractAttributes` | Same pattern |
| `Fulfillment` | `Performance` | Execution unit; supports DELIVERY, SERVICE, ACCESS, etc. |
| `fulfillmentAttributes` | `performanceAttributes` | Same pattern |
| `Payment` | `Consideration` + `Settlement` | Split: promise vs. discharge |
| (n/a) | `considerationAttributes` | New |
| (n/a) | `settlementAttributes` | New |

## The Resource Object

A `Resource` is a minimal, domain-neutral abstraction. Key fields:
- `beckn:id` — globally unique identifier
- `beckn:descriptor` — name, description, images (from core `Descriptor`)
- `beckn:provider` — who provides it (from core `Provider`)
- `beckn:isAvailable` — whether it's currently available (replaces `beckn:isActive` on Item)
- `beckn:availableTo` — optional visibility constraint (NETWORK / PARTICIPANT / ROLE)
- `beckn:resourceAttributes` — your domain extension goes here

## The Offer Object (generalised)

Key fields added/changed vs. legacy Offer:
- `beckn:status` — lifecycle: DRAFT / SUBMITTED / UNDER_REVIEW / ACCEPTED / REJECTED / EXPIRED / WITHDRAWN
- `beckn:proposer` — who is making the offer (a `Provider`)
- `beckn:resourceRefs` — array of Resource IDs this offer covers
- `beckn:addOnRefs` — optional add-on Offer or Resource IDs
- `beckn:proposedConsideration` — value being offered (open object, monetary or otherwise)
- `beckn:offerAttributes` — your domain extension goes here

## The Contract Object

A `Contract` binds a multi-party agreement. Key fields:
- `beckn:status` — DRAFT / PENDING / CONFIRMED / IN_PROGRESS / COMPLETED / CANCELLED / FAILED / TERMINATED
- `beckn:parties[]` — array of `{beckn:participantId, beckn:role}` (minimum 2)
- `beckn:commitments[]` — what is agreed (array of `{beckn:ref, beckn:refType, beckn:quantity, beckn:commitmentAttributes}`)
- `beckn:consideration[]` — value promised (array of `Consideration` objects)
- `beckn:performance[]` — how execution occurs (array of `Performance` objects)
- `beckn:settlements[]` — how consideration is discharged (array of `Settlement` objects)
- `beckn:contractAttributes` — your domain extension goes here

**Commitment `beckn:refType` values:** `RESOURCE`, `OFFER`, `OTHER`

## The Performance Object

Replaces `Fulfillment`. Key fields:
- `beckn:id` — unique identifier
- `beckn:status` — PLANNED / IN_PROGRESS / COMPLETED / FAILED / CANCELLED
- `beckn:mode` — DELIVERY / SERVICE / ACCESS / TRANSFER / EXECUTION / OTHER
- `beckn:tracking` — core `Tracking` object
- `beckn:support` — core `SupportInfo` object
- `beckn:performanceAttributes` — your domain extension goes here

## The Consideration Object

Represents the value promised (not yet discharged). Key fields:
- `beckn:type` — MONETARY / TOKEN / CREDIT / ASSET / SERVICE / OTHER
- `beckn:status` — PROPOSED / AGREED / PENDING / SETTLED / FAILED / CANCELLED
- `beckn:amount` — open object (monetary or token amount)
- `beckn:considerationAttributes` — your domain extension goes here

## The Settlement Object

Represents the discharge of a Consideration. Key fields:
- `beckn:type` — MONETARY / TOKEN / CREDIT / ASSET / SERVICE / OTHER
- `beckn:status` — INITIATED / PENDING / COMPLETED / FAILED / CANCELLED
- `beckn:amount` — monetary or token amount
- `beckn:settlementRef` — external reference (gateway ID, blockchain tx hash, etc.)
- `beckn:settlementAttributes` — your domain extension goes here

## Context URI Convention

The canonical `@import` target for all v2.1 generalised schemas:
```
https://schema.beckn.io/core/v2/context.jsonld#generalised
```
The base URI stays at `v2` for backward compatibility. The `#generalised` fragment is an
opaque discriminator — it is never dereferenced by JSON-LD processors.

## Discovery vs. Transaction — What Attributes Matter Where

| Phase | Key Containers |
|-------|---------------|
| Discovery (`discover` / `on_discover`) | `resourceAttributes`, `offerAttributes` |
| Selection (`select` / `on_select`) | `resourceAttributes`, `offerAttributes` |
| Init (`init` / `on_init`) | `contractAttributes`, `performanceAttributes` |
| Confirm (`confirm` / `on_confirm`) | `contractAttributes`, `commitmentAttributes`, `performanceAttributes`, `considerationAttributes` |
| Status (`on_status`) | `contractAttributes`, `performanceAttributes`, `settlementAttributes` |
| Update | Whichever container's data changes |

## Backward Compatibility

v2.1 is backward compatible at the API layer. Transaction endpoints accept `anyOf: [order, contract]`
in the `message` payload. Networks can migrate incrementally — during migration, a BPP may
respond with both `order` and `contract` in the same message. The `schema_context` field in
the `Context` envelope is the discriminator: v2 contexts resolve legacy objects; the
`#generalised` context resolves v2.1 objects.

## Composability Pattern

```yaml
# attributes.yaml (your v2.1 extension)
components:
  schemas:
    MyDomainResourceAttributes:
      type: object
      x-jsonld-context: "./context.jsonld"
      x-beckn-container: resourceAttributes
      properties:
        resourceCapacity:
          type: number
          x-jsonld-id: "mdra:resourceCapacity"
        # ... domain-specific properties only
```

The core v2.1 YAML is referenced via `$ref`, never copy-pasted.
