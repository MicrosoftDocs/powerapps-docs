---
title: "Add an appointment, email, phone call, notes or task activity to the Timeline in a Model-driven app| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/07/2018
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


<!--from editor: In this file, "timeline" is sometimes all caps and sometimes title cap (Timeline). The images show it both ways, adjacent to each other. I think we should use it only one way in text and because all caps seems like shouting, I recommend just the title cap.-->


Add **Activities** in the **Timeline** area to keep track of all your communications with a customer or contact. For example, you can take notes, add a task, send email, add phone call details, or set up appointments. The system automatically timestamps every activity and shows who created it. You and other people on your team can scroll through the activities to see the history as you work with a customer.

- Activities that you add from within a record appear in the **Timeline** area of the record. 
- If the **Regarding** field of an activity is set, the activity appears in the record it is associated with. 
- You can also choose the filter pane to filter the activities by record type and date. 
- When a new activity is created, you will get a **What you missed** notification in the **Timeline** area.

  > [!div class="mx-imgBorder"]
  > ![Timeline view of activities in PowerApps](media/TimelineViewOfActivity.png "Timeline view of activities in PowerApps")  
 
**Add an activity from the nav bar**
 
The fastest way to add an activity is to use the shortcut on the nav bar and then link it to a record. For example, you can create a phone call activity and then link it to a contact in the system using the **Regarding** field.

1. On the nav bar, select the **plus sign** ![Create record button](media/create-record-button.png "Create record button"), and then select **Activities**. 

   > [!div class="mx-imgBorder"]
   > ![Shortcut to add an activity in PowerApps](media/QuickCreate.png "Shortcut to add an activity in PowerApps")  
 
2. Choose the type of activity you want to add.

3. Fill in the required information. Use the **Regarding** field to associate the activity with a record.

4. When you're done, select **Save**.

 
## Add a phone call  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** section, select  **plus sign** > **Phone Call**.  

   > [!div class="mx-imgBorder"]
   > ![Add a phone activity in PowerApps](media/addphonecall.png "Add a phone activity in PowerApps")
  
3. Fill in the **Subject** of the call.

     In the **Notes** area, provide a summary of the conversation with the customer. 
  
     The **Call To** field is automatically populated with the record you added the phone call activity to. You can select a different record if needed.  
  
4. By default, the direction is set to **Outgoing**. You can change it to **Incoming** by selecting **Outgoing**. 
  
5. When you're done filling in the form, select **Save** to save the activity.  
  
## Add a task  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** section, select  **plus sign** > **Task**.
  
3. The **Owner** field is set to the current user by default. If you want to reassign the task, select the lookup icon, and then select another user or team.  
  
4. When you're done filling in the form, select **Save** to save the activity. 
  
## Add an email  

To add an email activity to a record, you must first save the record you are adding the activity to.  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** section, select  **plus sign** > **E-mail**. 

3. Fill in the subject of the email and use the space provided to write the email.
  
4. To add an attachment to the email, save the email. Then, in the **Attachments** section, select **+** to add an attachment.  
  
5. To use a template for the email body, on the command bar, click **Insert Template**, and then select the template.   
  
6. When you're done filling in the form, select **Send**. 
  
## Add an appointment  

To add an appointment activity to a record, you must first save the record you are adding the activity to.  
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** section, select  **plus sign** > **Appointment**.  
  
3. Use the tooltips to fill in the required information.
  
4. When you're done filling in the form, select **Save** to save the appointment.

## Add notes

You can also easily add notes in the activities area.
  
1. Open the record that you want to add the activity to. For example, a contact record.
  
2. In the **Timeline** section, start entering your notes. Use **Add an attachment** to add any attachments to the note.

3. When you're done filling in the form, select **Add Note** to save the note.

   > [!div class="mx-imgBorder"]
   > ![Add a note](media/addnote.png "Add a note")

Once the note has been added, you can delete or edit the note. You can also add a note using the **plus sign** in the upper section of the **TIMELINE** area.

> [!div class="mx-imgBorder"]
> ![Update a note](media/addnote2.png "Update a note")
  
  
