---
title: "flowlog table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the flowlog table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# flowlog table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Automate Online Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /flowlogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /flowlogs(*flowlogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /flowlogs(*flowlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /flowlogs<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /flowlogs(*flowlogid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|Upsert||<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
|UpsertMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|flowlogs|
|DisplayCollectionName|Flow Logs|
|DisplayName|Flow Log|
|EntitySetName|flowlogs|
|IsBPFEntity|False|
|LogicalCollectionName|flowlogs|
|LogicalName|flowlog|
|OwnershipType|None|
|PrimaryIdAttribute|flowlogid|
|PrimaryNameAttribute|name|
|SchemaName|flowlog|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [cloudflowid](#BKMK_cloudflowid)
- [cloudflowrunid](#BKMK_cloudflowrunid)
- [cloudflowrunidPId](#BKMK_cloudflowrunidPId)
- [data](#BKMK_data)
- [desktopflowid](#BKMK_desktopflowid)
- [flowlogId](#BKMK_flowlogId)
- [flowmachinegroupid](#BKMK_flowmachinegroupid)
- [flowmachineid](#BKMK_flowmachineid)
- [flowsessionid](#BKMK_flowsessionid)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [level](#BKMK_level)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [parentobjectid](#BKMK_parentobjectid)
- [parentobjectidIdType](#BKMK_parentobjectidIdType)
- [PartitionId](#BKMK_PartitionId)
- [TTLInSeconds](#BKMK_TTLInSeconds)
- [type](#BKMK_type)
- [workqueueid](#BKMK_workqueueid)
- [workqueueitemid](#BKMK_workqueueitemid)


### <a name="BKMK_cloudflowid"></a> cloudflowid

|Property|Value|
|--------|-----|
|Description|The Power Automate Cloud Flow Id this log is linked to.|
|DisplayName|Cloud Flow Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cloudflowid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_cloudflowrunid"></a> cloudflowrunid

|Property|Value|
|--------|-----|
|Description|The Power Automate Cloud Flow run this log is linked to.|
|DisplayName|Cloud Flow Run Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|cloudflowrunid|
|RequiredLevel|None|
|Targets|flowrun|
|Type|Lookup|


### <a name="BKMK_cloudflowrunidPId"></a> cloudflowrunidPId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|cloudflowrunidpid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_data"></a> data

|Property|Value|
|--------|-----|
|Description|The logged data.|
|DisplayName|Data|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|data|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_desktopflowid"></a> desktopflowid

|Property|Value|
|--------|-----|
|Description|The Desktop Flow Id this log is linked to.|
|DisplayName|Desktop Flow Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|desktopflowid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_flowlogId"></a> flowlogId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Flow Log|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|flowlogid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_flowmachinegroupid"></a> flowmachinegroupid

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|flowmachinegroupid|
|RequiredLevel|None|
|Targets|flowmachinegroup|
|Type|Lookup|


### <a name="BKMK_flowmachineid"></a> flowmachineid

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|flowmachineid|
|RequiredLevel|None|
|Targets|flowmachine|
|Type|Lookup|


### <a name="BKMK_flowsessionid"></a> flowsessionid

|Property|Value|
|--------|-----|
|Description|The Power Automate Desktop Flow Session this log belongs to.|
|DisplayName|Flow Session Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|flowsessionid|
|RequiredLevel|None|
|Targets|flowsession|
|Type|Lookup|


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


### <a name="BKMK_level"></a> level

|Property|Value|
|--------|-----|
|Description|The level of the log.|
|DisplayName|Level|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|level|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### level Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|Verbose||
|100000001|Debug||
|100000002|Info||
|100000003|Warning||
|100000004|Error||



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|The name of the log.|
|DisplayName|Log Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
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


### <a name="BKMK_parentobjectid"></a> parentobjectid

|Property|Value|
|--------|-----|
|Description|The id of the parent object.|
|DisplayName|Parent Object Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentobjectid|
|RequiredLevel|SystemRequired|
|Targets|flowsession|
|Type|Lookup|


### <a name="BKMK_parentobjectidIdType"></a> parentobjectidIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentobjectididtype|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|--------|-----|
|Description|Logical partition id. A logical partition consists of a set of records with same partition id.|
|DisplayName|Partition Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|partitionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|--------|-----|
|Description|Time to live in seconds.|
|DisplayName|Time to live|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ttlinseconds|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_type"></a> type

|Property|Value|
|--------|-----|
|Description|The type of the log.|
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|type|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|100000000|CustomLog||
|100000001|DesktopFlowRunAction||
|100000002|DesktopFlowRunQueuePriorityChanged||
|100000003|DesktopFlowRunQueued||
|100000004|DesktopFlowRunQueueAssigned||
|100000005|DesktopFlowRunQueueAssignFailed||
|100000006|DesktopFlowRunQueueRunConfirmed||
|100000007|DesktopFlowRunQueueRunCompleted||



### <a name="BKMK_workqueueid"></a> workqueueid

|Property|Value|
|--------|-----|
|Description|The Work Queue this log is linked to.|
|DisplayName|Work Queue Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|workqueueid|
|RequiredLevel|None|
|Targets|workqueue|
|Type|Lookup|


### <a name="BKMK_workqueueitemid"></a> workqueueitemid

|Property|Value|
|--------|-----|
|Description|The Work Queue Item this log is linked to.|
|DisplayName|Work Queue Item Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|workqueueitemid|
|RequiredLevel|None|
|Targets|workqueueitem|
|Type|Lookup|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [cloudflowidName](#BKMK_cloudflowidName)
- [cloudflowrunidName](#BKMK_cloudflowrunidName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [desktopflowidName](#BKMK_desktopflowidName)
- [flowmachinegroupidName](#BKMK_flowmachinegroupidName)
- [flowmachineidName](#BKMK_flowmachineidName)
- [flowsessionidName](#BKMK_flowsessionidName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [parentobjectidName](#BKMK_parentobjectidName)
- [parentobjectidYomiName](#BKMK_parentobjectidYomiName)
- [VersionNumber](#BKMK_VersionNumber)
- [workqueueidName](#BKMK_workqueueidName)
- [workqueueitemidName](#BKMK_workqueueitemidName)


### <a name="BKMK_cloudflowidName"></a> cloudflowidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|cloudflowidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_cloudflowrunidName"></a> cloudflowrunidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|cloudflowrunidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_desktopflowidName"></a> desktopflowidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|desktopflowidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_flowmachinegroupidName"></a> flowmachinegroupidName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|flowmachinegroupidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_flowmachineidName"></a> flowmachineidName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|flowmachineidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_flowsessionidName"></a> flowsessionidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|flowsessionidname|
|MaxLength|100|
|RequiredLevel|None|
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


### <a name="BKMK_OwnerId"></a> OwnerId

**Added by**: Active Solution Solution

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


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
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


### <a name="BKMK_parentobjectidName"></a> parentobjectidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentobjectidname|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_parentobjectidYomiName"></a> parentobjectidYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentobjectidyominame|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_workqueueidName"></a> workqueueidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workqueueidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_workqueueitemidName"></a> workqueueitemidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workqueueitemidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_flowlog_createdby](#BKMK_lk_flowlog_createdby)
- [lk_flowlog_createdonbehalfby](#BKMK_lk_flowlog_createdonbehalfby)
- [lk_flowlog_modifiedby](#BKMK_lk_flowlog_modifiedby)
- [lk_flowlog_modifiedonbehalfby](#BKMK_lk_flowlog_modifiedonbehalfby)
- [flowsession_flowlog_parentobjectid](#BKMK_flowsession_flowlog_parentobjectid)
- [flowsession_flowlog_flowsessionid](#BKMK_flowsession_flowlog_flowsessionid)
- [workflow_flowlog_cloudflowid](#BKMK_workflow_flowlog_cloudflowid)
- [flowrun_flowlog_cloudflowrunid](#BKMK_flowrun_flowlog_cloudflowrunid)
- [workflow_flowlog_desktopflowid](#BKMK_workflow_flowlog_desktopflowid)
- [flowmachine_flowlog_flowmachineid](#BKMK_flowmachine_flowlog_flowmachineid)
- [flowmachinegroup_flowlog_flowmachinegroupid](#BKMK_flowmachinegroup_flowlog_flowmachinegroupid)
- [workqueue_flowlog_workqueueid](#BKMK_workqueue_flowlog_workqueueid)
- [workqueueitem_flowlog_workqueueitemid](#BKMK_workqueueitem_flowlog_workqueueitemid)


### <a name="BKMK_lk_flowlog_createdby"></a> lk_flowlog_createdby

**Added by**: System Solution Solution

See the [lk_flowlog_createdby](systemuser.md#BKMK_lk_flowlog_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_flowlog_createdonbehalfby"></a> lk_flowlog_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_flowlog_createdonbehalfby](systemuser.md#BKMK_lk_flowlog_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_flowlog_modifiedby"></a> lk_flowlog_modifiedby

**Added by**: System Solution Solution

See the [lk_flowlog_modifiedby](systemuser.md#BKMK_lk_flowlog_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_flowlog_modifiedonbehalfby"></a> lk_flowlog_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_flowlog_modifiedonbehalfby](systemuser.md#BKMK_lk_flowlog_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_flowsession_flowlog_parentobjectid"></a> flowsession_flowlog_parentobjectid

**Added by**: Power Automate Core Components Solution

See the [flowsession_flowlog_parentobjectid](flowsession.md#BKMK_flowsession_flowlog_parentobjectid) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_flowsession_flowlog_flowsessionid"></a> flowsession_flowlog_flowsessionid

**Added by**: Power Automate Core Components Solution

See the [flowsession_flowlog_flowsessionid](flowsession.md#BKMK_flowsession_flowlog_flowsessionid) one-to-many relationship for the [flowsession](flowsession.md) table/entity.

### <a name="BKMK_workflow_flowlog_cloudflowid"></a> workflow_flowlog_cloudflowid

**Added by**: System Solution Solution

See the [workflow_flowlog_cloudflowid](workflow.md#BKMK_workflow_flowlog_cloudflowid) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_flowrun_flowlog_cloudflowrunid"></a> flowrun_flowlog_cloudflowrunid

See the [flowrun_flowlog_cloudflowrunid](flowrun.md#BKMK_flowrun_flowlog_cloudflowrunid) one-to-many relationship for the [flowrun](flowrun.md) table/entity.

### <a name="BKMK_workflow_flowlog_desktopflowid"></a> workflow_flowlog_desktopflowid

**Added by**: System Solution Solution

See the [workflow_flowlog_desktopflowid](workflow.md#BKMK_workflow_flowlog_desktopflowid) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_flowmachine_flowlog_flowmachineid"></a> flowmachine_flowlog_flowmachineid

**Added by**: Power Automate Core Components Solution

See the [flowmachine_flowlog_flowmachineid](flowmachine.md#BKMK_flowmachine_flowlog_flowmachineid) one-to-many relationship for the [flowmachine](flowmachine.md) table/entity.

### <a name="BKMK_flowmachinegroup_flowlog_flowmachinegroupid"></a> flowmachinegroup_flowlog_flowmachinegroupid

**Added by**: Power Automate Core Components Solution

See the [flowmachinegroup_flowlog_flowmachinegroupid](flowmachinegroup.md#BKMK_flowmachinegroup_flowlog_flowmachinegroupid) one-to-many relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

### <a name="BKMK_workqueue_flowlog_workqueueid"></a> workqueue_flowlog_workqueueid

**Added by**: Power Automate Core Components Solution

See the [workqueue_flowlog_workqueueid](workqueue.md#BKMK_workqueue_flowlog_workqueueid) one-to-many relationship for the [workqueue](workqueue.md) table/entity.

### <a name="BKMK_workqueueitem_flowlog_workqueueitemid"></a> workqueueitem_flowlog_workqueueitemid

**Added by**: Power Automate Core Components Solution

See the [workqueueitem_flowlog_workqueueitemid](workqueueitem.md#BKMK_workqueueitem_flowlog_workqueueitemid) one-to-many relationship for the [workqueueitem](workqueueitem.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.flowlog?text=flowlog EntityType" />