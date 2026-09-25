---
title: "Get Started with the Dataverse Ask APIs (Preview)"
description: "Learn how to access and use the Dataverse Ask APIs, authenticate and authorize callers, compose requests, handle errors, and retry safely."
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

# Get started with the Dataverse Ask APIs (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

Before calling the Dataverse Ask APIs, configure the environment and an identity, and understand the HTTP and retry requirements described in this article.

## Prerequisites

In the Power Platform admin center, turn on **Business Applications in Work IQ for this environment** for each environment where you want to use the Dataverse Ask APIs. [Learn how to manage feature settings](/power-platform/admin/settings-features)


> [!IMPORTANT]
> When you create a semantic model, Dataverse indexes the tables that you select. This indexing process uses Dataverse database storage.
>
> To view how much storage indexing uses in an environment, check the **DataverseSearch** table (formerly **RelevanceSearch**). This storage counts toward database storage consumption on the **Summary** and **Dataverse** tabs.


## Authentication

The Dataverse Ask APIs use the same Microsoft Entra ID OAuth authentication as other Dataverse HTTP endpoints.

1. Register your application in Microsoft Entra ID.
1. Configure delegated access for an interactive application, or create a Dataverse application user for a server-to-server application.
1. Acquire an access token for the Dataverse environment URL.
1. Send the token in the `Authorization` header of every request.

For delegated authentication, request the `<environment-url>/user_impersonation` scope. For confidential clients, request `<environment-url>/.default`.

```http
Authorization: Bearer <access-token>
```

For registration choices, flows, and code examples, see [Use OAuth authentication with Microsoft Dataverse](../authenticate-oauth.md).

## Authorization and privileges

Authentication identifies the user or application user. Dataverse security roles determine what the caller can do.

### Semantic model management

In the Power Platform admin center, assign the caller a security role that includes privileges to create and delete semantic models. The following security roles include these privileges:

- Dataverse Search Role
- Environment Maker
- System Administrator
- System Customizer

If you use a custom security role, a system administrator can [configure its privileges in the Power Platform admin center](/power-platform/admin/create-edit-security-role#edit-privileges-of-a-security-role).

### Ask operations

The caller must have **Read** access to the Dataverse tables and columns included in the semantic model. The service only uses data that the caller is authorized to read. Record ownership, business unit access, sharing, and column-level security can affect the results.

An application that uses server-to-server authentication runs with the privileges assigned to its Dataverse application user. Grant only the privileges the application requires.

## Compose requests

Build the base URL by appending `/api/iq/v1.0/` to the organization URI:

If the organization URI is `https://contoso.api.crm.dynamics.com/`, the full base URL is:

```text
https://contoso.api.crm.dynamics.com/api/iq/v1.0/
```

Use HTTPS and include these headers:

```http
Authorization: Bearer <access-token>
Accept: application/json
```

For requests with a JSON body, also include:

```http
Content-Type: application/json
```

The Dataverse Ask APIs aren't an OData service. Don't include OData-specific headers or query options unless another article explicitly requires them.

Use UTF-8 for request bodies. Use the property name and choice value casing shown in the API articles.

## Process responses

Check the HTTP status code before deserializing a successful response. Response bodies use JSON. Successful operations return these status codes:

| Operation | Status code |
|---|---|
| [List semantic models](manage-semantic-models.md#list-semantic-models) | `200 OK` |
| [Create semantic model](manage-semantic-models.md#create-a-semantic-model) | `201 Created` |
| [Delete semantic model](manage-semantic-models.md#delete-a-semantic-model) | `200 OK` |
| [Ask using semantic model](ask-semantic-model.md) | `200 OK` |

Some response properties are nullable. Don't assume that a summary, citation links, raw rows, or a paging token is present.

The shape of each item in `rawResult` depends on the question and the data used to answer it. Process each item as a JSON object rather than deserializing every Ask response into one fixed row type.

## Handle errors

For an unsuccessful response:

1. Check the HTTP status code.
1. If the response has a JSON body, log the error type and message for diagnostics.
1. Check for a `Retry-After` response header.
1. Retry only transient failures.
1. Don't write logic that depends on undocumented error properties or exact message text.


### Expected status codes

Handle these types of errors:

| Status code | Meaning | Recommended action |
|---|---|---|
| `400 Bad Request` | The request is invalid, a required environment capability isn't enabled, or no authorized table can be used. | Correct the request or environment configuration. Don't retry the same request unchanged. |
| `401 Unauthorized` | The access token is missing, invalid, expired, or for another resource. | Acquire a valid token for the environment and try again. |
| `403 Forbidden` | The caller lacks a required privilege. | Assign an appropriate security role or use another identity. |
| `404 Not Found` | The requested semantic model doesn't exist. | Confirm the semantic model identifier or name. |
| `429 Too Many Requests` | The caller exceeded a service protection limit. | Wait for the `Retry-After` duration before retrying. |
| `500 Internal Server Error` | An unexpected error occurred. | Retry with backoff if the operation is safe to repeat. If the error persists, contact Microsoft Support. |
| `503 Service Unavailable` | The service or required metadata is temporarily unavailable. | Retry with backoff. |

### Retry transient errors

Treat `429`, `500`, `502`, `503`, and `504` responses as potentially transient. Also retry network failures for which the request outcome is known to be safe.

Use this retry order:

1. If the response includes `Retry-After`, wait for that duration.
1. Otherwise, use exponential backoff with random jitter.
1. Limit the retry count and total elapsed time.
1. Stop retrying nontransient responses.
1. Log the final failure and the correlation information returned by the service.

Avoid immediately retrying multiple requests in parallel because this action can extend throttling.

### Consider operation safety

- **List** and **Ask** requests are safe to retry after a transient failure.
- Before retrying **Create**, list the semantic models to determine whether the first request succeeded. Semantic model names must be unique.
- Before retrying **Delete**, list the semantic models to determine whether the model still exists. Treat a missing model after an uncertain delete response as a completed delete.


## Next steps

- [Manage semantic models](manage-semantic-models.md)
- [Ask questions using a semantic model](ask-semantic-model.md)
