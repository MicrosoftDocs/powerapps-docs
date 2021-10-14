---
title: "Share an embedded canvas app | MicrosoftDocs"
description: Learn how to share an embedded canvas app
ms.custom: ""
ms.date: 06/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Richdimsft"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Share an embedded canvas app

This article explains what's needed to share an embedded canvas app that you have already created.

After you have created and added an embedded canvas app to a model-driven form you will need to take steps to ensure that all users that have access to the model-driven form also have access to the canvas app and the data that it uses. Please refer to the following guidelines:
-	Share your embedded canvas app with Everyone in your organization or a security group or specific users. More information: [Share an app](../canvas-apps/share-app.md#share-an-app)
-	Ensure that users have appropriate permissions for any Microsoft Dataverse tables that your embedded canvas app uses. Specifically add read pmermissions for the "Canvas App" table under the customization section.  More information: [Manage table permissions](../canvas-apps/share-app.md#manage-table-permissions)
-	Ensure that users have appropriate permission for data on any cloud services that your embedded canvas app uses, such as SharePoint or OneDrive. The steps to share are specific to each cloud service and beyond the scope of Power Apps.

> [!NOTE]
> Currently, you must explicitly share canvas apps through app sharing. The **Canvas App** privilege in a security role does not share the embedded or standalone application. 

Embedded canvas apps are also solution aware. By default embedded canvas apps are created in the same solution as the host model-driven form. To move the embedded canvas app from one environment to another export and import embedded canvas apps as a part of a solution just like any other component.

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]