# VerificationSummary — Shared Type

**Type:** Shared sub-schema
**Protocol Version:** 2.1
**Semantic Model:** generalised
**Version:** 1.0.0
**Used By:** `JobApplicationContractAttributes`, `HiringProcessPerformanceAttributes`, `CourseEnrollmentContractAttributes`

## Overview

`VerificationSummary` is the outcome record of a credential verification check. It is
designed to be shared across hiring-jobs, hiring-candidates, and skilling packs — and is
general enough to apply to any Beckn domain that requires credential gating.

## Privacy Principles

- No VC payloads are included
- No VP payloads are included
- No PII is included
- `proof_metadata_hash` provides integrity reference only

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `overall_result` | enum | Yes | PASS / FAIL / PARTIAL / PENDING |
| `reason_codes` | array of string | No | Failure reason codes |
| `verified_categories` | array of string | No | Successfully verified credential classes |
| `verified_subtypes` | array of string | No | Successfully verified specific credentials |
| `checked_at` | date-time | Yes | Verification timestamp |
| `proof_metadata_hash` | string | No | Hash of VP used (integrity only) |

## Upstream Candidate

Verification summary is domain-agnostic — relevant to healthcare (license verification),
financial services (KYC), logistics (driver license), and more. Strong upstream candidate.
