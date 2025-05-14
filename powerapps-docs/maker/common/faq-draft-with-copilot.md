---
title: FAQ about drafting well-written input text with Copilot
description: This FAQ provides information about the AI technology used to draft well-written input text with Copilot, along with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
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

# FAQ about drafting well-written input text with Copilot

These frequently asked questions (FAQ) describe the AI impact of drafting well-written input text with Copilot in Power Apps.

##  What is Draft with Copilot? 

**Draft with Copilot** is a feature for users of Power Apps who want to create well-written input text while saving time. It surfaces in multi-line text boxes and rich text editors.

## What are the system’s capabilities? 

It takes the user's input and uses advanced language models to generate content suggestions, correct grammar errors, and eloquently refine the user's ideas. The user can also change the tone and length of the output to fit their scenario.

## What is the system’s intended use? 

As an AI assistant to users, it provides content suggestions and refined text based on the user's input.

## How was Draft with Copilot evaluated? What metrics are used to measure performance? 

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we're conducting studies with users to gather feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. We're also monitoring telemetry data to track the number of users who tried the feature, the success rate of the feature, and the ratio of positive feedback to negative feedback.

Before releasing the **Draft with Copilot** feature in preview, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20\t%20%22_blank).

## What are the limitations of Draft with Copilot? How can users minimize the impact of the Draft with Copilot limitations when using the system? 

- To use this capability, you must be a premium user. 
- Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. 
- For more information, go to [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520). 
- This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview). 
- This capability is in process of rolling out, and may not be available in your region yet. 
- This capability may be subject to usage limits or capacity throttling. 
- Your environment must be in the United States region or the [**Move data across regions**](/power-platform/admin/geographical-availability-copilot) checkbox must be selected in Power Platform admin center.
- This feature doesn’t support non-English language input. 

## What operational factors and settings allow for effective and responsible use of the system? 

If you get this error, **There was a problem using this description. Try again.**, this might be due to capacity limits. We recommend that you give the system some time before trying again. It may also be that you have not given the system enough information to properly generate output. Add more details to try again.

 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
