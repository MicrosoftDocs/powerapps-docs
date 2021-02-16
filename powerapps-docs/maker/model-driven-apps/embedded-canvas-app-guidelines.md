---
title: "Guidelines on working with embedded canvas apps | MicrosoftDocs"
description: Understand the recommended ways to work with embedded canvas apps in Power Apps
ms.custom: ""
ms.date: 08/28/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
author: "RichdiMSFT"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Guidelines on working with embedded canvas apps

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

This topic provides guidelines on working with embedded canvas apps as well as helpful tips to troubleshoot any issues you might encounter.

-	Embedded canvas apps are only supported with Unified Interface model-driven apps.
-	You can only enable three embedded canvas apps for each form with Web, and one for Tablet and Phone client types. 
-	You can have multiple embedded canvas apps added to the form, but can only enable three at a time for Web and one at a time for Tablet and Phone client types. 
-	If you try to enable more than three embedded canvas apps with the Web client type on a model-driven app form you will get the message "You have more than three canvas apps with Web form factor, the maximum is three for this form factor. The number of canvas apps are limited to three for Web and one for Tablet and Phone form factors."
   - To enable or disable an embedded canvas app see [Enable an embedded canvas app](#enable-an-embedded-canvas-app) and [Disable an embedded canvas app](#disable-an-embedded-canvas-app).
-	We recommend that you have a single embedded canvas app for each form tab.
-	When adding an embedded canvas app to a model-driven form always use a required column that is guaranteed to have a value. If your column does not have a value your embedded canvas app will not refresh in response to any change in data on the host model-driven form.
-	Publishing a model-driven form does not also publish the embedded canvas app.
     - Embedded canvas apps need to be published independent of the host model-driven form. More information: [Publish an app](../canvas-apps/save-publish-app.md#publish-an-app).
-	If opening Power Apps Studio to create or edit an embedded canvas app via the **Customize** button in the canvas app control properties is blocked due to a web browser pop-up blocker, you must enable the make.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again.
-	Embedded canvas apps are not displayed when creating a new row since they need a row context to be passed to them.
-	The ModelDrivenFormIntegration.Item object is read-only. 
     - To write back data you must use the Common Data Service connector. More information: [Microsoft Dataverse](/connectors/commondataservice/)
-	Embedded canvas apps can only be created via the host model-driven form. 
- When you view a model-driven form with an embedded canvas app, if you see an error message that reads "It looks like you don’t have access to this app" ask its owner to share it with you" make sure that the author has shared the embedded canvas app with you. More information: [Share an embedded canvas app](share-embedded-canvas-app.md).
- Adding a canvas app on the sub-grid control is no longer available.
    - In the preview release, makers were able to add a canvas app on a sub-grid control. With canvas app embedding on model-driven forms now generally available, adding an embedded canvas app on a model-driven form is streamlined to the column. 
    - This makes it easier for makers since they don't have to decide up front whether to pass the current (main form) row as data context or a list of rows related to the current (main form) row. 
    - Makers always start with a column and can access both the current (main form) row or a list of rows related to the current (main form) row.
    - To access the list of related rows in the canvas app, makers can use the Common Data Service connector and [Filter](../canvas-apps/functions/function-filter-lookup.md) function with the [Improve data sources experience and Dataverse views](https://powerapps.microsoft.com/blog/improved-data-source-selection-and-common-data-service-views/) capability enabled in the canvas app.  
    For example, to access the *Active Contacts* view of the *Contacts* table, makers can use: *Filter(Contacts, 'Contacts (Views)'.'Active Contacts')*.
    - Existing canvas apps that use the sub-grid control will continue to work. However, we recommend that you migrate these apps to use a column instead. More information: [Migrating embedded canvas apps on model-driven forms that use a list of rows related to the current (main form) row](embedded-canvas-app-migrate-from-preview.md#migrating-embedded-canvas-apps-on-model-driven-forms-that-use-a-list-of-rows-related-to-the-current-main-form-row) for details.

## Enable an embedded canvas app
1. Select the column that is customized to display as an embedded canvas app.
2. In the **Column Properties** dialog, select the **Controls** tab.
3. In the list of controls select **Canvas app** and then select the **Web** option.
4. Select **OK**.

## Disable an embedded canvas app
1. Select the Column that is customized to display as an embedded canvas app.
2. In the **Column Properties** dialog, select the **Controls** tab.
3. In the list of controls select the default control and then select the **Web** option.
4. Select **OK**.

## Known issues and limitations with embedded canvas apps
- The canvas app custom control is only supported for use with the **Web** client type. Currently, the **Phone** and **Tablet** client types aren't supported.
- The ModelDrivenFormIntegration control does not provide a value for columns of a related table. 
  - For example, when the ModelDrivenFormIntegration control is connected to the Accounts table, using *ModelDrivenFormIntegration.Item.’Primary Contact’.’Full Name’* will not return a value. 
  - To access columns of a related table makers can use either of the expressions listed here:
    - *LookUp(Accounts, Account = GUID(First(ModelDrivenFormIntegration.Data).ItemId)).'Primary Contact'.'Full Name'*  
      - *ItemId* is empty at authoring time but will have a value at runtime.
    - *LookUp(Accounts, Account = ModelDrivenFormIntegration.Item.Account).'Primary Contact'.'Full Name'* (This expression is easier to read, but the previous expression will perform slightly better.)
- You can’t use the **Canvas App** privilege in a security role to grant app users access to either an embedded or standalone canvas app. For more information on sharing an embedded canvas app, please refer to: [Share an embedded canvas app](share-embedded-canvas-app.md).
- If you write back the same data that is being displayed in the host model-driven form, the form will continue to display old data until it is refreshed. An easy way to do that is to use the [RefreshForm](embedded-canvas-app-actions.md#refreshformshowprompt) method.

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]