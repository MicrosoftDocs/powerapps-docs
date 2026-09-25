---
title: "Manage Dataverse semantic models (Preview)"
description: "Learn how to manage Dataverse semantic models with APIs that list, create, and delete models. Follow the steps to manage models in your environment."
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

# Manage Dataverse semantic models (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

Dataverse semantic models define the Dataverse tables available for answering natural-language questions. This article explains how to list, create, and delete these models by using the Dataverse Ask APIs, helping you manage which tables your application can query.

Before using these APIs, complete the steps in [Get started with the Dataverse Ask APIs](get-started.md).

Replace `[Organization URI]` with the organization URI, such as `https://contoso.api.crm.dynamics.com`.

## Choose tables for a semantic model

Use table logical names, such as `account`, `contact`, and `opportunity`. Don't use display names, entity set names, or collection names.

Choose only tables relevant to the questions your application needs to answer. The identity that submits an [Ask request](ask-semantic-model.md) must have read access to the selected tables, columns, and records.

## List semantic models

The List operation returns semantic models available in the current Dataverse environment.

```http
GET [Organization URI]/api/iq/v1.0/semanticmodel HTTP/1.1
Authorization: Bearer <access token>
Accept: application/json
```

A successful request returns `200 OK`:

```json
{
  "data": [
    {
      "id": "00000000-0000-0000-0000-000000000001",
      "uniqueName": "Sales pipeline",
      "source": "SemanticModelAPI",
      "description": "This is a test semantic model for demo purpose",
      "tables": [
        "account",
        "opportunity"
      ],
      "createdBy": "Adele Vance",
      "modifiedOn": "2026-08-17T20:00:00Z",
      "createdOn": "2026-08-15T17:30:00Z",
      "ownerId": "00000000-0000-0000-0000-000000000002",
      "owner": "Adele Vance"
    }
  ]
}
```

Don't rely on array order. Locate a model by its exact `uniqueName` or `id`.

### Semantic model properties

| Name | Type | Nullable | Description |
|---|---|---|---|
| `id` | String (GUID) | Yes | The unique identifier of the semantic model. |
| `uniqueName` | String | Yes | The unique name of the semantic model. |
| `tables` | Array of String | Yes | Logical names of the associated Dataverse tables. |
| `createdBy` | String | Yes | The full name of the user who created the semantic model. |
| `modifiedOn` | String (date-time) | Yes | The UTC date and time when the semantic model was last modified. |
| `createdOn` | String (date-time) | Yes | The UTC date and time when the semantic model was created. |
| `ownerId` | String (GUID) | Yes | The unique identifier of the semantic model owner. |
| `owner` | String | Yes | Full name of the user who owns this semantic model. |
| `source` | String | Yes | Identifies the channel that created the semantic model. |
| `description` | String | Yes | Description of this semantic model. |

## Create a semantic model

The create operation associates a unique name with one or more Dataverse tables.

```http
POST [Organization URI]/api/iq/v1.0/semanticmodel HTTP/1.1
Authorization: Bearer <access token>
Accept: application/json
Content-Type: application/json

{
  "uniqueName": "Sales pipeline",
  "tables": [
    "account",
    "opportunity"
  ]
}
```

### Request properties

| Name | Type | Required | Description |
|---|---|---|---|
| `uniqueName` | String | Yes | The unique name of the semantic model to create. |
| `tables` | Array of String | Yes | One or more Dataverse table logical names to associate with the model. |

A successful request returns `201 Created`:

```json
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000001",
    "uniqueName": "Sales pipeline",
    "createdOn": "2026-08-17T20:00:00Z"
  },
  "message": "Semantic model created successfully"
}
```

| Name | Type | Nullable | Description |
|---|---|---|---|
| `data.id` | String (GUID) | Yes | The unique identifier of the created semantic model. |
| `data.uniqueName` | String | Yes | The unique name of the created semantic model. |
| `data.createdOn` | String (date-time) | No | The UTC date and time when the semantic model was created. |
| `message` | String | Yes | A message describing the result of the operation. |

Store `id` if your application needs to delete the model later. Use `uniqueName` as the `semanticModelName` value in an [Ask request](ask-semantic-model.md).

Semantic model names must be unique in an environment. If a request has an uncertain outcome because of a network or transient error, list semantic models before sending it again.

## Delete a semantic model

The delete operation uses the semantic model `id`, not its name.

Before deleting a semantic model, [find the apps and agents that use it](#find-apps-and-agents-that-use-a-semantic-model) to assess the impact.

> [!IMPORTANT]
> You can delete only semantic models that you created by using the [Create operation](#create-a-semantic-model). You can't delete semantic models associated with an app module, bot, or agent by using this API.

```http
DELETE [Organization URI]/api/iq/v1.0/semanticmodel/00000000-0000-0000-0000-000000000001 HTTP/1.1
Authorization: Bearer <access token>
Accept: application/json
```

| Name | Type | Description |
|---|---|---|
| `id` | String (GUID) | The unique identifier of the semantic model to delete. |

A successful request returns `200 OK`:

```json
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000001"
  },
  "message": "Semantic model deleted successfully"
}
```

| Name | Type | Nullable | Description |
|---|---|---|---|
| `data.id` | String (GUID) | Yes | The unique identifier of the deleted semantic model. |
| `message` | String | Yes | A message describing the result of the operation. |

After deletion, applications can no longer use the model name in Ask requests.

## Find apps and agents that use a semantic model

Use the optional `include=botinfo` query parameter to identify app modules, bot components, and agents that use each semantic model. Use this information to assess dependencies before you change or delete a semantic model, or to investigate which applications and agents reference it.

The `botinfo` value isn't case-sensitive. The `include` parameter accepts a comma-separated list of values.

```http
GET [Organization URI]/api/iq/v1.0/semanticmodel?include=botinfo HTTP/1.1
Authorization: Bearer <access token>
Accept: application/json
```

A successful request returns `200 OK`:

```json
{
  "data": [
    {
      "id": "00000000-0000-0000-0000-000000000003",
      "uniqueName": "Sales pipeline",
      "source": "SemanticModelAPI",
      "description": "This is a test semantic model for demo purpose",
      "tables": [
        "lead",
        "product"
      ],
      "createdBy": "Adele Vance",
      "modifiedOn": "2026-08-17T20:00:00Z",
      "createdOn": "2026-08-15T17:30:00Z",
      "ownerId": "00000000-0000-0000-0000-000000000004",
      "owner": "Adele Vance",
      "m365AppModuleId": "00000000-0000-0000-0000-000000000005",
      "appModulePrimaryName": "Customer Service Hub",
      "appModulePrimaryUniqueName": "Customerservicehub",
      "m365AppModuleIdSecondary": "00000000-0000-0000-0000-000000000006",
      "appModuleSecondaryName": "Power Pages Management",
      "appModuleSecondaryUniqueName": "mspp_PowerPageManagement",
      "bots": [
        {
          "botComponentName": "SalesSpecificQnA",
          "agentName": "Copilot in Dynamics 365 Sales"
        }
      ]
    }
  ]
}
```

### Additional app and agent properties

| Name | Type | Nullable | Description |
|---|---|---|---|
| `m365AppModuleId` | String | Yes | ID of the model-driven app associated with an ALM-compliant primary semantic model. This value is backed by a Dataverse lookup relationship to the app module. |
| `m365AppModuleIdSecondary` | String | Yes | App module ID associated with a secondary semantic model. This value is stored as a GUID and doesn't create an ALM-managed relationship to the app module. |
| `appModulePrimaryName` | String | Yes | Display name of the app module referenced by `m365AppModuleId`. |
| `appModulePrimaryUniqueName` | String | Yes | Logical name of the app module referenced by `m365AppModuleId`. |
| `appModuleSecondaryName` | String | Yes | Display name of the app module whose ID is stored in `m365AppModuleIdSecondary`. |
| `appModuleSecondaryUniqueName` | String | Yes | Logical name of the app module whose ID is stored in `m365AppModuleIdSecondary`. |
| `bots` | Array of Object | Yes | Bot components and agents that use the semantic model. |
| `botComponentName` | String | Yes | Display name of a bot component that uses or references the semantic model. Returned within the `bots` collection. |
| `agentName` | String | Yes | Display name of the agent that contains the bot component. Returned within the `bots` collection. |

## Fine-tune a semantic model
After you create the semantic model, you can fine-tune it on the Semantic model page in [Power Apps](https://make.powerapps.com):
- **Signals**: Turn system-inferred signal types, such as table summaries or form summaries, on or off across all tables. You can also exclude tables that contain sensitive or irrelevant data and turn off individual views or relationships that are outdated or misleading. For more information, see [Fine-tune semantic model signals](../../../maker/data-platform/fine-tune-semantic-model-signals.md).

- **Glossary**: Add business vocabulary that the system can't infer, such as acronyms or organization-specific terms, so agents interpret user questions correctly. For more information, see [Manage semantic model glossary entries](../../../maker/data-platform/manage-semantic-model-glossary.md).

- **Refresh**: The semantic model regenerates automatically every 12 hours. To apply your changes immediately, trigger a manual regeneration. For more information, see [Regenerate the semantic model](../../../maker/data-platform/regenerate-semantic-model.md).

## Related information

- [Ask questions using a semantic model](ask-semantic-model.md)
- [Handle errors](get-started.md#handle-errors)
- [Retry transient errors](get-started.md#retry-transient-errors)
