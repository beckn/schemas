# EmployerHiringContractAttributes Schema

**Container:** `Contract.contractAttributes`
**Protocol Version:** 2.0
**Semantic Model:** generalised
**Version:** 1.0.0
**Use Cases:** Employer-to-candidate hiring offer in a talent marketplace
**Tag:** hiring candidates contract offer employer

## Overview

`EmployerHiringContractAttributes` extends the v2.1 `Contract` container with metadata
specific to an employer-initiated hiring offer. The employer discovers a candidate profile
(via `CandidateProfileResourceAttributes`) and extends a formal offer — this schema captures
the terms of that offer and the candidate's response state.

## Contract Structure

```
Contract {
  parties:     [ { role: "EMPLOYER" }, { role: "CANDIDATE" } ]
  commitments: [ { refType: "RESOURCE", ref: "<candidate-profile-id>" } ]
  performance: [ { mode: "SERVICE", performanceAttributes: {...} } ]
  contractAttributes: { role_title, offered_compensation, candidate_response, ... }
}
```

## Design Rationale

**Specific compensation, not a range.** Unlike the Offer (which carries the candidate's
desired range), the contract carries the specific amount offered by the employer. This is
the concrete hiring offer, not a market signal.

**Candidate response as a lifecycle field.** The `candidate_response` enum enables
negotiation tracking within the Beckn protocol layer — NEGOTIATING signals that a counter-
proposal is expected without requiring a new contract. This is important for use cases
where multiple negotiation rounds occur before ACCEPTED.

## Non-Goals

- Does not capture the employment contract itself (post-Beckn)
- Does not capture credential verification (→ `HiringProcessPerformanceAttributes`)
