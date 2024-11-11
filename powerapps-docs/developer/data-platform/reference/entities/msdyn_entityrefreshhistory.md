---
title: "EntityRefreshHistory (msdyn_entityrefreshhistory) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the EntityRefreshHistory (msdyn_entityrefreshhistory) table/entity with Microsoft Dataverse."
ms.date: 11/09/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# EntityRefreshHistory (msdyn_entityrefreshhistory) table/entity reference



## Messages

The following table lists the messages for the EntityRefreshHistory (msdyn_entityrefreshhistory) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_entityrefreshhistories(*msdyn_entityrefreshhistoryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Create`<br />Event: True |`POST` /msdyn_entityrefreshhistories<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_entityrefreshhistories(*msdyn_entityrefreshhistoryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_entityrefreshhistories(*msdyn_entityrefreshhistoryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_entityrefreshhistories<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_entityrefreshhistories(*msdyn_entityrefreshhistoryid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_entityrefreshhistories(*msdyn_entityrefreshhistoryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_entityrefreshhistories(*msdyn_entityrefreshhistoryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the EntityRefreshHistory (msdyn_entityrefreshhistory) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **EntityRefreshHistory** |
| **DisplayCollectionName** | **EntityRefreshHistories** |
| **SchemaName** | `msdyn_entityrefreshhistory` |
| **CollectionSchemaName** | `msdyn_entityrefreshhistories` |
| **EntitySetName** | `msdyn_entityrefreshhistories`|
| **LogicalName** | `msdyn_entityrefreshhistory` |
| **LogicalCollectionName** | `msdyn_entityrefreshhistories` |
| **PrimaryIdAttribute** | `msdyn_entityrefreshhistoryid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_DataflowHistoryLookup](#BKMK_msdyn_DataflowHistoryLookup)
- [msdyn_DataflowId](#BKMK_msdyn_DataflowId)
- [msdyn_DataflowName](#BKMK_msdyn_DataflowName)
- [msdyn_EndTime](#BKMK_msdyn_EndTime)
- [msdyn_EntityName](#BKMK_msdyn_EntityName)
- [msdyn_entityrefreshhistoryId](#BKMK_msdyn_entityrefreshhistoryId)
- [msdyn_ErrorCount](#BKMK_msdyn_ErrorCount)
- [msdyn_ErrorInfoErrorCode](#BKMK_msdyn_ErrorInfoErrorCode)
- [msdyn_ErrorInfoErrorMessage](#BKMK_msdyn_ErrorInfoErrorMessage)
- [msdyn_ErrorInfoEvaluationResultJson](#BKMK_msdyn_ErrorInfoEvaluationResultJson)
- [msdyn_ErrorInfoEvaluationResultJsonMemo](#BKMK_msdyn_ErrorInfoEvaluationResultJsonMemo)
- [msdyn_ErrorInfoLoadToCdsErrorInfoJson](#BKMK_msdyn_ErrorInfoLoadToCdsErrorInfoJson)
- [msdyn_ErrorInfoLoadToCdsErrorInfoJsonMemo](#BKMK_msdyn_ErrorInfoLoadToCdsErrorInfoJsonMemo)
- [msdyn_InsertCount](#BKMK_msdyn_InsertCount)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_RefreshStatus](#BKMK_msdyn_RefreshStatus)
- [msdyn_StartTime](#BKMK_msdyn_StartTime)
- [msdyn_TransactionId](#BKMK_msdyn_TransactionId)
- [msdyn_UpsertCount](#BKMK_msdyn_UpsertCount)
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

### <a name="BKMK_msdyn_DataflowHistoryLookup"></a> msdyn_DataflowHistoryLookup

|Property|Value|
|---|---|
|Description||
|DisplayName|**DataflowHistoryLookup**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_dataflowhistorylookup`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_dataflowrefreshhistory|

### <a name="BKMK_msdyn_DataflowId"></a> msdyn_DataflowId

|Property|Value|
|---|---|
|Description||
|DisplayName|**DataflowId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_dataflowid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_DataflowName"></a> msdyn_DataflowName

|Property|Value|
|---|---|
|Description||
|DisplayName|**DataflowName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_dataflowname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_EndTime"></a> msdyn_EndTime

|Property|Value|
|---|---|
|Description||
|DisplayName|**EndTime**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_EntityName"></a> msdyn_EntityName

|Property|Value|
|---|---|
|Description||
|DisplayName|**EntityName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_entityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_entityrefreshhistoryId"></a> msdyn_entityrefreshhistoryId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**EntityRefreshHistory**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_entityrefreshhistoryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_ErrorCount"></a> msdyn_ErrorCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorCount**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_ErrorInfoErrorCode"></a> msdyn_ErrorInfoErrorCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorInfoErrorCode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorinfoerrorcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_ErrorInfoErrorMessage"></a> msdyn_ErrorInfoErrorMessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorInfoErrorMessage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorinfoerrormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_ErrorInfoEvaluationResultJson"></a> msdyn_ErrorInfoEvaluationResultJson

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorInfoEvaluationResultJson**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorinfoevaluationresultjson`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_ErrorInfoEvaluationResultJsonMemo"></a> msdyn_ErrorInfoEvaluationResultJsonMemo

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorInfoEvaluationResultJsonMemo**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorinfoevaluationresultjsonmemo`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_ErrorInfoLoadToCdsErrorInfoJson"></a> msdyn_ErrorInfoLoadToCdsErrorInfoJson

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorInfoLoadToCdsErrorInfoJson**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorinfoloadtocdserrorinfojson`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_ErrorInfoLoadToCdsErrorInfoJsonMemo"></a> msdyn_ErrorInfoLoadToCdsErrorInfoJsonMemo

|Property|Value|
|---|---|
|Description||
|DisplayName|**ErrorInfoLoadToCdsErrorInfoJsonMemo**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorinfoloadtocdserrorinfojsonmemo`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_InsertCount"></a> msdyn_InsertCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**InsertCount**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_insertcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description|**Required name field**|
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

### <a name="BKMK_msdyn_RefreshStatus"></a> msdyn_RefreshStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**RefreshStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_refreshstatus`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_StartTime"></a> msdyn_StartTime

|Property|Value|
|---|---|
|Description||
|DisplayName|**StartTime**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_starttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_TransactionId"></a> msdyn_TransactionId

|Property|Value|
|---|---|
|Description||
|DisplayName|**TransactionId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_transactionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_UpsertCount"></a> msdyn_UpsertCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**UpsertCount**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_upsertcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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
|Description|**Status of the EntityRefreshHistory**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_entityrefreshhistory_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the EntityRefreshHistory**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_entityrefreshhistory_statuscode`|

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

- [business_unit_msdyn_entityrefreshhistory](#BKMK_business_unit_msdyn_entityrefreshhistory)
- [lk_msdyn_entityrefreshhistory_createdby](#BKMK_lk_msdyn_entityrefreshhistory_createdby)
- [lk_msdyn_entityrefreshhistory_createdonbehalfby](#BKMK_lk_msdyn_entityrefreshhistory_createdonbehalfby)
- [lk_msdyn_entityrefreshhistory_modifiedby](#BKMK_lk_msdyn_entityrefreshhistory_modifiedby)
- [lk_msdyn_entityrefreshhistory_modifiedonbehalfby](#BKMK_lk_msdyn_entityrefreshhistory_modifiedonbehalfby)
- [msdyn_EntityRefreshHistory_DataflowHistor](#BKMK_msdyn_EntityRefreshHistory_DataflowHistor)
- [owner_msdyn_entityrefreshhistory](#BKMK_owner_msdyn_entityrefreshhistory)
- [team_msdyn_entityrefreshhistory](#BKMK_team_msdyn_entityrefreshhistory)
- [user_msdyn_entityrefreshhistory](#BKMK_user_msdyn_entityrefreshhistory)

### <a name="BKMK_business_unit_msdyn_entityrefreshhistory"></a> business_unit_msdyn_entityrefreshhistory

One-To-Many Relationship: [businessunit business_unit_msdyn_entityrefreshhistory](businessunit.md#BKMK_business_unit_msdyn_entityrefreshhistory)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entityrefreshhistory_createdby"></a> lk_msdyn_entityrefreshhistory_createdby

One-To-Many Relationship: [systemuser lk_msdyn_entityrefreshhistory_createdby](systemuser.md#BKMK_lk_msdyn_entityrefreshhistory_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entityrefreshhistory_createdonbehalfby"></a> lk_msdyn_entityrefreshhistory_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_entityrefreshhistory_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_entityrefreshhistory_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entityrefreshhistory_modifiedby"></a> lk_msdyn_entityrefreshhistory_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_entityrefreshhistory_modifiedby](systemuser.md#BKMK_lk_msdyn_entityrefreshhistory_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_entityrefreshhistory_modifiedonbehalfby"></a> lk_msdyn_entityrefreshhistory_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_entityrefreshhistory_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_entityrefreshhistory_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_EntityRefreshHistory_DataflowHistor"></a> msdyn_EntityRefreshHistory_DataflowHistor

One-To-Many Relationship: [msdyn_dataflowrefreshhistory msdyn_EntityRefreshHistory_DataflowHistor](msdyn_dataflowrefreshhistory.md#BKMK_msdyn_EntityRefreshHistory_DataflowHistor)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_dataflowrefreshhistory`|
|ReferencedAttribute|`msdyn_dataflowrefreshhistoryid`|
|ReferencingAttribute|`msdyn_dataflowhistorylookup`|
|ReferencingEntityNavigationPropertyName|`msdyn_DataflowHistoryLookup`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_entityrefreshhistory"></a> owner_msdyn_entityrefreshhistory

One-To-Many Relationship: [owner owner_msdyn_entityrefreshhistory](owner.md#BKMK_owner_msdyn_entityrefreshhistory)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_entityrefreshhistory"></a> team_msdyn_entityrefreshhistory

One-To-Many Relationship: [team team_msdyn_entityrefreshhistory](team.md#BKMK_team_msdyn_entityrefreshhistory)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_entityrefreshhistory"></a> user_msdyn_entityrefreshhistory

One-To-Many Relationship: [systemuser user_msdyn_entityrefreshhistory](systemuser.md#BKMK_user_msdyn_entityrefreshhistory)

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

- [msdyn_entityrefreshhistory_AsyncOperations](#BKMK_msdyn_entityrefreshhistory_AsyncOperations)
- [msdyn_entityrefreshhistory_BulkDeleteFailures](#BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures)
- [msdyn_entityrefreshhistory_DuplicateBaseRecord](#BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord)
- [msdyn_entityrefreshhistory_DuplicateMatchingRecord](#BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord)
- [msdyn_entityrefreshhistory_MailboxTrackingFolders](#BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders)
- [msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses](#BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses)
- [msdyn_entityrefreshhistory_ProcessSession](#BKMK_msdyn_entityrefreshhistory_ProcessSession)
- [msdyn_entityrefreshhistory_SyncErrors](#BKMK_msdyn_entityrefreshhistory_SyncErrors)

### <a name="BKMK_msdyn_entityrefreshhistory_AsyncOperations"></a> msdyn_entityrefreshhistory_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_entityrefreshhistory_AsyncOperations](asyncoperation.md#BKMK_msdyn_entityrefreshhistory_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures"></a> msdyn_entityrefreshhistory_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_entityrefreshhistory_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_entityrefreshhistory_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord"></a> msdyn_entityrefreshhistory_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_entityrefreshhistory_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_entityrefreshhistory_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord"></a> msdyn_entityrefreshhistory_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_entityrefreshhistory_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_entityrefreshhistory_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders"></a> msdyn_entityrefreshhistory_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_entityrefreshhistory_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_entityrefreshhistory_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses"></a> msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_ProcessSession"></a> msdyn_entityrefreshhistory_ProcessSession

Many-To-One Relationship: [processsession msdyn_entityrefreshhistory_ProcessSession](processsession.md#BKMK_msdyn_entityrefreshhistory_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_entityrefreshhistory_SyncErrors"></a> msdyn_entityrefreshhistory_SyncErrors

Many-To-One Relationship: [syncerror msdyn_entityrefreshhistory_SyncErrors](syncerror.md#BKMK_msdyn_entityrefreshhistory_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_entityrefreshhistory_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_entityrefreshhistory?displayProperty=fullName>
