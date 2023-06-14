---
title: Transparency note for continue to edit your app with Copilot 
description: The transparency note discusses continue to edit your app with Copilot and the key considerations for making use of this technology responsibly. .
ms.date: 6/14/2023
ms.custom: 
  - transparency-note
ms.topic: article
author: norliu 
ms.author: norliu
ms.reviewer: mduelae
---

# Transparency note for continue to edit your app with Copilot 

This transparency note describes the AI impact of Power Apps' continue to edit your app with Copilot feature. 

##  What is continue to edit your app with Copilot? 

[Describe the system in plain English. What type of system is this? What does it do? At a high level, what does the system take as input? What kind of outputs does the system produce?] 

Continue to edit your app with Copilot is a feature that aims at taking the heavy lift for makers in the app making process so makers can tell Copilot their requirements and Copilot make it happen for makers. It will include actions like adding/editing/styling a control, working with containers, bulk editing etc. So makers can focus more on designing the app and also stay in control by reviewing all actions Copilot does for them. 
 
## What are the system’s capabilities? 

The system has following capabilities:

- Adding a screen from existing screen templates 

- Adding and updating properties of a single control – classic controls only 

- Bulk updating controls 

- Working with containers 

- Default suggestions for people to know what to type in. 

- Templatized formulas:

    - Navigate(), (~"Create button Home that navigates to the Home Screen") 

    - SubmitForm() (~"Create Submit button for Form2") 

Supported components/controls: 

- Screen 

- Container 

- Gallery 

- Form 

- Button 

- Label 

- TextInput 

## What is the system’s intended use? 

Generate UI actions for makers. The scope for preview release includes: 

- Add a screen from existing screen templates 

- Add and update properties of a single classic control 

- Bulk update controls on a single screen 

- Work with containers 

- Default suggestions for people to know what to type in. 

- Templatized formulas for build: 

    - Navigate(), (~"Create button Home that navigates to the Home Screen") 

    - Gallery.Selected (~"Link Form2 with Gallery 3") 

    - SubmitForm() (~"Create Submit button for Form2") 

- Merging with Power Apps Ideas for MPPC 

## How was continue to edit your app with Copilot evaluated? What metrics are used to measure performance? 

We measure the feature qualitatively and quantitatively. We will conduct user studies with makers to ask for their feedback, how they think about the quality of the feature, feedback on experiences, and suggestions for improvement. 
We will also track from telemetry including how many makers tried the feature, how many were able to get a response and what’s the thumbsup and down ratio. 
Continue to build apps with Copilot underwent substantial testing before the feature was released in preview. If you encounter issues with the content being generated, please submit feedback.  Your feedback will be used to improve Microsoft products and services. IT admins for your organization will be able to view and manage your feedback data. Read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20\t%20%22_blank).

## What are the limitations of continue to edit your app with Copilot? How can users minimize the impact of the [Feature] limitations when using the system? 

- To use this capability, you must have a [Microsoft Dataverse database](/power-platform/admin/create-database) in your environment. 
- Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. 
- For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520). 
- This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview). 
- This capability is in process of rolling out, and may not be available in your region yet. 
- This capability may be subject to usage limits or capacity throttling. 
- Your environment must be in the United States region.
- The feature works best on English, it doesn’t support other languages well yet. 
- The feature only supports limited controls and actions (as listed in the intended use section above) and MSFT is actively working on expanding scope and supporting more actions incrementally. 

## What operational factors and settings allow for effective and responsible use of the system? 

Follow these guildlines to make the most of the feature:  

- Use everyday words to describe how you want to edit your app, such as “add a new screen”, “add a new email screen”, or “add 2 buttons”.
- When results don't meet your expectations, try to be specific, like “add a new button in the selected container”, “make the selected button red”, or “when clicking on Button1 show Screen 2”. 
- You can also try the default suggestions that are offered in the Copilot panel and make modifications. And if it still doesn’t meet your needs, send us your feedback. 


## See also 
- [Use natural language to edit an app (preview)](../canvas-apps/ai-edit-app.md)

 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]

