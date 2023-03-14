---
title: Add a chatbot control to your canvas app
description: A control that enables embedding of any published Power Virtual Agent (PVA) bot into Power Apps for end-user.
author: mduelae
ms.topic: conceptual
ms.custom: 
  - canvas
  - intro-internal
ms.reviewer: 
ms.date: 3/13/2023
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - mduelae
---

# Add a chatbot control to your canvas app

A Chatbot control can embed a published Power Virtual Agents bot of any kind in the Canvas app. Makers will first need to create and publish a bot on the Power Virtual Agents web app and then follow the steps by adding in to the Chatbot control.

This opens big opportunities for automation to help end-users to get answers faster. For example, with AI chatbots, makers can create an extended tree of answers to support their users. With boosted conversations in Power Virtual Agents bots, a new feature on PVA, makers can create a number of prompts and then have a fallback to the generative AI support that gets answers from the specific source that maker provides (for example, documentation or public web site).

Maker can design the control by giving it a suitable name, changing the size of the control window and positioning it anywhere on the screen.

> [!IMPORTANT]
>
> - This is a preview feature. This capability is in gated preview, and you'll need to apply for consideration to take part in the trial. To apply, go to [Limited preview request](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR2LogRPRiTJDo1Rd8KnmcFRUMzlLTDZVQlJKSzNIWkVCMzE0VDFYVzk2QS4u).

>
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
>
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
>
> - This capability is in process of rolling out, and may not be available in your region yet.
>
> - This capability  may be subject to usage limits or capacity throttling.


## Steps to add a control with a bot

1. First of all, you need to turn on the feature. Go Settings – Upcoming features – Chatbot component. Move toggle to "on". Close the Setting window.

![](media/image2.png)

2. Add control to your screen by finding the control name - Chatbot (preview) - under the "Input" section of the controls' list. The placeholder Chatbot window will be placed on your screen.

![](media/image3.png)

3. To connect your bot, you need to insert the bot's Schema name to the control Property panel. If you don't have any published bots yet, go to the PVA page and create a bot. You can create any bot: an AI bot or a new generative AI enriched PVA bot. Once you publish it, you will have a Schema name that you can add to the control properties.

4. You can change the position of the control, or its name, or its size to your liking.

## Key properties 

There are two main properties: Schema name and Header label

Schema name – is the property you use to connect your published PVA bot to the Chatbot control. You take it from the PVA side, and once added – your bot is embedded to your app. You must use this property to connect your bot.

Header label – is how you want your bot be called and visible to your end users. If nothing is entered, the control defaults to "Chatbot".

![](media/image4.png)

There are other properties such as the position on the screen and size of the window. You can use either these fields to adjust the look of your control, or you can adjust in directly on the screen by moving it around and resizing the window.

## Limitations

1. The PVA bot must be published in order for it to be added to Power Apps via Chatbot control.

2. Currently, you can only embed a bot with no user authentication.

## Recommended content

-  PVA documentation: [Microsoft Power Virtual Agents documentation - Power Virtual Agents \| Microsoft Learn](https://learn.microsoft.com/en-us/power-virtual-agents/)

-  Quickstart \| Create your bot: [Power Virtual Agents preview quickstart (preview) - Power Virtual Agents \| Microsoft Learn](https://learn.microsoft.com/en-us/power-virtual-agents/preview/quickstart)

-  AI-based boosted conversations overview (preview): [AI-based boosted conversations overview (preview) - Power Virtual Agents \| Microsoft Learn](https://learn.microsoft.com/en-us/power-virtual-agents/nlu-gpt-overview)

-  Power Apps Copilot control: //insert link when Miti's documentation has a link



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
