---
title: "AttributeMap Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the AttributeMap entity."

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
# AttributeMap Entity Reference

Represents a mapping between attributes where the attribute values should be copied from a record into the form of a new related record.

## Entity Properties

**DisplayName**: Attribute Map<br />
**DisplayCollectionName**: Attribute Maps<br />
**SchemaName**: AttributeMap<br />
**CollectionSchemaName**: AttributeMaps<br />
**LogicalName**: attributemap<br />
**LogicalCollectionName**: attributemaps<br />
**EntitySetName**: attributemaps<br />
**PrimaryIdAttribute**: attributemapid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeMapId](#BKMK_AttributeMapId)
- [EntityMapId](#BKMK_EntityMapId)
- [IsSystem](#BKMK_IsSystem)
- [ParentAttributeMapId](#BKMK_ParentAttributeMapId)
- [SourceAttributeName](#BKMK_SourceAttributeName)
- [TargetAttributeName](#BKMK_TargetAttributeName)


### <a name="BKMK_AttributeMapId"></a> AttributeMapId

**Description**: Unique identifier of the attribute map.<br />
**DisplayName**: <br />
**LogicalName**: attributemapid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_EntityMapId"></a> EntityMapId

**Description**: Unique identifier of the entity map with which the attribute map is associated.<br />
**DisplayName**: <br />
**LogicalName**: entitymapid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: entitymap


### <a name="BKMK_IsSystem"></a> IsSystem

**Description**: Information about whether this attribute map is user-defined or system-defined.<br />
**DisplayName**: Is System<br />
**LogicalName**: issystem<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ParentAttributeMapId"></a> ParentAttributeMapId

**Description**: Unique identifier of the parent attribute map.<br />
**DisplayName**: <br />
**LogicalName**: parentattributemapid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: attributemap


### <a name="BKMK_SourceAttributeName"></a> SourceAttributeName

**Description**: Name of the source attribute for the mapping.<br />
**DisplayName**: <br />
**LogicalName**: sourceattributename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_TargetAttributeName"></a> TargetAttributeName

**Description**: Name of the target attribute for the mapping.<br />
**DisplayName**: <br />
**LogicalName**: targetattributename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AttributeMapIdUnique](#BKMK_AttributeMapIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AttributeMapIdUnique"></a> AttributeMapIdUnique

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: attributemapidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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

**Description**: Unique identifier of the user who created the attribute map.<br />
**DisplayName**: <br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the attribute map was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the attributemap.<br />
**DisplayName**: <br />
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

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the attribute map.<br />
**DisplayName**: <br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the attribute map was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the attributemap.<br />
**DisplayName**: <br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization with which the attribute map is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


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


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
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

- [AttributeMap_AsyncOperations](#BKMK_AttributeMap_AsyncOperations)
- [userentityinstancedata_attributemap](#BKMK_userentityinstancedata_attributemap)
- [attribute_map_attribute_maps](#BKMK_attribute_map_attribute_maps)
- [AttributeMap_BulkDeleteFailures](#BKMK_AttributeMap_BulkDeleteFailures)


### <a name="BKMK_AttributeMap_AsyncOperations"></a> AttributeMap_AsyncOperations

Same as asyncoperation entity [AttributeMap_AsyncOperations](asyncoperation.md#BKMK_AttributeMap_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AttributeMap_AsyncOperations<br />
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


### <a name="BKMK_userentityinstancedata_attributemap"></a> userentityinstancedata_attributemap

Same as userentityinstancedata entity [userentityinstancedata_attributemap](userentityinstancedata.md#BKMK_userentityinstancedata_attributemap) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_attributemap<br />
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


### <a name="BKMK_attribute_map_attribute_maps"></a> attribute_map_attribute_maps

Same as attributemap entity [attribute_map_attribute_maps](attributemap.md#BKMK_attribute_map_attribute_maps) Many-To-One relationship.

**ReferencingEntity**: attributemap<br />
**ReferencingAttribute**: parentattributemapid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: attribute_map_attribute_maps<br />
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


### <a name="BKMK_AttributeMap_BulkDeleteFailures"></a> AttributeMap_BulkDeleteFailures

Same as bulkdeletefailure entity [AttributeMap_BulkDeleteFailures](bulkdeletefailure.md#BKMK_AttributeMap_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: AttributeMap_BulkDeleteFailures<br />
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

- [entity_map_attribute_maps](#BKMK_entity_map_attribute_maps)
- [organization_attributemap](#BKMK_organization_attributemap)
- [modifiedonbehalfby_attributemap](#BKMK_modifiedonbehalfby_attributemap)
- [createdonbehalfby_attributemap](#BKMK_createdonbehalfby_attributemap)
- [createdby_attributemap](#BKMK_createdby_attributemap)
- [modifiedby_attributemap](#BKMK_modifiedby_attributemap)
- [attribute_map_attribute_maps](#BKMK_attribute_map_attribute_maps)


### <a name="BKMK_entity_map_attribute_maps"></a> entity_map_attribute_maps

See entitymap Entity [entity_map_attribute_maps](entitymap.md#BKMK_entity_map_attribute_maps) One-To-Many relationship.

### <a name="BKMK_organization_attributemap"></a> organization_attributemap

See organization Entity [organization_attributemap](organization.md#BKMK_organization_attributemap) One-To-Many relationship.

### <a name="BKMK_modifiedonbehalfby_attributemap"></a> modifiedonbehalfby_attributemap

See systemuser Entity [modifiedonbehalfby_attributemap](systemuser.md#BKMK_modifiedonbehalfby_attributemap) One-To-Many relationship.

### <a name="BKMK_createdonbehalfby_attributemap"></a> createdonbehalfby_attributemap

See systemuser Entity [createdonbehalfby_attributemap](systemuser.md#BKMK_createdonbehalfby_attributemap) One-To-Many relationship.

### <a name="BKMK_createdby_attributemap"></a> createdby_attributemap

See systemuser Entity [createdby_attributemap](systemuser.md#BKMK_createdby_attributemap) One-To-Many relationship.

### <a name="BKMK_modifiedby_attributemap"></a> modifiedby_attributemap

See systemuser Entity [modifiedby_attributemap](systemuser.md#BKMK_modifiedby_attributemap) One-To-Many relationship.

### <a name="BKMK_attribute_map_attribute_maps"></a> attribute_map_attribute_maps

See attributemap Entity [attribute_map_attribute_maps](attributemap.md#BKMK_attribute_map_attribute_maps) One-To-Many relationship.
attributemap

