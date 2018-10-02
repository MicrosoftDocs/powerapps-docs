---
title: "Add a appointment, email, phone call, or task activity in a Model-driven appp| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 10/01/2018
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
# Add a appointment, email, phone call, or task activity in a Model-driven app 

Use **Activities** in a Model-driven app, to keep track of your all your communication with a customer or contact. For example, you can take notes, send email, add phone call details, or set up appointments. The system automatically timestamps every activity and shows who created it. You and other people on your team can scroll through the activities to see the history as you work with a customer.

- Activities that you add from within a record appear in the **TIMELINE** area of the record. 
- If the **Regarding** field of an activity is set, the activity appears in the record it is associated with. 
- You can also choose the filter pane to filter the activities by record type and date. 
- When a new activity is created, you will get a **What you missed** notification in the **TIMELINE** area.
  
 ![Timeline view of Activities in PowerApps](user/media/TimelineViewOfActivity.png "Timeline view of Activities in PowerApps")  
 
**Add an activity from the nav bar**
 
Quickly create a new activity using the shortcut on the nav bar and then link it to a record. For example, you can create a phone call activity and then link it to a contact in the system using the **Regarding** field.

1. On the nav bar, click the **plus sign**![Create record button](user/media/create-record-button.png "Create record button"), and then click **Activities**. 

 ![Shortcut to add an Activities in PowerApps](user/media/QuickCreate.png "Shortcut to add an Activities in PowerApps")  
 
2. Choose the type of activity you want too add.

3. Fill in the required information. Use the **Regarding** field to associate the activity with a record.

4. When you're done click, **Save**.

  
## Add a phone call  
  
1.  Open the record that you want to add the activity to. For exampole, contact record.
  
2.  In the **Timeline** section, click  **plus sign** > **Phone Call**.  

![Add a Phone Activity in PowerApps](user/media/addphonecall.png "Add a Phone Activity in PowerApps")
  
3.  In the Description area, provide a summary of the conversation with the customer. You must fill in this area before you can save the phone call.  
  
     The **Call With** field is automatically populated with the customer name you select in the account or contact field. You can select a different contact, account, lead, or user record if required.  
  
4.  By default, the direction is set to **Outgoing**. You can change it to **Incoming** by clicking or tapping the **Phone Support** button in the list of case records. To select multiple records, click **Look Up More Records**, and then in the **Look Up Records** dialog box, select the records.  
  
5.  Select the **Left voice mail** check box if you make an outgoing call to a customer and leave a voice mail for them. You can also select this check box if a customer leaves a voice mail message when they call you.  
  
6.  Click **OK** to save the activity.  
  
> [!NOTE]
>  By default, every phone call activity that you add in context of a record is marked Completed when the record is saved at least once. If you do not want every phone call activity to be marked Completed by default, you can use the OrgDBOrgSetting MakeSocialPanePhoneCallCompleted and set it to **false**.  [Learn more about OrgDBOrgSettings](https://support.microsoft.com/en-us/help/2691237/orgdborgsettings-tool-for-microsoft-dynamics-crm). 
> 
>  However, if you add a phone call activity to an unsaved record, or if you create a new activity and then set the **Regarding** field of the activity to another entity record, the activity is set to an Open state. You can click the **Complete** link to close the activity as **Completed**. The **Complete** link is available only after you save the case record at least once. 
  
## Add a task  
  
1. Open the record you want to add the activity to.  
  
2. In the middle of the page, click **Activities** > **Add Task**.  
  
3. [!INCLUDE[proc_handy_infotips](../includes/proc-handy-infotips.md)]  
  
4. The **Owner** field is set to the current user by default. If you want to reassign the task, click the lookup icon, and then select another user or team.  
  
5. Click **OK** to save the task.  
  
## Add an email  
 To add an email activity to a record, you must first save the record you are adding the activity to.  
  
1. Open the record you want to add the activity to.  
  
2. In the middle of the page, click **Activities** > **More Commands**![More Commands button in Appointment Activity](../customer-service/media/morecommands.gif "More Commands button in Appointment Activity") > **Email**.  
  
3. [!INCLUDE[proc_handy_infotips](../includes/proc-handy-infotips.md)]  
  
4. To save the record, click **Save**.  
  
5. To add an attachment to the email, under **Attachments**, on the right, click **+**.  
  
6. To use a template for the email body, in the email editor, click **Insert Template**, and then select the template.  
  
7. To attach an article to the email, in the email editor, click **Insert Article**, and then add the article.  
  
8. Click **Save**.  
  
## Add an appointment  
 To add an appointment activity to a record, you must first save the record you are adding the activity to.  
  
1. Open the record you want to add the activity to.  
  
2. In the middle of the page, click **Activities** > **More Commands**![More Commands button in Appointment Activity](../customer-service/media/morecommands.gif "More Commands button in Appointment Activity") > **Appointment**.  
  
3. [!INCLUDE[proc_handy_infotips](../includes/proc-handy-infotips.md)]  
  
4. To save the record, click **Save**.  
  
## Add notes  
 You can also easily add notes in the activities area. And if you’re on the latest version of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)], you have the benefits of using OneNote to take or review customer notes from within your Dynamics 365 records. For more information on OneNote, see: [Set up OneNote integration in Dynamics 365](../admin/set-up-onenote-integration-in-dynamics-365.md).  
  
 This doesn’t replace the current Notes feature, but gives you another way to access notes stored in OneNote.  
  
 ![Add notes or OneNote notes in Dynamics 365](../customer-service/media/addnotesoronenotenotes.png "Add notes or OneNote notes in Dynamics 365")  
  
1.  Open the record you want to add the activity to.  
  
2.  In the middle of the page, click **Notes** or **OneNote**. Then do one of the following:  
  
- In the **Notes** area, start typing your notes.  
  
- In the **OneNote** area, select a notebook to make entries.  
  
  ![Add Meeting Notes in OneNote](../customer-service/media/addonenotenotes.png "Add Meeting Notes in OneNote")  
  
  > [!NOTE]
  >  The notebook is stored in the associated SharePoint folder for the record. If there is more than one associated folder, the notebook is created in the first folder. For more information see, [Set up OneNote integration in Dynamics 365](../admin/set-up-onenote-integration-in-dynamics-365.md).  
  
## Create an activity and associate it with a customer  
 You can also create an activity from the Activity area and then link it to a customer or support case.  
  
1. Go to your work area.  
  
2. [!INCLUDE[proc_activities](../includes/proc-activities.md)]  
  
3. On the command bar, select and add an activity. [!INCLUDE[proc_handy_infotips](../includes/proc-handy-infotips.md)]  
  
4. Use the **Regarding** field on the activity form to associate it with a customer or support case.  
  
### See Also  
