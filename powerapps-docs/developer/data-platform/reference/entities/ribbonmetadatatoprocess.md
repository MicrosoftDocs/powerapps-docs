---
title: "Ribbon Metadata To Process (RibbonMetadataToProcess) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Ribbon Metadata To Process (RibbonMetadataToProcess) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Ribbon Metadata To Process (RibbonMetadataToProcess) table/entity reference (Microsoft Dataverse)

Container for Ribbon Metadata To Process

## Messages

The following table lists the messages for the Ribbon Metadata To Process (RibbonMetadataToProcess) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `RetrieveMultiple`<br />Event: False |`GET` /RibbonMetadataSetToProcess<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Ribbon Metadata To Process (RibbonMetadataToProcess) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Ribbon Metadata To Process** |
| **DisplayCollectionName** | **Ribbon Metadata Set To Process** |
| **SchemaName** | `RibbonMetadataToProcess` |
| **CollectionSchemaName** | `RibbonMetadataToProcesses` |
| **EntitySetName** | `RibbonMetadataSetToProcess`|
| **LogicalName** | `ribbonmetadatatoprocess` |
| **LogicalCollectionName** | `ribbonmetadatatoprocesses` |
| **PrimaryIdAttribute** | `ribbonmetadatarowid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EntityName](#BKMK_EntityName)
- [ExceptionMessage](#BKMK_ExceptionMessage)
- [IsDbUpdate](#BKMK_IsDbUpdate)
- [RetryCount](#BKMK_RetryCount)
- [RibbonMetadataRowId](#BKMK_RibbonMetadataRowId)
- [SolutionId](#BKMK_SolutionId)
- [SolutionName](#BKMK_SolutionName)
- [Status](#BKMK_Status)

### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|---|---|
|Description|**Entity Logical Name**|
|DisplayName|**Entity Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ExceptionMessage"></a> ExceptionMessage

|Property|Value|
|---|---|
|Description|**Exception message**|
|DisplayName|**Exception message which occurred during ribbon entity processing.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exceptionmessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_IsDbUpdate"></a> IsDbUpdate

|Property|Value|
|---|---|
|Description|**Is entity created via Db Update**|
|DisplayName|**Is entity created via Db Update**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdbupdate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|10|
|MinValue|0|

### <a name="BKMK_RetryCount"></a> RetryCount

|Property|Value|
|---|---|
|Description|**Retry Count**|
|DisplayName|**Retry Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`retrycount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_RibbonMetadataRowId"></a> RibbonMetadataRowId

|Property|Value|
|---|---|
|Description|**Unique identifier for Ribbon Metadata Instance To Process**|
|DisplayName|**Ribbon Metadata To Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ribbonmetadatarowid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Solution Id**|
|DisplayName|**Solution Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionName"></a> SolutionName

|Property|Value|
|---|---|
|Description|**Solution Name of the ribbon entity**|
|DisplayName|**Solution Name of the ribbon entity.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Status"></a> Status

|Property|Value|
|---|---|
|Description|**Status**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`status`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CompletedOn](#BKMK_CompletedOn)
- [CreatedOn](#BKMK_CreatedOn)
- [ProcessedOn](#BKMK_ProcessedOn)

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the ribbon entity record has finished processing. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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

### <a name="BKMK_ProcessedOn"></a> ProcessedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was processed. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Processed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.ribbonmetadatatoprocess?displayProperty=fullName>
