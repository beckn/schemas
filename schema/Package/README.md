# Package

## Overview
The **Package** entity describes a physical unit of goods prepared for transport. Each shipment may contain one or more packages with distinct weights, dimensions, and handling requirements.

## IRI
`https://schema.beckn.org/logistics/Package`

## Beckn Core Mapping
| Logistics Concept | Beckn Core | Relationship |
|---|---|---|
| Package | Item | `owl:equivalentClass` |

## Key Attributes
| Attribute | Type | Description |
|---|---|---|
| id | string | Unique package ID |
| weight | object | Weight with unit |
| dimensions | object | L x W x H |
| fragile | boolean | Fragile handling flag |
| hazardous | boolean | Hazardous material flag |
| declaredValue | object | Insured value |
| packageType | enum | BOX / ENVELOPE / PALLET etc. |
| temperatureControl | object | Cold chain requirements |

## Version
Current version: **v2.0** — [v2.0/attributes.yaml](./v2.0/attributes.yaml)
