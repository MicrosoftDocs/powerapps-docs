---
title: Enable users to discuss ideas
description: Explains how to extend the Employee Ideas sample app for Microsoft Teams to take users to a discussion about an idea in Teams.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/25/2021
ms.subservice: teams
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
  - sbahl10
---

# Enable users to discuss ideas

The Employee Ideas sample app for Microsoft Teams makes it easy to capture ideas and suggestions from your colleagues and have colleagues vote for their favorite ideas. But you might want to make this more interactive by facilitating discussions around ideas.

Currently the Employee Ideas app posts messages to a teams channel when an Idea is submitted. In this article, we'll extend the app to provide a mechanism for users to go to the idea channel message so the can interact and discuss the idea with other users.

## Prerequisites

- Install the Employee Ideas app in a team from <https://aka.ms/TeamsEmployeeIdeas>.

- Enable posting of Teams channel messages in the app settings.

- Add the Power Apps app in Teams by selecting the ellipses (…) and searching  for **Power Apps**.

- Right-click on the Power Apps app, and select **Pop out app** to launch Power Apps in a new window.

## Add the message ID column

The Employee Ideas sample app posts messages to teams channels when an app or a campaign are created. However, it currently doesn't store any record of that message. Since we want the app to give users the ability to comment, and discuss the idea using the posted message thread, we'll update the app to preserve the ID of the message.

1. Open the Ideas app using Power Apps in Microsoft Teams.

1. Go to the **Build** tab.

1. Select the data panel.

1. Locate **Employee Ideas** table in the data panel.

1. Select **…** (ellipsis), and then select **Edit data**.

1. Select **Add column**.

1. Enter a, such as **Message ID**.

1. Select **Create**.

1. Select **Close** in the bottom-right corner to return to Power Apps Studio.

## Update the submit button to capture the message ID

Now we'll update the button that submits ideas to store the message ID in the **Employee Ideas** table so that later we can facilitate joining the conversation.

1. In Teams, right-click on Power Apps from the left-pane, and select **Pop out app**.

1. Select the **Build** tab.

1. Select the team in which Employee Ideas is installed.

1. Select **Installed apps.**

1. In the Employee Ideas tile, select the Ideas link.btn    

1. Switch to the **Tree View** to see controls in the app.

1. Search for **btnCampaignIdeaControls_Submit** to find the button that will submit an idea.

    > [!NOTE]
    > This control has an **OnSelect** formula with it that will create the **Employee Idea** record in Dataverse for Teams, and create the Teams message. Copy the formula outside of the app, in case you need to revert any changes.

1. Select the **btnCampaignIdeaControls_Submit** button in the tree view.

1. Find the part of the formula that begins with the following:

    ```powerapps-dot
    If(
        tglIdeaDetailControls_PostToTeams.Value,......
    ```

    And replace that part of the formula with the following:

    ```powerapps-dot
    If(
        tglIdeaDetailControls_PostToTeams.Value,
        If(
            IsError(
                UpdateContext(
                    {
                        locTeamsMessage: MicrosoftTeams.PostMessageToChannelV3(
                            gblSettingTeamId,
                            gblSettingNotificationChannelId,
                            {
                                content: Concatenate(
                                    "A new employee idea has been created!",
                                    "<br><br>",
                                    "<b>Description</b>",
                                    "<br>",
                                    locFormRecordIdea.Description
                                ),
                                contentType: "html"
                            },
                            {subject: locFormRecordIdea.Title}
                        )
                    }
                )
            ),
            Notify(
                "Message was not posted. You may not have access to the Team and/or Channel. Contact the app administrator.",
                NotificationType.Warning),
                Patch(
                    'Employee Ideas',
                    locFormRecordIdea,
                    {'Message ID': locTeamsMessage.id}
            )
        )
    );
    ```

## Customize app – Add a button to direct user to discuss Idea

> [!NOTE]
> This app is responsively designed. Follow the steps below to maintain responsive design.

1. In the tree view, search for the **btnCampaignIdeaControls_Votes** control.

1. With this control selected, switch to **Insert** panel, and select **Button**.

1. Switch back to the **Tree View** panel, and select **Button1**.

    > [!NOTE]
    > The button should be in the same container as the vote button.

1. Update **Button1** properties:

    | **Property** | **Value**                                                                                           |
    |--------------|-----------------------------------------------------------------------------------------------------|
    | Text         | "Discuss"                                                                                           |
    | X            | btnCampaignIdeaControls_Votes.X - Self.Width - 20                                                   |
    | Y            | btnCampaignIdeaControls_Votes.Y                                                                     |
    | DisplayMode  | If(  IsBlankOrError(gblRecordCampaignIdea.'Message ID'),  DisplayMode.Disabled,  DisplayMode.Edit ) |
    | Visible      | btnCampaignIdeaControls_Votes.Visible                                                               |

1. Set the **OnSelect** property of the button to the following:

    > [!NOTE]
    > The example below uses **msteams:** as the launcher. This launcher can also be **https:**, or dynamically switch to use the appropriate client.

    ```powerapps-dot
    With(
    {varMessage: gblRecordCampaignIdea.'Message ID'},
    Launch(
    Concatenate(
    "msteams://teams.microsoft.com/l/message/",
    gblSettingNotificationChannelId,
    "/",
    varMessage,
    "?groupId=",
    gblSettingTeamId,
    "&parentMessageId=",
    varMessage
    )
    )
    )
    ```

1. Save and publish the app.

## Test the app

Now that you've the discuss button to the app, lets test the process:

1. Open the modified Ideas app.

1. Create an idea, toggling the post to teams toggle to yes.

1. Select the **Discuss** button.

1. Verify that you're taken to the posted message and can reply to it.

### See also

- [Understand Employee ideas app architecture](employee-ideas-architecture.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Teams store](use-sample-apps-from-Teams-store.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
