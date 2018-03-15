---
title: "LookUpMapping Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the LookUpMapping entity."

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
# LookUpMapping Entity Reference

In a data map, maps a lookup attribute in a source file to Microsoft Dynamics 365.

## Entity Properties

**DisplayName**: Lookup Mapping<br />
**DisplayCollectionName**: Lookup Mappings<br />
**SchemaName**: LookUpMapping<br />
**CollectionSchemaName**: LookUpMappings<br />
**LogicalName**: lookupmapping<br />
**LogicalCollectionName**: lookupmappings<br />
**EntitySetName**: lookupmappings<br />
**PrimaryIdAttribute**: lookupmappingid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ColumnMappingId](#BKMK_ColumnMappingId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [LookUpAttributeName](#BKMK_LookUpAttributeName)
- [LookUpEntityName](#BKMK_LookUpEntityName)
- [LookUpMappingId](#BKMK_LookUpMappingId)
- [LookUpSourceCode](#BKMK_LookUpSourceCode)
- [ProcessCode](#BKMK_ProcessCode)
- [StatusCode](#BKMK_StatusCode)
- [TransformationParameterMappingId](#BKMK_TransformationParameterMappingId)


### <a name="BKMK_ColumnMappingId"></a> ColumnMappingId

**Description**: Unique identifier of the column mapping with which this lookup mapping is associated.<br />
**DisplayName**: Column Mapping Id<br />
**LogicalName**: columnmappingid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: columnmapping


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the component is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_LookUpAttributeName"></a> LookUpAttributeName

**Description**: Name of the field with which the lookup is associated.<br />
**DisplayName**: Lookup Field Name<br />
**LogicalName**: lookupattributename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_LookUpEntityName"></a> LookUpEntityName

**Description**: Name of the entity with which the lookup is associated.<br />
**DisplayName**: Lookup Entity Name<br />
**LogicalName**: lookupentityname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_LookUpMappingId"></a> LookUpMappingId

**Description**: Unique identifier of the lookup mapping.<br />
**DisplayName**: <br />
**LogicalName**: lookupmappingid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_LookUpSourceCode"></a> LookUpSourceCode

**Description**: Lookup source code for lookup mapping.<br />
**DisplayName**: Lookup Source<br />
**LogicalName**: lookupsourcecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Source
- **Value**: 1 **Label**: System



### <a name="BKMK_ProcessCode"></a> ProcessCode

**Description**: Information about whether the lookup mapping has to be processed.<br />
**DisplayName**: Process Code<br />
**LogicalName**: processcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Process
- **Value**: 2 **Label**: Ignore
- **Value**: 3 **Label**: Internal



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the lookup mapping.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Active **State**: 0



### <a name="BKMK_TransformationParameterMappingId"></a> TransformationParameterMappingId

**Description**: Unique identifier of the transformation parameter mapping with which this lookup mapping is associated.<br />
**DisplayName**: Transformation Parameter Mapping Id<br />
**LogicalName**: transformationparametermappingid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transformationparametermapping

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ColumnMappingIdName](#BKMK_ColumnMappingIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [LookUpMappingIdUnique](#BKMK_LookUpMappingIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [StateCode](#BKMK_StateCode)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


### <a name="BKMK_ColumnMappingIdName"></a> ColumnMappingIdName

**Description**: Name of the column mapping.<br />
**DisplayName**: <br />
**LogicalName**: columnmappingidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the lookup mapping.<br />
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

**Description**: Date and time when the lookup mapping was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the lookupmapping.<br />
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


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Information that specifies whether this component is managed.<br />
**DisplayName**: State<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_LookUpMappingIdUnique"></a> LookUpMappingIdUnique

**Description**: Unique identifier of the LookUp Mapping.<br />
**DisplayName**: <br />
**LogicalName**: lookupmappingidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the lookup mapping.<br />
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

**Description**: Date and time when the lookup mapping was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the lookupmapping.<br />
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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: For internal use only.<br />
**DisplayName**: Record Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the lookup mapping.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 0 **InvariantName**: Active



### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_userentityinstancedata_lookupmapping"></a> userentityinstancedata_lookupmapping

Same as userentityinstancedata entity [userentityinstancedata_lookupmapping](userentityinstancedata.md#BKMK_userentityinstancedata_lookupmapping) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_lookupmapping<br />
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

- [lk_lookupmapping_createdby](#BKMK_lk_lookupmapping_createdby)
- [lk_lookupmapping_createdonbehalfby](#BKMK_lk_lookupmapping_createdonbehalfby)
- [LookUpMapping_ColumnMapping](#BKMK_LookUpMapping_ColumnMapping)
- [lk_lookupmapping_modifiedby](#BKMK_lk_lookupmapping_modifiedby)
- [LookUpMapping_TransformationParameterMapping](#BKMK_LookUpMapping_TransformationParameterMapping)
- [lk_lookupmapping_modifiedonbehalfby](#BKMK_lk_lookupmapping_modifiedonbehalfby)


### <a name="BKMK_lk_lookupmapping_createdby"></a> lk_lookupmapping_createdby

See systemuser Entity [lk_lookupmapping_createdby](systemuser.md#BKMK_lk_lookupmapping_createdby) One-To-Many relationship.

### <a name="BKMK_lk_lookupmapping_createdonbehalfby"></a> lk_lookupmapping_createdonbehalfby

See systemuser Entity [lk_lookupmapping_createdonbehalfby](systemuser.md#BKMK_lk_lookupmapping_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_LookUpMapping_ColumnMapping"></a> LookUpMapping_ColumnMapping

See columnmapping Entity [LookUpMapping_ColumnMapping](columnmapping.md#BKMK_LookUpMapping_ColumnMapping) One-To-Many relationship.

### <a name="BKMK_lk_lookupmapping_modifiedby"></a> lk_lookupmapping_modifiedby

See systemuser Entity [lk_lookupmapping_modifiedby](systemuser.md#BKMK_lk_lookupmapping_modifiedby) One-To-Many relationship.

### <a name="BKMK_LookUpMapping_TransformationParameterMapping"></a> LookUpMapping_TransformationParameterMapping

See transformationparametermapping Entity [LookUpMapping_TransformationParameterMapping](transformationparametermapping.md#BKMK_LookUpMapping_TransformationParameterMapping) One-To-Many relationship.

### <a name="BKMK_lk_lookupmapping_modifiedonbehalfby"></a> lk_lookupmapping_modifiedonbehalfby

See systemuser Entity [lk_lookupmapping_modifiedonbehalfby](systemuser.md#BKMK_lk_lookupmapping_modifiedonbehalfby) One-To-Many relationship.
lookupmapping

