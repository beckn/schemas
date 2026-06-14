# ServiceCoordinationOffer — v2.1

**Schema Pack Version:** 2.1.0
**Released:** June 2026
**Status:** under-review

## Notes

Offer-level terms for a coordination engagement. Extends `ServiceOffer/v2.1`.

### Container

- **Offer.offerAttributes**

### Key fields

- `coordinationSlaWindows` — per-urgency `lapseWindowHours` / `slaBreachWindowHours`
- `retryPolicy` — NOTIFY_ON_FIRST_REFUSAL / ONE_SILENT_RETRY (plain enum)
- `handoffSupported` — boolean (T1 transfer support)
- `maxActiveReferrals` — optional capacity signal
