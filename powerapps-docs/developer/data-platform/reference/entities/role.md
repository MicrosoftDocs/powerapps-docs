---
title: "Security Role (Role) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Security Role (Role) table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Security Role (Role) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Grouping of security privileges. Users are assigned roles that authorize their access to the Microsoft CRM system.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|AddPrivilegesRole|<xref href="Microsoft.Dynamics.CRM.AddPrivilegesRole?text=AddPrivilegesRole Action" />|<xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>|
|Create|POST [*org URI*]/api/data/v9.0/roles<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/roles(*roleid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|RemovePrivilegeRole|<xref href="Microsoft.Dynamics.CRM.RemovePrivilegeRole?text=RemovePrivilegeRole Action" />|<xref:Microsoft.Crm.Sdk.Messages.RemovePrivilegeRoleRequest>|
|ReplacePrivilegesRole|<xref href="Microsoft.Dynamics.CRM.ReplacePrivilegesRole?text=ReplacePrivilegesRole Action" />|<xref:Microsoft.Crm.Sdk.Messages.ReplacePrivilegesRoleRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/roles(*roleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveAadUserRoles|<xref href="Microsoft.Dynamics.CRM.RetrieveAadUserRoles?text=RetrieveAadUserRoles Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAadUserRolesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/roles<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrieveRolePrivilegesRole|<xref href="Microsoft.Dynamics.CRM.RetrieveRolePrivilegesRole?text=RetrieveRolePrivilegesRole Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRolePrivilegesRoleRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/roles(*roleid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Roles|
|DisplayCollectionName|Security Roles|
|DisplayName|Security Role|
|EntitySetName|roles|
|IsBPFEntity|False|
|LogicalCollectionName|roles|
|LogicalName|role|
|OwnershipType|BusinessOwned|
|PrimaryIdAttribute|roleid|
|PrimaryNameAttribute|name|
|SchemaName|Role|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CanBeDeleted](#BKMK_CanBeDeleted)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsInherited](#BKMK_IsInherited)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [RoleId](#BKMK_RoleId)


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the role is associated.|
|DisplayName|Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|businessunitid|
|RequiredLevel|SystemRequired|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_CanBeDeleted"></a> CanBeDeleted

|Property|Value|
|--------|-----|
|Description|Tells whether the role can be deleted.|
|DisplayName|Can Be Deleted|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|canbedeleted|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsInherited"></a> IsInherited

|Property|Value|
|--------|-----|
|Description|Role is inherited by users from team membership, if role associated with team.|
|DisplayName|Is Inherited|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isinherited|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### IsInherited Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Team privileges only||
|1|Direct User (Basic) access level and Team privileges||



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the role.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_RoleId"></a> RoleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the role.|
|DisplayName|Role|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|roleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [ParentRoleId](#BKMK_ParentRoleId)
- [ParentRoleIdName](#BKMK_ParentRoleIdName)
- [ParentRootRoleId](#BKMK_ParentRootRoleId)
- [ParentRootRoleIdName](#BKMK_ParentRootRoleIdName)
- [RoleIdUnique](#BKMK_RoleIdUnique)
- [RoleTemplateId](#BKMK_RoleTemplateId)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the role.|
|DisplayName|Created By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the role was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the role.|
|DisplayName|Created By Impersonator|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the role.|
|DisplayName|Modified By|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the role was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the role.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the role.|
|DisplayName|Organization|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ParentRoleId"></a> ParentRoleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent role.|
|DisplayName|Parent Role|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentroleid|
|RequiredLevel|None|
|Targets|role|
|Type|Lookup|


### <a name="BKMK_ParentRoleIdName"></a> ParentRoleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentroleidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ParentRootRoleId"></a> ParentRootRoleId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the parent root role.|
|DisplayName|Parent Root Role|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentrootroleid|
|RequiredLevel|SystemRequired|
|Targets|role|
|Type|Lookup|


### <a name="BKMK_ParentRootRoleIdName"></a> ParentRootRoleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentrootroleidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_RoleIdUnique"></a> RoleIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Unique Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|roleidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_RoleTemplateId"></a> RoleTemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the role template that is associated with the role.|
|DisplayName|Role Template|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|roletemplateid|
|RequiredLevel|None|
|Targets|roletemplate|
|Type|Lookup|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the role.|
|DisplayName|Version number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [role_parent_role](#BKMK_role_parent_role)
- [Role_AsyncOperations](#BKMK_Role_AsyncOperations)
- [role_parent_root_role](#BKMK_role_parent_root_role)
- [Role_BulkDeleteFailures](#BKMK_Role_BulkDeleteFailures)
- [Role_SyncErrors](#BKMK_Role_SyncErrors)


### <a name="BKMK_role_parent_role"></a> role_parent_role

Same as role table [role_parent_role](role.md#BKMK_role_parent_role) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|parentroleid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|role_parent_role|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Role_AsyncOperations"></a> Role_AsyncOperations

Same as asyncoperation table [Role_AsyncOperations](asyncoperation.md#BKMK_Role_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Role_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_role_parent_root_role"></a> role_parent_root_role

Same as role table [role_parent_root_role](role.md#BKMK_role_parent_root_role) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|role|
|ReferencingAttribute|parentrootroleid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|role_parent_root_role|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Role_BulkDeleteFailures"></a> Role_BulkDeleteFailures

Same as bulkdeletefailure table [Role_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Role_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Role_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Role_SyncErrors"></a> Role_SyncErrors

Same as syncerror table [Role_SyncErrors](syncerror.md#BKMK_Role_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Role_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_rolebase_modifiedby](#BKMK_lk_rolebase_modifiedby)
- [role_parent_role](#BKMK_role_parent_role)
- [organization_roles](#BKMK_organization_roles)
- [business_unit_roles](#BKMK_business_unit_roles)
- [lk_role_createdonbehalfby](#BKMK_lk_role_createdonbehalfby)
- [lk_role_modifiedonbehalfby](#BKMK_lk_role_modifiedonbehalfby)
- [role_parent_root_role](#BKMK_role_parent_root_role)
- [lk_rolebase_createdby](#BKMK_lk_rolebase_createdby)
- [solution_role](#BKMK_solution_role)


### <a name="BKMK_lk_rolebase_modifiedby"></a> lk_rolebase_modifiedby

See systemuser Table [lk_rolebase_modifiedby](systemuser.md#BKMK_lk_rolebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_role_parent_role"></a> role_parent_role

See role Table [role_parent_role](role.md#BKMK_role_parent_role) One-To-Many relationship.

### <a name="BKMK_organization_roles"></a> organization_roles

See organization Table [organization_roles](organization.md#BKMK_organization_roles) One-To-Many relationship.

### <a name="BKMK_business_unit_roles"></a> business_unit_roles

See businessunit Table [business_unit_roles](businessunit.md#BKMK_business_unit_roles) One-To-Many relationship.

### <a name="BKMK_lk_role_createdonbehalfby"></a> lk_role_createdonbehalfby

See systemuser Table [lk_role_createdonbehalfby](systemuser.md#BKMK_lk_role_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_role_modifiedonbehalfby"></a> lk_role_modifiedonbehalfby

See systemuser Table [lk_role_modifiedonbehalfby](systemuser.md#BKMK_lk_role_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_role_parent_root_role"></a> role_parent_root_role

See role Table [role_parent_root_role](role.md#BKMK_role_parent_root_role) One-To-Many relationship.

### <a name="BKMK_lk_rolebase_createdby"></a> lk_rolebase_createdby

See systemuser Table [lk_rolebase_createdby](systemuser.md#BKMK_lk_rolebase_createdby) One-To-Many relationship.

### <a name="BKMK_solution_role"></a> solution_role

See solution Table [solution_role](solution.md#BKMK_solution_role) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Role table is the first table in the relationship. Listed by **SchemaName**.

- [systemuserroles_association](#BKMK_systemuserroles_association)
- [roleprivileges_association](#BKMK_roleprivileges_association)
- [appmoduleroles_association](#BKMK_appmoduleroles_association)
- [teamroles_association](#BKMK_teamroles_association)
- [applicationuserrole](#BKMK_applicationuserrole)


### <a name="BKMK_systemuserroles_association"></a> systemuserroles_association

See systemuser Table [systemuserroles_association](systemuser.md#BKMK_systemuserroles_association) Many-To-Many Relationship.

### <a name="BKMK_roleprivileges_association"></a> roleprivileges_association

See privilege Table [roleprivileges_association](privilege.md#BKMK_roleprivileges_association) Many-To-Many Relationship.

### <a name="BKMK_appmoduleroles_association"></a> appmoduleroles_association

See appmodule Table [appmoduleroles_association](appmodule.md#BKMK_appmoduleroles_association) Many-To-Many Relationship.

### <a name="BKMK_teamroles_association"></a> teamroles_association

See team Table [teamroles_association](team.md#BKMK_teamroles_association) Many-To-Many Relationship.

### <a name="BKMK_applicationuserrole"></a> applicationuserrole

See applicationuser Table [applicationuserrole](applicationuser.md#BKMK_applicationuserrole) Many-To-Many Relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.role?text=role EntityType" />