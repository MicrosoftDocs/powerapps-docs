---
title: "Add an appointment, email, phone call, notes or task activity to the Timeline in a Model-driven app| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 02/03/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Add an appointment, email, phone call, note, or task activity to the timeline 


Add **Activities** in the **Timeline** wall to keep track of all your communications with a customer or contact. For example, you can take notes, add posts, add a task, send email, add phone call details, or set up appointments. The system automatically timestamps every activity and shows who created it. You and other people on your team can scroll through the activities to see the history as you work with a customer. 

- Activities that you add from within a record appear in the **Timeline** wall of the record. 
- If the **Regarding** field of an activity is set, the activity appears in the record it is associated with. 
- You can also choose the filter pane to filter the activities by record type and date. 
- When a new activity is created, you will get a **What you missed** notification in the **Timeline** wall.
- An email with an attached image will be shown inline with the body of the email.

  > [!div class="mx-imgBorder"]
  > ![Timeline view of activities in Power Apps](media/TimelineViewOfActivity.png "Timeline view of activities in Power Apps")

  1. Search Records
  2. Take notes
  3. Add info and activities
  4. Filter
  5. More commands
  6. Activity status
  7. Activity icons
  8. Date and time
 
## Add an activity from the nav bar
 
The fastest way to add an activity is to use the shortcut on the nav bar and then link it to a record. For example, you can create a phone call activity and then link it to a contact in the system using the **Regarding** field.

1. On the nav bar, select the **plus sign** ![Create record button](media/create-record-button.png "Create record button"), and then select **Activities**. 

   > [!div class="mx-imgBorder"]
   > ![Shortcut to add an activity in Power Apps](media/QuickCreate.png "Shortcut to add an activity in Power Apps")  
 
2. Choose the type of activity you want to add.

3. Fill in the required information. Use the **Regarding** field to associate the activity with a record.

4. When you're done, select **Save**.

 
## Add a phone call  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** wall, select  **plus sign** > **Phone Call**. 


   > [!div class="mx-imgBorder"]
   > ![Add a phone activity in Power Apps](media/addphonecall.png "Add a phone activity in Power Apps")
  
3. Fill in the **Subject** of the call.

     In the **Notes** area, provide a summary of the conversation with the customer. 
  
     The **Call To** field is automatically populated with the record you added the phone call activity to. You can select a different record if needed.  
  
4. By default, the direction is set to **Outgoing**. You can change it to **Incoming** by selecting **Outgoing**.
  
5. When you're done filling in the form, select **Save** to save the activity.  
  
## Add a task  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** wall, select  **plus sign** > **Task**.
  
3. The **Owner** field is set to the current user by default. If you want to reassign the task, select the lookup icon, and then select another user or team.  
  
4. When you're done filling in the form, select **Save** to save the activity. 
  
## Add an email  

To add an email activity to a record, you must first save the record you are adding the activity to.  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** wall, select  **plus sign** > **E-mail**. 

3. Fill in the subject of the email and use the space provided to write the email.
  
4. To add an attachment to the email, save the email. Then, in the **Attachments** section, select **+** to add an attachment.  
  
5. To use a template for the email body, on the command bar, select **Insert Template**, and then select the template. For more information on inserting an email template, see [Insert an email template](insert-email-template.md). 
  
6. When you're done filling in the form, select **Send**. 



### List emails in a conversation view

To list emails in a conversation view, go to **Settings** > **Personalization Settings** > **Email** tab and then select **Show email as a conversation on Timeline**. For more information on personal settings, see [Set personal options](https://docs.microsoft.com/powerapps/user/set-personal-options#email-tab-options). Once enabled, you can open any form that has a timeline and your emails will be grouped into conversation threads with the latest email at the top.

   > [!div class="mx-imgBorder"]
   > ![Set personal options](media/emailsettings1.png "Set personal options")
   
   > [!div class="mx-imgBorder"]
   > ![Set personal options email](media/emailsettings2.png "Set personal options for email")

  
## Add an appointment  

To add an appointment activity to a record, you must first save the record you are adding the activity to.  

> [!NOTE]
> Recurring appointments are not supported on the Dynamics 365 App for Outlook, Dynamics 365 for phones app, and when you run the model-driven apps web client on your mobile phone web browser.
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** wall, select  **plus sign** > **Appointment**.  
  
3. Use the tooltips to fill in the required information.
  
4. When you're done filling in the form, select **Save** to save the appointment.

## Add notes

You can also easily add notes in the activities area.
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** wall, start entering your notes. Use **Add an attachment** to add any attachments to the note.

3. When you're done filling in the form, select **Add Note** to save the note.


> [!NOTE]
> You can also add a note using the **plus sign** in the upper section of the **Timeline** wall.

   > [!div class="mx-imgBorder"]
   > ![Add a note](media/addnote.png "Add a note")

Once the note has been added, you can delete or edit the note. Select the note or hover the cursor on the note to see the edit and delete icons.


> [!div class="mx-imgBorder"]
> ![Update a note](media/addnote2.png "Update a note")

## Add a post 

1. Open the record that you want to add a post to. For example, a contact record.

2. In the **Timeline** wall, select  **plus sign** > **Post**. 

3. Enter your post in the text field 

4. When you're done filling in the form, select **Add** to save the post.

> [!div class="mx-imgBorder"]
> ![Update a post](media/post.png "Add a post")
  
  Once you save the post, it will appear at the top of the timeline wall.
  
## Refresh the Timeline 

You can refresh the timeline wall to see the most up to date information.

In the **Timeline** wall, select ![More button ](media/MoreButton.png "More button") and then select **Refresh Timeline**.

> [!div class="mx-imgBorder"]
> ![Refresh the Timeline ](media/refresh.png "Refresh the Timeline")


## Use the filter pane

Quickly filter activities, notes or posts in the timeline wall by record type or activity type and date using the filter pane. You can select multiple filters and filter options at the same time. You can filter and see activity due date, modified date, or by the status of the activity.

- In the **Timeline** wall, select **Open Filter Pane** funnel icon.


![Filter pane in the Timeline ](media/timeline-filter2.png "Filter pane in the Timeline") ![Filter pane in the Timeline ](media/timeline-filter5.png "Filter pane in the Timeline")


## Manage Activities
Manage activities directly from the timeline wall including assigning an activity to another person, deleting or closing an activity, add an activity to a queue, opening an associated record or editing notes and posts.

  ![Timeline command bar options](media/timeline-options1.png "Timeline command bar options")
  ![Timeline command bar options](media/timeline-options2.png "Timeline command bar options")
  ![Timeline command bar options](media/timeline-options3.png "Timeline command bar options")
  ![Timeline command bar options](media/timeline-options4.png "Timeline command bar options")

## See also

[Set up timeline control](../maker/model-driven-apps/set-up-timeline-control.md)

[FAQs for timeline control](../maker/model-driven-apps/faqs-timeline-control.md)

[FAQs about Activities and the Timeline Wall](faq-for-timeline-and-activity.md)

[Timeline section in the Customer Service Hub app](https://docs.microsoft.com/dynamics365/customer-service/customer-service-hub-user-guide-basics#timeline)
