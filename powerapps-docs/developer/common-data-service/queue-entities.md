---
title: "Queue entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Queues in PowerApps are instrumental in organizing, prioritizing, and monitoring the progress of your work." 
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID Temp owner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Queue entities

*Queues* are instrumental in organizing, prioritizing, and monitoring the progress of your work. As a central location for work management, queues assist you in processing cases, responding to service calls, or sending out product information to prospective customers. Programmatically, a queue is a collection of queue items. A queue item serves as a container for an entity record, such as a task, an email, or a case that needs processing. See [Queue Entity](reference/entities/queue.md)

> [!NOTE]
> For information about working with queues using the UI, see [Queues overview](/dynamics365/customer-engagement/customer-service/set-up-queues-manage-activities-cases).  
  
The following information pertains to queues:  
  
-   All customizable entities can be enabled for queues.  
  
-   Queues may be public or private. Private queue items are only visible to the members of the queue.  
  
-   A private queue is automatically created for each new user or team.  
  
-   A queue can contain multiple entity types, such as tasks, emails, or cases.  
  
-   A queue contains information about the user who is working on a particular queue item. This helps you manage your resources more efficiently and helps to prevent duplication of work.  
  
-   Queues can be enabled for workflows and audit. This helps improve productivity and track the entity and attribute data changes for future analysis and reporting.  
  
<a name="BKMK_MemberCapabilities"></a>   
## Members capabilities  
 Queues are categorized into *public* or *private* queues. Private queues have individual users as members to make controlling access to queues easier. If you add a team to a private queue, all the members of that team become members of the private queue.  
  
<a name="BKMK_publicAndPrivateQueues"></a>   
## Public and private queues  
 The [QueueViewType](reference/entities/queue.md#BKMK_QueueViewType) attribute is a picklist that defines whether a queue is public or private.  
  
-   All user queues are private queues for the user: Only the user will be able to see queue items in their private queue.  
  
-   Team queues are marked as private with members: the team owner and all team members will be able to see the queue in the application.  
  
-   All other queues are public. Everyone with read privileges for the queue entity will be able to see these queues.  
  
<a name="BKMK_QueueAttributes"></a>   
## Attributes used to manage queues  
 Use the following attributes to manage queues.  
  
|SchemaName|DisplayName|Type|Description|  
|----------------|-----------------|----------|-----------------|  
|NumberOfItems|Queue Items|Integer|Number of Queue items associated with the queue.|  
|NumberOfMembers|No. of Members|Integer|Number of Members associated with the queue.|  
|QueueViewType|Type|Picklist|Select whether the queue is public or private. A public queue can be viewed by all. A private queue can be viewed only by the members added to the queue.|  
  
<a name="BKMK_deletingQueues"></a>   
## Restrictions on deleting queues  
 A queue cannot be deleted if the following are true:  
  
-   When the queue has queue items.  
  
-   When any routing rule uses the queue.  
  
<a name="BKMK_Enabling"></a>   
## Enable entities for queues  
 To enable a customizable entity (`EntityMetadata.IsCustomizable = true`) for queues, use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> message to set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsValidForQueue> attribute to `true`. The queue entity and the queue item entity are customizable entities, but they cannot be enabled for queues.  
  
 The following list contains default queue-enabled entities in Common Data Service (CDS) for Apps:  
  
-   Appointment  
  
-   Campaignactivity  
  
-   CampaignResponse  
  
-   Email  
  
-   Fax  
  
-   Incident  
  
-   Letter  
  
-   PhoneCall  
  
-   RecurringAppointmentMaster  
  
-   ServiceAppointment  
  
-   SocialActivity  
  
-   Task  
  
<a name="BKMK_Inheriting"></a>   
## Inherit privileges and provide limited access to a queue  
 A queue and a queue item have a parental relationship in which operations on the parent queue record are propagated to the child queue item records.  
  
> [!NOTE]
>  In this particular parental relationship, only the Delete action is cascaded from the parent queue entity to the child queue item entity. Other actions, such as Assign, Merge or Share are not cascaded.  
  
 The privileges on a queue item are inherited from the privileges on a queue.  
  
- If you have `prvReadQueue` privilege, you also have read privilege on a queue item entity.  
  
- If you have `prvAppendToQueue` privilege, you also have create, update, and delete privileges on a queue item entity.  
  
  Often, you must limit access to the queue when permitting access to the queue items. As a queue owner with full access to the queue, you might want to share a queue with a team that will have only limited access to the queue. For example, if the support team is given read and append to privileges on a queue, team members cannot make any changes to the queue, such as changing queue name or queue owner. However, they can create, retrieve, update, and delete queue items.  
  
<a name="BKMK_Actions"></a>   
## Actions on queues and queue items  
 You can perform a variety of actions on queues and queue items, if you have appropriate privileges on the queue entity and the queue item entity.  
  
### Actions on queues  
 Perform the following actions on the queues:  
  
-   Customize queues and queue items by adding custom attributes.  
  
-   Add an entity record to a queue.  
  
    > [!NOTE]
    >  An entity record cannot be added in multiple queues. An exception is an email entity record with the status “Received”.  
  
-   Add entity records of different entity types in the same queue.  
  
-   Change an ownership of a queue by assigning it to another user or team.  
  
-   Add principals to a private queue using the <xref:Microsoft.Crm.Sdk.Messages.AddPrincipalToQueueRequest>.  
  
-   Clean up the history for a queue by deleting inactive queue items in the queue, such as completed or canceled phone calls.  
  
-   Retrieve all the queues that a user has access to using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveUserQueuesRequest>  
  
-   Make a queue the default queue for a user by setting the `SystemUser.QueueId` attribute to the ID of the queue. The same queue can be specified as a default queue for different users.  
  
-   Create a workflow that operates on all private queues. For example, whenever a user creates a task, the workflow adds the task to the default queue of the user. You can also create a workflow that operates only on a particular queue.  
  
-   Configure an email for incoming messages, if you want incoming email messages to be delivered to a queue.  
  
### Actions on queue items  
 Perform the following actions on the queue items:  
  
- Assign a queue item to a user using the <xref:Microsoft.Crm.Sdk.Messages.PickFromQueueRequest>.  
  
- Move a queue item from a source queue to a destination queue by using the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest> message. A queue item can be moved from one queue to another until it is deactivated by using the <xref:Microsoft.Crm.Sdk.Messages.SetStateRequest> message.  
  
  > [!NOTE]
  >  A queue item is automatically deactivated if the state of the record in the queue item changed from Active to Inactive. This applies to queue-enabled entities that have Active and Inactive states. To determine if an entity is queue-enabled and if an entity record can be in an Active or Inactive state, see entity metadata information.  
  
- Release a queue item back to the queue using the <xref:Microsoft.Crm.Sdk.Messages.ReleaseToQueueRequest>.  
  
- Delete a queue item from a queue by using the <xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> message. When you delete a queue item, a referenced entity record is not deleted. However, when you delete an entity record, all queue items that reference this entity record are deleted.  
  
### See also  
 <!--[Configure EMail for Incoming Messages](configure-email-incoming-messages.md)-->  
 
[Queue Entity](reference/entities/queue.md)   
[QueueItem Entity](reference/entities/queueitem.md)   
<xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest>   
 