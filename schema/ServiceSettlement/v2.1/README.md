# ServiceSettlement — v2.1

**Schema Pack Version:** 2.1.0
**Released:** April 2026
**Status:** Initial release

## Notes

Initial release of the ServiceSettlement schema targeting the v2.1 generalised model. This schema records payment settlement details including whether the provider has received payment, when it was recorded, and the receipt reference. It also supports post-completion settlement adjustments for on-actuals reconciliation, partial delivery, and full refund scenarios.

### Container

- **Settlement.settlementAttributes**

### Key features

- Payment receipt confirmation (`paymentReceivedByProvider`)
- Payment recording timestamp (`paymentRecordedAt`)
- Receipt reference tracking (`receiptRef`)
- Settlement notes (`paymentNotes`)
- Post-completion adjustment type: NONE, ON_ACTUALS, PARTIAL, FULL_REFUND (`adjustmentType`)
- Adjustment amount, reason, and timestamp (`adjustmentAmount`, `adjustmentReason`, `adjustedAt`)
- Final settlement reference after all adjustments are applied (`finalSettlementRef`)
- Dispute/grievance reference linking to active or resolved disputes (`disputeRef`)
