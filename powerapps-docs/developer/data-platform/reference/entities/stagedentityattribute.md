---
title: "Staged Entity Attribute (StagedEntityAttribute) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Staged Entity Attribute (StagedEntityAttribute) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Staged Entity Attribute (StagedEntityAttribute) table/entity reference (Microsoft Dataverse)

Stores staged entity attribute metadata to be processed in async.

## Messages

The following table lists the messages for the Staged Entity Attribute (StagedEntityAttribute) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /stagedentityattributes<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /stagedentityattributes(*stagedentityattributeid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /stagedentityattributes(*stagedentityattributeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /stagedentityattributes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /stagedentityattributes(*stagedentityattributeid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /stagedentityattributes(*stagedentityattributeid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Staged Entity Attribute (StagedEntityAttribute) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Staged Entity Attribute** |
| **DisplayCollectionName** | **Staged Entity Attribute** |
| **SchemaName** | `StagedEntityAttribute` |
| **CollectionSchemaName** | `StagedEntityAttributes` |
| **EntitySetName** | `stagedentityattributes`|
| **LogicalName** | `stagedentityattribute` |
| **LogicalCollectionName** | `stagedentityattributes` |
| **PrimaryIdAttribute** | `stagedentityattributeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeDescription](#BKMK_AttributeDescription)
- [AttributeOf](#BKMK_AttributeOf)
- [AttributeTypeId](#BKMK_AttributeTypeId)
- [ComponentState](#BKMK_ComponentState)
- [EntityId](#BKMK_EntityId)
- [ExternalName](#BKMK_ExternalName)
- [HasMultipleLabels](#BKMK_HasMultipleLabels)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsLogical](#BKMK_IsLogical)
- [IsPKAttribute](#BKMK_IsPKAttribute)
- [LogicalName](#BKMK_LogicalName)
- [Name](#BKMK_Name)
- [OriginalLocalizedDescription](#BKMK_OriginalLocalizedDescription)
- [OriginalLocalizedName](#BKMK_OriginalLocalizedName)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PhysicalName](#BKMK_PhysicalName)
- [SolutionId](#BKMK_SolutionId)
- [StagedEntityAttributeId](#BKMK_StagedEntityAttributeId)
- [StagingExecutionContextId](#BKMK_StagingExecutionContextId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [ValidForReadAPI](#BKMK_ValidForReadAPI)

### <a name="BKMK_AttributeDescription"></a> AttributeDescription

|Property|Value|
|---|---|
|Description|**The attribute decription with properties for async metadata creation**|
|DisplayName|**AttributeDescription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributedescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8000|

### <a name="BKMK_AttributeOf"></a> AttributeOf

|Property|Value|
|---|---|
|Description|**The id of the parent attribute.**|
|DisplayName|**Attribute of**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributeof`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_AttributeTypeId"></a> AttributeTypeId

|Property|Value|
|---|---|
|Description|**The AttributeTypeId for staged attribute.**|
|DisplayName|**AttributeTypeId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributetypeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**ComponentState for staged attribute**|
|DisplayName|**ComponentState**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue||
|MinValue||

### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|---|---|
|Description|**The ID of the entity for staged attribute.**|
|DisplayName|**EntityId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ExternalName"></a> ExternalName

|Property|Value|
|---|---|
|Description|**The external name of the staged attribute for virtual entity.**|
|DisplayName|**External Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`externalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_HasMultipleLabels"></a> HasMultipleLabels

|Property|Value|
|---|---|
|Description|**Determines if Staged Attribute has multiple labels**|
|DisplayName|**HasMultipleLabels**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`hasmultiplelabels`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedentityattribute_hasmultiplelabels`|
|DefaultValue|False|
|True Label||
|False Label||

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

### <a name="BKMK_IsLogical"></a> IsLogical

|Property|Value|
|---|---|
|Description|**Determines if Staged Attribute IsLogical**|
|DisplayName|**IsLogical**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`islogical`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedentityattribute_islogical`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_IsPKAttribute"></a> IsPKAttribute

|Property|Value|
|---|---|
|Description|**Determines if Staged Attribute is Primary Key**|
|DisplayName|**IsPKAttribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ispkattribute`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedentityattribute_ispkattribute`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|---|---|
|Description|**The LogicalName of the staged attribute.**|
|DisplayName|**LogicalName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the staged attribute.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_OriginalLocalizedDescription"></a> OriginalLocalizedDescription

|Property|Value|
|---|---|
|Description|**The localized description of the attribute.**|
|DisplayName|**OriginalLocalizedDescription**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedescription`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8000|

### <a name="BKMK_OriginalLocalizedName"></a> OriginalLocalizedName

|Property|Value|
|---|---|
|Description|**The original localized name of the staged attribute.**|
|DisplayName|**Original Localized Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`originallocalizedname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

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

### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|---|---|
|Description|**The PhysicalName of the staged attribute.**|
|DisplayName|**PhysicalName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`physicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**The SolutionId for staged attribute.**|
|DisplayName|**SolutionId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StagedEntityAttributeId"></a> StagedEntityAttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity attribute instances**|
|DisplayName|**Staged Entity Attribute identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stagedentityattributeid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_StagingExecutionContextId"></a> StagingExecutionContextId

|Property|Value|
|---|---|
|Description|**A unique identifier used to tie together all objects staged within the same transaction.**|
|DisplayName|**Staging Execution Context Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagingexecutioncontextid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Staged Entity Attribute**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`stagedentityattribute_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Staged Entity Attribute**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`stagedentityattribute_statuscode`|

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

### <a name="BKMK_ValidForReadAPI"></a> ValidForReadAPI

|Property|Value|
|---|---|
|Description|**Determines if Staged Attribute is ValidForReadAPI**|
|DisplayName|**ValidForReadAPI**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`validforreadapi`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_stagedentityattribute_validforreadapi`|
|DefaultValue|False|
|True Label||
|False Label||


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
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

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**OverwriteTime for staged attribute.**|
|DisplayName|**OverwriteTime**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

- [lk_stagedentityattribute_createdby](#BKMK_lk_stagedentityattribute_createdby)
- [lk_stagedentityattribute_createdonbehalfby](#BKMK_lk_stagedentityattribute_createdonbehalfby)
- [lk_stagedentityattribute_modifiedby](#BKMK_lk_stagedentityattribute_modifiedby)
- [lk_stagedentityattribute_modifiedonbehalfby](#BKMK_lk_stagedentityattribute_modifiedonbehalfby)

### <a name="BKMK_lk_stagedentityattribute_createdby"></a> lk_stagedentityattribute_createdby

One-To-Many Relationship: [systemuser lk_stagedentityattribute_createdby](systemuser.md#BKMK_lk_stagedentityattribute_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedentityattribute_createdonbehalfby"></a> lk_stagedentityattribute_createdonbehalfby

One-To-Many Relationship: [systemuser lk_stagedentityattribute_createdonbehalfby](systemuser.md#BKMK_lk_stagedentityattribute_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedentityattribute_modifiedby"></a> lk_stagedentityattribute_modifiedby

One-To-Many Relationship: [systemuser lk_stagedentityattribute_modifiedby](systemuser.md#BKMK_lk_stagedentityattribute_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_stagedentityattribute_modifiedonbehalfby"></a> lk_stagedentityattribute_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_stagedentityattribute_modifiedonbehalfby](systemuser.md#BKMK_lk_stagedentityattribute_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [stagedentityattribute_AsyncOperations](#BKMK_stagedentityattribute_AsyncOperations)
- [stagedentityattribute_BulkDeleteFailures](#BKMK_stagedentityattribute_BulkDeleteFailures)
- [stagedentityattribute_MailboxTrackingFolders](#BKMK_stagedentityattribute_MailboxTrackingFolders)
- [stagedentityattribute_PrincipalObjectAttributeAccesses](#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses)
- [stagedentityattribute_ProcessSession](#BKMK_stagedentityattribute_ProcessSession)
- [stagedentityattribute_SyncErrors](#BKMK_stagedentityattribute_SyncErrors)

### <a name="BKMK_stagedentityattribute_AsyncOperations"></a> stagedentityattribute_AsyncOperations

Many-To-One Relationship: [asyncoperation stagedentityattribute_AsyncOperations](asyncoperation.md#BKMK_stagedentityattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentityattribute_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentityattribute_BulkDeleteFailures"></a> stagedentityattribute_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure stagedentityattribute_BulkDeleteFailures](bulkdeletefailure.md#BKMK_stagedentityattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentityattribute_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentityattribute_MailboxTrackingFolders"></a> stagedentityattribute_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder stagedentityattribute_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_stagedentityattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentityattribute_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses"></a> stagedentityattribute_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess stagedentityattribute_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`stagedentityattribute_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentityattribute_ProcessSession"></a> stagedentityattribute_ProcessSession

Many-To-One Relationship: [processsession stagedentityattribute_ProcessSession](processsession.md#BKMK_stagedentityattribute_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentityattribute_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_stagedentityattribute_SyncErrors"></a> stagedentityattribute_SyncErrors

Many-To-One Relationship: [syncerror stagedentityattribute_SyncErrors](syncerror.md#BKMK_stagedentityattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`stagedentityattribute_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.stagedentityattribute?displayProperty=fullName>
