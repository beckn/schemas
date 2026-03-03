# Consignment

## Overview
A **Consignment** groups multiple packages or shipments under a single commercial transaction between a shipper and consignee. Commonly identified by an Air Waybill (AWB) number in courier and freight contexts.

## IRI
`https://schema.beckn.org/logistics/Consignment`

## Beckn Core Mapping
| Logistics Concept | Beckn Core | Relationship |
|---|---|---|
| Consignment | Order | `owl:equivalentClass` |

## Use Cases
- Courier: Multiple parcels booked by a business for multiple recipients
- Interstate: Freight consignment with AWB number
- Long Haul: Full truck load with customs documentation

## Version
Current version: **v2.0** — [v2.0/attributes.yaml](./v2.0/attributes.yaml)
