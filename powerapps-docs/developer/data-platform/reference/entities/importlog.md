---
title: "Import Log (ImportLog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Import Log (ImportLog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Import Log (ImportLog) table/entity reference (Microsoft Dataverse)

Failure reason and other detailed information for a record that failed to import.

## Messages

The following table lists the messages for the Import Log (ImportLog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /importlogs(*importlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /importlogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Import Log (ImportLog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Import Log** |
| **DisplayCollectionName** | **ImportLogs** |
| **SchemaName** | `ImportLog` |
| **CollectionSchemaName** | `ImportLogs` |
| **EntitySetName** | `importlogs`|
| **LogicalName** | `importlog` |
| **LogicalCollectionName** | `importlogs` |
| **PrimaryIdAttribute** | `importlogid` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdditionalInfo](#BKMK_AdditionalInfo)
- [ColumnValue](#BKMK_ColumnValue)
- [ErrorDescription](#BKMK_ErrorDescription)
- [ErrorNumber](#BKMK_ErrorNumber)
- [HeaderColumn](#BKMK_HeaderColumn)
- [ImportDataId](#BKMK_ImportDataId)
- [ImportFileId](#BKMK_ImportFileId)
- [ImportLogId](#BKMK_ImportLogId)
- [LineNumber](#BKMK_LineNumber)
- [LogPhaseCode](#BKMK_LogPhaseCode)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [StatusCode](#BKMK_StatusCode)

### <a name="BKMK_AdditionalInfo"></a> AdditionalInfo

|Property|Value|
|---|---|
|Description|**Additional information related to the error.**|
|DisplayName|**More Information**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`additionalinfo`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_ColumnValue"></a> ColumnValue

|Property|Value|
|---|---|
|Description|**Value in the column.**|
|DisplayName|**Column Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`columnvalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

### <a name="BKMK_ErrorDescription"></a> ErrorDescription

|Property|Value|
|---|---|
|Description|**Description of an error.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errordescription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_ErrorNumber"></a> ErrorNumber

|Property|Value|
|---|---|
|Description|**Error code of an error.**|
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`errornumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|10000000|
|MinValue|0|

### <a name="BKMK_HeaderColumn"></a> HeaderColumn

|Property|Value|
|---|---|
|Description|**Name of the column heading.**|
|DisplayName|**Column Heading**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`headercolumn`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ImportDataId"></a> ImportDataId

|Property|Value|
|---|---|
|Description|**Unique identifier of the import data for this import log.**|
|DisplayName|**Source Row**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importdataid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|importdata|

### <a name="BKMK_ImportFileId"></a> ImportFileId

|Property|Value|
|---|---|
|Description|**Unique identifier of the import file for this import log.**|
|DisplayName|**Import File Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`importfileid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|importfile|

### <a name="BKMK_ImportLogId"></a> ImportLogId

|Property|Value|
|---|---|
|Description|**Unique identifier of the import log.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importlogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_LineNumber"></a> LineNumber

|Property|Value|
|---|---|
|Description|**Original line number of the data used in this log.**|
|DisplayName|**Original Row Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`linenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|10000000|
|MinValue|0|

### <a name="BKMK_LogPhaseCode"></a> LogPhaseCode

|Property|Value|
|---|---|
|Description|**Phase for which the log is recorded.**|
|DisplayName|**Log Phase**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`logphasecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`importlog_logphasecode`|

#### LogPhaseCode Choices/Options

|Value|Label|
|---|---|
|0|**Parse**|
|1|**Transform**|
|2|**Import Create**|
|3|**Import Update**|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the import log.**|
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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the import log.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`importlog_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />State:0<br />TransitionData: None|


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
- [SequenceNumber](#BKMK_SequenceNumber)
- [StateCode](#BKMK_StateCode)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the import log.**|
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
|Description|**Date and time when the import log was created.**|
|DisplayName|**Created On**|
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
|Description|**Unique identifier of the delegate user who created the importlog.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the import log.**|
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
|Description|**Date and time when the import log was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the importlog.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
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
|Description||
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
|Description|**Business unit that owns the import log.**|
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
|Description|**Unique identifier of the team who owns the import log.**|
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
|Description|**Unique identifier of the user who owns the import log.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_SequenceNumber"></a> SequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the error in this log.**|
|DisplayName|**Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sequencenumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|10000000|
|MinValue|0|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the import log.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`importlog_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 0<br />InvariantName: `Active`|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [BusinessUnit_ImportLogs](#BKMK_BusinessUnit_ImportLogs)
- [ImportLog_ImportData](#BKMK_ImportLog_ImportData)
- [ImportLog_ImportFile](#BKMK_ImportLog_ImportFile)
- [lk_importlog_createdonbehalfby](#BKMK_lk_importlog_createdonbehalfby)
- [lk_importlog_modifiedonbehalfby](#BKMK_lk_importlog_modifiedonbehalfby)
- [lk_importlogbase_createdby](#BKMK_lk_importlogbase_createdby)
- [lk_importlogbase_modifiedby](#BKMK_lk_importlogbase_modifiedby)
- [owner_importlogs](#BKMK_owner_importlogs)
- [SystemUser_ImportLogs](#BKMK_SystemUser_ImportLogs)
- [team_ImportLogs](#BKMK_team_ImportLogs)

### <a name="BKMK_BusinessUnit_ImportLogs"></a> BusinessUnit_ImportLogs

One-To-Many Relationship: [businessunit BusinessUnit_ImportLogs](businessunit.md#BKMK_BusinessUnit_ImportLogs)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportLog_ImportData"></a> ImportLog_ImportData

One-To-Many Relationship: [importdata ImportLog_ImportData](importdata.md#BKMK_ImportLog_ImportData)

|Property|Value|
|---|---|
|ReferencedEntity|`importdata`|
|ReferencedAttribute|`importdataid`|
|ReferencingAttribute|`importdataid`|
|ReferencingEntityNavigationPropertyName|`importdataid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_ImportLog_ImportFile"></a> ImportLog_ImportFile

One-To-Many Relationship: [importfile ImportLog_ImportFile](importfile.md#BKMK_ImportLog_ImportFile)

|Property|Value|
|---|---|
|ReferencedEntity|`importfile`|
|ReferencedAttribute|`importfileid`|
|ReferencingAttribute|`importfileid`|
|ReferencingEntityNavigationPropertyName|`importfileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importlog_createdonbehalfby"></a> lk_importlog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_importlog_createdonbehalfby](systemuser.md#BKMK_lk_importlog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importlog_modifiedonbehalfby"></a> lk_importlog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_importlog_modifiedonbehalfby](systemuser.md#BKMK_lk_importlog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importlogbase_createdby"></a> lk_importlogbase_createdby

One-To-Many Relationship: [systemuser lk_importlogbase_createdby](systemuser.md#BKMK_lk_importlogbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_importlogbase_modifiedby"></a> lk_importlogbase_modifiedby

One-To-Many Relationship: [systemuser lk_importlogbase_modifiedby](systemuser.md#BKMK_lk_importlogbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_importlogs"></a> owner_importlogs

One-To-Many Relationship: [owner owner_importlogs](owner.md#BKMK_owner_importlogs)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_SystemUser_ImportLogs"></a> SystemUser_ImportLogs

One-To-Many Relationship: [systemuser SystemUser_ImportLogs](systemuser.md#BKMK_SystemUser_ImportLogs)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_ImportLogs"></a> team_ImportLogs

One-To-Many Relationship: [team team_ImportLogs](team.md#BKMK_team_ImportLogs)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [ImportLog_AsyncOperations](#BKMK_ImportLog_AsyncOperations)
- [ImportLog_BulkDeleteFailures](#BKMK_ImportLog_BulkDeleteFailures)

### <a name="BKMK_ImportLog_AsyncOperations"></a> ImportLog_AsyncOperations

Many-To-One Relationship: [asyncoperation ImportLog_AsyncOperations](asyncoperation.md#BKMK_ImportLog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportLog_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ImportLog_BulkDeleteFailures"></a> ImportLog_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure ImportLog_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportLog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ImportLog_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.importlog?displayProperty=fullName>
