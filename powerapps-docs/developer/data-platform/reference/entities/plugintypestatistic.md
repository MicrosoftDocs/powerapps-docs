---
title: "Plug-in Type Statistic (PluginTypeStatistic) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Plug-in Type Statistic (PluginTypeStatistic) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Plug-in Type Statistic (PluginTypeStatistic) table/entity reference (Microsoft Dataverse)

Plug-in type statistic.

## Messages

The following table lists the messages for the Plug-in Type Statistic (PluginTypeStatistic) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /plugintypestatistics(*plugintypestatisticid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /plugintypestatistics<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Plug-in Type Statistic (PluginTypeStatistic) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Plug-in Type Statistic** |
| **DisplayCollectionName** | **Plug-in Type Statistics** |
| **SchemaName** | `PluginTypeStatistic` |
| **CollectionSchemaName** | `PluginTypeStatistics` |
| **EntitySetName** | `plugintypestatistics`|
| **LogicalName** | `plugintypestatistic` |
| **LogicalCollectionName** | `plugintypestatistics` |
| **PrimaryIdAttribute** | `plugintypestatisticid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [AverageExecuteTimeInMilliseconds](#BKMK_AverageExecuteTimeInMilliseconds)
- [CrashContributionPercent](#BKMK_CrashContributionPercent)
- [CrashCount](#BKMK_CrashCount)
- [CrashPercent](#BKMK_CrashPercent)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExecuteCount](#BKMK_ExecuteCount)
- [FailureCount](#BKMK_FailureCount)
- [FailurePercent](#BKMK_FailurePercent)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [PluginTypeId](#BKMK_PluginTypeId)
- [PluginTypeStatisticId](#BKMK_PluginTypeStatisticId)
- [TerminateCpuContributionPercent](#BKMK_TerminateCpuContributionPercent)
- [TerminateHandlesContributionPercent](#BKMK_TerminateHandlesContributionPercent)
- [TerminateMemoryContributionPercent](#BKMK_TerminateMemoryContributionPercent)
- [TerminateOtherContributionPercent](#BKMK_TerminateOtherContributionPercent)

### <a name="BKMK_AverageExecuteTimeInMilliseconds"></a> AverageExecuteTimeInMilliseconds

|Property|Value|
|---|---|
|Description|**The average execution time (in milliseconds) for the plug-in type.**|
|DisplayName|**The average execution time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`averageexecutetimeinmilliseconds`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_CrashContributionPercent"></a> CrashContributionPercent

|Property|Value|
|---|---|
|Description|**The plug-in type percentage contribution to crashes.**|
|DisplayName|**Percentage contribution to crashes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`crashcontributionpercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_CrashCount"></a> CrashCount

|Property|Value|
|---|---|
|Description|**Number of times the plug-in type has crashed.**|
|DisplayName|**Number of times crashed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`crashcount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_CrashPercent"></a> CrashPercent

|Property|Value|
|---|---|
|Description|**Percentage of crashes for the plug-in type.**|
|DisplayName|**Percentage of crashes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`crashpercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the plug-in type statistic.**|
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
|Description|**Date and time when the plug-in type statistic was created.**|
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
|Description|**Unique identifier of the delegate user who created the plug-in type statistic.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExecuteCount"></a> ExecuteCount

|Property|Value|
|---|---|
|Description|**Number of times the plug-in type has been executed.**|
|DisplayName|**Execution Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executecount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_FailureCount"></a> FailureCount

|Property|Value|
|---|---|
|Description|**Number of times the plug-in type has failed.**|
|DisplayName|**Failure Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`failurecount`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_FailurePercent"></a> FailurePercent

|Property|Value|
|---|---|
|Description|**Percentage of failures for the plug-in type.**|
|DisplayName|**Failure Percent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`failurepercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the plug-in type statistic.**|
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
|Description|**Date and time when the plug-in type statistic was last modified.**|
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
|Description|**Unique identifier of the delegate user who modified the plug-in type statistic.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the plug-in type statistic is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in type associated with this plug-in type statistic.**|
|DisplayName|**Plugin Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`plugintypeid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|plugintype|

### <a name="BKMK_PluginTypeStatisticId"></a> PluginTypeStatisticId

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in type statistic.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plugintypestatisticid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_TerminateCpuContributionPercent"></a> TerminateCpuContributionPercent

|Property|Value|
|---|---|
|Description|**The plug-in type percentage contribution to Worker process termination due to excessive CPU usage.**|
|DisplayName|**Terminate CPU Contribution Percent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`terminatecpucontributionpercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_TerminateHandlesContributionPercent"></a> TerminateHandlesContributionPercent

|Property|Value|
|---|---|
|Description|**The plug-in type percentage contribution to Worker process termination due to excessive handle usage.**|
|DisplayName|**Terminate Handles Contribution Percent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`terminatehandlescontributionpercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_TerminateMemoryContributionPercent"></a> TerminateMemoryContributionPercent

|Property|Value|
|---|---|
|Description|**The plug-in type percentage contribution to Worker process termination due to excessive memory usage.**|
|DisplayName|**Terminate Memory Contribution Percent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`terminatememorycontributionpercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

### <a name="BKMK_TerminateOtherContributionPercent"></a> TerminateOtherContributionPercent

|Property|Value|
|---|---|
|Description|**The plug-in type percentage contribution to Worker process termination due to unknown reasons.**|
|DisplayName|**Terminate Other Contribution Percent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`terminateothercontributionpercent`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100|
|MinValue|0|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_plugintypestatistic](#BKMK_createdby_plugintypestatistic)
- [lk_plugintypestatisticbase_createdonbehalfby](#BKMK_lk_plugintypestatisticbase_createdonbehalfby)
- [lk_plugintypestatisticbase_modifiedonbehalfby](#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby)
- [modifiedby_plugintypestatistic](#BKMK_modifiedby_plugintypestatistic)
- [organization_plugintypestatistic](#BKMK_organization_plugintypestatistic)
- [plugintype_plugintypestatistic](#BKMK_plugintype_plugintypestatistic)

### <a name="BKMK_createdby_plugintypestatistic"></a> createdby_plugintypestatistic

One-To-Many Relationship: [systemuser createdby_plugintypestatistic](systemuser.md#BKMK_createdby_plugintypestatistic)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_plugintypestatisticbase_createdonbehalfby"></a> lk_plugintypestatisticbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_plugintypestatisticbase_createdonbehalfby](systemuser.md#BKMK_lk_plugintypestatisticbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_plugintypestatisticbase_modifiedonbehalfby"></a> lk_plugintypestatisticbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_plugintypestatisticbase_modifiedonbehalfby](systemuser.md#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_plugintypestatistic"></a> modifiedby_plugintypestatistic

One-To-Many Relationship: [systemuser modifiedby_plugintypestatistic](systemuser.md#BKMK_modifiedby_plugintypestatistic)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_plugintypestatistic"></a> organization_plugintypestatistic

One-To-Many Relationship: [organization organization_plugintypestatistic](organization.md#BKMK_organization_plugintypestatistic)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugintype_plugintypestatistic"></a> plugintype_plugintypestatistic

One-To-Many Relationship: [plugintype plugintype_plugintypestatistic](plugintype.md#BKMK_plugintype_plugintypestatistic)

|Property|Value|
|---|---|
|ReferencedEntity|`plugintype`|
|ReferencedAttribute|`plugintypeid`|
|ReferencingAttribute|`plugintypeid`|
|ReferencingEntityNavigationPropertyName|`plugintypeid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.plugintypestatistic?displayProperty=fullName>
