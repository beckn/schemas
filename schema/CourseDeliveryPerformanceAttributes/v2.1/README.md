# CourseDeliveryPerformanceAttributes — v2.1

Beckn v2.1 extension schema for the performanceAttributes container. Captures course delivery execution details: delivery URL (for ACCESS mode), session schedule (for SERVICE mode), attendance tracking, completion criteria, completion status, and issued credential reference.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/attributes.yaml](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/attributes.yaml](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/context.jsonld](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/context.jsonld](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/vocab.jsonld](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/CourseDeliveryPerformanceAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `delivery_url` | no | string | LMS or content platform URL for ACCESS mode courses. |
| `session_schedule` | no | array | Scheduled live sessions for SERVICE mode courses. |
| `attendance_tracking` | no | boolean | Whether attendance is formally tracked for this course. |
| `completion_criteria` | no | object | Criteria that must be met for the learner to be eligible for credential issuance. |
| `completion_status` | no | string | Current completion state for the enrolled learner. |
| `issued_credential_ref` | no | string | Reference to the VC issued upon course completion. Only populated after completion_status = COMPLETED and VC issuance succeeds.  |
