# ReputationSummary

**Container:** inline sub-schema (shared utility type)
**Tag:** hiring hiring-common shared-type
**Pack:** hiring-common
**Use Cases:** Any hiring-domain network requiring reputation signals

Attestation-based reputation capsule shared across hiring-domain schemas:
- `HiringJobResource.operator_reputation` — organisation/operator reputation
- `CandidateProfileResource.reputation_summary` — candidate reputation

No PII. Safe to expose at discovery stage.
Upstream candidate for promotion to beckn core common types.
