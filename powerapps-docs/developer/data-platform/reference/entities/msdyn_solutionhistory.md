---
title: "Solution History (msdyn_solutionhistory) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution History (msdyn_solutionhistory) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution History (msdyn_solutionhistory) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Solution History (msdyn_solutionhistory) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Create`<br />Event: True |`POST` /msdyn_solutionhistories<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Retrieve`<br />Event: True |`GET` /msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_solutionhistories<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_solutionhistories(*msdyn_solutionhistoryid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Solution History (msdyn_solutionhistory) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution History** |
| **DisplayCollectionName** | **Solutions History** |
| **SchemaName** | `msdyn_solutionhistory` |
| **CollectionSchemaName** | `msdyn_solutionhistories` |
| **EntitySetName** | `msdyn_solutionhistories`|
| **LogicalName** | `msdyn_solutionhistory` |
| **LogicalCollectionName** | `msdyn_solutionhistories` |
| **PrimaryIdAttribute** | `msdyn_solutionhistoryid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_activityid](#BKMK_msdyn_activityid)
- [msdyn_correlationid](#BKMK_msdyn_correlationid)
- [msdyn_endtime](#BKMK_msdyn_endtime)
- [msdyn_errorcode](#BKMK_msdyn_errorcode)
- [msdyn_exceptionmessage](#BKMK_msdyn_exceptionmessage)
- [msdyn_exceptionstack](#BKMK_msdyn_exceptionstack)
- [msdyn_ismanaged](#BKMK_msdyn_ismanaged)
- [msdyn_isoverwritecustomizations](#BKMK_msdyn_isoverwritecustomizations)
- [msdyn_ispatch](#BKMK_msdyn_ispatch)
- [msdyn_maxretries](#BKMK_msdyn_maxretries)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_operation](#BKMK_msdyn_operation)
- [msdyn_packagename](#BKMK_msdyn_packagename)
- [msdyn_packageversion](#BKMK_msdyn_packageversion)
- [msdyn_publisherid](#BKMK_msdyn_publisherid)
- [msdyn_publishername](#BKMK_msdyn_publishername)
- [msdyn_result](#BKMK_msdyn_result)
- [msdyn_retrycount](#BKMK_msdyn_retrycount)
- [msdyn_solutionhistorydescription](#BKMK_msdyn_solutionhistorydescription)
- [msdyn_solutionhistoryId](#BKMK_msdyn_solutionhistoryId)
- [msdyn_solutionid](#BKMK_msdyn_solutionid)
- [msdyn_solutionversion](#BKMK_msdyn_solutionversion)
- [msdyn_starttime](#BKMK_msdyn_starttime)
- [msdyn_status](#BKMK_msdyn_status)
- [msdyn_suboperation](#BKMK_msdyn_suboperation)
- [msdyn_totaltime](#BKMK_msdyn_totaltime)

### <a name="BKMK_msdyn_activityid"></a> msdyn_activityid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Activity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_activityid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_correlationid"></a> msdyn_correlationid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Correlation Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_correlationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_endtime"></a> msdyn_endtime

|Property|Value|
|---|---|
|Description||
|DisplayName|**End Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_errorcode"></a> msdyn_errorcode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Error Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_exceptionmessage"></a> msdyn_exceptionmessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Exception Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_exceptionmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_exceptionstack"></a> msdyn_exceptionstack

|Property|Value|
|---|---|
|Description||
|DisplayName|**Exception Stack**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_exceptionstack`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_ismanaged"></a> msdyn_ismanaged

|Property|Value|
|---|---|
|Description||
|DisplayName|**Managed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ismanaged`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_ismanaged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_isoverwritecustomizations"></a> msdyn_isoverwritecustomizations

|Property|Value|
|---|---|
|Description||
|DisplayName|**Overwrite Customizations**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isoverwritecustomizations`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_isoverwritecustomizations`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_ispatch"></a> msdyn_ispatch

|Property|Value|
|---|---|
|Description||
|DisplayName|**Patch**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ispatch`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_ispatch`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_maxretries"></a> msdyn_maxretries

|Property|Value|
|---|---|
|Description|**Maximum number of retries.**|
|DisplayName|**Maximum Retries**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_maxretries`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Solution Name**|
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

### <a name="BKMK_msdyn_operation"></a> msdyn_operation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Operation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_operation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_operation`|

#### msdyn_operation Choices/Options

|Value|Label|
|---|---|
|0|**Import**|
|1|**Uninstall**|
|2|**Export**|
|3|**Publish**|
|4|**PublishAll**|
|5|**LanguageProvision**|
|6|**ImportTranslation**|
|7|**RibbonMetadataGeneration**|
|8|**WorkflowSetState**|
|9|**None**|
|10|**ExportLite**|
|11|**UpdatingMissingPackages**|

### <a name="BKMK_msdyn_packagename"></a> msdyn_packagename

|Property|Value|
|---|---|
|Description||
|DisplayName|**Package Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_packagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_packageversion"></a> msdyn_packageversion

|Property|Value|
|---|---|
|Description||
|DisplayName|**Package Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_packageversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_publisherid"></a> msdyn_publisherid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Publisher Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_publisherid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_publishername"></a> msdyn_publishername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Publisher Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_publishername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_msdyn_result"></a> msdyn_result

|Property|Value|
|---|---|
|Description||
|DisplayName|**Result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_result`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_result`|
|DefaultValue|False|
|True Label|Success|
|False Label|Failure|

### <a name="BKMK_msdyn_retrycount"></a> msdyn_retrycount

|Property|Value|
|---|---|
|Description|**Retry count**|
|DisplayName|**Retry count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_retrycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_solutionhistorydescription"></a> msdyn_solutionhistorydescription

|Property|Value|
|---|---|
|Description|**Comments associated with solution installation**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionhistorydescription`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_msdyn_solutionhistoryId"></a> msdyn_solutionhistoryId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Solutionhistory**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionhistoryid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_solutionid"></a> msdyn_solutionid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_solutionversion"></a> msdyn_solutionversion

|Property|Value|
|---|---|
|Description||
|DisplayName|**Solution Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_starttime"></a> msdyn_starttime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_starttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_status"></a> msdyn_status

|Property|Value|
|---|---|
|Description||
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_status`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_status`|

#### msdyn_status Choices/Options

|Value|Label|
|---|---|
|0|**Started**|
|1|**Completed**|
|2|**Queued**|

### <a name="BKMK_msdyn_suboperation"></a> msdyn_suboperation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Suboperation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_suboperation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_solutionhistory_msdyn_suboperation`|

#### msdyn_suboperation Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**New**|
|2|**Upgrade**|
|3|**Update**|
|4|**Delete**|
|5|**InlineUpgrade**|
|6|**WaitingForMissingPackages**|
|7|**InstalledMissingPackages**|
|8|**FailedInstallingMissingPackages**|

### <a name="BKMK_msdyn_totaltime"></a> msdyn_totaltime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Total Time (seconds)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_totaltime`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_solutionhistory?displayProperty=fullName>
