---
title: Prompt guide customizations to Copilot chat in model-driven apps
description: Learn how to customize Copilot chat using prompts in model-driven apps to add topics
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 03/07/2025
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
# Prompt guide customizations (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

A prompt library is a collection of prewritten, tested, and optimized prompts designed to help shape the interactions and responses of the Copilot chat. They ensure that the Copilot chat provides relevant, accurate, and contextually appropriate information based on the user’s needs and preferences.

:::image type="content" source="media/mda-copilot-chat-prompt-guide.png" alt-text="Prompt guide for Model-driven apps copilot" lightbox="media/mda-copilot-chat-prompt-guide.png":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

The following steps detail how to add specific queries to the prompt guide. A *Power Apps Help* section is appended to the existing out-of-the-box Copilot prompt guide. Alternatively, you can copy the sample code into a new topic directly from the [Prompt guide customizations topic sample](#prompt-guide-customizations-topic-sample). All the prompts shown to the end user via the prompt guide are stored in the Copilot Studio agent used for the app.

1. Open the agent backing the app in Copilot Studio and add a new blank topic.
   :::image type="content" source="media/mda-copilot-promptguide-addtopic.png" alt-text="Add blank topic" lightbox="media/mda-copilot-promptguide-addtopic.png":::
1. Rename the topic to reflect the topic intent and change the topic trigger to **Event received**.
   :::image type="content" source="media/mda-copilot-promptguide-eventreceived.png" alt-text="Event received for topic" lightbox="media/mda-copilot-promptguide-eventreceived.png":::
1. Select **Edit** under **Event received**, and then set the event name as `Microsoft.PowerApps.Copilot.RequestSparks`, which is the reserved name for prompt guide.
   :::image type="content" source="media/mda-copilot-promptguide-requestspark.png" alt-text="Spark request for topic" lightbox="media/mda-copilot-promptguide-requestspark.png":::
1. Optionally, you can set the conditions to prompt entries in case they're specific to the page context. For example, this prompt entry checks if the page context's table type name matches the specified value. If the condition is true, the custom prompts are shown to the user.

   `condition:Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName = "Entity name"`
1. Under **Priority**, add an appropriate priority value so the trigger is fired after the higher priority topics. Priority values can have 0 to 10K range with 0 being highest. Although about 200 is recommended as it allows for more options to add higher priority topics later, 10 is used in this example.
1. Select **+** under **Event received**, and then select **Variable management** > **Parse value** to add a next step for variable management parse value.

   :::image type="content" source="media/mda-copilot-promptguide-variable.png" alt-text="Add variable" lightbox="media/mda-copilot-promptguide-variable.png":::
1. Paste the following Power Fx formula into the **Parse value** box, and then select **Insert**.

   ```powerappsfl
   [{displayName:"Power Apps Help",displaySubtitle:"Power Apps Help",iconName:"List24Regular",sparks:[{displayName:"What is Copilot chat?",type:"MCSMessageSkill"},{displayName:"How can I use the record picker?",type:"PromptTextSkill"},{displayName:"What types of questions can I ask Copilot?",type:"PromptTextSkill"},{displayName:"How do I provide feedback on Copilot’s responses?",type:"PromptTextSkill"}]}]
   ```
For the sparks type you can either use `MCSMessageSkill`, which are directly sent to Copilot Studio as user messages or `PromptTextSkill` when you want to populate the **Chat Input** box. `PromptTextSkill` is useful when you want additional input from the user, such as specifying a record or table name among other things. For example:
   `How many **[table name]** are active?`
   `What are the **[table name]** assigned to me?`
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
1. The sparks definition is saved in a global variable so you need to set the variable **Global** and name it `PA_Copilot_Sparks.sparkGroups` and/or `Global.PA_Copilot_Sparks.sparks`. This populates the flyout with your prompts. Next, add a step to set variable value.

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
        {displayName:"What is Copilot chat?",type:"MCSMessageSkill"},
        {displayName:"How can I use the record picker?",type:"MCSMessageSkill"},
        {displayName:"What types of questions can I ask Copilot?",type:"PromptTextSkill"},
        {displayName:"How do I provide feedback on Copilot’s responses?",type:"PromptTextSkill"}
        ]}]

    - kind: SetVariable
      id: setVariable_pDu9cr
      variable: Global.PA_Copilot_Sparks.sparkGroups
      value: =ForAll(Sequence(CountRows(Global.PA_Copilot_Sparks.sparkGroups)+CountRows(Topic.SparkGroupCustom)), If(Value<=CountRows(Global.PA_Copilot_Sparks.sparkGroups),Index (Global.PA_Copilot_Sparks.sparkGroups,Value), Index(Topic.SparkGroupCustom, Value - CountRows(Global.PA_Copilot_Sparks.sparkGroups))))
```

> [!NOTE]
> If your agent supports multiple languages and needs prompt guide translation, all your user facing question strings must be set using a `SetTextVariable`.

- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
