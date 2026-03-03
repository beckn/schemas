# Vehicle

## Overview
A **Vehicle** is a transport asset used across all logistics use cases, from bicycles for last-mile delivery to heavy trucks for long haul freight.

## IRI
`https://schema.beckn.org/logistics/Vehicle`

## Use Cases
- Hyperlocal: Bicycle, e-scooter, motorcycle
- Courier: Van, mini-truck
- Interstate/Long Haul: HCV trucks, container trucks, trailers
- Express: Motorcycles, cars, vans

## Key Attributes
| Attribute | Type | Description |
|---|---|---|
| type | enum | Vehicle category |
| payloadCapacity | object | Max cargo weight |
| hasRefrigeration | boolean | Cold chain capability |
| gpsEnabled | boolean | Real-time tracking |
| currentLocation | object | Live GPS with speed |

## Version
Current version: **v2.0** — [v2.0/attributes.yaml](./v2.0/attributes.yaml)
