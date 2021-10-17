---
title: "Add connectors to a custom page for your model-driven app" 
description: "Learn how to add a connector to a custom page"
ms.custom: ""
ms.date: 07/22/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: "article"
author: "aorth"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Add connectors to a custom page for your model-driven app

This article outlines the use of Power Apps connectors within a custom page. The most common connectors are listed here. This article also includes the known issues for connectors in custom pages.

Publishing a model-driven app with custom pages will consolidate all of the connections within the app. This connector consolidation allows for a single consent prompt for all of the connectors at the start of the app.

## Verified connectors for custom pages

| Connector | Status | Comments |
|--|--|--|
| [Office 365 Users](../canvas-apps/connections/connection-office365-users.md) | Verified |
| [Outlook](../canvas-apps/connections/connection-office365-outlook.md) | Verified |
| [SharePoint Online](../canvas-apps/connections/connection-sharepoint-online.md) | Verified |
| [SQL Server](../canvas-apps/connections/connection-azure-sqldatabase.md) | Verified | Includes AAD Auth, SQL Server Auth, Windows Auth, and Windows Auth non-shared | 
| Power Automate | Verified |
| [Teams](/connectors/teams/) | Verified |
| [Custom connector](../canvas-apps/register-custom-api.md) | Verified |
| [Excel Online for Business](../canvas-apps/connections/connection-excel.md) | Verified |  |
| [Excel via file share](../canvas-apps/connections/connection-excel.md) | Verified |  |

The connectors listed here are also supported with the on-premises data gateway for canvas apps.

## Known issues

* There's no support to enable bypassing Microsoft connectors.
* Cross environment Microsoft Dataverse connections can be used but the consent prompt isn't presented to the user.

### See also

[Model-driven app custom page overview](model-app-page-overview.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Overview of Power Apps connectors](../canvas-apps/connections-list.md)