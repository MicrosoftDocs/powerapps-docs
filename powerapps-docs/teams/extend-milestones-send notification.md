---
title: Send notification to the Team when work item status is updated in the Milestones sample app
description: Learn how to send an adaptive card when a work item status is updated in the Milestones Power Apps template for Microsoft Teams.
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/25/2021
author: joel-lindstrom	
ms.author: v-ljoel
ms.reviewer: tapanm
contributors:
  - joel-linkstrom
  - navjotm
  - tapanm-msft
---

# Send notification to the Team when work item status is updated in the Milestones sample app

The Milestones sample app for Microsoft Teams allows users to track progress of completion of work items in projects across milestones. While the app allows work items to be updated and maintained, there's currently no standard notifications about work item updates to the team.

In this article, we'll learn how to create a Power Automate flow to send an adaptive card notification to the Team (in which the app is installed) when work item status changes.

## Prerequisites

To complete this exercise, we would need the ability to log in into Teams that will be available as part of select Microsoft 365 subscriptions and will also need to have the Milestones Power Apps template for Teams installed. This app can be installed from <https://aka.ms/TeamsInspection>.

## Log in into the Milestones app

1. Select the Power Apps icon on the left and go to the Build tab.

1. Select the Team in which the Milestones app is installed from the left app  menu.

1. Select **Installed apps** and select on Milestones to open the app. The Milestones app opens.

## Add condition to call the Power Automate flow

1. From the tree view in the left pane, select the **Projects** screen.

1. On the screen, press down the **Alt** key, and select to open any one project. The Add/Edit Work Item screen opens.

1. Select the **Done** button.

1. Select the **OnSelect** property of the done button.

1. On selecting the **Done** button, along with the other updates that run in the  background, we also want to trigger a flow that would send out an adaptive card update to the Team if the status of the work item is updated. To do this change, add the following to the top of the OnSelect formula:

    ```powerapps-dot
    If(
    
    locEditWorkItem,
    
    //adding code to call a flow when status changes
    
    If(
    
    locSelectedWorkItem.'Work Item Status'.'Project Work Item Status' \<\>
    cmbAddWorkItemStatus.Selected.'Project Work Item Status',
    
    true //your flow call will come here
    
    );
    
    ```

1. Copy the entire code from the **OnSelect** property of the **Done** button, and paste it in a text editor for use later.

1. Select **...** (ellipsis) next to **Settings** on the top ribbon, and select **Power Automate**.

1. The **Data** pop-up opens with the option to **Create a new flow**.

1. Select the **Create a new flow** button. A browser window opens with the new Power Automate flow screen.

1. Update the name of the flow to – "Send Adaptive card notification when the status of the work order changes".

1. Select the option to trigger Power Apps from the list of triggers. The new flow gets created and the Power Apps step is loaded on the screen.

## Create the Power Automate flow

1. After following the steps in the previous section, select the **+New** step button.

1. Select the action **Get a row by ID**, and select Table Name as **Project Work Items**.

1. Under Row ID, open the dynamic content and select the **Ask in Power Apps** option.

1. Rename the step to "Get Work Item record".

1. Select the **+Next** step button again, and select the action **Get a row by ID**, and select Table Name as **Work Item Statuses**.

1. Under Row ID open the dynamic content, select **Work Item Status (Value)**.

1. Rename the step to Get Work Item Status record.

1. Add another step by selecting **+New** step.

1. Add the action Initialize variable.

    - Rename step to Initialize variable - "Card Title"

    - Name - "varCardTitle"

    - Type - "String"

    - Value = Status update for Work Item {*and then select dynamic content Name of the Work item added in step 3*}

1. Add another step by selecting **+New** step.

1. Add the action Initialize variable.

    - Rename step to Initialize variable - Review Link

    - Name - "varReviewWorkItemLink"

    - Type - "String"

    - Value = <!--- needs review --->

1. For the **Review Work Item Link** action, we'll use the link to the app. To find this link, open the team where the Milestones app is installed, and copy the link for tab in which the app is installed. You can copy the link to the tab by opening the tab, then selecting **...** (ellipses) in the upper right corner.

    Your URL will look similar to the following example:

    `https://teams.microsoft.com/l/entity/GUID/_djb2_msteams_prefix_956529380?context=%7B%22subEntityId%22%3Anull%2C%22channelId%22%3A%2219%3AGUID%40thread.tacv2%22%7D&groupId=GUID&tenantId=GUID`

1. To continue, copy the part of the URL that comes after **context=**, and use a URL decoder such as <https://www.urldecoder.org/> to decode the URL.

1. Copy that decoded text and go back to the Power Automate flow.

1. Add a new step to the flow to initialize a variable.

1. Rename the step to **Initialize variable – Review Work Item Link**.

    - Name - "varReviewWorkItemLink"

    - Type - "String"

    - Value - {paste the text copied from the decoded url above}

1. Add a new step with the action **Compose**, and in the **Inputs** field, paste the following snippet.

    ```
    replace(replace(replace(variables('varReviewIdeasLink'),'{','%7B'),'"','%22'),'}','%7D')
    ```

1. Add another step by selecting **+New step**.

1. Select the action Post adaptive card in a chat or channel (Preview).

    - Post as = User

    - Post in = Channel

    - Team = {the team in which your app is installed}

    - Channel = General

    - Adaptive Card = <!--- needs review --->

    ```
       {
       
       "type": "AdaptiveCard",
       
       "body": [
       
       {
       
       "type": "TextBlock",
       
       "size": "large",
       
       "weight": "Bolder",
       
       "text": "Status Update for
       @{outputs('Get_Work_Item_record')?['body/msft_name']}",
       
       "wrap": true
       
       },
       
       {
       
       "type": "TextBlock",
       
       "text": "Status for Work Item
       '@{outputs('Get_Work_Item_record')?['body/msft_name']}' has been updated to
       @{outputs('Get_Work_Item_Status_record')?['body/msft_name']}",
       
       "wrap": true
       
       }
       
       ],
       
       "actions": [
       
       {
       
       "type": "Action.OpenUrl",
       
       "title": "View @{variables('varCardTitle')}",
       
       "url":
       "[https://teams.microsoft.com/l/entity/040880f4-0c68-4c38-8821-d5efd2b6ddbe/_djb2_msteams_prefix_956529380?context=@{outputs('Compose](https://teams.microsoft.com/l/entity/040880f4-0c68-4c38-8821-d5efd2b6ddbe/_djb2_msteams_prefix_956529380?context=@%7boutputs('Compose)')}"
       
       }
       
       ],
       
       "\$schema": "<http://adaptivecards.io/schemas/adaptive-card.json>",
       
       "version": "1.2"
       
       }
       
    ```

1. Save the flow.

## Trigger the flow from the Power Apps

1. After the flow is saved, go back to the Teams editor, and open the app in Power Apps.

1. In the tree view, select the **Add/Edit Work Item** screen.

1. Select the **Update** button.

1. Update the **OnSelect** property to make sure the flow is triggered.

1. Copy the formula from wherever you had pasted it earlier into the **OnSelect** property.

1. In the first If condition that was added on the top, replace “true” with the run function used to trigger the flow trigger. See example below.

    ```
    If(
    
    locEditWorkItem,
    
    //adding code to call a flow when status changes
    
    If(
    
    locSelectedWorkItem.'Work Item Status'.'Project Work Item Status' \<\>
    cmbAddWorkItemStatus.Selected.'Project Work Item Status',
    SendAdaptivecardnotificationwhenthestatusoftheworkorderchanges.Run(locSelectedWorkItem.'Project Work item') //your flow call will come here
    
    );
    
    //end code
    ```

## Update the Loading screen

1. From the tree view, select the **Loading Screen**.

1. Expand the loading screen and then **conLoading_HiddenHelper** under it.

1. Select the timer **tmrLoadingDelay** and select the **OnTimerEnd** property.

1. If the app is opened via the adaptive card link, it should directly open the work item record that was updated, which means that we would need a way to check if a work item id is being passed to the app.

1. The Loading page formula needs to be updated to include the Work Item number, so we need to Update the **OnTimerEnd** property to the following:

    ```
    If(
    
    gblAppLoaded,// && !IsBlankOrError(gblAppStyles),
    
    If(
    
    !IsBlank(Param("subEntityId")), //check if the parameter is blank or not
    
    If( //if the parameter is not blank, check if the user is on a mobile device or
    desktop/web and then populate the relevant variables and collections to make
    deep linking work
    
    (!IsBlank(Param("hostClientType")) && (Param("hostClientType") = "android" Or
    Param("hostClientType") = "ios")) \|\| (IsBlank(Param("hostClientType")) &&
    (Acceleration.X \> 0 \|\| Acceleration.Y \> 0 \|\| Acceleration.Z \> 0)) Or
    tglAdmin_Mobile.Value,
    
    //project cover colors
    
    ClearCollect(
    
    colMobileProjectCoverColors,
    
    {
    
    Color: "\#F4B9B9",
    
    Theme: "default",
    
    Base: "Color1"
    
    },
    
    {
    
    Color: "\#94BFFF",
    
    Theme: "default",
    
    Base: "Color2"
    
    },
    
    {
    
    Color: "\#E6F0FF",
    
    Theme: "default",
    
    Base: "Color3"
    
    },
    
    {
    
    Color: "\#5AC6CC",
    
    Theme: "default",
    
    Base: "Color4"
    
    },
    
    {
    
    Color: "\#C5E9EA",
    
    Theme: "default",
    
    Base: "Color5"
    
    },
    
    {
    
    Color: "\#F0F9FA",
    
    Theme: "default",
    
    Base: "Color6"
    
    },
    
    {
    
    Color: "\#EE6F99",
    
    Theme: "default",
    
    Base: "Color7"
    
    },
    
    {
    
    Color: "\#F495BF",
    
    Theme: "default",
    
    Base: "Color8"
    
    },
    
    {
    
    Color: "\#F4D2DC",
    
    Theme: "default",
    
    Base: "Color9"
    
    },
    
    {
    
    Color: "\#CEF0CD",
    
    Theme: "default",
    
    Base: "Color10"
    
    },
    
    {
    
    Color: "\#BDBDE6",
    
    Theme: "default",
    
    Base: "Color11"
    
    },
    
    {
    
    Color: "\#E2E2F6",
    
    Theme: "default",
    
    Base: "Color12"
    
    },
    
    {
    
    Color: "\#F4F4FC",
    
    Theme: "default",
    
    Base: "Color13"
    
    },
    
    {
    
    Color: "\#FBF6D9",
    
    Theme: "default",
    
    Base: "Color14"
    
    },
    
    {
    
    Color: "\#791818",
    
    Theme: "dark",
    
    Base: "Color1"
    
    },
    
    {
    
    Color: "\#053385",
    
    Theme: "dark",
    
    Base: "Color2"
    
    },
    
    {
    
    Color: "\#6264A7",
    
    Theme: "dark",
    
    Base: "Color3"
    
    },
    
    {
    
    Color: "\#002F31",
    
    Theme: "dark",
    
    Base: "Color4"
    
    },
    
    {
    
    Color: "\#025C5F",
    
    Theme: "dark",
    
    Base: "Color5"
    
    },
    
    {
    
    Color: "\#03787C",
    
    Theme: "dark",
    
    Base: "Color6"
    
    },
    
    {
    
    Color: "\#461525",
    
    Theme: "dark",
    
    Base: "Color7"
    
    },
    
    {
    
    Color: "\#CC3D6D",
    
    Theme: "dark",
    
    Base: "Color8"
    
    },
    
    {
    
    Color: "\#EA5788",
    
    Theme: "dark",
    
    Base: "Color9"
    
    },
    
    {
    
    Color: "\#043615",
    
    Theme: "dark",
    
    Base: "Color10"
    
    },
    
    {
    
    Color: "\#33344A",
    
    Theme: "dark",
    
    Base: "Color11"
    
    },
    
    {
    
    Color: "\#6264A7",
    
    Theme: "dark",
    
    Base: "Color12"
    
    },
    
    {
    
    Color: "\#464775",
    
    Theme: "dark",
    
    Base: "Color13"
    
    },
    
    {
    
    Color: "\#FFAA44",
    
    Theme: "dark",
    
    Base: "Color14"
    
    }
    
    );
    
    //local table of character widths, used for auto width labels
    
    ClearCollect(
    
    colMobileCharsWidth,
    
    staticCharWidths
    
    );
    
    //stock project cover images
    
    ClearCollect(
    
    colMobileStockImages,
    
    {appStockImage: Blank()},
    
    {appStockImage: ProjectCover_Future},
    
    {appStockImage: ProjectCover_Work},
    
    {appStockImage: ProjectCover_Shapes},
    
    {appStockImage: ProjectCover_Design},
    
    {appStockImage: ProjectCover_Flow},
    
    {appStockImage: ProjectCover_Abstract},
    
    {appStockImage: ProjectCover_Mountain},
    
    {appStockImage: ProjectCover_Vision},
    
    {appStockImage: ProjectCover_DarkShapes},
    
    {appStockImage: ProjectCover_Morning},
    
    {appStockImage: ProjectCover_Sublime},
    
    {appStockImage: ProjectCover_Tech},
    
    {appStockImage: ProjectCover_Neon},
    
    {appStockImage: ProjectCover_City}
    
    );
    
    Set(
    
    gblMobileProject,
    
    LookUp(
    
    'Project Work Items',
    
    'Project Work item' = GUID(Param("subEntityId"))
    
    ).Project
    
    );
    
    ClearCollect(
    
    colMobileWorkItems,
    
    Filter(
    
    'Project Work Items',
    
    Project.Project = gblMobileProject.Project
    
    )
    
    );
    
    UpdateContext(
    
    {
    
    locMobileCompletionStatus: First(
    
    Sort(
    
    'Project Work Item Statuses',
    
    Sequence,
    
    Ascending
    
    )
    
    )
    
    }
    
    );
    
    Clear(colMobileWorkItemStatuses);
    
    ForAll(
    
    Sort(
    
    Filter(
    
    'Project Work Item Statuses',
    
    'Project Work Item Status' \<\> locMobileCompletionStatus.'Project Work Item
    Status'
    
    ),
    
    Sequence,
    
    Ascending
    
    ),
    
    Collect(
    
    colMobileWorkItemStatuses,
    
    {
    
    Name: ThisRecord.Name,
    
    Color: ThisRecord.Color,
    
    'Color Dark': ThisRecord.'Color Dark',
    
    'Project Work Item Status': ThisRecord.'Project Work Item Status',
    
    Sequence: ThisRecord.Sequence
    
    }
    
    )
    
    );
    
    Collect(
    
    colMobileWorkItemStatuses,
    
    {
    
    Name: locMobileCompletionStatus.Name,
    
    Color: locMobileCompletionStatus.Color,
    
    'Color Dark': locMobileCompletionStatus.'Color Dark',
    
    'Project Work Item Status': locMobileCompletionStatus.'Project Work Item
    Status',
    
    Sequence: locMobileCompletionStatus.Sequence
    
    }
    
    );
    
    Navigate(
    
    'Mobile Work Item Details Screen',
    
    ScreenTransition.None,
    
    {
    
    locMobileSelectedWorkItem: LookUp(
    
    'Project Work Items',
    
    'Project Work item' = GUID(Param("subEntityId"))
    
    ),
    
    locMobileShowWorkItemDetail: true,
    
    locMobileShowSearchWorkItem: false,
    
    locMobileNavToDetailFromAbout: true
    
    }
    
    ),
    
    Set(
    
    gblProject,
    
    LookUp(
    
    'Project Work Items',
    
    'Project Work item' = GUID(Param("subEntityId"))
    
    ).Project
    
    );
    
    UpdateContext(
    
    {
    
    locCompletionStatus: First(
    
    Sort(
    
    'Project Work Item Statuses',
    
    Sequence,
    
    Ascending
    
    )
    
    )
    
    }
    
    );
    
    Clear(colWorkItemStatuses);
    
    ForAll(
    
    Sort(
    
    Filter(
    
    'Project Work Item Statuses',
    
    'Project Work Item Status' \<\> locCompletionStatus.'Project Work Item Status'
    
    ),
    
    Sequence,
    
    Ascending
    
    ),
    
    Collect(
    
    colWorkItemStatuses,
    
    {
    
    Name: ThisRecord.Name,
    
    Color: ThisRecord.Color,
    
    'Color Dark': ThisRecord.'Color Dark',
    
    'Project Work Item Status': ThisRecord.'Project Work Item Status',
    
    Sequence: ThisRecord.Sequence
    
    }
    
    )
    
    );
    
    Collect(
    
    colWorkItemStatuses,
    
    {
    
    Name: locCompletionStatus.Name,
    
    Color: locCompletionStatus.Color,
    
    'Color Dark': locCompletionStatus.'Color Dark',
    
    'Project Work Item Status': locCompletionStatus.'Project Work Item Status',
    
    Sequence: locCompletionStatus.Sequence
    
    }
    
    );
    
    Navigate(
    
    'Add/Edit Work Item',
    
    ScreenTransition.None,
    
    {
    
    locEditWorkItem: true,
    
    locSelectedWorkItem: LookUp(
    
    'Project Work Items',
    
    'Project Work item' = GUID(Param("subEntityId"))
    
    ),
    
    locAddProject: false,
    
    locExpandProjectList: true,
    
    locProjectSortOrder: true,
    
    locSortWorkItemBy: "eta",
    
    locShowSearchWorkItem: false,
    
    locAddWorkItem: false,
    
    locProjectStatusSelection: "Milestone status",
    
    locWorkItemSortOrder: true
    
    }
    
    )
    
    ),
    
    If( //if the parameter is blank, check if the user is on a mobile device or
    desktop/web and redirect the user accordingly
    
    (!IsBlank(Param("hostClientType")) && (Param("hostClientType") = "android" Or
    Param("hostClientType") = "ios")) \|\| (IsBlank(Param("hostClientType")) &&
    Acceleration.X \> 0) Or tglAdmin_Mobile.Value,
    
    Navigate(
    
    'Mobile Projects Screen',
    
    ScreenTransition.None
    
    ),
    
    Navigate(
    
    'Projects Screen',
    
    ScreenTransition.None,
    
    {
    
    locShowFirstRun: gblFirstRun,
    
    locShowPowerAppsPrompt: gblRecordUserSettings.'Display Splash (Power Apps)' =
    'Display Splash (Power Apps) (Project User Settings)'.Yes
    
    }
    
    )
    
    )
    
    )
    
    )
    ```

## Publish the Milestones app

All the changes to the Milestones app are completed. The app can now be published by selecting the Publish to Teams button on the top right.

## Test the Power Automate flow

1. Go to Teams and open the Milestones app.

1. Open an existing work item and update the Status to a different value.

1. An Adaptive Card notification is received on the Teams channel where the app is installed.

### See also

- [Deploy Milestones sample app broad distribution app](milestones-broad-distribution.md)
- [Customize Milestones sample app](customize-milestones.md)
- [Understand Milestones sample app architecture](milestones-architecture.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]