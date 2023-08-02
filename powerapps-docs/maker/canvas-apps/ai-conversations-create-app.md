---
title: Build apps through conversation
description: Build apps through conversation with AI.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 3/13/2022
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Build apps through conversation (preview)

[This article is prerelease documentation and is subject to change.]

Create Power Apps with the help of AI. Describe the app that you want to build, and AI will design it for you.

With the **Copilot** feature in Power Apps, you get in-app guidance using natural language processing to help you build your app.

The AI assistant is available from the Power Apps home screen. You can tell the AI assistant what kind of information you want to collect, track, or show and the assistant will generate a Dataverse table and use it to build your canvas app.

> [!div class="mx-imgBorder"]
> ![Tell the AI assistant the information you want to track in your app.](media/artificial-intelligence/create-app-using-ai-1.png)

> [!IMPORTANT]
> - To use this capability your environment must be in the US region.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability  may be subject to usage limits or capacity throttling.
> - To understand capabilities and limitations of AI-powered and Copilot features in Power Apps, see [Transparency notes for Power Apps](../common/transparency-note.md)



## Prerequisites

Prerequisites for AI features: [AI Copilot overview (preview)](ai-overview.md)


## Step 1: Create an app with the help of AI

To help you get started, let's build an app to track housekeeping tasks for a hotel.

1. Sign in to [Power Apps](https://make.powerapps.com).

2. In the text box, enter **hotel housekeeping**.

   > [!div class="mx-imgBorder"]
   > ![Describle your app.](media/artificial-intelligence/describe-your-app.png)

3. A Dataverse table with data that includes typical hotel housekeeping tasks is created for you.

## Step 2: Review the table for your app

Based on what you described, AI generates a table for your app. You can take the following actions:

1. **Suggestions**: These are suggested actions that you can ask the AI assistant to take to help you finalize the table.

2. **View column**: Select to view the column name.

3. **Edit table name**: View the table name and its properties.

4. **Copilot**: Enter text to instruct the AI assistant on how to modify the table, such as remove room type column.

5. **Create app**: Select **Create app** to create an app based on the table or select **Cancel** to start over.

   > [!div class="mx-imgBorder"]
   > ![Review table for your app.](media/artificial-intelligence/table-created.png)

   
   > [!IMPORTANT]
   > If you encounter any issues during the app creation process related to permissions or if you don't have access to Dataverse, a dialog box will appear asking you to create the app in your own environment. You will need to confirm that the table and app can be created in your environment to proceed. In case you don't have a personal developer environment, a new one will be automatically created for you. For more information, see [Get your developer environment (preview)](../maker-create-environment.md).

## Step 3: Make edits

If you want to make changes, use the **Copilot** panel to describe what you want to do, and it will make the change for you. Let's ask **Copilot** to add a column to track cleaning start and end time.

1. In the **Copilot** text box enter, **Add columns to track start and end time**.

   > [!div class="mx-imgBorder"]
   > ![Enter text to tell Copilot how you want to edit the table.](media/artificial-intelligence/add-column.png)

2. **Copilot** has added two new columns called, **Start Time** and **End Time**.

   > [!div class="mx-imgBorder"]
   > ![Example of columns that Copilot created.](media/artificial-intelligence/column-created.png)


3. You can continue editing the table by adding features such as room status, change rooms, or set priority levels for each room. When you're ready to create your app, select **Create app**.


### See also

[AI Copilot overview (preview)](ai-overview.md)

[Add Chatbot control to a canvas app (preview)](add-ai-chatbot.md)

[Add Copilot control to a canvas app (preview)](add-ai-copilot.md)

[Leverage Azure OpenAI Service in AI Builder (preview)](/ai-builder/prebuilt-azure-openai) 



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
