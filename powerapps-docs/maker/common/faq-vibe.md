---
title: FAQ for Power Apps vibe experience (preview)
description: FAQ that discusses Power Apps vibe experience and the key considerations for making use of this technology responsibly.
author: damialajogun
contributors: mduelae 
ms.custom:
  - responsible-ai-faqs
ms.topic: faq
ms.date: 03/11/2026
ms.update-cycle: 180-days
ms.author: damialajogun
ms.reviewer: mkaur
ms.collection: 
    - bap-ai-copilot
---

# FAQ for the Power Apps vibe experience (preview)

## What is Power Apps vibe?

Power Apps vibe is an AI-powered app creation experience that helps makers quickly build functional business applications using natural language. Makers describe what they want to build, and vibe translates those descriptions into working app experiences, including data, screens, and logic. At a high level, Power Apps vibe takes maker prompts and optional context as input and produces a draft app that makers can review, refine, and publish. 

## What can Power Apps vibe do?

Power Apps vibe helps makers create apps faster by generating a fully functional app (including app structures, screens, and interactions) based on natural language descriptions. Makers can iteratively refine their apps by adjusting prompts, editing generated outputs, and previewing changes in real time. Power Apps vibe is designed to accelerate early app creation and reduce the effort required to get from an idea to a usable application. 

## What is the intended use of Power Apps vibe?

Power Apps vibe is intended to support makers who want to quickly prototype, explore, and build business applications without starting from scratch. It helps makers translate ideas into working apps, learn app-building concepts through iteration, and accelerate time to value. 

## How was Power Apps vibe evaluated? What metrics are used to measure performance?

Power Apps vibe is evaluated using a combination of qualitative and quantitative methods. Evaluation includes user studies with makers to assess the quality of generated outputs, usability of the experience, and how effectively Power Apps vibe supports app creation workflows. Feedback from these studies helps identify strengths, gaps, and opportunities for improvement.

In addition to qualitative feedback, telemetry data is monitored to understand how makers use Power Apps vibe in practice. This data includes metrics such as feature usage, completion and success rates, and the ratio of positive to negative feedback signals. Before release, Power Apps vibe undergoes extensive functional testing to validate reliability and behavior across supported scenarios. For more information, see the [Privacy Statement](/privacy/privacystatement).

## What are the limitations of Power Apps vibe? How can users minimize the impact of Power Apps vibe’s limitations when using the system?

Like other AI-powered experiences, Power Apps vibe has known limitations. Generated apps might not always fully reflect a maker’s intent. They might require extra refinement or might not be suitable for complex or highly customized production scenarios without further modification. Outputs are based on the information provided by the maker and the capabilities available in the platform. 

Known limitations include:
- Non-English languages aren't supported. 
- Supports image attachment up to 2 MB. 
- You can't access or edit apps created outside of Power Apps vibe. 
- If you export an app and edit it outside Power Apps vibe (for example, in VS Code), redeploying via PAC CLI creates a new app, and it disconnects from the original plan. 
- Currently, you can only have one app per plan; multiple apps within a single plan aren't supported. 
- You can't open preexisting plans in Power Apps vibe. 
- Canvas and model-driven apps aren't supported; you can't recommend, open, or edit these app types in Power Apps vibe. 
- Existing tables aren't automatically recommended during data model proposal; you can manually add existing tables to your plan. 
- Editing existing Dataverse tables via chat isn't currently supported; you can make changes to these tables through the data editor manually. 
- Direct code edits in Code view or Split view aren't supported; you can't modify code directly in these views. 
- You can't directly create proposed technologies (apart from code apps) from the plan; you must add additional technologies manually.

Makers can minimize the impact of these limitations by: 

- Providing clear, specific descriptions of their app requirements. 
- Iterating on prompts and reviewing generated outputs carefully. 
- Testing app behavior and data interactions before publishing. 
- Treating generated apps as a starting point rather than a finished solution. 

Makers are ultimately responsible for validating that their apps meet their functional, security, and compliance requirements. 
  
## What operational factors and settings allow for effective and responsible use of Power Apps vibe?

Effective and responsible use of Power Apps vibe depends on how makers configure and interact with the system. Makers should: 

- Clearly describe business scenarios, users, and tasks when prompting 
- Review generated content before saving or sharing it 
- Test apps in appropriate environments prior to broader use 
- Follow organizational governance, data, and compliance policies 

## How do I provide feedback for Power Apps vibe?

- Select the thumbs up or thumbs down in the chat pane to provide feedback on a specific action. 
- Select the **Give feedback** icon in the command bar to provide general feedback, report an issue, or share suggestions. 

## See also

[Create apps, data, and plans together using vibe (preview)](../../vibe/create-app-data-plan.md)



