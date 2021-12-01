---
title: "RibbonMetadataToProcess table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the RibbonMetadataToProcess table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# RibbonMetadataToProcess table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Container for Ribbon Metadata To Process


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/RibbonMetadataSetToProcess<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RibbonMetadataToProcesses|
|DisplayCollectionName|Ribbon Metadata Set To Process|
|DisplayName|Ribbon Metadata To Process|
|EntitySetName|RibbonMetadataSetToProcess|
|IsBPFEntity|False|
|LogicalCollectionName|ribbonmetadatatoprocesses|
|LogicalName|ribbonmetadatatoprocess|
|OwnershipType|None|
|PrimaryIdAttribute|ribbonmetadatarowid|
|PrimaryNameAttribute||
|SchemaName|RibbonMetadataToProcess|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Entity Logical Name|
|DisplayName|Entity Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|entityname|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ExceptionMessage"></a> ExceptionMessage

|Property|Value|
|--------|-----|
|Description|Exception message|
|DisplayName|Exception message which occurred during ribbon entity processing.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|exceptionmessage|
|MaxLength|1024|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsDbUpdate"></a> IsDbUpdate

|Property|Value|
|--------|-----|
|Description|Is entity created via Db Update|
|DisplayName|Is entity created via Db Update|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|isdbupdate|
|MaxValue|10|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_RetryCount"></a> RetryCount

|Property|Value|
|--------|-----|
|Description|Retry Count|
|DisplayName|Retry Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|retrycount|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_RibbonMetadataRowId"></a> RibbonMetadataRowId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Ribbon Metadata Instance To Process|
|DisplayName|Ribbon Metadata To Process|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|ribbonmetadatarowid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Solution Id|
|DisplayName|Solution Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionName"></a> SolutionName

|Property|Value|
|--------|-----|
|Description|Solution Name of the ribbon entity|
|DisplayName|Solution Name of the ribbon entity.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutionname|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Status"></a> Status

|Property|Value|
|--------|-----|
|Description|Status|
|DisplayName|Status|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|status|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CompletedOn](#BKMK_CompletedOn)
- [CreatedOn](#BKMK_CreatedOn)
- [ProcessedOn](#BKMK_ProcessedOn)


### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the ribbon entity record has finished processing. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Completed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|completedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ProcessedOn"></a> ProcessedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the record was processed. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.|
|DisplayName|Processed On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|processedon|
|RequiredLevel|None|
|Type|DateTime|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.ribbonmetadatatoprocess?text=ribbonmetadatatoprocess EntityType" />