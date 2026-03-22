# HiringProcessPerformanceAttributes Schema

**Container:** `Performance.performanceAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Hiring pipeline tracking in employer-to-candidate talent marketplace
**Tag:** hiring candidates performance pipeline interview

## Overview

`HiringProcessPerformanceAttributes` extends the v2.1 `Performance` container with the
current state of the hiring pipeline — from initial screening through to offer acceptance
or withdrawal. Performance mode is `SERVICE`.

It supports credential verification triggered by the employer during the process (e.g. at
the interview or offer stage), reusing `VerificationSummary` from `hiring-common`.

## Non-Goals

- Does not store the employment contract terms (→ `EmployerHiringContractAttributes`)
- Does not store assessment scores or detailed interview notes (PII concern)
