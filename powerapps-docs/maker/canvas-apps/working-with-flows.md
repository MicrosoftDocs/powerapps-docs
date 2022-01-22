---
title: Use Power Automate pane (preview)
description: Learn about how to use Power Automate pane to work with flows in Power Apps
author: TashasEv
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/21/2022
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

# Use Power Automate pane (preview)

[This article is pre-release documentation and is subject to change.]

You can now create new flows, or add existing flows, and even edit existing flows using Power Automate pane within Power Apps Studio. You don't have to browse to [Power Automate](https://flow.microsoft.com) to work with flows and then return to Power Apps Studio for app editing. In order to use this capability, you'll have to enable the **Power Automate pane** setting.

> [!NOTE]
> - This feature must be enabled on a per-app basis.
> - Flows that you create or edit, and save from inside Power Apps Studio are also visible and available in [Power Automate](https://flow.microsoft.com).
> - Saved changes to the flows using Power Apps Studio will remain intact even if you close Power Apps Studio without saving changes to the app.
> - Removing a flow from a canvas app doesn't delete the flow from [Power Automate](https://flow.microsoft.com).

## Enable Power Automate pane

> [!IMPORTANT]
> - This feature is being rolled out and depending on your region, it may not be available for your tenant yet.
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Power Automate pane needs to be enabled manually through the feature switch. To enable the feature:

1. Open a [new](data-platform-create-app.md) or an [existing](edit-app.md) app in Power Apps Studio.

1. Select **Settings** at the top.

1. Select **Upcoming features**.

1. Under the **Preview** tab, select **Enable Power Automate pane** to turn on this feature. You may be prompted to close and reopen your canvas app to see the change.

   :::image type="content" source="media/working-with-flows/power-automate-pane-feature.png" alt-text="A screenshot of the Upcoming Features dialog box showing the Enable Power Automate feature toggle.":::

    Save the app and relaunch Power Apps Studio. The Power Automate pane now appears in Power Apps Studio.

   :::image type="content" source="media/working-with-flows/power-automate-button.png" alt-text="A screenshot highlighting the Power Automate option in the left pane":::

## Create a new flow

To start with flows inside Power Apps Studio, select **Create new flow** in the Power Automate pane.

   :::image type="content" source="media/working-with-flows/create-new-flow.png" alt-text="A screenshot showing Create your flow screen having several options to choose a flow template from.":::

This action opens the **Create your flow** modal dialog within Power Apps Studio. You can choose to create the flow from the available templates, or create a flow from scratch.

### Start with a template

Power Automate provides several flow templates that you can choose from by default. This section explains how to create a flow using such available templates from within Power Apps Studio.

1. From the list of available templates, select a template of your choice. For this example, we'll use **Click a button in Power Apps to send an email**.

   :::image type="content" source="media/working-with-flows/selected-flow-template.png" alt-text="A screenshot showing Click a button in Power Apps to send an email template.":::

1. The next step shows the connections required to create a flow based on the  selected template. More information: [Connectors overview](connections-list.md)

   :::image type="content" source="media/working-with-flows/connections.png" alt-text="A screenshot showing connections required by the flow.":::

1. (Optional) If you want, you can use **Edit in advanced mode** to update the connection, and customize the flow template. When done, select **Save** to save the flow. Skip the next step since this completes your flow creation process.

1. Select **Next** > **Create** to create the flow.

    The flow now appears in the list of flows inside the Power Automate pane, under the **In your app** section.

    :::image type="content" source="media/working-with-flows/flow-in-your-app.png" alt-text="A screenshot showing the flow added to your app.":::

    > [!TIP]
    > For more information about creating cloud flows from templates, see [Create a cloud flow from a template](/power-automate/get-started-logic-template).

### Create from blank

Instead of using the available templates, you can also create a flow from scratch, and customize the steps as per your requirement.

1. Select **Create from blank**.

1. Add and customize the flow with steps and actions, as shown in the below example.

    :::image type="content" source="media/working-with-flows/customize-blank-flow.png" alt-text="A screenshot showing example workflow.":::

1. When done, select **Save** from top-right corner of the screen.

    > [!TIP]
    > For more information about customizing and configuring cloud flows, see **How-to** articles starting from [Add multiple actions and advanced options to a cloud flow](/power-automate/multi-step-logic-flow).

## Add an existing flow

You may have access to the existing flows in the environment where you're creating your app. To add and use these flows in your app, select **Add flow**, and then choose the flow from the **Add a flow from this environment** section.

:::image type="content" source="media/working-with-flows/add-existing-flow.png" alt-text="A screenshot showing the option to add existing flows from the current environment.":::

> [!TIP]
> You can hover over the flow to see more details before adding to your app.

You must meet the following requirements to be able to add an existing flow to a canvas app:

- You must have access to the flow.
- If the canvas app is part of a solution, you'll only see the flows that are part of the same solution.
- Flows must have a Power Apps trigger.

After added, the flow will appear under **In your app** section inside the Power Automate pane.

## Edit an existing flow

You can now edit flows added to your app without leaving Power Apps Studio.

1. Under the **In your app** section of the Power Automate pane, select **..** (ellipsis) to the right of a flow.

1. Select **Edit**.

    :::image type="content" source="media/working-with-flows/edit-flow.png" alt-text="A screenshot showing the option to edit an existing flow.":::

    Flow opens inside the editor.

    :::image type="content" source="media/working-with-flows/edit-flow-editor.png" alt-text="A screenshot showing the flow open in editor for customization.":::

1. Make your changes, and then select **Save**.

    > [!TIP]
    > You'll be prompted to save the unsaved changes if you try to close the editor.

## Refresh a flow

If any changes are made to the flow in [Power Automate](https://flow.microsoft.com) (instead of using Power Apps Studio) while you're editing the app, you'll need to refresh your flow to get the latest changes.

To refresh the flow and pull the latest changes, select **...** (ellipsis) to the right of your flow, and then, select **Refresh**.

:::image type="content" source="media/working-with-flows/refresh-flow.png" alt-text="A screenshot showing the option to refresh the flow and pull in the latest changes.":::

A loading spinner will appear, and the flow will be refreshed.

## Remove a Flow

To remove a flow from your app, select **...** (ellipsis) to the right of your flow, and then, select **Remove from app**.

:::image type="content" source="media/working-with-flows/remove-flow.png" alt-text="A screenshot showing the option to remove the flow from the app.":::

This action only removes flow from the app, while the flow remains intact in the environment. You can add the flow again to the same app, or use in other apps.

### See also

- [Start a flow in a canvas app](using-logic-flows.md)
- [Add and configure controls](add-configure-controls.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
