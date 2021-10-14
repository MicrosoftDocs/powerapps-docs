---
title: "SolutionHistoryData table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SolutionHistoryData table/entity."
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

# SolutionHistoryData table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

solution history data


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/solutionhistories<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SolutionHistoryDatas|
|DisplayCollectionName|SolutionHistoryDatas|
|DisplayName|SolutionHistoryData|
|EntitySetName|solutionhistories|
|IsBPFEntity|False|
|LogicalCollectionName|solutionhistorydatas|
|LogicalName|solutionhistorydata|
|OwnershipType|None|
|PrimaryIdAttribute|solutionhistorydataid|
|PrimaryNameAttribute||
|SchemaName|SolutionHistoryData|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [CorrelationId](#BKMK_CorrelationId)
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
|--------|-----|
|Description|The Activity Id.|
|DisplayName|The Activity Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activityid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_CorrelationId"></a> CorrelationId

|Property|Value|
|--------|-----|
|Description|The Correlation Id.|
|DisplayName|The Correlation Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|correlationid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_EndTime"></a> EndTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|DateTime of the end of the solution event.|
|DisplayName|End Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|endtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ErrorCode"></a> ErrorCode

|Property|Value|
|--------|-----|
|Description|The error code of the operation performed on the solution.|
|DisplayName|ErrorCode|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|errorcode|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ExceptionMessage"></a> ExceptionMessage

|Property|Value|
|--------|-----|
|Description|The Exception Message.|
|DisplayName|ExceptionMessage|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exceptionmessage|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExceptionStack"></a> ExceptionStack

|Property|Value|
|--------|-----|
|Description|The Exception Stack.|
|DisplayName|ExceptionStack|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exceptionstack|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Is Solution Managed|
|DisplayName|Is Solution Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsMicrosoftPublisher"></a> IsMicrosoftPublisher

|Property|Value|
|--------|-----|
|Description|Is the solution published by a Microsoft publisher.|
|DisplayName|Is Published by Microsoft|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismicrosoftpublisher|
|RequiredLevel|None|
|Type|Boolean|

#### IsMicrosoftPublisher Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsOverwriteCustomizations"></a> IsOverwriteCustomizations

|Property|Value|
|--------|-----|
|Description|Does the event overwrite customizations.|
|DisplayName|Is Overwrite Customizations|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isoverwritecustomizations|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsOverwriteCustomizations Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsPatch"></a> IsPatch

|Property|Value|
|--------|-----|
|Description|Is Solution Patch|
|DisplayName|Is Solution Patch|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ispatch|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsPatch Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Operation"></a> Operation

|Property|Value|
|--------|-----|
|Description|The operation performed on the solution.|
|DisplayName|Operation|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|operation|
|RequiredLevel|None|
|Type|Picklist|

#### Operation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Import||
|1|Uninstall||
|2|Export||



### <a name="BKMK_PackageName"></a> PackageName

|Property|Value|
|--------|-----|
|Description|Name of the package.|
|DisplayName|PackageName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|packagename|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PackageVersion"></a> PackageVersion

|Property|Value|
|--------|-----|
|Description|Version of the package.|
|DisplayName|PackageVersion|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|packageversion|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PublisherName"></a> PublisherName

|Property|Value|
|--------|-----|
|Description|Name of the solution's publisher.|
|DisplayName|PublisherName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|publishername|
|MaxLength|512|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Result"></a> Result

|Property|Value|
|--------|-----|
|Description|The result of the operation performed on the solution.|
|DisplayName|Result|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|result|
|MaxValue|1|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_SolutionHistoryDataId"></a> SolutionHistoryDataId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|SolutionHistoryDataId|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutionhistorydataid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|The Solution.|
|DisplayName|The Solution|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_SolutionName"></a> SolutionName

|Property|Value|
|--------|-----|
|Description|Name of the solution.|
|DisplayName|SolutionName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solutionname|
|MaxLength|65|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionVersion"></a> SolutionVersion

|Property|Value|
|--------|-----|
|Description|The Version of the Solution.|
|DisplayName|SolutionVersion|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|solutionversion|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StartTime"></a> StartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|DateTime of the start of the solution event.|
|DisplayName|Start Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|starttime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_Status"></a> Status

|Property|Value|
|--------|-----|
|Description|The status of the operation performed on the solution.|
|DisplayName|Status|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|status|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Status Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Start||
|1|End||



### <a name="BKMK_SubOperation"></a> SubOperation

|Property|Value|
|--------|-----|
|Description|The suboperation performed on the solution.|
|DisplayName|SubOperation|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|suboperation|
|RequiredLevel|None|
|Type|Picklist|

#### SubOperation Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|New||
|2|Upgrade||
|3|Update||
|4|Delete||




### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.solutionhistorydata?text=solutionhistorydata EntityType" />