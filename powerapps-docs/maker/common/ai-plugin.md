---
title: AI plugins in Power Platform (preview)
description: Use Power Apps to create AI plugins.
ms.date: 11/07/2023
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.topic: how-to
ms.subservice: common
manager: tapanm
ms.custom: bap-template
search.audienceType: 
  - maker, admin
ms.collection: 
    - bap-ai-copilot
---

# AI plugins in Power Platform (preview)

[This article is prerelease documentation and is subject to change.]

The AI plugins leverage Power Platform components like flows, connectors or prompts to define a specific business behavior which can be added to a Copilot. The Copilot will use the appropriate plugin able to address the questions of an end user in the application. You can use [Power Apps](https://make.powerapps.com) to view and create AI plugins for use across Power Platform and Microsoft 365. 

With AI plugins, makers can build capabilities enabling Copilot to answer questions they wouldn’t be able to tackle by default or to enhance out-of-the-box answers.

Use [Power Apps](https://make.powerapps.com/) to create AI plugins. You can also go to [Microsoft Copilot Studio](/microsoft-copilot-studio/copilot-plugins-overview) to create AI plugins for use across Power Platform.

:::image type="content" source="media/ai-plugins.png" alt-text="AI plugin":::

> [!NOTE]
> This article introduces you to the AI plugin experience available in Power Apps interface. The experience creating AI plugins in Power Apps is same in Microsoft Copilot Studio. For detailed step-by-step instructions creating AI plugins using Power Apps or Microsoft Copilot Studio interface, see [Create AI plugins for Microsoft Copilot](/microsoft-copilot-studio/copilot-ai-plugins)

## Types of AI plugins.

You can create the following different types of AI plugins using Power Apps experience.


|ColumPlugin type  |Description  |
|---------|---------|
|Prompts plugins     | Prompts allow generating content using natural language which includes summarizing, classifying, extracting entities, translating, assessing sentiment and much more. [Learn more](AIB prompts doc page)   |
|Custom connector plugins     | Custom connectors allow retrieving and updating data from external sources accessed through APIs. [Lean more](/connectors/custom-connectors)  |
|Open AI plugins       | Open AI plugins provide access to data sources, allowing specific data to be surfaced through AI experiences that would not normally be available through general models. [Learn more](https://platform.openai.com/docs/plugins/introduction) |
|Power Automate flow plugins     | Power Automate flows allow defining custom automations. These kinds of plugins are appropriate when a Maker wants to perform several actions which are not only about accessing data or generating content. [Learn more](/power-automate) |


## Create AI plugins

To create AI pluguins, go to Power Apps and choose AI plugin from the left-pane. And then, follow the guided walkthroughs as described in [Create AI plugins for Microsoft Copilot](/microsoft-copilot-studio/copilot-ai-plugins).

## Use AI plugins
AI plugins enable adding new behaviors to Copilots across products such as MCS/PVA and Microsoft Copilot. To learn about how to use AI plugins, see [Use plugin actions in Microsoft Copilot Studio](/power-virtual-agents/advanced-plugin-actions).

### See also

[Building  AI plugins for discovery by copilots](build-ai-plugin-for-copilot.md)
