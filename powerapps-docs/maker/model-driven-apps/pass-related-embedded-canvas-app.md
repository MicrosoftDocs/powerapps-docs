---
title: "Pass a list of related records as data context with an embedded canvas app | MicrosoftDocs"
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
author: "Mattp123"
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

# Pass a list of related records as data context to an embedded canvas app

This topic explains how to add an embedded canvas app and pass a list of records related to the current (main form) record as a data context to the embedded canvas app.

> [!NOTE]
> This feature is currently in preview. <br />
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Imagine that you want to add an embedded canvas app on an account main form and pass a list of contacts related to the current account record to the embedded canvas app. To do this, follow these steps:

1.	Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and open the form editor for a main form of an entity, such as the account entity.
2.	Select the section on the form where you want the embedded canvas app to appear.
3.	With the section selected, on the **Insert** tab, in the **Control** group, select **Sub-Grid**.
4.	In the **Set Properties** dialog: 
   1. Select the **Display** tab, and then in the in the **Name** box enter a name for the grid control.
   2. In the **Data Source** section, select an **Entity** and **Default View** that corresponds to the list of records that you want to pass as data context to the embedded canvas app.
   3. Select the **Controls** tab, and then select **Add Control…**
   4. In the **Add Control** dialog, in the list of available controls, select **Canvas app** and then select **Add**.
   5. In the **Field Properties** dialog, in the list of controls select **Canvas app** and then select the **Web** option.
   6.	In the section below the controls list, see the list of properties corresponding to the Canvas app control and note the following:
    - 	The **Entity name** property specifies the entity that will provide the data to your embedded canvas app. It will be set to the entity that you selected earlier.
        -  Even though this property appears changeable, changing it has no effect on the embedded canvas app. It is meant to only serve as a reference for you.
    -  The **View name** property specifies the view of the entity that will be used to filter the data provided to your embedded canvas app. It will be set to the **Default View** you selected earlier.
        -  The data (fields and values) sent to the embedded canvas app at runtime are determined by this view. Only use fields in your canvas app that are included in the view or add them to the view if needed. Any fields that are not included in the view display as empty values at runtime.
        -  The filter criteria for a view are not used at authoring time. Therefore, the data that you see when authoring embedded canvas apps is not filtered, it is simply a list of top few records that you have access to. At runtime, the filter criteria for the view are applied as expected users only see relevant data.
    -  The **App ID** property specifies the ID of the embedded canvas app. It is automatically generated and filled-in for you when the canvas app is created.
        - 	Notice that any change to the App ID value breaks the link from the model-driven form to the embedded canvas app.
7.	Select the **Customize** button to create or edit the canvas app. This opens PowerApps Studio in a new browser tab.
	 > [!IMPORTANT]
     > If opening PowerApps Studio is blocked due to a web browser pop-up blocker you must enable the web.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again. 
8.	In PowerApps Studio notice that there is a **ModelDrivenFormIntegration** control located in the the left pane. This control is responsible for bringing contextual data from the host model-driven form to the embedded canvas app. 
9.	Select the **Gallery1** control and observe that its **Items** property is set to **ModelDrivenFormIntegration.Data**.
10.	In the property pane on the right, next to **Fields**, select **Edit**.
11.	In the data pane, change the field mapped to the **Title1** control to **FullName** or another field that has data.
12.	Observe that the gallery is displaying the data being passed to it from the host model-driven form via the **ModelDrivenFormIntegration** control, and then close the data pane.
13.	Select the **File** tab, and select **App settings**.
14.	On the **Advanced settings** tab, in the **Experimental features** section, select **On** next to **Enable app embedding user experience**, and the select Save.
1. Select the **The cloud** tab, provide a unique name for the app, and then select **Save** (bottom right). Note the following: 
    - Saving an app for the first time automatically publishes the app. 
	  - On subsequent saves you must select **Publish** and then **Publish this version** to make your changes available.
16.	Select **Back**, and then select the browser tab that has the form editor open. 
17.	Observe that the **App ID** property of the **Canvas app** control now has a value automatically filled in. Note the following: 
     - 	The form editor has a direct link with PowerApps Studio that was opened in another browser tab in an earlier step.
     - 	The form editor has been listening for the App ID to be sent to it.
     - 	The App ID was sent to it when the app was saved.
18.	In the **Field Properties** dialog, select the **Display** tab, clear **Display label on the form**, and then select **OK**.
     - If you already have a canvas app embedded on this form a message is displayed that “Only one canvas app can be enabled on a form.” To add the new canvas app you must first disable the current one. <!-- (LINK TO ARTICLE #5 – ANCHOR-DISABLE-APP)--> Then, enable the new embedded canvas app. <!-- (LINK TO ARTICLE #5 – ANCHOR-ENABLE-APP)   -->
19.	On the **Home** tab select **Save**, and then select **Publish**.

When users open a model-driven app (Unified Interface only) that includes the form you have modified they see the embedded canvas app on the form. Changing the record displayed on the main form changes the data context that is passed to the form and the embedded app refreshes to show the relevant data.

This topic showed you how to get started with the embedding a canvas app in a model-driven form. You can further customize the embedded canvas app to connect and bring in data from a variety of data sources. Use the Filter, Search and LookUp functions and the context passed in from the host model-driven form to filter or find specific records in those data sources. Use the WYSIWYG canvas app editor to easily design the interface to match your requirements.

## See also
[Embed a canvas app in a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass the current record as data context to an embedded canvas app](pass-current-embedded-canvas-app.md)