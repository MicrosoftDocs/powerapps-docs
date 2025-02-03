---
title: Customize Copilot chat in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 01/07/2025
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

You customize Copilot chat using [Microsoft Copilot Studio](/microsoft-copilot-studio/) and expand the capabilities to go beyond just handling [Microsoft Dataverse tables Q&A](/power-apps/user/use-copilot-model-driven-apps) and out-of-the-box skills. Before customizing, make sure [Copilot chat is enabled](/power-apps/maker/model-driven-apps/add-ai-copilot#enable-copilot-for-model-driven-apps-in-your-environment) for your environment.

> [!NOTE]
>
> - Copilot Studio license and agent editing permissions are required to customize Copilot chat.
> - This feature is only available in standalone model-driven apps and isn't yet supported for Dynamics 365 apps.

1. Go to https://make.preview.powerapps.com. 
1. Open your model-driven app in edit mode, and then on the left navigation bar select **...** > **Configure in Copilot Studio**. You're taken to Microsoft Copilot Studio where your app’s agent is set up. Every standalone model-driven app Copilot has its own dedicated agent available for customizations. Setting up the agent for the first time takes a few seconds.
   :::image type="content" source="media/mda-command-copilot-studio.png" alt-text="Open Copilot Studio to customize Copilot chat in model-driven app designer." lightbox="media/mda-command-copilot-studio.png":::
   > [!IMPORTANT]
   > - If **...** doesn't appear in the left navigation pane, the feature isn't available yet in your environment. You can provision a new [early release environments](/power-platform/admin/early-release) to access the feature. This is a preview feature and only available in early release environments.
1. Customize your agent by adding [knowledge sources](#add-knowledge-to-copilot-chat) or [topics](#add-new-topic-to-copilot-chat). Customizing this agent only impacts the Copilot chat of the specific app it's provisioned for.
   :::image type="content" source="media/mda-copilot-chat-copilot-studio.png" alt-text="Model-driven-app Copilot chat in Copilot Studio" lightbox="media/mda-copilot-chat-copilot-studio.png":::
1. **Publish** the agent after you make customizations to ensure changes are available to users.

## Add knowledge to Copilot chat

You can extend your app’s Copilot chat intelligence by adding additional knowledge sources in Copilot Studio. For example, you can add a link to an external public-facing website like Power Apps documentation by adding `https://learn.microsoft.com/power-apps/` as knowledge to enable your Copilot chat to respond to questions related to creating apps in Power Apps. Another example is to upload your organization’s internal knowledge as a document to enable Copilot chat to respond to relevant queries that aren't a part of the app data.

:::image type="content" source="media/mda-copilot-chat-add-knowledge.png" alt-text="Add Knowledge to Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-add-knowledge.png":::

More information: [Add knowledge to an existing agent – Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-existing-copilot). 

> [!NOTE]
>
> - Currently only [Public website](/microsoft-copilot-studio/knowledge-add-public-website), [File upload](/microsoft-copilot-studio/knowledge-add-file-upload) and [SharePoint](/microsoft-copilot-studio/nlu-generative-answers-sharepoint-onedrive) knowledge source types are supported. [Dataverse knowledge](/microsoft-copilot-studio/knowledge-add-dataverse) isn't part of this preview.
> - Copilot studio [Generative AI orchestration](/microsoft-copilot-studio/advanced-generative-actions) isn't supported currently. You can use classic orchestration topic whose trigger phrases match most closely with the user's query for a given skill.

Once knowledge is enabled, app users can ask relevant questions to get responses along with the knowledge references.

:::image type="content" source="media/mda-copilot-chat-knowledge-reference.png" alt-text="Knowledge reference in the Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-knowledge-reference.png":::

## Add new topic to Copilot chat

 In Copilot Studio, you can add topics to your app’s Copilot agent. These topics can be customized to use various trigger types and can respond with simple messages, adaptive cards, or generative answers. Additionally, topics can also initiate actions like flows, connectors, and Dataverse plug-ins enabling seamless point in time integration with external systems.

:::image type="content" source="media/mda-copilot-chat-add-topic.png" alt-text="Add topic to Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-add-topic.png":::

More information: [Create and edit topics – Microsoft Copilot Studio](/microsoft-copilot-studio/authoring-create-edit-topics?tabs=webApp).

> [!NOTE]
> Copilot Studio has inline capability to "Test your agent" and can be used to validate topics as they're added. However, topics using out-of-the-box model-driven app custom variables like `Global.PA__Copilot_Model_PageContext.pageContext.id` can only be tested in the published Copilot.

## Prompt guide customizations

A prompt library is a collection of prewritten, tested, and optimized prompts designed to help shape the interactions and responses of the Copilot chat. They ensure that the Copilot chat provides relevant, accurate, and contextually appropriate information based on the user’s needs and preferences.

:::image type="content" source="media/mda-copilot-chat-prompt-guide.png" alt-text="Prompt guide for Model-driven apps copilot" lightbox="media/mda-copilot-chat-prompt-guide.png":::

The following steps detail how to add specific queries to the prompt guide. A *Power Apps Help* section is appended to the existing out-of-the-box Copilot prompt guide. Alternatively, you can copy the sample code into a new topic directly from the [prompt guide sample](#prompt-guide-customizations-topic-sample). All the prompts shown to the end user via the prompt guide are stored in the Copilot Studio agent used for the app.

1. Open the agent backing the app in Copilot Studio and add a new blank topic.
   :::image type="content" source="media/mda-copilot-promptguide-addtopic.png" alt-text="Add blank topic" lightbox="media/mda-copilot-promptguide-addtopic.png":::
1. Rename the topic to reflect the topic intent and change the topic trigger to **Event received**.
   :::image type="content" source="media/mda-copilot-promptguide-eventreceived.png" alt-text="Event received for topic" lightbox="media/mda-copilot-promptguide-eventreceived.png":::
1. Select **Edit** under **Event received**, and then set the event name as `Microsoft.PowerApps.Copilot.RequestSparks`, which is the reserved name for prompt guide.
   :::image type="content" source="media/mda-copilot-promptguide-requestspark.png" alt-text="Spark request for topic" lightbox="media/mda-copilot-promptguide-requestspark.png":::
1. Optionally, you can set the conditions to prompt entries in case they're specific to the app name, page context, and so on. For example, this prompt entry checks if the current app's unique name or the page context's table type name matches specified values. If either condition is true, the Copilot chat is activated.

   `condition: =Global.PA_Copilot_Model_SessionContext.appUniqueName = "yourAppName" or Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName = "Entity name"`
1. Under **Priority**, add an appropriate priority value so the trigger is fired after the higher priority topics. Priority values can have 0 to 10K range with 0 being highest. 10 is used in this example.
1. Select **+** under **Event received**, and then select **Variable management** > **Parse value** to add a next step for variable management parse value.

   :::image type="content" source="media/mda-copilot-promptguide-variable.png" alt-text="Add variable" lightbox="media/mda-copilot-promptguide-variable.png":::
1. Paste the following Power Fx formula into the **Parse value** box, and then select **Insert**.

   ```powerappsfl
   [{displayName:"Power Apps Help",displaySubtitle:"Power Apps Help",iconName:"List24Regular",sparks:[{displayName:"What is Copilot chat?",type:"PromptText"},{displayName:"How can I use the record picker?",type:"PromptText"},{displayName:"What types of questions can I ask Copilot?",type:"PromptText"},{displayName:"How do I provide feedback on Copilot’s responses?",type:"PromptText"}]}]
   ```

   :::image type="content" source="media/mda-copilot-promptguide-parsevalue.png" alt-text="Parsing prompt guide entries" lightbox="media/mda-copilot-promptguide-parsevalue.png":::

1. Set the **Data type** as **Table**. The **Edit schema** link appears.
1. Select **Edit schema** and paste the following schema, and then select **Confirm**.

   ```yml
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
   ```

1. Set **Save as** to save as a new custom variable and name it something meaningful such as *SparkGroupCustom*.
   :::image type="content" source="media/mda-copilot-promptguide-customSparkGroup.png" alt-text="Custom spark group" lightbox="media/mda-copilot-promptguide-customSparkGroup.png":::

1. Select **+** under the **Parse value** step, and then select **Variable management** > **Set a variable value**.
1. The sparks definition is saved in a global variable so you need to set the variable **Global** and name it `PA_Copilot_Sparks.sparkGroups` and/or `Global.PA_Copilot_Sparks.sparks`. This populates the flyout with your prompts. Next, add a step to set variable value. <!-- Is this done somewhere in the Parse value step or do you create a new step to add this? Also, do you create a new variable or use an existing one? -->
   
   :::image type="content" source="media/mda-copilot-promptguide-setGlobalSparks.png" alt-text="Set global sparks" lightbox="media/mda-copilot-promptguide-setGlobalSparks.png":::

1. Search for the sparks definition name from the previous step, such as `Global.PA_Copilot_Sparks.sparkGroups`, and set the value to the following Power Fx merge function.

   ```powerappsfl
   ForAll(Sequence(CountRows(Global.PA_Copilot_Sparks.sparkGroups)+CountRows(Topic.SparkGroupCustom)), If(Value<=CountRows(Global.PA_Copilot_Sparks.sparkGroups),Index (Global.PA_Copilot_Sparks.sparkGroups,Value), Index(Topic.SparkGroupCustom, Value - CountRows(Global.PA_Copilot_Sparks.sparkGroups))))
   ```
   :::image type="content" source="media/mda-copilot-promptguide-mergeGlobalSparks.png" alt-text=" Merge global sparks" lightbox="media/mda-copilot-promptguide-mergeGlobalSparks.png":::Merge

   Replace the variable name with the variable name you used for the custom prompts, which in this example is *SparkGroupCustom*.

1. **Publish** the agent and play the app.

   :::image type="content" source="media/mda-copilot-promptguide-chat-screen.png" alt-text="Prompt guide using global sparks" lightbox="media/mda-copilot-promptguide-chat-screen.png":::

## Prompt guide customizations topic sample

Here is the full topic code, which can be copied directly into the new topic. <!--Where and instead of what? Where in the above procedure would you use this? -->

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

## Known Limitations

- Copilot chat agents currently aren’t identified by the platform as a dependency. You must manually add the relevant Copilot chat agent to your model-driven app solution before export and import to another environment.
- **Configure in Copilot Studio** action can create agents with the same display name for apps that have the same initial characters in the app name. When this occurs, rename the agent while publishing to avoid confusion.
- The [Image](/microsoft-copilot-studio/authoring-send-message#add-an-image) and [Video](/microsoft-copilot-studio/authoring-send-message#add-an-image) message types from agent to user aren't supported. As a workaround, you can use Adaptive Cards.

## Related information

- [Add Copilot chat to model-driven apps](../model-driven-apps/add-ai-copilot.md)
- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
