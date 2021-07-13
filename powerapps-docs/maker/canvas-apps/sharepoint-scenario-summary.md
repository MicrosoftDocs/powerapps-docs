---
title: Walk end-to-end through the completed SharePoint Online integration scenario
description: Take an end-to-end walk through the scenario we've built out in this series of tutorials.
author: NickWaggoner
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 06/18/2020
ms.subservice: canvas-maker
ms.author: niwaggon
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Walk end-to-end through the completed SharePoint Online integration scenario
> [!NOTE]
> This article is part of a tutorial series on using Power Apps, Power Automate, and Power BI with SharePoint Online. Make sure you read the [series introduction](sharepoint-scenario-intro.md) to get a sense of the big picture, as well as related downloads.

We have covered a huge amount of ground in this series of tutorials, from building canvas apps and flows, to creating reports and embedding them in SharePoint. We hope you've learned a lot and have enough exposure to how these technologies integrate, so that you can integrate canvas apps, flows, and reports into SharePoint based on your own needs. Before we finish, we want to walk through the scenario end-to-end and see how all the parts work together.

## Step 1: Add a project to the Project Requests list
1. In the **Project Requests** list, click or tap **All Items**, then **Project Requests app**.
   
    ![Project Requests app view.](./media/sharepoint-scenario-summary/09-00-01-view-app.png)
2. Click **Open**, which opens the app in a new browser tab.
   
    ![Open Project Requests app.](./media/sharepoint-scenario-summary/09-00-02-open-app.png)
3. In the app, click or tap ![Add item icon.](./media/sharepoint-scenario-summary/icon-add-item.png) to create a new item.
4. Fill out the form with the following values:
   
   * **Title** = "Mobile devices for design team"

   * **Approved** = "Pending"

   * **Description** = "The design team will now use Contoso-supplied devices"

   * **EstimatedDays** = "30"

   * **ProjectType** = "New hardware"

   * **RequestDate** = "03/01/2017"

   * **Requestor** = "Emily Braun"
     
     ![Project requests edit form.](./media/sharepoint-scenario-summary/09-01-01-app-new.png)
5. Click or tap ![Check mark icon.](./media/sharepoint-scenario-summary/icon-check-mark.png), then close the browser tab.
6. Go back to the **Project Requests** list, click or tap **Project Requests app**, then **All Items**.
   
    ![View all items.](./media/sharepoint-scenario-summary/09-01-01a-view-all.png)
7. Verify the new entry in the list.
   
    ![SharePoint list with new entry.](./media/sharepoint-scenario-summary/09-01-02-list-new.png)

## Step 2: Approve the project
1. When you add the item in Step 1, the flow should run and send out an approval mail. Check the inbox of the approver's email account.
   
    ![Approval request email.](./media/sharepoint-scenario-summary/09-02-01-allan-email.png)
2. Click **Approve**. The flow runs another process, and you get feedback like the following directly in the email.
   
    ![Action complete.](./media/sharepoint-scenario-summary/09-02-01a-action-complete.png)
3. Check the inbox of the requestor's email account, and you should see an approval email.
   
    ![Approval email to requestor.](./media/sharepoint-scenario-summary/09-02-02-megan-email.png)
4. Verify the updated entry in the list.
   
    ![SharePoint list with updated entry.](./media/sharepoint-scenario-summary/09-02-03-yes.png)

## Step 3: Assign a manager to the project
1. First, let's look at the **Project Details** list in SharePoint. The new project has a value of **Unassigned** in the **PMAssigned** column.
   
    ![Unassigned SharePoint list item.](./media/sharepoint-scenario-summary/09-03-01-unassigned.png)
2. In the SharePoint site, in the left navigation, click or tap **Project Management app**.
3. On the first screen, click or tap **Assign Manager**.
   
    ![Assign manager to project.](./media/sharepoint-scenario-summary/09-03-02-intro-screen.png)
4. On the **Assign Manager** screen, you see the two unassigned projects from the list. Select the **Mobile devices for design team** project.
   
    ![Unassigned project selected in app.](./media/sharepoint-scenario-summary/09-03-03-selected.png)
5. In the **Manager** text input, enter "Joni Sherman", then click **OK**.
   
    The change is applied to the list, and the gallery refreshes so only the remaining unassigned project is displayed.
   
    ![Manager assigned to project.](./media/sharepoint-scenario-summary/09-03-04-updated.png)
6. Close the app, and go back to the SharePoint list. You'll see that the project entry is now updated with the project manager name.
   
    ![Assigned SharePoint list item.](./media/sharepoint-scenario-summary/09-03-05-assigned.png)

## Step 4: Add time estimates for the project
1. Click or tap ![Back icon.](./media/sharepoint-scenario-summary/icon-back.png) to go back to the first screen, then click or tap **Update Details**.
   
    ![Update details.](./media/sharepoint-scenario-summary/09-04-00-intro-screen.png)
2. On the **View Projects** screen, enter "Mobile" in the search box.
   
    ![Search in app.](./media/sharepoint-scenario-summary/09-04-01-search-mobile.png)
3. Click ![Details arrow icon.](./media/sharepoint-scenario-summary/icon-details-arrow.png) for the **Mobile devices for design team** item.
   
    ![Select project to update.](./media/sharepoint-scenario-summary/09-04-02-select-project.png)
4. On the **Update Details** screen, set the following values:
   
   * The **Status** field = "Not started"

   * The **ProjectedStartDate** field = "3/6/2017"

   * The **ProjectedEndDate** field = "3/24/2017"

   * The **ProjectedDays** field = "15"
     
     ![Update project details.](./media/sharepoint-scenario-summary/09-04-03-update.png)
5. Click or tap ![Check mark icon.](./media/sharepoint-scenario-summary/icon-check-mark.png) to apply the change to the SharePoint list.
6. Close the app, and go back to the list. You'll see that the project entry is now updated with the date and day changes.
   
   ![Details updated in SharePoint list.](./media/sharepoint-scenario-summary/09-04-04-updated-list.png)

## Step 5: Review report data for existing projects
1. In SharePoint Online, click or tap **Site contents**, then **Site Pages**.
2. Open the **Project Analysis** page that we created earlier.
   
    ![Embedded project analysis report.](./media/sharepoint-scenario-summary/09-05-01-report-complete.png)
3. Review the variance visualization.
   
    ![Chart showing variance.](./media/sharepoint-scenario-summary/09-05-02-chart-variance.png)
   
    As we noted when we created this visualization, there is a lot more variance for projects that were run by Irvin Sayers versus Joni Sherman.
4. Drill into the visualization, and you see that much of the variance comes from two projects that took a lot longer than projected.
   
    ![Chart showing variance details.](./media/sharepoint-scenario-summary/09-05-03-chart-variance-drill.png)
5. Review the table that shows how long it takes for projects to go from approval to projected start date.
   
    ![Table showing start date differences.](./media/sharepoint-scenario-summary/09-05-04-chart-diff-completed.png)
   
    As we noted when we created this visualization, the projects that Irvin Sayers is assigned to take longer to start, with two projects taking much longer than the rest.

## Step 6: Respond to pending project delays
1. In the Power BI service, click or tap the **project-analysis** dataset, then click or tap **REFRESH NOW**. The refresh triggers the alert we set up for pending projects.
   
    ![Refresh dataset now.](./media/sharepoint-scenario-summary/09-06-01-refresh.png)
2. After the refresh is complete, the **Notification Center** at top right shows a new notification icon.
   
    ![Power BI notification center.](./media/sharepoint-scenario-summary/09-06-02-alert.png)
   
    This can take some time, so check back if you don't see it right away.
3. Open the Notification Center to see the details of the alert that fired.
   
    ![Notification for data alert.](./media/sharepoint-scenario-summary/09-06-03-notification.png)
4. Check the inbox for the person who created the alert (Megan Bowen in our case).
   
    ![Alert email from Power BI.](./media/sharepoint-scenario-summary/09-06-04-email-powerbi.png)
5. Check the inbox for the person you added in the data alerts flow (Allan DeYoung in our case).
   
    ![Alert email from Power Automate.](./media/sharepoint-scenario-summary/09-06-05-email-flow.png)
6. Now that you have information on pending projects, you can go back and approve any that have been waiting for your attention.

That brings us to the conclusion of our end-to-end walkthrough and this series of tutorials. We encourage you to continue your journey at the following sites:

* [Power Apps](https://www.powerapps.com/)
* [Power Automate](https://flow.microsoft.com)
* [Power BI](https://www.powerbi.com)
* [Power Users Community](https://powerusers.microsoft.com/)
* [SharePoint](https://sharepoint.microsoft.com)
* [Microsoft Tech Community](https://techcommunity.microsoft.com/)

Let us know in the comments if you have any feedback on this series, suggestions for additions, or ideas for additional content that will help you work with the technologies that we covered.

### See also

- [SharePoint integration scenarios](sharepoint/scenarios-intro.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]