---
title: "Guidelines on working with embedded canvas apps | MicrosoftDocs"
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

# Guidelines on working with embedded canvas apps
This topic provides guidelines on working with embedded canvas apps as well as helpful tips to troubleshoot any issues you might encounter.

-	Embedded canvas apps are supported on Unified Interface only and limited to online environments.
-	Embedded canvas apps are currently supported only on the web.
     - Support for tablet and mobile will be added in a future release.
-	You can only enable one embedded canvas app per form. 
     - You can have multiple embedded canvas apps added to the form but can only enable one at a time.
     - If you try to enable more than one embedded canvas app on a model-driven form you will get a message that reads “Only one canvas app can be enabled on a form.”.
     - Steps to enable or disable an embedded canvas app are provided later in this article.
-	Embedded canvas apps can only be created, edited and played via the host model-driven form.
     - You cannot create an embedded canvas app directly outside of the context of a model-driven form.
     - Similarly opening an embedded canvas app for editing or playing outside of the context of a model-driven form is not supported.

> [!NOTE]
> Currently you may be able to open an embedded canvas app for editing and/or playing outside of the model-driven form but this will be disabled in a future release.

-	When using a Sub-Grid control to add an embedded canvas app to a model-driven form
     - The data (fields and values) sent to the embedded canvas app at runtime is determined by the View. Only use fields in your embedded canvas app that are included in the View or add them to the View if needed. Any fields that are not included in the View will show empty values at runtime. 
     - The filter criteria for a View are not used at authoring time. Therefore the data that you see when authoring embedded canvas apps is not filtered, it is simple a list of top few records that you have access to. At runtime the filter criteria for the View will be applied as expected and you will only see relevant data.
-	When using a field control to add an embedded canvas app to a model-driven form always use a required field that is guaranteed to have a value. If your field does not have a value your embedded canvas app will not refresh in response to any change in data on the host model-driven form.
-	Publishing a model-driven form does not automatically publish embedded canvas apps.
     - Embedded canvas apps need to be published independent of the host model-driven form. 
     - More information: [Publish an app](../canvas-apps/save-publish-app.md#publish-an-app).
-	The Canvas app privilege in the Customization of a Security Role tab do not currently affect Canvas apps (embedded or standalone). For more information on sharing an embedded canvas app, please refer to: [Share an embedded canvas app](share-embedded-canvas-app.md).
-	If opening PowerApps Studio to create or edit an embedded canvas app via the Customize button in Canvas app control properties is blocked due to a web browser pop-up blocker you must enable the web.powerapps.com site or temporarily disable the pop-up blocker and then select Customize again.
-	Embedded canvas apps are not displayed when creating a new record since they need a record context to be passed to them.
     - Currently when creating a new record an embedded canvas app on a form is not displayed even after the record is saved. We are aware of this issue and will address it in a future release.
-	The ModelDrivenFormIntegration.Data object is read-only. 
     - To write back data you have to use the Common Data Service connector. 
     - If you are writing back the same data that is being displayed in the host model-driven form, the form will continue to display old data until it is refreshed. We are investigating ways to improve this experience.
-	The ModelDrivenFormIntegration.Data object is a list of records. 
     - Even the current record is passed to the embedded canvas app via ModelDrivenFormIntegration.Data as a list that contains a single record.
     - To directly reference the record you can use the [First function](../canvas-apps/functions/function-first-last.md). Example: First(ModelDrivenFormIntegration.Data).Name
-	The ModelDrivenFormIntegration.Data object currently does not work with the Display form and Edit form controls.
     - Support for Display form control is in-progress and will be included in some future release.
-	Manually changing the App ID in the Canvas app control properties is to be avoided as much as possible.
     - The App ID of the Canvas app is automatically generated and filled in for you. 
     - If for some reason you do need to manually edit it you need to ensure that any App ID you use corresponds to an embedded canvas app and not just a standalone canvas app.
     - The embedded canvas app must also be created with the same data context that your model-driven form is going to send.
     - After you have updated the App ID click on the Customize button to establish the connection to the new app.
- When viewing a model-driven form with an embedded canvas app, if you see an error message that reads "Sorry we didn't find that app." check to see that the embedded canvas app is in the same solution as the model-driven form and has been shared with the user.

## Enable an embedded canvas app
1. Select the Field or Sub-Grid control that is customized to display as an embedded canvas app.
2. In the **Field Properties** (or **Set Properties** for Sub-Grid) dialog, select the **Controls** tab.
3. In the list of controls select **Canvas app** and then select the **Web** option.
4. Select OK.

## Disable an embedded canvas app
1. Select the Field or Sub-Grid control that is customized to display as an embedded canvas app.
2. In the **Field Properties** (or **Set Properties** for Sub-Grid) dialog, select the **Controls** tab.
3. In the list of controls select the default control and then select the **Web** option.
4. Select OK.

## See also
[Embed a canvas app in a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass the current record as data context to an embedded canvas app](pass-current-embedded-canvas-app.md) <br />
[Pass a list of related records as data context to an embedded canvas app](pass-related-embedded-canvas-app.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md)
