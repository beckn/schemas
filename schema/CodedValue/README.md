# CodedValue Schema

**Container:** *(none — shared sub-schema, not a first-class Beckn container)*
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Use Cases:** Any schema requiring typed, machine-filterable codes drawn from an external authority
**Tag:** generic-service shared-type

## Overview

`CodedValue` is a shared sub-schema for representing a single code drawn from an external or
administrative coding authority (e.g. LGD, KNBS, ISO, ICD-10). It is modelled on the
[FHIR Coding](https://www.hl7.org/fhir/datatypes.html#Coding) pattern.

It is **not** a first-class Beckn schema — it carries no `x-beckn-container`, no `profile.json`,
and no `renderer.json`. It does carry `context.jsonld` and `vocab.jsonld` so that its `code` and
`display` fields are properly mapped to IRIs when embedded in JSON-LD payloads.

## The triple

```yaml
"@context": "https://lgdirectory.gov.in"   # authority URI
"@type":    "LGDDistrict"                   # code class within the authority
code:       "507"                           # the code string
display:    "Nashik"                        # optional human-readable label (informational)
```

The `(@context, @type, code)` triple uniquely identifies a value within the authority's namespace.
The `display` field is informational only — never filter on it. Note that `@context` and `@type`
inside a CodedValue instance are JSON-LD keywords — they self-resolve and are not mapped in
`context.jsonld`.

## Attachment Points

Not attached to any Beckn container directly. Referenced via `$ref` as a property type within
other schemas' `attributes.yaml`. Always use the canonical absolute URL:

```
$ref: "https://schema.beckn.io/CodedValue/v2.1/attributes.yaml#/components/schemas/CodedValue"
```

## Design Rationale

- **External authority alignment** — CodedValue is used only when the code system is maintained
  by an authority outside the network (government directories, standards bodies, commodity
  classification agencies). For small, stable, network-owned value sets, a plain `enum` is
  preferred.
- **Machine filterability** — the `(@context, @type, code)` triple provides a globally unique,
  unambiguous key that discovery filters can match against precisely, without depending on
  human-readable labels.
- **FHIR Coding alignment** — the pattern mirrors FHIR's `Coding` datatype to maximise
  interoperability with health information systems already using authority-backed code systems.
- **JSON-LD compatibility** — `context.jsonld` maps `code` → `cv:code` and `display` → `cv:display`
  so that CodedValue instances are fully resolvable when embedded in JSON-LD payloads produced
  by parent schemas.

## Non-Goals

- Does not define or validate the code systems themselves — that is the responsibility of the
  named authority.
- Does not model composite or hierarchical codes — use multiple CodedValue fields or a structured
  sub-object for that.
- Does not replace `enum` for value sets owned by the schema.

## Current Consumers

| Schema | Field | Authority examples |
|---|---|---|
| `AgriServiceResource` (agri-services-ext) | `coverageAreaCodes` | LGD, KNBS, IEBC, India Post |
| `AgriCropAdvisoryResource` (agri-advisory-v21) | `cropTypes`, `coverageAreaCodes` | FAO crop codes, LGD |
| `AgriWeatherResource` (agri-advisory-v21) | `weatherParameters`, `coverageAreaCodes` | WMO, LGD |
| `AgriCommodityPriceResource` (agri-advisory-v21) | `commodities`, `marketCodes`, `coverageAreaCodes` | FAO, APMC, LGD |
| `AgriDigitalPerformance` (agri-services-ext) | `targetLocation` | LGD, KNBS |

## Upstream Candidates

`CodedValue` itself is a strong candidate for promotion into the Beckn Protocol core vocabulary
(alongside `Credential`, `Location`, etc.). Until that promotion occurs,
`generic-service/CodedValue/v2.1/attributes.yaml` is the canonical cross-pack reference point.
Extension packs must `$ref` this file directly rather than defining their own copy.

## Resolution & extension convention

How a `CodedValue` resolves to its valid `code` set, and how a network extends a value set without forking a schema, is specified in **the CodedValue resolution & extension convention (RFC-001, draft)**.
