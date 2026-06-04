# List — v2.0

A generic, domain-agnostic collection of elements. Each element carries an `id`, a `descriptor`, and an extensible `listElementAttributes` bag. The `order` property indicates whether the elements are ranked ascending, descending, or unordered. List is meant to be **extended** by more specific list types.

## Files

| File | Purpose |
|---|---|
| [https://schema.beckn.io/List/v2.0/attributes.yaml](https://schema.beckn.io/List/v2.0/attributes.yaml) | OpenAPI schema envelope (versioned path) |
| [https://schema.beckn.io/List/v2.0/context.jsonld](https://schema.beckn.io/List/v2.0/context.jsonld) | JSON-LD context (versioned path) |
| [https://schema.beckn.io/List/v2.0/vocab.jsonld](https://schema.beckn.io/List/v2.0/vocab.jsonld) | RDF vocabulary (versioned path) |

## Properties

| Property | Required | Type | Description |
|---|---|---|---|
| `@context` | yes | string | JSON-LD context reference |
| `@type` | yes | string | JSON-LD type |
| `elements` | no | array of `{ id, descriptor, listElementAttributes }` | The members of the list. `descriptor` is a Descriptor; `listElementAttributes` is an Attributes bag. |
| `order` | no | string (enum) | Ordering of the elements: `ASCENDING`, `DESCENDING`, or `UNORDERED` (default `UNORDERED`). |
