---
title: FAQ for the Plan designer
description: FAQ that discusses the Power Apps the Plan designer and the key considerations for making use of this technology responsibly.
author: norliu
contributors: mduelae 
ms.custom:
  - responsible-ai-faqs
ms.topic: faq
ms.date: 6/19/2025
ms.author: norliu
ms.reviewer: mkaur
ms.collection: 
    - bap-ai-copilot
---

# FAQ for the Plan designer

## What is the Plan designer?

The Plan designer is an AI-powered experience that builds an end-to-end business solution in minutes. Describe your business problem in natural language and include images, like a screenshot of a legacy app or a process diagram. The Plan designer outlines user roles and requirements, and generates a complete Power Platform solution with objects like Dataverse tables, Power Apps (canvas and model-driven apps), Power Automate cloud flows, Power Pages sites, Power BI, and Microsoft Copilot Studio agents. You can iterate and refine your business requirements in the Plan designer to get a more precise solution that fits your needs.

## What can the Plan designer do?

The Plan designer builds an end-to-end business solution based on a description of a business problem and can include images, like a legacy app or process diagram. A complete plan outlines user roles and requirements, and includes an end-to-end Power Platform solution with objects like Dataverse tables, Power Apps (canvas and model-driven apps), Power Automate cloud flows, Power Pages, Power BI, and Microsoft Copilot Studio agents.

## What is the Plan designer’s intended use?

Plan designer lets makers describe their business problem and quickly get a comprehensive plan. The plan includes user stories, data schema, and apps, flows, and agents to build. This approach saves time and helps users learn and integrate different Power Platform products.

The plan also serves as documentation that users can refer to later.

## How was the Plan designer evaluated? What metrics are used to measure performance?

We evaluate the feature both qualitatively and quantitatively. To check quality, we conduct user studies with makers to get feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. Also, monitor telemetry data to track the number of makers who try the feature, the feature's success rate, and the ratio of positive to negative feedback. Before releasing the feature, run extensive testing to check its functionality. If you find any issues with the generated content, provide feedback. Microsoft uses your feedback to improve products and services. Your organization's IT admins can access your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20%5Ct%20%22_blank).

## What are the limitations of the Plan designer? How can users minimize the impact of system or product name’s limitations when using the system?

- To use this capability, you need a Microsoft Dataverse database in your environment.
- This capability is powered by Azure OpenAI Service.
- This capability can be subject to usage limits or capacity throttling.
- This feature lets you use a maximum input size of 4,000 tokens, including both text and images (about 3,000 words if your input only has text).
  
## What operational factors and settings allow for effective and responsible use of the Plan designer?

- Use these tips to get the most out of this feature:
- Clearly describe the business problems end to end, including the types of user involved and the tasks they need to finish.
- If you upload an image, explain what the image shows in the text and explicitly ask Plan designer to use it. For example, say "Use the ERD attached."
- If the results aren't what you expect, keep iterating with Plan designer by selecting the specific part you want to edit and typing your requirement.
- Try the default suggestions in the banner, then customize them to suit your needs. If you still can't get the results you want, send us your feedback.


## How do I provide feedback on the Plan designer?

- Select the thumbs up or thumbs down in the plan document to provide feedback on a specific section. 
- Select the **Give feedback** icon in the command bar to provide general feedback on the Plan designer experience. 

### See also
[Overview of Plan designer](../plan-designer/plan-designer.md)
