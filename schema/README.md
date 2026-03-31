# Common Schema Directory

Generated index of schema folders and latest descriptions.

| Schema | Latest Version | Description |
|---|---|---|
| [AcceptedPaymentMethod](https://schema.beckn.io/AcceptedPaymentMethod/README.md) | v2.0 | Payment methods accepted by a payee |
| [Ack](https://schema.beckn.io/Ack/README.md) | v2.0 | Synchronous receipt acknowledgement returned for every accepted Beckn request.
Supports both the v2.0 format (status + signature CounterSignature) and the
v2.0-rc1 legacy format (ack_status + transaction_id + timestamp) via oneOf
for backward compatibility. |
| [AckNoCallback](https://schema.beckn.io/AckNoCallback/README.md) | v2.0 | Request received but no callback will follow (e.g. agents not found, inventory unavailable, provider closed, context.try preview complete).

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [AckResponse](https://schema.beckn.io/AckResponse/README.md) | v2.0 | Schema definition for AckResponse in the Beckn Protocol |
| [AddOn](https://schema.beckn.io/AddOn/README.md) | v2.0 | Add-on to a catalog resource

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Address](https://schema.beckn.io/Address/README.md) | v2.0 | **Postal address** aligned with schema.org `PostalAddress`. Use for human-readable addresses. Geometry lives in `Location.geo` as GeoJSON. |
| [AffectedLine](https://schema.beckn.io/AffectedLine/README.md) | v2.0 | Attributes for the AffectedLine entity in the Beckn Mobility domain. |
| [Alert](https://schema.beckn.io/Alert/README.md) | v2.0 | Schema definition for Alert in the Beckn Protocol v2.0.1 |
| [AncillaryService](https://schema.beckn.io/AncillaryService/README.md) | v2.0 | Attributes for the AncillaryService entity in the Beckn Mobility domain. |
| [Asset](https://schema.beckn.io/Asset/README.md) | v2.0 | Attributes for the Asset entity in the Beckn Mobility domain. |
| [AsyncError](https://schema.beckn.io/AsyncError/README.md) | v2.0 | Error returned asynchronously during a callback. Wraps the base `Error` schema with JSON-LD type annotations to allow linked-data processing.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Attributes](https://schema.beckn.io/Attributes/README.md) | v2.0 | JSON-LD aware container for domain-specific attributes of an Item. MUST include @context (URI) and @type (compact or full IRI). Any additional properties are allowed and interpreted per the provided JSON-LD context. |
| [Authority](https://schema.beckn.io/Authority/README.md) | v2.0 | Attributes for the Authority entity in the Beckn Mobility domain. |
| [BaggageAllowance](https://schema.beckn.io/BaggageAllowance/README.md) | v2.0 | Attributes for the BaggageAllowance entity in the Beckn Mobility domain. |
| [BecknAction](https://schema.beckn.io/BecknAction/README.md) | v2.0 | Unified Beckn action envelope. All Beckn API requests and callbacks conform to this schema. The context identifies the action being performed; the message carries the action-specific payload. Message content is validated via if/then dispatch based on context.action. For unknown or extension endpoints, no if/then branch applies and message remains unconstrained.
This schema supersedes RequestAction and CallbackAction, both of which were structurally invalid. The request/callback distinction is encoded in the context.action value (e.g. beckn/discover vs beckn/on_discover), not in a separate schema type. |
| [BecknEndpoint](https://schema.beckn.io/BecknEndpoint/README.md) | v2.0 | A Beckn protocol endpoint identifier. Must start with the prefix "beckn/" followed by one or more lowercase segments (letters and underscores only) separated by forward slashes. Standard endpoints are listed in the oneOf below with their descriptions. New actors may define extension endpoints without modifying this schema — the pattern accepts any conforming beckn/ prefixed string. |
| [BikeAllowed](https://schema.beckn.io/BikeAllowed/README.md) | v2.0 | Attributes for the BikeAllowed entity in the Beckn Mobility domain. |
| [BookingRule](https://schema.beckn.io/BookingRule/README.md) | v2.0 | Attributes for the BookingRule entity in the Beckn Mobility domain. |
| [Buyer](https://schema.beckn.io/Buyer/README.md) | v2.0 | Schema definition for Buyer in the Beckn Protocol |
| [CallbackAction](https://schema.beckn.io/CallbackAction/README.md) | v2.0 | DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. The $id also lacked a version segment.
Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). Callback actions are those with on_ prefixed endpoints (e.g. beckn/on_discover, beckn/on_confirm) and are validated by the same BecknAction schema via if/then dispatch on context.action.
This schema will be removed in a future major version. |
| [CancelAction](https://schema.beckn.io/CancelAction/README.md) | v2.0 | Beckn /beckn/cancel action envelope. Sent by a BAP to a BPP to request cancellation of an active contract. Set context.try to true to first retrieve cancellation terms and fees before committing. |
| [CancellationOutcome](https://schema.beckn.io/CancellationOutcome/README.md) | v2.0 | Schema definition for CancellationOutcome in the Beckn Protocol v2.0.1 |
| [CancellationPolicy](https://schema.beckn.io/CancellationPolicy/README.md) | v2.0 | Schema definition for CancellationPolicy in the Beckn Protocol v2.0.1 |
| [CancellationReason](https://schema.beckn.io/CancellationReason/README.md) | v2.0 | Schema definition for CancellationReason in the Beckn Protocol v2.0.1 |
| [CandidateAvailabilityOfferAttributes](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/README.md) | v2.1 | Availability and compensation expectation terms under which a candidate profile is offered to employers. The proposedConsideration on the core Offer carries the candidate's headline desired salary; this extension provides the full range, notice period, and contract type preferences. |
| [CandidateProfileResourceAttributes](https://schema.beckn.io/CandidateProfileResourceAttributes/README.md) | v2.1 | Discoverable profile attributes of a candidate Resource. Captures what the candidate brings (skills, experience, availability) and what they seek (location preference, work mode, job type). Designed for privacy: no name, contact, or identity data. Credentials are referenced via SkillEntry with optional VC attestation URLs. |
| [Carrier](https://schema.beckn.io/Carrier/README.md) | v2.0 | A Carrier is a transport service provider responsible for moving goods across distances. Carriers operate fleets of vehicles and may own/manage logistics hubs. Maps to beckn:Provider. |
| [Catalog](https://schema.beckn.io/Catalog/README.md) | v2.1 | Catalog schema for Beckn Protocol v2.0.0

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CatalogOnPublishAction](https://schema.beckn.io/CatalogOnPublishAction/README.md) | v2.0 | Catalog publish processing results from CDS to BPP.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CatalogProcessingResult](https://schema.beckn.io/CatalogProcessingResult/README.md) | v2.0 | Schema definition for CatalogProcessingResult in the Beckn Protocol v2.1 |
| [CatalogPublishAction](https://schema.beckn.io/CatalogPublishAction/README.md) | v2.0 | Beckn /beckn/catalog_publish message payload. Sent by a BPP to a CDS
(Catalog Discovery Service) to publish or update one or more catalogs.
The CDS indexes the catalogs and makes them discoverable. |
| [CatalogPublishResponse](https://schema.beckn.io/CatalogPublishResponse/README.md) | v2.0 | Beckn /beckn/on_catalog_publish message payload. Sent by a CDS back to a BPP
after processing a catalog publish request. Contains per-catalog processing results
indicating success, failure, or partial indexing. |
| [CatalogPullAction](https://schema.beckn.io/CatalogPullAction/README.md) | v2.0 | Message payload for catalog/pull

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CatalogSubscribeAction](https://schema.beckn.io/CatalogSubscribeAction/README.md) | v2.0 | Message payload for catalog/subscription.
At least one of `networkIds` or `schemaTypes` must be non-empty.
An empty `schemaTypes` array is treated as the wildcard sentinel `"*"`,
matching all schema types for the specified networks.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CatalogSubscription](https://schema.beckn.io/CatalogSubscription/README.md) | v2.0 | Full subscription record

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CategoryCode](https://schema.beckn.io/CategoryCode/README.md) | v2.1 | Schema definition for CategoryCode in the Beckn Protocol v2.0.1 |
| [CheckoutTerminal](https://schema.beckn.io/CheckoutTerminal/README.md) | v2.0 | The checkout terminal where the consumer makes the payment |
| [CodedValue](https://schema.beckn.io/CodedValue/README.md) | v2.1 | An authority-governed code value. The @context URI identifies the code system authority (e.g. UN ISIC, UNESCO ISCED, India NSQF). The @type identifies the class of code within that system. The code is the actual value. This pattern avoids hardcoding country-specific enumerations into the schema. |
| [Commitment](https://schema.beckn.io/Commitment/README.md) | v2.0 | This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [ConfirmAction](https://schema.beckn.io/ConfirmAction/README.md) | v2.0 | Beckn /beckn/confirm action envelope. Sent by a BAP to a BPP to confirm a contract, finalising the transaction terms agreed during the select–init negotiation cycle. |
| [Consideration](https://schema.beckn.io/Consideration/README.md) | v2.0 | Generalized representation of value exchanged under a Contract.

Consideration is domain-neutral and may represent:
- Monetary value
- Credits / tokens
- Asset transfer
- Service exchange
- Compliance artifact

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Consignment](https://schema.beckn.io/Consignment/README.md) | v2.0 | A Consignment is a collection of packages or shipments grouped together under a single commercial transaction between a shipper and consignee. Maps to beckn:Order. |
| [Constraint](https://schema.beckn.io/Constraint/README.md) | v2.0 | Schema definition for Constraint in the Beckn Protocol v2.0.1 |
| [Consumer](https://schema.beckn.io/Consumer/README.md) | v2.0 | Schema definition for Consumer in the Beckn Protocol v2.0.1 |
| [Contact](https://schema.beckn.io/Contact/README.md) | v2.0 | Contact information for sender, receiver, driver, or operator. |
| [ContactHandle](https://schema.beckn.io/ContactHandle/README.md) | v2.0 | Attributes for the ContactHandle entity in the Beckn Mobility domain. |
| [Context](https://schema.beckn.io/Context/README.md) | v2.0 | Every API call in Beckn protocol has a context. It provides a high-level overview to the receiver about the nature of the intended transaction. Typically, it is the BAP that sets the transaction context based on the consumer's location and action on their UI. The context object contains four types of fields: (1) demographic information about the transaction using fields like domain, country, and region; (2) addressing details like the sending and receiving platform's ID and API URL; (3) interoperability information like the protocol version implemented by the sender; and (4) transaction details like the method being called at the receiver's endpoint, the transaction_id that represents an end-to-end user session at the BAP, a message ID to pair requests with callbacks, a timestamp to capture sending times, a ttl to specify the validity of the request, and a key to encrypt information if necessary. |
| [Contract](https://schema.beckn.io/Contract/README.md) | v2.0 | This is a JSON-LD compliant, linked-data schema that specifies a generic multi-party, digitally signed Contract between a set of participants. based on the vocabulary defined in the @context. By default, it is the most generic form of contract i.e beckn:Contract. However, based on the mapping being used in @context, it could take values like retail:Order, mobility:Reservation, healthcare:Appointment, and so on, which will be defined as sub-classes of beckn:Contract. |
| [ContractItem](https://schema.beckn.io/ContractItem/README.md) | v2.0 | A line item within a Contract, linking an accepted Offer and ordered Item with quantity and price. |
| [CounterSignature](https://schema.beckn.io/CounterSignature/README.md) | v2.0 | A signed receipt transmitted in the synchronous `Ack` response body, proving that the
receiver authenticated, received, and processed the inbound request.

`CounterSignature` shares the same wire format as `Signature` but differs:
- **Signer**: the response receiver (not the request sender)
- **Location**: transmitted in the `Ack` response body (not in the `Authorization` header)
- **`digest`**: covers the Ack response body (not the inbound request body)
- **`(request-digest)`** and **`(message-id)`** MUST be included in the signing string

Signing string format:
```
(created): {unixTimestamp}
(expires): {unixTimestamp}
digest: BLAKE-512={base64DigestOfAckBody}
(request-digest): BLAKE-512={base64DigestOfInboundRequestBody}
(message-id): {messageId}
``` |
| [Courier](https://schema.beckn.io/Courier/README.md) | v2.0 | A Courier is an individual delivery agent responsible for last-mile pickup and delivery of packages, typically in hyperlocal or urban delivery contexts. Maps to beckn:Agent. |
| [CourseConsiderationAttributes](https://schema.beckn.io/CourseConsiderationAttributes/README.md) | v2.1 | Beckn v2.1 extension schema for the considerationAttributes container. Captures value-exchange specifics for a course enrollment — fee category, payment schedule, installment count, subsidy source, and refund policy. Used when course pricing_type is FULL_FEE, SUBSIDIZED, or SCHOLARSHIP. |
| [CourseDeliveryPerformanceAttributes](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/README.md) | v2.1 | Beckn v2.1 extension schema for the performanceAttributes container. Captures course delivery execution details: delivery URL (for ACCESS mode), session schedule (for SERVICE mode), attendance tracking, completion criteria, completion status, and issued credential reference. |
| [CourseEnrollmentContractAttributes](https://schema.beckn.io/CourseEnrollmentContractAttributes/README.md) | v2.1 | Beckn v2.1 extension schema for the contractAttributes container. Represents the transaction-level state of a course enrollment: enrollment reference, cohort assignment, prerequisite verification outcome, and credential issuance tracking. Parties: SKILL_SEEKER and SKILL_PROVIDER. |
| [CourseOfferAttributes](https://schema.beckn.io/CourseOfferAttributes/README.md) | v2.1 | Commercial and availability terms under which a course is offered. The proposedConsideration on the core Offer carries the headline fee; this extension provides pricing type context and enrollment window. |
| [CourseResourceAttributes](https://schema.beckn.io/CourseResourceAttributes/README.md) | v2.1 | Intrinsic attributes of a training course or program Resource. Domain-generic: applicable to any skilling vertical — vocational training, professional certification, higher education, government skill schemes, etc. |
| [Credential](https://schema.beckn.io/Credential/README.md) | v2.0 | A credential artifact that is either (a) a W3C Verifiable Credential (opaque JSON object) or (b) a document attachment reference requiring manual/offline verification. |
| [CredentialRequirement](https://schema.beckn.io/CredentialRequirement/README.md) | v2.1 | A single credential requirement or prerequisite. Specifies what a candidate or enrollee must hold. Category is a broad class; subtype is the specific credential within that class. |
| [DayType](https://schema.beckn.io/DayType/README.md) | v2.0 | Attributes for the DayType entity in the Beckn Mobility domain. |
| [DeliveryPolicy](https://schema.beckn.io/DeliveryPolicy/README.md) | v2.0 | Callback delivery retry configuration

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [DeliverySlot](https://schema.beckn.io/DeliverySlot/README.md) | v2.0 | A DeliverySlot is a time window offered or agreed upon for delivery of a shipment. Maps to beckn:TimeSlot. |
| [DepartureMessage](https://schema.beckn.io/DepartureMessage/README.md) | v2.0 | Attributes for the DepartureMessage entity in the Beckn Mobility domain. |
| [Descriptor](https://schema.beckn.io/Descriptor/README.md) | v2.1 | Schema definition for Descriptor in the Beckn Protocol v2.0.1

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Direction](https://schema.beckn.io/Direction/README.md) | v2.0 | Attributes for the Direction entity in the Beckn Mobility domain. |
| [DiscoverAction](https://schema.beckn.io/DiscoverAction/README.md) | v2.0 | Beckn /beckn/discover action envelope. Sent by a BAP to a BPP (or registry) to discover catalogs matching a given intent. |
| [DisplayedRating](https://schema.beckn.io/DisplayedRating/README.md) | v2.0 | Schema definition for DisplayedRating in the Beckn Protocol v2.0.1 |
| [DistributionChannel](https://schema.beckn.io/DistributionChannel/README.md) | v2.0 | Attributes for the DistributionChannel entity in the Beckn Mobility domain. |
| [Document](https://schema.beckn.io/Document/README.md) | v2.0 | A document, that can be parsed, printed, download or displayed. This has intentionally been kept separate from MediaFile as they may contain additional attributes like signature, schema etc. |
| [Driver](https://schema.beckn.io/Driver/README.md) | v2.0 | Attributes for the Driver entity in the Beckn Mobility domain. |
| [DropPolicy](https://schema.beckn.io/DropPolicy/README.md) | v2.0 | Attributes for the DropPolicy entity in the Beckn Mobility domain. |
| [Eligibility](https://schema.beckn.io/Eligibility/README.md) | v2.0 | Schema definition for Eligibility in the Beckn Protocol v2.0.1 |
| [EmergencyEvent](https://schema.beckn.io/EmergencyEvent/README.md) | v2.0 | Attributes for the EmergencyEvent entity in the Beckn Mobility domain. |
| [EmployerHiringContractAttributes](https://schema.beckn.io/EmployerHiringContractAttributes/README.md) | v2.1 | Contract-level metadata for an employer-to-candidate hiring offer. Captures the specific role details being offered, compensation amount (as distinct from the candidate's desired range), proposed joining date, offer expiry, and candidate response state. |
| [Entitlement](https://schema.beckn.io/Entitlement/README.md) | v2.0 | A contractually granted, policy-governed right that allows a specific party to access, use, or claim a defined economic resource within stated scope and validity constraints. It represents the enforceable permission created by an order, independent of the credential used to exercise it. |
| [EntitySelector](https://schema.beckn.io/EntitySelector/README.md) | v2.0 | Attributes for the EntitySelector entity in the Beckn Mobility domain. |
| [Error](https://schema.beckn.io/Error/README.md) | v2.0 | Schema definition for Error in the Beckn Protocol v2.0.1 |
| [ErrorResponse](https://schema.beckn.io/ErrorResponse/README.md) | v2.0 | Schema definition for ErrorResponse in the Beckn Protocol v2.0.1 |
| [EstimatedTimetableDelivery](https://schema.beckn.io/EstimatedTimetableDelivery/README.md) | v2.0 | Attributes for the EstimatedTimetableDelivery entity in the Beckn Mobility domain. |
| [Event](https://schema.beckn.io/Event/README.md) | v2.0 | Attributes for the Event entity in the Beckn Mobility domain. |
| [ExchangePoints](https://schema.beckn.io/ExchangePoints/README.md) | v2.0 | Attributes for the ExchangePoints entity in the Beckn Mobility domain. |
| [Fare](https://schema.beckn.io/Fare/README.md) | v2.0 | Attributes for the Fare entity in the Beckn Mobility domain. |
| [FareBreakup](https://schema.beckn.io/FareBreakup/README.md) | v2.0 | Attributes for the FareBreakup entity in the Beckn Mobility domain. |
| [FareComponent](https://schema.beckn.io/FareComponent/README.md) | v2.0 | Attributes for the FareComponent entity in the Beckn Mobility domain. |
| [FareEstimate](https://schema.beckn.io/FareEstimate/README.md) | v2.0 | Attributes for the FareEstimate entity in the Beckn Mobility domain. |
| [FareLegRule](https://schema.beckn.io/FareLegRule/README.md) | v2.0 | Attributes for the FareLegRule entity in the Beckn Mobility domain. |
| [FareMedium](https://schema.beckn.io/FareMedium/README.md) | v2.0 | Attributes for the FareMedium entity in the Beckn Mobility domain. |
| [FareProduct](https://schema.beckn.io/FareProduct/README.md) | v2.0 | Attributes for the FareProduct entity in the Beckn Mobility domain. |
| [FareResult](https://schema.beckn.io/FareResult/README.md) | v2.0 | Attributes for the FareResult entity in the Beckn Mobility domain. |
| [FareTransferRule](https://schema.beckn.io/FareTransferRule/README.md) | v2.0 | Attributes for the FareTransferRule entity in the Beckn Mobility domain. |
| [Feed](https://schema.beckn.io/Feed/README.md) | v2.0 | Attributes for the Feed entity in the Beckn Mobility domain. |
| [Feedback](https://schema.beckn.io/Feedback/README.md) | v2.0 | Feedback collected from a user (consumer, provider, or fulfillment agent) |
| [FlightSegment](https://schema.beckn.io/FlightSegment/README.md) | v2.0 | Attributes for the FlightSegment entity in the Beckn Mobility domain. |
| [FnBItem](https://schema.beckn.io/FnBItem/README.md) | v2.1 | A Beckn schema for a food and beverage item in retail F&B ordering.

FnBItem v2.1 extends beckn:RetailItem with comprehensive food-specific
attributes covering classification, allergens, additives, nutritional information,
cuisine, and preparation guidance.

Inheritance: beckn:RetailItem ← beckn:FnBItem
Use in: beckn:Commitment.commitmentAttributes for F&B orders |
| [FnBOffer](https://schema.beckn.io/FnBOffer/README.md) | v2.0 | A Beckn schema for food and beverage offer attributes.

FnBOffer extends beckn:RetailCoreOfferAttributes with F&B-specific offer
customization groups — the structured mechanism by which a food item's
configurable options (size, crust, toppings, add-ons) are declared and
priced within an offer.

A CustomizationGroup represents one dimension of configurability (e.g.
pizza size, crust type, topping selection). Each group has one or more
options with optional price deltas.

Inheritance: beckn:RetailCoreOfferAttributes ← beckn:FnBOffer
Use in: beckn:Offer.offerAttributes for F&B catalog items |
| [FnBPriceSpecification](https://schema.beckn.io/FnBPriceSpecification/README.md) | v2.0 | A price specification for food and beverage (F&B) delivery orders.

FnBPriceSpecification specializes beckn:PriceSpecification for the specific price
calculation structure of a food ordering and delivery transaction. It is derived
from extensive research into how food delivery platforms (Domino's, Zomato, Swiggy,
UberEats) model itemised bills, including:

- Size-dependent item and topping pricing (a topping on a Regular pizza costs less
  than on a Large pizza; add-on price = f(size, topping_type))
- Crust upcharges (premium crusts like Cheese Burst or Pan cost more)
- Combo discount mechanics (bundle savings expressed as negative values)
- Delivery and packaging fees distinct from item charges
- Platform convenience charges

**Component type codes:**

Item-level charges (may appear multiple times — once per line item):
- BASE_ITEM         — Base price of a food or beverage item at its selected size
- SIZE_UPCHARGE     — Premium for selecting a larger size over the base size (e.g. Regular → Medium)
- TOPPING           — Individual topping or ingredient add-on; price varies by item size
- ADDON             — Optional add-on item (dip, sauce, condiment packet)
- CUSTOMIZATION     — Surcharge for a special preparation request
- SIDE              — A side dish added to the order

Combo and offer adjustments (typically negative):
- COMBO_SAVINGS     — Discount from applying a bundle/meal combo deal (negative)
- COMBO_UPCHARGE    — Premium for upgrading within a combo (e.g. regular to medium pizza)
- OFFER_DISCOUNT    — Time-limited promotional discount applied at order level (negative)
- COUPON_DISCOUNT   — Discount from a promo/coupon code (negative)
- LOYALTY_DISCOUNT  — Discount from loyalty points redemption (negative)

Order-level charges:
- DELIVERY_FEE      — Delivery charge (flat, distance-based, or surge-adjusted)
- PACKAGING_FEE     — Restaurant packaging charge (boxes, insulated bags, eco-packaging)
- SMALL_ORDER_FEE   — Surcharge applied when order value is below the minimum
- PLATFORM_FEE      — App/platform convenience service charge

Gratuity:
- TIP               — Customer gratuity (added voluntarily by the consumer)

Notes:
- Tax components (GST, VAT, etc.) are jurisdiction-specific and MUST be modelled
  using PriceSpecificationComponent variants, not as codes in this schema.
- For TOPPING components, referenceItemId SHOULD be set to the ID of the base
  item to which the topping belongs, since topping price varies by item size.
- Negative values MUST be used for COMBO_SAVINGS, OFFER_DISCOUNT, COUPON_DISCOUNT,
  and LOYALTY_DISCOUNT.

Inheritance: beckn:PriceSpecification ← beckn:FnBPriceSpecification
schema.org alignment: schema:PriceSpecification (via inheritance)
Use in: beckn:Consideration.considerationAttributes for F&B orders |
| [FoodAndBeverageItem](https://schema.beckn.io/FoodAndBeverageItem/README.md) | v2.1 | A Beckn schema for a food and beverage item in retail F&B ordering.

FoodAndBeverageItem v2.1 extends beckn:RetailItem with comprehensive food-specific
attributes covering classification, allergens, additives, nutritional information,
cuisine, and preparation guidance.

Inheritance: beckn:RetailItem ← beckn:FoodAndBeverageItem
Use in: beckn:Commitment.commitmentAttributes for F&B orders |
| [FoodAndBeverageOffer](https://schema.beckn.io/FoodAndBeverageOffer/README.md) | v2.0 | - |
| [Form](https://schema.beckn.io/Form/README.md) | v2.1 | Describes a form |
| [FormSubmission](https://schema.beckn.io/FormSubmission/README.md) | v2.0 | A user's submitted response to a Beckn form. Captures the filled-in field values keyed by form field names. Typically attached to a RatingInput to convey feedback form answers alongside a rating. |
| [Frequency](https://schema.beckn.io/Frequency/README.md) | v2.0 | Attributes for the Frequency entity in the Beckn Mobility domain. |
| [Fulfillment](https://schema.beckn.io/Fulfillment/README.md) | v2.1 | Schema definition for Fulfillment in the Beckn Protocol v2.0.1 |
| [FulfillmentAgent](https://schema.beckn.io/FulfillmentAgent/README.md) | v2.0 | The entity directly involved in fulfilling the order. It could be a person, an organization, a machine, a software application, or an AI Agent. |
| [FulfillmentMode](https://schema.beckn.io/FulfillmentMode/README.md) | v2.0 | Describes the mode of fulfillment. This is an extensible container allowing domain-specific fulfillment modes to be expressed via attributes. |
| [FulfillmentStage](https://schema.beckn.io/FulfillmentStage/README.md) | v2.0 | Schema definition for FulfillmentStage in the Beckn Protocol v2.0.1 |
| [FulfillmentStageAuthorization](https://schema.beckn.io/FulfillmentStageAuthorization/README.md) | v2.0 | A credential/document/proof relevant to authorization at a fulfillment stage endpoint. This may be a token to be verified (QR/OTP/URL) or a document to be inspected manually. |
| [FulfillmentStageEndpoint](https://schema.beckn.io/FulfillmentStageEndpoint/README.md) | v2.0 | A stage boundary endpoint (entry or exit) within a fulfillment, such as pickup, handover, warehouse in/out, border crossing, gate entry/exit, security check, etc. May require one or more proofs/permits/tokens/documents. |
| [FulfillmentStop](https://schema.beckn.io/FulfillmentStop/README.md) | v2.0 | Attributes for the FulfillmentStop entity in the Beckn Mobility domain. |
| [GeneralMessageDelivery](https://schema.beckn.io/GeneralMessageDelivery/README.md) | v2.0 | Attributes for the GeneralMessageDelivery entity in the Beckn Mobility domain. |
| [GeoJSONGeometry](https://schema.beckn.io/GeoJSONGeometry/README.md) | v2.0 | **GeoJSON geometry** per RFC 7946. Coordinates are in **EPSG:4326 (WGS-84)** and MUST follow **[longitude, latitude, (altitude?)]** order.
Supported types: - Point, LineString, Polygon - MultiPoint, MultiLineString, MultiPolygon - GeometryCollection (uses `geometries` instead of `coordinates`)
Notes: - For rectangles, use a Polygon with a single linear ring where the first
  and last positions are identical.
- Circles are **not native** to GeoJSON. For circular searches, use
  `SpatialConstraint` with `op: s_dwithin` and a Point + `distanceMeters`,
  or approximate the circle as a Polygon.
- Optional `bbox` is `[west, south, east, north]` in degrees. |
| [Geofence](https://schema.beckn.io/Geofence/README.md) | v2.0 | Attributes for the Geofence entity in the Beckn Mobility domain. |
| [GeofencingZone](https://schema.beckn.io/GeofencingZone/README.md) | v2.0 | Attributes for the GeofencingZone entity in the Beckn Mobility domain. |
| [GroceryItem](https://schema.beckn.io/GroceryItem/README.md) | v2.0 | - |
| [HiringJobOfferAttributes](https://schema.beckn.io/HiringJobOfferAttributes/README.md) | v2.1 | Commercial and availability terms under which a job opportunity is offered. The proposedConsideration on the core Offer object carries the midpoint or headline compensation figure; this extension provides the full range and period breakdown for display and filtering. |
| [HiringJobResourceAttributes](https://schema.beckn.io/HiringJobResourceAttributes/README.md) | v2.1 | Intrinsic attributes of a job opportunity Resource. Domain-generic: applicable to any hiring vertical (tech, construction, logistics, healthcare, gig economy, etc.). |
| [HiringProcessPerformanceAttributes](https://schema.beckn.io/HiringProcessPerformanceAttributes/README.md) | v2.1 | Execution state of the hiring process service. Covers the pipeline from initial screening through to offer acceptance or withdrawal. Includes optional credential verification triggered by the employer during the hiring process. |
| [HomeAndKitchenItem](https://schema.beckn.io/HomeAndKitchenItem/README.md) | v2.0 | - |
| [Hub](https://schema.beckn.io/Hub/README.md) | v2.0 | A Hub is a logistics fulfillment center, sorting facility, or distribution point where goods are consolidated, sorted, and dispatched for onward delivery. Maps to beckn:Location. |
| [HyperlocalDelivery](https://schema.beckn.io/HyperlocalDelivery/README.md) | v2.0 | A Beckn domain schema for hyperlocal (same-city, typically sub-2-hour) physical delivery
of goods or prepared food from an origin to a destination within a short radius.

HyperlocalDelivery is a concrete, domain-specific fulfillmentAttributes value for a
beckn:Fulfillment entry. It is fully aligned with schema:ParcelDelivery.

schema.org alignment: schema:ParcelDelivery (subtype of schema:Intangible)
Use in: beckn:Fulfillment.fulfillmentAttributes |
| [Incident](https://schema.beckn.io/Incident/README.md) | v2.0 | Attributes for the Incident entity in the Beckn Mobility domain. |
| [InitAction](https://schema.beckn.io/InitAction/README.md) | v2.0 | Beckn /beckn/init action envelope. Sent by a BAP to a BPP to initialise a contract with consumer details (billing address, fulfillment preferences, etc.). |
| [Instruction](https://schema.beckn.io/Instruction/README.md) | v2.0 | Schema definition for Instruction in the Beckn Protocol v2.0.1 |
| [Intent](https://schema.beckn.io/Intent/README.md) | v2.0 | A declaration of an intent to discover catalogs. |
| [Interchange](https://schema.beckn.io/Interchange/README.md) | v2.0 | Attributes for the Interchange entity in the Beckn Mobility domain. |
| [Invoice](https://schema.beckn.io/Invoice/README.md) | v2.1 | Schema definition for Invoice in the Beckn Protocol v2.0.1 |
| [Item](https://schema.beckn.io/Item/README.md) | v2.1 | Schema definition for Item in the Beckn Protocol v2.0.1 |
| [Itinerary](https://schema.beckn.io/Itinerary/README.md) | v2.0 | Attributes for the Itinerary entity in the Beckn Mobility domain. |
| [ItineraryElement](https://schema.beckn.io/ItineraryElement/README.md) | v2.0 | Attributes for the ItineraryElement entity in the Beckn Mobility domain. |
| [JobApplicationContractAttributes](https://schema.beckn.io/JobApplicationContractAttributes/README.md) | v2.1 | Transaction-level metadata for a job application contract. Captures the application reference, aggregate verification outcome, and reverification state. No credential payloads are stored here. |
| [JobApplicationPerformanceAttributes](https://schema.beckn.io/JobApplicationPerformanceAttributes/README.md) | v2.1 | Execution metadata for the verification and routing service performed during a job application. Includes the verification method used, per-requirement results, proof integrity reference, and routing outcome. No VC or VP payloads are stored. |
| [Journey](https://schema.beckn.io/Journey/README.md) | v2.0 | Attributes for the Journey entity in the Beckn Mobility domain. |
| [Leg](https://schema.beckn.io/Leg/README.md) | v2.0 | Attributes for the Leg entity in the Beckn Mobility domain. |
| [Level](https://schema.beckn.io/Level/README.md) | v2.0 | Attributes for the Level entity in the Beckn Mobility domain. |
| [Line](https://schema.beckn.io/Line/README.md) | v2.0 | Attributes for the Line entity in the Beckn Mobility domain. |
| [LineageEntry](https://schema.beckn.io/LineageEntry/README.md) | v2.0 | A causal attribution record asserting that the Beckn transaction in which this entry appears was triggered by a specific upstream Beckn interaction. Used in Context.lineage at transaction boundaries — when a new transaction is initiated as a direct consequence of an upstream interaction. MUST NOT be included within subsequent steps of the same transaction, and MUST NOT be propagated by downstream responses. |
| [Location](https://schema.beckn.io/Location/README.md) | v2.0 | A **place** represented by **GeoJSON geometry** (Point/Polygon/Multi*) and optional human-readable `address`. This unifies all Beckn location fields into a single, widely-adopted representation (GeoJSON). |
| [LocationGroup](https://schema.beckn.io/LocationGroup/README.md) | v2.0 | Attributes for the LocationGroup entity in the Beckn Mobility domain. |
| [LocationGroupStop](https://schema.beckn.io/LocationGroupStop/README.md) | v2.0 | Attributes for the LocationGroupStop entity in the Beckn Mobility domain. |
| [LocationInformationRequest](https://schema.beckn.io/LocationInformationRequest/README.md) | v2.0 | Attributes for the LocationInformationRequest entity in the Beckn Mobility domain. |
| [LogisticsAlert](https://schema.beckn.io/LogisticsAlert/README.md) | v2.0 | An Alert is a notification or warning related to a shipment, such as delays, exceptions, damage reports, or SLA breaches. Maps to beckn:Event. |
| [LogisticsCancellationPolicy](https://schema.beckn.io/LogisticsCancellationPolicy/README.md) | v2.0 | Defines terms under which a shipment booking can be cancelled. |
| [LogisticsDriver](https://schema.beckn.io/LogisticsDriver/README.md) | v2.0 | A Driver is an individual who operates a vehicle for logistics delivery. Drivers are assigned to shipments and responsible for physical transport. Maps to beckn:Agent. |
| [LogisticsFeedback](https://schema.beckn.io/LogisticsFeedback/README.md) | v2.0 | Qualitative feedback from sender or receiver about a logistics experience. |
| [LogisticsOperator](https://schema.beckn.io/LogisticsOperator/README.md) | v2.0 | Entity operating a logistics network or fleet, responsible for end-to-end delivery service. |
| [LogisticsPlace](https://schema.beckn.io/LogisticsPlace/README.md) | v2.0 | A geographic location relevant to logistics such as origin, destination, hub, or waypoint. Includes structured address and GPS coordinates. Maps to beckn:Location and schema:Place. |
| [LogisticsRating](https://schema.beckn.io/LogisticsRating/README.md) | v2.0 | A numeric score given by a user for a logistics service, driver, or carrier. |
| [LogisticsReceipt](https://schema.beckn.io/LogisticsReceipt/README.md) | v2.0 | Digital acknowledgment of payment and delivery for a logistics service. |
| [LogisticsRoute](https://schema.beckn.io/LogisticsRoute/README.md) | v2.0 | A Route is the planned path for a shipment from origin to destination, potentially passing through multiple hubs and waypoints. Maps to beckn:Journey. |
| [LogisticsSupportCase](https://schema.beckn.io/LogisticsSupportCase/README.md) | v2.0 | Customer support ticket for shipment issues — loss, damage, delay, or billing. |
| [LogisticsVehicle](https://schema.beckn.io/LogisticsVehicle/README.md) | v2.0 | A Vehicle is a transport asset used for logistics operations. Vehicle types range from bicycles for hyperlocal delivery to heavy trucks for long haul freight. Maps to beckn:Asset. |
| [LostAndFoundItem](https://schema.beckn.io/LostAndFoundItem/README.md) | v2.0 | Attributes for the LostAndFoundItem entity in the Beckn Mobility domain. |
| [MasterSearchAction](https://schema.beckn.io/MasterSearchAction/README.md) | v2.0 | Message payload for catalog/master_search

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [MediaFile](https://schema.beckn.io/MediaFile/README.md) | v2.0 | A image, audio, or video typically intended for display purposes |
| [MediaInput](https://schema.beckn.io/MediaInput/README.md) | v2.0 | Reference to an image, audio clip, or video used for multimodal search. |
| [MediaSearch](https://schema.beckn.io/MediaSearch/README.md) | v2.0 | Container for multimodal search inputs and configuration. Supports searching through **images, audio notes, and videos** alongside text, filters, and spatial predicates. For GET, this object should be JSON-encoded and URL-escaped. |
| [MediaSearchOptions](https://schema.beckn.io/MediaSearchOptions/README.md) | v2.0 | How the discovery engine should use the provided media inputs. |
| [Message](https://schema.beckn.io/Message/README.md) | v2.0 | Open payload container for Beckn action messages. The specific content of the message object is determined by the action value in the accompanying Context. BecknAction constrains message content based on context.action via if/then dispatch rules. Direct use of this schema provides no payload constraints — use BecknAction for validated action payloads. |
| [MobilityCancellationPolicy](https://schema.beckn.io/MobilityCancellationPolicy/README.md) | v2.0 | Attributes for the CancellationPolicy entity in the Beckn Mobility domain. |
| [MobilityFeedback](https://schema.beckn.io/MobilityFeedback/README.md) | v2.0 | Attributes for the Feedback entity in the Beckn Mobility domain. |
| [MobilityRating](https://schema.beckn.io/MobilityRating/README.md) | v2.0 | Attributes for the Rating entity in the Beckn Mobility domain. |
| [MonitoredCall](https://schema.beckn.io/MonitoredCall/README.md) | v2.0 | Attributes for the MonitoredCall entity in the Beckn Mobility domain. |
| [MonitoredVehicleJourney](https://schema.beckn.io/MonitoredVehicleJourney/README.md) | v2.0 | Attributes for the MonitoredVehicleJourney entity in the Beckn Mobility domain. |
| [NackBadRequest](https://schema.beckn.io/NackBadRequest/README.md) | v2.0 | NACK — Bad Request: Malformed or invalid request; the server could not parse or validate the payload.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [NackUnauthorized](https://schema.beckn.io/NackUnauthorized/README.md) | v2.0 | Invalid or missing authentication credentials; signature could not be verified.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Network](https://schema.beckn.io/Network/README.md) | v2.0 | Attributes for the Network entity in the Beckn Mobility domain. |
| [NoShowPolicy](https://schema.beckn.io/NoShowPolicy/README.md) | v2.0 | Attributes for the NoShowPolicy entity in the Beckn Mobility domain. |
| [OccupancyStatus](https://schema.beckn.io/OccupancyStatus/README.md) | v2.0 | Attributes for the OccupancyStatus entity in the Beckn Mobility domain. |
| [Offer](https://schema.beckn.io/Offer/README.md) | v2.1 | A generalized, cross-domain Offer that captures the terms under which
one or more Resources may be committed.

Core intent:
- Support multiple terms/eligibility/constraints/price points for the same Resource(s)
- Support dynamic / on-the-fly offers (e.g., bundling, combinational discounts,
 eligibility changes, capacity-aware pricing)

This mirrors the role of Offer in current Beckn (and schema.org patterns),
but keeps the shape minimal and composable via `beckn:offerAttributes`.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [OnCancelAction](https://schema.beckn.io/OnCancelAction/README.md) | v2.0 | Beckn /beckn/on_cancel callback envelope. Sent by a BPP to a BAP in response to a /beckn/cancel call, returning the contract with status set to CANCELLED and any applicable cancellation outcome. |
| [OnConfirmAction](https://schema.beckn.io/OnConfirmAction/README.md) | v2.0 | Beckn /beckn/on_confirm callback envelope. Sent by a BPP to a BAP in response to a /beckn/confirm call, returning the confirmed contract with status set to CONFIRMED. |
| [OnDiscoverAction](https://schema.beckn.io/OnDiscoverAction/README.md) | v2.0 | Beckn /beckn/on_discover message payload. Sent by a BPP or CDS to a BAP
in response to a discover request. Contains matching catalogs. |
| [OnInitAction](https://schema.beckn.io/OnInitAction/README.md) | v2.0 | Beckn /beckn/on_init callback envelope. Sent by a BPP to a BAP in response to a /beckn/init call, with the updated contract including payment terms and billing confirmation. |
| [OnRateAction](https://schema.beckn.io/OnRateAction/README.md) | v2.0 | Beckn /beckn/on_rate callback envelope. Sent by a BPP to a BAP in response to a /beckn/rate call, optionally returning rating forms to collect structured feedback from the consumer. |
| [OnSelectAction](https://schema.beckn.io/OnSelectAction/README.md) | v2.0 | Beckn /beckn/on_select callback envelope. Sent by a BPP to a BAP in response to a /beckn/select call, with updated contract terms. |
| [OnStatusAction](https://schema.beckn.io/OnStatusAction/README.md) | v2.0 | Beckn /beckn/on_status callback envelope. Sent by a BPP to a BAP in response to a /beckn/status call (or as an unsolicited status push), returning the current state of the contract. |
| [OnSupportAction](https://schema.beckn.io/OnSupportAction/README.md) | v2.0 | Beckn /beckn/on_support callback envelope. Sent by a BPP to a BAP in response to a /beckn/support call, returning support contact details and available channels. |
| [OnTrackAction](https://schema.beckn.io/OnTrackAction/README.md) | v2.0 | Beckn /beckn/on_track callback envelope. Sent by a BPP to a BAP in response to a /beckn/track call, returning a Tracking handle with the URL and/or WebSocket endpoint for real-time fulfillment tracking. |
| [OnUpdateAction](https://schema.beckn.io/OnUpdateAction/README.md) | v2.0 | Beckn /beckn/on_update callback envelope. Sent by a BPP to a BAP in response to a /beckn/update call (or as an unsolicited update push), returning the updated contract state. |
| [Operator](https://schema.beckn.io/Operator/README.md) | v2.0 | Attributes for the Operator entity in the Beckn Mobility domain. |
| [Order](https://schema.beckn.io/Order/README.md) | v2.0 | Schema definition for Order in the Beckn Protocol |
| [OrderItem](https://schema.beckn.io/OrderItem/README.md) | v2.0 | Schema definition for OrderItem in the Beckn Protocol |
| [Organization](https://schema.beckn.io/Organization/README.md) | v2.0 | An organization such as a company, non-profit, or governmental institution. Modeled after schema.org/Organization. |
| [Package](https://schema.beckn.io/Package/README.md) | v2.0 | A Package is a physical unit of goods prepared for transport within a shipment. Maps to beckn:Item. |
| [Pagination](https://schema.beckn.io/Pagination/README.md) | v2.0 | Pagination metadata returned with list responses

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Participant](https://schema.beckn.io/Participant/README.md) | v2.0 | Schema definition for Participant in the Beckn Protocol v2.0.1 |
| [Passenger](https://schema.beckn.io/Passenger/README.md) | v2.0 | Attributes for the Passenger entity in the Beckn Mobility domain. |
| [PassengerCount](https://schema.beckn.io/PassengerCount/README.md) | v2.0 | Attributes for the PassengerCount entity in the Beckn Mobility domain. |
| [PassengerGroup](https://schema.beckn.io/PassengerGroup/README.md) | v2.0 | Attributes for the PassengerGroup entity in the Beckn Mobility domain. |
| [Pathway](https://schema.beckn.io/Pathway/README.md) | v2.0 | Attributes for the Pathway entity in the Beckn Mobility domain. |
| [Pattern](https://schema.beckn.io/Pattern/README.md) | v2.0 | Attributes for the Pattern entity in the Beckn Mobility domain. |
| [Payment](https://schema.beckn.io/Payment/README.md) | v2.0 | Schema definition for Payment in the Beckn Protocol |
| [PaymentAction](https://schema.beckn.io/PaymentAction/README.md) | v2.0 | Schema definition for PaymentAction in the Beckn Protocol v2.0.1 |
| [PaymentTerm](https://schema.beckn.io/PaymentTerm/README.md) | v2.0 | A single payment instruction for an order. Represents one line item in the paymentTerms array of an Order — e.g., a pre-order UPI payment, a cash-on-delivery amount, or an instalment. |
| [PaymentTerms](https://schema.beckn.io/PaymentTerms/README.md) | v2.0 | Schema definition for PaymentTerms in the Beckn Protocol v2.0.1 |
| [PaymentTrigger](https://schema.beckn.io/PaymentTrigger/README.md) | v2.0 | Describes when in the order lifecycle a payment flow should be triggered. Typically useful for initiating checkouts and settlement flows. |
| [Performance](https://schema.beckn.io/Performance/README.md) | v2.0 | Generalized execution/performance unit. This is where downstream objects bind:
- Fulfillment-like details (where/when/how)
- Tracking handles
- Support touchpoints
- Status updates

A minimal envelope that carries identity, status, and a performanceAttributes
bag that holds the concrete domain-specific delivery schema.

Domain specification authors can attach rich context and types via `performanceAttributes`.

For example, Hyperlocal delivery details (pickup/delivery locations, items shipped, agent, etc.)
are placed inside performanceAttributes using a well-known domain schema such as
HyperlocalDelivery. Use the generic Attributes schema when no well-known
domain schema exists.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Person](https://schema.beckn.io/Person/README.md) | v2.0 | A person (alive, deceased, or fictional). Modeled after schema.org/Person. |
| [PickupDropoffPoint](https://schema.beckn.io/PickupDropoffPoint/README.md) | v2.0 | Attributes for the PickupDropoffPoint entity in the Beckn Mobility domain. |
| [PickupPolicy](https://schema.beckn.io/PickupPolicy/README.md) | v2.0 | Attributes for the PickupPolicy entity in the Beckn Mobility domain. |
| [Place](https://schema.beckn.io/Place/README.md) | v2.0 | Attributes for the Place entity in the Beckn Mobility domain. |
| [PlaceRequest](https://schema.beckn.io/PlaceRequest/README.md) | v2.0 | Attributes for the PlaceRequest entity in the Beckn Mobility domain. |
| [Plan](https://schema.beckn.io/Plan/README.md) | v2.0 | Attributes for the Plan entity in the Beckn Mobility domain. |
| [PlanningResult](https://schema.beckn.io/PlanningResult/README.md) | v2.0 | Attributes for the PlanningResult entity in the Beckn Mobility domain. |
| [Policy](https://schema.beckn.io/Policy/README.md) | v2.0 | Schema definition for Policy in the Beckn Protocol v2.0.1 |
| [PriceSpecification](https://schema.beckn.io/PriceSpecification/README.md) | v2.1 | Schema definition for PriceSpecification in the Beckn Protocol v2.0.1 |
| [PricingModel](https://schema.beckn.io/PricingModel/README.md) | v2.0 | Attributes for the PricingModel entity in the Beckn Mobility domain. |
| [ProcessingNotice](https://schema.beckn.io/ProcessingNotice/README.md) | v2.0 | Schema definition for ProcessingNotice in the Beckn Protocol v2.0.1 |
| [Prognosis](https://schema.beckn.io/Prognosis/README.md) | v2.0 | Attributes for the Prognosis entity in the Beckn Mobility domain. |
| [Proof](https://schema.beckn.io/Proof/README.md) | v2.0 | Proof of delivery or pickup evidence, including photos, signatures, OTP confirmations, or digital receipts. Maps to beckn:Document. |
| [Provider](https://schema.beckn.io/Provider/README.md) | v2.1 | Schema definition for Provider in the Beckn Protocol v2.0.1

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [PullResultFile](https://schema.beckn.io/PullResultFile/README.md) | v2.0 | JSON body of `GET /catalog/pull/result/{requestId}/catalogs.json`.
Same structure as the inline `catalog` array in the callback payload —
a list of distribution-envelope catalog objects.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Quantity](https://schema.beckn.io/Quantity/README.md) | v2.0 | Schema definition for Quantity in the Beckn Protocol v2.0.1 |
| [Quay](https://schema.beckn.io/Quay/README.md) | v2.0 | Attributes for the Quay entity in the Beckn Mobility domain. |
| [Quote](https://schema.beckn.io/Quote/README.md) | v2.0 | A price quote generated by a BPP for a specific selection of offers and fulfillment options. Returned in on_select, on_init, and on_confirm responses. Aggregates item prices, taxes, delivery charges, and discounts into a total. |
| [RateAction](https://schema.beckn.io/RateAction/README.md) | v2.0 | Beckn /beckn/rate action envelope. Sent by a BAP to a BPP to submit one or more rating inputs for entities in a completed contract (order, fulfillment, item, provider, agent, support). |
| [Rating](https://schema.beckn.io/Rating/README.md) | v2.1 | Aggregated rating information for an entity. Aligns with schema.org/AggregateRating semantics. |
| [RatingForm](https://schema.beckn.io/RatingForm/README.md) | v2.0 | A form designed to capture rating and feedback from a user. This can be used by both BAP and BPP to fetch ratings and feedback of their respective users. |
| [RatingInput](https://schema.beckn.io/RatingInput/README.md) | v2.1 | A form designed to capture rating and feedback from a user. This can be used by both BAP and BPP to fetch ratings and feedback of their respective users.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Receipt](https://schema.beckn.io/Receipt/README.md) | v2.0 | Attributes for the Receipt entity in the Beckn Mobility domain. |
| [RecurringSchedule](https://schema.beckn.io/RecurringSchedule/README.md) | v2.0 | Defines a recurring temporal schedule such as operating hours or serviceability timing windows. Supports day-based recurrence and optional holiday exclusions. |
| [RefundTerms](https://schema.beckn.io/RefundTerms/README.md) | v2.0 | Schema definition for RefundTerms in the Beckn Protocol v2.0.1 |
| [RequestAction](https://schema.beckn.io/RequestAction/README.md) | v2.0 | DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema.
Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). The request/callback distinction is encoded in context.action (e.g. beckn/discover for requests, beckn/on_discover for callbacks).
This schema will be removed in a future major version. |
| [RequestDigest](https://schema.beckn.io/RequestDigest/README.md) | v2.0 | A cryptographic binding that explicitly ties a callback to the
specific inbound request that triggered it. Establishes bilateral non-repudiation
for the asynchronous leg of a Beckn interaction.

Use `lineage` (on `Context`) for cross-transaction causality.

Verification steps:
1. Recompute BLAKE2b-512 digest of the original request body; compare to `digest`.
2. Confirm `messageId` matches the `messageId` from the original request `Context`.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Resource](https://schema.beckn.io/Resource/README.md) | v2.0 | A minimal, domain-neutral abstraction representing any discoverable,
referenceable, or committable unit of value, capability, service,
entitlement, or asset within the network.

Examples:
- A retail product SKU, a mobility ride, a job role, a carbon credit unit,
 a dataset/API entitlement, a training course, a clinic service slot.

Designed for composability through `resourceAttributes` where
domain packs can plug in their specific fields without changing the core.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [RetailCoreFulfillmentAttributes](https://schema.beckn.io/RetailCoreFulfillmentAttributes/README.md) | v2.0 | Retail-specific fulfillment attribute pack extending Beckn core Fulfillment. Used as the value of Fulfillment.fulfillmentAttributes for retail domain fulfillments. Covers supported fulfillment types, delivery endpoint, operating schedule, SLA semantics, and handling constraints. |
| [RetailCoreItemAttributes](https://schema.beckn.io/RetailCoreItemAttributes/README.md) | v2.0 | Retail-specific item attribute pack, used as the value of Item.itemAttributes for retail domain items. Covers physical properties, food classification, regulatory declarations, and verifiable credentials. |
| [RetailCoreOfferAttributes](https://schema.beckn.io/RetailCoreOfferAttributes/README.md) | v2.0 | Retail-specific offer attribute pack, used as the value of Offer.offerAttributes for retail domain offers. Covers return/cancellation/replacement policies, payment constraints, serviceability (distance + timing), daily time window, and holidays. |
| [RetailCoreOrderAttributes](https://schema.beckn.io/RetailCoreOrderAttributes/README.md) | v2.0 | Retail-specific order-level attributes that extend core Beckn Order. Used as the value of Order.orderAttributes for retail domain orders. Captures transaction-instance metadata relevant to retail domains without duplicating core Order semantics. |
| [RetailItem](https://schema.beckn.io/RetailItem/README.md) | v2.1 | A minimal retail item schema for use in Contract.commitments[].commitmentAttributes.

RetailItem is the foundational schema for items in retail transactions.
It extends beckn:Resource with the core retail item properties: price, quantity,
and verifiable credentials. Domain-specific schemas (e.g. FoodAndBeverageItem)
extend RetailItem with additional domain-specific attributes.

Inheritance: beckn:Resource ← beckn:RetailItem
Use in: beckn:Commitment.commitmentAttributes for retail orders |
| [ReturnPolicy](https://schema.beckn.io/ReturnPolicy/README.md) | v2.0 | Defines conditions for returning goods and reverse logistics workflows. |
| [Review](https://schema.beckn.io/Review/README.md) | v2.0 | Attributes for the Review entity in the Beckn Mobility domain. |
| [RideOption](https://schema.beckn.io/RideOption/README.md) | v2.0 | Attributes for the RideOption entity in the Beckn Mobility domain. |
| [RideRequest](https://schema.beckn.io/RideRequest/README.md) | v2.0 | Attributes for the RideRequest entity in the Beckn Mobility domain. |
| [Rider](https://schema.beckn.io/Rider/README.md) | v2.0 | Attributes for the Rider entity in the Beckn Mobility domain. |
| [RiderCategory](https://schema.beckn.io/RiderCategory/README.md) | v2.0 | Attributes for the RiderCategory entity in the Beckn Mobility domain. |
| [Route](https://schema.beckn.io/Route/README.md) | v2.0 | Attributes for the Route entity in the Beckn Mobility domain. |
| [SafetyPolicy](https://schema.beckn.io/SafetyPolicy/README.md) | v2.0 | Attributes for the SafetyPolicy entity in the Beckn Mobility domain. |
| [SalesOfferPackage](https://schema.beckn.io/SalesOfferPackage/README.md) | v2.0 | Attributes for the SalesOfferPackage entity in the Beckn Mobility domain. |
| [Seat](https://schema.beckn.io/Seat/README.md) | v2.0 | Attributes for the Seat entity in the Beckn Mobility domain. |
| [Segment](https://schema.beckn.io/Segment/README.md) | v2.0 | Attributes for the Segment entity in the Beckn Mobility domain. |
| [SelectAction](https://schema.beckn.io/SelectAction/README.md) | v2.0 | Beckn /beckn/select action envelope. Sent by a BAP to a BPP to select items and offers from a catalog, initiating the negotiation cycle. |
| [ServerError](https://schema.beckn.io/ServerError/README.md) | v2.0 | Internal failure on the network participant's application; the request could not be processed. The response body MAY contain an `error` object with additional details.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [ServiceCalendar](https://schema.beckn.io/ServiceCalendar/README.md) | v2.0 | Attributes for the ServiceCalendar entity in the Beckn Mobility domain. |
| [ServiceClass](https://schema.beckn.io/ServiceClass/README.md) | v2.0 | Attributes for the ServiceClass entity in the Beckn Mobility domain. |
| [ServiceDelivery](https://schema.beckn.io/ServiceDelivery/README.md) | v2.0 | Attributes for the ServiceDelivery entity in the Beckn Mobility domain. |
| [Settlement](https://schema.beckn.io/Settlement/README.md) | v2.0 | This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [SettlementSchedule](https://schema.beckn.io/SettlementSchedule/README.md) | v2.0 | Schema definition for SettlementSchedule in the Beckn Protocol v2.0.1 |
| [SettlementTerm](https://schema.beckn.io/SettlementTerm/README.md) | v2.0 | Describes the terms of settlement associated with a given transaction. This is not to be confused with the PaymentAction as it describes all the places where the money gets disbursed after reconciliation. |
| [Shape](https://schema.beckn.io/Shape/README.md) | v2.0 | Attributes for the Shape entity in the Beckn Mobility domain. |
| [Shipment](https://schema.beckn.io/Shipment/README.md) | v2.0 | A Shipment represents the movement of one or more packages from an origin to a destination. It is the top-level fulfillment entity in a logistics transaction and maps to beckn:Fulfillment. |
| [ShippingFare](https://schema.beckn.io/ShippingFare/README.md) | v2.0 | Total cost charged for a logistics service including base freight, surcharges, taxes. |
| [ShippingFareBreakup](https://schema.beckn.io/ShippingFareBreakup/README.md) | v2.0 | A single line item in the fare breakup for a logistics service. |
| [Signature](https://schema.beckn.io/Signature/README.md) | v2.0 | A digitally signed authentication credential in the HTTP `Authorization` header.
Follows draft-cavage-http-signatures-12 as profiled by BECKN-006.

Format:
```
Signature keyId="{subscriberId}\|{uniqueKeyId}\|{algorithm}",algorithm="{algorithm}",created="{unixTimestamp}",expires="{unixTimestamp}",headers="{signedHeaders}",signature="{base64Signature}"
```

\| Attribute \| Description \|
\|-----------\|-------------\|
\| `keyId` \| `{subscriberId}\\|{uniqueKeyId}\\|{algorithm}` — FQDN, registry UUID, signing algorithm \|
\| `algorithm` \| MUST be `ed25519` \|
\| `created` \| Unix timestamp when the signature was created \|
\| `expires` \| Unix timestamp when the signature expires \|
\| `headers` \| Space-separated signed headers. MUST include `(created)`, `(expires)`, `digest` \|
\| `signature` \| Base64-encoded Ed25519 signature over the signing string \|

Signing string:
`(created): {value}\n(expires): {value}\ndigest: BLAKE-512={digest}`
where `digest` is a BLAKE2b-512 hash of the request body, Base64-encoded. |
| [Skill](https://schema.beckn.io/Skill/README.md) | v2.0 | Schema definition for Skill in the Beckn Protocol v2.0.1 |
| [SkillEntry](https://schema.beckn.io/SkillEntry/README.md) | v2.1 | A single skill, qualification, or credential held by a candidate. The attested flag and proof_request_url are optional — allowing the schema to function in early-stage ecosystems where VC infrastructure is not yet universal. As VCs become available for specific skills, the proof_request_url can be populated without any schema change. |
| [SpatialConstraint](https://schema.beckn.io/SpatialConstraint/README.md) | v2.0 | **Spatial predicate** using **OGC CQL2 (JSON semantics)** applied to one or more geometry targets in an item. This is where clients express spatial intent.
Key ideas: - `targets`: one or more **JSONPath-like** pointers that locate geometry

  fields within each item document (e.g., `$['availableAt'][*]['geo']`).
- `op`: spatial operator (CQL2). Common ones:

    • `S_WITHIN`     (A is completely inside B)
    • `S_INTERSECTS` (A intersects B)
    • `S_CONTAINS`   (A contains B)
    • `S_DWITHIN`    (A within distance of B)
- `geometry`: **GeoJSON** literal used as the predicate reference geometry. - `distanceMeters`: required for `S_DWITHIN` when using a GeoJSON Point/shape. - `quantifier`: if a target resolves to an array, choose whether **ANY** (default),

  **ALL**, or **NONE** of elements must satisfy the predicate.

CRS: unless otherwise stated, all coordinates are **EPSG:4326**. |
| [State](https://schema.beckn.io/State/README.md) | v2.0 | Schema definition for State in the Beckn Protocol v2.0.1 |
| [Station](https://schema.beckn.io/Station/README.md) | v2.0 | Attributes for the Station entity in the Beckn Mobility domain. |
| [StationInformation](https://schema.beckn.io/StationInformation/README.md) | v2.0 | Attributes for the StationInformation entity in the Beckn Mobility domain. |
| [StationStatus](https://schema.beckn.io/StationStatus/README.md) | v2.0 | Attributes for the StationStatus entity in the Beckn Mobility domain. |
| [StatusAction](https://schema.beckn.io/StatusAction/README.md) | v2.0 | Beckn /beckn/status action envelope. Sent by a BAP to a BPP to request the current status of an existing contract/order, identified by its id. |
| [Stop](https://schema.beckn.io/Stop/README.md) | v2.0 | Attributes for the Stop entity in the Beckn Mobility domain. |
| [StopArea](https://schema.beckn.io/StopArea/README.md) | v2.0 | Attributes for the StopArea entity in the Beckn Mobility domain. |
| [StopEvent](https://schema.beckn.io/StopEvent/README.md) | v2.0 | Attributes for the StopEvent entity in the Beckn Mobility domain. |
| [StopMonitoring](https://schema.beckn.io/StopMonitoring/README.md) | v2.0 | Attributes for the StopMonitoring entity in the Beckn Mobility domain. |
| [StopPlace](https://schema.beckn.io/StopPlace/README.md) | v2.0 | Attributes for the StopPlace entity in the Beckn Mobility domain. |
| [StopPoint](https://schema.beckn.io/StopPoint/README.md) | v2.0 | Attributes for the StopPoint entity in the Beckn Mobility domain. |
| [StopTime](https://schema.beckn.io/StopTime/README.md) | v2.0 | Attributes for the StopTime entity in the Beckn Mobility domain. |
| [StopTimeUpdate](https://schema.beckn.io/StopTimeUpdate/README.md) | v2.0 | Attributes for the StopTimeUpdate entity in the Beckn Mobility domain. |
| [Support](https://schema.beckn.io/Support/README.md) | v2.0 | Support request payload sent by a BAP to a BPP in the /beckn/support call. Used to request support contact information, report an issue, or open a support ticket for an existing order. |
| [SupportAction](https://schema.beckn.io/SupportAction/README.md) | v2.0 | Beckn /beckn/support action envelope. Sent by a BAP to a BPP to request support contact information or to open a support ticket for an existing order/contract. |
| [SupportCase](https://schema.beckn.io/SupportCase/README.md) | v2.0 | Attributes for the SupportCase entity in the Beckn Mobility domain. |
| [SupportInfo](https://schema.beckn.io/SupportInfo/README.md) | v2.1 | Canonical support contact for an entity, mapped to schema.org ContactPoint. |
| [SupportRequest](https://schema.beckn.io/SupportRequest/README.md) | v2.0 | Support request by a user. If no field is set, the user can expect a public support contact info |
| [SupportResponse](https://schema.beckn.io/SupportResponse/README.md) | v2.0 | Support response payload returned by a BPP to a BAP in the /beckn/on_support callback. Contains the support ticket reference, available contact channels, SLA commitment, and optional consumer acknowledgement details. |
| [SupportTicket](https://schema.beckn.io/SupportTicket/README.md) | v2.0 | A support ticket raised against an order |
| [SurgeMultiplier](https://schema.beckn.io/SurgeMultiplier/README.md) | v2.0 | Attributes for the SurgeMultiplier entity in the Beckn Mobility domain. |
| [SystemPricingPlan](https://schema.beckn.io/SystemPricingPlan/README.md) | v2.0 | Attributes for the SystemPricingPlan entity in the Beckn Mobility domain. |
| [TariffZone](https://schema.beckn.io/TariffZone/README.md) | v2.0 | Attributes for the TariffZone entity in the Beckn Mobility domain. |
| [Telemetry](https://schema.beckn.io/Telemetry/README.md) | v2.0 | Attributes for the Telemetry entity in the Beckn Mobility domain. |
| [Ticket](https://schema.beckn.io/Ticket/README.md) | v2.0 | Attributes for the Ticket entity in the Beckn Mobility domain. |
| [Time](https://schema.beckn.io/Time/README.md) | v2.0 | Represents a moment or duration in time. Can express a timestamp, a duration, or a time range. |
| [TimePeriod](https://schema.beckn.io/TimePeriod/README.md) | v2.1 | Time window with date-time precision for availability/validity

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Timetable](https://schema.beckn.io/Timetable/README.md) | v2.0 | Attributes for the Timetable entity in the Beckn Mobility domain. |
| [TrackAction](https://schema.beckn.io/TrackAction/README.md) | v2.1 | This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Tracking](https://schema.beckn.io/Tracking/README.md) | v2.1 | Information regarding live tracking of the fufillment of a contract

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [TrackingRequest](https://schema.beckn.io/TrackingRequest/README.md) | v2.0 | Schema definition for TrackingRequest in the Beckn Protocol v2.0.1 |
| [TrackingUpdate](https://schema.beckn.io/TrackingUpdate/README.md) | v2.0 | A TrackingUpdate is a real-time or periodic update on the status and location of a shipment during transit. Maps to beckn:Event. |
| [TransactionEndpoint](https://schema.beckn.io/TransactionEndpoint/README.md) | v2.0 | Beckn protocol transaction endpoint identifier. |
| [Transfer](https://schema.beckn.io/Transfer/README.md) | v2.0 | Attributes for the Transfer entity in the Beckn Mobility domain. |
| [TransitAlert](https://schema.beckn.io/TransitAlert/README.md) | v2.0 | Attributes for the Alert entity in the Beckn Mobility domain. |
| [TransitEntitlement](https://schema.beckn.io/TransitEntitlement/README.md) | v2.0 | Attributes for the Entitlement entity in the Beckn Mobility domain. |
| [TransportObject](https://schema.beckn.io/TransportObject/README.md) | v2.0 | Attributes for the TransportObject entity in the Beckn Mobility domain. |
| [TransportProvider](https://schema.beckn.io/TransportProvider/README.md) | v2.0 | Attributes for the Provider entity in the Beckn Mobility domain. |
| [TravelDocument](https://schema.beckn.io/TravelDocument/README.md) | v2.0 | Attributes for the TravelDocument entity in the Beckn Mobility domain. |
| [Trip](https://schema.beckn.io/Trip/README.md) | v2.0 | Attributes for the Trip entity in the Beckn Mobility domain. |
| [TripDescriptor](https://schema.beckn.io/TripDescriptor/README.md) | v2.0 | Attributes for the TripDescriptor entity in the Beckn Mobility domain. |
| [TripRequest](https://schema.beckn.io/TripRequest/README.md) | v2.0 | Attributes for the TripRequest entity in the Beckn Mobility domain. |
| [TripResult](https://schema.beckn.io/TripResult/README.md) | v2.0 | Attributes for the TripResult entity in the Beckn Mobility domain. |
| [TripSpecification](https://schema.beckn.io/TripSpecification/README.md) | v2.0 | Attributes for the TripSpecification entity in the Beckn Mobility domain. |
| [TripUpdate](https://schema.beckn.io/TripUpdate/README.md) | v2.0 | Attributes for the TripUpdate entity in the Beckn Mobility domain. |
| [UpdateAction](https://schema.beckn.io/UpdateAction/README.md) | v2.0 | Beckn /beckn/update action envelope. Sent by a BAP to a BPP to request changes to an active contract (e.g., update fulfillment address, add items, change quantities). The context.try flag must be true during negotiation. |
| [Vehicle](https://schema.beckn.io/Vehicle/README.md) | v2.0 | Attributes for the Vehicle entity in the Beckn Mobility domain. |
| [VehicleCategory](https://schema.beckn.io/VehicleCategory/README.md) | v2.0 | Attributes for the VehicleCategory entity in the Beckn Mobility domain. |
| [VehicleDescriptor](https://schema.beckn.io/VehicleDescriptor/README.md) | v2.0 | Attributes for the VehicleDescriptor entity in the Beckn Mobility domain. |
| [VehicleJourney](https://schema.beckn.io/VehicleJourney/README.md) | v2.0 | Attributes for the VehicleJourney entity in the Beckn Mobility domain. |
| [VehicleMonitoringDelivery](https://schema.beckn.io/VehicleMonitoringDelivery/README.md) | v2.0 | Attributes for the VehicleMonitoringDelivery entity in the Beckn Mobility domain. |
| [VehiclePosition](https://schema.beckn.io/VehiclePosition/README.md) | v2.0 | Attributes for the VehiclePosition entity in the Beckn Mobility domain. |
| [VehicleStatus](https://schema.beckn.io/VehicleStatus/README.md) | v2.0 | Attributes for the VehicleStatus entity in the Beckn Mobility domain. |
| [VehicleType](https://schema.beckn.io/VehicleType/README.md) | v2.0 | Attributes for the VehicleType entity in the Beckn Mobility domain. |
| [VerificationSummary](https://schema.beckn.io/VerificationSummary/README.md) | v2.1 | Summary of a credential verification check. Contains the overall result, reason codes for any failures, and which credential categories were successfully verified. No VC or VP payloads are included. |
| [WaitingPolicy](https://schema.beckn.io/WaitingPolicy/README.md) | v2.0 | Attributes for the WaitingPolicy entity in the Beckn Mobility domain. |
| [Waypoint](https://schema.beckn.io/Waypoint/README.md) | v2.0 | A Waypoint is an intermediate stop or checkpoint on a logistics route, such as a sorting hub, relay station, or customs checkpoint. Maps to beckn:Stop. |
