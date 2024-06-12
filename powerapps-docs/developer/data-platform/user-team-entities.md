---
title: "User and team tables (Microsoft Dataverse)"
description: "Learn about user and team management using which you can create and maintain user accounts and profiles."
ms.date: 01/13/2023
ms.reviewer: pehecke
ms.topic: article
author: paulliew
ms.subservice: dataverse-developer
ms.author: paulliew
search.audienceType: 
  - developer
---
# User and team tables

User and team management is the area of Microsoft Dataverse where you can create and maintain user accounts and profiles.  

 A *user* is any person who works for a business unit who uses Dataverse. Each user has a user account. All users must be associated with only one business unit. This association controls which customer data the user has access to. Included in the user's account is information such as the user's telephone numbers, email address, and a link to the user's manager. Each user has privileges and rights to manage their own personal settings. Each user corresponds to a user in the Microsoft Entra ID for that organization. When you create a user, you must assign the user to at least one security role. Even if the user is part of a team that has assigned roles, the user should be assigned to a role. For more information about access levels and roles, see [Security concepts for developers](security-concepts.md).  

 A *team* is a group of users. Teams let users across an organization collaborate and share information. For more information about teams, see [Use Teams to Collaborate and Share Information](use-access-teams-owner-teams-collaborate-share-information.md).  

 Users or teams can own records. Set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OwnershipType> to <xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes>.`UserOwned` or <xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes>.`TeamOwned` to enable ownership. You can use the <xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsOwnerRequest> message or the <xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsSystemUserRequest> message to do bulk reassignment of all records for an owner.  

 The following illustration shows the relationships for users and teams.  

 ![User and team table relationship diagram.](media/crm-v5s-em-userteam.gif "User and team table relationship diagram")  

## Users

 The following table provides details about the significant attributes for the system user table.
 
 [!INCLUDE[cc-terminology](includes/cc-terminology.md)]
 


|   Column name    |                                                                                                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     AccessMode      | Specifies the type of access that this user has to Dataverse. This is sometimes referred to as the type of user.<br /><br /> -   Administrative – The user has access to the Settings area but doesn't have access to the Sales, Marketing, and Service areas.<br />-   Non-Interactive – The user can access the system but only through the Web service.<br />-   Read – The user has read-only access.<br />-   Read-Write – The user has both read and write access.<br />-   Support User – The Dataverse support team created the user. |
|       CalType       |                                                               Specifies the user's license type.<br /><br /> -   Administrative – The user has administrative user rights.<br />-   Device Full – The user who is using the device running Dataverse has both read and write access.<br />-   Device Limited – The user who is using the device running Dataverse only has read access.<br />-   Full – The user has both read and write access.<br />-   Limited – The user only has read access.                                                                |
|     IsDisabled      |                                                                                                                                                                                                                                             Specifies whether the user is disabled. Only licensed users or users who have an access mode of support or non-interactive can be enabled. Support users can't be disabled.                                                                                                                                                                                                                                              |
|     IsLicensed      |                                                                                                                                                                             Specifies whether the user is licensed. This applies to customers who access Dataverse through the Microsoft Online Services Environment. This attribute is read-only, and is updated by the system.                                                                                                                                                                              |
| IsSyncWithDirectory |                                                                                                                                 Specifies whether the user is synchronized with the Microsoft 365 directory. This applies to customers who access Dataverse through the Microsoft Online Services Environment. This attribute can only be set on create and is otherwise read-only.                                                                                                                                 |
|       QueueId       |                                                                                                                                                                                                                                                                                                               Specifies the default queue for the user.                                                                                                                                                                                                                                                                                                               |

 Access checks are additive. You can access tables based on the roles assigned to the user plus the roles assigned to the team that a user is a member of. This allows a user to have privileges outside their business unit.  

> [!NOTE]
> A user's set of privileges is a union of privileges from the user's roles and privileges from all teams' roles in which the user is a member.  

 Non-interactive users are often used when writing service-to-service code because they don't use up a license. Dataverse allows for seven free non-interactive users. To disable a non-interactive user, update the user record changing the `accessmode` value to any other value. The user is disabled automatically.

To find the user who is currently logged on or who is impersonated, call the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> message.  

### Delete a user

 In Dataverse, users can be disabled and deleted. You can delete a user from Power Platform (Dataverse) assuming you have the required access permission to the [SystemUser table](reference/entities/systemuser.md) row. There's a sequence of tasks to follow. You can't simply delete the row in a single call. You must first delete the user registered in Microsoft Entra ID and then delete the user in Dataverse. The procedure to follow is outlined below.

Log into Microsoft Azure [portal](https://portal.azure.com), and then follow these steps:

1. Select **Microsoft Entra ID**, and then under **Manage** select **Users**
1. Delete the user - this is called a 'soft delete' as the user record remains until permanently deleted
1. Permanently delete the user either manually or wait 30 days until Azure permanently deletes the user through automation

After the system user is soft or permanently deleted in Azure, the user status will be shown as disabled in Dataverse. You can find this user row in the SystemUser table.

In Dataverse:

1. Reassign any existing table rows the user is assigned to - there should be no table rows assigned to the user before to deleting the user
1. Delete the user by using an SDK or Web API call - this is a soft delete
1. Permanently delete the system user by an API call a second time

> [!TIP]
> There is an over-ride where the user row in Dataverse can be deleted without permanently deleting the user's Microsoft Entra ID record. This can be done by setting the [OrgDbOrgSetting](reference/entities/organization.md#BKMK_OrgDbOrgSettings) `AuthorizationSkipAadUserStateValidation=true`. This removes the need to do step #2 in the above Azure procedure. See [Environment database settings](/power-platform/admin/environment-database-settings) to update this value.

More information: [Delete users from environment](/power-platform/admin/delete-users), [Update and delete table rows using the Web API](webapi/update-delete-entities-using-web-api.md), [Update and delete table rows using the SDK for .NET](org-service/entity-operations-update-delete.md)

## Community tools

**User Settings Utility** is a tool that XrmToolbox community developed for Dataverse. See the [Developer tools](developer-tools.md) article for community-developed tools.

> [!NOTE]
> The community tools are not a product of Dataverse and does not extend support to the community tools.
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also  
   
 [Use Teams to Collaborate and Share Information](use-access-teams-owner-teams-collaborate-share-information.md)<br/>   
 [Team table reference](reference/entities/team.md)<br/>   
 [Specify time zone settings for a user](specify-time-zone-settings-user.md)<br/>   
 [Sample: Share Records Using GrantAccess, ModifyAccess and RevokeAccess Messages](org-service/samples/share-records-using-grantaccess-modifyaccess-revokeaccess-messages.md)<br/>   
 [Sample: Share a record using an access team](org-service/samples/share-record-using-access-team.md)<br/>   
 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
