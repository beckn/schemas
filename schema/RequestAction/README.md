# Request Action

DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). The request/callback distinction is encoded in context.action (e.g. beckn/discover for requests, beckn/on_discover for callbacks). This schema will be removed in a future major version.

Part of the [Beckn Protocol Core Schema](../../README.md)

## Versions

| Version | Status |
|---------|--------|
| [v2.0](./v2.0/README.md) | Current |
