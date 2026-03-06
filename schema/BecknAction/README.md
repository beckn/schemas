# Beckn Action

Unified Beckn action envelope. All Beckn API requests and callbacks conform to this schema. The context identifies the action being performed; the message carries the action-specific payload. Message content is validated via if/then dispatch based on context.action. For unknown or extension endpoints, no if/then branch applies and message remains unconstrained. This schema supersedes RequestAction and CallbackAction, both of which were structurally invalid. The request/callback distinction is encoded in the context.action value (e.g. beckn/discover vs beckn/on_discover), not in a separate schema type.

Part of the [Beckn Protocol Core Schema](../../README.md)

## Versions

| Version | Status |
|---------|--------|
| [v2.0](./v2.0/README.md) | Current |
