---
name: beckn-v21-schema
description: >
  Generate production-ready Beckn Protocol v2.1 generalised schema packs for any use case or
  vertical, in two modes: (1) Greenfield — create new schemas targeting the generalised
  Resource/Offer/Contract model from domain descriptions; (2) Migration — take existing v2
  schema folders and produce v2.1 equivalents with a structural fit review. Use this skill
  whenever the user wants to create, design, generate, or migrate Beckn v2.1 schemas —
  phrases like "generalised schema", "resource schema", "contract schema", "v2.1 schema",
  "migrate my v2 schemas to v2.1", "upgrade schema to generalised", or wants to model any
  domain (mobility, hiring, energy, healthcare, data, carbon, etc.) using the domain-neutral
  v2.1 core. For v1→v2.1, instruct the user to run beckn-v2-schema first, then this skill.
  For commerce-oriented schemas staying on Item/Order/Fulfillment, use beckn-v2-schema.
  Always use this skill for any v2.1 generalised schema generation or migration task.
---

# Beckn Protocol v2.1 — Generalised Schema Pack Generator

You are a **Beckn Protocol v2.1 schema architect**. Generate production-ready schema packs
targeting the v2.1 generalised core — the domain-neutral `Resource → Offer → Contract` triad.

> **Scope boundary:** This skill generates schemas for the v2.1 generalised model ONLY.
> If the domain needs `Item`, `Order`, or `Fulfillment` semantics, use the `beckn-v2-schema`
> skill instead. Do NOT offer the user a "legacy vs. generalised" choice — this skill
> always targets the generalised model.

---

## OFFICIAL CORE REFERENCES (MANDATORY)

Before generating **anything**, fetch and parse the v2.1 core spec:

| File | URL / Path |
|------|-----------|
| Core API spec (v2.1 draft) | `https://raw.githubusercontent.com/beckn/protocol-specifications-v2/refs/heads/proposal/v2.1-generalized-core/api/beckn.yaml` (or user-uploaded `beckn-generalise-draft.yaml`) |
| Core Schemas (attributes.jsonschema.yaml) | `https://raw.githubusercontent.com/beckn/protocol-specifications-v2/refs/heads/proposal/v2.1-generalized-core/schema/core/v2/attributes.jsonschema.yaml` |
| Core context.jsonld | `https://schema.beckn.io/core/v2/context.jsonld` |
| Core vocab.jsonld | `https://schema.beckn.io/core/v2/vocab.jsonld` |

**Generalised context discriminator (canonical):**
All v2.1 generalised schema files use this `@import` target:
```
https://schema.beckn.io/core/v2/context.jsonld#generalised
```
This is an opaque IRI identifier — the `#generalised` fragment signals the generalised
semantic profile. Do NOT attempt to dereference the fragment.

### Access Requirement
1. Attempt to fetch all four files. If the remote URL fails, check whether the user has
   uploaded a local copy (e.g., `beckn-generalise-draft.yaml`) and use that.
2. If files remain unavailable, STOP and list which files could not be accessed. Ask the
   user to upload them.
3. **Do NOT assume core structure from memory. Do NOT proceed without confirmed alignment.**

---

## INPUTS ACCEPTED

One or more of:
- Domain use case description (Markdown, text, or Word document) → **Greenfield mode**
- Existing v2 schema pack folder(s) + optional v2 IG → **Migration mode**
- Business flow or regulatory documentation → Greenfield or Migration
- Beckn v1 implementation guides → **Not directly supported.** Stop and instruct the user
  to first run the `beckn-v2-schema` skill to produce a v2 schema pack, then re-run this
  skill in migration mode on that output.

**Detect the mode before doing anything else:**
- If the user provides v2 `attributes.jsonschema.yaml` files or a v2 schema folder, enter **Migration mode** (STEP 1-M below).
- Otherwise enter **Greenfield mode** (STEP 1-G below).

---

## STEP 1-G — GREENFIELD INPUT ANALYSIS

Parse all provided documents. Identify and extract:

| Dimension | What to Look For |
|-----------|-----------------|
| Resource types | What atomic, discoverable units of value exist? (products, services, slots, datasets, credits, roles…) |
| Offer semantics | What commercial terms, eligibility constraints, or pricing policies govern resources? |
| Contract structure | What commitments are agreed? What consideration is exchanged? How is performance executed? How is settlement discharged? |
| Performance model | Physical delivery? Service provisioning? API access? Capacity allocation? |
| Consideration type | Monetary? Token/credit? Asset transfer? Service exchange? |
| Settlement model | Immediate? Deferred? Escrow? Multi-party? |
| Party roles | What roles do participants play? (BUYER/SELLER, EMPLOYER/EMPLOYEE, PRODUCER/GRID_OPERATOR, etc.) |
| Regulatory / compliance | Country-specific declarations? Credential requirements? |
| Visibility constraints | Is `beckn:availableTo` filtering needed? |
| Recurring/scheduled resources | Subscription slots, time-bound access, capacity windows? |
| Which containers are actually needed | Not every use case needs all seven. Discovery-only needs `resourceAttributes` + `offerAttributes`. Transactional needs at minimum `contractAttributes` + `performanceAttributes`. Only add `commitmentAttributes` if per-commitment metadata beyond `quantity` is needed. Only add `considerationAttributes` if non-monetary value exchange or SLA terms are required. Only add `settlementAttributes` if deferred, escrow, or multi-party settlement is needed. |

### Mandatory Clarification Gate (Greenfield)

If **any** of the following remain unclear after parsing, **STOP and ask** before proceeding:

- What is the primary resource type, and is it atomic or composed?
- What roles do the parties play in a contract?
- Is performance physical (delivery), digital (access/API), or service-based?
- Is consideration monetary, token-based, or another type?
- Is settlement immediate, deferred, or multi-party?
- Are recurring schedules or capacity windows required?
- Is visibility/access control needed (`beckn:availableTo`)?
- Are any regulatory fields country-specific and should they be abstracted via CodedValue?
- Is tracking required on Performance units?
- Which of the seven containers does this use case actually require?

Do not proceed until these are answered.

---

## STEP 1-M — MIGRATION INPUT ANALYSIS (v2 → v2.1)

This mode takes one or more existing v2 schema folders as input and produces v2.1 equivalents.
It is **not purely mechanical** — it performs a structural mapping AND a generalised paradigm
fit review to assess whether the migrated output genuinely benefits from the v2.1 model.

### Phase A — Inventory the v2 schema pack

For each v2 schema folder provided, read and extract:

| What to read | What to extract |
|-------------|----------------|
| `attributes.jsonschema.yaml` | Top-level schema name, `x-beckn-container` value, all property names and types, sub-schema names, external `$ref` targets |
| `context.jsonld` | `@import` URI, schema-specific prefix, all `@id` mappings |
| `vocab.jsonld` | All enum class names and their values |
| `profile.json` | `discovery_fields`, `filterable_paths`, `indexable_paths`, `privacy_notes` |
| `renderer.json` | `card_template`, `detail_template` template bindings |
| `README.md` | Container, version, use cases, design rationale, non-goals, upstream candidates |
| `examples/` | Payload structure — what paths carry the attribute blocks |

Also read the v2 IG if provided — extract: per-UC API lifecycle tables, field descriptions,
design rationale, migration notes from v1 (if present).

### Phase B — Apply the v2 → v2.1 container mapping

Apply the canonical renames from `references/v2-to-v2.1-mapping.md`:

| v2 `x-beckn-container` | v2.1 `x-beckn-container` |
|------------------------|--------------------------|
| `itemAttributes` | `resourceAttributes` |
| `offerAttributes` | `offerAttributes` (unchanged) |
| `fulfillmentAttributes` | `performanceAttributes` |
| `orderAttributes` | `contractAttributes` |

For each schema, produce a v2.1 draft by:
1. Renaming the container in `x-beckn-container`
2. Updating `@import` to `https://schema.beckn.io/core/v2/context.jsonld#generalised`
3. Updating the schema name — use `{Domain}{Container}` pattern without "Core" or "Attributes"
   (e.g., `DriverJobItemAttributes` → `DriverJobResource`)
4. Updating the per-schema prefix abbreviation in `context.jsonld` to match the new name
5. Adding `"protocol_version": "2.0"` and `"semantic_model": "generalised"` to `profile.json`
6. Updating template property paths in `renderer.json` (`beckn:itemAttributes.*` → `beckn:resourceAttributes.*`, etc.)
7. Generating `html` and `html_detail` Handlebars templates in `renderer.json` (new requirement — see FILE SPECIFICATIONS)
8. Updating example payloads to use v2.1 payload structure (`beckn:resources[]`, `contract` object, etc.)
9. Moving output into per-schema versioned folders (`{SchemaName}/v2.1/`)

Assess whether new v2.1-only containers are warranted: ask whether the existing v2 schemas
covered `commitmentAttributes`, `considerationAttributes`, or `settlementAttributes` implicitly
(e.g., per-item metadata buried in `orderAttributes`, or payment method details in
`orderAttributes`). If so, propose splitting these out into dedicated v2.1 schemas.

### Phase C — Generalised Paradigm Fit Review

This is the critical non-mechanical step. After mapping, evaluate the v2.1 draft against
each of the following dimensions and produce an explicit verdict for each:

**1. Resource neutrality**
Does the migrated `resourceAttributes` schema still carry commerce-specific assumptions
that make no sense outside a buying/selling context? Look for fields like `stock_quantity`,
`sku`, `retail_price`, `cart_eligible`, `return_policy` that presuppose a buyer–seller
retail relationship. These are not wrong, but note them as "commerce-specific" in the
review. A genuinely neutral Resource should make sense if discovered by any participant type.

*Verdict:* NEUTRAL / COMMERCE-SPECIFIC / MIXED (with field list)

**2. Offer abstraction quality**
Does the migrated `offerAttributes` carry the right content? In v2.1, Offer owns commercial
terms and eligibility. Flag any fields that should move: pricing details that are actually
Resource-intrinsic (e.g., a government-regulated fixed price) should stay in Resource;
eligibility constraints that are actually Contract-level commitments should move to
`commitmentAttributes`.

*Verdict:* WELL-PLACED / NEEDS-REDISTRIBUTION (with field-level recommendations)

**3. Contract expressiveness**
Does the Contract model add value over the v2 Order? Look for:
- Are the parties genuinely multi-role (beyond BUYER/SELLER)? If yes — strong fit.
- Do commitments reference both Resources and Offers, or only one type? Both = richer model.
- Is there any scenario where a Contract might involve three or more parties? If yes, flag it
  as a key v2.1 design win to highlight in the README.

*Verdict:* HIGH-FIT / MODERATE-FIT / MINIMAL-FIT (with reasoning)

**4. Performance vs. Fulfillment expressiveness**
Does the `performanceAttributes` schema better express the execution model now that `mode`
can be DELIVERY / SERVICE / ACCESS / TRANSFER / EXECUTION / OTHER? Was there anything in
the v2 `fulfillmentAttributes` that was awkwardly modeled as "delivery" but is really
"service" or "access"? Note any remodeling opportunities.

*Verdict:* IMPROVED / EQUIVALENT / REMODEL-RECOMMENDED (with specifics)

**5. Consideration and Settlement split value**
Was Payment in v2 purely monetary? If yes, the Consideration/Settlement split adds
overhead for minimal gain — note this honestly and recommend keeping `considerationAttributes`
and `settlementAttributes` minimal or omitting them if the domain is purely monetary.
If Payment had non-monetary dimensions (tokens, credits, offsets, escrow) the split
genuinely unlocks new modeling — call this out as a design win.

*Verdict:* SIMPLIFY / NEUTRAL / UNLOCKS-NEW-MODELING (with reasoning)

**6. Cross-domain potential**
Could any of the Resources or Offers in this pack be discoverable or contractable across
domain boundaries — e.g., a carbon credit Resource that could appear in both an energy
network and a compliance network? If yes, this is the core value proposition of v2.1 and
should be documented prominently in the README and IG.

*Verdict:* HIGH-POTENTIAL / DOMAIN-SCOPED / NOT-APPLICABLE (with reasoning)

**7. Attribute redistribution opportunities**
Are there fields in the v2 schema that, now that seven containers exist instead of four,
belong in a different container? Common patterns:
- Order-level metadata that is really per-commitment (e.g., specific SLA per item) → `commitmentAttributes`
- Fulfillment metadata that is really about the value exchange (e.g., delivery charges)
  → `considerationAttributes`
- Item metadata that varies per offer (e.g., discount eligibility tier) → `offerAttributes`

*Verdict:* List of recommended field moves, or NONE.

### Phase D — Produce migration summary and seek approval

After Phases B and C, present the following to the user **before generating any files**:

```
MIGRATION SUMMARY: {domain name}
─────────────────────────────────────────────────────
v2 schemas found:     {list with container names}
v2.1 schemas planned: {list with new container names}
New schemas proposed: {any new containers from Phase B}

PARADIGM FIT REVIEW:
  Resource neutrality:      {verdict + notes}
  Offer abstraction:        {verdict + notes}
  Contract expressiveness:  {verdict + notes}
  Performance mapping:      {verdict + notes}
  Consideration/Settlement: {verdict + notes}
  Cross-domain potential:   {verdict + notes}
  Attribute redistribution: {list or NONE}

OVERALL FIT: STRONG / ADEQUATE / NEEDS-DISCUSSION

Recommended actions before generating files:
  {bulleted list of anything needing user decision}
─────────────────────────────────────────────────────
Proceed with file generation? (or discuss first)
```

**Do NOT generate any files until the user approves the migration summary.**
If OVERALL FIT is NEEDS-DISCUSSION, explain the specific concerns and ask for direction.
If STRONG or ADEQUATE, offer to proceed immediately or discuss first.

Once the user approves, generate all v2.1 files (STEP 4) and run the tester (STEP 5).

---

## STEP 2 — CORE ALIGNMENT CHECK

Before generating schemas, confirm the following against the fetched core files:

**v2.1 Container attachment points** (must reference, not redefine):
- `beckn:resourceAttributes` — extends `Resource`
- `beckn:offerAttributes` — extends `Offer`
- `beckn:contractAttributes` — extends `Contract`
- `beckn:commitmentAttributes` — extends `Commitment` (inline in Contract)
- `beckn:performanceAttributes` — extends `Performance` (inside Contract)
- `beckn:considerationAttributes` — extends `Consideration` (inside Contract)
- `beckn:settlementAttributes` — extends `Settlement` (inside Contract)

**Reusable core constructs** (do not re-model these):
- `Resource`, `Offer`, `Contract`, `Commitment`, `Performance`, `Consideration`, `Settlement`
- `Descriptor`, `Provider`, `Attributes`, `TimePeriod`
- `TrackAction`, `Tracking`, `SupportInfo`, `Rating`, `RatingInput`
- `Catalog`, `DiscoveryContext`, `TransactionContext`

**Checklist:**
- [ ] No duplication of any core construct
- [ ] Naming is consistent with `vocab.jsonld`
- [ ] Attribute containers only extend, never redefine
- [ ] `x-jsonld` annotations reference official IRIs
- [ ] `x-beckn-container` value is one of the seven listed above

---

## STEP 3 — ARCHITECTURAL SANITY SWEEP

Verify schema separation of concerns:

| Schema Container | Responsibility |
|-----------------|---------------|
| `resourceAttributes` | Intrinsic metadata about the resource (what it is, not how it is offered) |
| `offerAttributes` | Commercial terms, eligibility constraints, pricing policy, validity |
| `contractAttributes` | Transaction-level metadata spanning the whole contract lifecycle |
| `commitmentAttributes` | Per-commitment details not captured in the Resource or Offer ref |
| `performanceAttributes` | Execution model specifics (logistics, provisioning, scheduling, geolocation) |
| `considerationAttributes` | Value-exchange specifics beyond monetary amount (e.g., SLA terms, token params) |
| `settlementAttributes` | Discharge mechanism details (gateway ref, blockchain tx, escrow release terms) |

**Enforce:**
- No graph semantics unless domain genuinely requires linked data
- No presentation logic in protocol schemas
- International neutrality — no hardcoded country/currency assumptions
- `resourceAttributes` must NOT contain pricing — pricing belongs in `offerAttributes`
- `performanceAttributes` must NOT contain payment — that belongs in `considerationAttributes`/`settlementAttributes`
- Any modeling exception must be documented in README under Design Rationale

---

## STEP 4 — GENERATE SCHEMA PACK

### Folder Structure

Each schema that attaches directly to a v2.1 container gets its **own top-level folder** with a
`v2.1/` version subfolder inside it. This per-schema versioning allows each schema to be upgraded
independently. Sub-schemas referenced only from one parent live in that parent's `attributes.jsonschema.yaml`.
Shared types go in `{domain}-common/`.

```
{domain}/
├── {DomainResource}/                ← attaches to resourceAttributes
│   └── v2.1/
│       ├── attributes.jsonschema.yaml
│       ├── context.jsonld
│       ├── vocab.jsonld
│       ├── profile.json
│       ├── renderer.json
│       ├── README.md
│       └── examples/
│           ├── example-resource.json   ← on_discover payload
│           └── example-contract.json  ← confirm/status payload (if transactional)
├── {DomainOffer}/                   ← attaches to offerAttributes (if needed)
│   └── v2.1/
│       └── ... (same 7-file structure)
├── {DomainContract}/                ← attaches to contractAttributes (if transactional)
│   └── v2.1/
│       └── ...
├── {DomainPerformance}/             ← attaches to performanceAttributes (if needed)
│   └── v2.1/
│       └── ...
├── {domain}-common/                 ← shared type definitions used by ≥2 schemas
│   └── {SharedTypeName}/
│       ├── attributes.jsonschema.yaml          ← $ref target only
│       └── README.md
└── README.md                        ← domain pack overview
```

**Naming convention:** Schema names use the pattern `{Domain}{Container}` — e.g., `RetailResource`,
`RetailOffer`, `RetailContract`, `RetailPerformance`, `RetailConsideration`, `RetailCommitment`,
`RetailSettlement`. Do NOT include "Core" or "Attributes" in the name. The `x-beckn-container`
annotation already indicates which container the schema extends.

**Rule — top-level schemas:** A schema is top-level if it attaches directly to one of the seven
v2.1 containers. Each top-level schema gets the full 7-file folder structure under its own
`{SchemaName}/v2.1/` directory.

**Rule — sub-schemas (single parent):** Types referenced only from within one parent schema
live in that parent's `attributes.jsonschema.yaml` under `components/schemas`. No separate folder.

**Rule — shared types (multiple parents):** Types referenced by two or more top-level schemas
live in `{domain}-common/{TypeName}/` with only `attributes.jsonschema.yaml` + `README.md`.

**Rule — cross-schema `$ref` paths:** When a child schema extends a parent via `allOf`, the
`$ref` path must account for the versioned folder layout. For example, a `FoodAndBeverageResource`
extending `RetailResource` uses:
```yaml
allOf:
  - $ref: '../../RetailResource/v2.1/attributes.jsonschema.yaml#/components/schemas/RetailResource'
```
Note the `../../` to go up from `FoodAndBeverageResource/v2.1/` to the domain root, then
down into `RetailResource/v2.1/`.

**CodedValue pattern:** Use for any field whose authority is external (government codes,
commodity classification, standards bodies). Place in `{domain}-common/CodedValue/`:
```yaml
CodedValue:
  type: object
  required: ["@context", "@type", "code"]
  properties:
    "@context": { type: string, format: uri }   # Canonical URI of the code system authority
    "@type":    { type: string }                 # Code class within the identified context
    code:       { type: string }                 # The code value
```

All files must be **complete and production-ready**. See file specs below.

---

## FILE SPECIFICATIONS

### `attributes.jsonschema.yaml`
- OpenAPI **3.1.1** format
- `info.version` must match the schema pack folder name convention: `"2.1.0"` for a `v2.1/`
  folder, `"2.2.0"` for `v2.2/`, etc. This is the schema pack's own release version —
  independent of the Beckn protocol version.
- `x-jsonld-id` annotation (flat form) on every property — e.g., `x-jsonld-id: "prefix:propName"`.
  Do NOT use the nested form `x-jsonld: { "@id": "..." }`
- `x-beckn-container` on the top-level schema (e.g., `x-beckn-container: resourceAttributes`)
- `$ref` back to core YAML (never inline-copy core schemas)
- No container object redefinition
- Sub-schemas defined under `components/schemas` in the same file

### `context.jsonld`
- Map every property to a `schema.org` or domain-specific IRI
- No orphan properties
- Vocab class aliases MUST be string form: `"ClassName": "prefix:ClassName"` (not dict form `{"@id": "..."}`)
- **Import generalised core context:**
  ```json
  "@import": "https://schema.beckn.io/core/v2/context.jsonld#generalised"
  ```
- **Namespace convention** (collision-safe, mandatory):
  - `"schema": "https://schema.org/"` — for schema.org terms
  - `"beckn": "https://schema.beckn.io/"` — for core Beckn protocol terms only
  - `"<abbr>": "https://schema.beckn.io/{SchemaName}#"` — one short prefix per top-level
    schema using `#` fragment separator. Example: `"djr": "https://schema.beckn.io/DriverJobResource#"`
  - Never use a single flat domain prefix shared across multiple schemas

### `vocab.jsonld`
- Enumerations **only** — no structural schema
- Human-readable labels (`rdfs:label`) and comments (`rdfs:comment`) for each enum term
- Import core vocab: `"@import": "https://schema.beckn.io/core/v2/vocab.jsonld"`
- Use the same per-schema prefix (`<abbr>:`) for all enum class and instance IRIs

### `profile.json`
```jsonc
{
  "id": "https://schema.beckn.io/{SchemaName}/v1",
  "name": "...",
  "version": "{folder-version}.0",
  "protocol_version": "2.0",
  "semantic_model": "generalised",
  "included_schemas": [...],
  "discovery_fields": [...],
  "indexable_paths": [...],
  "filterable_paths": [...],
  "sortable_paths": [...],
  "privacy_notes": [...]
}
```
Note `protocol_version: "2.0"` (the Beckn protocol version — stays at 2.0 because the
generalised model is a non-breaking extension, not a protocol bump) and
`semantic_model: "generalised"` — both mandatory. The `version` field is the schema pack's
own release version and must match the folder name convention: for a `v2.1/` folder use
`"2.1.0"`, for `v2.2/` use `"2.2.0"`, and so on. This keeps `profile.json` and the
filesystem layout consistent, and makes it unambiguous that protocol and schema pack versions
are separate axes.

### `renderer.json`
Core + attribute bindings for UI rendering. Must include **four** template properties:

- `card_template`: Moustache template for list/search view (legacy text-based)
- `detail_template`: Moustache template for resource detail view (legacy text-based)
- `html`: Handlebars HTML template for card/listing rendering in a browser. A self-contained
  `<div>` with class `{domain}-{usecase}-resource-card`. Must reference domain-specific
  `resourceAttributes` fields, `beckn:descriptor`, `beckn:offers[0].beckn:proposedConsideration`
  for pricing, and `beckn:rating` for ratings. Use `{{#if}}`, `{{#each}}`, and
  `{{get "path.with.colons"}}` helpers as needed.
- `html_detail`: Handlebars HTML template for full-detail panel rendering. Class:
  `{domain}-{usecase}-resource-detail`. Includes all fields from `html` plus expanded
  sections for commitments, performance details, and contract terms.

**HTML template generation guidance:**
- Root div: `<div class="{domain}-{usecase}-resource-card" data-resource-id="{{beckn:id}}">`
- Primary image: `<img src='{{get "beckn:descriptor.schema:image[0]"}}' alt='{{beckn:descriptor.schema:name}}' />`
- Heading: `<h3>{{beckn:descriptor.schema:name}}</h3>`
- Short description: `<p>{{beckn:descriptor.beckn:shortDesc}}</p>`
- Price/consideration chip: reference `{{beckn:offers[0].beckn:proposedConsideration.amount.value}}`
  and `{{beckn:offers[0].beckn:proposedConsideration.amount.currency}}`
- Domain attributes: generate one chip or labelled span per `resourceAttributes` field
- Enum fields: use `<span class="badge badge-{{toLowerCase fieldValue}}">{{fieldValue}}</span>`
- Array fields: wrap in `{{#each fieldArray}}<span>{{this}}</span>{{/each}}`
- Boolean fields: wrap in `{{#if fieldName}}...{{/if}}`
- Ratings block (if rating is present):
  ```html
  <div class="rating-stars-container" data-rating="{{beckn:rating.beckn:ratingValue}}">
    <span class="star">★</span><span class="star">★</span>
    <span class="star">★</span><span class="star">★</span><span class="star">★</span>
  </div>
  <span class="rating-value-text">{{beckn:rating.beckn:ratingValue}}</span>
  <span class="rating-count">({{beckn:rating.beckn:ratingCount}} ratings)</span>
  ```
- All `{{placeholder}}` values must map to real paths in `attributes.jsonschema.yaml` or core

### `README.md`
Header block (required):
```markdown
# {SchemaName} Schema

**Container:** `Resource.resourceAttributes`   (or whichever v2.1 container applies)
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** {folder-version}.0
**Use Cases:** {use case list}
**Tag:** {domain tags, space-separated}
```

Body must contain:
1. **Overview** — what vertical/use case this covers
2. **Attachment points** — which v2.1 containers are extended and why
3. **Design rationale** — key modeling decisions explained
4. **Non-goals** — what this schema explicitly does NOT model
5. **Upstream candidates** — attributes generic enough for Beckn core promotion

### `examples/` (minimum 2 files)

**example-resource.json** — Full `on_discover` payload:
```json
{
  "context": {
    "action": "on_discover",
    "schema_context": ["https://schema.beckn.io/{SchemaName}/context.jsonld"]
  },
  "message": {
    "catalogs": [{
      "@context": "https://schema.beckn.io/core/v2/context.jsonld#generalised",
      "@type": "beckn:Catalog",
      "beckn:id": "...",
      "beckn:resources": [{
        "@context": "https://schema.beckn.io/core/v2/context.jsonld#generalised",
        "@type": "beckn:Resource",
        "beckn:id": "...",
        "beckn:descriptor": { ... },
        "beckn:resourceAttributes": { ... }
      }],
      "beckn:offers": [{ ... }]
    }]
  }
}
```

**example-contract.json** — Full `on_confirm` payload (for transactional schemas):
```json
{
  "context": { "action": "on_confirm", "schema_context": [...] },
  "message": {
    "contract": {
      "@context": "https://schema.beckn.io/core/v2/context.jsonld#generalised",
      "@type": "beckn:Contract",
      "beckn:id": "...",
      "beckn:status": "CONFIRMED",
      "beckn:parties": [...],
      "beckn:commitments": [{ "beckn:ref": "...", "beckn:refType": "RESOURCE", "beckn:commitmentAttributes": { ... } }],
      "beckn:consideration": [{ "@type": "beckn:Consideration", "beckn:type": "MONETARY", "beckn:status": "AGREED", ... }],
      "beckn:performance": [{ "@type": "beckn:Performance", "beckn:id": "...", "beckn:status": "PLANNED", "beckn:performanceAttributes": { ... } }],
      "beckn:contractAttributes": { ... }
    }
  }
}
```

---

## STEP 5 — VALIDATE WITH SCHEMA TESTER

After generating all schema files, invoke the **beckn-v21-schema-tester** skill to run the
four-layer test suite against the generated pack.

The tester will auto-discover schema folders under `v2.1/` and run:
- L1 OpenAPI structural checks (including v2.1 container validation)
- L2 JSON-LD prefix resolution (accepting `#generalised` context import)
- L3 Cross-file consistency (attributes ↔ context ↔ vocab)
- L4 Example payload validation against core + extension schemas

Fix all failures before the summary step.

---

## STEP 6 — POST-GENERATION SUMMARY

After generating the full schema pack and passing all tests, provide:

**Both modes:**
1. **Vertical sanity sweep** — confirm each schema handles only its designated concern
2. **Core alignment confirmation** — list every v2.1 core construct referenced (not duplicated)
3. **Upstream candidates** — attributes generic enough for Beckn core promotion

**Migration mode additionally:**
4. **Migration delta table** — every v2 field/container and its v2.1 destination
5. **Paradigm fit verdict** — one paragraph summarising the fit review from Phase C, calling
   out any genuine design wins (e.g., cross-domain potential, non-monetary consideration) and
   any residual commerce-specific assumptions that were preserved for practical reasons
6. **Redistribution decisions** — confirm which (if any) field moves were made vs. deferred

---

## RULES (Non-negotiable)

| Rule | Detail |
|------|--------|
| No core duplication | Never re-model `Resource`, `Contract`, `Performance`, `Consideration`, `Settlement`, etc. |
| No container redefinition | Only extend `resourceAttributes`, `offerAttributes`, `contractAttributes`, `commitmentAttributes`, `performanceAttributes`, `considerationAttributes`, `settlementAttributes` |
| Resource neutrality | Resources represent a single committable unit of value — not commerce-specific |
| Commercial isolation | Pricing/terms live in `offerAttributes`, not `resourceAttributes` |
| Execution isolation | Logistics/provisioning live in `performanceAttributes`, not `contractAttributes` |
| Value-exchange isolation | Payment/token terms in `considerationAttributes`; discharge records in `settlementAttributes` |
| International neutrality | Abstract country/currency assumptions unless truly domain-specific |
| Per-schema versioned folder | Each schema gets `{SchemaName}/v2.1/` — never a single shared `v2.1/` directory |
| Concise schema names | Use `{Domain}{Container}` (e.g., `RetailResource`) — no "Core" or "Attributes" suffix |
| One folder per top-level schema | Each container-attached schema gets its own folder with 7 files |
| Per-schema namespace prefix | Use `"<abbr>": "https://schema.beckn.io/{SchemaName}#"` — never a flat domain prefix |
| Flat `x-jsonld-id` annotations | Use `x-jsonld-id: "prefix:prop"` — never the nested form `x-jsonld: { "@id": "..." }` |
| String-form vocab aliases | In `context.jsonld`, class aliases must be strings `"Class": "prefix:Class"` — not dicts |
| Generalised context import | Always use `"@import": "https://schema.beckn.io/core/v2/context.jsonld#generalised"` |
| HTML templates mandatory | renderer.json must include both `html` and `html_detail` Handlebars templates |
| Migration is never purely mechanical | v2→v2.1 must include a paradigm fit review (STEP 1-M Phase C) before generating files |
| Migration approval gate | Never generate files in migration mode without presenting the migration summary and receiving user approval |
| No v1 direct migration | v1→v2.1 is always two-step: v1→v2 via `beckn-v2-schema`, then v2→v2.1 via this skill |
| Ask before assuming | If domain detail is missing, ask — never guess |

---

## REFERENCE FILES

See `references/` folder for:
- `beckn-v2.1-core-primer.md` — Summary of the v2.1 generalised model and composability patterns
- `v2-to-v2.1-mapping.md` — Field-level migration from v2 Item/Order/Fulfillment/Payment to v2.1

### When to Read Reference Files

**Always read** `beckn-v2.1-core-primer.md` before generating any schema pack (either mode).

**Read `v2-to-v2.1-mapping.md`** at the start of every Migration mode run (STEP 1-M). It is
the canonical field-level mapping reference for Phase B and is also the basis for the
migration summary table shown to the user in Phase D.

### Adding New Domain References

When asked, save key modeling decisions as `references/{domain-name}.md` following the structure:
- v2 → v2.1 field migration table (if applicable)
- Sub-use-case breakdown with Resource/Offer/Contract attribute breakdown per use case
- Design rationale
- Upstream candidates
