# Governance — Beckn Protocol Core Schema

**Status:** Released  
**Author(s):** Ravi Prakash (FIDE / Beckn Foundation)  
**Created:** 2026-02-23  
**Updated:** 2026-02-23  
**Conformance impact:** Informative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Aligned with the Beckn Protocol v2 Governance Model. See [protocol-specifications-v2 GOVERNANCE.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/GOVERNANCE.md).

---

## Abstract

This document defines the governance model for the `beckn/common_schema` repository, which contains the Beckn Protocol Core Schema definitions. It describes the roles, responsibilities, decision-making processes, and lifecycle rules that govern all changes to the core schemas, their JSON-LD contexts, and their RDF vocabularies.

---

## 1. Introduction

The Beckn Protocol Core Schema is a foundational artefact of the Beckn Protocol v2 ecosystem. Because changes to these schemas can affect every Beckn network and every domain pack that builds on them, a clear and predictable governance model is essential.

This governance model is designed to balance three goals:

- **Stability** — implementors must be able to rely on the schemas not changing in breaking ways without adequate notice.
- **Evolvability** — the schemas must be able to grow and improve as the protocol matures.
- **Openness** — any participant in the Beckn ecosystem SHOULD be able to propose changes.

The key words MUST, SHOULD, and MAY in this document are used as defined in [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md).

---

## 2. Governing Body

The Beckn Protocol Core Schema is governed by the **Beckn Foundation**, acting through the **Core Schema Working Group** (CSWG).

The CSWG is responsible for:
- Reviewing and approving all Normative changes to the core schemas
- Publishing new versioned releases
- Maintaining backward-compatibility guarantees
- Resolving disputes between contributors

**Founding Maintainer:** Ravi Prakash (FIDE / Beckn Foundation)

---

## 3. Roles

### 3.1 Maintainer

A Maintainer has write access to the repository and is responsible for:
- Reviewing and merging pull requests
- Enforcing the schema authoring conventions defined in [`docs/2_Schema_Structure.md`](./docs/2_Schema_Structure.md)
- Tagging releases
- Maintaining the CHANGELOG

The current list of Maintainers is recorded in the repository's GitHub Teams configuration.

### 3.2 Contributor

A Contributor is any individual or organisation that submits a pull request or raises an issue. Contributors do not require prior approval to participate. All contributions are governed by the [`CONTRIBUTING.md`](./CONTRIBUTING.md) guidelines and the [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

### 3.3 Adopter

An Adopter is any organisation that uses the core schemas in a production Beckn network. Adopters are encouraged to participate in schema proposals, particularly for deprecation and migration notices.

---

## 4. Design Principles

All schema changes MUST be evaluated against the following Beckn constitutional principles:

- **Interoperability-first:** A schema change MUST NOT reduce interoperability between conformant implementations without a Major version increment.
- **Abstraction over specificity:** Schemas MUST remain domain-agnostic. Domain-specific attributes belong in domain schema packs, not in this repository.
- **Optimal ignorance:** Schemas SHOULD NOT include attributes that are not required for interoperability. Minimalism is preferred.
- **Security by design:** Any schema change that introduces a new authentication, authorisation, or cryptographic attribute MUST include an explicit security analysis in the proposing RFC.
- **Reusability before novelty:** Before introducing a new schema, contributors MUST verify that no existing schema covers the required semantics.

---

## 5. Change Process

### 5.1 Types of Change

Changes are classified by their conformance impact:

| Type | Description | Example |
|---|---|---|
| **Patch** | Corrects errors without altering semantics or structure | Fix a typo in a description field |
| **Minor** | Adds new optional attributes or new schemas (backward-compatible) | Add a new optional field to `Address` |
| **Major** | Removes or renames attributes, changes semantics, or removes schemas | Rename `orderStatus` to `contractStatus` |
| **Informative** | Updates documentation, examples, or metadata only | Update a doc in `docs/` |

### 5.2 Proposing a Change

1. **Raise an issue** in the repository describing the proposed change, its motivation, and its conformance impact classification.
2. If the change is Minor or Major, the proposer SHOULD author a short RFC document in `docs/` following the template in [`3_RFC_Template.md`](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/3_RFC_Template.md).
3. Open a pull request referencing the issue.
4. The PR MUST receive at least one approving review from a Maintainer before merging.
5. Major changes MUST remain open for a minimum of **14 calendar days** to allow community review.

### 5.3 Lazy Consensus

For Patch and Informative changes, **lazy consensus** applies: if no Maintainer raises an objection within **7 calendar days** of a PR being opened, it MAY be merged by any Maintainer.

For Minor and Major changes, **explicit approval** from at least one Maintainer is required.

### 5.4 Merge Criteria

A pull request MAY be merged when all of the following are satisfied:

- [ ] The schema change follows the directory and file conventions in [`docs/2_Schema_Structure.md`](./docs/2_Schema_Structure.md)
- [ ] The JSON-LD context and vocabulary have been updated consistently with the schema change
- [ ] The `schema/README.md` schema list has been updated if a schema was added or removed
- [ ] The `CHANGELOG.md` has been updated with an entry for this change
- [ ] No unresolved review comments remain

---

## 6. Versioning Policy

The core schemas use a **path-based versioning scheme** aligned with the Beckn Protocol semver policy defined in [`5_Versioning_and_Compatibility.md`](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/5_Versioning_and_Compatibility.md).

| Version Increment | Trigger | Directory change |
|---|---|---|
| **Patch** (e.g., v2.0 → v2.0.1) | Documentation correction, no structural change | None — existing directory updated |
| **Minor** (e.g., v2.0 → v2.1) | New optional attributes or new schemas added | New `v2.1/` directory; `v2.0/` retained |
| **Major** (e.g., v2.0 → v3.0) | Breaking structural or semantic change | New `v3.0/` directory; `v2.0/` deprecated |

### 6.1 Deprecation

A schema or attribute that is deprecated MUST:

1. Be annotated with a deprecation notice in its `attributes.yaml` (`deprecated: true` and a `description` citing the replacement)
2. Have its JSON-LD context entry updated with an `@comment` indicating the deprecated status and the replacement IRI
3. Remain in the repository for a minimum of **one Major version cycle** after deprecation before removal
4. Be listed in the `CHANGELOG.md` deprecation section for the relevant release

---

## 7. Release Process

1. A Maintainer creates a release branch `release/vX.Y`.
2. The `CHANGELOG.md` is updated with the full set of changes for the release.
3. A GitHub Release is tagged as `vX.Y.0`.
4. The `schema/context.jsonld` namespace IRI is updated if a Major version increment has occurred.

---

## 8. RFC Lifecycle

Schema proposals that are documented as RFCs in `docs/` follow this lifecycle:

```
Proposal → Draft → Candidate → Released → Deprecated → Removed
```

| Stage | Description |
|---|---|
| **Proposal** | Issue raised; RFC document not yet authored |
| **Draft** | RFC document authored; open for community comment |
| **Candidate** | Approved by at least one Maintainer; implementation testing underway |
| **Released** | Merged and tagged in a release |
| **Deprecated** | Superseded by a later RFC; retained for reference |
| **Removed** | Archived; no longer applicable |

---

## 9. Code of Conduct

All participants in this repository MUST abide by the [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md). Violations may be reported to the Beckn Foundation at [conduct@beckn.org](mailto:conduct@beckn.org).

---

## 10. References

- [2_Keyword_Definitions.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md)
- [5_Versioning_and_Compatibility.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/5_Versioning_and_Compatibility.md)
- [21_Schema_Pack_Contract.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/21_Schema_Pack_Contract.md)
- [RFC 2119 — Key words for use in RFCs](https://datatracker.ietf.org/doc/html/rfc2119)
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial governance model for core_schema repository |
