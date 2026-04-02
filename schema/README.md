# Common Schema Directory

Generated index of schema folders and latest descriptions.

| Schema | Latest Version | Description |
|---|---|---|
| [AcceptedPaymentMethod](https://schema.beckn.io/AcceptedPaymentMethod/README.md) | v2.0 | Payment methods accepted by a payee |
| [Ack](https://schema.beckn.io/Ack/README.md) | v2.0 | New v2.0 Ack format carrying an HTTP Counter-Signature proving the receiver authenticated, received, and processed the inbound request. |
| [AckNoCallback](https://schema.beckn.io/AckNoCallback/README.md) | v2.0 | Request received but no callback will follow (e.g. agents not found, inventory unavailable, provider closed, context.try preview complete). |
| [AckResponse](https://schema.beckn.io/AckResponse/README.md) | v2.0 | Schema definition for AckResponse in the Beckn Protocol |
| [AddOn](https://schema.beckn.io/AddOn/README.md) | v2.0 | Add-on to a catalog resource |
| [Address](https://schema.beckn.io/Address/README.md) | v2.0 | **Postal address** aligned with schema.org `PostalAddress`. Use for human-readable addresses. Geometry lives in `Location.geo` as GeoJSON. |
| [AffectedLine](https://schema.beckn.io/AffectedLine/README.md) | v2.0 | A reference to a transport line that is affected by a service disruption or alert. |
| [Alert](https://schema.beckn.io/Alert/README.md) | v2.0 | Schema definition for Alert in the Beckn Protocol v2.0.1 |
| [AncillaryService](https://schema.beckn.io/AncillaryService/README.md) | v2.0 | An optional or additional service available for purchase alongside base transport, such as extra baggage or lounge access. |
| [AsyncError](https://schema.beckn.io/AsyncError/README.md) | v2.0 | Error returned asynchronously during a callback. Wraps the base `Error` schema with JSON-LD type annotations to allow linked-data processing. |
| [Attributes](https://schema.beckn.io/Attributes/README.md) | v2.0 | JSON-LD aware container for domain-specific attributes of an Item. MUST include @context (URI) and @type (compact or full IRI). Any additional properties are allowed and interpreted per the provided JSON-LD context. |
| [Authority](https://schema.beckn.io/Authority/README.md) | v2.0 | A governmental or administrative body responsible for planning, regulating, and overseeing transport services within a jurisdiction. |
| [BaggageAllowance](https://schema.beckn.io/BaggageAllowance/README.md) | v2.0 | The quantity and weight of baggage a passenger is permitted to carry or check in without incurring additional charges. |
| [BikeAllowed](https://schema.beckn.io/BikeAllowed/README.md) | v2.0 | An indicator specifying whether bicycles are permitted on board a particular route or vehicle journey. |
| [BookingRule](https://schema.beckn.io/BookingRule/README.md) | v2.0 | A set of rules governing how and when a demand-responsive transport service must be booked in advance. |
| [Buyer](https://schema.beckn.io/Buyer/README.md) | v2.0 | Schema definition for Buyer in the Beckn Protocol |
| [CallbackAction](https://schema.beckn.io/CallbackAction/README.md) | v2.0 | DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. The $id also lacked a version segment.
Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). Callback actions are those with on_ prefixed endpoints (e.g. beckn/on_discover, beckn/on_confirm) and are validated by the same BecknAction schema via if/then dispatch on context.action.
This schema will be removed in a future major version. |
| [CancelAction](https://schema.beckn.io/CancelAction/README.md) | v2.0 | Beckn /beckn/cancel message payload. Sent by a BAP to a BPP to request
cancellation of an active contract. Set context.try to true to first
retrieve cancellation terms and fees before committing.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [CancellationOutcome](https://schema.beckn.io/CancellationOutcome/README.md) | v2.0 | Schema definition for CancellationOutcome in the Beckn Protocol v2.0.1 |
| [CancellationPolicy](https://schema.beckn.io/CancellationPolicy/README.md) | v2.0 | Schema definition for CancellationPolicy in the Beckn Protocol v2.0.1 |
| [CancellationReason](https://schema.beckn.io/CancellationReason/README.md) | v2.0 | Schema definition for CancellationReason in the Beckn Protocol v2.0.1 |
| [CandidateAvailabilityOfferAttributes](https://schema.beckn.io/CandidateAvailabilityOfferAttributes/README.md) | v2.1 | Availability and compensation expectation terms under which a candidate profile is offered to employers. The proposedConsideration on the core Offer carries the candidate's headline desired salary; this extension provides the full range, notice period, and contract type preferences. |
| [CandidateProfileResourceAttributes](https://schema.beckn.io/CandidateProfileResourceAttributes/README.md) | v2.1 | Discoverable profile attributes of a candidate Resource. Captures what the candidate brings (skills, experience, availability) and what they seek (location preference, work mode, job type). Designed for privacy: no name, contact, or identity data. Credentials are referenced via SkillEntry with optional VC attestation URLs. |
| [Carrier](https://schema.beckn.io/Carrier/README.md) | v2.0 | A Carrier is a transport service provider responsible for moving goods across distances. Carriers operate fleets of vehicles and may own/manage logistics hubs. Maps to beckn:Provider. |
| [Catalog](https://schema.beckn.io/Catalog/README.md) | v2.1 | Catalog schema for Beckn Protocol v2.0.0

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CatalogOnPublishAction](https://schema.beckn.io/CatalogOnPublishAction/README.md) | v2.0 | Catalog publish processing results from CDS to BPP. |
| [CatalogProcessingResult](https://schema.beckn.io/CatalogProcessingResult/README.md) | v2.0 | Processing result for a single catalog submission. |
| [CatalogPublishAction](https://schema.beckn.io/CatalogPublishAction/README.md) | v2.0 | Catalog publish request payload. |
| [CatalogPublishResponse](https://schema.beckn.io/CatalogPublishResponse/README.md) | v2.0 | Beckn /beckn/on_catalog_publish message payload. Sent by a CDS back to a BPP
after processing a catalog publish request. Contains per-catalog processing results
indicating success, failure, or partial indexing. |
| [CatalogPullAction](https://schema.beckn.io/CatalogPullAction/README.md) | v2.0 | Message payload for catalog/pull

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [CatalogSubscribeAction](https://schema.beckn.io/CatalogSubscribeAction/README.md) | v2.0 | Message payload for catalog/subscription.
At least one of `networkIds` or `schemaTypes` must be non-empty.
An empty `schemaTypes` array is treated as the wildcard sentinel `"*"`,
matching all schema types for the specified networks. |
| [CatalogSubscription](https://schema.beckn.io/CatalogSubscription/README.md) | v2.0 | Full subscription record |
| [CategoryCode](https://schema.beckn.io/CategoryCode/README.md) | v2.1 | Schema definition for CategoryCode in the Beckn Protocol v2.0.1 |
| [CheckoutTerminal](https://schema.beckn.io/CheckoutTerminal/README.md) | v2.0 | The checkout terminal where the consumer makes the payment |
| [CodedValue](https://schema.beckn.io/CodedValue/README.md) | v2.1 | An authority-governed code value. The @context URI identifies the code system authority (e.g. UN ISIC, UNESCO ISCED, India NSQF). The @type identifies the class of code within that system. The code is the actual value. This pattern avoids hardcoding country-specific enumerations into the schema. |
| [Commitment](https://schema.beckn.io/Commitment/README.md) | v2.0 | Container schemas fetched from beckn.yaml. This cannot be extended as it is a reserved schema in beckn protocol. Any additional properties added to this schema can only be made using its *Attributes property |
| [ConfirmAction](https://schema.beckn.io/ConfirmAction/README.md) | v2.0 | Beckn /beckn/confirm message payload. Sent by a BAP to a BPP to confirm
a contract, finalising the transaction terms agreed during the
select-init negotiation cycle.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [Consideration](https://schema.beckn.io/Consideration/README.md) | v2.0 | Generalized representation of value exchanged under a Contract.

Consideration is domain-neutral and may represent:
- Monetary value
- Credits / tokens
- Asset transfer
- Service exchange
- Compliance artifact |
| [Consignment](https://schema.beckn.io/Consignment/README.md) | v2.0 | A Consignment is a collection of packages or shipments grouped together under a single commercial transaction between a shipper and consignee. Maps to beckn:Order. |
| [Constraint](https://schema.beckn.io/Constraint/README.md) | v2.0 | Schema definition for Constraint in the Beckn Protocol v2.0.1 |
| [Consumer](https://schema.beckn.io/Consumer/README.md) | v2.0 | Schema definition for Consumer in the Beckn Protocol v2.0.1 |
| [Contact](https://schema.beckn.io/Contact/README.md) | v2.0 | Contact information for sender, receiver, driver, or operator. |
| [Context](https://schema.beckn.io/Context/README.md) | v2.0 | Base context schema for all Beckn API calls. Contains addressing information
(BAP/BPP identifiers and API URLs), protocol version, the action being called,
transaction and message IDs, timestamp, TTL, and optional encryption key.
This schema defines all possible properties but imposes NO required-field
constraints. Endpoint-specific validation is defined inline in operation request schemas. |
| [Contract](https://schema.beckn.io/Contract/README.md) | v2.0 | This is a JSON-LD compliant, linked-data schema that specifies a generic multi-party, digitally signed Contract between a set of participants. based on the vocabulary defined in the @context. By default, it is the most generic form of contract i.e beckn:Contract. However, based on the mapping being used in @context, it could take values like retail:Order, mobility:Reservation, healthcare:Appointment, and so on, which will be defined as sub-classes of beckn:Contract. Alternate description A digitally agreed commitment between two or more participants governing the exchange of economic or non-economic value.  Contract is the canonical contract object in the generalized Beckn v2.1 protocol. It replaces the commerce-specific Order construct as the canonical transaction object at the API layer.  A Contract binds:  - Commitments (what is agreed)  - Consideration (value promised)  - Performance (how execution occurs)  - Settlements (how consideration is discharged)  The model is domain-neutral and supports commerce, hiring, energy markets, carbon exchanges, data access, mobility, subscriptions, and other use cases. |
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
| [DayType](https://schema.beckn.io/DayType/README.md) | v2.0 | A classification of a day (e.g., weekday, weekend, public holiday) used to define when a service pattern is valid. |
| [DeliveryPolicy](https://schema.beckn.io/DeliveryPolicy/README.md) | v2.0 | Callback delivery retry configuration

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [DeliverySlot](https://schema.beckn.io/DeliverySlot/README.md) | v2.0 | A DeliverySlot is a time window offered or agreed upon for delivery of a shipment. Maps to beckn:TimeSlot. |
| [DepartureMessage](https://schema.beckn.io/DepartureMessage/README.md) | v2.0 | A real-time message containing predicted departure times for vehicles at a stop, as used in VDV real-time standards. |
| [Descriptor](https://schema.beckn.io/Descriptor/README.md) | v2.1 | Schema definition for Descriptor in the Beckn Protocol v2.0.1 |
| [Direction](https://schema.beckn.io/Direction/README.md) | v2.0 | The direction of travel of a transport service along a route, typically expressed as inbound or outbound. |
| [DiscoverAction](https://schema.beckn.io/DiscoverAction/README.md) | v2.0 | Beckn /beckn/discover message payload as published at schema.beckn.io.
Requires all discover qualifiers to be nested inside an `intent`
container object.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [DisplayedRating](https://schema.beckn.io/DisplayedRating/README.md) | v2.0 | Schema definition for DisplayedRating in the Beckn Protocol v2.0.1 |
| [Document](https://schema.beckn.io/Document/README.md) | v2.0 | A document, that can be parsed, printed, download or displayed. This has intentionally been kept separate from MediaFile as they may contain additional attributes like signature, schema etc. |
| [Driver](https://schema.beckn.io/Driver/README.md) | v2.0 | A person who operates a transport vehicle and is responsible for the safe delivery of passengers during a mobility service trip. |
| [DropPolicy](https://schema.beckn.io/DropPolicy/README.md) | v2.0 | A set of rules governing the locations and conditions under which passengers may be dropped off at the end of a ride-hailing or on-demand transport service. |
| [Eligibility](https://schema.beckn.io/Eligibility/README.md) | v2.0 | Schema definition for Eligibility in the Beckn Protocol v2.0.1 |
| [EmergencyEvent](https://schema.beckn.io/EmergencyEvent/README.md) | v2.0 | A critical safety or operational event requiring immediate response, such as an accident, vehicle breakdown, or passenger emergency. |
| [EmployerHiringContractAttributes](https://schema.beckn.io/EmployerHiringContractAttributes/README.md) | v2.1 | Contract-level metadata for an employer-to-candidate hiring offer. Captures the specific role details being offered, compensation amount (as distinct from the candidate's desired range), proposed joining date, offer expiry, and candidate response state. |
| [Entitlement](https://schema.beckn.io/Entitlement/README.md) | v2.0 | A contractually granted, policy-governed right that allows a specific party to access, use, or claim a defined economic resource within stated scope and validity constraints. It represents the enforceable permission created by an order, independent of the credential used to exercise it. |
| [EntitySelector](https://schema.beckn.io/EntitySelector/README.md) | v2.0 | A selector that identifies which transport entities (routes, trips, stops, or agencies) are affected by a given alert. |
| [Error](https://schema.beckn.io/Error/README.md) | v2.0 | Schema definition for Error in the Beckn Protocol v2.0.1 |
| [ErrorResponse](https://schema.beckn.io/ErrorResponse/README.md) | v2.0 | Schema definition for ErrorResponse in the Beckn Protocol v2.0.1 |
| [EstimatedTimetableDelivery](https://schema.beckn.io/EstimatedTimetableDelivery/README.md) | v2.0 | A real-time data delivery providing predicted departure and arrival times for a set of vehicle journeys. |
| [ExchangePoints](https://schema.beckn.io/ExchangePoints/README.md) | v2.0 | Locations in a transport network where fixed-route and flexible services connect, enabling passenger interchange. |
| [Fare](https://schema.beckn.io/Fare/README.md) | v2.0 | The monetary cost of travel for a specific journey or service, calculated based on applicable fare rules and passenger categories. |
| [FareBreakup](https://schema.beckn.io/FareBreakup/README.md) | v2.0 | A detailed breakdown of the total fare into its constituent components, including base fare, taxes, surcharges, and discounts. |
| [FareComponent](https://schema.beckn.io/FareComponent/README.md) | v2.0 | A component of an air travel fare that applies to a specific flight segment or leg, used in aviation pricing. |
| [FareEstimate](https://schema.beckn.io/FareEstimate/README.md) | v2.0 | An estimated fare for a requested trip, typically returned in response to a search before the booking is confirmed. |
| [FareLegRule](https://schema.beckn.io/FareLegRule/README.md) | v2.0 | A rule defining how a fare is applied to a single leg of a journey based on origin, destination, network, and time. |
| [FareMedium](https://schema.beckn.io/FareMedium/README.md) | v2.0 | The physical or digital medium used to carry or present a fare product, such as a contactless card, mobile app, or paper ticket. |
| [FareProduct](https://schema.beckn.io/FareProduct/README.md) | v2.0 | A purchasable entitlement to travel defining conditions of use, validity, and applicable passenger categories. |
| [FareResult](https://schema.beckn.io/FareResult/README.md) | v2.0 | The calculated fare for a requested trip, returned as part of a trip planning or fare enquiry response. |
| [FareTransferRule](https://schema.beckn.io/FareTransferRule/README.md) | v2.0 | A rule defining how fares from different legs are combined when a passenger makes a transfer between services. |
| [Feed](https://schema.beckn.io/Feed/README.md) | v2.0 | A data publication providing transit or mobility information in a standardised format for consumption by applications or planners. |
| [FlightSegment](https://schema.beckn.io/FlightSegment/README.md) | v2.0 | A single non-stop flight operated between two airports, forming a unit of an air travel itinerary. |
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
| [FnBPriceSpecification](https://schema.beckn.io/FnBPriceSpecification/README.md) | v2.0 | A price specification for food and beverage (F&B) delivery orders.  FnBPriceSpecification specializes beckn:PriceSpecification for the specific price calculation structure of a food ordering and delivery transaction. It is derived from extensive research into how food delivery platforms (Domino's, Zomato, Swiggy, UberEats) model itemised bills, including:  - Size-dependent item and topping pricing (a topping on a Regular pizza costs less   than on a Large pizza; add-on price = f(size, topping_type)) - Crust upcharges (premium crusts like Cheese Burst or Pan cost more) - Combo discount mechanics (bundle savings expressed as negative values) - Delivery and packaging fees distinct from item charges - Platform convenience charges  **Component type codes:**  Item-level charges (may appear multiple times — once per line item): - BASE_ITEM         — Base price of a food or beverage item at its selected size - SIZE_UPCHARGE     — Premium for selecting a larger size over the base size (e.g. Regular → Medium) - TOPPING           — Individual topping or ingredient add-on; price varies by item size - ADDON             — Optional add-on item (dip, sauce, condiment packet) - CUSTOMIZATION     — Surcharge for a special preparation request - SIDE              — A side dish added to the order  Combo and offer adjustments (typically negative): - COMBO_SAVINGS     — Discount from applying a bundle/meal combo deal (negative) - COMBO_UPCHARGE    — Premium for upgrading within a combo (e.g. regular to medium pizza) - OFFER_DISCOUNT    — Time-limited promotional discount applied at order level (negative) - COUPON_DISCOUNT   — Discount from a promo/coupon code (negative) - LOYALTY_DISCOUNT  — Discount from loyalty points redemption (negative)  Order-level charges: - DELIVERY_FEE      — Delivery charge (flat, distance-based, or surge-adjusted) - PACKAGING_FEE     — Restaurant packaging charge (boxes, insulated bags, eco-packaging) - SMALL_ORDER_FEE   — Surcharge applied when order value is below the minimum - PLATFORM_FEE      — App/platform convenience service charge  Gratuity: - TIP               — Customer gratuity (added voluntarily by the consumer)  Notes: - Tax components (GST, VAT, etc.) are jurisdiction-specific and MUST be modelled   using PriceSpecificationComponent variants, not as codes in this schema. - For TOPPING components, referenceItemId SHOULD be set to the ID of the base   item to which the topping belongs, since topping price varies by item size. - Negative values MUST be used for COMBO_SAVINGS, OFFER_DISCOUNT, COUPON_DISCOUNT,   and LOYALTY_DISCOUNT.  Inheritance: beckn:PriceSpecification ← beckn:FnBPriceSpecification schema.org alignment: schema:PriceSpecification (via inheritance) Use in: beckn:Consideration.considerationAttributes for F&B orders |
| [FoodAndBeverageItem](https://schema.beckn.io/FoodAndBeverageItem/README.md) | v2.1 | A Beckn schema for a food and beverage item in retail F&B ordering.

FoodAndBeverageItem v2.1 extends beckn:RetailItem with comprehensive food-specific
attributes covering classification, allergens, additives, nutritional information,
cuisine, and preparation guidance.

Inheritance: beckn:RetailItem ← beckn:FoodAndBeverageItem
Use in: beckn:Commitment.commitmentAttributes for F&B orders |
| [FoodAndBeverageOffer](https://schema.beckn.io/FoodAndBeverageOffer/README.md) | v2.0 | - |
| [Form](https://schema.beckn.io/Form/README.md) | v2.1 | Describes a form |
| [FormSubmission](https://schema.beckn.io/FormSubmission/README.md) | v2.0 | A user's submitted response to a Beckn form. Captures the filled-in field values keyed by form field names. Typically attached to a RatingInput to convey feedback form answers alongside a rating. |
| [Frequency](https://schema.beckn.io/Frequency/README.md) | v2.0 | A headway-based service specification indicating how often a vehicle runs on a route within a given time window. |
| [Fulfillment](https://schema.beckn.io/Fulfillment/README.md) | v2.1 | Schema definition for Fulfillment in the Beckn Protocol v2.0.1 |
| [FulfillmentAgent](https://schema.beckn.io/FulfillmentAgent/README.md) | v2.0 | The entity directly involved in fulfilling the order. It could be a person, an organization, a machine, a software application, or an AI Agent. |
| [FulfillmentMode](https://schema.beckn.io/FulfillmentMode/README.md) | v2.0 | Describes the mode of fulfillment. This is an extensible container allowing domain-specific fulfillment modes to be expressed via attributes. |
| [FulfillmentStage](https://schema.beckn.io/FulfillmentStage/README.md) | v2.0 | Schema definition for FulfillmentStage in the Beckn Protocol v2.0.1 |
| [FulfillmentStageAuthorization](https://schema.beckn.io/FulfillmentStageAuthorization/README.md) | v2.0 | A credential/document/proof relevant to authorization at a fulfillment stage endpoint. This may be a token to be verified (QR/OTP/URL) or a document to be inspected manually. |
| [FulfillmentStageEndpoint](https://schema.beckn.io/FulfillmentStageEndpoint/README.md) | v2.0 | A stage boundary endpoint (entry or exit) within a fulfillment, such as pickup, handover, warehouse in/out, border crossing, gate entry/exit, security check, etc. May require one or more proofs/permits/tokens/documents. |
| [FulfillmentStop](https://schema.beckn.io/FulfillmentStop/README.md) | v2.0 | A specific location associated with a fulfillment (trip or journey) at which passengers board, alight, or transfer between services. |
| [GeneralMessageDelivery](https://schema.beckn.io/GeneralMessageDelivery/README.md) | v2.0 | A real-time delivery of textual messages or alerts related to service disruptions or passenger information. |
| [GeoJSONGeometry](https://schema.beckn.io/GeoJSONGeometry/README.md) | v2.0 | **GeoJSON geometry** per RFC 7946. Coordinates are in **EPSG:4326 (WGS-84)** and MUST follow **[longitude, latitude, (altitude?)]** order. Supported types: - Point, LineString, Polygon - MultiPoint, MultiLineString, MultiPolygon - GeometryCollection (uses `geometries` instead of `coordinates`) Notes: - For rectangles, use a Polygon with a single linear ring where the first  and last positions are identical. - Circles are **not native** to GeoJSON. For circular searches, use  `SpatialConstraint` with `op: s_dwithin` and a Point + `distanceMeters`,  or approximate the circle as a Polygon. - Optional `bbox` is `[west, south, east, north]` in degrees. |
| [Geofence](https://schema.beckn.io/Geofence/README.md) | v2.0 | A virtual geographic boundary used to define service areas, restricted zones, or operational boundaries for mobility assets. |
| [GeofencingZone](https://schema.beckn.io/GeofencingZone/README.md) | v2.0 | A virtual geographic boundary used to define operational areas, speed limits, parking rules, or restrictions for shared mobility services. |
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
| [Incident](https://schema.beckn.io/Incident/README.md) | v2.0 | A reported event on the transport network that affects normal service operations, such as a disruption, roadblock, or infrastructure failure. |
| [InitAction](https://schema.beckn.io/InitAction/README.md) | v2.0 | Beckn /beckn/init message payload. Sent by a BAP to a BPP to initialise
a contract with consumer details (billing address, fulfillment preferences, etc.).
(Context wrapper stripped; only the message-content portion is inlined.) |
| [Instruction](https://schema.beckn.io/Instruction/README.md) | v2.0 | Schema definition for Instruction in the Beckn Protocol v2.0.1 |
| [Intent](https://schema.beckn.io/Intent/README.md) | v2.0 | A declaration of an intent to transact |
| [Interchange](https://schema.beckn.io/Interchange/README.md) | v2.0 | A planned transfer connection point where passengers switch between two or more transport services, with defined timing constraints. |
| [Invoice](https://schema.beckn.io/Invoice/README.md) | v2.1 | Schema definition for Invoice in the Beckn Protocol v2.0.1 |
| [Item](https://schema.beckn.io/Item/README.md) | v2.1 | Schema definition for Item in the Beckn Protocol v2.0.1 |
| [Itinerary](https://schema.beckn.io/Itinerary/README.md) | v2.0 | A complete planned trip containing an ordered sequence of legs, including transfer points, durations, and timing. |
| [ItineraryElement](https://schema.beckn.io/ItineraryElement/README.md) | v2.0 | A component of an aviation itinerary such as a flight segment, ground transport leg, or ancillary service. |
| [JobApplicationContractAttributes](https://schema.beckn.io/JobApplicationContractAttributes/README.md) | v2.1 | Transaction-level metadata for a job application contract. Captures the application reference, aggregate verification outcome, and reverification state. No credential payloads are stored here. |
| [JobApplicationPerformanceAttributes](https://schema.beckn.io/JobApplicationPerformanceAttributes/README.md) | v2.1 | Execution metadata for the verification and routing service performed during a job application. Includes the verification method used, per-requirement results, proof integrity reference, and routing outcome. No VC or VP payloads are stored. |
| [Journey](https://schema.beckn.io/Journey/README.md) | v2.0 | A complete travel itinerary from origin to destination, potentially comprising multiple legs using different transport modes. |
| [Leg](https://schema.beckn.io/Leg/README.md) | v2.0 | A single uninterrupted segment of a journey made using one transport mode or service between two consecutive locations. |
| [Level](https://schema.beckn.io/Level/README.md) | v2.0 | A floor or vertical level within a multi-level transit station or facility, used to define internal navigation paths. |
| [Line](https://schema.beckn.io/Line/README.md) | v2.0 | A named, branded public transport service identified by a number or name, typically operating over one or more routes. |
| [LineageEntry](https://schema.beckn.io/LineageEntry/README.md) | v2.0 | A causal attribution record asserting that the Beckn transaction in which this entry appears was triggered by a specific upstream Beckn interaction. Used in Context.lineage at transaction boundaries — when a new transaction is initiated as a direct consequence of an upstream interaction. MUST NOT be included within subsequent steps of the same transaction, and MUST NOT be propagated by downstream responses. |
| [Location](https://schema.beckn.io/Location/README.md) | v2.0 | A place represented by GeoJSON geometry and optional address.
Source: main/schema/core/v2/attributes.yaml#Location |
| [LocationGroup](https://schema.beckn.io/LocationGroup/README.md) | v2.0 | A set of geographic locations (stops or areas) that can collectively serve as an origin or destination for flexible transit services. |
| [LocationGroupStop](https://schema.beckn.io/LocationGroupStop/README.md) | v2.0 | An association between a stop and a location group, used in flexible transit service planning. |
| [LocationInformationRequest](https://schema.beckn.io/LocationInformationRequest/README.md) | v2.0 | A request for details about a specific geographic location, stop, or point of interest in the transport network. |
| [Logistics](https://schema.beckn.io/Logistics/README.md) | v2.0 | A Carrier is a transport service provider responsible for moving goods across distances. Carriers operate fleets of vehicles and may own/manage logistics hubs. Maps to beckn:Provider. |
| [LogisticsAlert](https://schema.beckn.io/LogisticsAlert/README.md) | v2.0 | An Alert is a notification or warning related to a shipment, such as delays, exceptions, damage reports, or SLA breaches. Maps to beckn:Event. |
| [LogisticsCancellationPolicy](https://schema.beckn.io/LogisticsCancellationPolicy/README.md) | v2.0 | Defines terms under which a shipment booking can be cancelled. |
| [LogisticsDriver](https://schema.beckn.io/LogisticsDriver/README.md) | v2.0 | A Driver is an individual who operates a vehicle for logistics delivery. Drivers are assigned to shipments and responsible for physical transport. Maps to beckn:Agent. |
| [LogisticsFare](https://schema.beckn.io/LogisticsFare/README.md) | v2.0 | Total cost charged for a logistics service including base freight, surcharges, taxes. |
| [LogisticsFareBreakup](https://schema.beckn.io/LogisticsFareBreakup/README.md) | v2.0 | A single line item in the fare breakup for a logistics service. |
| [LogisticsFeedback](https://schema.beckn.io/LogisticsFeedback/README.md) | v2.0 | Qualitative feedback from sender or receiver about a logistics experience. |
| [LogisticsOperator](https://schema.beckn.io/LogisticsOperator/README.md) | v2.0 | Entity operating a logistics network or fleet, responsible for end-to-end delivery service. |
| [LogisticsPlace](https://schema.beckn.io/LogisticsPlace/README.md) | v2.0 | A geographic location relevant to logistics such as origin, destination, hub, or waypoint. Includes structured address and GPS coordinates. Maps to beckn:Location and schema:Place. |
| [LogisticsRating](https://schema.beckn.io/LogisticsRating/README.md) | v2.0 | A numeric score given by a user for a logistics service, driver, or carrier. |
| [LogisticsReceipt](https://schema.beckn.io/LogisticsReceipt/README.md) | v2.0 | Digital acknowledgment of payment and delivery for a logistics service. |
| [LogisticsRoute](https://schema.beckn.io/LogisticsRoute/README.md) | v2.0 | A Route is the planned path for a shipment from origin to destination, potentially passing through multiple hubs and waypoints. Maps to beckn:Journey. |
| [LogisticsSupportCase](https://schema.beckn.io/LogisticsSupportCase/README.md) | v2.0 | Customer support ticket for shipment issues — loss, damage, delay, or billing. |
| [LogisticsVehicle](https://schema.beckn.io/LogisticsVehicle/README.md) | v2.0 | A Vehicle is a transport asset used for logistics operations. Vehicle types range from bicycles for hyperlocal delivery to heavy trucks for long haul freight. Maps to beckn:Asset. |
| [LostAndFoundItem](https://schema.beckn.io/LostAndFoundItem/README.md) | v2.0 | An item that has been reported lost or found in connection with a transport service. |
| [MasterSearchAction](https://schema.beckn.io/MasterSearchAction/README.md) | v2.0 | Message payload for catalog/master_search

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [MediaFile](https://schema.beckn.io/MediaFile/README.md) | v2.0 | A image, audio, or video typically intended for display purposes |
| [MediaInput](https://schema.beckn.io/MediaInput/README.md) | v2.0 | Reference to an image, audio clip, or video used for multimodal search. |
| [MediaSearch](https://schema.beckn.io/MediaSearch/README.md) | v2.0 | Container schemas fetched from beckn.yaml. This cannot be extended as it is a reserved schema in beckn protocol. Any additional properties added to this schema can only be made using its *Attributes property |
| [MediaSearchOptions](https://schema.beckn.io/MediaSearchOptions/README.md) | v2.0 | How the discovery engine should use the provided media inputs. |
| [Message](https://schema.beckn.io/Message/README.md) | v2.0 | Open payload container for Beckn action messages. The specific content of the message object is determined by the action value in the accompanying Context. BecknAction constrains message content based on context.action via if/then dispatch rules. Direct use of this schema provides no payload constraints — use BecknAction for validated action payloads. |
| [Mobility](https://schema.beckn.io/Mobility/README.md) | v2.0 | Attributes for the Mobility entity in the Beckn Mobility domain. |
| [MonitoredCall](https://schema.beckn.io/MonitoredCall/README.md) | v2.0 | A real-time arrival or departure prediction for a specific vehicle at a specific stop within a monitored journey. |
| [MonitoredVehicleJourney](https://schema.beckn.io/MonitoredVehicleJourney/README.md) | v2.0 | A real-time representation of a vehicle journey being actively tracked, including position and schedule adherence data. |
| [NackBadRequest](https://schema.beckn.io/NackBadRequest/README.md) | v2.0 | NACK — Bad Request: Malformed or invalid request; the server could not parse or validate the payload. |
| [NackUnauthorized](https://schema.beckn.io/NackUnauthorized/README.md) | v2.0 | Invalid or missing authentication credentials; signature could not be verified. |
| [Network](https://schema.beckn.io/Network/README.md) | v2.0 | A grouping of routes and lines operated under a common brand or authority, used for fare and operational management. |
| [NoShowPolicy](https://schema.beckn.io/NoShowPolicy/README.md) | v2.0 | Rules governing the consequences and fees applied when a passenger fails to appear for a confirmed transport service booking. |
| [OccupancyStatus](https://schema.beckn.io/OccupancyStatus/README.md) | v2.0 | An indicator of the current passenger load level of a vehicle, such as empty, many seats available, or full. |
| [Offer](https://schema.beckn.io/Offer/README.md) | v2.1 | A generalized, cross-domain Offer that captures the terms under which one or more Resources may be committed.  Core intent: - Support multiple terms/eligibility/constraints/price points for the same Resource(s) - Support dynamic / on-the-fly offers (e.g., bundling, combinational discounts,  eligibility changes, capacity-aware pricing)  This mirrors the role of Offer in current Beckn (and schema.org patterns), but keeps the shape minimal and composable via `beckn:offerAttributes`. |
| [OnCancelAction](https://schema.beckn.io/OnCancelAction/README.md) | v2.0 | Beckn /beckn/on_cancel message payload. Sent by a BPP to a BAP in
response to a /beckn/cancel call, returning the contract with status
set to CANCELLED and any applicable cancellation outcome.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnConfirmAction](https://schema.beckn.io/OnConfirmAction/README.md) | v2.0 | Beckn /beckn/on_confirm message payload. Sent by a BPP to a BAP in
response to a /beckn/confirm call, returning the confirmed contract
with status set to CONFIRMED.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnDiscoverAction](https://schema.beckn.io/OnDiscoverAction/README.md) | v2.0 | The on_discover response payload containing matching catalogs. |
| [OnInitAction](https://schema.beckn.io/OnInitAction/README.md) | v2.0 | Beckn /beckn/on_init message payload. Sent by a BPP to a BAP in response
to a /beckn/init call, with the updated contract including payment terms
and billing confirmation.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnRateAction](https://schema.beckn.io/OnRateAction/README.md) | v2.0 | Beckn /beckn/on_rate message payload. Sent by a BPP to a BAP in
response to a /beckn/rate call, optionally returning rating forms
to collect structured feedback from the consumer.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnSelectAction](https://schema.beckn.io/OnSelectAction/README.md) | v2.0 | Beckn /beckn/on_select message payload. Sent by a BPP to a BAP in
response to a /beckn/select call, with updated contract terms.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnStatusAction](https://schema.beckn.io/OnStatusAction/README.md) | v2.0 | Beckn /beckn/on_status message payload. Sent by a BPP to a BAP in
response to a /beckn/status call (or as an unsolicited status push),
returning the current state of the contract.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnSupportAction](https://schema.beckn.io/OnSupportAction/README.md) | v2.0 | Beckn /beckn/on_support message payload. Sent by a BPP to a BAP in
response to a /beckn/support call, returning support contact details
and available channels.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnTrackAction](https://schema.beckn.io/OnTrackAction/README.md) | v2.0 | Beckn /beckn/on_track message payload. Sent by a BPP to a BAP in
response to a /beckn/track call, returning a Tracking handle with
the URL and/or WebSocket endpoint for real-time fulfillment tracking.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [OnUpdateAction](https://schema.beckn.io/OnUpdateAction/README.md) | v2.0 | Beckn /beckn/on_update message payload. Sent by a BPP to a BAP in
response to a /beckn/update call (or as an unsolicited update push),
returning the updated contract state.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [Operator](https://schema.beckn.io/Operator/README.md) | v2.0 | An organization that provides and operates public transport or shared mobility services under a defined service agreement. |
| [Order](https://schema.beckn.io/Order/README.md) | v2.0 | Schema definition for Order in the Beckn Protocol |
| [OrderItem](https://schema.beckn.io/OrderItem/README.md) | v2.0 | Schema definition for OrderItem in the Beckn Protocol |
| [Organization](https://schema.beckn.io/Organization/README.md) | v2.0 | An organization such as a company, non-profit, or governmental institution. Modeled after schema.org/Organization. |
| [Package](https://schema.beckn.io/Package/README.md) | v2.0 | A Package is a physical unit of goods prepared for transport within a shipment. Maps to beckn:Item. |
| [Pagination](https://schema.beckn.io/Pagination/README.md) | v2.0 | Pagination metadata returned with list responses

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Participant](https://schema.beckn.io/Participant/README.md) | v2.0 | Container schemas fetched from beckn.yaml. This cannot be extended as it is a reserved schema in beckn protocol. Any additional properties added to this schema can only be made using its *Attributes property |
| [Passenger](https://schema.beckn.io/Passenger/README.md) | v2.0 | A person who travels using a transport service and is identified in a booking or travel document. |
| [PassengerCount](https://schema.beckn.io/PassengerCount/README.md) | v2.0 | The measured number of passengers currently aboard a vehicle, used for real-time capacity and load management. |
| [PassengerGroup](https://schema.beckn.io/PassengerGroup/README.md) | v2.0 | A collection of passengers traveling together as a group, with a group size and a designated lead passenger. |
| [Pathway](https://schema.beckn.io/Pathway/README.md) | v2.0 | A connection between two points within a transit station (e.g., stairway, elevator, walkway) used for indoor navigation and accessibility routing. |
| [Pattern](https://schema.beckn.io/Pattern/README.md) | v2.0 | A unique sequence of stops visited by trips on a route, grouping trips with identical stop sequences and timing structures. |
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
domain schema exists. |
| [Person](https://schema.beckn.io/Person/README.md) | v2.0 | A person (alive, deceased, or fictional). Modeled after schema.org/Person. |
| [PickupDropoffPoint](https://schema.beckn.io/PickupDropoffPoint/README.md) | v2.0 | A designated location used as a pickup or dropoff point for passengers in a ride-hailing or demand-responsive transport service. |
| [PickupPolicy](https://schema.beckn.io/PickupPolicy/README.md) | v2.0 | A set of rules governing the locations and conditions under which passengers may be picked up for a ride-hailing or on-demand transport service. |
| [PlaceRequest](https://schema.beckn.io/PlaceRequest/README.md) | v2.0 | A request for a specific accommodation or seat assignment within a transport service during the booking process. |
| [Plan](https://schema.beckn.io/Plan/README.md) | v2.0 | A journey planning response containing one or more itinerary options for a given trip request. |
| [PlanningResult](https://schema.beckn.io/PlanningResult/README.md) | v2.0 | The output of a MaaS platform planning request, listing available transport options for a requested trip. |
| [Policy](https://schema.beckn.io/Policy/README.md) | v2.0 | Schema definition for Policy in the Beckn Protocol v2.0.1 |
| [PriceSpecification](https://schema.beckn.io/PriceSpecification/README.md) | v2.1 | Schema definition for PriceSpecification in the Beckn Protocol v2.0.1 |
| [ProcessingNotice](https://schema.beckn.io/ProcessingNotice/README.md) | v2.0 | Schema definition for ProcessingNotice in the Beckn Protocol v2.0.1 |
| [Prognosis](https://schema.beckn.io/Prognosis/README.md) | v2.0 | A real-time prediction of a vehicle's arrival or departure time at a stop, including an indication of prediction confidence. |
| [Proof](https://schema.beckn.io/Proof/README.md) | v2.0 | Proof of delivery or pickup evidence, including photos, signatures, OTP confirmations, or digital receipts. Maps to beckn:Document. |
| [Provider](https://schema.beckn.io/Provider/README.md) | v2.1 | Schema definition for Provider in the Beckn Protocol v2.0.1 |
| [PullResultFile](https://schema.beckn.io/PullResultFile/README.md) | v2.0 | JSON body of `GET /catalog/pull/result/{requestId}/catalogs.json`.
Same structure as the inline `catalog` array in the callback payload —
a list of distribution-envelope catalog objects.

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Quantity](https://schema.beckn.io/Quantity/README.md) | v2.0 | Schema definition for Quantity in the Beckn Protocol v2.0.1 |
| [Quay](https://schema.beckn.io/Quay/README.md) | v2.0 | A specific platform, bay, or boarding area within a Stop Place at which passengers board or alight from a vehicle. |
| [Quote](https://schema.beckn.io/Quote/README.md) | v2.0 | A price quote generated by a BPP for a specific selection of offers and fulfillment options. Returned in on_select, on_init, and on_confirm responses. Aggregates item prices, taxes, delivery charges, and discounts into a total. |
| [RateAction](https://schema.beckn.io/RateAction/README.md) | v2.0 | Beckn /beckn/rate message payload. Sent by a BAP to a BPP to submit
one or more rating inputs for entities in a completed contract
(order, fulfillment, item, provider, agent, support).
(Context wrapper stripped; only the message-content portion is inlined.) |
| [Rating](https://schema.beckn.io/Rating/README.md) | v2.1 | Aggregated rating information for an entity. Aligns with schema.org/AggregateRating semantics. |
| [RatingForm](https://schema.beckn.io/RatingForm/README.md) | v2.0 | A form designed to capture rating and feedback from a user. This can be used by both BAP and BPP to fetch ratings and feedback of their respective users. |
| [RatingInput](https://schema.beckn.io/RatingInput/README.md) | v2.1 | A form designed to capture rating and feedback from a user. This can be used by both BAP and BPP to fetch ratings and feedback of their respective users. |
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
| [Resource](https://schema.beckn.io/Resource/README.md) | v2.0 | A minimal, domain-neutral abstraction representing any discoverable, referenceable, or committable unit of value, capability, service, entitlement, or asset within the network.  Examples: - A retail product SKU, a mobility ride, a job role, a carbon credit unit,  a dataset/API entitlement, a training course, a clinic service slot.  Designed for composability through `resourceAttributes` where domain packs can plug in their specific fields without changing the core. |
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
| [RideOption](https://schema.beckn.io/RideOption/README.md) | v2.0 | A specific ride-hailing vehicle category and pricing option presented to a passenger in response to a ride request. |
| [RideRequest](https://schema.beckn.io/RideRequest/README.md) | v2.0 | A passenger's request for an on-demand transport service between two points, specifying origin, destination, and travel preferences. |
| [Rider](https://schema.beckn.io/Rider/README.md) | v2.0 | A person using a shared mobility service (such as a bike-share, scooter, or car-share) who has a registered account with the provider. |
| [RiderCategory](https://schema.beckn.io/RiderCategory/README.md) | v2.0 | A classification of passenger type (e.g., adult, child, senior, student) used to determine applicable fare entitlements. |
| [Route](https://schema.beckn.io/Route/README.md) | v2.0 | The physical or logical path followed by a transport service, defined as an ordered sequence of stops or waypoints. |
| [SafetyPolicy](https://schema.beckn.io/SafetyPolicy/README.md) | v2.0 | A set of rules, protocols, and standards governing safety requirements for drivers, vehicles, and passengers on a mobility platform. |
| [SalesOfferPackage](https://schema.beckn.io/SalesOfferPackage/README.md) | v2.0 | A combination of one or more fare products bundled for sale through a specific distribution channel. |
| [Seat](https://schema.beckn.io/Seat/README.md) | v2.0 | A specific seat position reserved or assigned to a passenger on a flight, train, or other transport service. |
| [Segment](https://schema.beckn.io/Segment/README.md) | v2.0 | A portion of a rail journey operated continuously by a single carrier between two consecutive stops or stations. |
| [SelectAction](https://schema.beckn.io/SelectAction/README.md) | v2.0 | Beckn /beckn/select message payload. Sent by a BAP to a BPP to select
items and offers from a catalog, initiating the negotiation cycle.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [ServerError](https://schema.beckn.io/ServerError/README.md) | v2.0 | Internal failure on the network participant's application; the request could not be processed. The response body MAY contain an `error` object with additional details. |
| [ServiceCalendar](https://schema.beckn.io/ServiceCalendar/README.md) | v2.0 | A schedule defining on which dates a transport service operates, including regular service days and exceptional dates. |
| [ServiceClass](https://schema.beckn.io/ServiceClass/README.md) | v2.0 | A classification of the level of service offered by a transport service, such as economy, business, or first class. |
| [ServiceDelivery](https://schema.beckn.io/ServiceDelivery/README.md) | v2.0 | The top-level response container in SIRI encapsulating one or more real-time data delivery types. |
| [Settlement](https://schema.beckn.io/Settlement/README.md) | v2.0 | Container schemas fetched from beckn.yaml. This cannot be extended as it is a reserved schema in beckn protocol. Any additional properties added to this schema can only be made using its *Attributes property |
| [SettlementSchedule](https://schema.beckn.io/SettlementSchedule/README.md) | v2.0 | Schema definition for SettlementSchedule in the Beckn Protocol v2.0.1 |
| [SettlementTerm](https://schema.beckn.io/SettlementTerm/README.md) | v2.0 | Describes the terms of settlement associated with a given transaction. This is not to be confused with the PaymentAction as it describes all the places where the money gets disbursed after reconciliation. |
| [Shape](https://schema.beckn.io/Shape/README.md) | v2.0 | The geographic path traced by a vehicle along a route, represented as an ordered sequence of geographic coordinates. |
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
| [SpatialConstraint](https://schema.beckn.io/SpatialConstraint/README.md) | v2.0 | **Spatial predicate** using **OGC CQL2 (JSON semantics)** applied to one or more geometry targets in an item. This is where clients express spatial intent. Key ideas: - `targets`: one or more **JSONPath-like** pointers that locate geometry    fields within each item document (e.g., `$['availableAt'][*]['geo']`). - `op`: spatial operator (CQL2). Common ones:      • `S_WITHIN`     (A is completely inside B)     • `S_INTERSECTS` (A intersects B)     • `S_CONTAINS`   (A contains B)     • `S_DWITHIN`    (A within distance of B) - `geometry`: **GeoJSON** literal used as the predicate reference geometry. - `distanceMeters`: required for `S_DWITHIN` when using a GeoJSON Point/shape. - `quantifier`: if a target resolves to an array, choose whether **ANY** (default),    **ALL**, or **NONE** of elements must satisfy the predicate.  CRS: unless otherwise stated, all coordinates are **EPSG:4326**. |
| [State](https://schema.beckn.io/State/README.md) | v2.0 | Schema definition for State in the Beckn Protocol v2.0.1 |
| [Station](https://schema.beckn.io/Station/README.md) | v2.0 | A major transit facility serving as a hub for one or more transport modes, typically offering waiting areas, ticketing, and interchange facilities. |
| [StationInformation](https://schema.beckn.io/StationInformation/README.md) | v2.0 | Static descriptive information about a shared mobility docking station, including its location, capacity, and features. |
| [StationStatus](https://schema.beckn.io/StationStatus/README.md) | v2.0 | The real-time operational state of a shared mobility station, including the number of available docks and vehicles. |
| [StatusAction](https://schema.beckn.io/StatusAction/README.md) | v2.0 | Beckn /beckn/status message payload. Sent by a BAP to a BPP to query
the current state of a contract/order by its identifier.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [Stop](https://schema.beckn.io/Stop/README.md) | v2.0 | A designated location where vehicles stop to allow passengers to board or alight from a transport service. |
| [StopArea](https://schema.beckn.io/StopArea/README.md) | v2.0 | A group of stops that collectively define a zone from which a demand-responsive service may pick up or drop off passengers. |
| [StopEvent](https://schema.beckn.io/StopEvent/README.md) | v2.0 | A departure or arrival event at a stop, used to retrieve the next or previous vehicle movements at a specific location. |
| [StopMonitoring](https://schema.beckn.io/StopMonitoring/README.md) | v2.0 | A real-time data service providing predicted arrivals and departures of vehicles at a specific stop. |
| [StopPlace](https://schema.beckn.io/StopPlace/README.md) | v2.0 | A physical location serving as a transit stop facility, comprising one or more quays, entrances, and associated infrastructure. |
| [StopPoint](https://schema.beckn.io/StopPoint/README.md) | v2.0 | An abstract or scheduled point in a public transport network at which passengers can board or alight from a service. |
| [StopTime](https://schema.beckn.io/StopTime/README.md) | v2.0 | The scheduled arrival and departure times for a vehicle at a specific stop within a vehicle journey. |
| [StopTimeUpdate](https://schema.beckn.io/StopTimeUpdate/README.md) | v2.0 | A real-time update to the predicted arrival or departure time of a vehicle at a specific stop within a journey. |
| [Support](https://schema.beckn.io/Support/README.md) | v2.0 | Describes a support session info |
| [SupportAction](https://schema.beckn.io/SupportAction/README.md) | v2.0 | Beckn /beckn/support message payload. Sent by a BAP to a BPP to request
support contact information or to open a support ticket for an existing
order/contract.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [SupportInfo](https://schema.beckn.io/SupportInfo/README.md) | v2.1 | Canonical support contact for an entity, mapped to schema.org ContactPoint. |
| [SupportRequest](https://schema.beckn.io/SupportRequest/README.md) | v2.0 | Support request by a user. If no field is set, the user can expect a public support contact info |
| [SupportResponse](https://schema.beckn.io/SupportResponse/README.md) | v2.0 | Support response payload returned by a BPP to a BAP in the /beckn/on_support callback. Contains the support ticket reference, available contact channels, SLA commitment, and optional consumer acknowledgement details. |
| [SupportTicket](https://schema.beckn.io/SupportTicket/README.md) | v2.0 | A support ticket raised against an order |
| [SurgeMultiplier](https://schema.beckn.io/SurgeMultiplier/README.md) | v2.0 | A dynamic pricing factor applied during periods of high demand that increases base fares proportionally to balance supply and demand. |
| [SystemPricingPlan](https://schema.beckn.io/SystemPricingPlan/README.md) | v2.0 | A pricing plan defined by a shared mobility system, describing costs and billing rules for vehicle use. |
| [TariffZone](https://schema.beckn.io/TariffZone/README.md) | v2.0 | A geographic zone used to define and apply fare structures, within which a single fare or set of rules applies. |
| [Ticket](https://schema.beckn.io/Ticket/README.md) | v2.0 | A document or digital record granting the holder the right to travel on a specific transport service or within a defined validity scope. |
| [Time](https://schema.beckn.io/Time/README.md) | v2.0 | Represents a moment or duration in time. Can express a timestamp, a duration, or a time range. |
| [TimePeriod](https://schema.beckn.io/TimePeriod/README.md) | v2.1 | Time window with date-time precision for availability/validity

This schema is part of the Long Term Support of Beckn Protocol V2.0 API specification and MUST NOT be extended. Any domain-specific extension must use the property of this schema which is of type Attribute. |
| [Timetable](https://schema.beckn.io/Timetable/README.md) | v2.0 | A structured schedule listing planned arrival and departure times for vehicles at each stop along a route. |
| [TrackAction](https://schema.beckn.io/TrackAction/README.md) | v2.1 | Details required to initiate real-time tracking (if relevant) for an ongoing transaction |
| [Tracking](https://schema.beckn.io/Tracking/README.md) | v2.1 | Information regarding live tracking of the fufillment of a contract |
| [TrackingRequest](https://schema.beckn.io/TrackingRequest/README.md) | v2.0 | Schema definition for TrackingRequest in the Beckn Protocol v2.0.1 |
| [TrackingUpdate](https://schema.beckn.io/TrackingUpdate/README.md) | v2.0 | A TrackingUpdate is a real-time or periodic update on the status and location of a shipment during transit. Maps to beckn:Event. |
| [TransactionEndpoint](https://schema.beckn.io/TransactionEndpoint/README.md) | v2.0 | Beckn protocol transaction endpoint identifier. |
| [Transfer](https://schema.beckn.io/Transfer/README.md) | v2.0 | A defined connection rule between two routes or services at a common stop, specifying minimum transfer time or transfer type. |
| [TransportObject](https://schema.beckn.io/TransportObject/README.md) | v2.0 | A generic transport entity in the OSLO mobility ontology representing any object involved in transport operations. |
| [TravelDocument](https://schema.beckn.io/TravelDocument/README.md) | v2.0 | A document (physical or digital) issued to a passenger proving entitlement to travel, used for validation or inspection. |
| [Trip](https://schema.beckn.io/Trip/README.md) | v2.0 | A confirmed and booked journey from an origin to a destination, representing a completed mobility service order. |
| [TripDescriptor](https://schema.beckn.io/TripDescriptor/README.md) | v2.0 | An identifier that uniquely references a specific vehicle journey in a real-time transit feed. |
| [TripRequest](https://schema.beckn.io/TripRequest/README.md) | v2.0 | A request submitted to a journey planning system specifying origin, destination, travel time, and preferences. |
| [TripResult](https://schema.beckn.io/TripResult/README.md) | v2.0 | The result of a trip planning request, containing one or more journey options with leg details and timing. |
| [TripSpecification](https://schema.beckn.io/TripSpecification/README.md) | v2.0 | A description of the desired journey used as input to search and price transport options. |
| [TripUpdate](https://schema.beckn.io/TripUpdate/README.md) | v2.0 | A multi-dimensional update to an in-progress or upcoming mobility trip, covering contract modifications (added/removed services, route changes), status notifications (driver arriving, trip started), and real-time tracking endpoint information. |
| [UpdateAction](https://schema.beckn.io/UpdateAction/README.md) | v2.0 | Beckn /beckn/update message payload. Sent by a BAP to a BPP to request
changes to an active contract (e.g., update fulfillment address, add items,
change quantities). The context.try flag must be true during negotiation.
(Context wrapper stripped; only the message-content portion is inlined.) |
| [Vehicle](https://schema.beckn.io/Vehicle/README.md) | v2.0 | A motorized or human-powered mobility asset used to carry passengers or goods between locations. |
| [VehicleCategory](https://schema.beckn.io/VehicleCategory/README.md) | v2.0 | A broad classification of vehicles by their physical type, such as two-wheeler, three-wheeler, four-wheeler, or bus. |
| [VehicleDescriptor](https://schema.beckn.io/VehicleDescriptor/README.md) | v2.0 | An identifier that uniquely references a specific vehicle in a real-time transit feed. |
| [VehicleJourney](https://schema.beckn.io/VehicleJourney/README.md) | v2.0 | A specific operational instance of a vehicle traveling a defined route at a scheduled time on a given service day. |
| [VehicleMonitoringDelivery](https://schema.beckn.io/VehicleMonitoringDelivery/README.md) | v2.0 | A real-time data delivery providing current positions and operational states of a set of vehicles. |
| [VehiclePosition](https://schema.beckn.io/VehiclePosition/README.md) | v2.0 | The current real-time geographic position, bearing, and speed of a vehicle operating a transport service. |
| [VehicleStatus](https://schema.beckn.io/VehicleStatus/README.md) | v2.0 | The real-time operational state of a vehicle or mobility asset, such as available, in use, reserved, or disabled. |
| [VehicleType](https://schema.beckn.io/VehicleType/README.md) | v2.0 | A class or category of vehicle defined by its mode of transport, capacity, propulsion type, and accessibility features. |
| [VerificationSummary](https://schema.beckn.io/VerificationSummary/README.md) | v2.1 | Summary of a credential verification check. Contains the overall result, reason codes for any failures, and which credential categories were successfully verified. No VC or VP payloads are included. |
| [WaitingPolicy](https://schema.beckn.io/WaitingPolicy/README.md) | v2.0 | Rules governing the maximum time a driver is required to wait for a passenger at the pickup location before being permitted to cancel the booking. |
| [Waypoint](https://schema.beckn.io/Waypoint/README.md) | v2.0 | A Waypoint is an intermediate stop or checkpoint on a logistics route, such as a sorting hub, relay station, or customs checkpoint. Maps to beckn:Stop. |
