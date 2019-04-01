---
title: "Guidelines on working with embedded canvas apps | MicrosoftDocs"
ms.custom: ""
ms.date: 01/07/2019
ms.reviewer: ""
ms.service: powerapps
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

# Guidelines on working with embedded canvas apps
[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This topic provides guidelines on working with embedded canvas apps as well as helpful tips to troubleshoot any issues you might encounter.

-	Embedded canvas apps are only supported with Unified Interface model-driven apps.
-	You can only enable one embedded canvas app per form. 
     - You can have multiple embedded canvas apps added to the form but can only enable one at a time.
     - If you try to enable more than one embedded canvas app on a model-driven form you will get a message that reads “Only one canvas app can be enabled on a form.”
     - To enable or disable an embedded canvas app see [Enable an embedded canvas app](#enable-an-embedded-canvas-app) and [Disable an embedded canvas app](#disable-an-embedded-canvas-app).
-	Embedded canvas apps can only be created, edited and played via the host model-driven form.
     - You can't create an embedded canvas app directly outside of the context of a model-driven form.
     - Similarly opening an embedded canvas app for editing or playing outside of the context of a model-driven form is not supported.

     > [!NOTE]
     > Although you may be able to open an embedded canvas app outside of a model-driven app, this is not supported.

-	Note the following when you use a sub-grid control to add an embedded canvas app to a model-driven form.
     - The data (fields and values) sent to the embedded canvas app at runtime are determined by the view that is specified as the **Default View** in the **Data Source** section of the sub-grid control’s properties. Only use fields in your embedded canvas app that are included in the view or add them to the view if needed. Any fields that are not included in the view will show empty values at runtime. 
     - The filter criteria for a view are not used at authoring time. Therefore, the data that you see when authoring embedded canvas apps is not filtered, it is simply a list of the top few records that you have access to. At runtime, the filter criteria for the view are applied as expected and only relevant data is displayed.
-	When using a field control to add an embedded canvas app to a model-driven form always use a required field that is guaranteed to have a value. If your field does not have a value your embedded canvas app will not refresh in response to any change in data on the host model-driven form.
-	Publishing a model-driven form does not also publish the embedded canvas app.
     - Embedded canvas apps need to be published independent of the host model-driven form. More information: [Publish an app](../canvas-apps/save-publish-app.md#publish-an-app).
-	If opening PowerApps Studio to create or edit an embedded canvas app via the **Customize** button in the canvas app control properties is blocked due to a web browser pop-up blocker, you must enable the web.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again.
-	Embedded canvas apps are not displayed when creating a new record since they need a record context to be passed to them.
-	The ModelDrivenFormIntegration.Data object is read-only. 
     - To write back data you must use the Common Data Service connector. More information: [Common Data Service](/connectors/commondataservice/)
-	The ModelDrivenFormIntegration.Data object is a list of records. 
     - Even the current record is passed to the embedded canvas app via ModelDrivenFormIntegration.Data as a list that contains a single record.
     - To directly reference the record you can use the [First function](../canvas-apps/functions/function-first-last.md). Example: First(ModelDrivenFormIntegration.Data).Name
-	Manually changing the App ID in the canvas app control properties is to be avoided as much as possible.
     - The App ID of the canvas app is automatically generated and filled in for you. 
     - If for some reason you do need to manually edit it, you need to ensure that any App ID you use corresponds to an *embedded* canvas app and not just a standalone canvas app. 
     - The embedded canvas app must also be created with the same data context that your model-driven form is going to send.
     - After you have updated the App ID select **Customize** to open it in PowerApps Studio and establish the connection to the new app.
     - Make a small change in the app to put it in an unsaved state, then save and publish the app.
- When you view a model-driven form with an embedded canvas app, if you see an error message that reads "Sorry we didn't find that app" make sure that the embedded canvas app is in the same solution as the model-driven form.
- When you view a model-driven form with an embedded canvas app, if you see an error message that reads "It looks like you don’t have access to this app. Ask its owner to share it with you" make sure that the author has shared the embedded canvas app with you. More information: [Share an embedded canvas app](share-embedded-canvas-app.md).

## Enable an embedded canvas app
1. Select the field or sub-grid control that is customized to display as an embedded canvas app.
2. In the **Field Properties** (or **Set Properties** for sub-grid) dialog, select the **Controls** tab.
3. In the list of controls select **Canvas app** and then select the **Web** option.
4. Select **OK**.

## Disable an embedded canvas app
1. Select the Field or sub-grid control that is customized to display as an embedded canvas app.
2. In the **Field Properties** (or **Set Properties** for sub-grid) dialog, select the **Controls** tab.
3. In the list of controls select the default control and then select the **Web** option.
4. Select **OK**.

## Known issues and limitations with embedded canvas apps
- The canvas app custom control is only supported for use with the **Web** client type. Currently, the **Phone** and **Tablet** client types aren't supported. More information: [Use custom controls for model-driven app data visualizations](use-custom-controls-data-visualizations.md)
- When you create a new record, an embedded canvas app on a form is not displayed even after the record is saved. 
-    The ModelDrivenFormIntegration.Data object currently does not work with the Display form and Edit form controls.
- You can’t use the **Canvas App** privilege in a security role to grant app users access to either an embedded or standalone canvas app. For more information on sharing an embedded canvas app, please refer to: [Share an embedded canvas app](share-embedded-canvas-app.md).
- If you write back the same data that is being displayed in the host model-driven form, the form will continue to display old data until it is refreshed. An easy way to do that is to use the [RefreshForm](embedded-canvas-app-actions.md) method.
- > If you do not see the IntelliSense for the [methods to perform predefined actions](embedded-canvas-app-actions.md) in embedded canvas apps that were created prior to the functionality being made available; save, close and re-open the app. 

## See also
[Embed a canvas app in a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass the current record as data context to an embedded canvas app](pass-current-embedded-canvas-app.md) <br />
[Pass a list of related records as data context to an embedded canvas app](pass-related-embedded-canvas-app.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md)
