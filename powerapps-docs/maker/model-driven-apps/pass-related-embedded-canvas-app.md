---
title: "Pass a list of related rows as data context with an embedded canvas app | MicrosoftDocs"
description: Learn how to pass a list of related rows as data context in an embedded canvas app
ms.custom: ""
ms.date: 06/25/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
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

# Pass a list of related rows as data context to an embedded canvas app
> [!IMPORTANT]
> Canvas apps embedded on model-driven forms are now out of preview and generally available. The steps listed below are outdated and applicable only to the public preview release of canvas apps embedded on model-driven forms.
>  For the updated list of steps for the latest release, please see: [Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md)

This topic explains how to add an embedded canvas app and pass a list of rows related to the current (main form) row as a data context to the embedded canvas app.

Let's say you want to add an embedded canvas app on an account main form and pass a list of contacts related to the current account row to the embedded canvas app. To do this, follow these steps:

1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and open the form editor for a main form of a table, such as the account table.
2.	Select the section on the form where you want the embedded canvas app to appear.
3.	With the section selected, on the **Insert** tab, in the **Control** group, select **Sub-Grid**.
4.	In the **Set Properties** dialog box, select the **Display** tab, and then in the **Name** box enter a name for the grid control.
5.  In the **Data Source** section, select an **Table** and **Default View** that corresponds to the list of rows that you want to pass as data context to the embedded canvas app.
6. Select the **Controls** tab, and then select **Add Control…**
7. In the **Add Control** dialog box, in the list of available controls, select **Canvas app** and then select **Add**.
8. In the **Set Properties** dialog box, in the list of controls select **Canvas app** and then select the **Web** option.
9. In the section below the controls list, see the list of properties corresponding to the Canvas app control and note the following:
     - The **Table name** property specifies the table that will provide the data to your embedded canvas app. It will be set to the table that you selected earlier.
         -  Even though this property appears changeable, changing it has no effect on the embedded canvas app. It is meant only to serve as a reference for you.
     -  The **View name** property specifies the view of the table that will be used to filter the data provided to your embedded canvas app. It will be set to the **Default View** you selected earlier.
         -  The data (fields and values) sent to the embedded canvas app at runtime are determined by this view. Only use columns in your canvas app that are included in the view or add them to the view if needed. Any columns that are not included in the view display as empty values at runtime.
         -  The filter criteria for a view are not used at authoring time. Therefore, the data that you see when authoring embedded canvas apps is not filtered, it is simply a list of top few rows that you have access to. At runtime, the filter criteria for the view are applied as expected so users only see relevant data.
     -  The **App ID** property specifies the ID of the embedded canvas app. It is automatically generated and filled-in for you when the canvas app is created.
         - 	Notice that any change to the App ID value breaks the link from the model-driven form to the embedded canvas app.
10.	Select the **Customize** button to create or edit the canvas app. This opens Power Apps Studio in a new browser tab.
	 > [!IMPORTANT]
     > If opening Power Apps Studio is blocked due to a web browser pop-up blocker, you must enable the make.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again. 
11.	In Power Apps Studio, notice that there is a **ModelDrivenFormIntegration** control located in the left pane. This control is responsible for bringing contextual data from the host model-driven form to the embedded canvas app. 
12.	Select the **Gallery1** control and observe that the **Items** property is set to **ModelDrivenFormIntegration.Data**.
13.	In the property pane on the right, next to **Columns**, select **Edit**.
14.	In the data pane, change the column mapped to the **Title1** control to **FullName** or another column that has data.
15.	Observe that the gallery displays the data being passed to it from the host model-driven form via the **ModelDrivenFormIntegration** control. Close the data pane.
16.	Select the **File** tab, and select **App settings**.
17.	On the **Advanced settings** tab, in the **Experimental features** section, set **Enable app embedding user experience** to **On**.
18. Select **Save**. 
19. Select the **The cloud** tab, provide a unique name for the app, and then select **Save** located on the lower right. Note the following: 
    -  Saving an app for the first time automatically publishes the app. 
	  -  On subsequent saves you must select **Publish** and then **Publish this version** to make your changes available.
20.	Select **Back**, and then select the browser tab that has the form editor open. 
21.	Observe that the **App ID** property of the **Canvas app** control now has a value automatically filled in. Note the following: 
     - 	The form editor has a direct link with Power Apps Studio that was opened in another browser tab in an earlier step.
     - 	The form editor has been listening for the App ID to be sent to it.
     - 	The App ID was sent to it when the app was saved.
22.	In the **Set Properties** dialog box, select the **Display** tab, clear **Display label on the form**, and then select **OK**.
     - If you already have a canvas app embedded on this form, a message is displayed that “Only one canvas app can be enabled on a form.” To add the new canvas app you must first [disable the current embedded canvas app](embedded-canvas-app-guidelines.md#disable-an-embedded-canvas-app). Then, [enable the new embedded canvas app](embedded-canvas-app-guidelines.md#enable-an-embedded-canvas-app).
23.	On the **Home** tab, select **Save**, and then select **Publish**.

After you have added an embedded canvas app to your model-driven form, share your embedded canvas app with other users. More information: [Share an embedded canvas app](share-embedded-canvas-app.md).

When users open a model-driven app (Unified Interface only) that includes the form you have modified, they see the embedded canvas app on the form. Changing the row displayed on the main form changes the data context that is passed to the form and the embedded app refreshes to show the relevant data.

This topic showed you how to get started with the embedding a canvas app in a model-driven form. You can further customize the embedded canvas app to connect and bring in data from a variety of data sources. Use the Filter, Search, and LookUp functions and the context passed in from the host model-driven form to filter or find specific rows in those data sources. Use the WYSIWYG canvas app editor to easily design the interface to match your requirements.

## See also
[Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md) <br />
[Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md) <br />
[Edit a canvas app embedded on a model-driven form](embedded-canvas-app-edit-classic-designer.md) <br />
[Customize the screen size and orientation of a canvas app embedded on a model-driven form](embedded-canvas-app-customize-screen.md) <br />
[Perform predefined actions on the host form from within an embedded canvas app](embedded-canvas-app-actions.md) <br />
[ModelDrivenFormIntegration control's properties and actions](embedded-canvas-app-properties-actions.md) <br />
[Share an embedded canvas app](share-embedded-canvas-app.md) <br />
[Guidelines on working with embedded canvas apps](embedded-canvas-app-guidelines.md) <br />
[Migrating embedded canvas apps on model-driven forms created using the public preview release to latest](embedded-canvas-app-migrate-from-preview.md) <br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]