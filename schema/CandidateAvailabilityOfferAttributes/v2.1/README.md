# CandidateAvailabilityOfferAttributes Schema

**Container:** `Offer.offerAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Candidate availability terms and compensation expectations in talent marketplace
**Tag:** hiring candidates offer availability compensation

## Overview

`CandidateAvailabilityOfferAttributes` extends the v2.1 `Offer` container with the
commercial and availability terms under which a candidate profile is offered to employers.
In this topology the candidate is the BPP; their Offer captures what they bring to the
engagement: when they are available, what notice period applies, and what compensation
they expect.

## Non-Goals

- Does not capture skills or profile metadata (→ `CandidateProfileResourceAttributes`)
- Does not capture the hiring contract outcome (→ `EmployerHiringContractAttributes`)
