---
title:  Create low-code plug-ins to use with Microsoft Copilot
description: 
author: mikefactorial
ms.author: mikefactorial
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 01/22/2024
ms.custom: template-how-to
---
# Create low-code plug-ins to use with Microsoft Copilot

Copilot actions are a way to extend the capabilities of your Copilot bots. With Copilot Generative AI actions, you create custom actions that can be triggered by your Copilot bot. These actions are used to perform a wide range of tasks, such as sending emails, creating records in Microsoft Dataverse, or calling external APIs. In this article, you create a low-code plug-in that can be used as to create an action in Microsoft Copilot Studio.

## Prerequisites

Before you begin, make sure you have the following prerequisites:

- Access to a Dataverse environment that includes the Dataverse Accelerator App for creating low-code plug-ins.
- Access to Copilot Studio in the same environment as your Dataverse environment.

## Basic low-code plugin example

In this example, you create a low-code instant plug-in that adds two numbers and returns the sum of those numbers. You then create a Copilot action that calls this low-code plug-in to perform the addition. The Copilot you create works for numbers as well as arbitrary text queries that contains numbers and fractions spelled out.

To create your basic low-code instant plug-in, follow these steps:

1. Open the Dataverse Accelerator App in your Dataverse environment by going to **Apps** > **All** > **Dataverse Accelerator App** and select **Play**.
2. From the Dataverse Accelerator App, select **New plug-in** and select **Instant plug-in**.
3. Enter a descriptive display name for your plug-in. For example *Sum numbers*, and then select **Create**.
4. In the **Parameters** section:
    - Add the following input parameters:
        - **Parameter Name**: Number1, Type: Float
        - **Parameter Name**: Number2, Type: Float
    - Add the following output parameter:
        - **Parameter Name**: Result, Type: Float
5. In the **Expression** section, enter the following code:

    ```
    {Result: Number1 + Number2}
    ```
      :::image type="content" source="media/low-code-plugin-copilot-action1.png" alt-text="Create instant low-code plugin that adds to numbers":::
6. Select **Save** to save your plug-in.

7. Create a copilot to call and then test your low-code plug-in as a Generative AI action. More information: [Use Generative Actions in Microsoft Copilot Studio](/microsoft-copilot-studio/advanced-generative-actions)

If everything is configured correctly, you see the expected result of 15.5 output in the chat window and the trace pane shows the inputs and outputs of your action. The trace pane looks similar to the following example. You can try some other prompts to test the action further and change the language to see how the action responds, such as *If I have 3 apples and my friend gives me 4 more, how many apples do I have in total?* or *If I have 1/2 pound of cheese and I order another 1/4 pound, how much cheese do I have total?*

:::image type="content" source="media/low-code-plugin-copilot-action3.png" alt-text="Results of adding two numbers from copilot":::

## More complex low-code plugin example

In this example, you create a low-code instant plug-in that wraps an existing API for use with a copilot. The action sends a notification to a user when the user prompts it to do so. The copilot determines the required parameters from the plain language query from the user and sends a notification using a Dataverse low-code plugin-in to a model-driven app in Power Apps.

To create your low-code instant plug-in, follow these steps:

1. Open the Dataverse Accelerator App in your Dataverse environment by going to **Apps** > **All** > Dataverse Accelerator App and select play.
2. From the Dataverse Accelerator App, select **New plug-in**, and then select **Instant plug-in**.
3. Enter a descriptive display name for your plug-in. For example, *Send in-app notification to user* and select **Create**.
4. In the **Parameters** section:
    - Add the following input parameters:
        - **Parameter Name**: UserName, Type: String
        - **Parameter Name**: Title, Type: String
        - **Parameter Name**: Body, Type: String
        - **Parameter Name**: Url, Type: String
    - Add the following output parameter:
        - **Parameter Name**: Result, Type: String
5. In the **Expression** section, enter the following code. Notice that we're wrapping the existing XSendAppNotification API with our plugin to give us the ability to find users by name which helps when we call it from Copilot who can only provide us with information the user knows about the person and not more esoteric IDs of records that the underlying API is expecting:

    ```
   XSendAppNotification(Title,
    First(Filter(Users, UserName in 'Full Name')), 
    Body,
    [XCreateUrlAction("Click Here", Url)]
   );
   {Result: "Success"}
    ```

   :::image type="content" source="media/low-code-plugin-copilot-action2.png" alt-text="Create a low-code plugin to send notification":::
1. Select **Save** to save your plug-in.
1. Create a copilot to call and then test your low-code plug-in as a Generative AI action. More information: [Use Generative Actions in Microsoft Copilot Studio](/microsoft-copilot-studio/advanced-generative-actions)

<!-- Need revised result detail-->
:::image type="content" source="media/low-code-plugin-copilot-action4.png" alt-text="Results of notifcation sent from copilot":::

## See also

[Use low-code plug-ins in Dataverse (preview)](low-code-plug-ins.md)