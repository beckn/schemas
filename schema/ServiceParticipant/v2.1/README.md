# ServiceParticipant — v2.1

**Schema Pack Version:** 2.1.0
**Released:** May 2025
**Status:** Initial release

## Notes

Initial release of the ServiceParticipant schema targeting the v2.1 generalised model.

Provides a domain-neutral base for participant attribute schemas in Beckn networks. The
sole field — `credentialRefs` (array of `Credential/2.0`) — is intentionally minimal:
role, identity, and domain-specific attributes belong in extending schemas that inherit
this one via `allOf`.
