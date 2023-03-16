---
title: Add Copilot control to a canvas app
description: Add copilot AI control to your canvas app.
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

# Add the Copilot control to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

The Copilot control is a next-generation AI assistant that makers can add to their apps for end-users. This is an AI-powered experience for app users to get insights about the data in their apps through conversation in natural language. Makers can add this control to any app and choose what data it can answer questions about.

> [!IMPORTANT]
> - This capability is in gated preview, and you'll need to apply for consideration to take part in the trial. To apply, go to [Limited preview request](https://go.microsoft.com/fwlink/?linkid=2227838).
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in process of rolling out, and may not be available in your region yet.
> - This capability  may be subject to usage limits or capacity throttling.


## Prerequisites

- Follow the prerequisites for AI features: [AI Copilot overview (preview)](ai-overview.md).


## Enable Copilot control for your app:

With your [canvas app open for editing](edit-app.md):

1. On the command bar, select **Settings** > **Upcoming features**.
2. From the **Preview** tab, set the toggle for **Copilot component** to **On**.

   > [!div class="mx-imgBorder"]
   > ![Turn on Copilot control.](media/copilot/copilot-1.png)

## Add the Copilot control

With your [canvas app open for editing](edit-app.md):

1. On the app authoring menu, select **Insert**.
2. Expand the **Input** menu and select **Copilot (preview)** to add this control.

   > [!div class="mx-imgBorder"]
   > ![Add teh copilot control.](media/copilot/copilot-2.png)

## Choose data

1. When the Copilot control is added, select a data source from the pane. Note that at this time, only a single Dataverse table can be selected for the Copilot control.

   > [!div class="mx-imgBorder"]
   > ![Select a data source.](media/copilot/copilot-3.png)

2. Alternatively, on the **Properties** tab of the right-hand pane, set **Data source (Items)** to the desired Dataverse table as your source of data.

3. Select the specific **Fields** and/or **View** over which the Copilot control answer questions.

   > [!div class="mx-imgBorder"]
   > ![Select fields or views.](media/copilot/copilot-4.png)

Due to current limitations, the Copilot control can answer questions over Dataverse tables that are smaller in size.

## Configure the control (optional)

In addition to choosing the data source, you can also configure the following properties:

- **Title**: Replaces the control's default title of **Copilot**, and can be updated to something more descriptive of what this Copilot control can help app users with.

- **Data summary**: Helps Copilot control give better responses to questions from app users. We recommend a brief 2-3 lines describing what the app is and what sort of questions this Copilot control will answer. This property does not impact the control's UI.

- **Placeholder text**: Replaces the control's default placeholder text in the text input box **Ask a question about the data**. We recommend updating this to a short line sharing guidance to app users about what type of questions this Copilot control can answer.

   > [!div class="mx-imgBorder"]
   > ![Configure the control.](media/copilot/copilot-5.png)









[!INCLUDE[footer-include](../../includes/footer-banner.md)]
