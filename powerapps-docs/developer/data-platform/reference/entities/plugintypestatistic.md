---
title: "PluginTypeStatistic table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the PluginTypeStatistic table/entity."
ms.date: 05/20/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# PluginTypeStatistic table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Plug-in type statistic.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/plugintypestatistics(*plugintypestatisticid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/plugintypestatistics<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|PluginTypeStatistics|
|DisplayCollectionName|Plug-in Type Statistics|
|DisplayName|Plug-in Type Statistic|
|EntitySetName|plugintypestatistics|
|IsBPFEntity|False|
|LogicalCollectionName|plugintypestatistics|
|LogicalName|plugintypestatistic|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|plugintypestatisticid|
|PrimaryNameAttribute||
|SchemaName|PluginTypeStatistic|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AverageExecuteTimeInMilliseconds](#BKMK_AverageExecuteTimeInMilliseconds)
- [CrashContributionPercent](#BKMK_CrashContributionPercent)
- [CrashCount](#BKMK_CrashCount)
- [CrashPercent](#BKMK_CrashPercent)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExecuteCount](#BKMK_ExecuteCount)
- [FailureCount](#BKMK_FailureCount)
- [FailurePercent](#BKMK_FailurePercent)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [PluginTypeId](#BKMK_PluginTypeId)
- [PluginTypeIdName](#BKMK_PluginTypeIdName)
- [PluginTypeStatisticId](#BKMK_PluginTypeStatisticId)
- [TerminateCpuContributionPercent](#BKMK_TerminateCpuContributionPercent)
- [TerminateHandlesContributionPercent](#BKMK_TerminateHandlesContributionPercent)
- [TerminateMemoryContributionPercent](#BKMK_TerminateMemoryContributionPercent)
- [TerminateOtherContributionPercent](#BKMK_TerminateOtherContributionPercent)


### <a name="BKMK_AverageExecuteTimeInMilliseconds"></a> AverageExecuteTimeInMilliseconds

|Property|Value|
|--------|-----|
|Description|The average execution time (in milliseconds) for the plug-in type.|
|DisplayName|The average execution time|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|averageexecutetimeinmilliseconds|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CrashContributionPercent"></a> CrashContributionPercent

|Property|Value|
|--------|-----|
|Description|The plug-in type percentage contribution to crashes.|
|DisplayName|Percentage contribution to crashes|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|crashcontributionpercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CrashCount"></a> CrashCount

|Property|Value|
|--------|-----|
|Description|Number of times the plug-in type has crashed.|
|DisplayName|Number of times crashed|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|crashcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CrashPercent"></a> CrashPercent

|Property|Value|
|--------|-----|
|Description|Percentage of crashes for the plug-in type.|
|DisplayName|Percentage of crashes|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|crashpercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the plug-in type statistic.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

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


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the plug-in type statistic was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the plug-in type statistic.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ExecuteCount"></a> ExecuteCount

|Property|Value|
|--------|-----|
|Description|Number of times the plug-in type has been executed.|
|DisplayName|Execution Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|executecount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_FailureCount"></a> FailureCount

|Property|Value|
|--------|-----|
|Description|Number of times the plug-in type has failed.|
|DisplayName|Failure Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|failurecount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_FailurePercent"></a> FailurePercent

|Property|Value|
|--------|-----|
|Description|Percentage of failures for the plug-in type.|
|DisplayName|Failure Percent|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|failurepercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the plug-in type statistic.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the plug-in type statistic was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the plug-in type statistic.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization with which the plug-in type statistic is associated.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the plug-in type associated with this plug-in type statistic.|
|DisplayName|Plugin Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|plugintypeid|
|RequiredLevel|SystemRequired|
|Targets|plugintype|
|Type|Lookup|


### <a name="BKMK_PluginTypeIdName"></a> PluginTypeIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|plugintypeidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PluginTypeStatisticId"></a> PluginTypeStatisticId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the plug-in type statistic.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|plugintypestatisticid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TerminateCpuContributionPercent"></a> TerminateCpuContributionPercent

|Property|Value|
|--------|-----|
|Description|The plug-in type percentage contribution to Worker process termination due to excessive CPU usage.|
|DisplayName|Terminate CPU Contribution Percent|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|terminatecpucontributionpercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TerminateHandlesContributionPercent"></a> TerminateHandlesContributionPercent

|Property|Value|
|--------|-----|
|Description|The plug-in type percentage contribution to Worker process termination due to excessive handle usage.|
|DisplayName|Terminate Handles Contribution Percent|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|terminatehandlescontributionpercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TerminateMemoryContributionPercent"></a> TerminateMemoryContributionPercent

|Property|Value|
|--------|-----|
|Description|The plug-in type percentage contribution to Worker process termination due to excessive memory usage.|
|DisplayName|Terminate Memory Contribution Percent|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|terminatememorycontributionpercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_TerminateOtherContributionPercent"></a> TerminateOtherContributionPercent

|Property|Value|
|--------|-----|
|Description|The plug-in type percentage contribution to Worker process termination due to unknown reasons.|
|DisplayName|Terminate Other Contribution Percent|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|terminateothercontributionpercent|
|MaxValue|100|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_plugintypestatisticbase_modifiedonbehalfby](#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby)
- [createdby_plugintypestatistic](#BKMK_createdby_plugintypestatistic)
- [lk_plugintypestatisticbase_createdonbehalfby](#BKMK_lk_plugintypestatisticbase_createdonbehalfby)
- [organization_plugintypestatistic](#BKMK_organization_plugintypestatistic)
- [modifiedby_plugintypestatistic](#BKMK_modifiedby_plugintypestatistic)
- [plugintype_plugintypestatistic](#BKMK_plugintype_plugintypestatistic)


### <a name="BKMK_lk_plugintypestatisticbase_modifiedonbehalfby"></a> lk_plugintypestatisticbase_modifiedonbehalfby

See systemuser Table [lk_plugintypestatisticbase_modifiedonbehalfby](systemuser.md#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_createdby_plugintypestatistic"></a> createdby_plugintypestatistic

See systemuser Table [createdby_plugintypestatistic](systemuser.md#BKMK_createdby_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_lk_plugintypestatisticbase_createdonbehalfby"></a> lk_plugintypestatisticbase_createdonbehalfby

See systemuser Table [lk_plugintypestatisticbase_createdonbehalfby](systemuser.md#BKMK_lk_plugintypestatisticbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_plugintypestatistic"></a> organization_plugintypestatistic

See organization Table [organization_plugintypestatistic](organization.md#BKMK_organization_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_modifiedby_plugintypestatistic"></a> modifiedby_plugintypestatistic

See systemuser Table [modifiedby_plugintypestatistic](systemuser.md#BKMK_modifiedby_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_plugintype_plugintypestatistic"></a> plugintype_plugintypestatistic

See plugintype Table [plugintype_plugintypestatistic](plugintype.md#BKMK_plugintype_plugintypestatistic) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.plugintypestatistic?text=plugintypestatistic EntityType" />