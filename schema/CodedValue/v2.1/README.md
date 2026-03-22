# CodedValue — Shared Type

**Type:** Shared sub-schema
**Protocol Version:** 2.1
**Semantic Model:** generalised
**Version:** 1.0.0
**Used By:** `HiringJobResourceAttributes`, `CourseResourceAttributes`, `CandidateProfileResourceAttributes`

## Overview

`CodedValue` is the standard pattern for any field whose valid values are defined by an
external authority (government classification systems, standards bodies, industry registries).
Using `CodedValue` instead of a hardcoded enum provides international neutrality — any
country's classification system can be expressed without a schema change.

## Example Uses

| Field | Context URI | Type | Code Example |
|-------|-------------|------|--------------|
| `industry_type` | ISIC URI | IndustryCode | "8299" |
| `course_domain` | ISCED URI | FieldOfEducationCode | "0613" |
| `qualification_level` | NSQF URI | QualificationLevel | "4" |

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `@context` | uri | Yes | Code system authority URI |
| `@type` | string | Yes | Code class within the system |
| `code` | string | Yes | The actual code value |
| `label` | string | No | Human-readable display label |
