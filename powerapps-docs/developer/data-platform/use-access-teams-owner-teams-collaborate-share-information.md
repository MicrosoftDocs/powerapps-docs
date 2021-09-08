---
title: "Use access teams and owner teams to collaborate and share information (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about using access teams and owner teams to colloborate and share information." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/28/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use access teams and owner teams to collaborate and share information

With *owner* teams or *access* teams, you can easily share business objects and collaborate with the users across business units in Microsoft Dataverse. A team belongs to one business unit, but it can include users from other business units. A user can be associated with more than one team.  
  
 An owner team owns rows and has security roles assigned to the team. The team’s privileges are defined by these security roles. In addition to privileges provided by the team, team members have the privileges defined by their individual security roles and by the roles from other teams in which they are members. A team has full access rights on the records that the team owns.  
  
> [!NOTE]
>  While teams provide access to a group of users, you must still associate individual users with security roles that grant the privileges they need to create, update, or delete user-owned records. These privileges cannot be applied by assigning security roles to a team and then adding the user to that team.  
  
 An access team doesn’t own records and doesn’t have security roles assigned to the team. The team members have privileges defined by their individual security roles and by roles from the teams in which they are members. The records are shared with an access team and the team is granted access rights on the records, such as Read, Write or Append.  
  
 The team functionality is supported by the `Team` and `TeamTemplate` tables. The `Team` table is used to create owner teams and user-created access teams. For auto-created access teams, the `Team` table and the `TeamTemplate` table are used.  
 
[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
<a name="BKMK_OwnerAccess"></a>   
## Owner team or access team?  
 Choosing the type of the team may depend on the goals, nature of the project, and even the size of your organization. There are a few guidelines that you can use when choosing the team type.  
  
### When to use owner teams  
  
- Owning records by tables other than users is required by your company’s business policies.  
  
- The number of teams is known at the design time of your Dataverse system.  
  
- Daily reporting on progress by owning teams is required.  
  
### When to use access teams  
  
- The teams are dynamically formed and dissolved. This typically happens if the clear criteria for defining the teams, such as established territory, product, or volume aren’t provided.  
  
- The number of teams isn’t known at the design time of your Dataverse system.  
  
- The team members require different access rights on the records. You can share a record with several access teams, each team providing different access rights on the record. For example, one team is granted the Read access right on the account and another team, the Read, Write and Share access rights on the same account.  
  
- A unique set of users requires access to a single record without having an ownership of the record.  
  
> [!NOTE]
>  Another kind of “access team” is addressed by the access team templates that are used by the web application. This is the type of team that changes often, such as a specific account record’s sales team. When a user is added to a sales team in an account, the web application, behind the scenes, creates a team specific to this record and adds the user to it.  
>   
>  This type of access team isn’t covered in this topic.  
  
<a name="BKMK_SettingUp"></a>   
## Setting up teams  
 In addition to owner and access team types, the access teams are further subdivided into user-created and auto-created (system-managed) teams. The setup information is specific to each team type.  
  
### Owner team  
 An owner team can own multiple rows. To create an owner team, use the `Team` table and set the `Team.TeamType` column to `Owner`. For a list of the `TeamType` values, refer to the [Team table reference](reference/entities/team.md).  
  
> [!NOTE]
> To view the table definitions in your environment, install the Table definition browser solution described in [Browse table definitions in your environment](browse-your-metadata.md). You can also browse the reference documentation for table in the [Table reference](reference/about-entity-reference.md). 
  
 To make a team an owner of the row, you have to assign a row to the team. To assign, use the <xref:Microsoft.Crm.Sdk.Messages.AssignRequest> message. To assign rows to an owner team in bulk, use the <xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsOwnerRequest> message or the <xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsSystemUserRequest> message.  
  
 A row owned by the team must have the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OwnershipType> property set to <xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes>.`TeamOwned`.  
  
 If an owner team doesn’t own rows and doesn’t have security roles assigned to the team, it can be converted to an access team, by using the <xref:Microsoft.Crm.Sdk.Messages.ConvertOwnerTeamToAccessTeamRequest> message. It is a one way conversion. You can’t convert the access team back to the owner team. During conversion, all queues and mailboxes associated with the team are deleted.  
  
 To add or remove team members, use the <xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest> message.  
  
### User-created access team  
 You can share multiple rows with a user-created access team. 
 
- To create an access team, use the `Team` table and set the `Team.TeamType` column to `Access`. For a list of the `TeamType` values, refer to the `Team` table definition.  
  
- To share a record with the user-created access team, use the <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest> message. For user-created teams, the `Team.SystemManaged` attribute is `false`. For a list of the `Team.SystemManaged` values, refer to the `Team` table definition.  
  
- To add or remove team members, use the <xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest> message.  
  
- To provide the team members with different access rights on the records, create several teams and grant each team a different set of access rights on the records.  
  
### Auto-created (system-managed) access team  
 An auto-created (system-managed) team is created for a specific row and can’t be shared with other records. For system-managed teams, you have to provide a team template. To create a template, use the `TeamTemplate` table. In the template, you have to specify the table type and the access rights on the row in the table, such as Read or Write that are granted to the team users when the team is created. The table that you specify in the template must be enabled for auto created access teams. To provide the team members with different access rights on the row, create several team templates. For example, for the account table, provide one template with the Read access right for team that only needs to view the row. Provide a second template with the Read, Write and Share access rights, for team that require more access to the same row.  
  
 To enable a table for the auto-created access teams, set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.AutoCreateAccessTeams> attribute to `true`.  
  
 A maximum number of team templates that you can create for a table is specified in the <xref:Microsoft.Xrm.Sdk.Deployment.TeamSettings.MaxAutoCreatedAccessTeamsPerEntity> deployment setting. The default value is 2. A maximum number of tables that you can enable for auto created access teams is specified in the <xref:Microsoft.Xrm.Sdk.Deployment.TeamSettings.MaxEntitiesEnabledForAutoCreatedAccessTeams> deployment setting. The default value is 5. 
  
 The users are automatically added and removed in the system-managed team, when you add or remove the users in a particular record by using the <xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RemoveUserFromRecordTeamRequest> message. The actual team is created when you add the first user to the record and the team ID is returned in <xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamResponse.AccessTeamId>. The `Team.SystemManaged` column for this team is set to `true`. For a list of the `Team.SystemManaged` values, refer to the `Team` entity metadata. You can find this information in the table definitions in your environment. The caller of the message must have the Share privilege on the table and the access rights on the row that match the access rights provided in the template. For example, if the template specifies the Read access rights, the calling user must have the Read access rights on the row. To be added to the team, a minimum access level a user must have on the table specified in the template is Basic (User) Read.  
  
 Because of the parental relation between the team template and system-managed access teams, when you delete a template, all teams associated with the template are deleted according to the cascading rules.  
  
 If you change access rights for the team template, the changes are only applied to the new auto-created access teams. The existing teams aren’t affected.  
  
<a name="BKMK_ShortSummary"></a>   
## Quick reference to teams  
 Use the following information as a quick reference to the available teams.  
  
|Team|When to use?|What entity to use?|Use team template?|What messages to use to add or remove team members?|Owns records?|How many rows owns or has access to?|Has security roles assigned?|  
|----------|------------------|-------------------------|------------------------|---------------------------------------------------------|-------------------|---------------------------------------------|----------------------------------|  
|Owner|Record ownership by the team is required.<br /><br /> The number of teams is known at the design time.|`Team`|No|<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>.|Yes|Can own multiple records.|Yes|  
|Access, user-created|Multiple records have to be shared with the team.<br /><br /> The number of teams isn’t known at design time.<br /><br /> Team members require different access rights on the records.|`Team`|No|<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>|No|Can access multiple records.|No. Provides access rights on the record.|  
|Access, auto-created (system-managed)|Unique set of users works on a single record.<br /><br /> Team members require different access rights on the records.<br /><br /> Creating teams automatically per record is desirable.|`TeamTemplate`<br /><br /> `Team`|Yes|<xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.RemoveUserFromRecordTeamRequest>|No|Can access only one record.|No. Provides access rights on the record.|  
  
> [!NOTE]
>  Owner teams and access teams provide access rights to the record and related rows, such as to an account and all opportunities related to this account. In case of parental relationship between the records, cascading rules are applied. For the owner teams, you can access tables based on the roles assigned to the user plus the roles assigned to the team that a user is a member of. This allows a user to have privileges outside their business unit. More information: [Table relationship behavior](/powerapps/maker/data-platform/create-edit-entity-relationships#table-relationship-behavior)  
> 
> [!NOTE]
>  A user must have sufficient privileges to join an access team. For example, if the access team has the Delete access right on an account, the user must have the Delete privilege on the Account entity to join the team. If you’re trying to add a user with insufficient privileges, you’ll see this error message: “You can’t add the user to the access team because the user doesn’t have sufficient privileges on the entity.”  
  
### See also  
 [Sample: Share a record using an access team](org-service/samples/share-record-using-access-team.md) <br/> 
 [User and Team tables](user-team-entities.md) <br/>  
 [Team table](reference/entities/team.md) <br/>  
 [TeamTemplate table](reference/entities/teamtemplate.md) <br/>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
