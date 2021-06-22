---
title: How to add tag to mark prioritized ideas in the Employee ideas app
description: Learn about how the customize the employee ideas app to mark prioritized ideas
author: sbahl10
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/22/2021
ms.author: v-shrutibahl
ms.reviewer: tapanm
contributors:
    - v-ljoel
---

# Employee Ideas – Add tag to mark prioritized ideas

The Employee Ideas Power Apps sample app for Microsoft Teams provides a platform for employees to submit ideas for various campaigns (i.e., categories for grouping ideas around common themes).

The Employee Ideas app solution consists of two apps:

1.  [Ideas app](https://docs.microsoft.com/powerapps/teams/bulletins#manage-bulletins-app)
    
2.  [Manage Ideas app](https://docs.microsoft.com/powerapps/teams/bulletins#bulletins-app)

With the Ideas app, Managers can setup campaigns, users can submit ideas, view other users’ ideas, and also vote for ideas that they like the best. The
experience can be customized by the admin or managers by editing campaigns, specifying justification questions that need to be answered by people submitting the ideas and also specify date threshold between which the campaign would be open for submitting ideas. The app also includes insights about who is submitting the greatest number of ideas and the most popular ideas during the week.

But once the ideas have been submitted and the voting period is over, how should a manager prioritize which ideas to act upon? You might prioritize those ideas with the most votes, or the ideas that are most aligned with your business goals and initiatives. But once you determine your prioritization logic, you will need a way to flag the ideas that are priority.

In this topic we will learn how to add a Priority tag to an Idea in the Manage Idea app so that the Manager can tag prioritized ideas. We will also add a label on the Idea in the Ideas app to indicate if it was a prioritized idea or not. When done, the manager will be able to mark prioritized ideas in the Manage Ideas app, and users of the Ideas app will be able to see that their idea has been prioritized.

> NOTE: before starting this topic, please review **How to customize Employee Ideas**  (insert link).

## Prerequisites

To complete this lesson, we would need the ability to login into Microsoft Teams which will be available as part of select Microsoft 365 subscriptions and will also need to have the Employee Ideas Power Apps template for Microsoft Teams installed. This app can be installed from ka.ms/TeamsEmployeeIdeas (confirm link).

## Login into the Manage Ideas app

1.  Select the Power Apps icon on the left and go to the Build tab.

2.  Select the Team in which the Employee Ideas app is installed from the left navigation menu.
    
3.  Select Installed Apps and select Manage Ideas to open the app.

4.  The Manage Ideas app opens.

## Add a new field to the Employee Ideas table

1.  Select the Data option from the left navigation menu.

2.  Select the Employee Ideas table and select the three dots.

3.  Select Edit data.

4.  Select +Add column.

5.  Set the following column properties

    - Name = Prioritize

    - Type = Yes/No

    - Default = No

6.  Select Done.

## Add new control to the Campaign Detail Screen

1.  From the tree view, select the Campaign Summary Screen.

2.  Press down the Alt key and select one of the campaigns.

3.  All the ideas under the select campaign are listed.

4.  Press down the Alt key and select one of the ideas.

5.  The idea details show up.

6.  Select the container conCampaignIdeaControls.

7.  Select the + Insert from the left navigation menu.

8.  Select Input -\> Toggle to add a Toggle button to the controls section of the Campaign Details Screen.
    
9.  You will want to make the toggle button have consistent look and fee with the other controls on the screen and set it to patch the idea priority field
    when set to prioritized. Set the following properties of the new toggle button.
    - X = btnCampaignIdeaControls_Share.X – 200
    
    - Y = btnCampaignIdeaControls_Share.Y
    
    - OnText = "Prioritized"
    
    - OffText = "Not Prioritized"
    
    - Font size = 12
    
    - OnCheck = Patch('Employee Ideas', gblRecordCampaignIdea, {Prioritize: 'Prioritize (Employee Ideas)'.Yes})
    
    - OnUncheck = Patch('Employee Ideas', gblRecordCampaignIdea, {Prioritize: 'Prioritize (Employee Ideas)'.No})

## Publish the Manage Ideas App

1.  All the changes to the Manage Ideas app are completed.

2.  The app can now be published by selecting the Publish to Teams button on the top right.

## Login into the Ideas app

1.  Select the Power Apps icon on the left and go to the Build tab.

2.  Select the Team in which the Employee Ideas app is installed from the left navigation menu.
    
3.  Select Installed Apps and select Ideas to open the app.

4.  The Ideas app opens.

## Add a label to the Ideas app

1.  From the tree view, select the Campaign Summary Screen.

2.  Press down the Alt key and select one of the campaigns.

3.  The Ideas list for the selected campaign opens.

4.  Press down the Alt key and select one of the ideas.

5.  The Idea Details for the selected idea opens.

6.  Select the label lblCampaignIdeaCard\_CreatedByOn.

7.  Next we want to update the label text to indicate that the idea is prioritized. Update the Text property to the following:
    
    ```
    Concatenate(
    
    gblRecordCampaignIdea.'Owning User'.'Full Name',
    
    " ",
    
    Text(
    
    gblRecordCampaignIdea.'Created On',
    
    "[\$-en-US]mm/dd h:mm:ss AM/PM "
    
    ),
    
    If(gblRecordCampaignIdea.Prioritize='Prioritize (Employee Ideas)'.Yes," \|
    Prioritized", " \| Not Prioritized")
    
    )
    ```
    
    

## Test the app

1.  Login into Teams and navigate to Team where the Employee Ideas app is installed.
    
2.  Select the Manage Ideas tab on the top.

3.  The Manage Ideas app opens.

4.  Select one of the Campaigns – say Workplace Safety.

5.  Open an existing idea.

6.  Verify that the label showing the creator of the idea plus the timestamp also shows whether the idea was prioritized or not.

![Priority displayed on Idea details screen](media/add-tag-to-mark-ideas-prioritized/priority-displayed-on-idea-details-screen.png "Priority displayed on Idea details screen")
