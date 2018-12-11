---
title: "Share an embedded canvas app | MicrosoftDocs"
ms.custom: ""
ms.date: 12/10/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "PowerApps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Share an embedded canvas app

After you add an embedded canvas app to a model-driven form you'll need to take steps to ensure that all users that have access to the model-driven form also have access to the canvas app and the data that it uses.
-	Share your embedded canvas app with either everyone in your organization, one or more security groups, or specific people. More information: [Share an app](../canvas-apps/share-app.md#share-an-app)
-	Ensure that users have appropriate permissions for any Common Data Service entities that your app uses. More information: [Manage entity permissions](../canvas-apps/share-app.md#manage-entity-permissions)
-	Ensure that users have appropriate permission for any other data sources that your app uses, such as SharePoint or OneDrive. The steps to share depend on the type of data you are sharing and are outside the security scope of PowerApps.

Embedded canvas apps are solution aware. By default, they're created in the same solution as the host model-driven form. To move the app from one environment to another you export and import embedded canvas apps as a part of a solution&mdash;just like any other component.

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md)


