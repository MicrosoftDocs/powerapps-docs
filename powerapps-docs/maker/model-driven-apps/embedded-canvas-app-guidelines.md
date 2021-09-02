---
title: "Guidelines and troubleshooting when working with embedded canvas apps | MicrosoftDocs"
description: Understand the recommended ways to work with embedded canvas apps in Power Apps
ms.custom: ""
ms.date: 09/02/2021
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "troubleshooting"
author: "RichdiMSFT"
ms.subservice: mda-maker
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
# Guidelines and troubleshooting for embedded canvas apps

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

## Saving data in an embedded canvas app
- A save event made from a model-driven app, such as selecting the Save button on the main form command bar, doesn’t save changes made in the embedded canvas app. 
- To save changes made in an embedded canvas app, use the [Dataverse connector](/connectors/commondataserviceforapps/).
- The ModelDrivenFormIntegration control OnDataRefresh action should only be used to refresh data within the embedded canvas app. We don’t recommend that you use the OnDataRefresh action to save changes within the embedded canvas app. 

## Known issues and limitations with embedded canvas apps

### Limitations

- The canvas app custom control is only supported for use with the **Web** client type. Currently, the **Phone** and **Tablet** client types aren't supported.
- You can’t use the **Canvas App** privilege in a security role to grant app users access to either an embedded or standalone canvas app. For more information on sharing an embedded canvas app, please refer to: [Share an embedded canvas app](share-embedded-canvas-app.md).
- If you write back the same data that is being displayed in the host model-driven form, the form will continue to display old data until it is refreshed. An easy way to do that is to use the [RefreshForm](embedded-canvas-app-actions.md#refreshformshowprompt) method.

### The ModelDrivenFormIntegration control doesn't provide a value for columns of a related table

For example, when the ModelDrivenFormIntegration control is connected to the Accounts table, using *ModelDrivenFormIntegration.Item.’Primary Contact’.’Full Name’* will not return a value. 

To access columns of a related table makers can use either of the expressions listed here:
    - *LookUp(Accounts, Account = GUID(First(ModelDrivenFormIntegration.Data).ItemId)).'Primary Contact'.'Full Name'*  
      - *ItemId* is empty at authoring time but will have a value at runtime.
    - *LookUp(Accounts, Account = ModelDrivenFormIntegration.Item.Account).'Primary Contact'.'Full Name'* (This expression is easier to read, but the previous expression will perform slightly better.)

### Embedded canvas app doesn’t render correctly

An embedded canvas app may not render correctly within the field on the model-driven app form, such as additional whitespace or scroll bars around the canvas app.
This issue can occur when one or both of the following are true.

- The **Scale to fit** option isn’t enabled with the canvas app. 
- The **App Name** property value is missing or is incorrectly defined in the embedded canvas app control.  This might occur when the model-driven app and canvas app have been imported as a solution into another Dataverse environment.

#### Enable scale to fit

By default, canvas apps have the scale to fit option enabled.
1. Open the canvas app that you’re embedding on a model-driven app form for editing.
1. In Power Apps studio, select **File** > **Settings** > **Screen size + orientation**. 
1. Under **Advanced Settings**, set **Scale to fit** to **On**.
   :::image type="content" source="media/scale-to-fit-canvas-app.png" alt-text="Scale to fit canvas app setting.":::

#### The App Name property value is missing or is incorrectly defined

To resolve this issue, choose the correct option:
- Managed solutions: If the solution was imported into an environment as a managed solution, follow these steps: 
   1. Sign into Power Apps and go to the development environment where you originally created your embedded canvas app. This is also the environment where the solution was exported.
   1. Open the unmanaged solution that includes the canvas app, and then find the canvas app in the list of solution components. Copy the canvas app **Name** exactly as it appears in the components list. For example, *contoso_flooringestimatesapp_624d7*.
   :::image type="content" source="media/copy-canvas-app-name.png" alt-text="Copy the canvas app unique name.":::

   1. In the same solution, edit the model-driven app that has the embedded canvas app control, and then set the canvas **App Name** to the embedded canvas app control using the value from the previous step. More information: [Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md)
   1. Export the solution from the development environment and then import the solution into your target environment.

- Unmanaged solutions: If the solution was imported into an environment as an unmanaged solution, edit the model-driven app, that has the embedded canvas app control, and then follow similar steps as described for a managed solution to set the canvas **App Name** property.

#### Error message: "You don’t have read privileges for the Canvas App entity. Please contact your administrator"

The error message is displayed on the model-driven app form where the embedded canvas app should appear.

This issue occurs because the app user doesn't have read access to the CanvasApp Extended Metadata table. To resolve this issue, add the user to a security role used for the app that has read access to the CanvasApp Extended Metadata table.

##### Grant read privileges for the CanvasApp Extended Metadata table

1. In Power Apps, on the left navigation pane select **Apps**, select the app you want, select **…**, and then select **Share**.
1. On the left pane, select the app, and then select **Manage security roles**.
1. Open the security role assigned to the app, such as the Basic User security role.
1. Select the **Custom Entities** tab, and set organization scope read privileges for the **CanvasApp Extended Metadata** table.
   :::image type="content" source="media/read-priv-canvasapp-ext-meta.png" alt-text="Set organization scope read privilege on the CanvasApp Extended Metadata table":::
1. Select **Save and Close** to close the security role window.

#### Embedded canvas app control loads the canvas app from a different environment

When a solution that contains a model-driven app with an embedded canvas app is imported into a target environment, the control loads the canvas app from the source environment (where the solution was exported). The control should load the canvas app from the target (current) environment.

This issue occurs because the app user doesn't have read access to the CanvasApp Extended Metadata table. To resolve this issue, add the user to a security role used for the app that has read access to the CanvasApp Extended Metadata table. More information: [Grant read privileges for the CanvasApp Extended Metadata table](#grant-read-privileges-for-the-canvasapp-extended-metadata-table)

### See also

[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]