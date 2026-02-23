# Changelog — Beckn Protocol Core Schema

All notable changes to the Beckn Protocol Core Schema are documented in this file.

This changelog follows the format: **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**. Change classifications (Patch / Minor / Major / Informative) are noted per entry, as defined in [GOVERNANCE.md § 5.1](./GOVERNANCE.md).

---

## [v2.0.0] — 2026-02-23

**Initial release of the Beckn Protocol Core Schema v2.0.**

This is the first versioned release of the core schema library, extracted and formalised from the Beckn Protocol v2.0 specification. The namespace for all schemas in this release is `https://schema.beckn.io/core/v2.0/`.

### Added

**New schemas (90 total):**

- `AcceptedPaymentMethod` — Enumeration of accepted payment methods for a transaction
- `Address` — Physical or postal address
- `Alert` — Notification or alert associated with an entity
- `Attributes` — Generic extensible attribute container
- `CancelAction` — Action object for cancellation requests
- `CancellationOutcome` — Result of a cancellation process
- `CancellationPolicy` — Policy governing cancellation terms
- `CancellationReason` — Reason for cancellation
- `Catalog` — Collection of items and offers provided by a provider
- `CatalogProcessingResult` — Result of catalog submission to a publishing service
- `CategoryCode` — Standardised category code
- `CheckoutTerminal` — Enumeration of checkout terminal types (BAP, BPP, POS, etc.)
- `ConfirmAction` — Action object for order confirmation
- `Constraint` — A constraint expression applied to an entity
- `Consumer` — The consumer participant in a transaction
- `Context` — The transaction context object carried in every API request
- `Contract` — A formalised agreement between buyer and provider (replaces `Order`)
- `ContractItem` — A line item within a Contract (replaces `OrderItem`)
- `Credential` — A verifiable credential or certificate
- `Descriptor` — Reusable descriptor for display text, images, and tags
- `DiscoverAction` — Action object for discovery requests
- `DisplayedRating` — Aggregated rating display object
- `Document` — A document or attachment associated with a transaction
- `Eligibility` — Eligibility criteria for an item or offer
- `Entitlement` — An entitlement granted by a provider
- `Error` — An error payload
- `ErrorResponse` — A full error response envelope
- `Feedback` — Feedback submitted by a participant
- `Form` — A form to be rendered at a checkout terminal
- `Fulfillment` — A fulfillment record associated with a contract
- `FulfillmentAgent` — The agent responsible for a fulfillment stage
- `FulfillmentMode` — The mode of fulfillment (delivery, pickup, etc.)
- `FulfillmentStage` — A stage within a multi-stage fulfillment
- `FulfillmentStageAuthorization` — Authorization required at a fulfillment stage
- `FulfillmentStageEndpoint` — Endpoint configuration for a fulfillment stage
- `GeoJSONGeometry` — A GeoJSON geometry object (Point, Polygon, etc.)
- `InitAction` — Action object for order initialisation
- `Instruction` — An instruction associated with a fulfillment or item
- `Intent` — The search intent expressed by a consumer
- `Invoice` — An invoice issued for a transaction
- `Item` — A product or service offered by a provider
- `Location` — A physical or virtual location
- `MediaFile` — A media file attachment
- `MediaInput` — Media input for visual/audio search
- `MediaSearch` — A media-based search request
- `MediaSearchOptions` — Options for a media search
- `Offer` — A promotional offer
- `OnCancelAction` — Callback action for cancellation
- `OnConfirmAction` — Callback action for confirmation
- `OnDiscoverAction` — Callback action for discovery
- `OnInitAction` — Callback action for initialisation
- `OnRateAction` — Callback action for rating
- `OnSelectAction` — Callback action for selection
- `OnStatusAction` — Callback action for status
- `OnSupportAction` — Callback action for support
- `OnTrackAction` — Callback action for tracking
- `OnUpdateAction` — Callback action for update
- `Organization` — An organisation entity
- `Participant` — A participant in the Beckn network
- `PaymentAction` — A payment action record
- `PaymentTerms` — Terms governing payment
- `PaymentTrigger` — The trigger condition for payment
- `Person` — A person entity
- `Policy` — A policy applied to a transaction or item
- `PriceSpecification` — A price breakdown specification
- `ProcessingNotice` — A notice issued during catalog or contract processing
- `Provider` — A provider of items and services
- `Quantity` — A quantity specification
- `RateAction` — Action object for rating requests
- `Rating` — A rating value
- `RatingForm` — A form for collecting ratings
- `RatingInput` — Input for a rating submission
- `RefundTerms` — Terms governing refunds
- `SelectAction` — Action object for item selection
- `SettlementSchedule` — A schedule for payment settlement
- `SettlementTerm` — A term within a settlement schedule
- `Skill` — A skill associated with a fulfillment agent
- `SpatialConstraint` — A spatial constraint using GeoJSON geometry
- `State` — A state descriptor for an entity
- `StatusAction` — Action object for status requests
- `SupportAction` — Action object for support requests
- `SupportInfo` — Support contact information
- `SupportRequest` — A support request
- `SupportTicket` — A support ticket
- `Time` — A time value
- `TimePeriod` — A time period with start and end
- `TrackAction` — Action object for tracking requests
- `Tracking` — A tracking record
- `TrackingRequest` — A tracking request
- `TransactionEndpoint` — An endpoint for a transaction participant
- `UpdateAction` — Action object for update requests

**Root JSON-LD artefacts:**
- `schema/context.jsonld` — Unified JSON-LD context for all core schemas; namespace `https://schema.beckn.io/core/v2.0/`; `@protected: true`
- `schema/vocab.jsonld` — RDF vocabulary for all core schemas

### Deprecated

The following terms are deprecated in v2.0 and replaced with new terms. Their IRIs are preserved in `schema/context.jsonld` as backward-compatible aliases.

| Deprecated term | Replacement | Notes |
|---|---|---|
| `Order` | `Contract` | IRI `beckn:Contract`; alias maintained |
| `OrderItem` | `ContractItem` | IRI `beckn:ContractItem`; alias maintained |
| `SupportInfo` | `Support` | IRI `beckn:Support`; alias maintained |
| `orderStatus` values | `contractStatus` values | Both enum sets map to the same IRIs |

---

*Older history (pre-v2.0) is documented in the [protocol-specifications-v2](https://github.com/beckn/protocol-specifications-v2) repository.*
