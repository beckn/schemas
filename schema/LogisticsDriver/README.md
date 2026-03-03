# Driver

## Overview
A **Driver** is an individual who operates a vehicle for logistics delivery. Drivers are assigned shipments and are responsible for pickup, transit, and delivery.

## IRI
`https://schema.beckn.org/logistics/Driver`

## Use Cases
- All logistics use cases: Hyperlocal, Courier, Interstate, Long Haul, Express

## Key Attributes
| Attribute | Type | Description |
|---|---|---|
| id | string | Unique driver ID |
| name | string | Driver full name |
| licenseNumber | string | Driving license |
| rating | number | Average driver rating |
| currentLocation | object | Real-time GPS coordinates |
| status | enum | AVAILABLE / ON_ROUTE etc. |
| backgroundVerified | boolean | Verification status |

## Version
Current version: **v2.0** — [v2.0/attributes.yaml](./v2.0/attributes.yaml)
