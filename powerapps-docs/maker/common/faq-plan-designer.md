---
title: FAQ for the Plan designer
description: FAQ that discusses the Power Apps the Plan designer and the key considerations for making use of this technology responsibly.
author: norliu
contributors: mduelae 
ms.topic: faq
ms.date: 4/10/2025
ms.author: norliu
ms.reviewer: mkaur
ms.collection: 
    - bap-ai-copilot
---

# FAQ for the Plan designer

## What is the Plan designer?

The Plan Designer is an AI-powered experience that builds an end-to-end business solution in a matter of minutes. By describing a business problem in natural language, and including images such as a legacy app, process diagram, you can expect an outline of user roles and requirements; more importantly, an end-to-end Power Platform solution generated with objects like Dataverse tables, Power Apps (canvas and model-driven apps), and Power Automate flows. In the Plan designer, you can continuously iterate and refine your business requirements to produce a more precise output tailored to your specific needs.

## What can the Plan designer do?

The Plan designer can build an end-to-end business solution based on a description of a business problem and including images such as a legacy app, process diagram. A complete plan includes an outline of user roles and requirements, an end-to-end Power Platform solution generated with objects like Dataverse tables, Power Apps (canvas and model-driven apps), and Power Automate flows.

## What is the Plan designer’s intended use?

The Plan Designer is intended to allow makers to describe their business problems and receive a comprehensive plan that includes user stories, data schema, apps, and flows. This approach saves users time by eliminating the need to learn different products within the Power Platform and creating assets separately. Additionally, the plan serves as documentation for future reference

## How was the Plan designer evaluated? What metrics are used to measure performance?

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we're conducting user studies with makers to gather their feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. Additionally, we're monitoring telemetry data to track the number of makers who tried the feature, the success rate of the feature, and the ratio of positive to negative feedback. Before releasing the Copilot feature in preview, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20%5Ct%20%22_blank).

## What are the limitations of the Plan designer? How can users minimize the impact of system or product name’s limitations when using the system?

- To use this capability, you must have a Microsoft Dataverse database in your environment.
- Preview features aren’t meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. For more information, see preview terms.
- This capability is powered by Azure OpenAI Service.
- This capability can be subject to usage limits or capacity throttling.
- This feature allows maximum input size of 4k tokens, including both text and images. (~ 3,000 words if your input only contains text)

## What operational factors and settings allow for effective and responsible use of the Plan designer?

- Here are some tips to help you get the most out of this feature:
- Try to describe the business problems end to end clearly, including types of user that needs to be involved, what tasks they should complete.
- If you’re uploading an image, make sure in the text you explain what that image is about and explicitly ask the Plan designer to use it. For example, use the ERD attached.
- If the results you get aren't what you expected, you can keep iterating with Plan designer by keep selecting a specific part you want to edit and type in your requirement.
- You can also try using the default suggestions provided in the banner and then customize them to suit your needs. And if you still can't get the desired results, send us your feedback.

## How do I provide feedback on the Plan designer?

- You can provide feedback to us using the Thumbs button in the Plan designer. We can help you better if you can provide more details.
- For Early access program, you can also directly reach out to the product team by contacting them in the Teams channel Intelligent Apps Early Access Discussion.

### See also 
[Use the Plan designer (preview)](../plan-designer/plan-designer.md)
