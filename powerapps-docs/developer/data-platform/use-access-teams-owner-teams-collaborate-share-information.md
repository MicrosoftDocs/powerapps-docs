---
title: "Access Teams and Owner Teams for Record Sharing"
description: "Learn when to use access teams and owner teams to share records and collaborate across business units. Choose the right team model." 
ms.custom: ""
ms.date: 03/31/2026
ms.reviewer: "pehecke"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "paulliew" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Use access teams and owner teams to collaborate and share information

By using *owner* teams or *access* teams, you can easily share business objects and collaborate with users across business units in Microsoft Dataverse. A team belongs to one business unit, but it can include users from other business units. A user can be associated with more than one team.  
  
 An owner team owns rows and has security roles assigned to the team. The team’s privileges are defined by these security roles. In addition to the privileges the team provides, team members have the privileges defined by their individual security roles and by the roles from other teams in which they are members. A team has full access rights on the records that the team owns.  
  
> [!NOTE]
> While teams provide access to a group of users, you must still associate individual users with security roles that grant the privileges they need to create, update, or delete user-owned records. These privileges can't be applied by assigning security roles to a team and then adding the user to that team.  
  
 An access team doesn't own records and doesn't have security roles assigned to the team. The team members have privileges defined by their individual security roles and by roles from the teams in which they are members. You share the records with an access team and grant the team access rights on the records, such as Read, Write, or Append. Therefore, access team members can't create records by using the access rights of the access team. A user is required to have a security role with Create privilege to create records.
  
 The `Team` and `TeamTemplate` tables support the team functionality. Use the `Team` table to create owner teams and user-created access teams. For auto-created access teams, use both the `Team` table and the `TeamTemplate` table.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
<a name="BKMK_OwnerAccess"></a>

## Owner team or access team?  

 Choosing the type of team depends on the goals, nature of the project, and even the size of your organization. Use the following guidelines when choosing the team type.  
  
### When to use owner teams  
  
- Your company’s business policies require that teams, rather than users, own records.  
  
- You know the number of teams at the design time of your Dataverse system.  
  
- You require daily reporting on progress by owning teams.  
  
### When to use access teams  
  
- Use access teams when the teams are dynamically formed and dissolved. This dynamic formation typically happens if you don't provide clear criteria for defining the teams, such as established territory, product, or volume.  
  
- Use access teams when you don't know the number of teams at the design time of your Dataverse system.  
  
- Use access teams when team members require different access rights on the records. You can share a record with several access teams, and each team provides different access rights on the record. For example, one team is granted the Read access right on the account, and another team is granted the Read, Write, and Share access rights on the same account.  
  
- Use access teams when a unique set of users requires access to a single record without having an ownership of the record.  
  
> [!NOTE]
> The web application uses access team templates to address another kind of "access team." This type of team changes often, such as a specific account record's sales team. When a user is added to a sales team in an account, the web application, behind the scenes, creates a team specific to this record and adds the user to it.  
>
> This type of access team isn't covered in this topic.  
  
<a name="BKMK_SettingUp"></a>

## Setting up teams  

 In addition to owner and access team types, access teams are further subdivided into user-created and auto-created (system-managed) teams. The setup information is specific to each team type.  
  
### Owner team  

 An owner team can own multiple rows. To create an owner team, use the `Team` table and set the `Team.TeamType` column to `Owner`. For a list of the `TeamType` values, see the [Team table reference](reference/entities/team.md).  
  
> [!NOTE]
> To view the table definitions in your environment, install the Table definition browser solution described in [Browse table definitions in your environment](browse-your-metadata.md). You can also browse the reference documentation for table in the [Table reference](reference/about-entity-reference.md).
  
 To make a team an owner of the row, assign a row to the team. To assign, use the <xref:Microsoft.Crm.Sdk.Messages.AssignRequest> message. To assign rows to an owner team in bulk, use the <xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsOwnerRequest> message or the <xref:Microsoft.Crm.Sdk.Messages.ReassignObjectsSystemUserRequest> message.  
  
 A row owned by the team must have the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OwnershipType> property set to <xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes>.`TeamOwned`.  
  
 If an owner team doesn't own rows and doesn't have security roles assigned to the team, you can convert it to an access team by using the <xref:Microsoft.Crm.Sdk.Messages.ConvertOwnerTeamToAccessTeamRequest> message. It's a one-way conversion. You can't convert the access team back to the owner team. During conversion, all queues and mailboxes associated with the team are deleted.  
  
 To add or remove team members, use the <xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest> message.  
  
### User-created access team  

 You can share multiple rows with a user-created access team.

- To create an access team, use the `Team` table and set the `Team.TeamType` column to `Access`. For a list of the `TeamType` values, see the `Team` table definition.  
  
- To share a record with the user-created access team, use the <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest> message. For user-created teams, the `Team.SystemManaged` attribute is `false`. For a list of the `Team.SystemManaged` values, see the `Team` table definition.  
  
- To add or remove team members, use the <xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest> message.  
  
- To provide the team members with different access rights on the records, create several teams and grant each team a different set of access rights on the records.  
  
### Auto-created (system-managed) access team  

 The system creates an auto-created (system-managed) team for a specific row, and you can't share it with other records. For system-managed teams, you must provide a team template. To create a template, use the `TeamTemplate` table. In the template, specify the table type and the access rights on the row in the table, such as Read or Write, that you grant to the team users when you create the team. The table that you specify in the template must be enabled for auto-created access teams. To give the team members different access rights on the row, create several team templates. For example, for the account table, provide one template with the Read access right for a team that only needs to view the row. Provide a second template with the Read, Write, and Share access rights, for a team that requires more access to the same row.  
  
 To enable a table for the auto-created access teams, set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.AutoCreateAccessTeams> attribute to `true`.  
  
 The `MaxAutoCreatedAccessTeamsPerEntity` [environment database settings](/power-platform/admin/environment-database-settings) specify the maximum number of team templates that you can create for a table. The default value is four. The `MaxEntitiesEnabledForAutoCreatedAccessTeams` [environment database settings](/power-platform/admin/environment-database-settings) specify the maximum number of tables that you can enable for auto-created access teams. The default value is 100. To update these settings, use the [OrganizationSettingsEditor](/power-platform/admin/environment-database-settings#install-the-organizationsettingseditor-tool).
  
 When you add or remove users in a particular record by using the <xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RemoveUserFromRecordTeamRequest> message, the system automatically adds and removes the users in the system-managed team. The actual team is created when you add the first user to the record, and the team ID is returned in <xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamResponse.AccessTeamId>. The `Team.SystemManaged` column for this team is set to `true`. For a list of the `Team.SystemManaged` values, refer to the `Team` entity metadata. You can find this information in the table definitions in your environment. The caller of the message must have the Share privilege on the table and the access rights on the row that match the access rights provided in the template. For example, if the template specifies the Read access rights, the calling user must have the Read access rights on the row. To be added to the team, a minimum access level a user must have on the table specified in the template is Basic (User) Read.  
  
 Because of the parental relation between the team template and system-managed access teams, when you delete a template, all teams associated with the template are deleted according to the cascading rules.  
  
 If you change access rights for the team template, the changes only apply to new auto-created access teams. The existing teams aren't affected.  
  
<a name="BKMK_ShortSummary"></a>

## Quick reference to teams  

 Use the following information as a quick reference to the available teams.  
  
|Team|When to use?|What entity to use?|Use team template?|What messages to use to add or remove team members?|Owns records?|How many rows owns or has access to?|Has security roles assigned?|  
|----------|------------------|-------------------------|------------------------|---------------------------------------------------------|-------------------|---------------------------------------------|----------------------------------|  
|Owner|Record ownership by the team is required.<br /><br /> The number of teams is known at the design time.|`Team`|No|<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>.|Yes|Can own multiple records.|Yes|  
|Access, user-created|Multiple records have to be shared with the team.<br /><br /> The number of teams isn’t known at design time.<br /><br /> Team members require different access rights on the records.|`Team`|No|<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>|No|Can access multiple records.|No. Provides access rights on the record.|  
|Access, auto-created (system-managed)|Unique set of users works on a single record.<br /><br /> Team members require different access rights on the records.<br /><br /> Creating teams automatically per record is desirable.|`TeamTemplate`<br /><br /> `Team`|Yes|<xref:Microsoft.Crm.Sdk.Messages.AddUserToRecordTeamRequest> <br /> <xref:Microsoft.Crm.Sdk.Messages.RemoveUserFromRecordTeamRequest>|No|Can access only one record.|No. Provides access rights on the record.|  
  
> [!NOTE]
> Owner teams and access teams provide access rights to the record and related rows, such as to an account and all opportunities related to this account. In case of parental relationship between the records, cascading rules are applied. For the owner teams, you can access tables based on the roles assigned to the user plus the roles assigned to the team that a user is a member of. This access model allows a user to have privileges outside their business unit. For more information, see [Table relationship behavior](/powerapps/maker/data-platform/create-edit-entity-relationships#table-relationship-behavior).  
>
> [!NOTE]
> A user must have sufficient privileges to join an access team. For example, if the access team has the Delete access right on an account, the user must have the Delete privilege on the Account entity to join the team. If you try to add a user with insufficient privileges, you see this error message: “You can’t add the user to the access team because the user doesn’t have sufficient privileges on the entity.”  
  
### See also  

 [Sample: Share a record using an access team](org-service/samples/share-record-using-access-team.md) <br/>
 [User and Team tables](user-team-entities.md) <br/>  
 [Team table](reference/entities/team.md) <br/>  
 [TeamTemplate table](reference/entities/teamtemplate.md) <br/>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
