---
title: "Security Role (Role) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Security Role (Role) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Security Role (Role) table/entity reference (Microsoft Dataverse)

Grouping of security privileges. Users are assigned roles that authorize their access to the Microsoft CRM system.

## Messages

The following table lists the messages for the Security Role (Role) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddPrivilegesRole`<br />Event: True |<xref:Microsoft.Dynamics.CRM.AddPrivilegesRole?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /roles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /roles(*roleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `RemovePrivilegeRole`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RemovePrivilegeRole?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RemovePrivilegeRoleRequest>|
| `ReplacePrivilegesRole`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ReplacePrivilegesRole?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ReplacePrivilegesRoleRequest>|
| `Retrieve`<br />Event: False |`GET` /roles(*roleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveAadUserRoles`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveAadUserRoles?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveAadUserRolesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /roles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveRolePrivilegesRole`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveRolePrivilegesRole?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveRolePrivilegesRoleRequest>|
| `Update`<br />Event: True |`PATCH` /roles(*roleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /roles(*roleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Security Role (Role) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Security Role** |
| **DisplayCollectionName** | **Security Roles** |
| **SchemaName** | `Role` |
| **CollectionSchemaName** | `Roles` |
| **EntitySetName** | `roles`|
| **LogicalName** | `role` |
| **LogicalCollectionName** | `roles` |
| **PrimaryIdAttribute** | `roleid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `BusinessOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicationId](#BKMK_ApplicationId)
- [AppliesTo](#BKMK_AppliesTo)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CanBeDeleted](#BKMK_CanBeDeleted)
- [Description](#BKMK_Description)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsAutoAssigned](#BKMK_IsAutoAssigned)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsInherited](#BKMK_IsInherited)
- [IsSystemGenerated](#BKMK_IsSystemGenerated)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [RoleId](#BKMK_RoleId)
- [SummaryofCoreTablePermissions](#BKMK_SummaryofCoreTablePermissions)

### <a name="BKMK_ApplicationId"></a> ApplicationId

|Property|Value|
|---|---|
|Description|**Application Id of user who created the role**|
|DisplayName|**Application Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_AppliesTo"></a> AppliesTo

|Property|Value|
|---|---|
|Description|**Personas/Licenses the security role applies to**|
|DisplayName|**Applies To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`appliesto`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit with which the role is associated.**|
|DisplayName|**Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|---|---|
|Description|**Tells whether the role can be deleted.**|
|DisplayName|**Can Be Deleted**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canbedeleted`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the security role**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsAutoAssigned"></a> IsAutoAssigned

|Property|Value|
|---|---|
|Description|**Value indicating whether security role is auto-assigned based on user license**|
|DisplayName|**Is Auto Assigned**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isautoassigned`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`securityrole_isautoassigned`|

#### IsAutoAssigned Choices/Options

|Value|Label|
|---|---|
|0|**No**|
|1|**Yes**|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsInherited"></a> IsInherited

|Property|Value|
|---|---|
|Description|**Role is inherited by users from team membership, if role associated with team.**|
|DisplayName|**Is Inherited**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isinherited`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`isinherited`|

#### IsInherited Choices/Options

|Value|Label|
|---|---|
|0|**Team privileges only**|
|1|**Direct User (Basic) access level and Team privileges**|

### <a name="BKMK_IsSystemGenerated"></a> IsSystemGenerated

|Property|Value|
|---|---|
|Description|**Is this role generated by the system**|
|DisplayName|**Is System Generated**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`issytemgenerated`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`role_issytemgenerated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the role.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RoleId"></a> RoleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role.**|
|DisplayName|**Role**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SummaryofCoreTablePermissions"></a> SummaryofCoreTablePermissions

|Property|Value|
|---|---|
|Description|**Summary of Core Table Permissions of the Role**|
|DisplayName|**Summary of Core Table Permissions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`summaryofcoretablepermissions`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [ParentRoleId](#BKMK_ParentRoleId)
- [ParentRootRoleId](#BKMK_ParentRootRoleId)
- [RoleIdUnique](#BKMK_RoleIdUnique)
- [RoleTemplateId](#BKMK_RoleTemplateId)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the role.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the role was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the role.**|
|DisplayName|**Created By Impersonator**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the role.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the role was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the role.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization associated with the role.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationidname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ParentRoleId"></a> ParentRoleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent role.**|
|DisplayName|**Parent Role**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentroleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|role|

### <a name="BKMK_ParentRootRoleId"></a> ParentRootRoleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent root role.**|
|DisplayName|**Parent Root Role**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentrootroleid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|role|

### <a name="BKMK_RoleIdUnique"></a> RoleIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roleidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RoleTemplateId"></a> RoleTemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier of the role template that is associated with the role.**|
|DisplayName|**Role Template**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`roletemplateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|roletemplate|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the role.**|
|DisplayName|**Version number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_roles](#BKMK_business_unit_roles)
- [lk_role_createdonbehalfby](#BKMK_lk_role_createdonbehalfby)
- [lk_role_modifiedonbehalfby](#BKMK_lk_role_modifiedonbehalfby)
- [lk_rolebase_createdby](#BKMK_lk_rolebase_createdby)
- [lk_rolebase_modifiedby](#BKMK_lk_rolebase_modifiedby)
- [organization_roles](#BKMK_organization_roles)
- [role_parent_role](#BKMK_role_parent_role-many-to-one)
- [role_parent_root_role](#BKMK_role_parent_root_role-many-to-one)
- [role_template_roles](#BKMK_role_template_roles)
- [solution_role](#BKMK_solution_role)

### <a name="BKMK_business_unit_roles"></a> business_unit_roles

One-To-Many Relationship: [businessunit business_unit_roles](businessunit.md#BKMK_business_unit_roles)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`businessunitid`|
|ReferencingEntityNavigationPropertyName|`businessunitid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_role_createdonbehalfby"></a> lk_role_createdonbehalfby

One-To-Many Relationship: [systemuser lk_role_createdonbehalfby](systemuser.md#BKMK_lk_role_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_role_modifiedonbehalfby"></a> lk_role_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_role_modifiedonbehalfby](systemuser.md#BKMK_lk_role_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_rolebase_createdby"></a> lk_rolebase_createdby

One-To-Many Relationship: [systemuser lk_rolebase_createdby](systemuser.md#BKMK_lk_rolebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_rolebase_modifiedby"></a> lk_rolebase_modifiedby

One-To-Many Relationship: [systemuser lk_rolebase_modifiedby](systemuser.md#BKMK_lk_rolebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_roles"></a> organization_roles

One-To-Many Relationship: [organization organization_roles](organization.md#BKMK_organization_roles)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid_organization`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_role_parent_role-many-to-one"></a> role_parent_role

One-To-Many Relationship: [role role_parent_role](#BKMK_role_parent_role-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`role`|
|ReferencedAttribute|`roleid`|
|ReferencingAttribute|`parentroleid`|
|ReferencingEntityNavigationPropertyName|`parentroleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_role_parent_root_role-many-to-one"></a> role_parent_root_role

One-To-Many Relationship: [role role_parent_root_role](#BKMK_role_parent_root_role-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`role`|
|ReferencedAttribute|`roleid`|
|ReferencingAttribute|`parentrootroleid`|
|ReferencingEntityNavigationPropertyName|`parentrootroleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_role_template_roles"></a> role_template_roles

One-To-Many Relationship: [roletemplate role_template_roles](roletemplate.md#BKMK_role_template_roles)

|Property|Value|
|---|---|
|ReferencedEntity|`roletemplate`|
|ReferencedAttribute|`roletemplateid`|
|ReferencingAttribute|`roletemplateid`|
|ReferencingEntityNavigationPropertyName|`roletemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solution_role"></a> solution_role

One-To-Many Relationship: [solution solution_role](solution.md#BKMK_solution_role)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`solutionid`|
|ReferencingEntityNavigationPropertyName|`solution_role`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [Role_AsyncOperations](#BKMK_Role_AsyncOperations)
- [Role_BulkDeleteFailures](#BKMK_Role_BulkDeleteFailures)
- [role_parent_role](#BKMK_role_parent_role-one-to-many)
- [role_parent_root_role](#BKMK_role_parent_root_role-one-to-many)
- [Role_SyncErrors](#BKMK_Role_SyncErrors)

### <a name="BKMK_Role_AsyncOperations"></a> Role_AsyncOperations

Many-To-One Relationship: [asyncoperation Role_AsyncOperations](asyncoperation.md#BKMK_Role_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Role_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Role_BulkDeleteFailures"></a> Role_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure Role_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Role_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Role_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_role_parent_role-one-to-many"></a> role_parent_role

Many-To-One Relationship: [role role_parent_role](#BKMK_role_parent_role-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`role`|
|ReferencingAttribute|`parentroleid`|
|ReferencedEntityNavigationPropertyName|`role_parent_role`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_role_parent_root_role-one-to-many"></a> role_parent_root_role

Many-To-One Relationship: [role role_parent_root_role](#BKMK_role_parent_root_role-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`role`|
|ReferencingAttribute|`parentrootroleid`|
|ReferencedEntityNavigationPropertyName|`role_parent_root_role`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Role_SyncErrors"></a> Role_SyncErrors

Many-To-One Relationship: [syncerror Role_SyncErrors](syncerror.md#BKMK_Role_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Role_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [application_role](#BKMK_application_role)
- [applicationuserrole](#BKMK_applicationuserrole)
- [appmoduleroles_association](#BKMK_appmoduleroles_association)
- [roleprivileges_association](#BKMK_roleprivileges_association)
- [systemuserroles_association](#BKMK_systemuserroles_association)
- [teamroles_association](#BKMK_teamroles_association)

### <a name="BKMK_application_role"></a> application_role

See [application application_role Many-To-Many Relationship](application.md#BKMK_application_role)

|Property|Value|
|---|---|
|IntersectEntityName|`applicationroles`|
|IsCustomizable|False|
|SchemaName|`application_role`|
|IntersectAttribute|`roleid`|
|NavigationPropertyName|`application_role`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_applicationuserrole"></a> applicationuserrole

See [applicationuser applicationuserrole Many-To-Many Relationship](applicationuser.md#BKMK_applicationuserrole)

|Property|Value|
|---|---|
|IntersectEntityName|`applicationuserrole`|
|IsCustomizable|False|
|SchemaName|`applicationuserrole`|
|IntersectAttribute|`roleid`|
|NavigationPropertyName|`applicationuserrole`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association

See [appmodule appmoduleroles_association Many-To-Many Relationship](appmodule.md#BKMK_appmoduleroles_association)

|Property|Value|
|---|---|
|IntersectEntityName|`appmoduleroles`|
|IsCustomizable|False|
|SchemaName|`appmoduleroles_association`|
|IntersectAttribute|`roleid`|
|NavigationPropertyName|`appmoduleroles_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_roleprivileges_association"></a> roleprivileges_association

See [privilege roleprivileges_association Many-To-Many Relationship](privilege.md#BKMK_roleprivileges_association)

|Property|Value|
|---|---|
|IntersectEntityName|`roleprivileges`|
|IsCustomizable|False|
|SchemaName|`roleprivileges_association`|
|IntersectAttribute|`roleid`|
|NavigationPropertyName|`roleprivileges_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_systemuserroles_association"></a> systemuserroles_association

See [systemuser systemuserroles_association Many-To-Many Relationship](systemuser.md#BKMK_systemuserroles_association)

|Property|Value|
|---|---|
|IntersectEntityName|`systemuserroles`|
|IsCustomizable|False|
|SchemaName|`systemuserroles_association`|
|IntersectAttribute|`roleid`|
|NavigationPropertyName|`systemuserroles_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_teamroles_association"></a> teamroles_association

See [team teamroles_association Many-To-Many Relationship](team.md#BKMK_teamroles_association)

|Property|Value|
|---|---|
|IntersectEntityName|`teamroles`|
|IsCustomizable|False|
|SchemaName|`teamroles_association`|
|IntersectAttribute|`roleid`|
|NavigationPropertyName|`teamroles_association`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.role?displayProperty=fullName>
