---
title: Customize Copilot chat in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 02/21/2025
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
# Customize Copilot chat using Copilot Studio (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Customize Copilot chat to make it even more intelligent and relevant for your organization by adding additional topics, knowledge sources, and more.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

You customize Copilot chat using [Microsoft Copilot Studio](/microsoft-copilot-studio/) and expand the capabilities to go beyond just handling [Microsoft Dataverse tables questions](/power-apps/user/use-copilot-model-driven-apps) and out-of-the-box skills. Before customizing, make sure [Copilot chat is enabled](/power-apps/maker/model-driven-apps/add-ai-copilot#enable-copilot-for-model-driven-apps-in-your-environment) for your environment.

> [!NOTE]
>
> - Copilot Studio license and agent editing permissions are required to customize Copilot chat.
> - This feature is only available in standalone model-driven apps and [Copilot in Dynamics 365 Sales](/dynamics365/sales/extend-copilot-chat). This feature isn't yet supported for other Dynamics 365 apps.

1. Go to https://make.preview.powerapps.com. 
1. Open your model-driven app in edit mode, and then on the left navigation bar select **...** > **Configure in Copilot Studio**. You're taken to Microsoft Copilot Studio where your app’s agent is set up. Every standalone model-driven app Copilot has its own dedicated agent available for customizations. Setting up the agent for the first time takes a few seconds.
   :::image type="content" source="media/mda-command-copilot-studio.png" alt-text="Open Copilot Studio to customize Copilot chat in model-driven app designer." lightbox="media/mda-command-copilot-studio.png":::
   > [!IMPORTANT]
   > - If **...** doesn't appear in the left navigation pane, the feature isn't available yet in your environment. You can provision a new [early release environments](/power-platform/admin/early-release) to access the feature. This is a preview feature and only available in early release environments.
1. Customize your agent by adding [knowledge sources](copilot-chat-mda-knowledge-topics.md#add-knowledge-to-copilot-chat) or [topics](copilot-chat-mda-knowledge-topics.md#add-new-topic-to-copilot-chat). Customizing this agent only impacts the Copilot chat of the specific app it's provisioned for.
   :::image type="content" source="media/mda-copilot-chat-copilot-studio.png" alt-text="Model-driven-app Copilot chat in Copilot Studio" lightbox="media/mda-copilot-chat-copilot-studio.png":::
1. **Publish** the agent after you make customizations to ensure changes are available to users.

## Prompt guide customizations topic sample

Here is the full topic code, which can be copied directly into the new topic.

```yml
kind: AdaptiveDialog
beginDialog:
  kind: OnEventActivity
  id: main
  priority: 200
  eventName: Microsoft.PowerApps.Copilot.RequestSparks
  actions:
    - kind: ParseValue
      id: iCepPf
      variable: Topic.SparkGroupCustom
      valueType:
        kind: Table
        properties:
          displayName: String
          displaySubtitle: String
          iconName: String
          sparks:
            type:
              kind: Table
              properties:
                displayName: String
                eventName: String
                iconName: String
                payload: String
                type: String
      value: |-
        =[{displayName:"Power Apps Help",displaySubtitle:"Power Apps Help",iconName:"List24Regular",
        sparks:[
        {displayName:"What is Copilot chat?",type:"PromptText"},
        {displayName:"How can I use the record picker?",type:"PromptText"},
        {displayName:"What types of questions can I ask Copilot?",type:"PromptText"},
        {displayName:"How do I provide feedback on Copilot’s responses?",type:"PromptText"}
        ]}]

    - kind: SetVariable
      id: setVariable_pDu9cr
      variable: Global.PA_Copilot_Sparks.sparkGroups
      value: =ForAll(Sequence(CountRows(Global.PA_Copilot_Sparks.sparkGroups)+CountRows(Topic.SparkGroupCustom)), If(Value<=CountRows(Global.PA_Copilot_Sparks.sparkGroups),Index (Global.PA_Copilot_Sparks.sparkGroups,Value), Index(Topic.SparkGroupCustom, Value - CountRows(Global.PA_Copilot_Sparks.sparkGroups))))
```

> [!NOTE]
> If your agent supports multiple languages and needs prompt guide translation, all your user facing question strings must be set using a `SetTextVariable`.

## Known limitations

- Copilot chat agents currently aren’t identified by the platform as a dependency. You must manually add the relevant Copilot chat agent to your model-driven app solution before export and import to another environment.
- **Configure in Copilot Studio** action can create agents with the same display name for apps that have the same initial characters in the app name. When this occurs, rename the agent while publishing to avoid confusion.
- The [Image](/microsoft-copilot-studio/authoring-send-message#add-an-image) and [Video](/microsoft-copilot-studio/authoring-send-message#add-an-image) message types from agent to user aren't supported. As a workaround, you can use Adaptive Cards.

## Related information

- [Add Copilot chat to model-driven apps](../model-driven-apps/add-ai-copilot.md)
- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
