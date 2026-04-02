# DayType — v2.0

A classification of a day (e.g., weekday, weekend, public holiday) used to define when a service pattern is valid.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/DayType/attributes.yaml](https://schema.beckn.io/DayType/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/DayType/v2.0/attributes.yaml](https://schema.beckn.io/DayType/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/DayType/attributes.jsonschema.yaml](https://schema.beckn.io/DayType/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/DayType/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/DayType/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/DayType/context.jsonld](https://schema.beckn.io/DayType/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/DayType/v2.0/context.jsonld](https://schema.beckn.io/DayType/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/DayType/vocab.jsonld](https://schema.beckn.io/DayType/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/DayType/v2.0/vocab.jsonld](https://schema.beckn.io/DayType/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `dayTypeCode` | no | string | Code identifying the day type (e.g. WEEKDAY, WEEKEND, HOLIDAY) |
| `daysOfWeek` | no | array | List of days of the week applicable to this day type |
| `startDate` | no | string | Start date and time of the period |
| `endDate` | no | string | End date and time of the period |
| `startTime` | no | string | Start time of day in HH:MM:SS format |
| `endTime` | no | string | End time of day in HH:MM:SS format |
