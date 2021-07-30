---
title: "Pass the current row as data context with an embedded canvas app | MicrosoftDocs"
description: Learn how to pass the current row as data context in an embedded canvas app
ms.custom: ""
ms.date: 07/29/2021
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

# Pass the current row as data context to an embedded canvas app

> [!IMPORTANT]
> Canvas apps embedded on model-driven forms are now out of preview and generally available. The steps listed below are outdated and applicable only to the public preview release of canvas apps embedded on model-driven forms.
>  For the updated list of steps for the latest release, please see: [Add an embedded canvas app on a model-driven form](embedded-canvas-app-add-classic-designer.md)

This topic explains how to add an embedded canvas app and pass the current (main form) row as a data context to the embedded canvas app.

Imagine that you want to add an embedded canvas app on an account main form and pass the current account row to the embedded canvas app. To do this, follow these steps: 

1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and open the form editor for a main form of a table, such as the account table. 
2.	Select the section on the form where you want the embedded canvas app to appear.
3.	Using the column explorer pane, add a required column, such as **Account Name**.
      > [!IMPORTANT]
      > Always use a required column that is guaranteed to have a value. If your column does not have a value, your embedded canvas app will not refresh in response to any change in data on the host model-driven form.
4.	With the column selected, on the **Home** tab in the **Edit** group, select **Change Properties**.
5.	On the **Column Properties** dialog box, select the **Controls** tab.
6.	On the **Controls** tab, select **Add Control...**.
7.	On the **Add Control** dialog box, in the list of available controls, select **Canvas app** and then select **Add**.
8.	In the **Column Properties** dialog box, in the list of controls select **Canvas app**, and then select the **Web** option.
9.	In the section below the controls list, the list of properties available to the canvas app control are displayed.
     - The **Table name** property specifies the table that will provide the data to your embedded canvas app. It will be set to the table that contains the column you added in an earlier step.
         - Notice that, even though this property appears changeable, changing it has no effect on the embedded canvas app. It is meant only to serve as a reference for you.
     - The **App ID** property specifies the ID of the embedded canvas app. It will be automatically generated and filled-in for you when the canvas app is created.
         - Notice that any change to the **App ID** value breaks the link from the model-driven form to the embedded canvas app.
10.	Select **Customize** to create or edit the canvas app. This opens Power Apps Studio in a new tab.
	   > [!NOTE]
     > - The **Customize** option is currently only available by using the classic form designer.
     > - If opening Power Apps Studio is blocked due to a web browser pop-up blocker you must enable the make.powerapps.com site or temporarily disable the pop-up blocker and then select **Customize** again.
11.	In Power Apps Studio notice that there is a special **ModelDrivenFormIntegration** control in the left pane. This control is responsible for bringing contextual data from the host model-driven form to the embedded canvas app.
12.	Select the **Gallery1** control and observe that the **Items** property is set to **ModelDrivenFormIntegration.Data**.
      > [!NOTE]
      > ModelDrivenFormIntegration.Data is a list of rows. In this example it has only one row. To directly reference the row you can use the First function. For example, *First(ModelDrivenFormIntegration.Data).Name*.
13.	In the property pane on the right, next to **Columns**, select **Edit**.
14.	In the data pane, change the column mapped to the **Title1** control to **Name** or another column that has data.
15.	Observe that the gallery displays the data being passed to it from the host model-driven form via the ModelDrivenFormIntegration control. Close the data pane.
16.	Select the **File** tab, and then select **Settings**.
17.	On the **Upcoming features** tab, in the **Experimental features** section, set **Optimize embedding appearance** to **On**.
18.	Select the **General** tab. Provide a unique name for the app and then select **Save**. Note the following: 
    -  Saving an app for the first time automatically publishes the app.
	  -  On subsequent saves, select **Publish** and then select **Publish this version** to make your changes available.
19. Close the **Settings** dialog.
20.	On the menu, select **Back** and then select the browser tab that has the form editor open. Observe that the **App ID** property of the canvas app control now has a value automatically filled in. Note the following: 
    - 	The form editor has a direct link with Power Apps Studio that was opened in another browser tab in an earlier step.
    - 	The form editor "listens" for the **App ID** to be sent to it.
    - 	The **App ID** is sent to the form editor when the app is saved.
21.	On the **Column Properties** dialog box, select the **Display** tab.
22.	Clear **Display label** on the form and then select **OK**.
    - 	If you already have a canvas app embedded on this form, a message is displayed that “Only one canvas app can be enabled on a form.” To add the new canvas app you must first [disable the current embedded canvas app](embedded-canvas-app-guidelines.md#disable-an-embedded-canvas-app). Then, [enable the new embedded canvas app](embedded-canvas-app-guidelines.md#enable-an-embedded-canvas-app).
23.	On the **Home** tab, select **Save**, and then select **Publish**.

After you have added an embedded canvas app to your model-driven form, share your embedded canvas app with other users. More information: [Share an embedded canvas app](share-embedded-canvas-app.md).

When users open a model-driven app (Unified Interface only) that includes the form you have modified, they see the embedded canvas app on the form. Changing the row displayed on the main form changes the data context that is passed to the form, and the embedded app refreshes to show the relevant data.

This topic showed you how to get started with embedding a canvas app in a model-driven form. You can further customize the embedded canvas app to connect and bring in data from a variety of data sources. Use the Filter, Search, and LookUp functions and the context passed in from the host model-driven form to filter or find specific rows in those data sources. Use the WYSIWYG canvas app editor to easily design the interface to match your requirements.

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