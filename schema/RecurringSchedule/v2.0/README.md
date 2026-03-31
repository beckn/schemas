# RecurringSchedule — v2.0

Defines a recurring temporal schedule such as operating hours or serviceability timing windows. Supports day-based recurrence and optional holiday exclusions.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/RecurringSchedule/attributes.yaml](https://schema.beckn.io/RecurringSchedule/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/RecurringSchedule/v2.0/attributes.yaml](https://schema.beckn.io/RecurringSchedule/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/RecurringSchedule/attributes.jsonschema.yaml](https://schema.beckn.io/RecurringSchedule/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/RecurringSchedule/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/RecurringSchedule/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/RecurringSchedule/context.jsonld](https://schema.beckn.io/RecurringSchedule/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/RecurringSchedule/v2.0/context.jsonld](https://schema.beckn.io/RecurringSchedule/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/RecurringSchedule/vocab.jsonld](https://schema.beckn.io/RecurringSchedule/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/RecurringSchedule/v2.0/vocab.jsonld](https://schema.beckn.io/RecurringSchedule/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `days` | no | array | Days of week on which the schedule applies. |
| `timeRange` | no | object | Daily time window for applicable days. |
| `holidays` | no | array | Specific dates excluded from this schedule. |
| `timezone` | no | string | IANA timezone identifier (e.g., Asia/Kolkata). |
