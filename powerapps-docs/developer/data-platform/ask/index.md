---
title: "Use Dataverse Ask APIs for Natural-Language Questions (Preview)"
description: "Learn how to create semantic models and ask natural-language questions about Microsoft Dataverse data by using the Dataverse Ask APIs."
ms.date: 09/25/2026
ms.collection: bap-ai-copilot
ms.reviewer: jdaly
ms.topic: overview
author: JasonHQX
ms.author: jasonhuang
ms.subservice: dataverse-developer
search.audienceType:
  - developer
ai-usage: ai-assisted
---

# Use the Dataverse Ask APIs (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

The Dataverse Ask APIs let your application ask natural-language questions about business data stored in Microsoft Dataverse. You define a *semantic model* that identifies the Dataverse tables relevant to a business scenario, and then submit questions against that model.

For example, an application can create a semantic model that includes the `account` and `opportunity` tables and then ask:

- Which open opportunities are expected to close this quarter?
- Summarize the opportunities for a specific account.
- Which accounts have the highest estimated revenue?

The response can include rows that answer the question, a natural-language summary, source links, the number of matching rows, and a paging token when more results are available.

## Why use the Dataverse Ask APIs?

Use these APIs when you want to add natural-language access to Dataverse data without requiring users to know table relationships, query syntax, or column logical names.

The API helps you:

- Define reusable scopes over one or more Dataverse tables.
- Add question-and-answer experiences to custom applications and services.
- Return both structured rows and a natural-language summary.
- Respect the Dataverse data access of the identity that submits the question.
- Page through larger result sets by using paging tokens.

The Dataverse Ask APIs complement the Dataverse Web API. Use the [Dataverse Web API](../webapi/overview.md) when your application needs precise create, retrieve, update, delete, or query operations. Use the Dataverse Ask APIs when the input is a natural-language question and the application needs the service to determine how to answer it from a defined set of tables.

## Licensing

For information and terms about Work IQ licensing, see [Licensing requirements](/microsoft-365/copilot/extensibility/work-iq/api-overview#licensing-requirements).

## Dataverse Ask API operations

| Operation | Description |
|---|---|
| [List semantic models](manage-semantic-models.md#list-semantic-models) | Lists semantic models available in the current environment. |
| [Create semantic model](manage-semantic-models.md#create-a-semantic-model) | Creates a named semantic model associated with one or more Dataverse tables. |
| [Delete semantic model](manage-semantic-models.md#delete-a-semantic-model) | Deletes a semantic model. |
| [Ask using semantic model](ask-semantic-model.md) | Submits a natural-language question against a named semantic model. |

## Dataverse Ask API characteristics

The Dataverse Ask APIs use JSON over HTTP at:

```text
https://<environment-url>/api/iq/v1.0/
```

It isn't part of the OData service at `/api/data/`. It doesn't provide an OData service document or metadata document, and it doesn't support OData query options such as `$select`, `$filter`, or `$expand`.

No Dataverse SDK for .NET or SDK for Python client classes are provided for these operations. Use an HTTP client and authenticate with a Microsoft Entra ID access token for the Dataverse environment.




## Get started

1. [Request access and prepare your application](get-started.md).
1. [Manage semantic models](manage-semantic-models.md).
1. [Ask questions using a semantic model](ask-semantic-model.md).

## Related information

- [Use OAuth authentication with Microsoft Dataverse](../authenticate-oauth.md)
- [Service protection API limits](../api-limits.md)
