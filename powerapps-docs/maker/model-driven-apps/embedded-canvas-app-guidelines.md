---
title: "Guidelines on working with embedded canvas apps | MicrosoftDocs"
ms.custom: ""
ms.date: 08/19/2019
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
This topic provides guidelines on working with embedded canvas apps as well as helpful tips to troubleshoot any issues you might encounter.

-	Embedded canvas apps are only supported with Unified Interface model-driven apps.
-	You can only enable one embedded canvas app per form. 
     - You can have multiple embedded canvas apps added to the form but can only enable one at a time.
     - If you try to enable more than one embedded canvas app on a model-driven form you will get a message that reads “Only one canvas app can be enabled on a form.”
     - To enable or disable an embedded canvas app see [Enable an embedded canvas app](#enable-an-embedded-canvas-app) and [Disable an embedded canvas app](#disable-an-embedded-canvas-app).
-	When adding an embedded canvas app to a model-driven form always use a required field that is guaranteed to have a value. If your field does not have a value your embedded canvas app will not refresh in response to any change in data on the host model-driven form.
-	Publishing a model-driven form does not also publish the embedded canvas app.
     - Embedded canvas apps need to be published independent of the host model-driven form. More information: [Publish an app](../canvas-apps/save-publish-app.md#publish-an-app).
-	If opening Power Apps Studio to create or edit an embedded canvas app via the **Customize** button in the canvas app control properties is blocked due to a web browser pop-up blocker, you must enable the make.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again.
-	Embedded canvas apps are not displayed when creating a new record since they need a record context to be passed to them.
-	The ModelDrivenFormIntegration.Item object is read-only. 
     - To write back data you must use the Common Data Service connector. More information: [Common Data Service](/connectors/commondataservice/)
-	Embedded canvas apps can only be created via the host model-driven form. 
    - Adding existing canvas apps as embedded on model-driven forms is currently not supported.
    - Support to embed an existing canvas app in a model-driven form using App ID will be provided in a future update.
- When you view a model-driven form with an embedded canvas app, if you see an error message that reads "Sorry we didn't find that app" make sure that the embedded canvas app is in the same solution as the model-driven form.
- When you view a model-driven form with an embedded canvas app, if you see an error message that reads "It looks like you don’t have access to this app. Ask its owner to share it with you" make sure that the author has shared the embedded canvas app with you. More information: [Share an embedded canvas app](share-embedded-canvas-app.md).
- Adding a canvas app on the sub-grid control is no longer available.
    - In the preview release, makers were able to add a canvas app on a sub-grid control. With canvas app embedding on model-driven forms now generally available, adding an embedded canvas app on a model-driven form is streamlined to the field. 
    - This makes it easier for makers since they don't have to decide up front whether to pass the current (main form) record as data context or a list of records related to the current (main form) record. 
    - Makers always start with a field and can access both the current (main form) record or a list of records related to the current (main form) record.
    - To access the list of related records in the canvas app, makers can use the Common Data Service connector and [Filter](../canvas-apps/functions/function-filter-lookup.md) function with the [Improve data sources experience and Common Data Service views](https://powerapps.microsoft.com/blog/improved-data-source-selection-and-common-data-service-views/) capability enabled in the canvas app.  
    For example, to access the *Active Contacts* view of the *Contacts* entity, makers can use: *Filter(Contacts, 'Contacts (Views)'.'Active Contacts')*.
    - Existing canvas apps that use the sub-grid control will continue to work. However, we recommend that you migrate these apps to use a field instead. More information: [Migrating embedded canvas apps on model-driven forms that use a list of records related to the current (main form) record](embedded-canvas-app-migrate-from-preview.md#migrating-embedded-canvas-apps-on-model-driven-forms-that-use-a-list-of-records-related-to-the-current-main-form-record) for details.

## Enable an embedded canvas app
1. Select the field that is customized to display as an embedded canvas app.
2. In the **Field Properties** dialog, select the **Controls** tab.
3. In the list of controls select **Canvas app** and then select the **Web** option.
4. Select **OK**.

## Disable an embedded canvas app
1. Select the Field that is customized to display as an embedded canvas app.
2. In the **Field Properties** dialog, select the **Controls** tab.
3. In the list of controls select the default control and then select the **Web** option.
4. Select **OK**.

## Known issues and limitations with embedded canvas apps
- The canvas app custom control is only supported for use with the **Web** client type. Currently, the **Phone** and **Tablet** client types aren't supported.
- The ModelDrivenFormIntegration control does not provide a value for fields of a related entity. 
  - For example, when the ModelDrivenFormIntegration control is connected to the Accounts entity, using *ModelDrivenFormIntegration.Item.’Primary Contact’.’Full Name’* will not return a value. 
  - To access fields of a related entity makers can use either of the expressions listed here:
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
