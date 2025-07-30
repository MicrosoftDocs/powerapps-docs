---
title: FAQ for rename controls in canvas apps with Copilot 
description: FAQ that discusses renaming canvas apps controls with Copilot.
ms.date: 5/25/2025
ms.update-cycle: 180-days
ms.custom: 
  - transparency-note
ms.topic: faq
author: mamali 
ms.author: mamali
ms.reviewer: 
ms.collection: 
    - bap-ai-copilot
---

# FAQ for rename controls in canvas apps with Copilot

These frequently asked questions (FAQ) describe the AI impact of Power Apps rename controls in canvas apps with Copilot feature. 

##  What is rename Canvas controls with Copilot?

With rename canvas controls with Copilot feature, makers can delegate renaming Canvas controls during app development to an AI assistant. When makers rename a control manually, they can expect Copilot to show up with renaming suggestions for other controls with valid property value. Makers can preview the suggestions before applying, ensuring full control over Copilot's suggestions. This feature's goal is to save makers time and effort otherwise spent manually renaming controls one by one, ensuring app maintainability and easy reference of controls in logic.
 
## What are the system’s capabilities? 

The following system capabilities are supported:
- Provide control rename suggestions based on primary property of the controls and naming convention/pattern used by maker during manual rename.
- Enable makers to apply all or selected rename suggestions.
- Apply rename to multiple controls at once, per the suggestions shown in preview.
- Copilot nudges the maker when they manually rename a control, and there are other controls of the same type under the same screen with valid, nondefault value such as **Button** or **Text** in **Text** property.
- Text property can be a Text literal or a formula returning Text type.
- Any formulas referencing the control name is automatically updated to use the rename.

The following controls are supported: 

- Button 
- Label 

Support for more controls is coming soon.

## What is the system’s intended use? 

As an AI assistant that helps people rename Canvas controls, Copilot provides the following list of UI actions for makers that are included in the preview release scope:
- Click on Copilot icon when it appears near Tree View after a manual rename action.
- Copilo only appears if there are other controls of the same type under the same screen with valid, nondefault value such as **Button** or **Text** in **Text** property.
- Preview control renaming suggestions provided by Copilot.
- Apply one or more rename suggestions at once.

## How was rename Canvas controls with Copilot evaluated? What metrics are used to measure performance? 

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we're conducting user studies with makers to gather their feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. Additionally, we're monitoring telemetry data to track the number of makers who tried the feature and the success rate and acceptance rate of the feature.
Before releasing the Copilot feature in preview, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20\t%20%22_blank).

## What are the limitations of rename Canvas controls with Copilot? How can users minimize the impact of rename Canvas controls with Copilot limitations when using the system? 

- Preview features aren’t meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. 
- For more information, see [preview terms](https://go.microsoft.com/fwlink/?linkid=2173149). 
- This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview). 
- This capability is in process of rolling out, and might not be available in your region yet. 
- This capability can be subject to usage limits or capacity throttling. 
- Your environment must be in the United States region.
- This feature doesn’t support non-English language input. 
- This feature only supports limited controls and actions as listed in the [intended use](faq-rename-control.md#what-is-rename-canvas-controls-with-copilot) section. Microsoft is actively working on expanding the scope of this feature and support more controls incrementally. 

## What operational factors and settings allow for effective and responsible use of the system? 

Here are some tips to help you get the most out of this feature:

- Use this feature after Text property of controls has been set to ensure quality results from Copilot. For example, a button with default Text property value "Button" or invalid Text property value If() won't be considered for rename. And if you still can't get the desired results, send us your feedback.
- Use standard and relevant name and naming pattern when manually renaming a control so Copilot can reference it while suggesting renames. Avoid use of special characters and space. For example, renaming a button to "collectResponse" will provide better renaming suggestions for other buttons than "collect_1"
- Ensure New Analysis Engine app setting is enabled in your app. Go to Settings, click Updates, New, and then turn on New analysis engine toggle to true.


## See also 
[Rename controls in canvas apps with Copilot (preview)](../canvas-apps/controls/copilot-rename-controls.md)

 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]
