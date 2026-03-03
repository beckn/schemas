# Shipment

## Overview

The **Shipment** entity is the core fulfillment object in the Beckn Logistics domain. It represents the complete lifecycle of moving goods from a pickup point to a delivery destination.

## IRI
`https://schema.beckn.org/logistics/Shipment`

## Beckn Core Mapping
| Logistics Concept | Beckn Core | Relationship |
|---|---|---|
| Shipment | Fulfillment | `owl:equivalentClass` |
| Shipment | Order | `skos:broadMatch` |

## Use Cases
- Hyperlocal Delivery: A grocery delivery from a dark store to a customer within 30 minutes
- Courier: A parcel booked for next-day delivery
- Interstate: A cargo consignment moving across state borders
- Long Haul: A truck-load shipment from Mumbai to Delhi
- Express: A time-critical document requiring same-day guaranteed delivery

## Key Attributes
| Attribute | Type | Description |
|---|---|---|
| id | string | Unique shipment identifier |
| trackingId | string | Public tracking number |
| status | enum | Current shipment status |
| origin | Place | Pickup location |
| destination | Place | Delivery location |
| serviceType | enum | HYPERLOCAL / COURIER / INTERSTATE / LONG_HAUL / EXPRESS |
| estimatedDelivery | dateTime | EDD |
| driver | Driver | Assigned driver |
| vehicle | Vehicle | Assigned vehicle |

## Version
Current version: **v2.0**

## Schema File
[v2.0/attributes.yaml](./v2.0/attributes.yaml)
