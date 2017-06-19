<properties
   pageTitle="Create an app to manage projects  | Microsoft PowerApps"
   description="In this task, we'll build an app from scratch. This app allows a user to assign a manager to projects and to update project details."
   services=""
   suite="powerapps"
   documentationCenter="na"
   authors="mgblythe"
   manager="anneta"
   editor=""
   tags=""/>
<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="06/12/2017"
   ms.author="mblythe"/>

# Create an app to manage projects 

**Note:** This article is part of a tutorial series on using PowerApps, Microsoft Flow, and Power BI with SharePoint Online. Make sure you read the [series introduction](sharepoint-scenario-intro.md) to get a sense of the big picture, as well as related downloads.

In this task, we'll build an app from scratch. This app allows a user to assign a manager to projects and to update project details. You will see some of the same controls and formulas you saw in the first app, but you will build more of the app yourself this time. The process is more complex, but you'll learn more, so we think it's a fair trade-off.

**Tip:** The [download package](https://aka.ms/o4ia0f) for this scenario includes a finished version of this app: project-details-app.msapp.

## Quick review of PowerApps Studio

You used PowerApps Studio for web in the last task, but we want to make sure you understand all the parts before we move on. You can continue to work in PowerApps Studio for web, or you can use [PowerApps Studio for Windows](https://aka.ms/powerappswin).

PowerApps Studio has three panes and a ribbon that make app creation feel like building a slide deck in PowerPoint:

1. Left navigation bar, which shows thumbnails of all the screens in your app and a tree view of all the app's controls

2. Middle pane, which contains the app screen you are working on

3. Right-hand pane, where you set options like layout and data sources

4. Property drop-down list, where you select the properties that formulas apply to

5. Formula bar, where you add formulas (like in Excel) that define app behavior

6. Ribbon, where you add controls and customize design elements

![PowerApps Studio](./media/sharepoint-scenario-build-app/04-00-00-powerapps-studio.png)

## Step 1: Create screens

With that review out of the way, let's start building an app. In this step, we'll create four blank screens for the app. We'll build these screens out in later steps.

| **Screen**        | **Purpose**                                       |
|-------------------|---------------------------------------------------|
| **SelectTask**    | Opening screen; navigate to other screens         |
| **AssignManager** | Assign a manager to an approved project           |
| **ViewProjects**  | View a list of projects, with summary information |
| **UpdateDetails** | View and update the details for a project         |

1. In PowerApps Studio, click or tap **New**, then under **Blank app**, click or tap **Phone Layout**.

    ![Blank app - phone layout](./media/sharepoint-scenario-build-app/04-01-01-blank-phone-app.png)

2. Save the app to the cloud:

    1. Click or tap **File**, which opens to an **App settings** tab. Enter the name "Project Management app".

       ![App name](./media/sharepoint-scenario-build-app/04-01-02-app-name.png)

    2. Click or tap **Save as**, verify that app will save to the cloud, then click **Save** in the lower right corner.

        ![Save to the cloud](./media/sharepoint-scenario-build-app/04-01-03-save-to-cloud.png)

    3. Click or tap ![Back to app icon](./media/sharepoint-scenario-build-app/icon-back-to-app.png) to go back to the app.


3. On the **Home** tab, click or tap **Screen1,** then rename the screen to **SelectTask**.

    ![Rename screen](./media/sharepoint-scenario-build-app/04-01-04-rename-screen.png)

4. Create and rename additional screens:

    1. On the **Home** tab, click or tap **New screen**, then rename that screen to **AssignManager**.

    2. Repeat the previous step for the other screens: **ViewProjects** and **UpdateDetails**.

    The app should now look like the following image.

    ![All app screens](./media/sharepoint-scenario-build-app/04-01-05-all-screens.png)

## Step 2: Connect to a SharePoint list

In this step, we'll connect to the **Product Details** SharePoint list. We only use one list in this app, but you could easily connect to both if you want to extend the app.

1. In the left navigation bar, click or tap the **SelectTask** screen.

2. In the middle pane, click or tap **connect to data**.

    ![Connect to data](./media/sharepoint-scenario-build-app/04-02-01-connect.png)

3. In the right pane, click or tap **New connection**.

    ![New connection](./media/sharepoint-scenario-build-app/04-02-02-new-connection.png)

4. Click or tap **SharePoint**, then **Connect**.

    ![SharePoint connection](./media/sharepoint-scenario-build-app/04-02-03-sharepoint-connection.png)

5. Enter a SharePoint URL, then click or tap **Go**.

    ![SharePoint URL for connection](./media/sharepoint-scenario-build-app/04-02-04-sharepoint-url.png)

6. Select the **Project Details** list, then click or tap **Connect**.

    ![Select Project Details list](./media/sharepoint-scenario-build-app/04-02-05-sharepoint-lists.png)

    The **Data sources** tab in the right pane now shows the connection that you have created.

    ![Data sources tab](./media/sharepoint-scenario-build-app/04-02-06-data-sources.png)

## Step 3: Build the SelectTask screen

In this step, we'll provide a way to navigate to the other screens in the app - working with some of the controls, formulas, and formatting options that PowerApps provides.

### Update the layout for the screen

1. In the left navigation bar, click or tap the **SelectTask** screen.

2. On the **Home** tab, click or tap **Layout**, then select the layout at top left.

    ![Select layout](./media/sharepoint-scenario-build-app/04-03-01-select-layout.png)

3. In the middle pane, select the default **[Title]**, then in the formula bar, update the **Text** property to "Contoso Project Management".

    ![Text property in formula bar](./media/sharepoint-scenario-build-app/04-03-02-text-property.png)

### Insert introductory text

1. On the **Insert** tab, click or tap **Text box**, then drag the text box down below the top banner.

    ![Add label](./media/sharepoint-scenario-build-app/04-03-03-text-default.png)

2. In the formula bar, set the following properties for the text box:

    - **Color** property = **DarkGray**

    - **Size** property = **18**

    - **Text** property = "**Click or tap a task to continue..."**

    ![Update label text](./media/sharepoint-scenario-build-app/04-03-04-text-updated.png)

### Add two navigation buttons

1. On the **Insert** tab, click or tap **Button**, then drag the button below the text box.

    ![Add button](./media/sharepoint-scenario-build-app/04-03-05-button-default.png)

2. In the formula bar, set the following properties for the button:

    - **OnSelect** property = **Navigate(AssignManager, Fade)**. When you run the app and click this button, you navigate to the second screen in the app, with a fade transition between the screens.

    - **Text** property = **"Assign Manager"**

3. Resize the button to accommodate the text.

    ![Update button text](./media/sharepoint-scenario-build-app/04-03-06-button-updated.png)

4. Copy the button and paste it below the first one, so you can create a second button with some different properties.

    ![Copy buttons](./media/sharepoint-scenario-build-app/04-03-07-buttons-copied.png)

5.  Set the following properties for the second button:

    - **OnSelect** property = **Navigate(ViewProjects, Fade)**.

    - **Text** property = **"Update Details"**

    ![Update button text](./media/sharepoint-scenario-build-app/04-03-08-buttons-final.png)

### Run the app

The app doesn't do a lot yet, but you can run it if you like:

1. Click or tap the **SelectTask** screen (the app always starts from the selected screen).

2. Click or tap ![Run app icon](./media/sharepoint-scenario-build-app/icon-run-arrow.png) in the upper right corner to run the app.

3. Click or tap one of the buttons to navigate to another screen.

4. Click or tap ![Close app preview icon](./media/sharepoint-scenario-build-app/icon-close-preview.png) in the upper right corner to close the app.

## Step 4: Build the AssignManager screen 

In this step, we'll add a gallery to display all projects that have been approved but don't yet have a manager. We'll add other controls, so you can assign a manager.

**Note:**  We'll build a page later in the app that allows you to edit all fields for a project (including the manager field), but we thought it would be cool to show you how to build a screen like this one as well.

1. Save the changes you've made so far.

2. In the left navigation bar, click or tap the **AssignManager** screen.

### Update the layout for the screen

1. Change the layout style to include a blue bar at the top.

2. Change **[Title]** to **Assign Manager**.

3. Add a text box with the following properties:

    - **Color** property = **DarkGray**

    - **Size** property = **18**

    - **Text** property = "**Select a project, then assign a manager"**

    ![Assign manager layout](./media/sharepoint-scenario-build-app/04-04-01-layout.png)

### Add a back arrow to return to the SelectTask screen

1. Click or tap the blue bar at the top of the screen.

2. On the **Insert** tab, click or tap **Icons**, then click or tap **Left**.

    ![Insert left arrow](./media/sharepoint-scenario-build-app/04-04-02-icon-left.png)

3. Move the arrow to the left side of the blue bar, and set the following properties:

    - **Color** property = **White**

    - **Height** property = **40**

    - **OnSelect** property = **Navigate(SelectTask, Fade)**

    - **Width** property = **40**

    ![Add back button](./media/sharepoint-scenario-build-app/04-04-03-left-arrow.png)

### Add and modify a gallery

1. On the **Insert** tab, click or tap **Gallery**, then **Text gallery** – **Vertical**.

    ![Add a text gallery](./media/sharepoint-scenario-build-app/04-04-04-gallery.png)

    The gallery is inserted with default text.

    ![Gallery with default text](./media/sharepoint-scenario-build-app/04-04-05-gallery-default.png)

2. Set the following properties for the gallery:

    - **BorderThickness** property = **1**

    - **BorderStyle** property = **Dotted**

    - **Items** property = **Filter('Project Details', PMAssigned="Unassigned")**. Only projects with no manager assigned are included in the gallery.

    ![Gallery with text from list](./media/sharepoint-scenario-build-app/04-04-06-gallery-updated.png)

3. In the right pane, update the fields to match the following list:

    - **ApprovedDate**

    - **Title**

    - **Status**

    ![Gallery fields](./media/sharepoint-scenario-build-app/04-04-07-gallery-fields.png)

4. Select the title in the first gallery item, and set the following properties:

    - **Size** property = **16**.

    - **FontWeight** property = **Bold**

5. Resize text boxes in the gallery as appropriate. The screen should now look like the following image.

    ![Formatted gallery](./media/sharepoint-scenario-build-app/04-04-07-gallery-size-text.png)

### Change the color of an item if it's selected

1. Select the gallery, then set the **TemplateFill** property to **If (ThisItem.IsSelected=true, Orange, White)**.

2. Select an item in the gallery. The screen should now look like the following image.

    ![Gallery with selected item](./media/sharepoint-scenario-build-app/04-04-08-gallery-selected.png)

### Add a text box, text input, and OK button to submit manager assignments

1.  Click or tap outside the gallery you've been working on.

2.  On the **Insert** tab, click or tap **Text box**. Drag the button below the gallery, to the left. Set the following properties for the text box:

    - **Size** property = **20**

    - **Text** property = **"Manager:"**

    ![Add Manager label](./media/sharepoint-scenario-build-app/04-04-09-controls-text.png)

3.  On the **Insert** tab, click or tap **Text**, then **Text input**. Drag the text input below the gallery, in the center. Set the following properties for the drop down:

    - **Height** property = **60**

    - **Size** property = **20**

    - **Width** property = **250**

    ![Add text input](./media/sharepoint-scenario-build-app/04-04-10-controls-text-box.png)

4.  On the **Insert** tab, click or tap **Button**. Drag the button below the gallery, to the right. Set the following properties for the button:

    - **Height** property = **60**

    - **OnSelect** property = **Patch('Project Details', LookUp('Project Details', ID = Gallery1.Selected.ID), {PMAssigned: TextInput2.Text})**. For more information, see [Formula deep-dive](#formula-deep-dive).

    - This formula updates the **Project Details** list, setting a value for the PMAssigned field.

    - **Size** property = **20**

    - **Text** property = **"OK"**

    - **Width** property = **80**

    ![Add OK button](./media/sharepoint-scenario-build-app/04-04-11-controls-button.png)

The completed screen should now look like the following image.

![Finished Assign Manager screen](./media/sharepoint-scenario-build-app/04-04-12-complete.png)

## Step 5: Build the ViewProjects screen

In this step, we'll add a gallery to the **ViewProjects** screen, like the gallery in the first app that we generated. This gallery provides a lot of functionality with minimal effort. The gallery displays items from the **Project Details** list. You select an item on this screen, then you edit the details on the **UpdateDetails** screen.

1. In the left navigation bar, click or tap the **ViewProjects** screen.

2. On the **Home** tab, click or tap **Layouts**, then select the layout you see in the following image.

    ![Select layout](./media/sharepoint-scenario-build-app/04-05-01-layout-v.png)

    PowerApps builds a complete screen, and inserts a gallery with default text.

3. In the blue bar at the top of the app, click or tap **[Title]**. In the formula bar, set the **Text** property to **"View Projects"**.

    ![View Projects gallery](./media/sharepoint-scenario-build-app/04-05-02-gallery-default-v.png)

4. Select the refresh button ![Refresh icon](./media/sharepoint-scenario-build-app/icon-refresh.png), and set its **OnSelect** property to **Refresh('Project Details')**.

5.  Select the new item button ![Add new icon](./media/sharepoint-scenario-build-app/icon-add-item.png), and set its **OnSelect** property to **NewForm(Form2); Navigate(UpdateDetails, ScreenTransition.None)**.

### Add a back arrow to return to the SelectTask screen

1. Click or tap the blue bar at the top of the screen.

2. On the **Insert** tab, click or tap **Icons**, then click or tap **Left**.

    ![Insert left arrow](./media/sharepoint-scenario-build-app/04-05-03-icon-left-v.png)

3. Move the arrow to the left of the refresh button in the blue bar, and set the following properties:

    - **Color** property = **White**

    - **Height** property = **40**

    - **OnSelect** property = **Navigate(SelectTask, Fade)**

    - **Width** property = **40**

    ![Back button](./media/sharepoint-scenario-build-app/04-05-04-left-arrow-v.png)

### Change the data source for the BrowseGallery2 gallery

1. Select the **BrowseGallery2** gallery

    ![View Projects gallery](./media/sharepoint-scenario-build-app/04-05-05a-gallery-selected-v.png)

2. Set the **Items** property of the gallery to **SortByColumns(Filter('Project Details', StartsWith(Title, TextSearchBox1.Text)), "Title", If(SortDescending1, Descending, Ascending))**.

    This sets the data source of the gallery to the **Project Details** list, and uses the **Title** field for search and sort.

3. Select the ![Details arrow icon](./media/sharepoint-scenario-build-app/icon-details-arrow.png) in the first gallery item, and set the **OnSelect** property to **Navigate(UpdateDetails, None)**.

    ![ View Projects gallery - first item selected](./media/sharepoint-scenario-build-app/04-05-05b-gallery-arrow-v.png)

4. In the right pane, update the fields to match the following list:

    - **Status**

    - **Title**

    - **PMAssigned**

    ![Gallery fields](./media/sharepoint-scenario-build-app/04-05-06-gallery-fields.png)

    The completed screen should now look like the following image.

    ![View Project screen finished](./media/sharepoint-scenario-build-app/04-05-07-viewprojects-final.png)

## Step 6: Build the UpdateDetails screen

In this step, we'll add an edit form and related controls to the **UpdateDetails** screen. On this screen, you edit details for a project that you selected on the **View Projects** screen.

### Update the layout for the screen

1. In the left navigation bar, click or tap the **UpdateDetails** screen.

2. Update the screen layout like you did for the **AssignManager** screen:

    1. Change the layout style to include a blue bar at the top.

    2. Change **[Title]** to **Update Details**.

### Add an edit form to the screen

1. On the **Insert** tab, click or tap **Forms**, then **Edit**.

    ![Insert edit form](./media/sharepoint-scenario-build-app/04-06-01-insert-edit-form.png)

2. Drag the form below the blue bar, then drag the bottom handle so the form covers the rest of the screen.

    ![Blank edit form](./media/sharepoint-scenario-build-app/04-06-02-blank-edit-form.png)

3. Set the following properties for the form:

    - **DataSource** property = **'Project Details'**

    - **Item property** = **BrowseGallery2.Selected**

4. With the form still selected, in the right pane click or tap the eye icon for each field in the following order:

    - **Title**

    - **PMAssigned**

    - **Status**

    - **ProjectedStartDate**

    - **ProjectedEndDate**

    - **ProjectedDays**

    - **ActualDays**

    ![Edit form fields](./media/sharepoint-scenario-build-app/04-06-03-edit-fields.png)

### Add controls to submit and reset the form

1. Click or tap the blue bar at the top of the screen.

2. On the **Insert** tab, click or tap **Icons**, then click or tap **Check**.

    ![Insert check mark](./media/sharepoint-scenario-build-app/04-06-04-check.png)

3. Move the check mark to the right of the blue bar, and set the following properties:

    - **Color** property = **White**

    - **Height** property = **40**

    - **OnSelect** property = **Submit(Form2)**. Because we're using the edit form control, we can use **Submit()** and other simple functions, instead of using **Patch()** like we did earlier.

    - **Width** property = **40**

4. On the **Insert** tab, click or tap **Icons**, then click or tap **Cancel**.

    ![Insert cancel mark](./media/sharepoint-scenario-build-app/04-06-05-cancel.png)

5. Move the cancel icon to the left of the blue bar, and set the following properties:

    - **Color** property = **White**

    - **Height** property = **40**

    - **OnSelect** property = **ResetForm(Form2); Back()**. This resets the form to its original values, and navigates back to the **ViewProjects** screen.

    - **Width** property = **40**

The completed screen should now look like the following image (if the fields are blank, make sure you select an item on the **View Projects** screen).

![Update Details screen finished](./media/sharepoint-scenario-build-app/04-06-06-edit-final.png)

## Step 7: Run the app

Now that the app is complete, let's run it to see how it works. We'll add a link on the SharePoint site to the app. You will be able to run the app in the browser, but you might need to share the app for other people to run it. For more information, see [Share your apps](https://powerapps.microsoft.com/guided-learning/learning-manage-share-apps).

First, we'll assume the role of the project approver - we'll look for any projects that don't have a manager assigned, and assign a manager to one of the projects. Then we'll assume the role of the project manager, and add some information about a project that is assigned to us.

### Add a link to the app

1. In the Office 365 app launcher, click or tap **PowerApps**.

    ![PowerApps in Office 365 app launcher](./media/sharepoint-scenario-build-app/04-07-02a-waffle.png)

2. In PowerApps, click or tap **Project Management app**.

    ![Select Project Management app](./media/sharepoint-scenario-build-app/04-07-02b-select-app.png)

3. Copy the address (URL) for the app in the browser.

    ![Copy app URL](./media/sharepoint-scenario-build-app/04-07-02ba-copy-url.png)

4. In SharePoint, click or tap **EDIT LINKS**.

    ![Edit SharePoint site links](./media/sharepoint-scenario-build-app/04-07-02c-edit-links.png)

5. Click or tap **(+) link**.

    ![Add app link to SharePoint site](./media/sharepoint-scenario-build-app/04-07-02d-add-link.png)

6. Enter "Project Management app", and paste in the address for the app.

    ![Edit link properties](./media/sharepoint-scenario-build-app/04-07-02e-link-dialog.png)

7. Click or tap **OK**, then **Save**.

    ![Save link changes](./media/sharepoint-scenario-build-app/04-07-02f-save.png)

### Assign a manager to a project

1. First, let's look at the **Project Details** list in SharePoint. Two projects have a value of **Unassigned** in the **PMAssigned** column. We will see these in the app.

    ![Unassigned projects in SharePoint list](./media/sharepoint-scenario-build-app/04-07-01-unassigned.png)

2. Click or tap the link that you created to the app.

3. On the first screen, click or tap **Assign Manager**.

    ![App intro screen](./media/sharepoint-scenario-build-app/04-07-03-intro-screen.png)

4. On the **Assign Manager** screen, you see the two unassigned projects from the list. Select the **New BI software** project.

    ![Gallery with item selected](./media/sharepoint-scenario-build-app/04-07-04-selected.png)

5. In the **Manager** text box, enter "Joni Sherman", then click **OK**.

    The change is applied to the list, and the gallery refreshes so only the remaining unassigned project is displayed.

    ![Assign manager to project](./media/sharepoint-scenario-build-app/04-07-05-updated.png)

6. Go back to the SharePoint list. You'll see that the project entry is now updated with the project manager name.

    ![Project manager assigned in SharePoint list](./media/sharepoint-scenario-build-app/04-07-07-assigned.png)

### Update details for the project

1.  Click or tap ![Back icon](./media/sharepoint-scenario-build-app/icon-back.png) to go back to the first screen, then click or tap **Update Details**.

    ![App intro screen](./media/sharepoint-scenario-build-app/04-07-08-intro-screen.png)

2.  On the **View Projects** screen, enter "New" in the search box.

    ![Search in app gallery](./media/sharepoint-scenario-build-app/04-07-09-search-new.png)

3.  Click ![Details arrow icon](./media/sharepoint-scenario-build-app/icon-details-arrow.png) for the **New BI software** item.

    ![Gallery item selected](./media/sharepoint-scenario-build-app/04-07-10-select-project.png)

4.  On the **Update Details** screen, set the following values:

    - The **Status** field = "Not started"

    - The **ProjectedStartDate** field = "3/6/2017"

    - The **ProjectedEndDate** field = "3/24/2017"

    - The **ProjectedDays** field = "15"

    ![Update item details](./media/sharepoint-scenario-build-app/04-07-11-update.png)

5. Click or tap ![Check mark icon](./media/sharepoint-scenario-build-app/icon-check-mark.png) to apply the change to the SharePoint list.

6. Close the app, and go back to the list. You see that the project entry is now updated with the date and day changes.

    ![Updated SharePoint list](./media/sharepoint-scenario-build-app/04-07-11-updated-list.png)

## Formula deep-dive (2) - optional

This is the second optional section on PowerApps formulas. In the first deep-dive, we looked at one of the formulas that PowerApps generates for the browse gallery in a three-screen app. In this deep-dive, we'll look at a formula that we use for the **AssignManager** screen of our second app. Here's the formula:

**Patch ( 'Project Details', LookUp ( 'Project Details', ID = Gallery1.Selected.ID ), {PMAssigned: TextInput2.Text} )**

What does this formula do? When you select an item in the gallery and click the **OK** button, the formula updates the **Project Details** list, setting the **PMAssigned** column to the value that you specify in the text box. The formula uses functions to do its work:

- The [**Patch** function](functions/function-patch.md) modifies one or more records of a data source.

- The [**LookUp** function](functions/function-filter-lookup.md) finds the first record in a table that satisfies a formula.

When you put the functions together in the formula, here's what happens:

1. When you click the **OK** button, the **Patch** function is called to update the **Project Details** list.

2. Within the **Patch** function, the **LookUp** function identifies which row of the **Project Details** list to update. It does this by comparing the ID of the selected gallery item to the ID in the list. For example, an ID of 12 means that the entry for **New BI software** should be updated.

3. Now that the **Patch** function has the right ID, it updates the **PMAssigned** field to the value in **TextInput2.Text**.

## Next steps

The next step in this tutorial series is to [create a Power BI report to analyze projects](sharepoint-scenario-build-report.md).
