---
title: How to make ideas editable by original creator
description: Learn about how to make ideas editable by original creator
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

# Make ideas editable by original creator

The Employee Ideas Power Apps sample app for Microsoft Teams provides a platform for employees to submit ideas for various campaigns (i.e., categories for grouping ideas around common themes).

The Employee Ideas app solution consists of two apps:

1.  [Ideas app](https://docs.microsoft.com/powerapps/teams/bulletins#manage-bulletins-app) 
    
2.  [Manage Ideas app](https://docs.microsoft.com/powerapps/teams/bulletins#bulletins-app)

With the Ideas app, Managers can setup campaigns, users can submit ideas, view other users’ ideas, and also vote for ideas that they like the best. The
experience can be customized by the admin or managers by editing campaigns, specifying justification questions that need to be answered by people submitting the ideas and also specify date threshold between which the campaign would be open for submitting ideas. The app also includes insights about who is submitting the greatest number of ideas and the most popular ideas during the week.

But what if a user wants to add more details about the idea after they submit the idea? The standard Employee Ideas app does not provide an edit button. But if you add an edit button, you will want to be careful to limit which idea a user can edit, as you would likely not want someone editing ideas that were submitted by other people.

In this topic we will learn how to enable the editing of an idea by the original creator of the idea.

> NOTE: before starting this topic, please review **How to customize Employee Ideas** (insert link).

## Prerequisites

To complete this lesson, we would need the ability to login into Microsoft Teams which will be available as part of select Microsoft 365 subscriptions and will also need to have the Employee Ideas Power Apps template for Microsoft Teams installed. This app can be installed from aka.ms/TeamsEmployeeIdeas.

## Open Employee Ideas in Power Apps

To start, let’s open the Employee Ideas app in Power Apps in Microsoft Teams

1.  Right click on the Power Apps icon on the Microsoft Teams app bar.

2.  Select the Build tab.

3.  Select the Team in which the Employee Ideas app is installed from the left navigation menu.
    
4.  Select Installed Apps and select Ideas to open the app.

5.  The Ideas app opens.

## Add an Edit button to the Campaign Details Screen

Next, let’s add a button to launch an edit screen when viewing ideas on the campaign details screen.

1.  Select the Tree view and open up the Campaign Summary Screen.

2.  Press down the Alt key and select one of the campaigns from the bottom.

3.  The Summary Detail Screen with the list of ideas in the selected campaign opens.
    
4.  Select conCampaignIdeaControls from the Tree view.

5.  Select the + Insert option and then select Button to add a new button to the container.
    
6.  Update the properties of the Button to the following

    - Name = btnCampaignIdeaControls_Edit

    - Text = "Edit"

    - ButtonType = "Primary"

    - X = Parent.Width - btnCampaignIdeaControls_Share.Width - Self.Width-30

    - Y = (Parent.Height - Self.Height) / 2

    - Width = 96

    - Height = 32

    - Visible = !locCreateNewIdea And locVisibleCampaignIdea

## Add a new screen

Next, add a screen that will be used to edit the idea selected when the edit button was selected.

1.  Select the Tree view from the left navigation.

2.  Select the New screen button to add a new screen.

3.  Select Blank layout.

4.  A new screen gets added.

5.  Rename the screen to – Edit Idea Screen.

6.  Select the Fill property of the screen and set the value to gblAppStyles.Background.Fill in the formula bar.
    
7.  Go back to the Campaign Details Screen and select the Edit button.

8. We need to get the details of the current Idea record and send to the edit screen. To do this, update the OnSelect property to the following

   ```
   OnSelect = 
   
      Clear(colResponses);
   
      Collect(
   
      colResponses,
   
      {
   
      appRef: GUID(),
   
      msft_name: "Title",
   
      msft_snapshot_sequence: -2,
   
      msft_employeeidea_responsetypecode: 'Employee Idea Response Type'.'Text
      (Single Line)',
   
      msft_responsetext: gblRecordCampaignIdea.Title,
   
      msft_responserating: Blank(),
   
      msft_snapshot_ratinghightext: "",
   
      msft_snapshot_ratinglowtext: ""
   
      },
   
      {
   
      appRef: GUID(),
   
      msft_name: "Description",
   
      msft_snapshot_sequence: -1,
   
      msft_employeeidea_responsetypecode: 'Employee Idea Response Type'.'Text
      (Multiple Lines)',
   
      msft_responsetext: gblRecordCampaignIdea.Description,
   
      msft_responserating: Blank(),
   
      msft_snapshot_ratinghightext: "",
   
      msft_snapshot_ratinglowtext: ""
   
      }
   
      );
   
      Collect(
   
      colResponses,
   
      Filter(
   
      'Employee Idea Responses',
   
      Idea.msft_employeeideaid = gblRecordCampaignIdea.msft_employeeideaid
   
      )
   
      );
   
   	Navigate('Edit Idea Screen')
   ```

   


### Add the header component

Employee Ideas leverages a header component to provide consistent menu experience between screens. We will now copy this component to our new screen so that users can navigate to the other app screens when on our new screen.

1.  Navigate to the Campaign Detail Screen.

2.  Copy the comHeader_CampaignDetail container from that screen and paste it on the new screen just added.
    
3.  Rename the container to comHeader_CampaignDetail\_EditScreen.

4.  Select the inputHeaderSettings property of the comHeader_CampaignDetail_EditScreen and paste the following formula
    
    ```
    {
    
    headerLabel: "Edit Idea",
    
    headerTooltip: "Edit Idea",
    
    headerWidth: 240,
    
    headerScreen: 'Edit Idea Screen'
    
    }
    ```
    
    
    
5.  Select inputHelpIcon property from the functions list and delete the contents from the formula bar.
    
6.  Select inputHelpScreen property from the functions list and delete the contents from the formula bar.
    
7.  There is a chance that the Link button still shows up in the header though it does not really do anything.
    
8.  To get rid of it:

    - Select the header component and go to Components tab in the Tree view.

    - Select the btnHeaderExternalLink control.

    - Select the Visible property of the control and select the whole thing – Ctrl + C – and then – Ctrl + V or just delete the last “)” and re-add it.
    
- Now when you go back to the screen, the visible property should have refreshed, and the Link button should no longer be visible.

### Add the left side navigation component

1.  Navigate back to the Campaign Detail Screen and copy the container conCampaignDetailNav.
    
2.  Come back to the Edit Idea Screen and paste the copied container.

3.  Update the following properties

    - Name = conCampaignDetailNav_EditScreen

    - Set X = 0

4.  Two errors will show up.

5.  One on imgCampaignDetail_SortGallery\_1 – DisplayMode formula.

6.  Since we copied the formula from another screen, there was a variable that checked to see if it was a new idea. Since this screen is only used for
    edit, update the DisplayMode formula to
    
    ```
    If(
    
    locVisibleCampaignView,
    
    DisplayMode.Edit,
    
    locVisibleCampaignIdea,
    
    DisplayMode.Edit,
    
    DisplayMode.Disabled
    
    )
    ```
    
7.  The other error would be on galCampaignDetailNav\_1 – DisplayMode formula.

8.  Since we copied the formula from another screen, there was a variable that checked to see if it was a new idea. Since this screen is only used for
    edit, update the DisplayMode formula to
    
    ```
    If(
    
    locVisibleCampaignView,
    
    DisplayMode.Edit,
    
    locVisibleCampaignIdea,
    
    DisplayMode.Edit,
    
    DisplayMode.Disabled
    
    )
    ```
    
    

## Add a new container for the Idea Details section

Now we will add a container that will include the idea details section on our idea edit screen.

1.  Select the newly added screen (Edit Idea Screen).

2.  Select the + Insert button from the left navigation.

3.  Select Layout -\> Container (just above the Media selection).

4.  A container gets added.

5.  Set the following properties on this container.

    - Name = conIdeaEditPane

    - X = 300

    - Y = comHeader_CampaignDetail_EditScreen.Y + comHeader_CampaignDetail_EditScreen.Height
    
    - Width = Parent.Width - conCampaignDetailNav\_1.Width
    
    - Height = Parent.Height - Self.Y
    
6.  Add another container inside this new container following steps 2 and 3 above.
    
7.  Set the following properties on this container

    - Name = conCampaignIdeaControls_EditScreen

    - X = 0

    - Y = 0

    - Width = Parent.Width

    - Height = 60

8.  Navigate to the Campaign Detail Screen and copy the controls – btnCampaignIdeaControls_Edit, btnCampaignIdeaControls_Back and
    imgCampaignIdeaControls\_Back. 
    
9.  Come back to the Edit Idea Screen and select the container added in step 6 above.
    
10. Paste the controls copied into this container.

11. Update the OnSelect property of btnCampaignIdeaControls_Back\_1 to Navigate('Campaign Detail Screen').
    
12. Select btnCampaignIdeaControls_Edit_1 and update the following properties

    - Text = “Update”

    - Visible = true

    - X = Parent.Width - Self.Width – 20

    - Y = (Parent.Height - Self.Height) / 2

    - Width = 96

    - Height = 32

13. We need to add a canvas to the new container added in step 2 above (conIdeaEditPane)
    
14. To add a canvas, add a new scrollable screen (New screen-\>Scenarios-\>Scrollable) & copy its canvas.
    
15. Then go back to the Edit Idea Screen and select the container conIdeaEditPane and paste the canvas there.
    
16. The canvas gets pasted in the container.

17. Set the following properties for the canvas

    - Name = canvasEditScreen

    - X = 0

    - Y = conCampaignIdeaControls_EditScreen.Y + conCampaignIdeaControls_EditScreen.Height
    
    - Width = Parent.Width
    
    - Height = Parent.Height - Self.Y
    
18. Now, navigate to the Campaign Detail Screen and copy the galIdeaResponses gallery.
    
19. Come back to the Edit Idea Screen and select the canvas added in the previous step.
    
20. Hit Ctrl + V to paste the gallery in the canvas.

21. The gallery gets pasted in the canvas.

22. An error may show up on the BorderThickness property of shpIdeaResponseRating_Value\_1.
    
23. Set the properties on galIdeaResponses.

    1.  BorderThickness = If((ThisItem.appRefNo \<\> ThisItem.appRatingValue),1,0)
        
    2.  X = 0
    
    3.  Y = 0
    
24.  We want to make the edit experience consistent with the new idea experience, so we will update the Items property of galIdeaResponseRating\_1 to the following

```
With(

{varRecord: ThisItem},

Table(

{

appRefNo: 1,

appRef: varRecord.appRef,

appRatingValue: varRecord.'Response Rating',

appRatingTextLow: varRecord.'Rating Text (Low)',

appRatingTextHigh: varRecord.'Rating Text (High)'

},

{

appRefNo: 2,

appRef: varRecord.appRef,

appRatingValue: varRecord.'Response Rating',

appRatingTextLow: varRecord.'Rating Text (Low)',

appRatingTextHigh: varRecord.'Rating Text (High)'

},

{

appRefNo: 3,

appRef: varRecord.appRef,

appRatingValue: varRecord.'Response Rating',

appRatingTextLow: varRecord.'Rating Text (Low)',

appRatingTextHigh: varRecord.'Rating Text (High)'

},

{

appRefNo: 4,

appRef: varRecord.appRef,

appRatingValue: varRecord.'Response Rating',

appRatingTextLow: varRecord.'Rating Text (Low)',

appRatingTextHigh: varRecord.'Rating Text (High)'

},

{

appRefNo: 5,

appRef: varRecord.appRef,

appRatingValue: varRecord.'Response Rating',

appRatingTextLow: varRecord.'Rating Text (Low)',

appRatingTextHigh: varRecord.'Rating Text (High)'

}

)

)

1.  
```

25. Update the OnSelect Property of imgIdeaResponseRating_Select\_1.

```
UpdateIf(

colResponses,

colResponses[@appRef] = ThisItem.appRef,

{msft_responserating: ThisItem.appRefNo}

);
```

26. We need to copy controls from dtcFilesImages from Campaign Detail Screen to the canvas.

![List of controls under dtcFileImages](media/make-ideas-editable-by-original-creator/controls-under-dtcfileimages-group.png "List of controls under dtcFileImages")

27. Select to expand the Edit Idea Screen.

28. Select galIdeaResponses_2 and then paste by hitting Ctrl+V.

29. A bunch of errors will pop.

![Errors on idea responses gallery](media/make-ideas-editable-by-original-creator/errors-on-idea-responses-gallery.png "Errors on idea responses gallery")

30. All except one are related to visibility of the controls, you can select the error and select Edit In Formula Bar.

31. Set the Visible property for all these to true.

32. There will be one error for lbldeaFiles_Header_2 on the Text property.

33. Update the Text property to “Attachments”.

34. Update the following property of lbldeaFiles_Header\_1.
    - Y = galIdeaResponses\_1.Y + galIdeaResponses_1.Height + 20
35. Select the Delete icon from the attachment section imgIdeaFile_Delete_1 and set the following property

    - OnSelect = Remove(colFiles,ThisItem);Collect(colRemovedFiles,ThisItem)

36. Select the Datacard that was added along with the canvas and update the following properties.

    - X = 0

    - Y = 0

    - Width = Parent.Width

    - Height = galIdeaFiles\_1.Y + galIdeaFiles\_1.Height + 20

37. Select galIdeaFiles_1 under the Datacard.

38. Select the OnSelect property and set it to Launch(ThisItem.msft_file.Value).

39. Now we will set the button to patch and update the selected idea. Select the Update button from the Edit Idea Screen – Container 3 and set the OnSelect property to the following

```
UpdateContext({locSelectedIdea: gblRecordCampaignIdea.'Employee Idea'});

Patch(

'Employee Ideas',

gblRecordCampaignIdea,

{

Title: LookUp(

colResponses,

Sequence = -2,

msft_responsetext

),

Description: LookUp(

colResponses,

Sequence = -1,

msft_responsetext

),

'Attachment Count': CountRows(

Filter(

colFiles,

appIsNew

)

)

}

);

ForAll(

RenameColumns(

Filter(

colResponses,

Sequence \>= 0,

!IsBlank('Employee Idea Response')

),

"msft\_employeeidea_responseid",

"ResponseId"

),

Patch(

'Employee Idea Responses',

LookUp(

'Employee Idea Responses',

'Employee Idea Response' = ResponseId

),

{

Instructions: ThisRecord.Instructions,

Question: ThisRecord.msft_employeeidea_questionid,

Sequence: ThisRecord.Sequence,

'Response Type': ThisRecord.'Response Type',

'Response Text': ThisRecord.'Response Text',

'Response Rating': ThisRecord.'Response Rating',

'Rating Text (Low)': ThisRecord.'Rating Text (Low)',

'Rating Text (High)': ThisRecord.'Rating Text (High)'

}

)

);

ForAll(

Filter(

colFiles,

appIsNew

),

Patch(

'Employee Idea Files',

Defaults('Employee Idea Files'),

{

Idea: gblRecordCampaignIdea,

Name: Text(ThisRecord.msft_name),

File: {

FileName: Text(ThisRecord.msft_name),

Value: ThisRecord.appFileValue

}

}

)

);

ForAll(

colRemovedFiles,

Remove(

'Employee Idea Files',

ThisRecord

)

);

Set(

gblRecordCampaignIdea,

LookUp(

'Employee Ideas',

'Employee Idea' = locSelectedIdea

)

);

ClearCollect(

colResponses,

Filter(

'Employee Idea Responses',

Idea.msft_employeeideaid = gblRecordCampaignIdea.msft_employeeideaid

)

);

ClearCollect(

colFiles,

Filter(

'Employee Idea Files',

'Employee Idea Files'[@Idea].'Employee Idea' = gblRecordCampaignIdea.'Employee
Idea'

)

);

Set(

gblRecordCampaignIdea,

LookUp(

'Employee Ideas',

'Employee Idea' = locSelectedIdea

)

);

Navigate(

'Campaign Detail Screen',

ScreenTransition.None,

{

locVisibleCampaignIdea: true,

locVisibleCampaignView: false,

locCreateNewIdea: false

}

)

## 
```

## Publish the Ideas App

1.  All the changes to the Bulletins app are completed.

2.  The app can now be published by selecting the Publish to Teams button on the top right.

## Test the app

Finally, let’s test the app and try editing an idea.

1.  Login into Teams and navigate to Team where the Ideas app is installed.

2.  Select the Ideas tab on the top.

3.  The Ideas app opens.

4.  Select on one of the Campaigns – say Workplace Safety.

5.  Open an idea that was created by your user – the idea should say who the idea was created by.
    
6.  Verify that the Edit button shows up on the Campaign Details screen.

![Select edit option on the Idea screen](media/make-ideas-editable-by-original-creator/select-edit-option-on-campaign-details-screen.png "Select edit option on the Idea screen")

7. Select the Edit button and verify that the Edit Idea screen opens.

8. Verify that all the details are displayed on the screen.

![Idea details screen](media/make-ideas-editable-by-original-creator/idea-details.png "Idea details screen")

9. Make some changes to the idea and then hit the Update button.

10. Verify that you are taken back to the Campaign Idea Details screen and all the changes you made are saved and viewable on this screen.
