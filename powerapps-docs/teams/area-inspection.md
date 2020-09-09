# Document Objective

In this tutorial, learn about the **Area Walk** (User) and **Area Walk** (Manager) apps, and how to use them effectively.

## Overview

**Area Inspection** consists of two different apps, one app for the users, and another app for the manager.

1. Area Walk (User) app

    This app is used by employees to perform the following actions:

    - Inspect an area within a building or other location in the course of
    completing their job. The app provides inspection checklists so that
    multiple areas can be inspected. For example, a store employee can use this app to inspect a section of a retail store to verify that the store is ready to open for the day.
    - When an issue is found during the inspection, the employee can log the issue and assign it to the right person so that it can be resolved quickly.

1. Area Walk (Manager) app

    This app is used by a manager to perform the following actions:

    - Configure area walk forms and define outcome
    - Gain visibility to inspection results and issue status.
    - Ensure that all identified issues have been addressed by the staff.
    - Identify repeat issues from prior area walks and analyze root cause and prevent them from happening in future.

## Area Walk Manager app

Manager app gives the manager the following capabilities.

- Configure the app
- Edit the app configuration
- Add area types
- Add areas
- Add inspection forms

### App configuration

To configure the app:

1. Sign in to Teams.

1. Select the team.

1. Go to the **Area Walks (Manager)** tab.

1. Select the *Channel* where the messages will be posted.

1. (Optional) Select the *Tasks* (Planner) instance to integrate the app with Planner.

1. Select **Continue** if you selected a *Tasks* (Planner) instance in the previous step, otherwise select **Skip**.

    ![Integrate with channel and planner](media/channel-planner-integrate.png "Integrate with channel and planner")

1. If you selected **Continue** in the previous step, follow the steps provided on the page (Steps 1 and 2) to get the SharePoint site URL. And then, paste the URl in *Step 3* input box.

1. Select **Let's go** if you entered a SharePoint site URL in the previous step, otherwise select **Skip** to use the app without SharePoint integration.
Select **Back** if you want to go back to the previous screen.

    ![Configure image storage](media/configure-storage.png "Configure image storage")

### Edit app configuration

To edit the app configuration:

1. Go to the **Area Walk (Manager)** tab in Teams.

1. Select ![Teams settings](media/teams-settings.png "Teams settings") on the top-right corner.

1. Select **General** from the settings menu.

1. Change the required settings.

1. Select **Save**.

    ![Edit app configuration](media/edit-app-configuration.png "Edit app configuration")

### Add area types

To start with the Area Walk App, you'll need to add area types first. The area types define the classes of different areas that can be added to the app for inspection.

To add the area types:

1. Go to the **Area Walk (Manager)** tab in Teams.

1. Select **Areas** tab inside the app.

1. Select ![Teams settings for areas](media/teams-settings.png "Teams settings for areas") on the top-right corner.

1. Select **Area type** from the left-pane inside the app.

1. Add, update, or delete area types as required. Examples: Interior, Food, Shopping.
   <br> For each area, you can enter *Title*, *Menu label*, and update icon.

1. Select **Save**.

    ![Add area type](media/add-area-type.png "Add area type")

### Add areas

Areas are the portions that needs to be inspected.

To add reas:

1. Go to the **Area Walk (Manager)** tab in Teams.

1. Select **Add area** from the left-pane inside the app.

>   3. In the form that opens, fill in the area details such as the **Title**
>   and select **Area Type** from the dropdown.

>   4. Click on **Save.**

![](media/1f023be9ded28396fe55bff661370b89.png)

Adding Inspection Forms
-----------------------

Inspections forms are tied to area types. You can define more than one
inspection form for each area type. Also each inspection form can be tied to
more than one area types.

>   Steps to add Inspection Forms:

1.  Go to **Area Walk (Manager)** tab in Teams.

2.  Select **Inspection Forms** tab.

3.  Click on **+ Add a form** to create a new Inspection form.

    1.  Add Title

    2.  Add Associated Area Types

    3.  Add Checklist steps using **+Add step**

4.  Use **copy** icon to copy a step

5.  Use **delete** icon to delete a step

6.  Use **up and down arrows** to change the sequence of the steps

>   You can enter one or more checklist steps for the inspection form. Each
>   checklist step can have a Title, Detailed Instructions, and an Image. Each
>   checklist item can also have up to three action buttons associated,
>   reflecting "Ok", "Issue" and "Not Applicable" outcomes. The labels of the
>   buttons can be customized.

![](media/55b5c55e08e3afaf6db58a5e72f7a776.png)

Area Walk User App
==================

User App – Enables users to Complete a full inspection of the areas as and when
required in their job.

>   (note: To run the installed app, select 'Area Walk' app from the available
>   tabs inside the Teams channel.)

>   The detailed steps on how to create an inspection is given below:

User lands to Home screen on opening the app
--------------------------------------------

![](media/561c5ccfe8cdf392523ceabe4273f398.png)

1.  App will Great you based on your Time "Good \<Morning/Afternoon/Evening\>,
    \<Your Name\>.

2.  The statistics of the planner tasks.

3.  The statistics of all inspections for last 7 days

>   **Note:** If the Planner is not selected from the manager App, users will be
>   not be able to view Planner task Statistics and will see below screen when
>   clicked on **Open Tasks**. On Seleting **Close**, the user will navigate to
>   previous Screen

![](media/d89bce19d65d7f6b4cfa5a6e11a2b773.png)

Choose the Area that needs to be inspected
------------------------------------------

>   On click of Inspect an Area, it navigates to the next screen which allows
>   user to select the area that needs to be inspected.

![](media/491ff593d268bcadb845eeb008f5dcc3.png)

1.  Search box: Searches for Areas based on the area type selected.

2.  Area types: Lists all the area types with and additional option "All"
    selected by default

3.  Areas: Lists all the areas based on selected area, if "All" is selected, all
    the areas are listed by default.

User chooses the inspection form
--------------------------------

If there are more than one inspection form associated to the area type, the app
allows user to choose one of the inspection forms, else the app directly
navigates to Inspection overview page

![](media/eb7330b9cb7ca293dd05ef5e2d373eed.png)

Inspection overview page 
-------------------------

This page shows the image of the area with number or checklist completed vs
total number of checklist steps in the form.

![](media/8ec813744858eb27b222ffd9699036a4.png)

1.  List of checklist steps for the form selected as per configuration in the
    manager app.

>   User must click on 'Begin Inspection' button or any of the checklist item to
>   start the inspection.

Inspection Form Page
--------------------

The user must fill in details and click on Review inspection

![](media/cda6a1a1c6fc6bb1d944e6110b579af3.png)

![](media/8a6d212dcb9095751058fb4e2e5cdf84.png)

1.  Checklist instruction: The instructions configured in the manager app is
    displayed here

2.  Checklist outcome: User must select either OK(gets highlighted in Green),
    Issue(gets highlighted in Red) or N/A(gets highlighted in Grey) from the
    inspection list against each checklist.

3.  Add details: User can add/capturing pictures by using **Photo** option ,
    Also add note by using **Note option** or add Planner Tasks by using
    **Task** option.

Adding a Planner Task to an Inspection step.
--------------------------------------------

User can add task which will automatically create a planner task in the teams
which is viewed by Store staff and the store staff is responsible for completing
this task.

1.  Click on the **Task** at Checklist step

2.  The Images and Notes will get populated on the task.

3.  Add addional images using **Add Photos** or delete the unwanted images by
    clicking on any image

4.  Click on **Assign** to search for the User(s) for whom you wanted to assign
    the task.

5.  Select a due date

6.  Update the description if required

7.  Click on **Add Task**

![](media/8a317fd05fc564ea68cd39172fd51563.png)

**Note:** If the Planner is not selected from the manager App, users will be not
b able to create tasks and will see belo screen when clicked on **Task** from
Checklist Step. On Seleting **Close**, the user will navigate to previous Screen

![](media/d89bce19d65d7f6b4cfa5a6e11a2b773.png)

Review inspection 
------------------

User can click on the checklist step to go back to the previous screen and
modify the outcome or click on "Submit Inspection" to submit inspection.

![](media/416657344886c4a357f1ef696c46a05a.png)

![](media/2f23e89e8c4b75c41d499c3cae689d8f.png)

Once inspection is submitted, the app navigates to next screen which shows the
status of the submission and list of all the areas of the current area type.
