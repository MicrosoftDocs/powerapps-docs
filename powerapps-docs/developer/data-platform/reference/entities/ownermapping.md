---
title: "Owner Mapping (OwnerMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Owner Mapping (OwnerMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Owner Mapping (OwnerMapping) table/entity reference (Microsoft Dataverse)

In a data map, maps ownership data from the source file to Microsoft Dynamics 365.

## Messages

The following table lists the messages for the Owner Mapping (OwnerMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /ownermappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /ownermappings(*ownermappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /ownermappings(*ownermappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /ownermappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Owner Mapping (OwnerMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Owner Mapping** |
| **DisplayCollectionName** | **Owner Mappings** |
| **SchemaName** | `OwnerMapping` |
| **CollectionSchemaName** | `OwnerMappings` |
| **EntitySetName** | `ownermappings`|
| **LogicalName** | `ownermapping` |
| **LogicalCollectionName** | `ownermappings` |
| **PrimaryIdAttribute** | `ownermappingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportMapId](#BKMK_ImportMapId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [OwnerMappingId](#BKMK_OwnerMappingId)
- [ProcessCode](#BKMK_ProcessCode)
- [SourceSystemUserName](#BKMK_SourceSystemUserName)
- [SourceUserValueForSourceCRMUserLink](#BKMK_SourceUserValueForSourceCRMUserLink)
- [StatusCode](#BKMK_StatusCode)
- [TargetSystemUserDomainName](#BKMK_TargetSystemUserDomainName)
- [TargetSystemUserId](#BKMK_TargetSystemUserId)
- [TargetUserValueForSourceCRMUserLink](#BKMK_TargetUserValueForSourceCRMUserLink)

### <a name="BKMK_ImportMapId"></a> ImportMapId

|Property|Value|
|---|---|
|Description|**Unique identifier of the data map with which the owner mapping is associated.**|
|DisplayName|**Data Map**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importmapid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|importmap|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the component is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_OwnerMappingId"></a> OwnerMappingId

|Property|Value|
|---|---|
|Description|**Unique identifier of the owner mapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownermappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ProcessCode"></a> ProcessCode

|Property|Value|
|---|---|
|Description|**Code that indicates whether the owner mapping has to be processed**|
|DisplayName|**Process Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`ownermapping_processcode`|

#### ProcessCode Choices/Options

|Value|Label|
|---|---|
|1|**Process**|
|2|**Ignore**|
|3|**Internal**|

### <a name="BKMK_SourceSystemUserName"></a> SourceSystemUserName

|Property|Value|
|---|---|
|Description|**Source user name that has to be replaced**|
|DisplayName|**Source System User Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcesystemusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_SourceUserValueForSourceCRMUserLink"></a> SourceUserValueForSourceCRMUserLink

|Property|Value|
|---|---|
|Description|**Source user value for source Microsoft Dynamics 365 user link.**|
|DisplayName|**Source User Value**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourceuservalueforsourcecrmuserlink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the owner mapping.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`ownermapping_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />State:0<br />TransitionData: None|

### <a name="BKMK_TargetSystemUserDomainName"></a> TargetSystemUserDomainName

|Property|Value|
|---|---|
|Description|**Microsoft Dynamics 365 logon name with which the source user name should be replaced.**|
|DisplayName|**Target Domain Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetsystemuserdomainname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|260|

### <a name="BKMK_TargetSystemUserId"></a> TargetSystemUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Microsoft Dynamics 365 user.**|
|DisplayName|**Target System User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`targetsystemuserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_TargetUserValueForSourceCRMUserLink"></a> TargetUserValueForSourceCRMUserLink

|Property|Value|
|---|---|
|Description|**Microsoft Dynamics CRM user.**|
|DisplayName|**Target User Value**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`targetuservalueforsourcecrmuserlink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|


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
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerMappingIdUnique](#BKMK_OwnerMappingIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [StateCode](#BKMK_StateCode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)

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
|Description|**Unique identifier of the user who created the owner mapping.**|
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
|Description|**Date and time when the owner mapping was created.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the ownermapping.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
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
|Description|**Unique identifier of the user who last modified the lookup mapping.**|
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
|Description|**Date and time when the owner mapping was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the ownermapping.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_OwnerMappingIdUnique"></a> OwnerMappingIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the OwnerMapping.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownermappingidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the owner mapping.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`ownermapping_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|

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

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_ownermapping_createdby](#BKMK_lk_ownermapping_createdby)
- [lk_ownermapping_createdonbehalfby](#BKMK_lk_ownermapping_createdonbehalfby)
- [lk_ownermapping_modifiedby](#BKMK_lk_ownermapping_modifiedby)
- [lk_ownermapping_modifiedonbehalfby](#BKMK_lk_ownermapping_modifiedonbehalfby)
- [OwnerMapping_ImportMap](#BKMK_OwnerMapping_ImportMap)
- [OwnerMapping_SystemUser](#BKMK_OwnerMapping_SystemUser)

### <a name="BKMK_lk_ownermapping_createdby"></a> lk_ownermapping_createdby

One-To-Many Relationship: [systemuser lk_ownermapping_createdby](systemuser.md#BKMK_lk_ownermapping_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_ownermapping_createdonbehalfby"></a> lk_ownermapping_createdonbehalfby

One-To-Many Relationship: [systemuser lk_ownermapping_createdonbehalfby](systemuser.md#BKMK_lk_ownermapping_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_ownermapping_modifiedby"></a> lk_ownermapping_modifiedby

One-To-Many Relationship: [systemuser lk_ownermapping_modifiedby](systemuser.md#BKMK_lk_ownermapping_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_ownermapping_modifiedonbehalfby"></a> lk_ownermapping_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_ownermapping_modifiedonbehalfby](systemuser.md#BKMK_lk_ownermapping_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_OwnerMapping_ImportMap"></a> OwnerMapping_ImportMap

One-To-Many Relationship: [importmap OwnerMapping_ImportMap](importmap.md#BKMK_OwnerMapping_ImportMap)

|Property|Value|
|---|---|
|ReferencedEntity|`importmap`|
|ReferencedAttribute|`importmapid`|
|ReferencingAttribute|`importmapid`|
|ReferencingEntityNavigationPropertyName|`importmapid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_OwnerMapping_SystemUser"></a> OwnerMapping_SystemUser

One-To-Many Relationship: [systemuser OwnerMapping_SystemUser](systemuser.md#BKMK_OwnerMapping_SystemUser)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`targetsystemuserid`|
|ReferencingEntityNavigationPropertyName|`targetsystemuserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.ownermapping?displayProperty=fullName>
