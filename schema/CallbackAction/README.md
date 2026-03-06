# Callback Action

DEPRECATED. This schema is structurally invalid and does not validate any payloads — the oneOf keyword was incorrectly nested inside properties, which is not valid JSON Schema. The $id also lacked a version segment. Use https://schema.beckn.io/BecknAction/v2.0 instead. BecknAction is the unified envelope for all Beckn actions (both request and callback directions). Callback actions are those with on_ prefixed endpoints (e.g. beckn/on_discover, beckn/on_confirm) and are validated by the same BecknAction schema via if/then dispatch on context.action. This schema will be removed in a future major version.

Part of the [Beckn Protocol Core Schema](../../README.md)

## Versions

| Version | Status |
|---------|--------|
| [v2.0](./v2.0/README.md) | Current |
