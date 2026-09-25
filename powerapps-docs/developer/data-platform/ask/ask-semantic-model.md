---
title: "Ask Questions Using a Dataverse Semantic model (Preview)"
description: "Learn how to use a Dataverse Semantic model to ask natural-language questions, retrieve structured Dataverse results, and page through responses."
ms.date: 09/25/2026
ms.collection: bap-ai-copilot
ms.reviewer: jdaly
ms.topic: how-to
author: JasonHQX
ms.author: jasonhuang
ms.subservice: dataverse-developer
search.audienceType:
  - developer
ai-usage: ai-assisted
---


# Ask questions by using a Dataverse Semantic model (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

Use the **Ask** operation with a Dataverse Semantic model to submit natural-language questions. The operation returns structured rows, a natural-language summary, and source links when available.

Before using this API:

1. Complete the steps in [Get started with the Dataverse Ask APIs](get-started.md).
1. [Create a semantic model](manage-semantic-models.md#create-a-semantic-model).
1. Grant the calling identity read access to the tables, columns, and records included in the semantic model.

Replace `[Organization URI]` with the environment URL, such as `https://contoso.api.crm.dynamics.com`.

## Send an Ask request

This example asks a question by using a semantic model named `Sales pipeline`.

```http
POST [Organization URI]/api/iq/v1.0/ask HTTP/1.1
Authorization: Bearer <access token>
Accept: application/json
Content-Type: application/json

{
  "query": "Which open opportunities have the highest estimated revenue?",
  "semanticModelName": "Sales pipeline",
  "searchMode": "Auto",
  "count": 100
}
```

### Request properties

These properties contain the information about your request:

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `query` | String | Yes | None | The natural-language question to answer. |
| `semanticModelName` | String | Yes | None | The exact `uniqueName` of the semantic model to use. |
| `searchMode` | [SearchMode](#searchmode) | No | `Auto` | The search strategy to use. |
| `count` | 32-bit integer | No | `100` | The maximum number of rows to return in this page. |
| `pagingToken` | String | No | null | An opaque token from a previous response used to retrieve the next page. |

### SearchMode

These values specify search strategy to use. 


| Value | Description |
|---|---|
| `Auto` | Lets the service select the search strategy. Use this value unless your scenario requires another mode. |
| `QuickResponse` | Favors a faster response. |
| `ThinkDeeper` | Favors deeper analysis when the question can take longer to answer. |

Search mode can affect response time. Applications should set an appropriate client timeout and provide progress feedback for interactive users.

## Review the Ask response

A successful request returns `200 OK`. The properties in each `rawResult` object depend on the question:

```json
{
  "rawResult": [
    {
      "opportunity": "Contoso renewal",
      "account": "Contoso",
      "estimatedRevenue": 125000
    }
  ],
  "citationLinks": [
    "[Organization URI]/main.aspx?pagetype=entityrecord&etn=opportunity&id=00000000-0000-0000-0000-000000000002"
  ],
  "summary": "The Contoso renewal has the highest estimated revenue.",
  "totalResultCount": 1,
  "pagingToken": null
}
```

### Response properties

A successful response contains these properties:

| Name | Type | Nullable | Description |
|---|---|---|---|
| `rawResult` | Array of Object | Yes | Rows returned for the question. Properties in each object depend on the question and generated query. |
| `citationLinks` | Array of String | Yes | Links to sources associated with the response. |
| `summary` | String | Yes | A natural-language summary of the result. |
| `totalResultCount` | 64-bit integer | No | The total number of matching rows when available. This value might reflect only the current page. |
| `pagingToken` | String | Yes | An opaque token to pass in a subsequent request to retrieve the next page. |

Treat `rawResult` as an array of dynamic JSON objects. Display `summary` when it's present, but don't require it to process the rows. Results vary with the caller's Dataverse privileges.

## Retrieve the next page

When `pagingToken` returned in the response isn't null, send another request with the same question, semantic model, search mode, and count. Copy the token exactly:

```http
POST [Organization URI]/api/iq/v1.0/ask HTTP/1.1
Authorization: Bearer <access token>
Accept: application/json
Content-Type: application/json

{
  "query": "Which open opportunities have the highest estimated revenue?",
  "semanticModelName": "Sales pipeline",
  "searchMode": "Auto",
  "count": 100,
  "pagingToken": "<paging-token-from-previous-response>"
}
```

Continue until the response returns a null or empty `pagingToken`.  Don't decode, modify, or construct paging tokens.

## Service protection limits

The Ask API enforces lower limits, so you don't reach the common Dataverse [Service protection API limits](../api-limits.md). You manage these limits in the same way.

The Ask API allows each user to send up to 30 requests per organization per minute. If you exceed this limit, the API returns a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error. Wait for the period specified by the `Retry-After` response header before sending more requests. The header value represents the number of seconds to wait.



## Related information

- [Manage semantic models](manage-semantic-models.md)
- [Handle errors](get-started.md#handle-errors)
- [Retry transient errors](get-started.md#retry-transient-errors)
