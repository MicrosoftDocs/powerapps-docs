---
title: "StagedEntityAttribute table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the StagedEntityAttribute table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# StagedEntityAttribute table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Stores staged entity attribute metadata to be processed in async.

**Added by**: Metadata Extension Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /stagedentityattributes<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /stagedentityattributes(*stagedentityattributeid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /stagedentityattributes(*stagedentityattributeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /stagedentityattributes<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /stagedentityattributes(*stagedentityattributeid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|StagedEntityAttributes|
|DisplayCollectionName|Staged Entity Attribute|
|DisplayName|Staged Entity Attribute|
|EntitySetName|stagedentityattributes|
|IsBPFEntity|False|
|LogicalCollectionName|stagedentityattributes|
|LogicalName|stagedentityattribute|
|OwnershipType|None|
|PrimaryIdAttribute|stagedentityattributeid|
|PrimaryNameAttribute|name|
|SchemaName|StagedEntityAttribute|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeDescription](#BKMK_AttributeDescription)
- [AttributeTypeId](#BKMK_AttributeTypeId)
- [ComponentState](#BKMK_ComponentState)
- [EntityId](#BKMK_EntityId)
- [HasMultipleLabels](#BKMK_HasMultipleLabels)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsLogical](#BKMK_IsLogical)
- [IsPKAttribute](#BKMK_IsPKAttribute)
- [LogicalName](#BKMK_LogicalName)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PhysicalName](#BKMK_PhysicalName)
- [SolutionId](#BKMK_SolutionId)
- [StagedEntityAttributeId](#BKMK_StagedEntityAttributeId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [ValidForReadAPI](#BKMK_ValidForReadAPI)


### <a name="BKMK_AttributeDescription"></a> AttributeDescription

|Property|Value|
|--------|-----|
|Description|The attribute decription with properties for async metadata creation|
|DisplayName|AttributeDescription|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|attributedescription|
|MaxLength|8000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_AttributeTypeId"></a> AttributeTypeId

|Property|Value|
|--------|-----|
|Description|The AttributeTypeId for staged attribute.|
|DisplayName|AttributeTypeId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|attributetypeid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|ComponentState for staged attribute|
|DisplayName|ComponentState|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|componentstate|
|MaxValue||
|MinValue||
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|--------|-----|
|Description|The ID of the entity for staged attribute.|
|DisplayName|EntityId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entityid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_HasMultipleLabels"></a> HasMultipleLabels

|Property|Value|
|--------|-----|
|Description|Determines if Staged Attribute has multiple labels|
|DisplayName|HasMultipleLabels|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|hasmultiplelabels|
|RequiredLevel|None|
|Type|Boolean|

#### HasMultipleLabels Choices/Options

|Value|Label|Description|
|-----|-----|--------|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
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


### <a name="BKMK_IsLogical"></a> IsLogical

|Property|Value|
|--------|-----|
|Description|Determines if Staged Attribute IsLogical|
|DisplayName|IsLogical|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|islogical|
|RequiredLevel|None|
|Type|Boolean|

#### IsLogical Choices/Options

|Value|Label|Description|
|-----|-----|--------|


### <a name="BKMK_IsPKAttribute"></a> IsPKAttribute

|Property|Value|
|--------|-----|
|Description|Determines if Staged Attribute is Primary Key|
|DisplayName|IsPKAttribute|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ispkattribute|
|RequiredLevel|None|
|Type|Boolean|

#### IsPKAttribute Choices/Options

|Value|Label|Description|
|-----|-----|--------|


### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|--------|-----|
|Description|The LogicalName of the staged attribute.|
|DisplayName|LogicalName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of the staged attribute.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|128|
|RequiredLevel|None|
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


### <a name="BKMK_PhysicalName"></a> PhysicalName

|Property|Value|
|--------|-----|
|Description|The PhysicalName of the staged attribute.|
|DisplayName|PhysicalName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|physicalname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|The SolutionId for staged attribute.|
|DisplayName|SolutionId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_StagedEntityAttributeId"></a> StagedEntityAttributeId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity attribute instances|
|DisplayName|Staged Entity Attribute identifier|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|stagedentityattributeid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Staged Entity Attribute|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Staged Entity Attribute|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ValidForReadAPI"></a> ValidForReadAPI

|Property|Value|
|--------|-----|
|Description|Determines if Staged Attribute is ValidForReadAPI|
|DisplayName|ValidForReadAPI|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|validforreadapi|
|RequiredLevel|None|
|Type|Boolean|

#### ValidForReadAPI Choices/Options

|Value|Label|Description|
|-----|-----|--------|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|OverwriteTime for staged attribute.|
|DisplayName|OverwriteTime|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
|DisplayName|Version Number|
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

- [stagedentityattribute_SyncErrors](#BKMK_stagedentityattribute_SyncErrors)
- [stagedentityattribute_AsyncOperations](#BKMK_stagedentityattribute_AsyncOperations)
- [stagedentityattribute_MailboxTrackingFolders](#BKMK_stagedentityattribute_MailboxTrackingFolders)
- [stagedentityattribute_ProcessSession](#BKMK_stagedentityattribute_ProcessSession)
- [stagedentityattribute_BulkDeleteFailures](#BKMK_stagedentityattribute_BulkDeleteFailures)
- [stagedentityattribute_PrincipalObjectAttributeAccesses](#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses)


### <a name="BKMK_stagedentityattribute_SyncErrors"></a> stagedentityattribute_SyncErrors

**Added by**: System Solution Solution

Same as the [stagedentityattribute_SyncErrors](syncerror.md#BKMK_stagedentityattribute_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|stagedentityattribute_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_stagedentityattribute_AsyncOperations"></a> stagedentityattribute_AsyncOperations

**Added by**: System Solution Solution

Same as the [stagedentityattribute_AsyncOperations](asyncoperation.md#BKMK_stagedentityattribute_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|stagedentityattribute_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_stagedentityattribute_MailboxTrackingFolders"></a> stagedentityattribute_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [stagedentityattribute_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_stagedentityattribute_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|stagedentityattribute_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_stagedentityattribute_ProcessSession"></a> stagedentityattribute_ProcessSession

**Added by**: System Solution Solution

Same as the [stagedentityattribute_ProcessSession](processsession.md#BKMK_stagedentityattribute_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|stagedentityattribute_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_stagedentityattribute_BulkDeleteFailures"></a> stagedentityattribute_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [stagedentityattribute_BulkDeleteFailures](bulkdeletefailure.md#BKMK_stagedentityattribute_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|stagedentityattribute_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses"></a> stagedentityattribute_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [stagedentityattribute_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_stagedentityattribute_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|stagedentityattribute_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_stagedentityattribute_createdby](#BKMK_lk_stagedentityattribute_createdby)
- [lk_stagedentityattribute_createdonbehalfby](#BKMK_lk_stagedentityattribute_createdonbehalfby)
- [lk_stagedentityattribute_modifiedby](#BKMK_lk_stagedentityattribute_modifiedby)
- [lk_stagedentityattribute_modifiedonbehalfby](#BKMK_lk_stagedentityattribute_modifiedonbehalfby)


### <a name="BKMK_lk_stagedentityattribute_createdby"></a> lk_stagedentityattribute_createdby

**Added by**: System Solution Solution

See the [lk_stagedentityattribute_createdby](systemuser.md#BKMK_lk_stagedentityattribute_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_stagedentityattribute_createdonbehalfby"></a> lk_stagedentityattribute_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_stagedentityattribute_createdonbehalfby](systemuser.md#BKMK_lk_stagedentityattribute_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_stagedentityattribute_modifiedby"></a> lk_stagedentityattribute_modifiedby

**Added by**: System Solution Solution

See the [lk_stagedentityattribute_modifiedby](systemuser.md#BKMK_lk_stagedentityattribute_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_stagedentityattribute_modifiedonbehalfby"></a> lk_stagedentityattribute_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_stagedentityattribute_modifiedonbehalfby](systemuser.md#BKMK_lk_stagedentityattribute_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.stagedentityattribute?text=stagedentityattribute EntityType" />