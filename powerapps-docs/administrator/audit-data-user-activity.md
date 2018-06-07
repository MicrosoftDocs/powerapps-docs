---
title: "Audit data and user activity for Dynamics 365 Customer Engagement | MicrosoftDocs"
ms.custom: ""
ms.date: 09/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: f8966997-6047-4ff7-b3ae-47cbceea96a2
caps.latest.revision: 17
author: "Mattp123"
ms.author: "matp"
manager: "brycho"
---
# Audit data and user activity for security and compliance 

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

The [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] auditing feature logs changes that are made to customer records and user access so you can review the activity later. The auditing feature is designed to meet the auditing, compliance, security, and governance policies of many regulated enterprises.  
  
 The audit logs help the [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] Administrator answer questions such as:  
  
-   Which user was accessing the system and when?  
  
-   Who updated this field value on this record and when?  
  
-   What was the previous field value before it was updated?  
  
-   What actions has this user taken recently?  
  
-   Who deleted this record?  
  
-   What locale was used to make the update?  
  
The following operations can be audited:  
  
-   Create, update, deactivate, and delete operations on records.  
  
-   Changes to the sharing privileges of a record.  
  
-   The N:N association or disassociation of records.  
  
-   Changes to security roles.  
  
-   Audit changes at the entity, attribute, and organization level. For example, enabling audit on an entity.  
  
-   Deletion of audit logs.  
  
-   For changes made to entity fields that can be localized, such as the Product entity name or description fields, the locale ID (LCID) appears in the audit record.  
  
System administrators and customizers can start or stop auditing for an organization.  
  
> [!IMPORTANT]
>  For [!INCLUDE[pn_crm_op_edition](../includes/pn-crm-onprem.md)], you may notice that auditing can significantly increase the size of the organization database over time. You can delete audit logs by going to **Settings** > **Auditing** > **Audit Log Management**. Additionally, you may want to stop auditing for maintenance purposes. Stopping auditing stops tracking for the organization during the period until auditing is started again. When you start auditing again, the same auditing selection is maintained that was previously used.  
  
<a name="BKMK_startAudit"></a>   
## Start or stop auditing for an organization  
 This task requires the system administrator or customizer security role or equivalent permissions.  
  
1. [!INCLUDE[proc_settings_administration](../includes/proc-settings-administration.md)]  
  
2.  Choose **System Settings**.  
  
3.  On the **Auditing** tab, select the **Start Auditing** check box to start auditing. Clear the **Start Auditing** check box to stop all auditing.  
  
4.  Select the entities you want to track. To start or stop auditing on specific entities, select or clear the following check boxes:  
  
    - **Audit user access**. Tracks when a user accesses [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] including the user name and time.  
  
    - **Common Entities**. Tracks common entities like Account, Contact, Goal, Product, and User.  
  
    - **Sales Entities**. Tracks sales-related entities like Competitor, Opportunity, Invoice, Order, and Quote.  
  
    - **Marketing Entities**. Tracks Campaign entity activity.  
  
    - **Customer Service Entities**. Tracks Case, Contract, Queue, and Service entity activity.  
  
5.  Click **OK**.  
  
<a name="BKMK_viewAuditlogs"></a>   
## View audit logging details  
 System administrators can see activity for the entities that are enabled for audit logging.  
  
1. [!INCLUDE[proc_settings_auditing](../includes/proc-settings-auditing.md)]  
  
2.  Choose **Audit Summary View**.  
  
3.  In the **Audit Summary View**, you can do the following:  
  
    -   Click **Enable/Disable Filters** to turn on filtering. Then, you can filter on a specific event, such as **Delete** actions.  
  
    -   Choose an **Event** to view specific details about the activity, such as field changes that were made during an update to a record and who performed the update.  
  
    -   Click the **Refresh** button  ![Refresh button](media/html-viewer-grid-refresh.gif "Refresh button") to view the most recent activity. 

<a name="BKMK_enable_ent_aud"></a>   
## Enable or disable entities and fields for auditing  
 System administrators or customizers can change the default audit settings for entities and for specific fields for an entity.  
  
 **To enable or disable auditing for an entity**  
  
1. [!INCLUDE[proc_settings_system](../includes/proc-settings-system.md)]  
  
2.  Click **Auditing**.  
  
3.  In the **Audit** area, choose **Entity and Field Audit Settings**.  
  
4.  Under **Components**, expand **Entities**.  
  
5.  Open the entity for which you want to enable or disable auditing.  
  
6.  To start auditing, on the **General** tab, in the **Data Services** section, select the **Auditing** check box to enable auditing, or clear the **Auditing** check box to disable it.  
  
     By default, when you start or stop auditing for an entity, you also start or stop auditing for all the fields of this entity.  
  
7.  Click **Save**.  
  
8.  Publish the customization. To publish for a single entity, choose the entity, such as Account, and then click **Publish** on the toolbar.  
  
 **To enable or disable auditing for specific fields on an entity**  
  
1.  Under the entity for which you want to enable or disable auditing with specific fields, click **Fields**.  
  
2.  To enable or disable a single field, open the field and in the Auditing section, select **Enable** or **Disable**.  
  
     To enable or disable more than one field, select the fields you want, and then on the toolbar click **Edit**. In the **Edit Multiple Fields** dialog box, in the Auditing area, click **Enabled** or **Disabled**.  
  
3.  Click **Save**.  
  
4.  Publish the customization. To publish for a single entity, choose the entity, such as Account, and then click **Publish** on the Actions toolbar.  
 
### See also  
 [Manage security, users and teams](https://docs.microsoft.com/dynamics365/customer-engagement/admin/manage-security-users-and-teams)<br/> 
 [Getting started with customization](../maker/model-driven-apps/getting-started-customization.md)   

