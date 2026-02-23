# Beckn Protocol Core Schema

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](./LICENSE.md)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-yellow.svg)]()
[![Version: v2.0](https://img.shields.io/badge/Version-v2.0-blue.svg)]()

> **⚠️ Active Development Notice**  
> This repository is under active development. All in-progress content lives in the [`draft`](../../tree/draft) branch. Content is being progressively reviewed and merged into `main` via pull requests.

---

## What Is This Repository?

This repository contains the **domain-agnostic core schema definitions** for the Beckn Protocol v2.0 — the canonical set of JSON-LD contexts, RDF vocabularies, and OpenAPI 3.1 attribute definitions that form the semantic foundation of every Beckn network.

Every participant in a Beckn network — buyers, sellers, platforms, gateways, and infrastructure services — speaks in terms of the types defined here: `Catalog`, `Item`, `Fulfillment`, `Contract`, `Intent`, `Provider`, `Consumer`, and ~85 others. This repository is where those types are formally defined.

---

## Why Does This Repository Exist? The Design Principles

### The Problem with v1.x

In Beckn Protocol v1.x, all schema definitions lived inside a single monolithic YAML file inside the protocol specifications repository. This caused compounding problems:

- **Versioning friction:** A change to any one schema — even a minor attribute addition — forced a version bump on the entire specification. There was no way to release `Address v1.1` without also releasing a new version of `Catalog`, `Fulfillment`, and every other schema.
- **Coupling:** Schema concerns were tightly entangled with protocol transport concerns. The payload shape and the API envelope lived in the same file.
- **Domain extensibility required forking:** When a domain (e.g., mobility, healthcare) needed to add domain-specific attributes, the only option was to fork the entire specification — there was no formal extension mechanism.
- **Semantic opacity:** Terms like `"address"` or `"status"` had no globally unique identity. Two implementations could disagree on what `"status"` meant, with no way to detect or resolve the conflict.

### The v2.0 Solution: A Three-Tier Schema Model

Beckn Protocol v2.0 solves this with a **three-tier schema model** that separates concerns cleanly across three repositories, each with its own versioning lifecycle:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Tier 1 — Transport Envelope                                        │
│  Repository: beckn/protocol-specifications-v2                       │
│  Contains: API message envelope, Context object, RequestContainer,  │
│            CallbackContainer, AckResponse, all 14 API actions       │
│  Versioned: with the full protocol specification                    │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  references payload schemas from
┌──────────────────────────────▼──────────────────────────────────────┐
│  Tier 2 — Core Schema  ◄  THIS REPOSITORY                           │
│  Repository: beckn/core_schema                                      │
│  Contains: All domain-agnostic schemas (Address, Catalog, Item,     │
│            Fulfillment, Contract, Intent, Provider, etc.)           │
│  Versioned: independently, per-schema                               │
│  Namespace: https://schema.beckn.io/core/v2.0/                      │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  extended by
┌──────────────────────────────▼──────────────────────────────────────┐
│  Tier 3 — Domain Schema Packs                                       │
│  Repository: one per vertical (e.g., beckn/mobility, beckn/health)  │
│  Contains: Domain-specific schemas that extend Tier 2 types         │
│  Versioned: independently, per domain pack                          │
│  Namespace: defined per domain (e.g., https://schema.beckn.io/mob/) │
└─────────────────────────────────────────────────────────────────────┘
```

### Core Design Principles

| Principle | What it means |
|-----------|---------------|
| **Separation of concerns** | Transport, core data types, and domain extensions live in independent repositories with independent versioning. A change to `Address` doesn't touch the protocol envelope. |
| **Domain-agnosticism** | Every schema in this repository must be meaningful across multiple industries. `Item` is a product in retail, a ride in mobility, a consultation in healthcare. No industry-specific attributes belong here. |
| **Independent schema versioning** | Each schema has its own version directory (`v2.0/`, `v2.1/`, etc.). `Fulfillment` can release v2.1 while `Address` stays at v2.0. |
| **Semantic grounding** | Every term maps to a globally unique IRI in the `beckn:` namespace (`https://schema.beckn.io/core/v2.0/`). `"address"` in a Beckn document is unambiguously `beckn:address` — not a plain string. |
| **OpenAPI 3.1 compatibility** | Every schema is a standalone, `$ref`-able OpenAPI 3.1 component. No schema registry or toolchain is required — just a URL. |
| **Linked Data alignment** | Every schema is simultaneously valid JSON and valid RDF. Systems that don't know JSON-LD process it as plain JSON. Systems that do can build knowledge graphs, run SPARQL queries, and align with external ontologies. |

---

## Advantages of This Architecture

### For Protocol Implementors
- **Stable, URL-addressable schemas** — Reference `Address v2.0` directly by URL in your OpenAPI definitions. It won't change unless explicitly versioned.
- **No monolithic dependency** — You can adopt the schemas you need without taking a dependency on the full protocol specification.
- **Forward compatibility** — Minor additions (new optional attributes) never break existing implementations.

### For Domain Pack Authors
- **Extend, don't fork** — Add `vehicleType` to `Fulfillment` in your mobility pack without modifying or forking the core schema.
- **Semantic interoperability out of the box** — Your domain-specific types share the same RDF namespace foundation. A healthcare `Item` and a logistics `Item` are both `beckn:Item` — interoperability is automatic for the shared attributes.
- **Governed extension points** — The Schema Pack Contract (defined in `protocol-specifications-v2`) specifies exactly how domain packs reference and extend core schemas.

### For the Ecosystem
- **Independent release cadences** — The core schema can release a new version without waiting for a full protocol specification release.
- **Immutable IRIs** — Once a term is published (e.g., `beckn:Contract`), its IRI is permanent. Linked Data graphs built years ago remain valid.
- **Formal deprecation path** — Terms are never silently removed. They are deprecated with a replacement reference, retained for at least one version cycle, and only removed (from structural files) in a Major release.

---

## How It Is Used in Beckn Protocol API Implementations

### 1. As OpenAPI `$ref` References

Every schema is available as a standalone OpenAPI 3.1 component, referenceable by raw URL. A Beckn BAP or BPP implementation simply `$ref`-references the schemas it needs:

```yaml
# In your OpenAPI spec:
components:
  schemas:
    Address:
      $ref: 'https://raw.githubusercontent.com/beckn/core_schema/main/schema/Address/v2.0/attributes.yaml#/components/schemas/Address'

    Catalog:
      $ref: 'https://raw.githubusercontent.com/beckn/core_schema/main/schema/Catalog/v2.0/attributes.yaml#/components/schemas/Catalog'
```

The Tier 1 transport envelope (`protocol-specifications-v2`) uses exactly this mechanism — it `$ref`-references the core schemas from this repository to define the payload body of each API action.

### 2. As a JSON-LD Context

Reference the root context in any JSON-LD document to make all Beckn core terms semantically unambiguous:

```json
{
  "@context": "https://schema.beckn.io/core/v2.0/context.jsonld",
  "@type": "Catalog",
  "descriptor": {
    "name": "Fresh Produce by Green Farms"
  },
  "providers": [
    {
      "@type": "Provider",
      "id": "prov-001",
      "descriptor": { "name": "Green Farms" }
    }
  ]
}
```

When processed as JSON-LD, `"Catalog"` resolves to `https://schema.beckn.io/core/v2.0/Catalog`, making it unambiguous in any context — a database, a knowledge graph, or an API call.

### 3. As an RDF Vocabulary

The `schema/vocab.jsonld` file defines all Beckn core schema types and properties as RDF classes and properties. This enables:
- SPARQL queries over Beckn data graphs
- Ontology alignment with Schema.org, GS1, and other semantic standards
- Automated inference and validation using RDF tooling

---

## How Domain Schema Packs Layer on Top

Domain schema packs (Tier 3) extend core schemas for specific industry verticals. The extension model has two forms:

### Attribute Extension via `allOf`

A domain pack adds industry-specific attributes by extending a core schema:

```yaml
# In beckn/mobility — schema/RideService/v1.0/attributes.yaml
components:
  schemas:
    RideService:
      allOf:
        - $ref: 'https://raw.githubusercontent.com/beckn/core_schema/main/schema/Item/v2.0/attributes.yaml#/components/schemas/Item'
        - type: object
          properties:
            vehicleType:
              type: string
              enum: [AUTO, CAB, BIKE]
            seatingCapacity:
              type: integer
```

`RideService` is a `beckn:Item` with additional mobility-specific attributes. The core `Item` schema is unchanged.

### JSON-LD Namespace Extension

Domain packs extend the JSON-LD context with their own namespace, without overriding any protected core terms:

```json
{
  "@context": [
    "https://schema.beckn.io/core/v2.0/context.jsonld",
    {
      "mob": "https://schema.beckn.io/mobility/v1.0/",
      "vehicleType": "mob:vehicleType",
      "seatingCapacity": "mob:seatingCapacity"
    }
  ],
  "@type": "RideService",
  "vehicleType": "CAB",
  "seatingCapacity": 4
}
```

The core terms remain `@protected` — domain packs add their own terms but cannot redefine what `beckn:address` or `beckn:item` means.

### The Layering Principle

```
beckn:Item                    ← Tier 2 Core Schema (this repository)
    ├── mob:RideService        ← Tier 3 Mobility Domain Pack
    ├── health:Consultation    ← Tier 3 Healthcare Domain Pack
    ├── energy:TariffSlot      ← Tier 3 Energy Domain Pack
    └── logistics:Shipment     ← Tier 3 Logistics Domain Pack
```

Each domain vertical gets its own namespace, its own versioning, and its own governance — but they all share the same semantic base. A platform consuming data from both a mobility provider and a logistics provider can unambiguously identify that both are dealing with `beckn:Item` objects, even though the domain-specific extensions differ.

---

## What to Expect: Incoming Content

The [`draft`](../../tree/draft) branch contains the complete v2.0 content currently under review. It will be progressively merged into `main` via pull requests. Here is a preview:

### Schema Library (~90 schemas)

| Category | Schemas |
|----------|---------|
| **Discovery** | `DiscoverAction`, `OnDiscoverAction`, `Catalog`, `Provider`, `Item`, `Offer`, `Intent`, `MediaSearch`, `MediaSearchOptions`, `MediaInput` |
| **Selection** | `SelectAction`, `OnSelectAction`, `CheckoutTerminal` |
| **Initialisation** | `InitAction`, `OnInitAction`, `Contract`, `ContractItem` |
| **Confirmation** | `ConfirmAction`, `OnConfirmAction` |
| **Fulfillment** | `Fulfillment`, `FulfillmentAgent`, `FulfillmentMode`, `FulfillmentStage`, `FulfillmentStageAuthorization`, `FulfillmentStageEndpoint`, `Tracking`, `TrackingRequest`, `TrackAction`, `OnTrackAction` |
| **Post-transaction** | `UpdateAction`, `OnUpdateAction`, `CancelAction`, `OnCancelAction`, `CancellationPolicy`, `CancellationOutcome`, `CancellationReason`, `StatusAction`, `OnStatusAction`, `RateAction`, `OnRateAction` |
| **Payment** | `PaymentAction`, `PaymentTerms`, `PaymentTrigger`, `AcceptedPaymentMethod`, `PriceSpecification`, `SettlementTerm`, `SettlementSchedule`, `RefundTerms`, `Invoice` |
| **Support** | `SupportAction`, `OnSupportAction`, `SupportRequest`, `SupportTicket`, `SupportInfo` |
| **Common types** | `Address`, `Person`, `Organization`, `Descriptor`, `Location`, `GeoJSONGeometry`, `TimePeriod`, `Time`, `Quantity`, `MediaFile`, `Skill`, `State`, `Alert`, `Instruction` |
| **Governance** | `Credential`, `Eligibility`, `Entitlement`, `Policy`, `Document`, `Form`, `Rating`, `RatingForm`, `RatingInput`, `DisplayedRating`, `Feedback` |
| **Infrastructure** | `Context`, `Error`, `ErrorResponse`, `ProcessingNotice`, `CatalogProcessingResult`, `TransactionEndpoint`, `Participant`, `Consumer`, `CategoryCode`, `Constraint`, `SpatialConstraint`, `Attributes` |

### Documentation (`docs/`)

| Document | Contents |
|----------|---------|
| `1_Introduction.md` | Three-tier model, design rationale, relationship to `protocol-specifications-v2` |
| `2_Schema_Structure.md` | Normative directory layout, file naming conventions, `attributes.yaml` structure |
| `3_JSON_LD_Context_and_Vocabulary.md` | `beckn:` namespace, `@protected` contexts, term mapping patterns, enum handling |
| `4_Versioning_and_Deprecation.md` | Semver rules, what triggers Minor vs Major, deprecation lifecycle, IRI retention |
| `5_Contributing_Schemas.md` | Step-by-step guide: proposal → authoring → PR, with templates and worked examples |

### Governance and Process Files

- `GOVERNANCE.md` — Maintainer roles, voting thresholds, review requirements, Major change process
- `CONTRIBUTING.md` — PR checklist, file templates, attribute authoring guidelines
- `CHANGELOG.md` — Full v2.0 change log including v1.x → v2.0 term renames
- `CODE_OF_CONDUCT.md` — Community standards
- `LICENSE.md` — CC BY-NC-SA 4.0

---

## Repository Structure (Preview)

```
core_schema/
├── schema/
│   ├── context.jsonld          ← Root JSON-LD context (@protected, all ~90 schemas)
│   ├── vocab.jsonld            ← Root RDF vocabulary (all classes and properties)
│   ├── README.md               ← Alphabetical schema index with descriptions
│   └── {SchemaName}/
│       └── v2.0/
│           ├── attributes.yaml ← OpenAPI 3.1 component definition
│           ├── context.jsonld  ← Per-schema JSON-LD context
│           └── vocab.jsonld    ← Per-schema RDF vocabulary
├── docs/
│   ├── README.md               ← Staged reading guide
│   ├── 1_Introduction.md
│   ├── 2_Schema_Structure.md
│   ├── 3_JSON_LD_Context_and_Vocabulary.md
│   ├── 4_Versioning_and_Deprecation.md
│   └── 5_Contributing_Schemas.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
└── LICENSE.md
```

---

## Related Repositories

| Repository | Tier | Description |
|------------|------|-------------|
| [beckn/protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2) | Tier 1 | Full protocol spec, API envelope, RFC documents |
| `beckn/core_schema` ← **this repo** | Tier 2 | Domain-agnostic core schema definitions |
| `beckn/mobility` *(planned)* | Tier 3 | Mobility domain schema pack |
| `beckn/healthcare` *(planned)* | Tier 3 | Healthcare domain schema pack |
| `beckn/energy` *(planned)* | Tier 3 | Energy domain schema pack |
| `beckn/logistics` *(planned)* | Tier 3 | Logistics domain schema pack |

---

## Current Status

| Branch | Purpose | Status |
|--------|---------|--------|
| `main` | Stable, reviewed content only | Active — this README |
| [`draft`](../../tree/draft) | All v2.0 schemas, docs, and governance files | Under review — being merged progressively |

---

## License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](./LICENSE.md) (CC BY-NC-SA 4.0).
