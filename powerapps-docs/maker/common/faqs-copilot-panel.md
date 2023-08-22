---
title: FAQ for continue to edit your app with Copilot 
description: FAQ that discusses continuing to edit your app with Copilot and the key considerations for making use of this technology responsibly.
ms.date: 6/14/2023
ms.custom: 
  - transparency-note
ms.topic: article
author: norliu 
ms.author: norliu
ms.reviewer: mduelae
---

# FAQ for continue to edit your app with Copilot 

These frequently asked questions (FAQ) describe the AI impact of Power Apps' continue to edit your app with Copilot feature. 

##  What is continue to edit your app with Copilot? 

With continue to edit your app with Copilot feature, makers can delegate some tasks of app development to an AI assistant by telling Copilot their requirements. Makers can expect actions such as add, edit, or style controls, work with containers, and bulk edits. This allows makers to concentrate on designing the app while maintaining oversight of all actions taken by Copilot.
 
## What are the system’s capabilities? 

The following system capabilities supported:
- Add a screen using pre-existing templates.
- Add and modify properties of a single control, limited to classic controls only.
- Update multiple controls at once.
- Work with containers.
- Provide default suggestions for users to help in typing.
- Use templatized formulas such as Navigate() to create buttons that perform specific actions, like navigating to the Home screen, and SubmitForm() for creating a Submit button for Form2.

The following controls are supported: 
- Screen 
- Container 
- Gallery 
- Form 
- Button 
- Label 
- TextInput 

## What is the system’s intended use? 

As an AI assistant that helps people find information, Copilot provides the following list of UI actions for makers that are included in the preview release scope:
- Add a screen using existing screen templates
- Add and update properties of a single classic control
- Bulk updates controls on a single screen
- Work with containers
- Provide default suggestions to guide users on what to type in
- Offer the following templatized formulas to build your app:
    - Navigate(): For example, "Create a button for Home that navigates to the Home Screen"

## How was continue to edit your app with Copilot evaluated? What metrics are used to measure performance? 

We evaluate the feature both qualitatively and quantitatively. To assess the quality of the feature, we are conducting user studies with makers to gather their feedback on their experiences, thoughts about the feature's quality, and suggestions for improvement. Additionally, we are monitoring telemetry data to track the number of makers who tried the feature, the success rate of the feature, and the ratio of positive to negative feedback.
Before releasing the Copilot feature in preview, we conducted extensive testing to ensure its functionality. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://go.microsoft.com/fwlink/?linkid=2182930%22%20\t%20%22_blank).

## What are the limitations of continue to edit your app with Copilot? How can users minimize the impact of the [Feature] limitations when using the system? 

- To use this capability, you must have a [Microsoft Dataverse database](/power-platform/admin/create-database) in your environment. 
- Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. 
- For more information, see [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520). 
- This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview). 
- This capability is in process of rolling out, and may not be available in your region yet. 
- This capability may be subject to usage limits or capacity throttling. 
- Your environment must be in the United States region.
- This feature doesn’t support non-English language input. 
- This feature only supports limited controls and actions as listed in the [intended use](faqs-copilot-panel.md#what-is-continue-to-edit-your-app-with-copilot) section. Microsoft is actively working on expanding the scope of this feature and support more actions incrementally. 

## What operational factors and settings allow for effective and responsible use of the system? 

Here are some tips to help you get the most out of this feature:

- Use simple language to explain the changes you want to make to your app, such as "add a new screen" or "insert 2 buttons".
- If the results you get aren't what you expected, try being more precise. For example, you could say "add a new button to the selected container", "change the color of the selected button to red", or "display Screen 2 when Button1 is clicked".
- You can also try using the default suggestions provided in the Copilot panel and then customize them to suit your needs. And if you still can't get the desired results, send us your feedback.


## See also 
- [Continue editing your app with Copilot (preview)](../canvas-apps/ai-edit-app.md)

 
[!INCLUDE[footer-include](../../includes/footer-banner.md)]

