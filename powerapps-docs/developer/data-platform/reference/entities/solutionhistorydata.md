---
title: "SolutionHistoryData table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the SolutionHistoryData table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# SolutionHistoryData table/entity reference (Microsoft Dataverse)

solution history data

## Messages

The following table lists the messages for the SolutionHistoryData table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `RetrieveMultiple`<br />Event: False |`GET` /solutionhistories<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the SolutionHistoryData table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SolutionHistoryData** |
| **DisplayCollectionName** | **SolutionHistoryDatas** |
| **SchemaName** | `SolutionHistoryData` |
| **CollectionSchemaName** | `SolutionHistoryDatas` |
| **EntitySetName** | `solutionhistories`|
| **LogicalName** | `solutionhistorydata` |
| **LogicalCollectionName** | `solutionhistorydatas` |
| **PrimaryIdAttribute** | `solutionhistorydataid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [CorrelationId](#BKMK_CorrelationId)
- [Description](#BKMK_Description)
- [EndTime](#BKMK_EndTime)
- [ErrorCode](#BKMK_ErrorCode)
- [ExceptionMessage](#BKMK_ExceptionMessage)
- [ExceptionStack](#BKMK_ExceptionStack)
- [IsManaged](#BKMK_IsManaged)
- [IsMicrosoftPublisher](#BKMK_IsMicrosoftPublisher)
- [IsOverwriteCustomizations](#BKMK_IsOverwriteCustomizations)
- [IsPatch](#BKMK_IsPatch)
- [Operation](#BKMK_Operation)
- [PackageName](#BKMK_PackageName)
- [PackageVersion](#BKMK_PackageVersion)
- [PublisherName](#BKMK_PublisherName)
- [Result](#BKMK_Result)
- [SolutionHistoryDataId](#BKMK_SolutionHistoryDataId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionName](#BKMK_SolutionName)
- [SolutionVersion](#BKMK_SolutionVersion)
- [StartTime](#BKMK_StartTime)
- [Status](#BKMK_Status)
- [SubOperation](#BKMK_SubOperation)

### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|---|---|
|Description|**The Activity Id.**|
|DisplayName|**The Activity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|---|---|
|Description|**The Correlation Id.**|
|DisplayName|**The Correlation Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`correlationid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Comments associated with solution installation**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|---|---|
|Description|**DateTime of the end of the solution event.**|
|DisplayName|**End Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|---|---|
|Description|**The error code of the operation performed on the solution.**|
|DisplayName|**ErrorCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`errorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ExceptionMessage"></a> ExceptionMessage

|Property|Value|
|---|---|
|Description|**The Exception Message.**|
|DisplayName|**ExceptionMessage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exceptionmessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ExceptionStack"></a> ExceptionStack

|Property|Value|
|---|---|
|Description|**The Exception Stack.**|
|DisplayName|**ExceptionStack**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exceptionstack`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Is Solution Managed**|
|DisplayName|**Is Solution Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`solutionhistorydata_ismanaged`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsMicrosoftPublisher"></a> IsMicrosoftPublisher

|Property|Value|
|---|---|
|Description|**Is the solution published by a Microsoft publisher.**|
|DisplayName|**Is Published by Microsoft**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismicrosoftpublisher`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutionhistorydata_ismicrosoftpublisher`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsOverwriteCustomizations"></a> IsOverwriteCustomizations

|Property|Value|
|---|---|
|Description|**Does the event overwrite customizations.**|
|DisplayName|**Is Overwrite Customizations**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isoverwritecustomizations`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`solutionhistorydata_isoverwritecustomizations`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPatch"></a> IsPatch

|Property|Value|
|---|---|
|Description|**Is Solution Patch**|
|DisplayName|**Is Solution Patch**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ispatch`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`solutionhistorydata_ispatch`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|---|---|
|Description|**The operation performed on the solution.**|
|DisplayName|**Operation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`operation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`solutionhistorydata_operation`|

#### Operation Choices/Options

|Value|Label|
|---|---|
|0|**Import**|
|1|**Uninstall**|
|2|**Export**|

### <a name="BKMK_PackageName"></a> PackageName

|Property|Value|
|---|---|
|Description|**Name of the package.**|
|DisplayName|**PackageName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packagename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_PackageVersion"></a> PackageVersion

|Property|Value|
|---|---|
|Description|**Version of the package.**|
|DisplayName|**PackageVersion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`packageversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PublisherName"></a> PublisherName

|Property|Value|
|---|---|
|Description|**Name of the solution's publisher.**|
|DisplayName|**PublisherName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`publishername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_Result"></a> Result

|Property|Value|
|---|---|
|Description|**The result of the operation performed on the solution.**|
|DisplayName|**Result**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`result`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1|
|MinValue|0|

### <a name="BKMK_SolutionHistoryDataId"></a> SolutionHistoryDataId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**SolutionHistoryDataId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionhistorydataid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**The Solution.**|
|DisplayName|**The Solution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionName"></a> SolutionName

|Property|Value|
|---|---|
|Description|**Name of the solution.**|
|DisplayName|**SolutionName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|65|

### <a name="BKMK_SolutionVersion"></a> SolutionVersion

|Property|Value|
|---|---|
|Description|**The Version of the Solution.**|
|DisplayName|**SolutionVersion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|---|---|
|Description|**DateTime of the start of the solution event.**|
|DisplayName|**Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`starttime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_Status"></a> Status

|Property|Value|
|---|---|
|Description|**The status of the operation performed on the solution.**|
|DisplayName|**Status**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`status`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`solutionhistorydata_status`|

#### Status Choices/Options

|Value|Label|
|---|---|
|0|**Start**|
|1|**End**|

### <a name="BKMK_SubOperation"></a> SubOperation

|Property|Value|
|---|---|
|Description|**The suboperation performed on the solution.**|
|DisplayName|**SubOperation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`suboperation`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`solutionhistorydata_suboperation`|

#### SubOperation Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**New**|
|2|**Upgrade**|
|3|**Update**|
|4|**Delete**|




### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.solutionhistorydata?displayProperty=fullName>
