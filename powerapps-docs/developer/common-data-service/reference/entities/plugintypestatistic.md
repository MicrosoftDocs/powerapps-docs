---
title: "PluginTypeStatistic Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the PluginTypeStatistic entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# PluginTypeStatistic Entity Reference

Plug-in type statistic.

## Entity Properties

**DisplayName**: Plug-in Type Statistic<br />
**DisplayCollectionName**: Plug-in Type Statistics<br />
**SchemaName**: PluginTypeStatistic<br />
**CollectionSchemaName**: PluginTypeStatistics<br />
**LogicalName**: plugintypestatistic<br />
**LogicalCollectionName**: plugintypestatistics<br />
**EntitySetName**: plugintypestatistics<br />
**PrimaryIdAttribute**: plugintypestatisticid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: The average execution time (in milliseconds) for the plug-in type.<br />
**DisplayName**: The average execution time<br />
**LogicalName**: averageexecutetimeinmilliseconds<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_CrashContributionPercent"></a> CrashContributionPercent

**Description**: The plug-in type percentage contribution to crashes.<br />
**DisplayName**: Percentage contribution to crashes<br />
**LogicalName**: crashcontributionpercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_CrashCount"></a> CrashCount

**Description**: Number of times the plug-in type has crashed.<br />
**DisplayName**: Number of times crashed<br />
**LogicalName**: crashcount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_CrashPercent"></a> CrashPercent

**Description**: Percentage of crashes for the plug-in type.<br />
**DisplayName**: Percentage of crashes<br />
**LogicalName**: crashpercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the plug-in type statistic.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the plug-in type statistic was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the plug-in type statistic.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExecuteCount"></a> ExecuteCount

**Description**: Number of times the plug-in type has been executed.<br />
**DisplayName**: Execution Count<br />
**LogicalName**: executecount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_FailureCount"></a> FailureCount

**Description**: Number of times the plug-in type has failed.<br />
**DisplayName**: Failure Count<br />
**LogicalName**: failurecount<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_FailurePercent"></a> FailurePercent

**Description**: Percentage of failures for the plug-in type.<br />
**DisplayName**: Failure Percent<br />
**LogicalName**: failurepercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the plug-in type statistic.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the plug-in type statistic was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the plug-in type statistic.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization with which the plug-in type statistic is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_PluginTypeId"></a> PluginTypeId

**Description**: Unique identifier of the plug-in type associated with this plug-in type statistic.<br />
**DisplayName**: Plugin Type<br />
**LogicalName**: plugintypeid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: plugintype


### <a name="BKMK_PluginTypeIdName"></a> PluginTypeIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: plugintypeidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PluginTypeStatisticId"></a> PluginTypeStatisticId

**Description**: Unique identifier of the plug-in type statistic.<br />
**DisplayName**: <br />
**LogicalName**: plugintypestatisticid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TerminateCpuContributionPercent"></a> TerminateCpuContributionPercent

**Description**: The plug-in type percentage contribution to Worker process termination due to excessive CPU usage.<br />
**DisplayName**: Terminate CPU Contribution Percent<br />
**LogicalName**: terminatecpucontributionpercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_TerminateHandlesContributionPercent"></a> TerminateHandlesContributionPercent

**Description**: The plug-in type percentage contribution to Worker process termination due to excessive handle usage.<br />
**DisplayName**: Terminate Handles Contribution Percent<br />
**LogicalName**: terminatehandlescontributionpercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_TerminateMemoryContributionPercent"></a> TerminateMemoryContributionPercent

**Description**: The plug-in type percentage contribution to Worker process termination due to excessive memory usage.<br />
**DisplayName**: Terminate Memory Contribution Percent<br />
**LogicalName**: terminatememorycontributionpercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0


### <a name="BKMK_TerminateOtherContributionPercent"></a> TerminateOtherContributionPercent

**Description**: The plug-in type percentage contribution to Worker process termination due to unknown reasons.<br />
**DisplayName**: Terminate Other Contribution Percent<br />
**LogicalName**: terminateothercontributionpercent<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 100<br />
**MinValue**: 0

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_userentityinstancedata_plugintypestatistic"></a> userentityinstancedata_plugintypestatistic

Same as userentityinstancedata entity [userentityinstancedata_plugintypestatistic](userentityinstancedata.md#BKMK_userentityinstancedata_plugintypestatistic) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_plugintypestatistic<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_plugintypestatisticbase_modifiedonbehalfby](#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby)
- [createdby_plugintypestatistic](#BKMK_createdby_plugintypestatistic)
- [lk_plugintypestatisticbase_createdonbehalfby](#BKMK_lk_plugintypestatisticbase_createdonbehalfby)
- [organization_plugintypestatistic](#BKMK_organization_plugintypestatistic)
- [modifiedby_plugintypestatistic](#BKMK_modifiedby_plugintypestatistic)
- [plugintype_plugintypestatistic](#BKMK_plugintype_plugintypestatistic)


### <a name="BKMK_lk_plugintypestatisticbase_modifiedonbehalfby"></a> lk_plugintypestatisticbase_modifiedonbehalfby

See systemuser Entity [lk_plugintypestatisticbase_modifiedonbehalfby](systemuser.md#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_createdby_plugintypestatistic"></a> createdby_plugintypestatistic

See systemuser Entity [createdby_plugintypestatistic](systemuser.md#BKMK_createdby_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_lk_plugintypestatisticbase_createdonbehalfby"></a> lk_plugintypestatisticbase_createdonbehalfby

See systemuser Entity [lk_plugintypestatisticbase_createdonbehalfby](systemuser.md#BKMK_lk_plugintypestatisticbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_plugintypestatistic"></a> organization_plugintypestatistic

See organization Entity [organization_plugintypestatistic](organization.md#BKMK_organization_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_modifiedby_plugintypestatistic"></a> modifiedby_plugintypestatistic

See systemuser Entity [modifiedby_plugintypestatistic](systemuser.md#BKMK_modifiedby_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_plugintype_plugintypestatistic"></a> plugintype_plugintypestatistic

See plugintype Entity [plugintype_plugintypestatistic](plugintype.md#BKMK_plugintype_plugintypestatistic) One-To-Many relationship.
plugintypestatistic

