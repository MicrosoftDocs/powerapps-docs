---
title: "Add connectors to a custom page for your model-driven app (preview)" 
description: ""
ms.custom: ""
ms.date: 06/06/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "aorth"
ms.assetid: b4098c96-bce1-4f57-804f-8694e6254e81
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Add connectors to a custom page for your model-driven app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic outlines the use of Power Apps connectors within a custom page.  The most common connectors are being verified and status is available in this page.  This page also includes any known issues for connectors in custom pages. 

Publishing a model-driven app with custom pages will consolidate all of the connections within the app. This connector consolidation allows for a single consent prompt for all of the connectors at the start of the app.

## Verified connectors for custom pages

| Connector | Status | Notes |
|--|--|--|
| [Office 365 Users](../canvas-apps/connections/connection-office365-users.md) | Verified |
| [Outlook](../canvas-apps/connections/connection-office365-outlook.md) | Verified |
| [SharePoint Online](../canvas-apps/connections/connection-sharepoint-online.md) | Verified |
| [SQL Server](../canvas-apps/connections/connection-azure-sqldatabase.md) | Verified | Includes AAD Auth, Sql Server Auth, Windows Auth, and Windows Auth non-shared | 
| Power Automate | Verified |
| [Teams](/connectors/teams/) | Verified |
| [Custom connector](../canvas-apps/register-custom-api.md) | Verified |
| [Excel Online for Business](../canvas-apps/connections/connection-excel.md) | Verified |  |
| [Excel via file share](../canvas-apps/connections/connection-excel.md) | Verified |  |

Note: connectors on the supported list are expected to work with on-prem gateway

## Upcoming changes to connectors for custom pages

* Environment variable support for connections
* Connection References support for shared connections

## Known issues

* No support to enable bypassing Microsoft connectors
* Cross environment Dataverse connections can be used but the consent prompt is not shown

## Related topics

[Model-driven app custom page overview](model-app-page-overview.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Overview of Power Apps connectors](../canvas-apps/connections-list.md)