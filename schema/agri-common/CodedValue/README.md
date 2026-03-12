# CodedValue — Shared Type Definition

**Location:** `agri-common/CodedValue/attributes.yaml`
**$ref target:** `../agri-common/CodedValue/attributes.yaml#/components/schemas/CodedValue`

---

## What this is

`CodedValue` is a **shared type definition** — not a first-class item schema. It has no catalogue entry, no renderer, and no Beckn profile. It exists purely as a reusable building block that other schemas in this pack reference via `$ref`.

It represents a typed code from any authoritative coding system, using JSON-LD identity conventions consistent with Beckn v2 extension schema patterns:

```json
{
  "@context": "https://lgdirectory.gov.in",
  "@type":    "LGDDistrict",
  "code":     "507"
}
```

---

## Why a shared type, not an inline definition

The same structure — authority URI + type name + code string — recurs wherever this schema pack needs to reference external or controlled code systems: in item attribute coverage areas, in fulfillment target locations, and potentially in offer attributes for commodity codes. Defining it once here and referencing it via `$ref` ensures:

- **Consistency** — all CodedValue instances across the pack have identical structure and validation rules.
- **Single point of change** — if the pattern evolves (e.g. adding an optional `display` label field), the change propagates everywhere automatically.
- **Clarity of intent** — a `$ref` to `CodedValue` communicates design intent more clearly than an anonymous inline object definition.

---

## Why it lives in `agri-common/`

The flat repository structure for Beckn v2 schema packs places every schema folder at the same level. `agri-common/` is the designated container for type definitions and utilities that are **shared across multiple schemas within the agri-advisory domain pack** but are not (yet) part of Beckn core.

The naming convention `<domain>-common/` scopes ownership clearly in a flat repo where multiple domain packs may coexist, avoiding collisions with similarly named folders in other domains.

---

## Upstream candidacy

`CodedValue` is explicitly an **upstream candidate** for promotion to Beckn core. The pattern is domain-agnostic — any Beckn domain that references external administrative codes, commodity classification systems, or third-party controlled vocabularies would benefit from it.

See **RFC-001-CodedValue-Pattern.md** in the root of this schema pack for the full design rationale, the thumb rules for `CodedValue` vs plain enum, and the upstream proposal.

If/when `CodedValue` is promoted to Beckn core:
1. The canonical location moves to a Beckn-maintained shared library (e.g. `beckn-core/shared/CodedValue/`).
2. All `$ref` paths in this pack that currently point to `../agri-common/CodedValue/attributes.yaml` are updated to the new canonical path.
3. This folder becomes a redirect shim or is retired.

---

## Current consumers in this pack

| Schema | Field | Purpose |
|---|---|---|
| `WeatherForecastItemAttributes` | `coverageAreaCodes` | Administrative codes (LGD district/sub-district) indicating forecast coverage area |
| `AgriAdvisoryFulfillmentAttributes` | `targetLocation.areaCodes` | Administrative codes identifying the buyer's target delivery location |

---

## Thumb rules: CodedValue vs plain enum

| Use `CodedValue` when… | Use a plain `enum` when… |
|---|---|
| The code authority is external (LGD, India Post, WMO, ICAR) | You own the value set entirely |
| Multiple code systems may be used for the same concept | Values are operational/structural (delivery modes, status flags) |
| The value set is too large or dynamic to enumerate | The set has ≤ 15 stable values |
| The field is a strong upstream candidate | The field is domain-specific with no cross-domain reuse |

For the full decision table and worked examples, see RFC-001-CodedValue-Pattern.md.
