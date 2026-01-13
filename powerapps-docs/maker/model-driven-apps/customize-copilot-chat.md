---
title: Customize Copilot chat in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 01/09/2026
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
  - Jacob-Wilkinson
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
---
# Customize Copilot chat using Copilot Studio (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Customize Copilot chat to make it even more intelligent and relevant for your organization by adding additional articles, knowledge sources, and more.

> [!IMPORTANT]
>
> This feature is generally available in Dynamics 365 apps, but remains a preview feature in Power Apps.
>
> - Preview features aren't meant for production use and might have restricted functionality These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - You must allow data movement across regions for Generative AI features as a prerequisite for using Copilot in Power Apps. This step is especially important if your organization and your environment are in different regions. Learn more in [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability might be subject to usage limits or capacity throttling.
> [!NOTE]
>
> Copilot chat in Power Apps is a preview feature that will be deprecated for model-driven apps in environments not [enabled for Dynamics 365 apps](/power-platform/admin/create-environment#create-an-environment-with-a-database), starting January 2026. We recommend switching to [Microsoft 365 Copilot chat](../../user/use-microsoft-365-copilot-model-driven-apps.md). During the transition period, makers can enable either one or both chat experiences. For more information, see [Deprecation of Copilot chat in model-driven apps](/power-platform/important-changes-coming#deprecation-of-copilot-chat-in-model-driven-apps)




You customize Copilot chat using [Microsoft Copilot Studio](/microsoft-copilot-studio/) and expand the capabilities to go beyond just handling [Microsoft Dataverse tables questions](../../user/use-copilot-model-driven-apps.md) and out-of-the-box skills. Before customizing, make sure [Copilot chat is enabled](add-ai-copilot.md#enable-copilot-for-model-driven-apps-in-your-environment) for your environment.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=d0439343-f464-4ec7-a92d-b3c528430fb5]



> [!NOTE]
>
> - Copilot Studio license and agent editing permissions are required to customize Copilot chat.
> - This feature is only available in standalone model-driven apps, which don't include both lead and opportunity tables. This feature isn't yet supported for Dynamics 365 apps.
> - This experience has changed to use [interactive agent](add-agents-to-app.md) and is currently rolling out to regions.

1. Go to https://make.preview.powerapps.com. 
1. Open your model-driven app in edit mode, and then on the left navigation bar select **...** > **Configure in Copilot Studio**. You're taken to Microsoft Copilot Studio where your app’s agent is set up. Every standalone model-driven app Copilot has its own dedicated agent available for customizations. Setting up the agent for the first time takes a few seconds.
   :::image type="content" source="media/mda-command-copilot-studio.png" alt-text="Open Copilot Studio to customize Copilot chat in model-driven app designer." lightbox="media/mda-command-copilot-studio.png":::
1. Customize your agent by adding [knowledge sources](copilot-chat-mda-knowledge.md) or [topics](copilot-chat-mda-topics.md). Customizing this agent only impacts the Copilot chat of the specific app it's provisioned for.
   :::image type="content" source="media/mda-copilot-chat-copilot-studio.png" alt-text="Model-driven-app Copilot chat in Copilot Studio" lightbox="media/mda-copilot-chat-copilot-studio.png":::
1. **Publish** the agent after you make customizations to ensure changes are available to users.

Power Apps creates a platform-owned agent named **Copilot in Power Apps** in each environment. This agent is only editable by a Power Platform environment admin and isn’t published to any channels by default. Although this agent can be viewed in Microsoft Copilot Studio, this agent shouldn't be edited since it isn't used by model-driven apps.

## Related information

- [Add Copilot chat to model-driven apps](../model-driven-apps/add-ai-copilot.md)
- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
