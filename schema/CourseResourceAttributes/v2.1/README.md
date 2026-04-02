# CourseResourceAttributes — v2.1

Intrinsic attributes of a training course or program Resource. Domain-generic: applicable to any skilling vertical — vocational training, professional certification, higher education, government skill schemes, etc.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/CourseResourceAttributes/attributes.yaml](https://schema.beckn.io/CourseResourceAttributes/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/CourseResourceAttributes/v2.1/attributes.yaml](https://schema.beckn.io/CourseResourceAttributes/v2.1/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/CourseResourceAttributes/attributes.jsonschema.yaml](https://schema.beckn.io/CourseResourceAttributes/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/CourseResourceAttributes/v2.1/attributes.jsonschema.yaml](https://schema.beckn.io/CourseResourceAttributes/v2.1/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/CourseResourceAttributes/context.jsonld](https://schema.beckn.io/CourseResourceAttributes/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/CourseResourceAttributes/v2.1/context.jsonld](https://schema.beckn.io/CourseResourceAttributes/v2.1/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/CourseResourceAttributes/vocab.jsonld](https://schema.beckn.io/CourseResourceAttributes/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/CourseResourceAttributes/v2.1/vocab.jsonld](https://schema.beckn.io/CourseResourceAttributes/v2.1/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `course_level` | no | string | Difficulty or qualification level of the course. |
| `course_domain` | no | $ref: https://schema.beckn.io/CodedValue/v2.1/attributes.yaml#/components/schemas/CodedValue | Subject domain of the course, expressed using an authority-governed code system (e.g. UNESCO ISCED, India NSQF sector codes).  |
| `delivery_mode` | no | string | How the course is delivered. |
| `duration` | no | string | Total course duration in ISO 8601 duration format. Examples: "P3W" (3 weeks), "PT40H" (40 hours), "P6M" (6 months).  |
| `location` | no | object | Physical location for ONSITE or HYBRID courses. |
| `capacity` | no | integer | Maximum number of learners per cohort or batch. |
| `schedule` | no | object | Cohort or batch schedule details. |
| `prerequisites` | no | array | Credential prerequisites the enrollee must satisfy. Uses the shared CredentialRequirement type.  |
| `outcome_credential` | no | object | The credential issued to a learner on successful course completion. Placed in resourceAttributes because it is intrinsic to the course and required at discovery time (learners search by intended outcome).  |
| `industry_type` | no | $ref: https://schema.beckn.io/CodedValue/v2.1/attributes.yaml#/components/schemas/CodedValue | Industry alignment of the course (optional). |
