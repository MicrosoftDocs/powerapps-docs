---
title: Start a flow in a canvas app
description: Learn about how to create a flow that performs one or more tasks after an event, such as a user selecting a button, occurs in a canvas app.
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
# Start a flow in a canvas app (retired)

You can use Power Automate to create logic that performs one or more tasks when an event occurs in a canvas app. For example, you can configure a button that performs a single task or multiple tasks. When the button is pressed, an item is created in a list (Microsoft Lists), an email or meeting request is sent, and a file is added to the cloud. You can configure any control in the app to start the flow, which continues to run even if you close Power Apps.

> [!NOTE]
> When a user runs a flow from within an app, that user must have permission to perform the tasks that are specified in the flow. Otherwise, the flow will fail.

## Enable classic Power Automate experience

By default, the new [Power Automate pane](working-with-flows.md) is enabled by default. To use the classic Power Automate experience to create a flow, switch back to the old experience manually.

> [!IMPORTANT]
> It’s recommended that you use the [Power Automate pane](working-with-flows.md) to create a flow. The classic Power Automate experience should only be used for troubleshooting. The classic experience will be retired soon and won't be available.

1. Open a [new](data-platform-create-app.md) or an [existing](edit-app.md) app in Power Apps Studio.

1. Select **Settings** at the top.

1. Select **Upcoming features**.

1. Under the **Retired** tab, select **Enable Classic Power Automate pane** to set the toggle to **On**.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps.
- Learn how to [configure a control](add-configure-controls.md).
- A SharePoint site with two lists.
  - List **RepairShop** contains Title, and ContactEmail columns.
  - List **Assets** contains Title, AssetType, and RepairShop columns. The AssetType column is a choice column with choices such as "Desktop" or "Laptop".
  - The RepairShop column in Assets list is a lookup column that gets values from the ContactEmail column in RepairShop list.
  - Create a few items in the **RepairShop** list for sample contacts.

## Create a flow

In this section, you create a flow using Power Automate that creates an item in a list using the input value for the list column from an app created using Power Apps. You create the app that uses this flow in the next section.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left-pane, select **Flows**.

1. Select **+ New flow** > **Instant cloud flow**.

1. Enter flow name, such as **FlowInApp**.

1. Under **Choose how to trigger this flow**, select **Power Apps**.

    :::image type="content" source="./media/using-logic-flows/ceate-instant-flow.png" alt-text="Screenshot that shows the flow option that lets's you choose how to trigger a Power Apps flow.":::

1. Select **Create**.

1. Select **+ New step**.

1. Under **Choose an operation**, search for or select **SharePoint** connector.

    :::image type="content" source="./media/using-logic-flows/choose-sharepoint-connector.png" alt-text="Screenshot that shows where you can search or choose a SharePoint connector when you choose an operation.":::

1. Search for, or select **Create item** action.

   :::image type="content" source="./media/using-logic-flows/sharepoint-create-item-action.png" alt-text="Screenshot that shows where you can search or choose the create item action.":::

1. For **Site Address**, enter or choose your SharePoint site that has the lists **Assets** and **RepairShop**.

1. For **List Name**, select the **Assets** list.

   :::image type="content" source="./media/using-logic-flows/site-and-list.png" alt-text="Screenshot that shows the site address and list name fields.":::

1. For **Title**, choose **Ask in Power Apps** from the **Dynamic content** tab. The action automatically updates to **Createitem_Title**.

   :::image type="content" source="./media/using-logic-flows/ask-in-powerapps-create-title.png" alt-text="screenshot that shows the Ask in Power Apps button where a title gets created." lightbox="./media/using-logic-flows/ask-in-powerapps-create-title.png":::

1. Choose values for **AssetType Value**, and **RepairShop Id** of your choice.

    :::image type="content" source="./media/using-logic-flows/assettype-repairshopid.png" alt-text="Screenshot that shows the AssetType Value and RepairShop Id fields.":::

1. Select **Save**.

> [!IMPORTANT]
> Arguments that pass from Power Apps to Power Automate are visible as network traffic and can be intercepted. Most traffic is likely harmless data that are irrelevant outside the application, for example arguments like "yes" or "Redmond".
>
> Evaluate the parameters passed to Power Automate and consider the consequences (if any) if they're changed by an exernal actor. To mitigate risks, validate the parameter values passed.  
>
> For example, if you send sensitive data to a person in your organization through email, for example `someuser@contoso.com`, validate the address in Power Automate. You can check the incoming arguments to confirm the organization, `@contoso.com`, and only allow the flow to proceed if the right organization is present.

## Add a flow to an app

In this section, you create an app using Power Apps that uses the flow created in the earlier section. The app uses text entered in a text box when the button is selected to trigger the flow to create an item in the selected list.

1. Create a [blank canvas app](create-blank-app.md) with a name such as **AppWithFlow**.

1. Select **+** (Insert) on the left-pane.

1. Select **Text input** control.

1. Select **Button** control.

1. On the canvas, move the button control below the text input control.

    ![Design the app.](./media/using-logic-flows/assettype-repairshopid.png "Design the app")

1. Select **Action** menu at the top, and then select **Power Automate**.

    > [!NOTE]
    > Adding a flow to the selected control or component clears out any existing formula for the chosen property. For example, when you add a flow to a button's `OnSelect` property that has a complex formula, the flow addition clears out this formula. Ensure you make a copy of the formula before adding the flow. However, this behavior is different when adding flow with the Power Automate pane enabled. Learn more in [Reference a flow](working-with-flows.md#reference-a-flow).

    :::image type="content" source="./media/using-logic-flows/action-power-automate.png" alt-text="Screenshot that shows what an associated flow looks like in Power Automate." lightbox="./media/using-logic-flows/action-power-automate.png":::

    Alternatively, if you enabled the **Enable Power Automate pane** preview feature, you can choose your flow from the left-pane inside Power Apps Studio.

    :::image type="content" source="media/using-logic-flows/power-automate-pane-add-flow.png" alt-text="A screenshot showing the Power Automate button in the left pane with the Add Flow dialog opened, showing the FlowInApp flow available to add to the app.":::

   More information: [Use Power Automate pane (preview)](working-with-flows.md)

1. Select **FlowInApp**.

1. In the formula bar, remove the formula for the selected **OnVisible** property.

1. Select the text input control.

1. From the top-left side of the screen, select the property list drop-down, and then select the **Default** property.

1. In the formula bar, change the default property value from `"Text input"` to `"Enter Asset Title"`.

1. Select the button control.

1. From the top-left side of the screen, select the property list drop-down, and then select the **Text** property.

1. In the formula bar, change the text property value from `"Button"` to `"Create Asset"`.

1. From the top-left side property list, select the **OnSelect** property for the button.

1. Enter the following formula in the formula bar.

    ```power-fx
    FlowInApp.Run(TextInput1.Text)
    ```

    In this formula, **FlowInApp** is the name of the flow you added using Power Automate. The **.Run** specifies the flow to execute. The flow executes with **TextInput1** text input control added to this canvas, with the value entered in this text box (**.Text**).

    When this button is selected, the app runs the flow with the value from the text input control, passing the text value to the flow to execute. And the flow creates the list item with this text input value along with rest of the selection inside the flow configuration.

    :::image type="content" source="./media/using-logic-flows/onselect-button.png" alt-text="Screenshot that shows the OnSelect property formula for a button on the canvas.":::

1. [Save and publish](save-publish-app.md) the app.

## Test the flow

Now that you have both the flow and the app created, run the app and verify the creation of an item inside the selected list.

1. In [Power Apps](https://make.powerapps.com), select **Apps**, and then, select the **AppWithFlow** app.

   :::image type="content" source="./media/using-logic-flows/run-app-with-flow.png" alt-text="Screenshot that shows where to find the Run AppWithFlow app.":::

1. Enter a value in the text input box, and then select **Create Asset**.

   :::image type="content" source="./media/using-logic-flows/run-app.png" alt-text="Screenshot that shows the entered value and the Create Asset button.":::

1. Verify that the item is created in your list.

   :::image type="content" source="./media/using-logic-flows/check-sharepoint-list.png" alt-text="Screenshot that shows the assets created in SharePoint.":::

Now that you created a sample app that runs a flow and adds an item inside a list, you can create more complex applications. Your apps can interact with Power Automate and manipulate data inside various data sources.

### Related information

- [Use Power Automate pane (preview)](working-with-flows.md)
- [Add and configure controls](add-configure-controls.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
