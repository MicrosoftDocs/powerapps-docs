---
title: "DuplicateRuleCondition Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the DuplicateRuleCondition entity."

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
ms.date: 03/07/2018
ms.author: jdaly
---
# DuplicateRuleCondition Entity Reference

Condition of a duplicate detection rule.

## Entity Properties

**DisplayName**: Duplicate Rule Condition<br />
**DisplayCollectionName**: Duplicate Rule Conditions<br />
**SchemaName**: DuplicateRuleCondition<br />
**CollectionSchemaName**: DuplicateRuleConditions<br />
**LogicalName**: duplicaterulecondition<br />
**LogicalCollectionName**: duplicateruleconditions<br />
**EntitySetName**: duplicateruleconditions<br />
**PrimaryIdAttribute**: duplicateruleconditionid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BaseAttributeName](#BKMK_BaseAttributeName)
- [DuplicateRuleConditionId](#BKMK_DuplicateRuleConditionId)
- [IgnoreBlankValues](#BKMK_IgnoreBlankValues)
- [MatchingAttributeName](#BKMK_MatchingAttributeName)
- [OperatorCode](#BKMK_OperatorCode)
- [OperatorParam](#BKMK_OperatorParam)
- [RegardingObjectId](#BKMK_RegardingObjectId)


### <a name="BKMK_BaseAttributeName"></a> BaseAttributeName

**Description**: Field that is being compared.<br />
**DisplayName**: Base Field<br />
**LogicalName**: baseattributename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_DuplicateRuleConditionId"></a> DuplicateRuleConditionId

**Description**: Unique identifier of the condition.<br />
**DisplayName**: Duplicate Rule Condition<br />
**LogicalName**: duplicateruleconditionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IgnoreBlankValues"></a> IgnoreBlankValues

**Description**: Determines whether to consider blank values as non-duplicate values<br />
**DisplayName**: Ignore Blank Values<br />
**LogicalName**: ignoreblankvalues<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: False


### <a name="BKMK_MatchingAttributeName"></a> MatchingAttributeName

**Description**: Field that is being compared with the base field.<br />
**DisplayName**: Matching Field<br />
**LogicalName**: matchingattributename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_OperatorCode"></a> OperatorCode

**Description**: Operator for this rule condition.<br />
**DisplayName**: Operator Code<br />
**LogicalName**: operatorcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Exact Match
- **Value**: 1 **Label**: Same First Characters
- **Value**: 2 **Label**: Same Last Characters
- **Value**: 3 **Label**: Same Date
- **Value**: 4 **Label**: Same Date and Time
- **Value**: 5 **Label**: Exact Match (Pick List Label)
- **Value**: 6 **Label**: Exact Match (Pick List Value)



### <a name="BKMK_OperatorParam"></a> OperatorParam

**Description**: Parameter value of N if the operator is Same First Characters or Same Last Characters.<br />
**DisplayName**: Operator Parameter<br />
**LogicalName**: operatorparam<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 1


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Unique identifier of the object with which the condition is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: duplicaterule

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the condition.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the condition was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the duplicate rule condition.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
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

**Description**: Unique identifier of the user who last modified the condition.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the condition was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the duplicate rule condition.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
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


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the duplicate rule condition.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the condition.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the condition.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Uniqueidentifier<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [DuplicateRuleCondition_SyncErrors](#BKMK_DuplicateRuleCondition_SyncErrors)
- [userentityinstancedata_duplicaterulecondition](#BKMK_userentityinstancedata_duplicaterulecondition)


### <a name="BKMK_DuplicateRuleCondition_SyncErrors"></a> DuplicateRuleCondition_SyncErrors

Same as syncerror entity [DuplicateRuleCondition_SyncErrors](syncerror.md#BKMK_DuplicateRuleCondition_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: DuplicateRuleCondition_SyncErrors<br />
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


### <a name="BKMK_userentityinstancedata_duplicaterulecondition"></a> userentityinstancedata_duplicaterulecondition

Same as userentityinstancedata entity [userentityinstancedata_duplicaterulecondition](userentityinstancedata.md#BKMK_userentityinstancedata_duplicaterulecondition) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_duplicaterulecondition<br />
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

- [lk_duplicaterulecondition_createdonbehalfby](#BKMK_lk_duplicaterulecondition_createdonbehalfby)
- [DuplicateRule_DuplicateRuleConditions](#BKMK_DuplicateRule_DuplicateRuleConditions)
- [lk_duplicaterulecondition_modifiedonbehalfby](#BKMK_lk_duplicaterulecondition_modifiedonbehalfby)
- [lk_duplicateruleconditionbase_modifiedby](#BKMK_lk_duplicateruleconditionbase_modifiedby)
- [lk_duplicateruleconditionbase_createdby](#BKMK_lk_duplicateruleconditionbase_createdby)


### <a name="BKMK_lk_duplicaterulecondition_createdonbehalfby"></a> lk_duplicaterulecondition_createdonbehalfby

See systemuser Entity [lk_duplicaterulecondition_createdonbehalfby](systemuser.md#BKMK_lk_duplicaterulecondition_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_DuplicateRule_DuplicateRuleConditions"></a> DuplicateRule_DuplicateRuleConditions

See duplicaterule Entity [DuplicateRule_DuplicateRuleConditions](duplicaterule.md#BKMK_DuplicateRule_DuplicateRuleConditions) One-To-Many relationship.

### <a name="BKMK_lk_duplicaterulecondition_modifiedonbehalfby"></a> lk_duplicaterulecondition_modifiedonbehalfby

See systemuser Entity [lk_duplicaterulecondition_modifiedonbehalfby](systemuser.md#BKMK_lk_duplicaterulecondition_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_duplicateruleconditionbase_modifiedby"></a> lk_duplicateruleconditionbase_modifiedby

See systemuser Entity [lk_duplicateruleconditionbase_modifiedby](systemuser.md#BKMK_lk_duplicateruleconditionbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_duplicateruleconditionbase_createdby"></a> lk_duplicateruleconditionbase_createdby

See systemuser Entity [lk_duplicateruleconditionbase_createdby](systemuser.md#BKMK_lk_duplicateruleconditionbase_createdby) One-To-Many relationship.
duplicaterulecondition

