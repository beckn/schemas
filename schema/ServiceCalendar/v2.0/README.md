# ServiceCalendar — v2.0

A schedule defining on which dates a transport service operates, including regular service days and exceptional dates.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/ServiceCalendar/attributes.yaml](https://schema.beckn.io/ServiceCalendar/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/ServiceCalendar/v2.0/attributes.yaml](https://schema.beckn.io/ServiceCalendar/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/ServiceCalendar/attributes.jsonschema.yaml](https://schema.beckn.io/ServiceCalendar/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/ServiceCalendar/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/ServiceCalendar/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/ServiceCalendar/context.jsonld](https://schema.beckn.io/ServiceCalendar/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/ServiceCalendar/v2.0/context.jsonld](https://schema.beckn.io/ServiceCalendar/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/ServiceCalendar/vocab.jsonld](https://schema.beckn.io/ServiceCalendar/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/ServiceCalendar/v2.0/vocab.jsonld](https://schema.beckn.io/ServiceCalendar/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `serviceId` | no | string | Unique identifier for the service calendar |
| `monday` | no | boolean | Whether service operates on Mondays |
| `tuesday` | no | boolean | Whether service operates on Tuesdays |
| `wednesday` | no | boolean | Whether service operates on Wednesdays |
| `thursday` | no | boolean | Whether service operates on Thursdays |
| `friday` | no | boolean | Whether service operates on Fridays |
| `saturday` | no | boolean | Whether service operates on Saturdays |
| `sunday` | no | boolean | Whether service operates on Sundays |
| `exceptionDates` | no | string | Dates on which service is added or removed from the regular schedule |
| `startDate` | no | string | Start date and time of the period |
| `endDate` | no | string | End date and time of the period |
| `startTime` | no | string | Start time of day in HH:MM:SS format |
| `endTime` | no | string | End time of day in HH:MM:SS format |
