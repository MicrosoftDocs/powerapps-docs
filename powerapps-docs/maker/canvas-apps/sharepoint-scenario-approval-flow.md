---
title: Create a flow to manage project approvals
description: Learn about how to create a flow that drives the process of approving projects.
author: stepsic-microsoft-com
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 06/18/2020
ms.subservice: canvas-maker
ms.author: stepsic
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Create a flow to manage project approvals
> [!NOTE]
> This article is part of a tutorial series on using Power Apps, Power Automate, and Power BI with SharePoint Online. Make sure you read the [series introduction](sharepoint-scenario-intro.md) to get a sense of the big picture, as well as related downloads.

In this task we'll create a flow that drives the process of approving projects. Power Automate is integrated with SharePoint, so it's easy to create a flow directly from a list. The flow we'll create is triggered when an item is added to the **Project Requests** list. The flow sends an email to the project approver, who approves or rejects the request directly in email. The flow then sends an approval or rejection email to the project requestor and updates our SharePoint lists appropriately.

## Step 1: Configure the flow template
1. In the **Project Requests** list, click or tap **Flow**, then **Create a flow**.
   
    ![Create a flow.](./media/sharepoint-scenario-approval-flow/03-01-01-create-flow.png)
2. In the right pane, click or tap **Start approval when a new item is added**.
   
    ![Create an approval flow.](./media/sharepoint-scenario-approval-flow/03-01-02-approval-flow.png)
3. If you're not already signed in, sign into SharePoint and Outlook, then click or tap **Continue**.
   
    ![Sign in to use template.](./media/sharepoint-scenario-approval-flow/03-01-03-continue.png)
   
    You now see the template for this flow, ready for you to complete. The boxes in the flow represent steps. They take input from previous steps, as well as input that you provide. Each step can then provide output to subsequent steps.
   
    ![Approval template.](./media/sharepoint-scenario-approval-flow/03-01-04-template.png)
4. In the **Assigned To** box, enter a name that is valid in your tenant.
   
    ![Approval email contact.](./media/sharepoint-scenario-approval-flow/03-01-05-approval-email.png)
   
    The next box in the flow responds to the project approver's decision and routes the flow to one of two *branches*: **If yes** or **If no**.
   
    ![Approval condition.](./media/sharepoint-scenario-approval-flow/03-01-06-condition.png)

## Step 2: Create actions for Approve = yes
By default, this branch sends an approval email to the requestor. We'll also update the **Project Requests** list, and add an item to the **Project Details** list because the project has been approved.

1. In the **If yes** branch, click or tap **Inform item creator of approval**, then **Edit** to see the default options for the email sent to the requestor.
   
    ![Edit email settings.](./media/sharepoint-scenario-approval-flow/03-01-07-yes-email.png)
2. By default, an email is sent to the person who created the list item, with the subject line and message body that you see. You can update these if you like.
   
    ![Change default email settings.](./media/sharepoint-scenario-approval-flow/03-01-07a-yes-email-defaults.png)
3. Click or tap **Add an Action**.
   
    ![Add an action.](./media/sharepoint-scenario-approval-flow/03-00-01-add-action.png)
4. Under **Choose an action**, search for "SharePoint", then click or tap **SharePoint – Update item**.
   
    ![Update item action.](./media/sharepoint-scenario-approval-flow/03-00-02-update.png)
5. Enter the SharePoint site URL and list name.
   
    ![Update item parameters.](./media/sharepoint-scenario-approval-flow/03-00-03-update-list.png)
6. Select the **Id** box, then click or tap **ID** in the *dynamic content* dialog box.
   
    ![List ID dynamic content.](./media/sharepoint-scenario-approval-flow/03-00-04-list-id.png)
   
    Dynamic content is available throughout the flow, based on previous steps. In this case, the SharePoint list information is available, and we can use it in the actions that we create.
7. Select the **Title** box, search for "Title" in the dynamic content dialog box, then click or tap **Title**.
   
    ![List title dynamic content.](./media/sharepoint-scenario-approval-flow/03-00-05-list-title.png)
8. In the **Approved** box, enter "Yes". This part of the flow should now look like the following image.
   
    ![Approved.](./media/sharepoint-scenario-approval-flow/03-01-08-yes-update-complete.png)
9. Click or tap **Add an Action** again. This time we'll add an item to the **Project Details** list for the project that was approved.
   
    ![Add an action.](./media/sharepoint-scenario-approval-flow/03-00-01-add-action.png)
10. Under **Choose an action**, search for "SharePoint", then select **SharePoint – Create item**.
    
    ![Create item action.](./media/sharepoint-scenario-approval-flow/03-01-09-create.png)
11. Enter the SharePoint site URL and list name.
    
    ![Create item parameters.](./media/sharepoint-scenario-approval-flow/03-01-10-yes-create-list.png)
12. Select the **Title** box, search for "Title" in the dynamic content dialog box, then click or tap **Title**.
    
    ![List title dynamic content.](./media/sharepoint-scenario-approval-flow/03-00-05-list-title.png)
13. Select the **RequestId** box, then click or tap **ID** in the dynamic content dialog box.
    
    ![List ID dynamic content.](./media/sharepoint-scenario-approval-flow/03-00-04-list-id.png)
14. In the **PMAssigned** box, enter "Unassigned". This part of the flow should now look like the following image.
    
    ![Create item complete.](./media/sharepoint-scenario-approval-flow/03-01-11-yes-create-complete.png)

## Step 3: Review action for Approve = no
By default, this branch sends a rejection email to the requestor. We'll also update the **Project Requests** list. The project isn't moving forward, so we don't add an item to the **Project Details** list.

1. In the **If no** branch, click or tap **Inform item creator of rejection**, then **Edit** to see the default options for the email sent to the requestor.
   
    ![Edit default options for email.](./media/sharepoint-scenario-approval-flow/03-01-12-no-email.png)
2. By default, an email is sent to the person who created the list item, with the subject line and message body that you see. You can update these if you like.
   
    ![Default email settings.](./media/sharepoint-scenario-approval-flow/03-01-13-no-email-defaults.png)
3. Click or tap **Add an Action**.
   
    ![Add an action.](./media/sharepoint-scenario-approval-flow/03-00-01-add-action.png)
4. Under **Choose an action**, search for "SharePoint", then click or tap **SharePoint – Update item**.
   
    ![Update item action.](./media/sharepoint-scenario-approval-flow/03-00-02-update.png)
5. Enter the SharePoint site URL and list name.
   
    ![Update item parameters.](./media/sharepoint-scenario-approval-flow/03-00-03-update-list.png)
6. Select the **Id** box, then click or tap **ID** in the dynamic content dialog box.
   
    ![List ID dynamic content.](./media/sharepoint-scenario-approval-flow/03-00-04-list-id.png)
7. Select the **Title** box, search for "Title" in the dynamic content dialog box, then click or tap **Title**.
   
    ![List title dynamic content.](./media/sharepoint-scenario-approval-flow/03-00-05-list-title.png)
8. In the **Approved** box, enter "No". This part of the flow should now look like the following image.
   
    ![Approved - No.](./media/sharepoint-scenario-approval-flow/03-01-08-no-update-complete.png)
9. At the top right of the screen, click or tap **Create flow**.
   
    The flow is now complete, and it should look like the following image if you collapse the boxes.
   
    ![Completed flow.](./media/sharepoint-scenario-approval-flow/03-01-16-flow-complete.png)

10. At the top right of the screen, click or tap **Done**.
   
    ![Done button.](./media/sharepoint-scenario-approval-flow/03-01-15a-done-button.png)

## Step 4: Run the approval flow
1. In the **Project Requests** list, click **Quick Edit** and add an item like the following:
   
   * **Title** = "New monitor for Megan"

   * **Description** = "Megan needs a 24" monitor"

   * **ProjectType** = "New hardware"

   * **RequestDate** = "02/03/2017"

   * **Requestor** = "Megan Bowen"

   * **EstimatedDays** = "1"

   * **Approved** = "Pending"

     ![Item added to list.](./media/sharepoint-scenario-approval-flow/03-02-01-list-add.png)
2. Click **Done** at the top of the page when you're finished.
   
    ![Done check mark.](./media/sharepoint-scenario-approval-flow/03-02-02-done.png)
3. Check the inbox of the approver's email account. You should have an email like the following.
   
    ![Email to Allan Deyoung.](./media/sharepoint-scenario-approval-flow/03-02-03-allan-email.png)
4. After you click **Approve** or **Reject**, the flow runs another process, and you get feedback like the following, directly in the email.
   
    ![Approval action complete.](./media/sharepoint-scenario-approval-flow/03-02-04-action-complete.png)
5. The flow sends an email to Megan with Allan's response, as in the following image. This email comes *from* Megan because she owns the flow.
   
    ![Email to Megan Bowen.](./media/sharepoint-scenario-approval-flow/03-02-05-megan-email.png)

## Next steps
The next step in this tutorial series is to [create an app to manage projects](sharepoint-scenario-build-app.md).

### See also

- [SharePoint integration scenarios](sharepoint/scenarios-intro.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]