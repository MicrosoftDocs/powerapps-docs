---
title: Add Chatbot control to your canvas app
description: A control that enables embedding of any published Power Virtual Agent (PVA) bot into Power Apps for end-user.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 3/13/2023
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add Chatbot control to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

Add Chatbot control to your canvas apps and embed a published [Power Virtual Agents](/power-virtual-agents/fundamentals-what-is-power-virtual-agents) chatbot to assist your end-users with a variety of requests&mdash;from providing simple answers to common questions to resolving issues requiring complex conversations. 

You can use an AI bot or AI boosted conversations bot:

- With AI chatbots, you can create an extended tree of answers to support your users. More information: [Power Virtual Agents preview quickstart (preview)](/power-virtual-agents/preview/quickstart)

- With AI boosted conversations Power Virtual Agents bot your bot can have a higher ability to respond to the user by using a number of prompts or generating a response based on provided "fallback" website which you set. The "fallback" website can include internal documents or publicly available websites. More information: [AI-based boosted conversations overview (preview)](/power-virtual-agents/nlu-gpt-overview)


You can design the Chabot control by giving it a name, change the size of the control window, and position it anywhere on the screen.

> [!div class="mx-imgBorder"]
> ![Sample Chabot control in a canvas app.](media/chatbot-control/ai-chatbot-control-1.png)


> [!IMPORTANT]
> - This capability is in gated preview, and you'll need to apply for consideration to take part in the trial. To apply, go to [Limited preview request](https://go.microsoft.com/fwlink/?linkid=2227838).
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in process of rolling out, and may not be available in your region yet.
> - This capability  may be subject to usage limits or capacity throttling.


## Prerequisites 

- Follow the prerequisites for AI features: [AI Copilot overview (preview)](ai-overview.md)
- To add the Chatbot control, you need to create and publish a bot on the [Power Virtual Agents web app](/power-virtual-agents/fundamentals-what-is-power-virtual-agents-portal).  You can create any bot such as an AI bot or a new generative AI enriched Power Virtual Agents bot.


## Bot schema name 

You need the bot schema name to add it to the Chatbot control properties in Power Apps Studio. Following these steps to get the schema name.

1. In Power Virtual Agents, open the bot you want to use. 
2. In the navigation menu, go to **Settings** > **Details**. 
3. Select the **Advanced** tab and note the **Schema name**.


## Turn on the Chatbot control

With your [canvas app open for editing](edit-app.md):

1. On the command bar, select **Settings** > **Upcoming features**.
2. From the **Preview** tab, set the toggle for **Chatbot component** to **On**.

   > [!div class="mx-imgBorder"]
   > ![Turn on Chatbot control.](media/chatbot-control/ai-chatbot-control-2.png)

## Add a control with a bot

With your [canvas app open for editing](edit-app.md):

1. On the app authoring menu, select **Insert**.
2. Expand the **Input** menu and then select **Chatbot (preview)**). Place the chatbot control where you want to add it on the screen. 

   > [!div class="mx-imgBorder"]
   > ![Add the Chatbot control.](media/chatbot-control/ai-chatbot-control-3.png)

2. In the Chatbot properties pane, enter the Power Virtual Agents bot schema name in the **Schema Name** field.

    You can change the name, the position, and size of the control.

### Key properties 

The following are the main properties for Chatbot control: 

- **Schema name**:  The schema name property must be entered to connect your published Power Virtual Agents bot to your canvas app. For more information on how to get the Schema name, see [Prerequisites](add-ai-chatbot.md#prerequisites) section in this article.

- **Header label**: This is the name of the bot that your end-user will see. If don't enter a header label, it will be **Chatbot**.

  > [!div class="mx-imgBorder"]
  > ![Add schema name.](media/chatbot-control/ai-chatbot-control-4.png)

Use the other properties or move the control on the screen to set position and size of the control on the screen. 

## Limitations

- You can only embed a bot with no user authentication.

## See also

[AI Copilot overview (preview)](ai-overview.md)

[Power Virtual Agents preview quickstart (preview)](/power-virtual-agents/preview/quickstart)

[AI-based boosted conversations overview (preview)](/power-virtual-agents/nlu-gpt-overview)

[Use the Copilot control](add-ai-copilot.md)

[Build apps through conversation (preview)](ai-conversations-create-app.md)





 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
