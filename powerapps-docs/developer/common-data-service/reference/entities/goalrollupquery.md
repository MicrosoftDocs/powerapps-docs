---
title: "GoalRollupQuery Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the GoalRollupQuery entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# GoalRollupQuery Entity Reference

Query that is used to filter the results of the goal rollup.

## Entity Properties

**DisplayName**: Rollup Query<br />
**DisplayCollectionName**: Rollup Queries<br />
**SchemaName**: GoalRollupQuery<br />
**CollectionSchemaName**: goalrollupqueries<br />
**LogicalName**: goalrollupquery<br />
**LogicalCollectionName**: goalrollupqueries<br />
**EntitySetName**: goalrollupqueries<br />
**PrimaryIdAttribute**: goalrollupqueryid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [FetchXml](#BKMK_FetchXml)
- [GoalRollupQueryId](#BKMK_GoalRollupQueryId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [QueryEntityType](#BKMK_QueryEntityType)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_FetchXml"></a> FetchXml

**Description**: String that specifies the condition criteria in FetchXML.<br />
**DisplayName**: Condition Criteria<br />
**LogicalName**: fetchxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_GoalRollupQueryId"></a> GoalRollupQueryId

**Description**: Unique identifier of the rollup query.<br />
**DisplayName**: Goal Rollup Query<br />
**LogicalName**: goalrollupqueryid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Sequence number of the import that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_Name"></a> Name

**Description**: Type a descriptive name for the goal rollup query.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Owner Id Type<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_QueryEntityType"></a> QueryEntityType

**Description**: Enter the record type of the rollup query.<br />
**DisplayName**: Entity Type<br />
**LogicalName**: queryentitytype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the goal rollup query is active or inactive.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 0 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 1 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the goal rollup query's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Open **State**: 0
- **Value**: 1 **Label**: Closed **State**: 1



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
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

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
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

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who last updated the record on behalf of another user.<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: Yomi name of the owner<br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the record.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: 


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the goal rollup query.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [goalrollupquery_actualint](#BKMK_goalrollupquery_actualint)
- [goal_rollupquery_actualmoney](#BKMK_goal_rollupquery_actualmoney)
- [goal_rollupquery_actualdecimal](#BKMK_goal_rollupquery_actualdecimal)
- [goal_rollupquery_customint](#BKMK_goal_rollupquery_customint)
- [goal_rollupquery_custommoney](#BKMK_goal_rollupquery_custommoney)
- [goal_rollupquery_customdecimal](#BKMK_goal_rollupquery_customdecimal)
- [goal_rollupquery_inprogressint](#BKMK_goal_rollupquery_inprogressint)
- [goal_rollupquery_inprogressmoney](#BKMK_goal_rollupquery_inprogressmoney)
- [goal_rollupquery_inprogressdecimal](#BKMK_goal_rollupquery_inprogressdecimal)
- [GoalRollupQuery_SyncErrors](#BKMK_GoalRollupQuery_SyncErrors)
- [goalrollupquery_AsyncOperations](#BKMK_goalrollupquery_AsyncOperations)
- [GoalRollupQuery_DuplicateMatchingRecord](#BKMK_GoalRollupQuery_DuplicateMatchingRecord)
- [userentityinstancedata_goalrollupquery](#BKMK_userentityinstancedata_goalrollupquery)
- [GoalRollupQuery_DuplicateBaseRecord](#BKMK_GoalRollupQuery_DuplicateBaseRecord)
- [goalrollupquery_ProcessSessions](#BKMK_goalrollupquery_ProcessSessions)


### <a name="BKMK_goalrollupquery_actualint"></a> goalrollupquery_actualint

Same as goal entity [goalrollupquery_actualint](goal.md#BKMK_goalrollupquery_actualint) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupqueryactualintegerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goalrollupquery_actualint<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_actualmoney"></a> goal_rollupquery_actualmoney

Same as goal entity [goal_rollupquery_actualmoney](goal.md#BKMK_goal_rollupquery_actualmoney) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupqueryactualmoneyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_actualmoney<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_actualdecimal"></a> goal_rollupquery_actualdecimal

Same as goal entity [goal_rollupquery_actualdecimal](goal.md#BKMK_goal_rollupquery_actualdecimal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupqueryactualdecimalid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_actualdecimal<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_customint"></a> goal_rollupquery_customint

Same as goal entity [goal_rollupquery_customint](goal.md#BKMK_goal_rollupquery_customint) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupquerycustomintegerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_customint<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_custommoney"></a> goal_rollupquery_custommoney

Same as goal entity [goal_rollupquery_custommoney](goal.md#BKMK_goal_rollupquery_custommoney) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupquerycustommoneyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_custommoney<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_customdecimal"></a> goal_rollupquery_customdecimal

Same as goal entity [goal_rollupquery_customdecimal](goal.md#BKMK_goal_rollupquery_customdecimal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupquerycustomdecimalid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_customdecimal<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_inprogressint"></a> goal_rollupquery_inprogressint

Same as goal entity [goal_rollupquery_inprogressint](goal.md#BKMK_goal_rollupquery_inprogressint) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupqueryinprogressintegerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_inprogressint<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_inprogressmoney"></a> goal_rollupquery_inprogressmoney

Same as goal entity [goal_rollupquery_inprogressmoney](goal.md#BKMK_goal_rollupquery_inprogressmoney) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupqueryinprogressmoneyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_inprogressmoney<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_goal_rollupquery_inprogressdecimal"></a> goal_rollupquery_inprogressdecimal

Same as goal entity [goal_rollupquery_inprogressdecimal](goal.md#BKMK_goal_rollupquery_inprogressdecimal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: rollupqueryinprogressdecimalid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goal_rollupquery_inprogressdecimal<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_GoalRollupQuery_SyncErrors"></a> GoalRollupQuery_SyncErrors

Same as syncerror entity [GoalRollupQuery_SyncErrors](syncerror.md#BKMK_GoalRollupQuery_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: GoalRollupQuery_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_goalrollupquery_AsyncOperations"></a> goalrollupquery_AsyncOperations

Same as asyncoperation entity [goalrollupquery_AsyncOperations](asyncoperation.md#BKMK_goalrollupquery_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goalrollupquery_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_GoalRollupQuery_DuplicateMatchingRecord"></a> GoalRollupQuery_DuplicateMatchingRecord

Same as duplicaterecord entity [GoalRollupQuery_DuplicateMatchingRecord](duplicaterecord.md#BKMK_GoalRollupQuery_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: GoalRollupQuery_DuplicateMatchingRecord<br />
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


### <a name="BKMK_userentityinstancedata_goalrollupquery"></a> userentityinstancedata_goalrollupquery

Same as userentityinstancedata entity [userentityinstancedata_goalrollupquery](userentityinstancedata.md#BKMK_userentityinstancedata_goalrollupquery) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_goalrollupquery<br />
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


### <a name="BKMK_GoalRollupQuery_DuplicateBaseRecord"></a> GoalRollupQuery_DuplicateBaseRecord

Same as duplicaterecord entity [GoalRollupQuery_DuplicateBaseRecord](duplicaterecord.md#BKMK_GoalRollupQuery_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: GoalRollupQuery_DuplicateBaseRecord<br />
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


### <a name="BKMK_goalrollupquery_ProcessSessions"></a> goalrollupquery_ProcessSessions

Same as processsession entity [goalrollupquery_ProcessSessions](processsession.md#BKMK_goalrollupquery_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: goalrollupquery_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [team_goalrollupquery](#BKMK_team_goalrollupquery)
- [lk_goalrollupquery_createdby](#BKMK_lk_goalrollupquery_createdby)
- [lk_goalrollupquery_createdonbehalfby](#BKMK_lk_goalrollupquery_createdonbehalfby)
- [lk_goalrollupquery_modifiedby](#BKMK_lk_goalrollupquery_modifiedby)
- [lk_goalrollupquery_modifiedonbehalfby](#BKMK_lk_goalrollupquery_modifiedonbehalfby)
- [business_unit_goalrollupquery](#BKMK_business_unit_goalrollupquery)


### <a name="BKMK_team_goalrollupquery"></a> team_goalrollupquery

See team Entity [team_goalrollupquery](team.md#BKMK_team_goalrollupquery) One-To-Many relationship.

### <a name="BKMK_lk_goalrollupquery_createdby"></a> lk_goalrollupquery_createdby

See systemuser Entity [lk_goalrollupquery_createdby](systemuser.md#BKMK_lk_goalrollupquery_createdby) One-To-Many relationship.

### <a name="BKMK_lk_goalrollupquery_createdonbehalfby"></a> lk_goalrollupquery_createdonbehalfby

See systemuser Entity [lk_goalrollupquery_createdonbehalfby](systemuser.md#BKMK_lk_goalrollupquery_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_goalrollupquery_modifiedby"></a> lk_goalrollupquery_modifiedby

See systemuser Entity [lk_goalrollupquery_modifiedby](systemuser.md#BKMK_lk_goalrollupquery_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_goalrollupquery_modifiedonbehalfby"></a> lk_goalrollupquery_modifiedonbehalfby

See systemuser Entity [lk_goalrollupquery_modifiedonbehalfby](systemuser.md#BKMK_lk_goalrollupquery_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_goalrollupquery"></a> business_unit_goalrollupquery

See businessunit Entity [business_unit_goalrollupquery](businessunit.md#BKMK_business_unit_goalrollupquery) One-To-Many relationship.
goalrollupquery

