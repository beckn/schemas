# CredentialRequirement — Shared Type

**Type:** Shared sub-schema (referenced by multiple top-level schemas)
**Protocol Version:** 2.1
**Semantic Model:** generalised
**Version:** 1.0.0
**Used By:** `HiringJobResourceAttributes`, `CourseResourceAttributes`

## Overview

`CredentialRequirement` represents a single credential requirement or prerequisite entry.
It is used wherever a Beckn participant specifies what a counterparty must hold in order
to be eligible — whether for a job application or a course enrollment.

The type follows a category + subtype pattern, where `category` is a broad credential class
(SKILL, DEGREE, LICENSE, etc.) and `subtype` is the specific credential within that class.
This mirrors the `verification_index` structure in DeDi registries, enabling direct mapping
between what is required and what is attested.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `category` | enum | Yes | Broad credential class |
| `subtype` | string | Yes | Specific credential name or code |
| `mandatory` | boolean | Yes | Whether failure blocks the transaction |

## Upstream Candidate

This type is generic enough to apply across hiring, skilling, healthcare credentialing,
driver licensing, financial compliance, and more. It is a strong candidate for promotion
into the Beckn v2.1 core schema as a reusable primitive.

## Non-Goals

- Does not carry the credential value or payload (that belongs in the wallet/DeDi layer)
- Does not specify the verification method (that belongs in `performanceAttributes`)
- Does not track verification outcome (that belongs in `VerificationSummary`)
