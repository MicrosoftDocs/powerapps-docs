---
title: Zero prompt experience for Copilot chat in model-driven apps
description: Learn how to customize Zero Prompt experience for model-driven apps to add topics with Power Apps and Microsoft Copilot Studio
author: HemantGaur
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 03/06/2025
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
# Zero prompt experience (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The zero prompt experience helps makers enhance user engagement and streamline interactions at the start of a Copilot chat session. By presenting a zero prompt experience adaptive card at the beginning of a chat session, users receive relevant information and options right away, reducing the need for additional prompts and iterations. The zero prompt experience can be context aware and hence, can be selectively shown for targeted pages.

:::image type="content" source="media/mda-copilot-zpe-sample-topic.png" alt-text="Zero prompt experience for model-driven apps Copilot chat" lightbox="media/mda-copilot-ZPE-sample-topic.png":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

## Customize the zero prompt experience

These steps detail how to customize the zero prompt experience.

1. Open the agent backing the app in Copilot Studio and add a new blank topic.
   :::image type="content" source="media/mda-copilot-zpe-addTopic.png" alt-text="Add blank topic" lightbox="media/mda-copilot-zpe-addTopic.png":::
1. Rename the topic to reflect the topic intent and change the topic trigger to **Event received**.
   :::image type="content" source="media/mda-copilot-zpe-event-received.png" alt-text="Event received for topic" lightbox="media/mda-copilot-zpe-event-received.png":::
1. Select **Edit** under **Event received**, and then set the event name as `Microsoft.PowerApps.Copilot.RequestZeroPrompt`, which is the reserved name for the zero prompt experience. Set priority to higher than 99 but lower than 100000. The priority is important because custom zero prompt experiences need to override the default platform provided ones.
   :::image type="content" source="media/mda-copilot-zpe-request-zero-prompt-event.png" alt-text="Zero prompt experience event" lightbox="media/mda-copilot-zpe-request-zero-prompt-event.png":::
1. Optionally, you can also set the conditions to the zero prompt experience in case it's specific to the page context. For example, this entry checks if the page context's table type name matches account. If the condition is true, the custom zero prompt experience is shown.
   `condition:Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName = "account"`
After this step, you can build your zero prompt messages using adaptive cards. For more information regarding building adaptive cards go to this information: https://adaptivecards.microsoft.com/. Once you have zero prompt experience cards, you can set the global variable `Global.PA_Copilot_ZeroPrompt` to your adaptive card definition.
1. The zero prompt includes all the flexibility of adaptive cards and you can trigger different skills from within it. When an adaptive card contains a button or anything that requires an `Action.Submit`, you have a few options you can use to handle that event. These event handlers are called `SkillTypes`. `Action.Submit` types should include the following properties: a data object with `SkillType` and scenario properties. You can use `MCSMessageSkill`, which are directly sent to Copilot Studio as user messages, or `PromptTextSkill` when you want to populate the **Chat Input** box. `PromptTextSkill` is useful when you want additional input from the user, such as specifying a record or table name among other things. For example:
   `How many [table name] are active?`
   `What are the [table name] assigned to me?`

1. When you trigger zero prompts, your select an action structure that should look like the action structure here. The scenario value should be `ZeroPromptCard` along with the source value as `ZeroPrompt`. Lastly, the value corresponds to the actual prompt.

```yml
   selectAction: {
   type: "Action.Submit",
   data: {
   	scenario: "ZeroPromptCard",
   	skillType: "MCSMessageSkill",
   	value:  "What are accounts in Redmond?",
   	source: "ZeroPrompt"
   }
},
```

## Zero prompt experience topic sample

Here is the full topic code, which can be copied directly into the new topic. You can edit the zero prompt experience questions in the options shown here and reuse the predefined cards.

```yml
kind: AdaptiveDialog
beginDialog:
  kind: OnEventActivity
  id: main
  condition: =Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName = "account"
  priority: 100
  eventName: Microsoft.PowerApps.Copilot.RequestZeroPrompt
  actions:
    - kind: SetVariable
      id: setVariable_acI6It
      variable: Topic.WelcomeMessage
      value: Welcome to the Zero Prompt Experience

    - kind: SetTextVariable
      id: setTextVariable_g4rSG0
      variable: Topic.FooterMessage
      value: This is custom ZPE footer message

    - kind: SetVariable
      id: setVariable_QUoZ5c
      variable: Topic.OverviewIcon
      value: "=\"data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0zLjUgNEMyLjY3MTU3IDQgMiA0LjY3MTU3IDIgNS41VjcuNUMyIDguMzI4NDMgMi42NzE1NyA5IDMuNSA5SDUuNUM2LjMyODQzIDkgNyA4LjMyODQzIDcgNy41VjUuNUM3IDQuNjcxNTcgNi4zMjg0MyA0IDUuNSA0SDMuNVpNMyA1LjVDMyA1LjIyMzg2IDMuMjIzODYgNSAzLjUgNUg1LjVDNS43NzYxNCA1IDYgNS4yMjM4NiA2IDUuNVY3LjVDNiA3Ljc3NjE0IDUuNzc2MTQgOCA1LjUgOEgzLjVDMy4yMjM4NiA4IDMgNy43NzYxNCAzIDcuNVY1LjVaTTkuNSA1QzkuMjIzODYgNSA5IDUuMjIzODYgOSA1LjVDOSA1Ljc3NjE0IDkuMjIzODYgNiA5LjUgNkgxNy41QzE3Ljc3NjEgNiAxOCA1Ljc3NjE0IDE4IDUuNUMxOCA1LjIyMzg2IDE3Ljc3NjEgNSAxNy41IDVIOS41Wk05LjUgN0M5LjIyMzg2IDcgOSA3LjIyMzg2IDkgNy41QzkgNy43NzYxNCA5LjIyMzg2IDggOS41IDhIMTUuNUMxNS43NzYxIDggMTYgNy43NzYxNCAxNiA3LjVDMTYgNy4yMjM4NiAxNS43NzYxIDcgMTUuNSA3SDkuNVpNMy41IDExQzIuNjcxNTcgMTEgMiAxMS42NzE2IDIgMTIuNVYxNC41QzIgMTUuMzI4NCAyLjY3MTU3IDE2IDMuNSAxNkg1LjVDNi4zMjg0MyAxNiA3IDE1LjMyODQgNyAxNC41VjEyLjVDNyAxMS42NzE2IDYuMzI4NDMgMTEgNS41IDExSDMuNVpNMyAxMi41QzMgMTIuMjIzOSAzLjIyMzg2IDEyIDMuNSAxMkg1LjVDNS43NzYxNCAxMiA2IDEyLjIyMzkgNiAxMi41VjE0LjVDNiAxNC43NzYxIDUuNzc2MTQgMTUgNS41IDE1SDMuNUMzLjIyMzg2IDE1IDMgMTQuNzc2MSAzIDE0LjVWMTIuNVpNOS41IDEyQzkuMjIzODYgMTIgOSAxMi4yMjM5IDkgMTIuNUM5IDEyLjc3NjEgOS4yMjM4NiAxMyA5LjUgMTNIMTcuNUMxNy43NzYxIDEzIDE4IDEyLjc3NjEgMTggMTIuNUMxOCAxMi4yMjM5IDE3Ljc3NjEgMTIgMTcuNSAxMkg5LjVaTTkuNSAxNEM5LjIyMzg2IDE0IDkgMTQuMjIzOSA5IDE0LjVDOSAxNC43NzYxIDkuMjIzODYgMTUgOS41IDE1SDE1LjVDMTUuNzc2MSAxNSAxNiAxNC43NzYxIDE2IDE0LjVDMTYgMTQuMjIzOSAxNS43NzYxIDE0IDE1LjUgMTRIOS41WiIgZmlsbD0iIzcwNzA3MCIvPg0KPC9zdmc+\""

    - kind: SetVariable
      id: setVariable_zeAjbE
      variable: Topic.ClockIcon
      value: "=\"data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0xMCA2LjUwMDEyQzEwIDYuMjIzOTggOS43NzYxNCA2LjAwMDEyIDkuNSA2LjAwMDEyQzkuMjIzODYgNi4wMDAxMiA5IDYuMjIzOTggOSA2LjUwMDEyVjEwLjUwMDFDOSAxMC43NzYzIDkuMjIzODYgMTEuMDAwMSA5LjUgMTEuMDAwMUgxMi41QzEyLjc3NjEgMTEuMDAwMSAxMyAxMC43NzYzIDEzIDEwLjUwMDFDMTMgMTAuMjI0IDEyLjc3NjEgMTAuMDAwMSAxMi41IDEwLjAwMDFIMTBWNi41MDAxMlpNMy4zNTI3MSA3Ljc5OTk4QzIuNTM0ODEgNy4yMjM4MSAyIDYuMjY3ODIgMiA1LjE4NzA1QzIgMy40MzA2NyAzLjQxMzUzIDIgNS4xNjU2MiAyQzYuMjQyNzQgMiA3LjE5MjE4IDIuNTQxNTEgNy43NjMxNCAzLjM2NTAxQzguNDY1NTMgMy4xMjgzIDkuMjE3NzggMyAxMCAzQzEwLjc3OTQgMyAxMS41MjkgMy4xMjczNyAxMi4yMjkyIDMuMzYyNDNDMTIuODAxIDIuNTM5OTcgMTMuNzUyNiAyIDE0LjgzMTEgMkMxNi41ODIzIDIgMTcuOTk5OSAzLjQyMjY4IDE3Ljk5OTkgNS4xNzUxNkMxNy45OTk5IDYuMjU0NzIgMTcuNDYyIDcuMjA4MjkgMTYuNjQxMiA3Ljc4MTU5QzE2Ljg3MzkgOC40Nzg3IDE3IDkuMjI0NjMgMTcgMTBDMTcgMTEuNzUzIDE2LjM1NTYgMTMuMzU1NSAxNS4yOTA4IDE0LjU4MzZMMTYuODUzNiAxNi4xNDYzQzE3LjA0ODggMTYuMzQxNiAxNy4wNDg4IDE2LjY1ODIgMTYuODUzNiAxNi44NTM0QzE2LjY1ODMgMTcuMDQ4NyAxNi4zNDE3IDE3LjA0ODcgMTYuMTQ2NCAxNi44NTM0TDE0LjU4MzcgMTUuMjkwN0MxMy4zNTU2IDE2LjM1NTYgMTEuNzUzMSAxNyAxMCAxN0M4LjI0Njk2IDE3IDYuNjQ0NDQgMTYuMzU1NiA1LjQxNjM4IDE1LjI5MDdMMy44NTM1NiAxNi44NTM2QzMuNjU4MyAxNy4wNDg5IDMuMzQxNzIgMTcuMDQ4OSAzLjE0NjQ1IDE2Ljg1MzZDMi45NTExOSAxNi42NTg0IDIuOTUxMTggMTYuMzQxOCAzLjE0NjQ0IDE2LjE0NjVMNC43MDkyNyAxNC41ODM2QzMuNjQ0NDEgMTMuMzU1NiAzIDExLjc1MyAzIDEwQzMgOS4yMzE0NCAzLjEyMzg2IDguNDkxODEgMy4zNTI3MSA3Ljc5OTk4Wk0zIDUuMTg3MDVDMyA1Ljg0OTE1IDMuMjkwOTggNi40NDE4NiAzLjc1MDcxIDYuODQyODZDNC40MTk0NiA1LjUyMTc0IDUuNDk0ODMgNC40NDEzNiA2LjgxMjIyIDMuNzY2MzJDNi40MTQwOSAzLjI5NjExIDUuODIzMjYgMyA1LjE2NTYyIDNDMy45NzMzNSAzIDMgMy45NzUzOSAzIDUuMTg3MDVaTTE2LjI0MTYgNi44Mjc2NEMxNi43MDYyIDYuNDI4NDEgMTYuOTk5OSA1LjgzNjE2IDE2Ljk5OTkgNS4xNzUxNkMxNi45OTk5IDMuOTcyNzMgMTYuMDI3OCAzIDE0LjgzMTEgM0MxNC4xNzE0IDMgMTMuNTc5NyAzLjI5NTMgMTMuMTgxMyAzLjc2MzAyQzE0LjQ5NjYgNC40MzUyNCAxNS41NzEyIDUuNTExMjggMTYuMjQxNiA2LjgyNzY0Wk00IDEwQzQgMTMuMzEzNyA2LjY4NjI5IDE2IDEwIDE2QzEzLjMxMzcgMTYgMTYgMTMuMzEzNyAxNiAxMEMxNiA2LjY4NjI5IDEzLjMxMzcgNCAxMCA0QzYuNjg2MjkgNCA0IDYuNjg2MjkgNCAxMFoiIGZpbGw9IiM3MDcwNzAiLz4NCjwvc3ZnPg==\""

    - kind: SetVariable
      id: setVariable_i1e9qL
      variable: Topic.ExclamationIcon
      value: "=\"data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0xMCAyQzE0LjQxODMgMiAxOCA1LjU4MTcyIDE4IDEwQzE4IDE0LjQxODMgMTQuNDE4MyAxOCAxMCAxOEM1LjU4MTcyIDE4IDIgMTQuNDE4MyAyIDEwQzIgNS41ODE3MiA1LjU4MTcyIDIgMTAgMlpNMTAgM0M2LjEzNDAxIDMgMyA2LjEzNDAxIDMgMTBDMyAxMy44NjYgNi4xMzQwMSAxNyAxMCAxN0MxMy44NjYgMTcgMTcgMTMuODY2IDE3IDEwQzE3IDYuMTM0MDEgMTMuODY2IDMgMTAgM1pNMTAgMTIuNUMxMC40MTQyIDEyLjUgMTAuNzUgMTIuODM1OCAxMC43NSAxMy4yNUMxMC43NSAxMy42NjQyIDEwLjQxNDIgMTQgMTAgMTRDOS41ODU3OSAxNCA5LjI1IDEzLjY2NDIgOS4yNSAxMy4yNUM5LjI1IDEyLjgzNTggOS41ODU3OSAxMi41IDEwIDEyLjVaTTEwIDZDMTAuMjQ1NSA2IDEwLjQ0OTYgNi4xNzY4OCAxMC40OTE5IDYuNDEwMTJMMTAuNSA2LjVWMTFDMTAuNSAxMS4yNzYxIDEwLjI3NjEgMTEuNSAxMCAxMS41QzkuNzU0NTQgMTEuNSA5LjU1MDM5IDExLjMyMzEgOS41MDgwNiAxMS4wODk5TDkuNSAxMVY2LjVDOS41IDYuMjIzODYgOS43MjM4NiA2IDEwIDZaIiBmaWxsPSIjNzA3MDcwIi8+DQo8L3N2Zz4=\""

    - kind: SetVariable
      id: setVariable_x6BNry
      variable: Topic.OptionOne
      value: "={skillType: \"PromptTextSkill\", optionGroup: \"Redmond Accounts!\", prompt: \"What are the accounts located in Redmond?\" }"

    - kind: SetVariable
      id: setVariable_4jjXcz
      variable: Topic.OptionTwo
      value: "={skillType: \"MCSMessageSkill\", optionGroup: \"Missing Phone Numbers\", prompt: \"Which accounts have missing phone numbers?\" }"

    - kind: SetVariable
      id: setVariable_DzjFpB
      variable: Topic.OptionThree
      value: "={skillType: \"MCSMessageSkill\", optionGroup: \"Active Accounts\", prompt: \"How many active accounts are there?\" }"

    - kind: SetVariable
      id: setVariable_q8Ne5M
      variable: Global.PA_Copilot_ZeroPrompt
      value: |-
        ={
                          type: "AdaptiveCard",
                          body: [
                              {
                                type: "ColumnSet",
                                id: "ms-platform-zpe-columnsetheader-dc291457-0726-4472-9264-ab644fe9b13e",
                                columns: [
                                    {
                                        type: "Column",
                                        items: [
                                        {
                                            type: "TextBlock",
                                            wrap: true,
                                            text: "Hi "&System.User.FirstName&","
                                        },
                                        {
                                            type: "TextBlock",
                                            wrap: true,
                                            text: ""&Topic.WelcomeMessage&"",
                                            id: "ms-platform-zpe-header-74453ffe-b4e3-4c81-9a6c-5c03dc4a3661",
                                            spacing: "Medium"
                                        },
                                        ]
                                    }
                                ]
                              },
                              {
                                  type: "Container",
                                  id: "ms-platform-zpe-actionscontainer-d44c003a-b977-4e0b-a3fc-f8d30d60110b",
                                  isVisible: ""&!IsBlank(Topic.OptionOne.prompt)&"",
                                  showBorder: true,
                                  roundedCorners: true,
                                  selectAction: {
                                      type: "Action.Submit",
                                      data: {
                                          scenario: "ZeroPromptCard",
                                          skillType: Topic.OptionOne.skillType,
                                          value:  ""&Topic.OptionOne.prompt&"",
                                          source: "ZeroPrompt"
                                      }
                                  },
                                  items: [
                                      {
                                          type: "ColumnSet",
                                          columns: [
                                              {
                                                  type: "Column",
                                                  width: "auto",
                                                  items: [
                                                      {
                                                          type: "Image",
                                                          url: ""&Topic.ExclamationIcon&"",
                                                          altText: ""&Topic.OptionOne.optionGroup&""
                                                      }
                                                  ]
                                              },
                                              {
                                                  type: "Column",
                                                  width: "stretch",
                                                  items: [
                                                      {
                                                          type: "TextBlock",
                                                          text: ""&Topic.OptionOne.optionGroup&"",
                                                          weight: "bolder"
                                                      },
                                                      {
                                                          type: "TextBlock",
                                                          text: ""&Topic.OptionOne.prompt&""
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  ]
                              },
                              {
                                  type: "Container",
                                  id: "ms-platform-zpe-actionscontainer-477da7ce-bd52-4870-a8c2-04071daa56e2",
                                  isVisible: ""&!IsBlank(Topic.OptionTwo.prompt)&"",
                                  showBorder: true,
                                  roundedCorners: true,
                                  selectAction: {
                                      type: "Action.Submit",
                                      data: {
                                          scenario: "ZeroPromptCard",
                                          skillType: Topic.OptionTwo.skillType,
                                          value: ""&Topic.OptionTwo.prompt&"",
                                          source: "ZeroPrompt"
                                      }
                                  },
                                  items: [
                                      {
                                          type: "ColumnSet",
                                          columns: [
                                              {
                                                  type: "Column",
                                                  width: "auto",
                                                  items: [
                                                      {
                                                          type: "Image",
                                                          url:  ""&Topic.ClockIcon&"",
                                                          altText: ""&Topic.OptionTwo.optionGroup&""
                                                      }
                                                  ]
                                              },
                                              {
                                                  type: "Column",
                                                  width: "stretch",
                                                  items: [
                                                      {
                                                          type: "TextBlock",
                                                          text: ""&Topic.OptionTwo.optionGroup&"",
                                                          weight: "bolder"
                                                      },
                                                      {
                                                          type: "TextBlock",
                                                          text: ""&Topic.OptionTwo.prompt&""
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  ]
                              },
                              {
                                  type: "Container",
                                  id: "ms-platform-zpe-actionscontainer-ff8b54c0-ba5a-435f-a66f-3978115ef39a",
                                  isVisible: ""&!IsBlank(Topic.OptionThree.prompt)&"",
                                  showBorder: true,
                                  roundedCorners: true,
                                  selectAction: {
                                      type: "Action.Submit",
                                      data: {
                                          scenario: "ZeroPromptCard",
                                          skillType: Topic.OptionThree.skillType,
                                          value: ""&Topic.OptionThree.prompt&"",
                                          source: "ZeroPrompt"
                                      }
                                  },
                                  items: [
                                      {
                                          type: "ColumnSet",
                                          columns: [
                                              {
                                                  type: "Column",
                                                  width: "auto",
                                                  items: [
                                                      {
                                                          type: "Image",
                                                          url:  ""&Topic.OverviewIcon&"",
                                                          altText: ""&Topic.OptionThree.optionGroup&""
                                                      }
                                                  ]
                                              },
                                              {
                                                  type: "Column",
                                                  width: "stretch",
                                                  items: [
                                                      {
                                                          type: "TextBlock",
                                                          text: ""&Topic.OptionThree.optionGroup&"",
                                                          weight: "bolder"
                                                      },
                                                      {
                                                          type: "TextBlock",
                                                          text: ""&Topic.OptionThree.prompt&""
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  ]
                              },
                              {
                                  type: "Container",
                                  id: "ms-platform-zpe-collapsed-footer-79fb882f-ec4e-4abd-bc65-8c523849da40",
                                  items: [
                                      {
                                          type: "ColumnSet",
                                          columns: [
                                              {
                                                  type: "Column",
                                                  width: "auto",
                                                  items: [
                                                      {
                                                          type: "TextBlock",
                                                          wrap: true,
                                                          text: ""&Topic.FooterMessage&"",
                                                          id: "fsFooterId"
                                                      },
                                                  ]
                                              }
                                          ]
                                      },
                                  ]
                              },
                          ],
                          '$schema': "http://adaptivecards.io/schemas/adaptive-card.json",
                          version: "1.5"
                      }
```

## Related articles

- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
















