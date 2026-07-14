---
title: Add knowledge to Copilot chat in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps to add knowledge
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 02/21/2025
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
---
# Add knowledge to Copilot chat in model-driven apps (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Extend your app’s Copilot chat intelligence by adding additional knowledge sources in Copilot Studio.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

## Add knowledge to Copilot chat

You can add additional knowledge sources in Copilot Studio. For example, you can add a link to an external public-facing website like Power Apps documentation by adding `https://learn.microsoft.com/power-apps/` as knowledge to enable your Copilot chat to respond to questions related to creating apps in Power Apps. Another example is to upload your organization’s internal knowledge as a document to enable Copilot chat to respond to relevant queries that aren't a part of the app data.

:::image type="content" source="media/mda-copilot-chat-add-knowledge.png" alt-text="Add Knowledge to Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-add-knowledge.png":::

More information: [Add knowledge to an existing agent – Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-existing-copilot). 

> [!NOTE]
>
> - Currently only [Public website](/microsoft-copilot-studio/knowledge-add-public-website), [File upload](/microsoft-copilot-studio/knowledge-add-file-upload) and [SharePoint](/microsoft-copilot-studio/nlu-generative-answers-sharepoint-onedrive) knowledge source types are supported. [Dataverse knowledge](/microsoft-copilot-studio/knowledge-add-dataverse) isn't part of this preview.
> - Copilot studio [Generative AI orchestration](/microsoft-copilot-studio/advanced-generative-actions) isn't supported currently. You can use classic orchestration topic whose trigger phrases match most closely with the user's query for a given skill.

Once knowledge is enabled, app users can ask relevant questions to get responses along with the knowledge references.

:::image type="content" source="media/mda-copilot-chat-knowledge-reference.png" alt-text="Knowledge reference in the Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-knowledge-reference.png":::


## Related articles

- [Customize Copilot chat using Copilot Studio (preview)](customize-copilot-chat.md)
- [Add topics to Copilot chat in model-driven apps (preview)](copilot-chat-mda-topics.md)
- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)