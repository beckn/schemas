# Beckn Protocol Core Schema — Documentation

This folder contains the RFC-style specification documents for the Beckn Protocol Core Schema repository.

The documents are ordered as a **progressive reading journey** — from the most general concepts through to the most detailed normative specifications. A reader who follows the documents in order will arrive at a full understanding of the core schema library, its structure, and its governance.

---

## How to Read This Documentation

Each document belongs to one of two types:

- **Narrative** — informative, conceptual explanations. No prior implementation knowledge required.
- **RFC** — normative specifications. Each RFC uses the keyword definitions from [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md) (MUST / SHOULD / MAY).

---

## Stage 1 — Before You Read Anything Else

> **Goal:** Understand what this repository is, where it sits in the Beckn ecosystem, and how the documents in it are structured.

| # | Document | Type | What you learn |
|---|---|---|---|
| 1 | [1_Introduction.md](./1_Introduction.md) | Narrative | What the Core Schema library is; its role in the three-tier schema model; how it relates to `protocol-specifications-v2` and domain schema packs |
| 2 | [2_Schema_Structure.md](./2_Schema_Structure.md) | RFC | The normative directory layout and file conventions for every schema in this repository |

---

## Stage 2 — Understanding the Semantic Layer

> **Goal:** Understand how JSON-LD contexts and RDF vocabularies give the schemas their machine-readable, interoperable semantics.

| # | Document | Type | What you learn |
|---|---|---|---|
| 3 | [3_JSON_LD_Context_and_Vocabulary.md](./3_JSON_LD_Context_and_Vocabulary.md) | RFC | How `schema/context.jsonld` and `schema/vocab.jsonld` work; the `beckn:` IRI namespace; `@protected` contexts; deprecated term aliases and backward compatibility |

---

## Stage 3 — Versioning and Evolution

> **Goal:** Understand how schemas evolve, how breaking changes are handled, and what backward-compatibility guarantees this repository provides.

| # | Document | Type | What you learn |
|---|---|---|---|
| 4 | [4_Versioning_and_Deprecation.md](./4_Versioning_and_Deprecation.md) | RFC | Schema version lifecycle; Patch / Minor / Major version semantics; deprecation rules; IRI backward-compatibility guarantees; v2.0 deprecation register |

---

## Stage 4 — Contributing

> **Goal:** Understand how to propose, author, and submit changes to the core schema library.

| # | Document | Type | What you learn |
|---|---|---|---|
| 5 | [5_Contributing_Schemas.md](./5_Contributing_Schemas.md) | Informative | How to propose a new schema; how to author the three required files; PR checklist; links to `CONTRIBUTING.md` and `GOVERNANCE.md` |

---

## Governance

All RFCs in this folder follow the lifecycle defined in [GOVERNANCE.md](../GOVERNANCE.md):

```
Proposal → Draft → Candidate → Released → Deprecated → Removed
```

Any normative change MUST include a conformance impact classification (Patch / Minor / Major / Informative) and explicit security/privacy implications, as required by the Governance Model.

---

## Quick Reference by Audience

| I am a... | Start here | Then read |
|---|---|---|
| **New to Beckn v2 schema** | 1 | 2, 3 |
| **Domain schema pack author** | 1, 2, 3 | 4, 5 |
| **Implementor using `$ref`** | 1, 2 | 3 |
| **Implementor using JSON-LD** | 1, 3 | 2, 4 |
| **Contributor proposing a new schema** | 1, 2, 3 | 4, 5 |
| **Maintainer reviewing a PR** | 2, 4 | 5, [GOVERNANCE.md](../GOVERNANCE.md) |

---

## Cross-Repository References

These documents in `protocol-specifications-v2` are directly relevant to readers of this repository:

| Document | Relevance |
|---|---|
| [5_Versioning_and_Compatibility.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/5_Versioning_and_Compatibility.md) | Protocol-wide versioning and semver policy |
| [6_Schema_Distribution_Model.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/6_Schema_Distribution_Model.md) | How core schema, domain packs, and the transport envelope relate |
| [20_JSONld_Context_and_Schema_Alignment.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/20_JSONld_Context_and_Schema_Alignment.md) | Protocol-wide JSON-LD context design rules |
| [21_Schema_Pack_Contract.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md) | How to build a domain schema pack on top of core schema |
| [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md) | MUST / SHOULD / MAY definitions used in all RFCs |
