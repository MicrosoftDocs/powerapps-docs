---
title: "Pass the current record as data context with an embedded canvas app | MicrosoftDocs"
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

# Pass the current record as data context to an embedded canvas app
This topic explains how to add an embedded canvas app and pass the current (main form) record as a data context to the embedded canvas app.

> [!NOTE]
> This feature is currently in preview. <br />
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)] 

Imagine that you want to add an embedded canvas app on an account main form and pass the current account record to the embedded canvas app. To do this, follow these steps: 

1.	Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and open the form editor for a main form of an entity, such as the account entity. 
2.	Select the section on the form where you want the embedded canvas app to appear.
3.	Using the field explorer pane, add a required field such as **Account Name**.
      > [!IMPORTANT]
      > Always use a required field that is guaranteed to have a value. If your field does not have a value, your embedded canvas app will not refresh in response to any change in data on the host model-driven form.
4.	With the field selected, on the **Home** tab on the ribbon, in the **Edit** group, select **Change Properties**.
5.	On the **Field Properties** dialog, select the **Controls** tab.
6.	On the **Controls** tab, select **Add Control...**.
7.	On the **Add Control** dialog, in the list of available controls, select **Canvas app** and then select **Add**.
8.	In the **Field Properties** dialog, in the list of controls select **Canvas app** and then select the **Web** option.
9.	In the section below the controls list, the list of properties available to the canvas app control are displayed.
     - The **Entity name** property specifies the entity that will provide the data to your embedded canvas app. It will be set to entity that contains the field you added in an earlier step.
     - Notice that, even though this property appears changeable, changing it has no effect on the embedded canvas app. It is meant to only serve as a reference for you.
     - The **App ID** property specifies the ID of the embedded canvas app. It will be automatically generated and filled-in for you when the canvas app is created.
     - Notice that, any change to the **App ID** value breaks the link from the model-driven form to the embedded canvas app.
10.	Select **Customize** to create or edit the canvas app. This opens PowerApps Studio in a new tab.
	   > [!NOTE]
       > If opening PowerApps Studio is blocked due to a web browser pop-up blocker you must enable the web.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again.
11.	In PowerApps Studio notice that there is a special **ModelDrivenFormIntegration** control in the left pane. This control is responsible for bringing contextual data from the host model-driven form to the embedded canvas app.
12.	Select the **Gallery1** control and observe that the **Items** property is set to **ModelDrivenFormIntegration.Data**.
      > [!NOTE]
      > ModelDrivenFormIntegration.Data is a list of records. In this example it has only one record. To directly reference the record you can use the First function. For example, *First(ModelDrivenFormIntegration.Data).Name*.
13.	In the property pane on the right, next to **Fields**, select **Edit**.
14.	In the data pane, change the field mapped to the **Title1** control to **Name** or another field that has data.
15.	Observe that the gallery displays the data being passed to it from the host model-driven form via the ModelDrivenFormIntegration control. Close the data pane.
16.	Select the **File** tab on the ribbon, and then select **App settings**.
17.	On the **Advanced settings** tab, in the **Experimental features** section, set **Enable app embedding user experience** to **On**.
18.	Select **Save**. 
19.	Select the **The cloud** tab. Provide a unique name for the app and then select **Save** located on the bottom right corner. Note the following: 
    -  Saving an app for the first time automatically publishes the app.
	  -  On a subsequent saves, select **Publish** and then select **Publish this version** to make your changes available.
20.	On the menu select **Back** and then select the browser tab that has the form editor open. Observe that the App ID property of the canvas app control now has a value automatically filled in. Note the following: 
    - 	The form editor has a direct link with PowerApps Studio that was opened in another browser tab in an earlier step.
    - 	The form editor "listens" for the **App ID** to be send to it.
    - 	The **App ID** is sent to the form editor when the app is saved.
21.	On the **Field Properties** dialog, select the **Display** tab.
22.	Uncheck **Display label** on the form and then select **OK**.
    - 	If you already have a canvas app embedded on this form a message is displayed that “Only one canvas app can be enabled on a form.” To add the new canvas app you must first disable the current one. <!-- (LINK TO ARTICLE #5 – ANCHOR-DISABLE-APP) --> Then, enable the new embedded canvas app. <!--(LINK TO ARTICLE #5 – ANCHOR-ENABLE-APP)  -->
23.	On the **Home** tab, select **Save**, and then select **Publish**.

When users open a model-driven app (Unified Interface only) that includes the form you have modified they see the embedded canvas app on the form. Changing the record displayed on the main form changes the data context that is passed to the form and the embedded app refreshes to show the relevant data.

This topic showed you how to get started with embedding a canvas app in a model-driven form. You can further customize the embedded canvas app to connect and bring in data from a variety of data sources. Use the Filter, Search and LookUp functions and the context passed in from the host model-driven form to filter or find specific records in those data sources. Use the WYSIWYG canvas app editor to easily design the interface to match your requirements.

## See also
[Embed a canvas app in a model-driven form](embed-canvas-app-in-form.md) <br />
[Pass a list of related records as data context to an embedded canvas app](pass-related-embedded-canvas-app.md)