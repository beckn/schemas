# Common Schema Directory

This directory contains the domain-agnostic core schema definitions for the Beckn Protocol v2.0.

Each schema is defined in three file formats — an OpenAPI 3.1 attribute definition, a JSON-LD context, and an RDF vocabulary — and versioned independently under a `v{MAJOR}.{MINOR}/` path.

For full documentation on the schema structure, file formats, and versioning rules, see [`docs/2_Schema_Structure.md`](../docs/2_Schema_Structure.md).

---

## Directory Structure

```
schema/
├── context.jsonld          ← Root JSON-LD context (all schemas, namespace: https://schema.beckn.io/core/v2.0/)
├── vocab.jsonld            ← Root RDF vocabulary (all schemas)
└── {SchemaName}/
    └── v2.0/
        ├── attributes.yaml ← OpenAPI 3.1.1 component definition
        ├── context.jsonld  ← Per-schema JSON-LD context
        └── vocab.jsonld    ← Per-schema RDF vocabulary
```

---

## Schemas Available (91 total, v2.0)

| Schema | Description |
|---|---|
| [AcceptedPaymentMethod](./AcceptedPaymentMethod/v2.0/) | Enumeration of accepted payment methods for a transaction |
| [Address](./Address/v2.0/) | Physical or postal address |
| [Alert](./Alert/v2.0/) | Notification or alert associated with an entity |
| [Attributes](./Attributes/v2.0/) | Generic extensible attribute container |
| [CancelAction](./CancelAction/v2.0/) | Action object for cancellation requests |
| [CancellationOutcome](./CancellationOutcome/v2.0/) | Result of a cancellation process |
| [CancellationPolicy](./CancellationPolicy/v2.0/) | Policy governing cancellation terms |
| [CancellationReason](./CancellationReason/v2.0/) | Reason for a cancellation |
| [Catalog](./Catalog/v2.0/) | Collection of items and offers provided by a provider |
| [CatalogProcessingResult](./CatalogProcessingResult/v2.0/) | Result of catalog submission to a publishing service |
| [CategoryCode](./CategoryCode/v2.0/) | Standardised category code |
| [CheckoutTerminal](./CheckoutTerminal/v2.0/) | Enumeration of checkout terminal types (BAP, BPP, POS, etc.) |
| [ConfirmAction](./ConfirmAction/v2.0/) | Action object for order confirmation |
| [Constraint](./Constraint/v2.0/) | A constraint expression applied to an entity |
| [Consumer](./Consumer/v2.0/) | The consumer participant in a transaction |
| [Context](./Context/v2.0/) | The transaction context object carried in every API request |
| [Contract](./Contract/v2.0/) | A formalised agreement between consumer and provider |
| [ContractItem](./ContractItem/v2.0/) | A line item within a Contract |
| [Credential](./Credential/v2.0/) | A verifiable credential or certificate |
| [Descriptor](./Descriptor/v2.0/) | Reusable descriptor for display text, images, and tags |
| [DiscoverAction](./DiscoverAction/v2.0/) | Action object for discovery requests |
| [DisplayedRating](./DisplayedRating/v2.0/) | Aggregated rating display object |
| [Document](./Document/v2.0/) | A document or attachment associated with a transaction |
| [Eligibility](./Eligibility/v2.0/) | Eligibility criteria for an item or offer |
| [Entitlement](./Entitlement/v2.0/) | An entitlement granted by a provider |
| [Error](./Error/v2.0/) | An error payload |
| [ErrorResponse](./ErrorResponse/v2.0/) | A full error response envelope |
| [Feedback](./Feedback/v2.0/) | Feedback submitted by a participant |
| [Form](./Form/v2.0/) | A form to be rendered at a checkout terminal |
| [Fulfillment](./Fulfillment/v2.0/) | A fulfillment record associated with a contract |
| [FulfillmentAgent](./FulfillmentAgent/v2.0/) | The agent responsible for a fulfillment stage |
| [FulfillmentMode](./FulfillmentMode/v2.0/) | The mode of fulfillment (delivery, pickup, etc.) |
| [FulfillmentStage](./FulfillmentStage/v2.0/) | A stage within a multi-stage fulfillment |
| [FulfillmentStageAuthorization](./FulfillmentStageAuthorization/v2.0/) | Authorization required at a fulfillment stage |
| [FulfillmentStageEndpoint](./FulfillmentStageEndpoint/v2.0/) | Endpoint configuration for a fulfillment stage |
| [GeoJSONGeometry](./GeoJSONGeometry/v2.0/) | A GeoJSON geometry object (Point, Polygon, etc.) |
| [InitAction](./InitAction/v2.0/) | Action object for order initialisation |
| [Instruction](./Instruction/v2.0/) | An instruction associated with a fulfillment or item |
| [Intent](./Intent/v2.0/) | The search intent expressed by a consumer |
| [Invoice](./Invoice/v2.0/) | An invoice issued for a transaction |
| [Item](./Item/v2.0/) | A product or service offered by a provider |
| [Location](./Location/v2.0/) | A physical or virtual location |
| [MediaFile](./MediaFile/v2.0/) | A media file attachment |
| [MediaInput](./MediaInput/v2.0/) | Media input for visual or audio search |
| [MediaSearch](./MediaSearch/v2.0/) | A media-based search request |
| [MediaSearchOptions](./MediaSearchOptions/v2.0/) | Options for a media search |
| [Offer](./Offer/v2.0/) | A promotional offer |
| [OnCancelAction](./OnCancelAction/v2.0/) | Callback action for cancellation |
| [OnConfirmAction](./OnConfirmAction/v2.0/) | Callback action for confirmation |
| [OnDiscoverAction](./OnDiscoverAction/v2.0/) | Callback action for discovery |
| [OnInitAction](./OnInitAction/v2.0/) | Callback action for initialisation |
| [OnRateAction](./OnRateAction/v2.0/) | Callback action for rating |
| [OnSelectAction](./OnSelectAction/v2.0/) | Callback action for selection |
| [OnStatusAction](./OnStatusAction/v2.0/) | Callback action for status |
| [OnSupportAction](./OnSupportAction/v2.0/) | Callback action for support |
| [OnTrackAction](./OnTrackAction/v2.0/) | Callback action for tracking |
| [OnUpdateAction](./OnUpdateAction/v2.0/) | Callback action for update |
| [Organization](./Organization/v2.0/) | An organisation entity |
| [Participant](./Participant/v2.0/) | A participant in the Beckn network |
| [PaymentAction](./PaymentAction/v2.0/) | A payment action record |
| [PaymentTerms](./PaymentTerms/v2.0/) | Terms governing payment |
| [PaymentTrigger](./PaymentTrigger/v2.0/) | The trigger condition for payment |
| [Person](./Person/v2.0/) | A person entity |
| [Policy](./Policy/v2.0/) | A policy applied to a transaction or item |
| [PriceSpecification](./PriceSpecification/v2.0/) | A price breakdown specification |
| [ProcessingNotice](./ProcessingNotice/v2.0/) | A notice issued during catalog or contract processing |
| [Provider](./Provider/v2.0/) | A provider of items and services |
| [Quantity](./Quantity/v2.0/) | A quantity specification |
| [RateAction](./RateAction/v2.0/) | Action object for rating requests |
| [Rating](./Rating/v2.0/) | A rating value |
| [RatingForm](./RatingForm/v2.0/) | A form for collecting ratings |
| [RatingInput](./RatingInput/v2.0/) | Input for a rating submission |
| [RefundTerms](./RefundTerms/v2.0/) | Terms governing refunds |
| [SelectAction](./SelectAction/v2.0/) | Action object for item selection |
| [SettlementSchedule](./SettlementSchedule/v2.0/) | A schedule for payment settlement |
| [SettlementTerm](./SettlementTerm/v2.0/) | A term within a settlement schedule |
| [Skill](./Skill/v2.0/) | A skill associated with a fulfillment agent |
| [SpatialConstraint](./SpatialConstraint/v2.0/) | A spatial constraint using GeoJSON geometry |
| [State](./State/v2.0/) | A state descriptor for an entity |
| [StatusAction](./StatusAction/v2.0/) | Action object for status requests |
| [SupportAction](./SupportAction/v2.0/) | Action object for support requests |
| [SupportInfo](./SupportInfo/v2.0/) | Support contact information _(deprecated — use `Support`)_ |
| [SupportRequest](./SupportRequest/v2.0/) | A support request raised by a participant |
| [SupportTicket](./SupportTicket/v2.0/) | A support ticket |
| [Time](./Time/v2.0/) | A time value |
| [TimePeriod](./TimePeriod/v2.0/) | A time period with start and end |
| [TrackAction](./TrackAction/v2.0/) | Action object for tracking requests |
| [Tracking](./Tracking/v2.0/) | A tracking record |
| [TrackingRequest](./TrackingRequest/v2.0/) | A tracking request |
| [TransactionEndpoint](./TransactionEndpoint/v2.0/) | An endpoint for a transaction participant |
| [UpdateAction](./UpdateAction/v2.0/) | Action object for update requests |

---

## Deprecated Term Aliases (v2.0)

The following terms are deprecated. They remain in `context.jsonld` as backward-compatible IRI aliases and their directories are retained, but new implementations SHOULD use the replacement terms.

| Deprecated term | Replacement | Notes |
|---|---|---|
| `Order` | `Contract` | IRI `beckn:Contract`; alias preserved in root context |
| `OrderItem` | `ContractItem` | IRI `beckn:ContractItem`; alias preserved in root context |
| `SupportInfo` | `Support` | IRI `beckn:Support`; alias preserved in root context |

---

## Version History

- **v2.0** — Initial release. 91 schemas extracted and formalised from Beckn Protocol v2.0. See [`../CHANGELOG.md`](../CHANGELOG.md) for the full change log.
