---
title: FAQ about generative pages in model-driven apps
description: This FAQ provides information about the AI technology used in the generative pages feature with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 07/10/2025
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: jasongre
ms.author: jasongre 
ms.reviewer: matp
ms.collection: 
    - bap-ai-copilot 
---
# FAQ about generative pages in model-driven apps

These frequently asked questions (FAQ) describe the AI impact of generative pages in model-driven apps.

## What are generative pages?

Generative pages simplify the app design process for model-driven app makers through AI code generation. By describing their needs in natural language, makers can create fully structured pages in their apps. The system processes these requirements and intelligently generates React code that covers both the frontend user experience and backend functionality, ensuring modern, consumer-grade UI experiences for enterprise applications. Makers must publish these pages before they are available to users in apps.

## What can you do with generative pages? 

With generative pages, makers can create and refine app pages in real time through an interactive, conversational experience. They can adjust elements, layout, and functionality to perfectly match their vision. This capability helps ensure designs adhere to best practices and deliver high-quality user experiences, making the app development process more efficient and intuitive. When makers are satisfied with the generated page, they can publish them so they are available when playing the app.

## What is the intended use of generative pages?

The intended use of generative pages is to streamline the app design process for model-driven app makers. By leveraging AI to generate React code based on natural language descriptions, makers can quickly create pages that meet their specific requirements. This tool is designed to enhance productivity and ensure that app designs are both functional and visually appealing.

## How were generative pages evaluated? What metrics are used to measure performance?

In our evaluations, we measure how often the agent can generate syntactically-correct code, and we also test how good the generation is from a UX perspective. Moreover, the agent is evaluated for satisfying Microsoft’s responsible AI principles.

## What are the limitations of generative pages? How can users minimize the impact of generative page limitations when using the system?

The current limitations of generative pages include:

- The system might have difficulty with complex design requirements.
- Pages can only connect to Dataverse tables and perform CRUD operations.
- There is no ability to manually edit the generated code.
- Generated pages can't be moved between environments.
- Must add all needed Dataverse tables in the first prompt.

Makers can minimize the impact of these limitations by testing any generated code before publishing it to users.

## What operational factors and settings allow for effective and responsible use of generative pages?  

Effective and responsible use of generative pages involves setting clear guidelines for app design requirements and ensuring that makers provide comprehensive descriptions. Regular training on best practices for using the tool and monitoring its performance can help maintain high standards. Additionally, incorporating user feedback and continuously
improving the system based on real-world usage can enhance its effectiveness.

Makers are always required to publish generative pages before they are made available to users. Extensive testing of any code before making it available in production is always
encouraged.

## Related articles

[Describe a page using natural language](../model-driven-apps/generative-pages.md)
