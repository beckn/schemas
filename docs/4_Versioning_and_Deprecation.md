# Versioning and Deprecation

**Status:** Released  
**Author(s):** Ravi Prakash (FIDE / Beckn Foundation)  
**Created:** 2026-02-23  
**Updated:** 2026-02-23  
**Conformance impact:** Normative  
**Security/privacy implications:** No security or privacy implications identified.  
**Replaces / Relates to:** Normative companion to [5_Versioning_and_Compatibility.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/5_Versioning_and_Compatibility.md) in `protocol-specifications-v2`. Aligned with [GOVERNANCE.md](../GOVERNANCE.md) § 6.

---

## Abstract

This document specifies the versioning scheme, version lifecycle, deprecation rules, and backward-compatibility guarantees for the Beckn Protocol Core Schema library. It defines what constitutes a Patch, Minor, or Major change; how version directories are created and retained; and what obligations the repository has toward consumers of deprecated terms.

The key words MUST, SHOULD, and MAY in this document are used as defined in [2_Keyword_Definitions.md](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md).

---

## 1. Context

The Beckn Protocol Core Schema is consumed by a wide variety of systems — domain schema packs, API gateways, catalog publishers, contract processing pipelines, and Linked Data platforms. These consumers have different tolerance for change:

- **Patch changes** (typo fixes, clarifications) are safe to absorb at any time.
- **Minor changes** (new optional attributes) require consumers to update their implementations to benefit, but do not break existing integrations.
- **Major changes** (renamed terms, removed schemas, semantic reinterpretations) require advance notice, a migration path, and a defined backward-compatibility window.

This document specifies the rules that govern all three change types.

---

## 2. Version Scheme

### 2.1 Repository Version

The repository as a whole is versioned using **Semantic Versioning** (`MAJOR.MINOR.PATCH`):

| Component | Trigger |
|---|---|
| `MAJOR` | A breaking change: removal of a schema, rename of a term, semantic reinterpretation |
| `MINOR` | A backward-compatible addition: new schema, new optional attribute |
| `PATCH` | A non-structural correction: typo fix, description update, example addition |

The current release is `v2.0.0`.

### 2.2 Schema Directory Version

Each schema's version directory uses the `v{MAJOR}.{MINOR}` path scheme (without Patch):

| Directory | Meaning |
|---|---|
| `v2.0/` | Initial v2 release |
| `v2.1/` | Minor update to v2 (new optional attributes or schemas) |
| `v3.0/` | Major update (breaking change) |

**Patch changes do not create new directories.** They are applied in place to the existing version directory, and the change is recorded in `CHANGELOG.md`.

### 2.3 Version in `attributes.yaml`

The `info.version` field in `attributes.yaml` MUST use three-part semver (`MAJOR.MINOR.PATCH`) and MUST be updated on every change (including Patch changes).

---

## 3. Change Classification

### 3.1 Patch Change

A Patch change:
- MUST NOT alter the set of attributes in any schema
- MUST NOT alter the JSON-LD term mappings in any context file
- MUST NOT alter the RDF class or property declarations in any vocabulary file
- MAY correct spelling, grammar, or formatting in any `description` field
- MAY add or correct examples

**Effect on versioning:**
- Repository version: `PATCH` increment (e.g., `v2.0.0` → `v2.0.1`)
- Schema directory: unchanged (no new directory)
- `info.version` in `attributes.yaml`: `PATCH` increment

### 3.2 Minor Change

A Minor change:
- MAY add new optional attributes to an existing schema
- MAY add new schemas
- MAY add new enumeration values to an existing controlled vocabulary
- MUST NOT remove any existing attribute, schema, or enumeration value
- MUST NOT change the type or semantics of any existing attribute

**Effect on versioning:**
- Repository version: `MINOR` increment (e.g., `v2.0.1` → `v2.1.0`)
- Schema directory: a new `v2.1/` directory is created; `v2.0/` is retained
- Root `schema/context.jsonld`: updated to include the new terms
- `CHANGELOG.md`: updated with the new additions

### 3.3 Major Change

A Major change:
- MAY remove a schema that has been deprecated for at least one Minor version cycle
- MAY rename a term (the old term MUST have been deprecated for at least one Minor version cycle)
- MAY alter the semantics of an existing attribute in a breaking way
- MUST include a deprecation notice in the preceding Minor release
- MUST include a migration guide in `CHANGELOG.md`
- MUST remain open for community review for a minimum of 14 calendar days (per [GOVERNANCE.md](../GOVERNANCE.md))

**Effect on versioning:**
- Repository version: `MAJOR` increment (e.g., `v2.1.0` → `v3.0.0`)
- Schema directory: a new `v3.0/` directory is created; `v2.x/` directories are retained and frozen
- Namespace IRI: updated to `https://schema.beckn.io/core/v3.0/`
- `CHANGELOG.md`: updated with the full breaking change log and migration instructions

---

## 4. Deprecation

### 4.1 What May Be Deprecated

Any of the following MAY be deprecated:
- An entire schema
- A required or optional attribute within a schema
- An enumeration value within a controlled vocabulary
- A term alias (e.g., a camelCase alias of a snake_case term)

### 4.2 Deprecation Process

A deprecation MUST follow this sequence:

**Step 1 — Announce (Minor release):**
- Add `deprecated: true` to the relevant attribute or schema in `attributes.yaml`
- Add a `description` note citing the replacement (e.g., `"Deprecated. Use Contract instead."`)
- Add an `@comment` to the relevant entry in `schema/context.jsonld`
- Add an `owl:deprecated` annotation to the relevant entry in `schema/vocab.jsonld`
- Record the deprecation in `CHANGELOG.md`

**Step 2 — Retain (same Minor release and all subsequent Minor releases):**
- The deprecated term MUST remain fully functional in all its files
- The deprecated term's IRI MUST be retained in `schema/context.jsonld`
- The per-schema `context.jsonld` and `vocab.jsonld` files MUST NOT be deleted

**Step 3 — Remove (Major release only):**
- The deprecated term MAY be removed from `attributes.yaml` and `vocab.jsonld` in a Major release
- The deprecated term's IRI MUST be retained in `schema/context.jsonld` indefinitely (for Linked Data backward compatibility)
- The version directory containing the deprecated schema MUST be retained (frozen, read-only)

### 4.3 Minimum Deprecation Window

A term MUST NOT be removed in a Major release unless it has been marked as deprecated in at least one preceding Minor or Major release.

The minimum deprecation window is **one Minor version cycle** before removal in a Major release.

---

## 5. Version Retention

### 5.1 Schema Directory Retention

When a new Minor version is released (e.g., `v2.1/`):
- The previous version directory (`v2.0/`) MUST be retained unchanged
- Both directories MUST be present in the repository simultaneously

When a new Major version is released (e.g., `v3.0/`):
- All previous version directories (`v2.0/`, `v2.1/`, etc.) MUST be retained, frozen
- The root `schema/context.jsonld` is updated to the new namespace
- The previous version's root context (`v2.0/context.jsonld`) MUST be accessible at its original URL

### 5.2 IRI Retention

IRIs assigned within a namespace version (e.g., `https://schema.beckn.io/core/v2.0/Address`) MUST be considered permanent. Once published, an IRI MUST NOT be reassigned to a different concept.

---

## 6. v2.0 Deprecation Register

The following terms were deprecated in v2.0 (the initial release). They are retained as backward-compatible aliases:

| Deprecated term | Replacement term | Replacement IRI | Notes |
|---|---|---|---|
| `Order` | `Contract` | `beckn:Contract` | Schema renamed for semantic clarity |
| `OrderItem` | `ContractItem` | `beckn:ContractItem` | Schema renamed for semantic clarity |
| `SupportInfo` | `Support` | `beckn:Support` | Schema renamed for brevity |
| `orderStatus` (enum values) | `contractStatus` (enum values) | Same IRIs | Enum key renamed; IRIs unchanged |

---

## 7. Conformance Requirements

| ID | Requirement | Level |
|---|---|---|
| VER-01 | The repository MUST use `MAJOR.MINOR.PATCH` versioning | MUST |
| VER-02 | Patch changes MUST NOT create new version directories | MUST |
| VER-03 | Minor changes MUST create a new `v{MAJOR}.{MINOR}/` directory | MUST |
| VER-04 | Previous version directories MUST be retained when a new version is released | MUST |
| VER-05 | A term MUST NOT be removed unless it has been deprecated in a prior release | MUST |
| VER-06 | Deprecated term IRIs MUST be retained in `schema/context.jsonld` indefinitely | MUST |
| VER-07 | The minimum deprecation window before removal is one Minor version cycle | MUST |
| VER-08 | Major changes MUST include a migration guide in `CHANGELOG.md` | MUST |
| VER-09 | Major changes MUST remain open for review for at least 14 calendar days | MUST |

---

## 8. Security Considerations

Retaining deprecated IRIs in the root context indefinitely ensures that Linked Data graphs built against older versions of the schema remain valid. Removing IRIs could silently corrupt the semantics of archived documents.

---

## 9. Migration Notes

This is the initial v2.0 release. The migration path from Beckn Protocol v1.x schemas is documented in the [protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2) repository.

---

## 10. References

- [5_Versioning_and_Compatibility.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/5_Versioning_and_Compatibility.md)
- [2_Keyword_Definitions.md — protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2/blob/core-2.0.0-rc2-alt/docs/2_Keyword_Definitions.md)
- [GOVERNANCE.md](../GOVERNANCE.md)
- [CHANGELOG.md](../CHANGELOG.md)
- [Semantic Versioning 2.0.0](https://semver.org/)

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| Draft-01 | 2026-02-23 | Ravi Prakash | Initial versioning and deprecation specification |
