---
title: "RelationshipRoleMap Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the RelationshipRoleMap entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# RelationshipRoleMap Entity Reference

Mapping of the primary associated objects between which the relationship role is valid.

## Entity Properties

**DisplayName**: Relationship Role Map<br />
**DisplayCollectionName**: Relationship Role Maps<br />
**SchemaName**: RelationshipRoleMap<br />
**CollectionSchemaName**: RelationshipRoleMaps<br />
**LogicalName**: relationshiprolemap<br />
**LogicalCollectionName**: relationshiprolemaps<br />
**EntitySetName**: relationshiprolemaps<br />
**PrimaryIdAttribute**: relationshiprolemapid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AssociateObjectTypeCode](#BKMK_AssociateObjectTypeCode)
- [PrimaryObjectTypeCode](#BKMK_PrimaryObjectTypeCode)
- [RelationshipRoleId](#BKMK_RelationshipRoleId)
- [RelationshipRoleMapId](#BKMK_RelationshipRoleMapId)


### <a name="BKMK_AssociateObjectTypeCode"></a> AssociateObjectTypeCode

**Description**: Type of the associated entity in the relationship role mapping.<br />
**DisplayName**: <br />
**LogicalName**: associateobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_PrimaryObjectTypeCode"></a> PrimaryObjectTypeCode

**Description**: Type of the primary entity in the relationship role mapping.<br />
**DisplayName**: <br />
**LogicalName**: primaryobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_RelationshipRoleId"></a> RelationshipRoleId

**Description**: Unique identifier of the relationship role. This relationship role is only valid in a relationship between an entity of type specified in the primaryobjecttypecode property and an entity of type specified in the associateobjecttypecode property.<br />
**DisplayName**: <br />
**LogicalName**: relationshiproleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: relationshiprole


### <a name="BKMK_RelationshipRoleMapId"></a> RelationshipRoleMapId

**Description**: Unique identifier of the relationship role map.<br />
**DisplayName**: <br />
**LogicalName**: relationshiprolemapid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

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
- [OrganizationId](#BKMK_OrganizationId)
- [RelationshipRoleIdName](#BKMK_RelationshipRoleIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the relationship role map.<br />
**DisplayName**: <br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: Name of the user who created the relationship role map.<br />
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

**Description**: YomiName of the user who created the relationship role map.<br />
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

**Description**: Date and time when the relationship role map was created.<br />
**DisplayName**: <br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the relationshiprolemap.<br />
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

**Description**: Unique identifier of the user who last modified the relationship role map.<br />
**DisplayName**: <br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: Name of the user who last modified the relationship role map.<br />
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

**Description**: YomiName of the user who last modified the relationship role map.<br />
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

**Description**: Date and time when the relationship role map record was last modified.<br />
**DisplayName**: <br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the relationshiprolemap.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization with which the relationship role map is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_RelationshipRoleIdName"></a> RelationshipRoleIdName

**Description**: Name of the relationship role.<br />
**DisplayName**: <br />
**LogicalName**: relationshiproleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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

- [RelationshipRoleMap_BulkDeleteFailures](#BKMK_RelationshipRoleMap_BulkDeleteFailures)
- [userentityinstancedata_relationshiprolemap](#BKMK_userentityinstancedata_relationshiprolemap)
- [RelationshipRoleMap_AsyncOperations](#BKMK_RelationshipRoleMap_AsyncOperations)


### <a name="BKMK_RelationshipRoleMap_BulkDeleteFailures"></a> RelationshipRoleMap_BulkDeleteFailures

Same as bulkdeletefailure entity [RelationshipRoleMap_BulkDeleteFailures](bulkdeletefailure.md#BKMK_RelationshipRoleMap_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RelationshipRoleMap_BulkDeleteFailures<br />
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


### <a name="BKMK_userentityinstancedata_relationshiprolemap"></a> userentityinstancedata_relationshiprolemap

Same as userentityinstancedata entity [userentityinstancedata_relationshiprolemap](userentityinstancedata.md#BKMK_userentityinstancedata_relationshiprolemap) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_relationshiprolemap<br />
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


### <a name="BKMK_RelationshipRoleMap_AsyncOperations"></a> RelationshipRoleMap_AsyncOperations

Same as asyncoperation entity [RelationshipRoleMap_AsyncOperations](asyncoperation.md#BKMK_RelationshipRoleMap_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: RelationshipRoleMap_AsyncOperations<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [modifiedby_relationship_role_map](#BKMK_modifiedby_relationship_role_map)
- [createdby_relationship_role_map](#BKMK_createdby_relationship_role_map)
- [lk_relationshiprolemap_modifiedonbehalfby](#BKMK_lk_relationshiprolemap_modifiedonbehalfby)
- [relationship_role_relationship_role_map](#BKMK_relationship_role_relationship_role_map)
- [lk_relationshiprolemap_createdonbehalfby](#BKMK_lk_relationshiprolemap_createdonbehalfby)


### <a name="BKMK_modifiedby_relationship_role_map"></a> modifiedby_relationship_role_map

See systemuser Entity [modifiedby_relationship_role_map](systemuser.md#BKMK_modifiedby_relationship_role_map) One-To-Many relationship.

### <a name="BKMK_createdby_relationship_role_map"></a> createdby_relationship_role_map

See systemuser Entity [createdby_relationship_role_map](systemuser.md#BKMK_createdby_relationship_role_map) One-To-Many relationship.

### <a name="BKMK_lk_relationshiprolemap_modifiedonbehalfby"></a> lk_relationshiprolemap_modifiedonbehalfby

See systemuser Entity [lk_relationshiprolemap_modifiedonbehalfby](systemuser.md#BKMK_lk_relationshiprolemap_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_relationship_role_relationship_role_map"></a> relationship_role_relationship_role_map

See relationshiprole Entity [relationship_role_relationship_role_map](relationshiprole.md#BKMK_relationship_role_relationship_role_map) One-To-Many relationship.

### <a name="BKMK_lk_relationshiprolemap_createdonbehalfby"></a> lk_relationshiprolemap_createdonbehalfby

See systemuser Entity [lk_relationshiprolemap_createdonbehalfby](systemuser.md#BKMK_lk_relationshiprolemap_createdonbehalfby) One-To-Many relationship.
relationshiprolemap

