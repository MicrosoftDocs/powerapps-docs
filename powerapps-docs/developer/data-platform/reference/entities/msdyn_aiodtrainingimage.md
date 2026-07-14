---
title: "AI Object Detection Image Mapping (msdyn_AIOdTrainingImage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AI Object Detection Image Mapping (msdyn_AIOdTrainingImage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AI Object Detection Image Mapping (msdyn_AIOdTrainingImage) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the AI Object Detection Image Mapping (msdyn_AIOdTrainingImage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_aiodtrainingimages(*msdyn_aiodtrainingimageid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_aiodtrainingimages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_aiodtrainingimages(*msdyn_aiodtrainingimageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_aiodtrainingimages(*msdyn_aiodtrainingimageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_aiodtrainingimages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_aiodtrainingimages(*msdyn_aiodtrainingimageid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_aiodtrainingimages(*msdyn_aiodtrainingimageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_aiodtrainingimages(*msdyn_aiodtrainingimageid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AI Object Detection Image Mapping (msdyn_AIOdTrainingImage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AI Object Detection Image Mapping** |
| **DisplayCollectionName** | **AI Object Detection Image Mappings** |
| **SchemaName** | `msdyn_AIOdTrainingImage` |
| **CollectionSchemaName** | `msdyn_AIOdTrainingImages` |
| **EntitySetName** | `msdyn_aiodtrainingimages`|
| **LogicalName** | `msdyn_aiodtrainingimage` |
| **LogicalCollectionName** | `msdyn_aiodtrainingimages` |
| **PrimaryIdAttribute** | `msdyn_aiodtrainingimageid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AIConfigurationId](#BKMK_msdyn_AIConfigurationId)
- [msdyn_AIOdImageId](#BKMK_msdyn_AIOdImageId)
- [msdyn_AIOdTrainingImageId](#BKMK_msdyn_AIOdTrainingImageId)
- [msdyn_LastModifiedDate](#BKMK_msdyn_LastModifiedDate)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_SourceType](#BKMK_msdyn_SourceType)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_AIConfigurationId"></a> msdyn_AIConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for AIConfiguration associated with Training Image.**|
|DisplayName|**AIConfiguration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aiconfigurationid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_aiconfiguration|

### <a name="BKMK_msdyn_AIOdImageId"></a> msdyn_AIOdImageId

|Property|Value|
|---|---|
|Description|**Unique identifier for Image associated with Training Image.**|
|DisplayName|**Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aiodimageid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_aiodimage|

### <a name="BKMK_msdyn_AIOdTrainingImageId"></a> msdyn_AIOdTrainingImageId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Training Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aiodtrainingimageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_LastModifiedDate"></a> msdyn_LastModifiedDate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Last Modified Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lastmodifieddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_SourceType"></a> msdyn_SourceType

|Property|Value|
|---|---|
|Description||
|DisplayName|**SourceType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sourcetype`|
|RequiredLevel|None|
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

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Training Image**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aiodtrainingimage_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Training Image**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aiodtrainingimage_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_msdyn_aiodtrainingimage](#BKMK_business_unit_msdyn_aiodtrainingimage)
- [lk_msdyn_aiodtrainingimage_createdby](#BKMK_lk_msdyn_aiodtrainingimage_createdby)
- [lk_msdyn_aiodtrainingimage_createdonbehalfby](#BKMK_lk_msdyn_aiodtrainingimage_createdonbehalfby)
- [lk_msdyn_aiodtrainingimage_modifiedby](#BKMK_lk_msdyn_aiodtrainingimage_modifiedby)
- [lk_msdyn_aiodtrainingimage_modifiedonbehalfby](#BKMK_lk_msdyn_aiodtrainingimage_modifiedonbehalfby)
- [msdyn_aiconfiguration_msdyn_aiodtrainingimage](#BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage)
- [msdyn_aiodimage_msdyn_aiodtrainingimage](#BKMK_msdyn_aiodimage_msdyn_aiodtrainingimage)
- [owner_msdyn_aiodtrainingimage](#BKMK_owner_msdyn_aiodtrainingimage)
- [team_msdyn_aiodtrainingimage](#BKMK_team_msdyn_aiodtrainingimage)
- [user_msdyn_aiodtrainingimage](#BKMK_user_msdyn_aiodtrainingimage)

### <a name="BKMK_business_unit_msdyn_aiodtrainingimage"></a> business_unit_msdyn_aiodtrainingimage

One-To-Many Relationship: [businessunit business_unit_msdyn_aiodtrainingimage](businessunit.md#BKMK_business_unit_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiodtrainingimage_createdby"></a> lk_msdyn_aiodtrainingimage_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aiodtrainingimage_createdby](systemuser.md#BKMK_lk_msdyn_aiodtrainingimage_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiodtrainingimage_createdonbehalfby"></a> lk_msdyn_aiodtrainingimage_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aiodtrainingimage_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aiodtrainingimage_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiodtrainingimage_modifiedby"></a> lk_msdyn_aiodtrainingimage_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aiodtrainingimage_modifiedby](systemuser.md#BKMK_lk_msdyn_aiodtrainingimage_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiodtrainingimage_modifiedonbehalfby"></a> lk_msdyn_aiodtrainingimage_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aiodtrainingimage_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aiodtrainingimage_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage"></a> msdyn_aiconfiguration_msdyn_aiodtrainingimage

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_msdyn_aiodtrainingimage](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`msdyn_aiconfigurationid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIConfigurationId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiodimage_msdyn_aiodtrainingimage"></a> msdyn_aiodimage_msdyn_aiodtrainingimage

One-To-Many Relationship: [msdyn_aiodimage msdyn_aiodimage_msdyn_aiodtrainingimage](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiodimage`|
|ReferencedAttribute|`msdyn_aiodimageid`|
|ReferencingAttribute|`msdyn_aiodimageid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIOdImageId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_aiodtrainingimage"></a> owner_msdyn_aiodtrainingimage

One-To-Many Relationship: [owner owner_msdyn_aiodtrainingimage](owner.md#BKMK_owner_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_aiodtrainingimage"></a> team_msdyn_aiodtrainingimage

One-To-Many Relationship: [team team_msdyn_aiodtrainingimage](team.md#BKMK_team_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_aiodtrainingimage"></a> user_msdyn_aiodtrainingimage

One-To-Many Relationship: [systemuser user_msdyn_aiodtrainingimage](systemuser.md#BKMK_user_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_aiodtrainingimage_AsyncOperations](#BKMK_msdyn_aiodtrainingimage_AsyncOperations)
- [msdyn_aiodtrainingimage_BulkDeleteFailures](#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures)
- [msdyn_aiodtrainingimage_DuplicateBaseRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)
- [msdyn_aiodtrainingimage_DuplicateMatchingRecord](#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)
- [msdyn_aiodtrainingimage_MailboxTrackingFolders](#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders)
- [msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox](#BKMK_msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox)
- [msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses)
- [msdyn_aiodtrainingimage_ProcessSession](#BKMK_msdyn_aiodtrainingimage_ProcessSession)
- [msdyn_aiodtrainingimage_SyncErrors](#BKMK_msdyn_aiodtrainingimage_SyncErrors)

### <a name="BKMK_msdyn_aiodtrainingimage_AsyncOperations"></a> msdyn_aiodtrainingimage_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_aiodtrainingimage_AsyncOperations](asyncoperation.md#BKMK_msdyn_aiodtrainingimage_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures"></a> msdyn_aiodtrainingimage_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_aiodtrainingimage_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aiodtrainingimage_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord"></a> msdyn_aiodtrainingimage_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_aiodtrainingimage_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_aiodtrainingimage_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord"></a> msdyn_aiodtrainingimage_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_aiodtrainingimage_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_aiodtrainingimage_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders"></a> msdyn_aiodtrainingimage_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_aiodtrainingimage_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aiodtrainingimage_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox"></a> msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox

Many-To-One Relationship: [msdyn_aiodtrainingboundingbox msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencingAttribute|`msdyn_aiodtrainingimageid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_msdyn_aiodtrainingboundingbox`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses"></a> msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_ProcessSession"></a> msdyn_aiodtrainingimage_ProcessSession

Many-To-One Relationship: [processsession msdyn_aiodtrainingimage_ProcessSession](processsession.md#BKMK_msdyn_aiodtrainingimage_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodtrainingimage_SyncErrors"></a> msdyn_aiodtrainingimage_SyncErrors

Many-To-One Relationship: [syncerror msdyn_aiodtrainingimage_SyncErrors](syncerror.md#BKMK_msdyn_aiodtrainingimage_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiodtrainingimage_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_aiodtrainingimage?displayProperty=fullName>
