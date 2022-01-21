---
title: Using Power Automate pane (preview)
description: Learn about how to use Power Automate pane to work with flows in Power Apps
author: TashasEv
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/20/2022
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - TashasEv
---

# Using Power Automate pane (preview)

[This article is pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This feature is being rolled out and depending on your region, it may not be available for your tenant yet.
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

With this feature, you can create new flows, or add existing flows, and even edit existing flows using Power Automate pane within Power Apps Studio. You don't have to browse to Power Automate to work with flows and return to Power Apps Studio any longer.

> [!NOTE]
> This feature must be enabled on a per-app basis.

## Enable Power Automate pane

Power Automate pane needs to be enabled manually through the feature switch. To enable the pane:

1. Open a [new](data-platform-create-app.md) or [existing](edit-app.md) an app in Power Apps Studio.

1. Select **Settings** at the top. 

1. Select **Upcoming Features**. 

1. Under the **Preview** tab, select **Enable Power Automate pane** to turn on this feature. You may be prompted to close and reopen your canvas app to see the change. 
   
   :::image type="content" source="media/work-with-flows/power-automate-pane-feature.png" alt-text="A screenshot of the Upcoming Features dialog box showing the Enable Power Automate feature toggle.":::
   
    The Power Automate option is added to the left-pane.

   :::image type="content" source="media/work-with-flows/power-automate-button.png" alt-text="A screenshow highlighting the Power Automate option in the left pane":::   

## Creating a new flow

To start with flows inside Power Apps Studio, select **Create new flow** in Power Automate pane.

   :::image type="content" source="media/work-with-flows/create-new-flow.png" alt-text="A screenshow showing Create your flow screen having several options to choose a flow template from.":::

This action opens the **Create your flow** modal dialog within Power Apps Studio. You can choose to create the flow from several available templates, or start with a blank template.

### Start with a template

Power Automate provides several flow templates that you can choose from by default. This section explains how to create a flow using such available templates from within Power Apps Studio.

1. From the list of available templates, select a template of your choice. For this example, we'll use **Click a button in Power Apps to send an email**.

   :::image type="content" source="media/work-with-flows/selected-flow-template.png" alt-text="A screenshow showing Click a button in Power Apps to send an email template.":::

3.  The next step shows the connections required to create a flow based on the template selected. &lt;&lt;Learn more about connections&gt;&gt;  
    ![Graphical user interface  text  application  email Description automatically generated](media/work-with-flows/image4.png)

4.  Optionally, selecting "Edit in advanced mode" here prompts you to accept any connections used within the flow template. Select "Continue" to accept the connections.  
    ![Graphical user interface  application  Teams Description automatically generated](media/work-with-flows/image5.png)

5.  The copy of the selected flow template now opens in the modal in edit mode. You can make changes to the flow here prior to saving.  
    ![Graphical user interface  application  Teams Description automatically generated](media/work-with-flows/image6.png)

6.  Once you have added the desired changes, save the flow using either Save button at the top right of the modal or the Save button below the body of the flow.  
    ![Graphical user interface Description automatically generated with medium confidence](media/work-with-flows/image7.png)  
    ![Graphical user interface  text  application  email Description automatically generated](media/work-with-flows/image8.png)

7.  Upon successfully saving the flow, it has been added to the app and appears under "In your app" in the Power Automate pane:  
    ![Graphical user interface  text  application Description automatically generated](media/work-with-flows/image9.png)

## Create from blank

Instead of using a template, you can also create your cloud flow from blank.

1.  Select "+ Add flow" in the Power Automate pane, then select "Add new flow":  
    ![Graphical user interface  text  application Description automatically generated](media/work-with-flows/image10.png)

2.  Select "+ Create from blank"  
    ![Graphical user interface  text  application  chat or text message Description automatically generated](media/work-with-flows/image11.png)

3.  The cloud flow editing screen appears, showing the Power Apps trigger:  
    ![A picture containing calendar Description automatically generated](media/work-with-flows/image12.png)

4.  Continue to create your custom flow by adding new steps using the "+ New step" button.  
    ![Graphical user interface  application Description automatically generated](media/work-with-flows/image13.png)

5.  Once complete, save the flow using either Save button at the top right of the modal or the Save button below the body of the flow.  
    ![Graphical user interface Description automatically generated with medium confidence](media/work-with-flows/image7.png)

## Adding an Existing Flow

You may have access to flows which already existed in the environment in which you're creating your app. To add these flows for use in your app:

1.  Select "+ Add flow" in the Power Automate pane. The "Add a flow" flyout opens, showing flows you have access to which are eligible for adding to your app.  
    ![Graphical user interface  application Description automatically generated](media/work-with-flows/image14.png)

&lt;&lt; TODO: validate these criteria for M2&gt;&gt;

Note: the following criteria determine whether flows are eligible for adding to your app:

-   You must have access to the flow

-   The flow must be in the same environment as the app

-   If the app is part of a solution, only flows that are part of a solution in the same environment will be shown

-   Only flows with a Power Apps trigger are eligible for adding to a canvas app for use in the app

2.  Hovering over the flow shows details about the flow. Select one to add it to your app

3.  Upon successfully adding the flow, it appears under "In your app" in the Power Automate pane:  
    ![Graphical user interface  text  application Description automatically generated](media/work-with-flows/image15.png)

## Editing an existing Flow

You can now edit flows added to your app without leaving the context of your app. To edit a flow:

1.  Under the "In your app" section of the Power Automate pane, click the ellipsis to the right of a flow to open the context menu. Select "Edit"

![Graphical user interface  application  Teams Description automatically generated](media/work-with-flows/image16.png)

2.  The flow designer opens, allowing you to edit and save your flow. &lt;&lt;TODO: Add screen capture&gt;&gt;

3.  If you attempt to close the designer without saving, you'll be prompted that you may lose unsaved changes if you continue &lt;&lt;TODO: Add screen capture&gt;&gt;

4.  Save the changes, and close the designer

5.  The flow refreshes to include the new changes

## Refresh a Flow

If you make changes to your flow in Power Automate instead of Power Apps while the app is open, you will need to refresh your flow to get the changes. To refresh the flow:

1.  Under the "In your app" section of the Power Automate pane, click the ellipsis to the right of a flow to open the context menu. Select "Refresh"  
    ![Graphical user interface  application  Teams Description automatically generated](media/work-with-flows/image17.png)

2.  A loading spinner appears and the flow is refreshed

## Remove a Flow

To remove a flow from your app:

1.  Under the "In your app" section of the Power Automate pane, click the ellipsis to the right of a flow to open the context menu. Select "Remove from app"  
    ![Graphical user interface  application  Teams Description automatically generated](media/work-with-flows/image18.png)

2.  The flow is removed from the app. The flow is not deleted from the environment; however, so you can re-add the flow to your app or another app as required.

### See also

[Add and configure controls](add-configure-controls.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

 

