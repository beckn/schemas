# MonitoredVehicleJourney — v2.0

A real-time representation of a vehicle journey being actively tracked, including position and schedule adherence data.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/MonitoredVehicleJourney/attributes.yaml](https://schema.beckn.io/MonitoredVehicleJourney/attributes.yaml) | OpenAPI schema envelope (latest path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/v2.0/attributes.yaml](https://schema.beckn.io/MonitoredVehicleJourney/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/attributes.jsonschema.yaml](https://schema.beckn.io/MonitoredVehicleJourney/attributes.jsonschema.yaml) | JSON Schema document (latest path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/v2.0/attributes.jsonschema.yaml](https://schema.beckn.io/MonitoredVehicleJourney/v2.0/attributes.jsonschema.yaml) | JSON Schema document (versioned path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/context.jsonld](https://schema.beckn.io/MonitoredVehicleJourney/context.jsonld) | JSON-LD context (latest path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/v2.0/context.jsonld](https://schema.beckn.io/MonitoredVehicleJourney/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/vocab.jsonld](https://schema.beckn.io/MonitoredVehicleJourney/vocab.jsonld) | RDF vocabulary (latest path) |
| [https://schema.beckn.io/MonitoredVehicleJourney/v2.0/vocab.jsonld](https://schema.beckn.io/MonitoredVehicleJourney/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `lineRef` | no | $ref: https://schema.beckn.io/Line/v2.0/attributes.yaml#/components/schemas/Line | Reference to the line being monitored |
| `directionRef` | no | $ref: https://schema.beckn.io/Direction/v2.0/attributes.yaml#/components/schemas/Direction | Direction of travel being monitored |
| `vehicleRef` | no | $ref: https://schema.beckn.io/Vehicle/v2.0/attributes.yaml#/components/schemas/Vehicle | Vehicle assigned to this journey |
| `vehicleLocation` | no | $ref: https://schema.beckn.io/VehiclePosition/v2.0/attributes.yaml#/components/schemas/VehiclePosition | Current geographic position of the vehicle |
| `bearing` | no | number | Compass bearing of travel in degrees |
| `delay` | no | number | Delay in seconds relative to schedule (negative = early) |
| `occupancy` | no | $ref: https://schema.beckn.io/OccupancyStatus/v2.0/attributes.yaml#/components/schemas/OccupancyStatus | Current passenger occupancy of the vehicle |
| `vehicleJourneyCode` | no | string | Unique code for this vehicle journey |
| `routeRef` | no | $ref: https://schema.beckn.io/Route/v2.0/attributes.yaml#/components/schemas/Route | Reference to the route being served |
| `serviceCalendarRef` | no | $ref: https://schema.beckn.io/ServiceCalendar/v2.0/attributes.yaml#/components/schemas/ServiceCalendar | Calendar defining when this journey operates |
| `patternRef` | no | $ref: https://schema.beckn.io/Pattern/v2.0/attributes.yaml#/components/schemas/Pattern | Journey pattern being followed |
| `stopTimes` | no | $ref: https://schema.beckn.io/StopTime/v2.0/attributes.yaml#/components/schemas/StopTime | Scheduled stop times for each stop on this journey |
