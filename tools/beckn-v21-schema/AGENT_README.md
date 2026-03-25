# Agent README — `beckn-v21-schema` Skill

> **Purpose:** This document tells an AI agent exactly how to invoke the `beckn-v21-schema`
> skill, what inputs to gather from the user, which questions to ask, how to detect operating
> mode, and what the skill will produce. Read this before calling the skill.

---

## 1. What This Skill Does

The `beckn-v21-schema` skill generates **production-ready schema packs** for the Beckn Protocol
v2.1 **generalised** model — the domain-neutral `Resource → Offer → Contract` triad that works
across any vertical: mobility, hiring, energy, carbon credits, healthcare, data access, and more.

The skill operates in two distinct modes:

| Mode | When to use |
|------|-------------|
| **Greenfield** | User provides a use case description, business flow, or domain document and wants new schemas created |
| **Migration** | User provides existing Beckn v2 schema folders (`attributes.yaml`, `context.jsonld`, etc.) and wants them upgraded to v2.1 |

> **Important scope boundary:** This skill ONLY targets the v2.1 generalised model. If the
> domain is commerce-oriented and must stay on `Item / Order / Fulfillment` semantics, use
> `beckn-v2-schema` instead. If you are unsure, default to this skill and let it guide you.

---

## 2. When to Invoke This Skill

Trigger this skill when the user says anything resembling:

- "Generate v2.1 schemas for [domain]"
- "Create a Beckn generalised schema for [use case]"
- "Migrate my v2 schemas to v2.1"
- "Upgrade our schema pack to the generalised model"
- "Model [domain] using the Resource/Offer/Contract structure"
- "Build a schema pack for [energy / hiring / carbon / data / mobility / etc.]"

Do NOT trigger this skill for:

- v1 → v2.1 migration (instruct user to run `beckn-v2-schema` first, then return here)
- Pure commerce domains that want to stay on `Item / Order` (use `beckn-v2-schema`)
- Implementation Guide (IG) generation (use `beckn-v21-impl-guide`)

---

## 3. Information to Collect from the User

Before invoking the skill, gather as much of the following as possible. The skill has its own
clarification gate, but the more context you collect upfront, the fewer interruptions there
will be.

### 3.1 Mode Detection (ask first)

Ask the user:

> "Do you have existing Beckn v2 schema folders you want to migrate, or are we starting from
> scratch with a use case description?"

- **Existing v2 schemas present** → **Migration mode**
- **No existing schemas** → **Greenfield mode**

### 3.2 Inputs Required per Mode

#### Greenfield Mode

Collect one or more of:

| Input | Format | Notes |
|-------|--------|-------|
| Use case description | Markdown, plain text, Word document | The richer, the better |
| Business flow | Any format | API lifecycle, sequence diagrams, user journeys |
| Regulatory or compliance docs | PDF, Word, text | Country-specific mandates, credential requirements |
| Domain name | Short slug (e.g., `ev-charging`, `driver-jobs`) | Used for folder naming |

**Minimum required:** A natural-language description of what the domain does, who the
participants are, and what is being exchanged.

#### Migration Mode

Collect:

| Input | Format | Notes |
|-------|--------|-------|
| Existing v2 schema folder(s) | Files or ZIP | Must include `attributes.yaml`, `context.jsonld`, `vocab.jsonld`, `profile.json`, `renderer.json`, `README.md`, and `examples/` |
| v2 Implementation Guide (optional) | Word / PDF / Markdown | Helps the skill reconstruct design rationale |

**Minimum required:** At least one complete v2 schema folder.

> ⚠️ If the user has Beckn **v1** implementation guides, do NOT proceed. Instruct them to
> first run `beckn-v2-schema` to produce a v2 pack, then return here for migration.

### 3.3 Clarifying Questions for Greenfield

If the use case description does not answer the following, ask them before invoking the skill.
These map directly to the skill's mandatory clarification gate:

1. **Resource type:** What is the atomic, discoverable unit of value? (e.g., an EV charging
   slot, a driver job posting, a carbon credit, a dataset licence)
2. **Party roles:** Who are the participants and what roles do they play?
   (e.g., EMPLOYER / EMPLOYEE, PRODUCER / GRID_OPERATOR, BUYER / SELLER)
3. **Performance model:** Is execution physical delivery, a digital service, API access,
   or capacity allocation?
4. **Consideration type:** Is value exchanged in money, tokens, credits, assets, or a
   service-for-service swap?
5. **Settlement model:** Is payment immediate, deferred, escrowed, or split across parties?
6. **Recurring or scheduled resources?** Are there subscription slots, time-bound access
   windows, or capacity reservations?
7. **Visibility control:** Does the domain need `beckn:availableTo` filtering
   (NETWORK / PARTICIPANT / ROLE)?
8. **Regulatory fields:** Are any fields country-specific or governed by a standards body?
   (These use the `CodedValue` pattern)
9. **Containers needed:** Is this discovery-only, or fully transactional?
   Discovery-only needs `resourceAttributes` + `offerAttributes`.
   Transactional adds `contractAttributes` + `performanceAttributes` at minimum.

You do NOT need all nine answered before invoking the skill — the skill will stop and ask if
any are missing. However, the more you resolve upfront, the smoother the run.

---

## 4. What the Skill Fetches Automatically

The skill will fetch the following Beckn core reference files autonomously. You do not need
to provide these unless the remote URLs are unavailable:

| File | URL |
|------|-----|
| Core API spec (v2.1 draft) | `https://raw.githubusercontent.com/beckn/protocol-specifications-v2/refs/heads/proposal/v2.1-generalized-core/api/beckn.yaml` |
| Core schema (`attributes.yaml`) | `https://raw.githubusercontent.com/beckn/protocol-specifications-v2/refs/heads/proposal/v2.1-generalized-core/schema/core/v2/attributes.yaml` |
| Core `context.jsonld` | `https://schema.beckn.io/core/v2/context.jsonld` |
| Core `vocab.jsonld` | `https://schema.beckn.io/core/v2/vocab.jsonld` |

If any of these fail and the user has a local copy (e.g., `beckn-generalise-draft.yaml`),
ask them to upload it before proceeding.

---

## 5. The Seven Extension Containers

Understanding these helps you interpret what the skill will generate and answer user
questions during the run.

```
Resource      → beckn:resourceAttributes      ← what is being offered (intrinsic metadata)
Offer         → beckn:offerAttributes         ← commercial terms and eligibility
Contract      → beckn:contractAttributes      ← transaction-level lifecycle metadata
Commitment    → beckn:commitmentAttributes    ← per-commitment detail inside a contract
Performance   → beckn:performanceAttributes   ← how execution occurs (delivery/service/access)
Consideration → beckn:considerationAttributes ← value-exchange specifics (beyond amount)
Settlement    → beckn:settlementAttributes    ← how consideration is discharged
```

Not every use case needs all seven. The skill will decide which containers are required
based on the domain analysis. Typical selections:

| Use Case Type | Containers Likely Needed |
|---------------|--------------------------|
| Discovery-only catalogue | `resourceAttributes`, `offerAttributes` |
| Fully transactional | All seven (or at minimum the first four + `performanceAttributes`) |
| Monetary-only payment | Omit `considerationAttributes` / `settlementAttributes` (minimal gain) |
| Non-monetary exchange (tokens, credits) | All seven — `considerationAttributes` / `settlementAttributes` unlock real value |

---

## 6. The v2 → v2.1 Container Name Map (Migration Mode)

Refer to this when explaining migration to the user:

| v2 Container | v2.1 Container | Notes |
|-------------|----------------|-------|
| `itemAttributes` | `resourceAttributes` | Name change only; semantics broadened |
| `offerAttributes` | `offerAttributes` | Unchanged |
| `fulfillmentAttributes` | `performanceAttributes` | Rename + `mode` enum expanded |
| `orderAttributes` | `contractAttributes` | Rename + multi-party parties model |
| *(not in v2)* | `commitmentAttributes` | New — per-commitment metadata |
| *(payment in v2)* | `considerationAttributes` | Split from Payment |
| *(payment in v2)* | `settlementAttributes` | Split from Payment |

---

## 7. Migration Mode — The Approval Gate

In migration mode, **the skill will NOT generate any files until it presents a Migration
Summary to the user and receives explicit approval.** The summary includes:

- List of v2 schemas found and their planned v2.1 equivalents
- A **Paradigm Fit Review** with verdicts on six dimensions (resource neutrality, offer
  abstraction quality, contract expressiveness, performance mapping, consideration/settlement
  split, cross-domain potential)
- An overall fit verdict: `STRONG` / `ADEQUATE` / `NEEDS-DISCUSSION`
- Recommended actions before proceeding

**Your role at this gate:** Present the summary clearly to the user, explain any `NEEDS-DISCUSSION`
items in plain language, and wait for their go-ahead (or their answers to any open questions)
before the skill continues.

---

## 8. What the Skill Produces

### Per-Schema Folder (7 files each)

For each top-level schema (one per container attachment), the skill generates:

| File | Contents |
|------|----------|
| `attributes.yaml` | OpenAPI 3.1.1 schema with `x-jsonld`, `x-beckn-container` annotations |
| `context.jsonld` | JSON-LD context mapping every property to a schema.org or domain IRI |
| `vocab.jsonld` | Enum class definitions with `rdfs:label` and `rdfs:comment` |
| `profile.json` | Discovery fields, filterable paths, privacy notes, `semantic_model: "generalised"` |
| `renderer.json` | Four Handlebars/Moustache templates for card and detail UI rendering |
| `README.md` | Overview, attachment points, design rationale, non-goals, upstream candidates |
| `examples/` | `example-resource.json` (on_discover) and `example-contract.json` (on_confirm) |

### Folder Structure

```
{domain}-{use-case}/
├── v2.1/
│   ├── {ResourceSchemaName}/
│   │   └── ... (7-file structure above)
│   ├── {OfferSchemaName}/         (if needed)
│   ├── {ContractSchemaName}/      (if transactional)
│   ├── {PerformanceSchemaName}/   (if needed)
│   └── {domain}-common/           (shared types used by ≥2 schemas)
└── README.md                      (domain pack overview)
```

### Post-Generation

After generating files, the skill automatically invokes the `beckn-v21-schema-tester` skill
to run a four-layer validation:

- **L1** — OpenAPI structural checks (container validation, `x-beckn-container` correctness)
- **L2** — JSON-LD prefix resolution (`#generalised` context import accepted)
- **L3** — Cross-file consistency (attributes ↔ context ↔ vocab)
- **L4** — Example payload validation against core + extension schemas

Any failures will be fixed before the final summary is delivered to the user.

---

## 9. Key Design Rules to Know (Agent Reference)

These rules are enforced by the skill. Knowing them helps you answer user questions and
detect when a domain might need a different skill.

| Rule | What it means |
|------|--------------|
| **No core duplication** | Never re-model `Resource`, `Contract`, `Performance`, `Consideration`, etc. |
| **Commercial isolation** | Pricing and eligibility belong in `offerAttributes`, not `resourceAttributes` |
| **Execution isolation** | Logistics/provisioning in `performanceAttributes`, not `contractAttributes` |
| **Value-exchange isolation** | Payment/token terms in `considerationAttributes`; discharge in `settlementAttributes` |
| **International neutrality** | No hardcoded country/currency unless truly domain-specific; use `CodedValue` |
| **One folder per top-level schema** | Each container attachment gets the full 7-file structure |
| **Versioned folder** | All output lives under `v2.1/` inside the domain root |
| **Per-schema namespace prefix** | e.g., `"djra": "https://schema.beckn.io/DriverJobResourceAttributes#"` — never a flat domain prefix |
| **Generalised context import** | Always `"@import": "https://schema.beckn.io/core/v2/context.jsonld#generalised"` |
| **HTML templates mandatory** | `renderer.json` must include both `html` and `html_detail` Handlebars templates |
| **Migration is never mechanical** | v2 → v2.1 always includes a paradigm fit review and user approval before file generation |
| **No v1 direct migration** | v1 → v2.1 is always two-step: run `beckn-v2-schema` first, then this skill |

---

## 10. Common Failure Points and How to Handle Them

| Situation | What to do |
|-----------|-----------|
| Core reference URLs unreachable | Ask user to upload local copies (`beckn-generalise-draft.yaml`, `attributes.yaml`) |
| User provides v1 IG | Stop. Instruct them to run `beckn-v2-schema` first to get a v2 pack, then come back |
| User wants `Item / Order` semantics (commerce) | Switch to `beckn-v2-schema` skill |
| Migration fit review returns `NEEDS-DISCUSSION` | Pause, explain the specific concerns to the user, get direction before continuing |
| Domain description is too vague | Use the nine clarifying questions in section 3.3 to extract detail |
| Schema tester reports L3/L4 failures | The skill will self-correct; if it cannot, surface the specific failing file to the user |

---

## 11. End-to-End Flow Summary

```
User request
    │
    ▼
Detect mode ──────────────────────────────────────────┐
    │ Greenfield                                       │ Migration
    ▼                                                  ▼
Collect use case description              Collect v2 schema folder(s)
    │                                                  │
    ▼                                                  ▼
Ask nine clarifying questions             Phase A: Inventory v2 schemas
(if any unanswered)                       Phase B: Apply container mapping
    │                                     Phase C: Paradigm fit review
    ▼                                     Phase D: Present summary → await approval
Fetch Beckn v2.1 core references                      │
    │                                                  │
    └──────────────────────┬───────────────────────────┘
                           ▼
                 Core alignment check (STEP 2)
                           │
                           ▼
                Architectural sanity sweep (STEP 3)
                           │
                           ▼
                Generate schema pack (STEP 4)
                  (7 files per top-level schema)
                           │
                           ▼
                Run beckn-v21-schema-tester (STEP 5)
                  Fix all failures
                           │
                           ▼
                Post-generation summary (STEP 6)
                  Vertical sweep, core alignment,
                  upstream candidates,
                  migration delta table (if migration)
```

---

## 12. Companion Skills

| Skill | When to use alongside this one |
|-------|-------------------------------|
| `beckn-v21-schema-tester` | Auto-invoked after generation; invoke manually to re-validate later |
| `beckn-v21-impl-guide` | After schemas are generated, to produce a Word IG document |
| `beckn-v2-schema` | For v1 → v2 step, or for commerce-oriented schemas staying on Item/Order |
| `beckn-v2-schema-tester` | If validating v2 (not v2.1) schema packs |

---

## 13. Example Agent Interaction Scripts

### Example A — Greenfield (EV Charging)

```
User: "I need Beckn v2.1 schemas for an EV charging network."

Agent: "I'll use the beckn-v21-schema skill to generate your schema pack.
        A few quick questions before we start:

        1. What is the atomic resource being offered? (e.g., a charging slot, a connector, a session)
        2. Who are the parties? (e.g., EV Owner, Charging Station Operator, Grid Operator)
        3. Is charging scheduled in advance, or on-demand?
        4. Is payment monetary, or are tokens/credits involved?
        5. Do you need multi-party settlement (e.g., revenue split between CPO and grid)?
        6. Any country-specific regulatory fields needed?

        Once you answer these, I'll invoke the skill to generate the full schema pack."
```

### Example B — Migration

```
User: "I have our v2 driver job schemas. Can you migrate them to v2.1?"

Agent: "Sure. Please upload your v2 schema folder(s) — specifically the
        attributes.yaml, context.jsonld, vocab.jsonld, profile.json,
        renderer.json, README.md, and examples/ files.

        If you have a v2 Implementation Guide for this domain, upload that too —
        it helps the skill preserve design rationale during migration.

        I'll then run the beckn-v21-schema skill in migration mode, which will
        analyse the structural fit, present you with a paradigm review and
        migration plan for your approval, then generate the v2.1 files."
```

### Example C — Wrong Starting Point (v1)

```
User: "Here's our v1 Beckn implementation guide. Migrate it to v2.1."

Agent: "v1 → v2.1 migration is a two-step process. This skill only handles
        the v2 → v2.1 step.

        First, I'll need to run the beckn-v2-schema skill on your v1 IG to
        produce a v2 schema pack. Once that's done, we can pass it to
        beckn-v21-schema to complete the migration to v2.1.

        Shall I start with the v2 step now?"
```

---

*This README is intended for AI agents invoking the `beckn-v21-schema` skill. For the full
technical specification of the skill itself, read `SKILL.md` in the same folder.*