---
title: Use Power Automate pane
description: Learn how to use Power Automate pane to work with flows in Power Apps.
author: TashasEv

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 12/17/2024
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
contributors:
  - mduelae
  - TashasEv
---

# Use Power Automate pane

Create new flows or add and edit existing flows using the Power Automate pane within Power Apps Studio. The Power Automate pane is enabled by default.

> [!IMPORTANT]
> Arguments that pass from Power Apps to Power Automate are visible as network traffic and can be intercepted. Most traffic is likely harmless data that are irrelevant outside the application, for example arguments like "yes" or "Redmond".
>
> Evaluate the parameters passed to Power Automate and consider the consequences (if any) if they're changed by an exernal actor. To mitigate risks, validate the parameter values passed.  
>
> For example, if you send sensitive data to a person in your organization through email, for example `someuser@contoso.com`, validate the address in Power Automate. You can check the incoming arguments to confirm the organization, `@contoso.com`, and only allow the flow to proceed if the right organization is present.

## Create a new flow

1. Open a [new](data-platform-create-app.md) or an [existing](edit-app.md) app in Power Apps Studio.

2. On the app authoring menu, select **Power Automate**.

   :::image type="content" source="media/working-with-flows/power-automate-button.png" alt-text="A screenshot highlighting the Power Automate option in the left pane.":::

3. In the Power Automate pane, select **Create new flow**.

   :::image type="content" source="media/working-with-flows/create-new-flow.png" alt-text="A screenshot showing the Create your flow screen having several options from which to choose a flow template.":::

This action opens the **Create your flow** modal dialog within Power Apps Studio. You can choose to create the flow from the available templates, or create a flow from scratch.

### Start with a template

Power Automate provides several flow templates that you can choose from by default. This section explains how to create a flow using such available templates from within Power Apps Studio.

1. From the list of available templates, select a template of your choice. For this example, we use **Click a button in Power Apps to send an email**.

   :::image type="content" source="media/working-with-flows/selected-flow-template.png" alt-text="A screenshot showing Click a button in Power Apps to send an email template.":::

1. The next step shows the connections required to create a flow based on the selected template. More information: [Connectors overview](connections-list.md)

   :::image type="content" source="media/working-with-flows/connections.png" alt-text="A screenshot showing connections required by the flow.":::

1. (Optional) You can use **Edit in advanced mode** to update the connection, and customize the flow template. When done, select **Save** to save the flow. Skip the next step since your flow creation process is now complete.

1. Select **Next** > **Create** to create the flow.

    The flow now appears in the list of flows inside the Power Automate pane, under the **In your app** section.

    :::image type="content" source="media/working-with-flows/flow-in-your-app.png" alt-text="A screenshot showing the flow added to your app.":::

    > [!TIP]
    > For more information about creating cloud flows from templates, see [Create a cloud flow from a template](/power-automate/get-started-logic-template).

### Create from blank

Instead of using the available templates, you can create a flow from scratch, and customize the steps as per your requirement.

1. Select **Create from blank**.

1. Add and customize the flow with steps and actions, as shown in the following example.

    :::image type="content" source="media/working-with-flows/customize-blank-flow.png" alt-text="A screenshot showing example workflow.":::

1. When done, select **Save** from upper right corner of the screen.

    > [!TIP]
    > For more information about customizing and configuring cloud flows, see the **How to** articles starting from [Add multiple actions and advanced options to a cloud flow](/power-automate/multi-step-logic-flow).

## Add an existing flow

You might have access to the existing flows in the environment where you're creating your app. To add and use these flows in your app, select **Add a flow**, and then choose the flow from the **Add a flow from this environment** section.

:::image type="content" source="media/working-with-flows/add-existing-flow.png" alt-text="A screenshot showing the option to add existing flows from the current environment.":::

> [!TIP]
> You can hover over the flow to see more details before adding to your app.

You must meet the following requirements to be able to add an existing flow to a canvas app:

- Have access to the flow
- Have access to see the flows that are part of the same solution
- Have a Power Apps trigger for your flows.

After being added, the flow will appear under the **In your app** section inside the Power Automate pane.

## Reference a flow

To reference the added flow, update the formula bar for the control or component within Power Apps Studio with the flow details. For example, to reference a flow named "PowerAppsbutton" that triggers an email without accepting any input parameters, use the following formula on the button's **OnSelect** property:

```power-fx
PowerAppsbutton.Run()
```

:::image type="content" source="media/working-with-flows/reference-flow.png" alt-text="A screenshot showing a flow added to the OnSelect property of the button with a formula.":::

This behavior is different from how the reference to a flow works within Power Apps Studio if the Power Automate pane is disabled.

When you add a flow with the Power Automate pane disabled, you must choose a behavior property of the control or the component that you want to associate with the flow. Adding a flow, in this case, clears any formula already associated with the chosen property (when the flow reference is added). Any existing formula gets removed, and you must carefully make a copy of the existing formula before adding the flow in order to preserve it. You can then paste your copied formula back after the flow reference is added.

For example, on a button's OnSelect property, adding the flow removes your existing formula, and you have to carefully make a copy of the existing formula before adding the flow. The following example shows the process with the Power Automate pane disabled. In this case, the formula added for the button property is removed to reference the added flow.

:::image type="content" source="media/working-with-flows/old-method.png" alt-text="A screenshot showing flow added to OnSelect property of the button that replaces existing formula for the button property." border="false":::

Whereas with the Power Automate pane enabled, any existing formula is preserved automatically (isn't removed). You can add the flow reference in the formula for a behavior property as per your requirement.

The following example shows the process with the Power Automate pane enabled. When the flow is added, the existing formula for the button's OnSelect property is preserved, and the flow reference isn't added automatically.

:::image type="content" source="media/working-with-flows/new-method.png" alt-text="A screenshot showing flow added to OnSelect property of the button that doesn't get replaced after the flow addition." border="false":::

Now you can reference the flow through the regular process of updating the formula for the control or component&mdash;as explained earlier.

## Edit an existing flow

You can now edit flows added to your app without leaving Power Apps Studio.

1. Under the **In your app** section of the Power Automate pane, select **...** (ellipsis) to the right of a flow.

1. Select **Edit**.

    :::image type="content" source="media/working-with-flows/edit-flow.png" alt-text="A screenshot showing the option to edit an existing flow.":::

    The flow opens inside the editor.

    :::image type="content" source="media/working-with-flows/edit-flow-editor.png" alt-text="A screenshot showing the flow open in editor for customization.":::

1. Make your changes, and then select **Save**.

    > [!IMPORTANT]
    > To avoid losing unsaved changes, ensure you select **Save** before closing the editor.

## Refresh a flow

If any changes are made to the flow in [Power Automate](https://make.powerautomate.com) (instead of using Power Apps Studio), refresh your flow to get the latest changes.

To refresh the flow and pull the latest changes, select **...** (ellipsis) to the right of your flow, and then select **Refresh**.

:::image type="content" source="media/working-with-flows/refresh-flow.png" alt-text="A screenshot showing the option to refresh the flow and pull in the latest changes.":::

A loading spinner appears, and the flow is refreshed.

  >[!IMPORTANT]
  > Failing to perform this step after making changes to a flow outside of Power App Studio can cause the run of the flow to fail, even for apps that had been previously published. It may also cause performance issues in the Power Platform, as each time the canvas app runs, it will attempt to validate the connections used by the flow based on the information from the time the flow was last added or refreshed, which may not succeed.

## Remove a flow

To remove a flow from your app, select **...** (ellipsis) to the right of your flow, and then select **Remove from app**.

:::image type="content" source="media/working-with-flows/remove-flow.png" alt-text="A screenshot showing the option to remove the flow from the app.":::

This action only removes the flow from the app, while the flow remains intact in the environment. You can add the flow again to the same app, or use it in other apps.

## Classic Power Automate experience

The Power Automate pane is now enabled by default. To use the classic Power Automate experience to [create a flow](using-logic-flows.md), switch back to the old experience manually.

> [!IMPORTANT]
> It’s recommended that you use the [Power Automate pane](working-with-flows.md) to create a flow. The classic Power Automate experience should only be used for troubleshooting. The classic experience will be retired soon and won't be available.

1. Open a [new](data-platform-create-app.md) or an [existing](edit-app.md) app in Power Apps Studio.

1. Select **Settings** at the top.

1. Select **Upcoming features**.

1. Under the **Retired** tab, select **Enable Classic Power Automate pane** to set the toggle to **On**. 

### See also

- [Add and configure controls](add-configure-controls.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
