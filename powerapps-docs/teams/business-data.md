---
title: Have a conversation about your business data in a Teams app.
description: Learn how to enable conversations about your business from within your Power App in Teams.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/24/2021
ms.author: namarwah
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - navjotm
    - joel-lindstrom
---

# Have a conversation about your business data in a Teams app

Apps in Microsoft Teams drive collaboration by enabling users to do work where they communicate and collaborate. One way to make your apps collaborative is by adding the ability to have a conversation about your app or the data in your app. Teams is your go-to place to have such conversations.

For example, in the [Profile+ sample app](profile-app.md) for Teams, when you select one or more profile cards in the app, you can start a chat with the selected people directly in Teams.

You might also want to use this capability for your apps. For example, if you're building a sales opportunity tracker for the sales manager to review upcoming deals, you might want to add a button for the user to chat with the sales person about the opportunity.

This way, Power Apps in Teams can use deep integration with other Teams capabilities to make apps collaborative. In this article, we'll learn how we can integrate Power Apps with Teams to facilitate conversations.

## Prerequisites

To complete this lesson, we'd need the ability to create apps within Teams that will be available as part of select Microsoft 365 subscriptions.

## Log in into Teams

Log in into Teams using either the Desktop app or the web app

## Create a new Team

In this section, we'll create a new Teams team and then create an app within that team. Skip this section if you already have a team you want to use instead.

1. To create a new team, select the Teams tab, and then select **Join or create a team** on the left bottom of the screen.

1. Select **Create Team** > **From Scratch** > **Public**, give the team a name such as "Calls and Meetings Integration", and select **Create**.

1. (Optional) If you have any members in your organization that you'd like to add to the team for testing purposes, select them, and add them in the popup for adding members.

1. Select **Close**.

The new team gets created, and is listed under the Teams tab.

## Create a new app

We'll create an app where the user can start a conversation for a particular team and Channel by selecting a button and typing in a message in a text box. The user can then select the **Submit** button to post the message in the particular
team and channel in Teams, then other user can join the conversation.

1. Open Teams.

1. Select **Power Apps** from the left-pane.

1. Select **+ New app** under **Recent apps**.

1. Select the team created earlier, and then select **Create**.

    The app gets created and Power Apps Studio opens to allow editing the app.

1. Enter a name for the app, such as "Conversation app", and select **Save**.

    The app is created with a default gallery on Screen 1.

## Add Teams as a connector

We need to add Teams as a connector to the app since we want to be able to access the teams and channels from the logged in user’s account.

1. Select **Data** from the left-pane.
1. Select **+ Add data**, and then select **Connectors**.
1. Scroll down and select **See all connectors**.
1. Search for and select Teams connector.

## Add a new table to capture company record

We need to add a table to maintain a list of companies we'll use as the company record, and to start a conversation about it.

1. Select **Data** from the left-pane.

1. Select **+ Add data** and then create a new table with the name "Company", and plural name as "Companies".

1. Add a few company names to the table, and then select **Close**.

## Add a new screen to select the customer

Next, we'll add a screen to the app so that users can select the customer that they want to have the conversation about.

1. In the tree view, select **+ New screen** > select **Scenarios** tab > select **List**.

    A new screen gets added with a gallery list.

1. Update the title of the gallery to "Companies List".

1. Select **Companies** as the data source for the gallery.

    The list of companies that was added shows up in the gallery **TemplateGalleryList1**.

1. Delete **Screen1** from the tree view, and rename the new screen to **Screen1**.

## Add a new table to capture the conversation details

We need to add another table to capture the details such as the Teams conversation ID, team, and channel related to a conversation started in the app.

1. Select **Data** > **+ Add data** > **Create new table**.

1. Enter table name as **Conversation** and plural name as **Conversations**.

1. Change the default **Name** column name to **ID**.

1. Add the following columns to the conversation table:

    | **Column**   | **Type**                       |
    | ------------ | ------------------------------ |
    | Team         | Text                           |
    | Team Channel | Text                           |
    | Team Name    | Text                           |
    | Channel Name | Text                           |
    | Company      | Lookup, related table= Company |

1. Save and close the table.

## Add a new screen to start or join a conversation

Now, we'll add a new screen where the app user can start or join a conversation.

1. In the tree view, select **+ New screen** > **Blank layout**.

1. Update the **Fill** property of the screen to something other than white color.

    In our example, we've set the Fill property of the screen to `RGBA(224, 224, 237, 1)`.

1. Select **+** (Insert) > **Input** > **Button**.

1. Update the following properties of the button.

    | Property  | Value                                              |
    |-----------|----------------------------------------------------|
    | Name      | startaconversation_Button                          |
    | Text      | "Start a conversation"                             |
    | Width     | 200                                                |
    | Height    | 32                                                 |
    | Font size | 12                                                 |
    | X         | `Parent.Width/2 - startaconversation_Button.Width/2` |
    | Y         | 100                                                |
    | OnSelect  | `Set(enterMessage,true)`                             |

1. Select **+** (Insert) > **Input** > **Combo box**.

1. Update the following properties of the Combo box.

    | Property | Value                                  |
    |----------|----------------------------------------|
    | Name     | team_Combobox                          |
    | Items    | `MicrosoftTeams.GetAllTeams().value`     |
    | Width    | 320                                    |
    | Height   | 32                                     |
    | X        | `Parent.Width/2 - team_ComboBox.Width/2` |
    | Y        | 200                                    |
    | Text     | "Team"                                 |
    | Tooltip  | "Team"                                 |
    | Visible  | enterMessage                           |

1. Add another combo box and update the following properties.

    | Property | Value                                                                                                               |
    |----------|---------------------------------------------------------------------------------------------------------------------|
    | Name     | channel_Combobox                                                                                                    |
    | Items    |         `If(!IsBlank(team_ComboBox.Selected.id),MicrosoftTeams.GetChannelsForGroup(team_ComboBox.Selected.id).value)` |
    | Width    | 320                                                                                                                 |
    | Height   | 32                                                                                                                  |
    | X        | `Parent.Width/2 - channel_ComboBox.Width/2`                                                                           |
    | Y        | 200                                                                                                                 |
    | Text     | "Channel"                                                                                                           |
    | Tooltip  | "Channel"                                                                                                           |
    | Visible  | enterMessage                                                                                                        |

1. Select **+** (Insert) > **Input** > **Text box**.

1. Update the following properties of the Textbox.

    | Property    | Value                                    |
    |-------------|------------------------------------------|
    | Name        | message_TextBox                          |
    | Value       | ""                                       |
    | Width       | 500                                      |
    | Height      | 180                                      |
    | X           | `Parent.Width/2 - message_TextBox.Width/2` |
    | Y           | 300                                      |
    | Placeholder | Type message here                        |
    | Visible     | enterMessage                             |

1. Select **+** (Insert) > **Input** > **Button**.

1. Update the following properties of the button.

    | Property  | Value                                  |
    |-----------|----------------------------------------|
    | Name      | submit_Button                          |
    | Value     | "Submit"                               |
    | Width     | 96                                     |
    | Height    | 32                                     |
    | Font size | 12                                     |
    | X         | `Parent.Width/2 - submit_Button.Width/2` |
    | Y         | 500                                    |
    | Visible   | enterMessage                           |

1. Copy the following formula in the **OnSelect** event of the button.

    ```powerapps-dot
    Patch(Conversations,Defaults(Conversations),{ID:MicrosoftTeams.PostMessageToChannelV3(team_ComboBox.Selected.id,channel_ComboBox.Selected.id,{content:message_TextBox.Value,contentType: "text"},{subject:"New conversation"}).id,Team:team_ComboBox.Selected.id,'Team Channel':channel_ComboBox.Selected.id, 'Team Name':team_ComboBox.Selected.displayName,'Channel Name':channel_ComboBox.Selected.displayName, Company: TemplateGalleryList1.Selected}); Set(enterMessage,false); Reset(team_ComboBox);Reset(channel_ComboBox);Reset(message_TextBox)
    ```

    > [!NOTE]
    > - In the above formula, we're using the **Patch** function to create a row in the **Conversations** table to capture the conversation ID along with the team, team name, channel and channel came. At the same time, we're also posting a message in the appropriate team and channel using the **PostMessageToChannelV3** function. We then set the **enterMessage** variable back to "false" to hide some of the fields and buttons whose visibility depends on this variable.
    > - The subject is hardcoded to “New conversation" to keep the app simple ,and not add another text box control to capture. But a text box can be added for subject to the screen and can be captured by the user. This formula will need to be adjusted accordingly to reference that control.
    > The **Reset** function doesn't work for the **Fluent UI Combobox** control. This is needed to not have any team or channel selected once a message is posted.

1. Select **+** (Insert) > **Input** > **Button**.

1. Update the following properties of the button.

    | Property  | Value                                  |
    |-----------|----------------------------------------|
    | Name      | joinconversation_Button                |
    | Text      | "Join conversation"                    |
    | Width     | 200                                    |
    | Height    | 32                                     |
    | Font size | 12                                     |
    | X         | `Parent.Width/2 - submit_Button.Width/2` |
    | Y         | 500                                    |
    | Visible   | enterMessage                           |

1. Copy the following formula in the **OnSelect** event of the button.

    ```powerapps-dot
    Launch(Concatenate("msteams://teams.microsoft.com/l/message/",Last(Sort(Conversations, 'Created On', Ascending)).'Team Channel',"/",Gallery1.Selected.etag,"?tenantId=",Param("tenandId"),"&groupId=",Last(Sort(Conversations, 'Created On', Ascending)).Team,"&parentMessageId=",LookUp(MicrosoftTeams.GetMessagesFromChannel(Last(Sort(Conversations, 'Created On', Ascending)).Team,Last(Sort(Conversations, 'Created On', Ascending)).'Team Channel').value,id = Last(Sort(Conversations, 'Created On', Ascending)).Team).etag,"&teamName=",Last(Sort(Conversations, 'Created  On', Ascending)).'Team Name',"&channelName=",Last(Sort(Conversations, 'Created On', Ascending)).'Channel Name'),{},LaunchTarget.New)
    ```

    > [!NOTE]
    > - In the above formula, we're using the **Launch** function to launch Teams using the team and channel parameters of the last record that was created in the **Conversations** table. We're doing this so that when a user starts a conversation and submits a message to post to a channel, the user can then select the **Join Conversation** button to go to the Teams post directly.
    > - We're using the last function here to keep it simple. If you anticipate using this app more extensively and anticipate having multiple conversations, you could get creative by using a gallery of conversations, and letting the user select which conversation they'd want to join.*

## Update the gallery OnSelect Property

Next, we'll update the **OnSelect** property of the company gallery so that when a user selects a company from the list, the app will go to the second screen.

1. Select **Screen1** from the tree view to open the **Companies** gallery.

2. Set the **OnSelect** property of the gallery item to `Navigate(Screen2)`.

## Save and publish the app

1. Select **Save** on the top-right to save the app.

1. Select **Publish** on the top-right to publish the app.

1. Select **Next**.

1. Under **Add to Channel**, make sure the channel under which the app should be shown is listed and shows as "1 active tab(s)" and not "0 active tab(s)".

1. Select **Save and Close** to complete the publishing of the app.

## Testing the app

Run the app in preview mode or go to the team in which the app is created.

1. The Companies gallery should show up as the first screen.
1. Select one of the companies.
1. You should only see two buttons: **Start a conversation** and **Join a conversation**.
1. Select **Start a conversation**.
1. Additional fields should show up:
    - Team (dropdown with a list of teams)
    - Channel (dropdown list of channels within the selected team)
    - Message box (text box to type in the message to be sent to the team)
    - Submit button (to submit the message)
1. Select a team.
1. Select a channel within the team.
1. Enter message.
1. Select **Submit**. All the additional fields/controls get hidden.
1. Select **Join conversation** to be taken to the team and channel chat where the last message was sent.

    ![Testing the app](media/have-a-conversation-about-your-business-data/testing-the-app-1.png "Testing the app")

### See also

- [Boards (preview) sample app](boards.md)
- [Bulletins sample app](bulletins.md)
- [Employee ideas sample app](employee-ideas.md)
- [Get connected (preview)](get-connected.md)  
- [Inspection sample apps](inspection.md)  
- [Issue reporting sample apps](issue-reporting.md)
- [Milestones sample app](milestones.md)
- [Perspectives (preview) sample app](perspectives.md)
- [Profile+ (preview) sample app](profile-app.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
