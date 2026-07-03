# CandidateAvailabilityOffer — v2.1

**Container:** `offerAttributes`  
**Protocol version:** Beckn v2.1 Generalised  
**Schema version:** 2.1.0  
**Status:** Active

## v2.1 Release Notes

Initial v2.1 release using generalised offerAttributes container.

## Files

| File | Description |
|------|-------------|
| `attributes.yaml` | OpenAPI 3.1.1 schema definition with x-beckn-container and x-jsonld-id annotations |
| `context.jsonld` | JSON-LD context — declares all prefixes; self-contained (no @import) |
| `vocab.jsonld` | Controlled vocabulary for domain-specific enumerated types |
| `profile.json` | Discovery and indexing configuration |
| `renderer.json` | UI rendering hints |
| `examples/` | Example JSON payloads |

## JSON-LD Context

This schema uses a self-contained `context.jsonld` that declares:
- `schema`: `https://schema.org/`
- `beckn`: `https://schema.beckn.io/`
- Per-schema prefix pointing to `https://schema.beckn.io/CandidateAvailabilityOffer#`

No `@import` is used — all prefixes are declared directly.

## Testing

Run the Beckn v2.1 schema tester from the `hiring-candidates/` directory:

```bash
cd hiring-candidates/
python3 tests/run_tests.py
```
