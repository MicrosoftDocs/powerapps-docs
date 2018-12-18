---
title: "Share an embedded canvas app | MicrosoftDocs"
ms.custom: ""
ms.date: 12/17/2018
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
This topic explains how to share an embedded canvas app that you have already created.

After you have created and added an embedded canvas app to a model-driven form you will need to take steps to ensure that all users that have access to the model-driven form also have access to the canvas app and the data that it uses. Please refer to the following guidelines:
-	Share your embedded canvas app with Everyone in your organization or a security group or specific users. More information: [Share an app](../canvas-apps/share-app.md#share-an-app)
-	Ensure that users have appropriate permissions for any Common Data Service entities that your embedded canvas app uses. More information: [Manage entity permissions](../canvas-apps/share-app.md#manage-entity-permissions)
-	Ensure that users have appropriate permission for data on any cloud services that your embedded canvas app uses, such as SharePoint or OneDrive. The steps to share are specific to each cloud service and beyond the scope of PowerApps.

> [!NOTE]
> The Canvas app privilege in the Customization of a Security Role tab does not currently affect Canvas apps (embedded or standalone)

Embedded canvas apps are also solution aware. By default embedded canvas apps are created in the same solution as the host model-driven form. To move the embedded canvas app from one environment to another export and import embedded canvas apps as a part of a solution just like any other component.

## See also
[Embed a canvas app in a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass the current record as data context to an embedded canvas app](pass-current-embedded-canvas-app.md) <br />
[Pass a list of related records as data context to an embedded canvas app](pass-related-embedded-canvas-app.md)
