---
title: "ConnectionRoleObjectTypeCode Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ConnectionRoleObjectTypeCode entity."

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
# ConnectionRoleObjectTypeCode Entity Reference

Specifies the entity type that can play specific role in a connection.

## Entity Properties

**DisplayName**: Connection Role Object Type Code<br />
**DisplayCollectionName**: Connection Role Object Type Codes<br />
**SchemaName**: ConnectionRoleObjectTypeCode<br />
**CollectionSchemaName**: ConnectionRoleObjectTypeCodes<br />
**LogicalName**: connectionroleobjecttypecode<br />
**LogicalCollectionName**: connectionroleobjecttypecodes<br />
**EntitySetName**: connectionroleobjecttypecodes<br />
**PrimaryIdAttribute**: connectionroleobjecttypecodeid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AssociatedObjectTypeCode](#BKMK_AssociatedObjectTypeCode)
- [ConnectionRoleId](#BKMK_ConnectionRoleId)
- [ConnectionRoleObjectTypeCodeId](#BKMK_ConnectionRoleObjectTypeCodeId)


### <a name="BKMK_AssociatedObjectTypeCode"></a> AssociatedObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: associatedobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_ConnectionRoleId"></a> ConnectionRoleId

**Description**: Unique identifier of the connection role associated with the Connection Role Object Type Code.<br />
**DisplayName**: Connection Role<br />
**LogicalName**: connectionroleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: connectionrole


### <a name="BKMK_ConnectionRoleObjectTypeCodeId"></a> ConnectionRoleObjectTypeCodeId

**Description**: Unique identifier of the connection role object type association.<br />
**DisplayName**: <br />
**LogicalName**: connectionroleobjecttypecodeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ConnectionRoleIdName](#BKMK_ConnectionRoleIdName)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ConnectionRoleIdName"></a> ConnectionRoleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: connectionroleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the connectionroleobjecttypecode.<br />
**DisplayName**: Organization <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
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


### <a name="BKMK_userentityinstancedata_connectionroleobjecttypecode"></a> userentityinstancedata_connectionroleobjecttypecode

Same as userentityinstancedata entity [userentityinstancedata_connectionroleobjecttypecode](userentityinstancedata.md#BKMK_userentityinstancedata_connectionroleobjecttypecode) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_connectionroleobjecttypecode<br />
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


### <a name="BKMK_connection_role_connection_role_object_type_codes"></a> connection_role_connection_role_object_type_codes

See connectionrole Entity [connection_role_connection_role_object_type_codes](connectionrole.md#BKMK_connection_role_connection_role_object_type_codes) One-To-Many relationship.
connectionroleobjecttypecode

