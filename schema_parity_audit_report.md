# Strict Schema Parity Audit (Property-Set Only)

Source of truth: `/home/ravi/www/spec_work/protocol-specifications-v2/api/v2.0.0/beckn.yaml`

## Scope and Rules
- Scope: only `components.schemas` in `beckn.yaml`
- Comparison: property sets only (effective properties via `properties` + composed branches)
- `$ref` handling: local refs resolved for effective property extraction; non-property metadata ignored

## Summary
- Total schemas in beckn.yaml scope: **69**
- Matched in @/schema: **69**
- Missing in @/schema: **0**
- Mismatched schemas: **36**
- Verdict: **FAIL**

## Mismatched Schemas Only
### AckNoCallback
- Schema file: `schema/AckNoCallback/v2.0/schema.json`
- Missing in schema (present in beckn): signature, status
- Extra in schema (absent in beckn): (none)

### AddOn
- Schema file: `schema/AddOn/v2.0/schema.json`
- Missing in schema (present in beckn): addOns, availableTo, considerationIds, descriptor, fulfillmentIds, id, offerAttributes, provider, resourceAttributes, resourceIds, validity
- Extra in schema (absent in beckn): (none)

### AsyncError
- Schema file: `schema/AsyncError/v2.0/schema.json`
- Missing in schema (present in beckn): errorCode, errorMessage
- Extra in schema (absent in beckn): (none)

### CancelAction
- Schema file: `schema/CancelAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### CatalogProcessingResult
- Schema file: `schema/CatalogProcessingResult/v2.0/schema.json`
- Missing in schema (present in beckn): errors, stats
- Extra in schema (absent in beckn): error, itemCount, warnings

### CatalogPublishAction
- Schema file: `schema/CatalogPublishAction/v2.0/schema.json`
- Missing in schema (present in beckn): catalogs
- Extra in schema (absent in beckn): context, message

### ConfirmAction
- Schema file: `schema/ConfirmAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### Context
- Schema file: `schema/Context/v2.0/schema.json`
- Missing in schema (present in beckn): domain, key, location, requestDigest, schemaContext
- Extra in schema (absent in beckn): lineage, try

### Contract
- Schema file: `schema/Contract/v2.0/schema.json`
- Missing in schema (present in beckn): commitments, consideration, contractAttributes, descriptor, performance, settlements
- Extra in schema (absent in beckn): @context, @type, contractValue, displayId, entitlements, fulfillments, items

### DiscoverAction
- Schema file: `schema/DiscoverAction/v2.0/schema.json`
- Missing in schema (present in beckn): intent, textSearch, text_search
- Extra in schema (absent in beckn): context, message

### Error
- Schema file: `schema/Error/v2.0/schema.json`
- Missing in schema (present in beckn): errorCode, errorMessage
- Extra in schema (absent in beckn): code, details, message

### InitAction
- Schema file: `schema/InitAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### Intent
- Schema file: `schema/Intent/v2.0/schema.json`
- Missing in schema (present in beckn): mediaSearch
- Extra in schema (absent in beckn): media_search, text_search

### Location
- Schema file: `schema/Location/v2.0/schema.json`
- Missing in schema (present in beckn): (none)
- Extra in schema (absent in beckn): @type

### MediaSearchOptions
- Schema file: `schema/MediaSearchOptions/v2.0/schema.json`
- Missing in schema (present in beckn): augment_text_search, restrict_results_to_media_proximity
- Extra in schema (absent in beckn): augmentTextSearch, restrictResultsToMediaProximity

### NackBadRequest
- Schema file: `schema/NackBadRequest/v2.0/schema.json`
- Missing in schema (present in beckn): signature
- Extra in schema (absent in beckn): (none)

### NackUnauthorized
- Schema file: `schema/NackUnauthorized/v2.0/schema.json`
- Missing in schema (present in beckn): signature
- Extra in schema (absent in beckn): (none)

### OnCancelAction
- Schema file: `schema/OnCancelAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### OnConfirmAction
- Schema file: `schema/OnConfirmAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### OnDiscoverAction
- Schema file: `schema/OnDiscoverAction/v2.0/schema.json`
- Missing in schema (present in beckn): catalogs
- Extra in schema (absent in beckn): context, message

### OnInitAction
- Schema file: `schema/OnInitAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### OnRateAction
- Schema file: `schema/OnRateAction/v2.0/schema.json`
- Missing in schema (present in beckn): ratings
- Extra in schema (absent in beckn): context, message

### OnSelectAction
- Schema file: `schema/OnSelectAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### OnStatusAction
- Schema file: `schema/OnStatusAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### OnSupportAction
- Schema file: `schema/OnSupportAction/v2.0/schema.json`
- Missing in schema (present in beckn): support
- Extra in schema (absent in beckn): context, message

### OnTrackAction
- Schema file: `schema/OnTrackAction/v2.0/schema.json`
- Missing in schema (present in beckn): tracking
- Extra in schema (absent in beckn): context, message

### OnUpdateAction
- Schema file: `schema/OnUpdateAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### Participant
- Schema file: `schema/Participant/v2.0/schema.json`
- Missing in schema (present in beckn): descriptor, participantAttributes
- Extra in schema (absent in beckn): @context, @type, credentials, displayName, email, rating, skills, telephone

### RateAction
- Schema file: `schema/RateAction/v2.0/schema.json`
- Missing in schema (present in beckn): ratingInputs
- Extra in schema (absent in beckn): context, message

### SelectAction
- Schema file: `schema/SelectAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### StatusAction
- Schema file: `schema/StatusAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message

### Support
- Schema file: `schema/Support/v2.0/schema.json`
- Missing in schema (present in beckn): channels, descriptor
- Extra in schema (absent in beckn): @context, @type, callbackPhone, issue, issueCode, ticketIds

### SupportAction
- Schema file: `schema/SupportAction/v2.0/schema.json`
- Missing in schema (present in beckn): support
- Extra in schema (absent in beckn): context, message

### TrackAction
- Schema file: `schema/TrackAction/v2.1/schema.json`
- Missing in schema (present in beckn): tracking
- Extra in schema (absent in beckn): (none)

### Tracking
- Schema file: `schema/Tracking/v2.1/schema.json`
- Missing in schema (present in beckn): contract, trackingAttributes
- Extra in schema (absent in beckn): refId

### UpdateAction
- Schema file: `schema/UpdateAction/v2.0/schema.json`
- Missing in schema (present in beckn): contract
- Extra in schema (absent in beckn): context, message
