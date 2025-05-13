---
title: FAQ for the Plan designer
description: FAQ that discusses the Power Apps the Plan designer and the key considerations for making use of this technology responsibly.
author: norliu
contributors: mduelae 
ms.topic: faq
ms.date: 5/19/2025
ms.author: norliu
ms.reviewer: mkaur
ms.collection: 
    - bap-ai-copilot
---

# FAQ for the Plan designer

## What is the Plan designer?

The Plan designer is an AI-powered experience that builds an end-to-end business solution in a matter of minutes. By simply describing a business problem in natural language, and including images such as a screenshot of a legacy app, process diagram, you can expect an outlined user role and requirements; more importantly, an end-to-end Power Platform solution generated with objects like Dataverse tables, Power Apps (canvas and model-driven apps), Power Automate cloud flows, Power Pages sites, Power BI, and Microsoft Copilot Studio agents. In the Plan designer you can iterate and further refine your business requirements to generate a more precise output based on your exact needs.

## What can the Plan designer do?

The plan designer can build an end-to-end business solution based on a description of a business problem and include images, such as a legacy app or process diagram. A complete plan includes an outlined user roles and requirements, an end-to-end Power Platform solution generated with objects like Dataverse tables, Power Apps (canvas and model-driven apps), Power Automate cloud flows, Power Pages, Power BI, and Microsoft Copilot Studio agents.

## What is the Plan designer’s intended use?

The intended use is a maker could come to Plan designer and by just describing their business problem, we can come up with a comprehensive plan including user stories, data schema, and apps/flows/agents to build so it can save time for the user to learn and integrate different products in the Power Platform.

Furthermore, the plan would serve as a documentation for user to refer to later.

## How was the Plan designer evaluated? What metrics are used to measure performance?

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we're conducting user studies with makers to gather their feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. Additionally, we're monitoring telemetry data to track the number of makers who tried the feature, the success rate of the feature, and the ratio of positive to negative feedback. Before releasing the feature, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20%5Ct%20%22_blank).

## What are the limitations of the Plan designer? How can users minimize the impact of system or product name’s limitations when using the system?

- To use this capability, you must have a Microsoft Dataverse database in your environment.
- This capability is powered by Azure OpenAI Service.
- This capability is in process of rolling out, and might not be available in your region yet.
- This capability can be subject to usage limits or capacity throttling.
- This feature lets a maximum input size of 4k tokens, including both text and images (~3,000 words if your input only contains text).


## What operational factors and settings allow for effective and responsible use of the Plan designer?

- Here are some tips to help you get the most out of this feature:
- Try to describe the business problems end to end clearly, including types of user that needs to be involved, what tasks they should complete. 
- If you’re uploading an image, make sure in the text you explain what that image is about and explicitly ask Plan designer to use it. E.g.,  use the ERD attached.
- If the results you get aren't what you expected, you can keep iterate with Plan designer by keep selecting a specific part you want to edit and type in your requirement.
- You can also try using the default suggestions provided in the banner and then customize them to suit your needs. And if you still can't get the desired results, send us your feedback.


## How do I provide feedback on the Plan designer?

- You can provide feedback to us using the Thumbs button in the Plan designer. We can help you better if you can provide more details. 
### See also 
[Overview of Plan designer](../plan-designer/plan-designer.md)
