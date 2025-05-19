---
title: FAQ on filtering, sorting, and searching Power Apps galleries with Copilot 
description: This FAQ outlines how AI filters, sorts, and searches Power Apps galleries with Copilot, addressing its usage, testing, evaluation, and limitations. 
ms.date: 05/22/2024
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: jordanchodak
ms.author: jordanchodak
ms.reviewer: smurkute
ms.collection: 
    - bap-ai-copilot 
---

# FAQ on filtering, sorting, and searching Power Apps galleries with Copilot

These frequently asked questions (FAQ) describe the AI effect of filtering, sorting, and searching Power Apps canvas galleries with Copilot.

## What is filtering, sorting, and searching with Copilot?

Filtering, sorting, and searching with Copilot is a feature for users of Power Apps who want to filter their galleries using natural language. It surfaces in galleries of canvas apps that use SharePoint as their backend. There are plans to expand to other data sources in the future.

## What are the system’s capabilities?

It takes the user's input and uses advanced language models to filter, sort, and search the gallery. The user can then add more filters, view and remove current filters, or accept to persist the filtered view.

## What is the system’s intended use?

As an AI assistant to users, it filters the gallery based on the user's input.

## How was filtering, sorting, and searching with Copilot evaluated? What metrics are used to measure performance?

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we're conducting studies with users to gather feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. We're also monitoring customer data to track the number of users who tried the feature, the success rate of the feature, and the ratio of positive feedback to negative feedback.

Before releasing the feature in preview, we conducted extensive testing to ensure its functionality. If you encounter any issues with your experience, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20\t%20%22_blank).

## What are the limitations of filtering, sorting, and searching with Copilot? How can users minimize the effect of the filtering, sorting, and searching with Copilot limitations when using the system?

- To use this capability, you must be a premium user.
- Preview features aren’t meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
- For more information, go to [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
- This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
- This capability might be subject to usage limits or capacity throttling.
- Your environment must be in the United States region or the [**Move data across regions**](/power-platform/admin/geographical-availability-copilot) checkbox must be selected in Power Platform admin center.
- This feature doesn’t support non-English language input.

## What operational factors and settings allow for effective and responsible use of the system?

If you get this error, **Sorry, Copilot can’t help right now. Try again later.**, this might be due to capacity limits. We recommend that you give the system some time before trying again.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
