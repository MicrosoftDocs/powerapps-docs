---
title: "Configure Exchange folder-level tracking rules (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to configure Exchange folder-level tracking rules" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/24/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "revachauhan" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Configure Exchange folder-level tracking rules

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Configure folder-level tracking rules to map a Microsoft Exchange inbox folder to a Microsoft Dataverse record so that all the emails in the Microsoft Exchange folder get automatically tracked against the mapped record in Dataverse. Folder-level tracking of emails will work only if:  

- The folder-level tracking feature is enabled for your Dataverse instance. You can enable folder-level tracking by using the web client or Dynamics 365 for Outlook. More information: [Configure folder-level tracking](/dynamics365/customer-engagement/admin/configure-outlook-exchange-folder-level-tracking)  

- The folder that you are tracking is under the **Inbox** folder in Microsoft Exchange. Emails in the folders that are not under the **Inbox** folder won’t be tracked.  

<a name="Create"></a>   

## Create and manage folder-level tracking rules 
 
 Use the [MailboxTrackingFolder table](/reference/entities/mailboxtrackingfolder.md) to programmatically configure and manage your folder-level tracking rules. To set up a tracking rule, use the following columns.  


|  Column       |  Description |
|-------------------------------|----|
| [ExchangeFolderId](/reference/entities/mailboxtrackingfolder.md#BKMK_ExchangeFolderId)  | Specify the Microsoft Exchange folder ID that you want to map. You can use the Exchange Web Services (EWS) to retrieve the ID of a folder under your Inbox folder. For more information, see [MSDN: How to: Work with folders by using EWS in Exchange](https://msdn.microsoft.com/library/office/dn535504.aspx). This is a required column. |
|         [MailboxId](/reference/entities/mailboxtrackingfolder.md#BKMK_MailboxId)     |   Specify the mailbox ID in Dataverse that you want to create the rule for. This is a required column.                                                                                                                                          |
| [RegardingObjectId](/reference/entities/mailboxtrackingfolder.md#BKMK_RegardingObjectId) |                                                                                                       Set the regarding object in Dataverse that you want the specified Microsoft Exchange folder to be mapped to. This is an optional column.                                                                                                       |

 The following sample code shows how you can create a folder-level tracking rule.  

```csharp  
// Create a folder-level tracking rule  
MailboxTrackingFolder newTrackingFolder = new MailboxTrackingFolder();  

// Set the required attributes  
newTrackingFolder.ExchangeFolderId = "123456"; // Sample value. Retrieve this value using Exchange Web Services (EWS)  
newTrackingFolder.MailboxId = new EntityReference(Mailbox.EntityLogicalName, _mailboxId);  

// Set the optional attributes  
newTrackingFolder.RegardingObjectId = new EntityReference(Account.EntityLogicalName, _accountId);  
newTrackingFolder.RegardingObjectId.Name = _accountName;  
newTrackingFolder.ExchangeFolderName = "Sample Exchange Folder";  

// Execute the request to create the rule   
_folderTrackingId = _serviceProxy.Create(newTrackingFolder);  
Console.WriteLine("Created folder-level tracking rule for '{0}'.\n", _mailboxName);  
```  

 You can create a maximum of 25 folder-level tracking rules per mailbox. The folder ID of the Microsoft Exchange folder can’t be validated at the time of creating the mapping using SDK. However, as soon as you create a mapping rule, and if the folder ID is invalid, it will show up in the UI in Dataverse to indicate that the mapping is invalid.  

 Any manual changes done to the regarding object in the tracked activity records, created in Dataverse as a result of the folder-level tracking rule, will be overridden the next time server-side synchronization occurs. For example, if you have set up a mapping between the `Adventure Works` folder and the `Adventure Works` account, all the emails in the `Adventure Works`Microsoft Exchange folder will be tracked as activities in Dataverse with the regarding set to the `Adventure Works` account record. If you change the regarding of some activities to any other record, it will automatically be overridden the next time server-side synchronization occurs.  

<a name="Retrieve"></a>   

## Retrieve folder-level tracking rules for a mailbox  

 You can retrieve all the folder-level tracking rules for a mailbox by using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveMailboxTrackingFoldersRequest> message. Pass the mailbox ID for which you want to retrieve the rules in the <xref:Microsoft.Crm.Sdk.Messages.RetrieveMailboxTrackingFoldersRequest>.<xref:Microsoft.Crm.Sdk.Messages.RetrieveMailboxTrackingFoldersRequest.MailboxId> property, and execute the message.  

 The following sample code shows how you can retrieve folder-level tracking rules for a mailbox.  

```csharp  
// Retrieve the folder mapping rules for a mailbox  
RetrieveMailboxTrackingFoldersRequest req = new RetrieveMailboxTrackingFoldersRequest  
{  
    MailboxId = _mailboxId.ToString()  
};  

RetrieveMailboxTrackingFoldersResponse resp = (RetrieveMailboxTrackingFoldersResponse_serviceProxy.Execute(req);  
Console.WriteLine("Retrieved folder-level tracking rules for {0}:", _mailboxName);  
int n = 1;  
foreach (var folderMapping in resp.MailboxTrackingFolderMappings)  
{  
    Console.WriteLine("\tRule {0}: '{1}' is mapped to '{2}'.",   
        n, folderMapping.ExchangeFolderName, folderMapping.RegardingObjectName);  
    n++;  
}  
```  

### See also  
 <xref href="Microsoft.Dynamics.CRM.RetrieveMailboxTrackingFolders?text=RetrieveMailboxTrackingFolders Function" /><br />
 [MailboxTrackingFolder table](/reference/entities/mailboxtrackingfolder.md)<br />
 [Mailbox table](/reference/entities/mailbox.md)<br />
 [Configure folder-level tracking](/dynamics365/customer-engagement/admin/configure-outlook-exchange-folder-level-tracking)<br />
 [Server-side Synchronization tables](server-side-synchronization-entities.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]