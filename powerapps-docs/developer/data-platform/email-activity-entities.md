---
title: "Email activity tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The email activity in lets you track and manage email communications with customers." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Email activity tables

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The email activity lets you track and manage email communications with customers. Microsoft Dataverse includes the Email Router software that manages the routing of email to or from Dataverse. The email activity is delivered using email protocols. Email Router supports the following email protocols: Exchange Web services, POP3, and SMTP. In addition to the Email Router software, the email activity can also be delivered by using Dynamics 365 for Outlook.  
  
<a name="Actions"></a>   

## Actions on an email activity  
 Using Dataverse web services, you can perform the following actions on an email activity:  
  
- Create, retrieve, update, and delete the email activity.  
  
- Send email messages, or send email messages by using email templates (`Template`). For more information about email templates, see [Template table](/reference/entities/template.md).  
  
- Attach files as attachments by using the (`ActivityMimeAttachment`) attribute in the email message.  
  
- Send mass or bulk email messages.  
  
- Configure incoming email messages to be delivered from Microsoft Exchange Server to any user or queue, or outgoing messages to be sent from any user or queue to Microsoft Exchange Server.  
  
   If the `Organization.RequireApprovalForuserEmail` and `Organization.RequireApprovalForQueueEmail` (process emails only for approved users/queues) organization attributes are set to **true** (1),  the following occurs: email messages are delivered or sent from a user or queue only if the primary email address of the user or queue is approved. The `SystemUser.EmailRouterAccessApproval` and the `Queue.EmailRouterAccessApproval` attributes indicate the status of the primary email address of the user and queue respectively, and the value must be set to 1. Otherwise, the incoming and outgoing messages will be blocked. You can update the user or queue record to change the attribute value, if it is not already in the approved state, provided your user account has the **prvApproveRejectEmailAddress** privilege assigned.
  
> [!NOTE]
>  In Dataverse, the `Email.StatusCode` attribute cannot be **null**.  
  
<a name="BulkE-Mail"></a>   

## Bulk email  
 Dataverse supports sending email to a large list of recipients through a bulk email request. When a bulk email request is sent to Dataverse, an asynchronous operation is created in the asynchronous service queue that sends the email messages by using a background process. This gives you improved system performance.  
  
 The <xref:Microsoft.Crm.Sdk.Messages.SendBulkMailRequest> and <xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest> messages are used for sending bulk email messages. The following lists the sequence used to send bulk email:  
  
1. Execute the `SendBulkMail` request. This request contains a query that selects the target email recipients and an email template for composing each email.  
  
2. The asynchronous service creates the email activities for each recipient.  
  
3. The asynchronous service sends each email message. The email messages have a "pending" send status.  
  
4. The email router, Dynamics 365 for Outlook, or a third-party email send component polls Dataverse for pending email messages, and if one is found, downloads it by using the `BackgroundSendEmail` request.  
  
5. The `BackgroundSendEmail` request performs the following operations: checks if pending email messages are present, downloads the email to the caller of the <xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest> message, and synchronizes the downloads if there are multiple callers.  
  
6. The caller of the <xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest> message receives the downloaded email message, and sends it out.  
  
<a name="E-MailAttachments"></a>   

## Email attachments  
 
Email attachments are files that can be attached to email messages or email templates. An attached file can be in any standard computer file format such as Office Outlook documents, Office Excel spreadsheets, CAD files, and PDF files. You can attach multiple files as email attachments to an email or email template. The maximum size of files that can be uploaded is determined by the **Organization.MaxUploadFileSize** property. This property is set in the **Email** tab of the **System Settings** in the Dynamics 365 application. This setting limits the size of files that can be attached to email messages, notes, and web resources. The default setting is 5 MB. 
  
 To attach an email attachment with an email message or template, you use the `ActivityMimeAttachment.ObjectId` and `ActivityMimeAttachment.ObjectTypeCode` columns while you are creating or updating an activity mime attachment row.  
  
 The following code sample shows how to attach an email attachment to an email:  
  
```csharp  
ActivityMimeAttachment _sampleAttachment = new ActivityMimeAttachment{  
    ObjectId = new EntityReference(Email.EntityLogicalName, _emailId),  
    ObjectTypeCode = Email.EntityLogicalName,  
    Subject = "Sample Attachment”,  
    Body = System.Convert.ToBase64String(new ASCIIEncoding().GetBytes("Example Attachment")),  
    FileName = "ExampleAttachment.txt"};  
```  
  
 Similarly, to attach the email attachment to a template instead of an email, you will replace the values of the `ActivityMimeAttachment.ObjectId` and `ActivityMimeAttachment.ObjectTypeCode` attributes as follows in the above code:  
  
```csharp  
ObjectId = new EntityReference(Template.EntityLogicalName, _templateId), ObjectTypeCode = Template.EntityLogicalName,  
```  
  
 For complete code sample about how to create email attachments, see [Sample: Create, Retrieve, Update, and Delete an E-Mail Attachment](/dynamics365/customer-engagement/developer/sample-create-retrieve-update-delete-email-attachment).  
  
### Reusing Email Attachments
  
 When you create an email attachment record, the attached file is saved as a file BLOB. The `ActivityMimeAttachment.AttachmentId` attribute of the email attachment record uniquely identifies the file BLOB. This is done to facilitate the reuse of the file attachments with other email and email template records, without creating and storing multiple copies of the same file in the database.  
  
 To reuse an existing file attachment:  
  
1.  Retrieve the `ActivityMimeAttachment` row that contains the attachment file that you want to re-use, as shown in the following code example:  
  
    ```csharp  
    ActivityMimeAttachment retrievedAttachment = (ActivityMimeAttachment)_serviceProxy.Retrieve(ActivityMimeAttachment.EntityLogicalName, _emailAttachmentId, new ColumnSet(true));  
    ```  
  
2.  Create a new email attachment, associate it with the required email or email template row, and point it to the attached file of the retrieved `ActivityMimeAttachment` row, as shown in the following code example:  
  
    ```csharp  
    ActivityMimeAttachment _reuseAttachment = new ActivityMimeAttachment{  
        ObjectId = new EntityReference(Email.EntityLogicalName, _emailId),  
        ObjectTypeCode = Email.EntityLogicalName,  
        Subject = "Sample Attachment”,  
        AttachmentId = retrievedAttachment.AttachmentId};  
    ```  
  
     Because you are reusing an existing attachment file, you do not have to specify the `ActivityMimeAttachment.Body` and `ActivityMimeAttachment.FileName` column values while you are creating and associating email attachment rows to emails or email templates.  
  
### See also  
 [Activity tables](activity-entities.md)   
 [Sample: Send an email](org-service/samples/send-email.md)   
 [Email table](/reference/entities/email.md)   
 [ActivityMimeAttachment table](/reference/entities/activitymimeattachment.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]