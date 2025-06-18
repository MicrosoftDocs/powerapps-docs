---
title: FAQ for building apps and tables through conversation
description: FAQ that discusses building apps through conversation and the key considerations for making use of this technology responsibly.
ms.date: 5/28/2025
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: franklanmsft
ms.author: franklan
ms.reviewer: mduelae
ms.collection: 
    - bap-ai-copilot
---

# FAQ for building apps and tables through conversation

These frequently asked questions (FAQ) describe the AI impact of build apps and tables through conversation feature.

## What is build apps and tables through conversation? 

Build apps and tables through conversation is a feature in the Power Apps that allows you to describe the app or table that you want to build, and AI will design it for you. To start, you use natural language to tell the AI assistant what kind of information you want to collect, track, or show. The assistant will generate a Dataverse table and use it to build your canvas app. The AI assistant is available from the Power Apps home page. 
 
## What are the system’s capabilities? 

This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview), which uses powerful language models. These language models generate new text in English that looks and sounds like text written by humans.  

Using Azure OpenAI service as a foundation, build apps through conversation considers your app description to propose relevant data tables on which to build your app. As part of data generation, the system recommends relevant columns, sample row data, and data types that you can customize. The sample data is for illustration only and is fictitious. No real association is intended or inferred.

## What is the system’s intended use? 

Build apps and tables through conversation is intended to simplify your app creation process by automatically generating a data table on which your app will be built. AI-generated content may have mistakes. Make sure it's accurate and appropriate before using it. For more information, [read the full terms](https://go.microsoft.com/fwlink/?linkid=2182773).


## How was build apps and tables through conversation evaluated? What metrics are used to measure performance? 

Build apps and tables through conversation underwent substantial testing before the feature was released. If you encounter issues with the content being generated, please submit feedback. Your feedback will be used to improve Microsoft products and services. IT admins for your organization will be able to view and manage your feedback data. 

For more information, see: [Data, privacy, and security for Azure OpenAI Service](/legal/cognitive-services/openai/data-privacy)

## What are the limitations of build apps and tables through conversation? How can users minimize the impact of the build apps through conversation limitations when using the system? 

This capability is in the process of rolling out, and may not be available in your region yet.

This capability may be subject to usage limits or capacity throttling.

The following are requirements to access this feature:

- Your account must have English (United States), French, German, Spanish, Dutch, Danish, Italian, Japanese, or Portuguese (Brazil) as the browser language.

- Have a [Microsoft Dataverse database](/power-platform/admin/create-database) in your environment. 

- AI Builder must be enabled for your environment to use the AI models or controls leveraging AI models: 

    1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

    2. Go to **Environments** > [select an environment] > **Settings** > **Features**. 

    3. On the **Features** settings page, under **AI Builder**, enable or disable **AI Builder preview models**. 

For more information, see [Copilot in Power Apps overview](../canvas-apps/ai-overview.md) 

## What operational factors and settings allow for effective and responsible use of the system? 

Follow these procedures to make the most of the feature: 

- Use everyday words to describe what your app should collect, track, list, or manage such as the following:
  - “Collect RSVPs for the team birthday party” 
  - “Track sales leads” 

- Customize the data table with prompts such as:
   - “Add a column for …” 
   - “Remove the … row” 
   - “Change the data type for the … column to… “ 

- When in doubt, you can ask the AI assistant for help by typing, “Give me suggestions”

## See also

- [Build apps through conversation](../canvas-apps/ai-conversations-create-app.md)

 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]

