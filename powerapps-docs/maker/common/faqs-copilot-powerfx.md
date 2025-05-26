---
title: FAQs about using Copilot with Power Fx
description: FAQ that discusses Copilot and Power Fx
ms.date: 7/15/2024
ms.custom:
  - transparency-note
ms.topic: faq
author: jorisde
ms.author: jorisde
ms.reviewer: mduelae
ms.collection:
    - bap-ai-copilot
---

# FAQ about using Copilot with Power Fx

These frequently asked questions (FAQ) describe the AI impact of using Copilot to write or explain Power Fx formulas. 

##  What is Copilot for Power Fx?

Power Apps Studio has several features to help makers understand and write Power Fx. Makers can use the formula bar to explain code, or use Power Fx comments in the formula bar to describe a formula and receive a suggested Power Fx expression. Additionally, the inline action bar on supported controls provides the ability to describe a formula and receive a suggested formula and a suggested property to apply the formula to.
 
## What are the system's capabilities?

- Write a comment in the formula bar that describes a formula to receive a suggested Power Fx expression.
- Receive an explanation for the current formula displayed in the formula bar.
- Open Copilot from a supported control's inline action bar to describe a formula and receive a suggested formula and suggested property to apply it to.

## What is the system's intended use?

- Generate a single Power Fx expression from an English description.
- Generate an English description of the formula shown in the formula bar.

## What languages are supported?

Because Power Fx can be used across many different features, each generally available (GA) feature may have a different set of supported languages the meet Microsoft's responsible AI standards. For details on language support for specific features see, [Create Power Fx formulas with Copilot](../canvas-apps/ai-formulas-formulabar.md#language-support)

## How was Power Fx with Copilot evaluated? What metrics are used to measure performance?

We qualitatively test the model's Power Fx formula generation and descriptions against an internally built set of Power Fx formulas and descriptions. Additionally, we're monitoring telemetry data to track the number of makers who tried the feature, the success rate of the feature, and the ratio of positive to negative feedback.
Before releasing the Copilot feature in preview, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=521839).

## What are the limitations of Power Fx with Copilot? How can users minimize the impact of Power Fx Copilot limitations when using the system?

- Named Formulas and User Defined Functions can't be generated with Copilot at this time.
- Variables have to be in use (declared) already for Copilot to use them, it doesn't introduce new variables.
- Preview features aren't meant for production use and might restrict functionality. These features are available before an official release so that customers can get early access and provide feedback. 
- More information available in [preview terms](https://go.microsoft.com/fwlink/?linkid=2173149). 
- This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview). 
- This capability is in process of rolling out, and might not be available in your region yet. 
- This capability can be subject to usage limits or capacity throttling. 
- Your environment must be in the United States region.
- This feature doesn't support non-English language input.  

## What operational factors and settings allow for effective and responsible use of the system?

Here are some tips to help you get the most out of this feature:

- Use simple language to explain the formula you're looking for, such as "if myvariable is true, return green" or "filter mylist on IDs that are larger than 5".
- If the results you get aren't what you expected, try being more precise with exact names of variables, controls and field names, or try rephrasing the question.
- If you still can't get the desired results, send us your feedback.

 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
