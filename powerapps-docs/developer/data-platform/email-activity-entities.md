---
title: "Email activity tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The email activity in lets you track and manage email communications with customers." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/08/2023
ms.reviewer: pehecke
ms.topic: article
author: DanaMartens # GitHub ID
ms.subservice: dataverse-developer
ms.author: dmartens # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
  - ProfessorKendrick
---
# Email activity tables

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The email activity lets you track and manage email communications with customers. 
  
<a name="Actions"></a>   

## Actions on an email activity

 Using Dataverse web services, you can perform the following actions on an email activity:  
  
- Create, retrieve, update, and delete the email activity.  
- Send email messages, or send email messages by using email templates (`Template`). For more information about email templates, see [Create email templates](../../user/email-template-create.md).  
- Attach files as attachments by using the (`ActivityMimeAttachment`) attribute in the email message.  
- Send mass or bulk email messages.  
- Configure incoming email messages to be delivered from Microsoft Exchange Server to any user or queue, or outgoing messages to be sent from any user or queue to Microsoft Exchange Server.  
  
   If the `Organization.RequireApprovalForuserEmail` and `Organization.RequireApprovalForQueueEmail` (process emails only for approved users/queues) organization attributes are set to **true** (1),  the following occurs: email messages are delivered or sent from a user or queue only if the primary email address of the user or queue is approved. The `SystemUser.EmailRouterAccessApproval` and the `Queue.EmailRouterAccessApproval` attributes indicate the status of the primary email address of the user and queue respectively, and the value must be set to 1. Otherwise, the incoming and outgoing messages will be blocked. You can update the user or queue record to change the attribute value, if it isn't already in the approved state, provided your user account has the **prvApproveRejectEmailAddress** privilege assigned.
  
> [!NOTE]
>  In Dataverse, the `Email.StatusCode` attribute cannot be **null**.  
  
<a name="BulkE-Mail"></a>   

## Bulk email

Dataverse supports sending email to a large list of recipients through a bulk email request. When a bulk email request is sent to Dataverse, an asynchronous operation is created in the asynchronous service queue that sends the email messages by using a background process. This gives you improved system performance.  
  
The <xref:Microsoft.Crm.Sdk.Messages.SendBulkMailRequest> and <xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest> messages are used for sending bulk email messages. The following lists the sequence used to send bulk email:  
  
1. Execute the `SendBulkMail` request. This request contains a query that selects the target email recipients and an email template for composing each email.  
1. The asynchronous service creates the email activities for each recipient.  
1. The asynchronous service sends each email message. The email messages have a "pending" send status.  
1. The email router, Dynamics 365 for Outlook, or a third-party email send component polls Dataverse for pending email messages, and if one is found, downloads it by using the `BackgroundSendEmail` request.  
1. The `BackgroundSendEmail` request performs the following operations: checks if pending email messages are present, downloads the email to the caller of the <xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest> message, and synchronizes the downloads if there are multiple callers.  

   > [!NOTE]
   > Your email service provider may have limits which affect how many emails you can send within a period of time. More information: [Exchange Online limits > Sending limits](/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits).

1. The caller of the <xref:Microsoft.Crm.Sdk.Messages.BackgroundSendEmailRequest> message receives the downloaded email message, and sends it out.  
  
<a name="E-MailAttachments"></a>   

## Email attachments  
 
Email attachments are files that can be attached to email messages or email templates. An attached file can be in any standard computer file format such as Office Outlook documents, Office Excel spreadsheets, CAD files, and PDF files. You can attach multiple files as email attachments to an email or email template. The maximum size of files that can be uploaded is determined by the **Organization.MaxUploadFileSize** property. This property is set in the **Email** tab of the **System Settings** in the Dynamics 365 application. This setting limits the size of files that can be attached to email messages, notes, and web resources. The default setting is 5 MB. 
  
To attach an email attachment with an email message or template, you use the `ActivityMimeAttachment.ObjectId` and `ActivityMimeAttachment.ObjectTypeCode` columns while you're creating or updating an activity mime attachment row.  
  
The following code sample shows how to attach an email attachment to an email:  
  
```csharp  
ActivityMimeAttachment _sampleAttachment = new ActivityMimeAttachment{  
    ObjectId = new EntityReference(Email.EntityLogicalName, _emailId),  
    ObjectTypeCode = Email.EntityLogicalName,  
    Subject = "Sample Attachment",  
    Body = System.Convert.ToBase64String(new ASCIIEncoding().GetBytes("Example Attachment")),  
    FileName = "ExampleAttachment.txt"};  
```  
  
Similarly, to attach the email attachment to a template instead of an email, you'll replace the values of the `ActivityMimeAttachment.ObjectId` and `ActivityMimeAttachment.ObjectTypeCode` attributes as follows in the above code:  
  
```csharp  
ObjectId = new EntityReference(Template.EntityLogicalName, _templateId), ObjectTypeCode = Template.EntityLogicalName,  
```  
  
For complete code sample about how to create email attachments, see [Sample: Create, retrieve, update, and delete an email attachment](org-service/samples/create-retrieve-update-delete-email-attachment.md).  
  
### Reusing Email Attachments
  
When you create an email attachment record, the attached file is saved as a file BLOB. The `ActivityMimeAttachment.AttachmentId` attribute of the email attachment record uniquely identifies the file BLOB. This is done to facilitate the reuse of the file attachments with other email and email template records, without creating and storing multiple copies of the same file in the database.  
  
To reuse an existing file attachment:  
  
1. Retrieve the `ActivityMimeAttachment` row that contains the attachment file that you want to reuse, as shown in the following code example:  
  
   ```csharp  
   ActivityMimeAttachment retrievedAttachment = 
       (ActivityMimeAttachment)_serviceProxy
       .Retrieve(ActivityMimeAttachment.EntityLogicalName, _emailAttachmentId, new ColumnSet(true));  
   ```  
  
1. Create a new email attachment, associate it with the required email or email template row, and point it to the attached file of the retrieved `ActivityMimeAttachment` row, as shown in the following code example:  
  
   ```csharp  
   ActivityMimeAttachment _reuseAttachment = new ActivityMimeAttachment{  
     ObjectId = new EntityReference(Email.EntityLogicalName, _emailId),  
     ObjectTypeCode = Email.EntityLogicalName,  
     Subject = "Sample Attachment",  
     AttachmentId = retrievedAttachment.AttachmentId};  
   ```  
  
  Because you're reusing an existing attachment file, you don't have to specify the `ActivityMimeAttachment.Body` and `ActivityMimeAttachment.FileName` column values while you're creating and associating email attachment rows to emails or email templates.  

## Email storage

Email descriptions (body of the email) have up to this point been stored in the Dataverse relational store. That is changing as the [Email.Description](reference/entities/email.md#BKMK_Description) column in the [email activity](reference/entities/email.md) table is being relocated to unstructured Azure Blob storage. Azure Blob storage is also used for storage of attachments, annotations, files, and images.

### Transition period

The data migration from Dataverse relation store to Azure Blob storage for all customers is expected to start in May 2023. This data migration will take place as a background process. The initial data movement for existing customers is expected to last for about 6 to 12 weeks, and possibly even longer depending on the size of the data. After the initial data movement, any remaining migration is a continuous process. All email descriptions older than 12 months will be moved into Azure Blob storage automatically. Newer emails will not be moved until they become 12 months old.

This data migration will be transparent to you with the exception that you will see a reduction in the size of the [ActivityPointer](reference/entities/activitypointer.md) table after the migration process is fully completed. In Power Platform admin center within the **Capacity** report, a new email line item will be available in **File usage**. The end result is an increase in the overall File storage consumption and reduction in the database storage consumed.

> [!NOTE]
> The increase in File storage will may be smaller than what is removed from the ActivityPointer table due to compression of file data.

The limitations mentioned in the next section will start applying to any data that has already moved to the Dataverse managed Azure blob storage even if all the data movement is not complete.

### Search and filtering limitations

For email descriptions (bodies) stored in Azure Blob storage, certain limitations apply to filtering, finding, and searching email descriptions as described below.

#### Filtering

Filtering on email descriptions is not supported. Some specific points to consider are as follows.

- FetchXML - You will not be able to search in email bodies using FetchXML.
- Quick Find and Advanced Find - Filtering email descriptions using these methods is not supported.

> [!TIP]
> For Quick Find, while filtering is not supported, the email body can be added as a returned column and the body data will be returned in the result.

#### Searching

You can enable [Dataverse search](webapi/relevance-search.md) on email descriptions to search email descriptions.
  
### See also

[Activity tables](activity-entities.md)<br />
[Sample: Send an email](org-service/samples/send-email.md)<br />
[Email table](reference/entities/email.md)<br />
[ActivityMimeAttachment table](reference/entities/activitymimeattachment.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
