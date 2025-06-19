---
title:  Create Dataverse low-code plug-ins to use with a copilot (preview)
description: Learn how to create low-code plug-ins to use with Microsoft Copilot generative AI actions.
author: mikefactorial
ms.author: sriknair
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 04/26/2024
ms.custom: template-how-to
ms.collection: bap-ai-copilot
---
# Create low-code plug-ins to use with a copilot (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Copilot actions are a way to extend the capabilities of your copilot bots. With Copilot generative AI actions, you create custom actions that are triggered by your copilot bot. These actions are used to perform a wide range of tasks, such as sending emails, creating records in Microsoft Dataverse, or calling external APIs. In this article, you create a basic low-code plug-in that adds two integers together and a more complex plug-in that can be used to send a notification either of which can be used to create an action in Microsoft Copilot Studio.

> [!IMPORTANT]
>
> - Instant low-code plug-ins are deprioritized and aren't being delivered as a feature. Instant low-code plug-ins are replaced with functions. More information: [Functions in Microsoft Dataverse (preview)](functions-overview.md)
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites to use the plug-in with Microsoft Copilot

Before you begin, make sure you have the following prerequisites:

- Access to a Dataverse environment that includes the Dataverse Accelerator App for creating low-code plug-ins.
- Access to Copilot Studio in the same environment as your Dataverse environment.

## Basic low-code plugin example

In this example you create a low-code instant plug-in that adds two numbers and returns the sum of those numbers. You then create a Copilot action that calls this low-code plug-in to perform the addition. The copilot you create works for numbers and arbitrary text queries that contain numbers and fractions spelled out.

To create your basic low-code instant plug-in, follow these steps:

1. Open the Dataverse Accelerator App in your Dataverse environment by going to **Apps** > **All** > **Dataverse Accelerator App** and select **Play**.
2. From the Dataverse Accelerator App, select **New plug-in** and select **Instant plug-in**.
3. Enter a descriptive display name for your plug-in. For example *Sum numbers*, and then select **Create**.
4. In the **Parameters** section:
    - Add the following input parameters:
        - **Parameter Name**: *Number1*, **Type**: **Float**
        - **Parameter Name**: *Number2*, **Type**: **Float**
    - Add the following output parameter:
        - **Parameter Name**: *Result, Type*: **Float**
5. In the **Expression** section, enter the following code:

    ```
    {Result: Number1 + Number2}
    ```
      :::image type="content" source="media/low-code-plugin-copilot-action1.png" alt-text="Create instant low-code plugin that adds to numbers" lightbox="media/low-code-plugin-copilot-action1.png":::
6. Select **Save** to save your plug-in.

### Create a copilot to call your basic low-code plug-in

Go to Copilot Studio, and open the environment that has the plug-in.

1. Create a copilot. More information: [Create and configure copilot plugins](/microsoft-copilot-studio/copilot-plugins-overview)
1. Enable generative actions on the copilot. More information: [Enable generative actions](/microsoft-copilot-studio/advanced-generative-actions#enable-generative-actions)
1. Add a generative AI action. When you add the action, search for 'Perform an unbound action in selected environment' and select the action. More information: [Use Generative Actions in Microsoft Copilot Studio](/microsoft-copilot-studio/advanced-generative-actions)
1. Configure the action with the following details:
   - Add a model description that lets the copilot know when to call this action. Use plain English to describe the conditions under which this action should be called. For example, you can enter "Adds numbers and return the sum of those numbers given 2 floating point values." More information: [Authoring descriptions](/microsoft-copilot-studio/advanced-generative-actions#authoring-descriptions)
   - Use these **Inputs**:
      - Change **How will the copilot fill this input for the Organization** parameter to **Set as a value**.
      - Select your current environment (the environment in which you created your low-code plug-in) as the value for the **Organization** parameter.
      - Change **How will the copilot fill this input for the Action Name** parameter to **Set as a value**.
      - Select the low-code plug-in you created as the value for the **Action Name** parameter. If you're unsure what the name of your plug-in is you can find it in the Dataverse Accelerator App by selecting it from the list and selecting **Copy code snippet** and then pasting the code into a text editor.
   - Additional **Inputs**:
       - Add and the following input parameters. Adding additional inputs doesn't currently show details in Copilot Studio. You can verify that the inputs were added correctly by selecting **Open the code edit and reviewing the code**, which should show the additional inputs under the inputs section in the action YAML:
          - **Parameter Name**: *Number1*
          - **Parameter Name**: *Number2*
1. Save and publish the copilot.

### Test your copilot action

Follow these steps in the **Test copilot** pane in Copilot Studio.

1. Select the sparkle icon at the top of the chat window to start tracing mode. This allows you to confirm that your action is being called and verifies the inputs and outputs of your action. More information: [Testing you copilot using generative actions](/microsoft-copilot-studio/advanced-generative-actions#testing-your-copilot-using-generative-actions)
1. Enter the text in the chat window *Add 5.2 and 10.3* and select **Send**.

If everything is configured correctly, you see the expected result of 15.5 output in the chat window and the trace pane shows the inputs and outputs of your action. The trace pane looks similar to the following example. You can try some other prompts to test the action further and change the language to see how the action responds. Some examples:

- *If I have 3 apples and my friend gives me 4 more, how many apples do I have in total?*
- *If I have 1/2 pounds of cheese and I order another 1/4 pounds, how much cheese do I have total?*

:::image type="content" source="media/low-code-plugin-copilot-action3.png" alt-text="Results of adding two numbers from copilot" lightbox="media/low-code-plugin-copilot-action3.png":::

## Send notification low-code plugin example

In this example you create a low-code instant plug-in that wraps an existing API for use with a copilot. The action sends a notification to the user specified in the copilot action when the user creating the action tests it in Copilot Studio. The copilot determines the required parameters from the plain language query from the user and sends a notification using a Dataverse low-code plugin-in to a model-driven app in Power Apps.

To create your low-code instant plug-in, follow these steps:

1. Open the Dataverse Accelerator App in your Dataverse environment by going to **Apps** > **All** > Dataverse Accelerator App and select play.
2. From the Dataverse Accelerator App, select **New plug-in**, and then select **Instant plug-in**.
3. Enter a descriptive display name for your plug-in. For example, *Send in-app notification to user* and select **Create**.
4. In the **Parameters** section:
    - Add the following input parameters:
        - **Parameter Name**: *UserName, Type*: **String**
        - **Parameter Name**: *Title, Type*: **String**
        - **Parameter Name**: *Body, Type*: **String**
        - **Parameter Name**: *Url, Type*: **String**
    - Add the following output parameter:
        - **Parameter Name**: *Result, Type*: **String**
5. In the **Expression** section, enter the following code. Notice that we're wrapping the existing `XSendAppNotification` API with the plugin to give the ability to find users by name. This behavior helps when called from copilot, which can only provide information the user knows about the person and not more esoteric IDs of records that the underlying API is expecting:

   ```powerappsfl
   XSendAppNotification(Title,
   First(Filter(Users, UserName in 'Full Name')), 
   Body,
   [XCreateUrlAction("Click Here", Url)]
   );
   {Result: "Success"}
   ```

   :::image type="content" source="media/low-code-plugin-copilot-action2.png" alt-text="Create a low-code plugin to send notification" lightbox="media/low-code-plugin-copilot-action2.png":::
6. Select **Save** to save your plug-in.

### Create a copilot to call your send notification low-code plug-in

Go to Copilot Studio, and open the environment that has the plug-in.

1. Create a copilot. More information: [Create and configure copilot plugins](/microsoft-copilot-studio/copilot-plugins-overview)
1. Enable generative actions on the copilot. More information: [Enable generative actions](/microsoft-copilot-studio/advanced-generative-actions#enable-generative-actions)
1. Add a generative AI action. When you add the action, search for 'Perform an unbound action in selected environment' and select the action. More information: [Use Generative Actions in Microsoft Copilot Studio](/microsoft-copilot-studio/advanced-generative-actions)
1. Configure the action with the following details:
   - Add a model description that lets the copilot know when to call this action. Use plain English to describe the conditions under which this action should be called. For example, you can enter "Calls a Dataverse API to send a notification to a user in Dataverse to remind or alert them to something important with a title, body and optionally a link for more details." More information: [Authoring descriptions](/microsoft-copilot-studio/advanced-generative-actions#authoring-descriptions)
   - Use these **Inputs**:
      -  Change **How will the copilot fill this input for the Organization** parameter to **Set as a value**.
      - Select your current environment from the dropdown list (the environment in which you created your low-code plug-in) as the value for the **Organization** parameter. You need to put your cursor in the textbox in order for the list of available environments to show.
      - Change **How will the copilot fill this input for the Action Name** parameter to **Set as a value**.
      - Select the low-code plug-in you created as the value for the **Action Name** parameter. You need to put your cursor in the textbox in order for the list of available APIs to show. The value to enter here is the schema name of the low-code plugin, such as `org_SendInAppNotificationToUser`. If you're unsure what the schema name of your plug-in is you can find it in the Dataverse Accelerator App by selecting it from the list and selecting **Copy code snippet** and then pasting the code into a text editor.
   - Additional **Inputs**:
       - Select **Add** and add following input parameters. Notice that adding additional inputs doesn't currently show details in Copilot Studio. This is a known issue. You can verify that the inputs were added correctly by selecting **Open the code edit and reviewing the code**, which should show the additional inputs under the inputs section in the action YAML:
          - **Parameter Name**: *UserName*
          - **Parameter Name**: *Title*
          - **Parameter Name**: *Body*
          - **Parameter Name**: *Url*
1. Save and publish the copilot.

### Test your send notification copilot action

Follow these steps in the **Test copilot** pane in Copilot Studio.

1. Select the sparkle icon at the top of the chat window to start tracing mode. This allows you to confirm that your action is being called and verifies the inputs and outputs of your action. More information: [Testing you copilot using generative actions](/microsoft-copilot-studio/advanced-generative-actions#testing-your-copilot-using-generative-actions)
1. Enter the text in the chat window *Send a notification to my user to check out this url https://copilotstudio.microsoft.com*, and then select **Send**.

If everything is configured correctly, you see that a notification has been sent in the **Test copilot** pane. The notification is sent as a model-driven in-app notification when the specified user plays the app. 

:::image type="content" source="media/low-code-plugin-copilot-action4.png" alt-text="Results of notifcation sent from copilot" lightbox="media/low-code-plugin-copilot-action4.png":::

You can try some other prompts to test the action further and you could change the plugin to be smarter about how it searches for users given a name to see how the action responds. For example, you could add a step to search for the user by email address if the name doesn't return a result.

## See also

[Use low-code plug-ins in Dataverse](low-code-plug-ins.md)