---
title: Enable users to discuss ideas | Microsoft Docs
description: Explains how to extend the Employee Ideas template app for Microsoft Teams to take users to a discussion about an idea in Microsoft Teams.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/22/2021
ms.author: v-ljoel
ms.reviewer: tapanm
---

# Enable users to discuss ideas

The Employee Ideas template Power App for Microsoft Teams makes it easy to capture ideas and suggestions from your colleagues and have colleagues vote for their favorite ideas. But you might want to make this more interactive by facilitating discussions around ideas.

Currently the Employee Ideas app posts messages to a teams channel when an Idea is submitted. In this topic we will extend the app to provide a mechanism for users to navigate to the idea channel message so the can interact and discuss the idea with other users.

## Prerequisites:

-   Install the Employee Ideas app in a team from  <https://aka.ms/TeamsEmployeeIdeas>.

-   Enable posting of Teams channel messages in the app settings.

-   Add the Power Apps app in Teams by selecting the elipses (…) and searching  for **Power Apps.**

-   Right click on the Power Apps app and select **Pop out app** to launch Power  apps in a new window.

## Add the message ID column

The Employee Ideas template app posts messages to Teams channels when an app or a campaign are created; however, it currently does not store any record of that message. Since we want the app to give users the ability to comment and discuss the idea via the posted message thread, we will update the app to preserve the ID of the message.

1.  Open the Ideas app in the Power Apps app in Microsoft Teams.

2. Go to the **Build** tab.

3. Select the data panel.

4.  Locate Employee Ideas table in the data panel.

5. Select the (…) ellipsis and select **Edit data**. 

6. Add a column by

   1.  Selecting **Add column**.

   2.  Entering a name, such as **Message ID**.

   3.  Select **Create**.

7. Select **Close**  in the bottom-right corner, to return to Power Apps studio.

## Update the submit button to capture the message ID
Now we update the button that submits ideas to store the message ID in the Employee Ideas table so that later we can facilitate joining the conversation.

1. Switch to the **Tree View** to see controls in the app.
2. Search for **btnCampaignIdeaControls_Submit** to find the button which will  submit an idea.

   > NOTE
   >
   >  This control has an OnSelect formula with it that will create the
   > Employee Idea Dataverse for Teams record, and create the Teams message. Please make a copy of the formula outside of the app, in case you need to revert any change

3. Select the **btnCampaignIdeaControls_Submit** button  in the tree view.

4. Find the part of the formula that begins with the following:
```
If(
    tglIdeaDetailControls_PostToTeams.Value,......
```
Replace that part of the formula with the following:

```
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
```



## Customize App – Add a button to direct user to discuss Idea

> NOTE 
> This app is responsively designed, please follow steps below to maintain responsive design.

1.  In the tree view, search for the **btnCampaignIdeaControls_Votes** control.

2.  With this control selected, switch to ‘Insert’ panel and select button.

3.  Switch back to the ‘Tree View’ panel and select Button1

> NOTE 
> The button should be in the same container as the vote button.

2.  Update Button1 properties:

| **Property** | **Value**                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------|
| Text         | "Discuss"                                                                                           |
| X            | btnCampaignIdeaControls_Votes.X - Self.Width - 20                                                   |
| Y            | btnCampaignIdeaControls_Votes.Y                                                                     |
| DisplayMode  | If(  IsBlankOrError(gblRecordCampaignIdea.'Message ID'),  DisplayMode.Disabled,  DisplayMode.Edit ) |
| Visible      | btnCampaignIdeaControls_Votes.Visible                                                               |

3.  Set the OnSelect property/function of the button


> NOTE 
> The example below uses msteams: as the launcher – this can also be https:, or dynamically switch to use the appropriate client

```
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
4.  Save and publish the app.

## Test the app

Now that you have the discuss button to the app, let’s test the process:

1.  Open the modified Ideas app.

2.  Create an idea, toggling the post to teams toggle to yes.

3.  Select the **Discuss** button.

4.  Verify that you are taken to the posted message and can reply to it.
