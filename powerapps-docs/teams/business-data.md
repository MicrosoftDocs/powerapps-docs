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

To complete this lesson, we'd need the ability to create apps within Teams which will be available as part of select Microsoft 365 subscriptions.

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

1. Add a few company names to the table, and then select close to close the table.

## Add a new screen to the app

Next we will add a screen to the app so that users can select the customer which they want to discuss:

1. In the tree view select +New screen, select Scenarios tab and select **List**.

2. A new screen gets added with a gallery list.

3. Update the Title of the Gallery to “Companies List.”

4. Select Companies as the Data Source for the Gallery.

5. The list of companies that was added shows up in the gallery TemplateGalleryList1.

6.  Delete Screen1 from the tree view and rename this screen to say Screen1.

## Add a new table to capture Conversation details

We need to add another table to capture details like Teams conversation id, team, channel etc. related to a conversation started in the ap To do this, select the Data icon from the left navigation menu:

3.  Select +Add data -\> + Create new table.

4.  Table name = Conversation.

5.  Plural name = Conversations.

6.  The table gets created with one column called Name.

7.  Change that column name to ID.

8.  Add the following columns to the conversation table:

    | **Column**   | **Type**                       |
    | ------------ | ------------------------------ |
    | Team         | Text                           |
    | Team Channel | Text                           |
    | Team Name    | Text                           |
    | Channel Name | Text                           |
    | Company      | Lookup, related table= Company |
    
7.  Save and close the table

## Add a new screen to the app

Now we will add a new screen where the app user can start or join a conversation:

1.  In the tree view select +New screen and select Blank layout.
2.  A new screen gets added.
3.  Update the Fill property of the screen to something other than white.
4.  In our example, we set the Fill property of the screen to RGBA(224, 224,
    237, 1).
5.  Select the + (Insert) option from the left navigation menu.
6.  Select Input-\> Button to add a button to the screen.
7.  Update the following properties of the button.

| Property  | Value                                              |
|-----------|----------------------------------------------------|
| Name      | startaconversation_Button                          |
| Text      | "Start a conversation"                             |
| Width     | 200                                                |
| Height    | 32                                                 |
| Font size | 12                                                 |
| X         | Parent.Width/2 - startaconversation_Button.Width/2 |
| Y         | 100                                                |
| OnSelect  | Set(enterMessage,true)                             |

8.  Select the + (Insert) option from the left navigation menu.

9.  Select Input-\> Combobox to add it to the screen.

10. Update the following properties of the Combobox.

| Property | Value                                  |
|----------|----------------------------------------|
| Name     | team_Combobox                          |
| Items    | MicrosoftTeams.GetAllTeams().value     |
| Width    | 320                                    |
| Height   | 32                                     |
| X        | Parent.Width/2 - team_ComboBox.Width/2 |
| Y        | 200                                    |
| Text     | "Team"                                 |
| Tooltip  | "Team"                                 |
| Visible  | enterMessage                           |

11. Select the + (Insert) option from the left navigation menu.

12. Select Input-\> Combobox to add it to the screen.

13. Update the following properties of the Combobox.

| Property | Value                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------------------|
| Name     | channel_Combobox                                                                                                    |
| Items    |         If(!IsBlank(team_ComboBox.Selected.id),MicrosoftTeams.GetChannelsForGroup(team_ComboBox.Selected.id).value) |
| Width    | 320                                                                                                                 |
| Height   | 32                                                                                                                  |
| X        | Parent.Width/2 - channel_ComboBox.Width/2                                                                           |
| Y        | 200                                                                                                                 |
| Text     | "Channel"                                                                                                           |
| Tooltip  | "Channel"                                                                                                           |
| Visible  | enterMessage                                                                                                        |

14. Select the + (Insert) option from the left navigation menu.

15. Select Input-\> Textbox to add it to the screen.

16. Update the following properties of the Textbox.

| Property    | Value                                    |
|-------------|------------------------------------------|
| Name        | message_TextBox                          |
| Value       | ""                                       |
| Width       | 500                                      |
| Height      | 180                                      |
| X           | Parent.Width/2 - message_TextBox.Width/2 |
| Y           | 300                                      |
| Placeholder | Type message here                        |
| Visible     | enterMessage                             |

17. Select the + (Insert) option from the left navigation menu.

18. Select Input-\> Button to add a button to the screen.

19. Update the following properties of the button.

| Property  | Value                                  |
|-----------|----------------------------------------|
| Name      | submit_Button                          |
| Value     | "Submit"                               |
| Width     | 96                                     |
| Height    | 32                                     |
| Font size | 12                                     |
| X         | Parent.Width/2 - submit_Button.Width/2 |
| Y         | 500                                    |
| Visible   | enterMessage                           |

20.  Use this code in the OnSelect button of the button:

```
Patch(Conversations,Defaults(Conversations),{ID:MicrosoftTeams.PostMessageToChannelV3(team_ComboBox.Selected.id,channel_ComboBox.Selected.id,{content:message_TextBox.Value,contentType: "text"},{subject:"New conversation"}).id,Team:team_ComboBox.Selected.id,'Team Channel':channel_ComboBox.Selected.id, 'Team Name':team_ComboBox.Selected.displayName,'Channel Name':channel_ComboBox.Selected.displayName, Company: TemplateGalleryList1.Selected}); Set(enterMessage,false); Reset(team_ComboBox);Reset(channel_ComboBox);Reset(message_TextBox)
```

> NOTE: In the above formula, we are using the Patch function to create a row in the Conversations table to capture the conversation ID along with the Team, Team Name, Channel and Channel Name while at the same time also posting a message in the appropriate Team and Channel using the PostMessageToChannelV3 function. We then also set the enterMessage variable back to false to hide some of the fields and buttons whose visibility depends on this variable
>
> Also, note that the subject here is hardcoded to “New conversation” to keep the app simple and not add another text box control to capture. But a text box can be added for subject to the screen and can be captured by the user. This formula will need to be adjusted accordingly to reference that control.
>
> The Reset function does not work for the Fluent UI Combobox control. This is needed to not have any team or channel selected once a message is posted.*

20. Select the **+** (Insert) option from the left navigation menu.

21. Select Input-\> Button to add a button to the screen.

22. Update the following properties of the button.

| Property  | Value                                  |
|-----------|----------------------------------------|
| Name      | joinconversation_Button                |
| Text      | "Join conversation"                    |
| Width     | 200                                    |
| Height    | 32                                     |
| Font size | 12                                     |
| X         | Parent.Width/2 - submit_Button.Width/2 |
| Y         | 500                                    |
| Visible   | enterMessage                           |

23.  Use this code in the OnSelect button of the button:

```
Launch(
    Concatenate(
        "msteams://teams.microsoft.com/l/message/",
        Last(Sort(Conversations, 'Created On', Ascending)).'Team Channel',
        "/",
        Gallery1.Selected.etag,
        "?tenantId=",
        Param("tenandId"),
        "&groupId=",
        Last(Sort(Conversations, 'Created On', Ascending)).Team,
        "&parentMessageId=",   
        LookUp(MicrosoftTeams.GetMessagesFromChannel(Last(Sort(Conversations, 'Created On', Ascending)).Team,
        Last(Sort(Conversations, 'Created On', Ascending)).'Team Channel').value,
        id = Last(Sort(Conversations, 'Created On', Ascending)).Team).etag,
        "&teamName=",
        Last(Sort(Conversations, 'Created  On', Ascending)).'Team Name',
        "&channelName=",
        Last(Sort(Conversations, 'Created On', Ascending)).'Channel Name'
    ),
    {},
    LaunchTarget.New
)
```

> NOTE: In the above formula, we are using the Launch function to launch Teams using the team and channel parameters of the last record that was created in the Conversations table. We are doing this so that when a user starts a conversation and submits a message to post to a channel, the user can then select the **Join Conversation** button to navigate to the Teams post directly.
>
> We are using the last function here to keep it simple. If you anticipate using this app more extensively and anticipate having multiple conversations, you could get creative by using a gallery of conversations and letting the user select which one he would want to join.*

## Update Gallery OnSelect Property

Now we will update the OnSelect property of the company gallery so that when a user selects a company from the list, the app will navigate to the second screen:

1. Select **Screen1** from the tree view to open the Companies gallery.

2. Set the **OnSelect** Property of the gallery item to Navigate(Screen2).

## Save and Publish the App

1.  Select **Save** on the top right to save the app.

2.  Select the Publish button on the top right to Publish the app.

3.  Select Next on the popup.

4.  Under Add to Channel, make sure the Channel under which the app should be shown is listed and shows as 1 active tab(s) and not 0 active tab(s).

5.  Select Save and Close to complete the publishing of the app.

6.  The app gets published.

## Testing the app

Run the App in preview mode or go to the team in which the app is created

1.  The Companies gallery should show up as the first screen.
2.  Select one of the companies.
3.  The next screen should open .
4.  You should only see two buttons – Start a conversation and Join conversation.
5.  Select the **Start a conversation** button.
6.  Additional fields should show up – Team (dropdown – list of teams), Channel (dropdown – list of channels within the selected team), Message box (text box to type in the message to be sent to the team), Submit button (to submit the message).
7.  Select a Team.
8.  Select a Channel within the team.
9.  Type in a message.
10.  Select the **Submit** button.
11.  All the additional fields/controls get hidden.
12.  Select **Join conversation** button to be taken to the Team and Channel chat where the last message was sent.

![Testing the app](media/have-a-conversation-about-your-business-data/testing-the-app-1.png "Testing the app")wind

### See also

- [Boards (Preview) sample app](boards.md)
- [Bulletins sample app](bulletins.md)
- [Employee ideas sample app](employee-ideas.md)
- [Get connected (Preview)](get-connected.md)  
- [Inspection sample apps](inspection.md)  
- [Issue reporting sample apps](issue-reporting.md)
- [Milestones sample app](milestones.md)
- [Perspectives (Preview) sample app](perspectives.md)
- [Profile+ (Preview) sample app](profile-app.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
