---
title: Add topics to Copilot chat in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps to add topics
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
# Add topics to Copilot chat in model-driven apps (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Extend your app’s Copilot chat intelligence by adding topics in Copilot Studio.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

## Add new topics to Copilot chat

 In Copilot Studio, you can add topics to your app’s Copilot agent. These topics can be customized to use various trigger types and can respond with simple messages, adaptive cards, or generative answers. Additionally, topics can also initiate actions like flows, connectors, and Dataverse plug-ins enabling seamless point in time integration with external systems.

:::image type="content" source="media/mda-copilot-chat-add-topic.png" alt-text="Add topic to Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-add-topic.png":::

More information: [Create and edit topics – Microsoft Copilot Studio](/microsoft-copilot-studio/authoring-create-edit-topics?tabs=webApp).

> [!NOTE]
> Copilot Studio has inline capability to "Test your agent" and can be used to validate topics as they're added. However, topics using out-of-the-box model-driven app custom variables like `Global.PA__Copilot_Model_PageContext.pageContext.id` can only be tested in the published Copilot.

## Related articles

- [Customize Copilot chat using Copilot Studio (preview)](customize-copilot-chat.md)
- [Add knowledge and topics to Copilot chat in model-driven apps (preview)](copilot-chat-mda-knowledge.md)
- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
