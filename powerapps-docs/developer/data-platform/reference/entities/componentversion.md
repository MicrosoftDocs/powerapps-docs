---
title: "componentversion table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the componentversion table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# componentversion table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Component Versioning Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /componentversions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /componentversions(*componentversionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /componentversions(*componentversionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /componentversions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /componentversions(*componentversionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|componentversions|
|DisplayCollectionName|Component Versions|
|DisplayName|Component Version|
|EntitySetName|componentversions|
|IsBPFEntity|False|
|LogicalCollectionName|componentversions|
|LogicalName|componentversion|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|componentversionid|
|PrimaryNameAttribute|componentversionname|
|SchemaName|componentversion|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ChangeSummary](#BKMK_ChangeSummary)
- [Component](#BKMK_Component)
- [ComponentIdType](#BKMK_ComponentIdType)
- [componentversionname](#BKMK_componentversionname)
- [Operation](#BKMK_Operation)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [RestoredFromVersion](#BKMK_RestoredFromVersion)
- [SystemChangeSummary](#BKMK_SystemChangeSummary)


### <a name="BKMK_ChangeSummary"></a> ChangeSummary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Change Summary|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|changesummary|
|MaxLength|2048|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Component"></a> Component

|Property|Value|
|--------|-----|
|Description|Owning component.|
|DisplayName|Component|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|component|
|RequiredLevel|ApplicationRequired|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_ComponentIdType"></a> ComponentIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidtype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_componentversionname"></a> componentversionname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Version Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|componentversionname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Operation|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|operation|
|RequiredLevel|None|
|Type|Picklist|

#### Operation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Create||
|1|Update||
|2|Publish||
|3|Restore||
|4|Solution Import||



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


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_RestoredFromVersion"></a> RestoredFromVersion

|Property|Value|
|--------|-----|
|Description|Base version that was restored.|
|DisplayName|Restored From Version|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|restoredfromversion|
|RequiredLevel|None|
|Targets|componentversion|
|Type|Lookup|


### <a name="BKMK_SystemChangeSummary"></a> SystemChangeSummary

|Property|Value|
|--------|-----|
|Description||
|DisplayName|System Change Summary|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|systemchangesummary|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentName](#BKMK_ComponentName)
- [componentversionId](#BKMK_componentversionId)
- [ComponentYomiName](#BKMK_ComponentYomiName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningTeamName](#BKMK_OwningTeamName)
- [OwningTeamYomiName](#BKMK_OwningTeamYomiName)
- [OwningUser](#BKMK_OwningUser)
- [OwningUserName](#BKMK_OwningUserName)
- [OwningUserYomiName](#BKMK_OwningUserYomiName)
- [restoredfromversionName](#BKMK_restoredfromversionName)


### <a name="BKMK_ComponentName"></a> ComponentName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_componentversionId"></a> componentversionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Component Version|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentversionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentYomiName"></a> ComponentYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentyominame|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
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
|MaxLength|200|
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
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
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
|MaxLength|200|
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
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningTeamName"></a> OwningTeamName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteamname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeamYomiName"></a> OwningTeamYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteamyominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_OwningUserName"></a> OwningUserName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningusername|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningUserYomiName"></a> OwningUserYomiName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguseryominame|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_restoredfromversionName"></a> restoredfromversionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|restoredfromversionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_restoreversions"></a> restoreversions

Same as the [restoreversions](componentversion.md#BKMK_restoreversions) many-to-one relationship for the [componentversion](componentversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|componentversion|
|ReferencingAttribute|restoredfromversion|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|restoredtoversions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_componentversion_createdby](#BKMK_lk_componentversion_createdby)
- [lk_componentversion_modifiedby](#BKMK_lk_componentversion_modifiedby)
- [team_componentversion](#BKMK_team_componentversion)
- [user_componentversion](#BKMK_user_componentversion)
- [restoreversions](#BKMK_restoreversions)
- [workflow_componentversions](#BKMK_workflow_componentversions)


### <a name="BKMK_lk_componentversion_createdby"></a> lk_componentversion_createdby

**Added by**: System Solution Solution

See the [lk_componentversion_createdby](systemuser.md#BKMK_lk_componentversion_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_componentversion_modifiedby"></a> lk_componentversion_modifiedby

**Added by**: System Solution Solution

See the [lk_componentversion_modifiedby](systemuser.md#BKMK_lk_componentversion_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_componentversion"></a> team_componentversion

**Added by**: System Solution Solution

See the [team_componentversion](team.md#BKMK_team_componentversion) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_user_componentversion"></a> user_componentversion

**Added by**: System Solution Solution

See the [user_componentversion](systemuser.md#BKMK_user_componentversion) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_restoreversions"></a> restoreversions

See the [restoreversions](componentversion.md#BKMK_restoreversions) one-to-many relationship for the [componentversion](componentversion.md) table/entity.

### <a name="BKMK_workflow_componentversions"></a> workflow_componentversions

**Added by**: System Solution Solution

See the [workflow_componentversions](workflow.md#BKMK_workflow_componentversions) one-to-many relationship for the [workflow](workflow.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.componentversion?text=componentversion EntityType" />