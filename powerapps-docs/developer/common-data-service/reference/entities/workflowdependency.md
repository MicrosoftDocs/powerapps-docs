---
title: "WorkflowDependency Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the WorkflowDependency entity."

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
# WorkflowDependency Entity Reference

Dependencies for a process.

## Entity Properties

**DisplayName**: Process Dependency<br />
**DisplayCollectionName**: Process Dependencies<br />
**SchemaName**: WorkflowDependency<br />
**CollectionSchemaName**: WorkflowDependencies<br />
**LogicalName**: workflowdependency<br />
**LogicalCollectionName**: workflowdependencies<br />
**EntitySetName**: workflowdependencies<br />
**PrimaryIdAttribute**: workflowdependencyid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CustomEntityName](#BKMK_CustomEntityName)
- [DependentAttributeName](#BKMK_DependentAttributeName)
- [DependentEntityName](#BKMK_DependentEntityName)
- [EntityAttributes](#BKMK_EntityAttributes)
- [ParameterName](#BKMK_ParameterName)
- [ParameterType](#BKMK_ParameterType)
- [RelatedAttributeName](#BKMK_RelatedAttributeName)
- [RelatedEntityName](#BKMK_RelatedEntityName)
- [SdkMessageId](#BKMK_SdkMessageId)
- [Type](#BKMK_Type)
- [WorkflowDependencyId](#BKMK_WorkflowDependencyId)
- [WorkflowId](#BKMK_WorkflowId)


### <a name="BKMK_CustomEntityName"></a> CustomEntityName

**Description**: Name of the entity used in the process.<br />
**DisplayName**: Custom Entity<br />
**LogicalName**: customentityname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_DependentAttributeName"></a> DependentAttributeName

**Description**: Name of the attribute used in the process.<br />
**DisplayName**: Dependent Attribute Name<br />
**LogicalName**: dependentattributename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_DependentEntityName"></a> DependentEntityName

**Description**: Name of the entity used in the process.<br />
**DisplayName**: Dependent Entity Name<br />
**LogicalName**: dependententityname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_EntityAttributes"></a> EntityAttributes

**Description**: Comma-separated list of attributes that will be passed to process instance.<br />
**DisplayName**: <br />
**LogicalName**: entityattributes<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_ParameterName"></a> ParameterName

**Description**: Name of the process parameter.<br />
**DisplayName**: <br />
**LogicalName**: parametername<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ParameterType"></a> ParameterType

**Description**: Fully qualified name of the CLR type of the local parameter.<br />
**DisplayName**: <br />
**LogicalName**: parametertype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_RelatedAttributeName"></a> RelatedAttributeName

**Description**: Attribute of the primary entity that specifies related entity.<br />
**DisplayName**: <br />
**LogicalName**: relatedattributename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_RelatedEntityName"></a> RelatedEntityName

**Description**: Name of the related entity.<br />
**DisplayName**: Related Entity<br />
**LogicalName**: relatedentityname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_SdkMessageId"></a> SdkMessageId

**Description**: Unique identifier of the SDK message.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sdkmessage


### <a name="BKMK_Type"></a> Type

**Description**: Type of the process dependency.<br />
**DisplayName**: Type<br />
**LogicalName**: type<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Sdk association
- **Value**: 2 **Label**: Local parameter
- **Value**: 3 **Label**: Primary entity
- **Value**: 4 **Label**: Primary entity - before SDK operation
- **Value**: 5 **Label**: Primary entity - after SDK operation
- **Value**: 6 **Label**: Related entity
- **Value**: 7 **Label**: Custom entity definition that workflow depends on
- **Value**: 8 **Label**: Attribute definition that workflow depends on
- **Value**: 9 **Label**: Argument Entity that workflow depends on



### <a name="BKMK_WorkflowDependencyId"></a> WorkflowDependencyId

**Description**: Unique identifier of the process dependency.<br />
**DisplayName**: Process Dependency<br />
**LogicalName**: workflowdependencyid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_WorkflowId"></a> WorkflowId

**Description**: Unique identifier of the process with which the dependency is associated.<br />
**DisplayName**: Process<br />
**LogicalName**: workflowid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: workflow

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
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the process dependency.<br />
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

**Description**: Date and time when the process dependency was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the process dependency.<br />
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

**Description**: Unique identifier of the user who last modified the process dependency.<br />
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

**Description**: Date and time when the process dependency was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the process dependency.<br />
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


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the parent workflow instance.<br />
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

**Description**: Unique identifier of the business unit that owns the process dependency.<br />
**DisplayName**: <br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the process dependency.<br />
**DisplayName**: <br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
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


### <a name="BKMK_userentityinstancedata_workflowdependency"></a> userentityinstancedata_workflowdependency

Same as userentityinstancedata entity [userentityinstancedata_workflowdependency](userentityinstancedata.md#BKMK_userentityinstancedata_workflowdependency) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_workflowdependency<br />
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

- [workflow_dependency_modifiedonbehalfby](#BKMK_workflow_dependency_modifiedonbehalfby)
- [workflow_dependency_createdonbehalfby](#BKMK_workflow_dependency_createdonbehalfby)
- [workflow_dependency_modifiedby](#BKMK_workflow_dependency_modifiedby)
- [sdkmessageid_workflow_dependency](#BKMK_sdkmessageid_workflow_dependency)
- [workflow_dependency_createdby](#BKMK_workflow_dependency_createdby)
- [workflow_dependencies](#BKMK_workflow_dependencies)


### <a name="BKMK_workflow_dependency_modifiedonbehalfby"></a> workflow_dependency_modifiedonbehalfby

See systemuser Entity [workflow_dependency_modifiedonbehalfby](systemuser.md#BKMK_workflow_dependency_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_workflow_dependency_createdonbehalfby"></a> workflow_dependency_createdonbehalfby

See systemuser Entity [workflow_dependency_createdonbehalfby](systemuser.md#BKMK_workflow_dependency_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_workflow_dependency_modifiedby"></a> workflow_dependency_modifiedby

See systemuser Entity [workflow_dependency_modifiedby](systemuser.md#BKMK_workflow_dependency_modifiedby) One-To-Many relationship.

### <a name="BKMK_sdkmessageid_workflow_dependency"></a> sdkmessageid_workflow_dependency

See sdkmessage Entity [sdkmessageid_workflow_dependency](sdkmessage.md#BKMK_sdkmessageid_workflow_dependency) One-To-Many relationship.

### <a name="BKMK_workflow_dependency_createdby"></a> workflow_dependency_createdby

See systemuser Entity [workflow_dependency_createdby](systemuser.md#BKMK_workflow_dependency_createdby) One-To-Many relationship.

### <a name="BKMK_workflow_dependencies"></a> workflow_dependencies

See workflow Entity [workflow_dependencies](workflow.md#BKMK_workflow_dependencies) One-To-Many relationship.
workflowdependency

