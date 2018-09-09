---
title: "ConnectionRoleAssociation Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ConnectionRoleAssociation entity."
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
# ConnectionRoleAssociation Entity Reference



## Entity Properties

**DisplayName**: <br />
**DisplayCollectionName**: <br />
**SchemaName**: ConnectionRoleAssociation<br />
**CollectionSchemaName**: <br />
**LogicalName**: connectionroleassociation<br />
**LogicalCollectionName**: <br />
**EntitySetName**: connectionroleassociations<br />
**PrimaryIdAttribute**: connectionroleassociationid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AssociatedConnectionRoleId](#BKMK_AssociatedConnectionRoleId)
- [ConnectionRoleAssociationId](#BKMK_ConnectionRoleAssociationId)
- [ConnectionRoleId](#BKMK_ConnectionRoleId)


### <a name="BKMK_AssociatedConnectionRoleId"></a> AssociatedConnectionRoleId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: associatedconnectionroleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ConnectionRoleAssociationId"></a> ConnectionRoleAssociationId

**Description**: Unique identifier of the connection role association.<br />
**DisplayName**: <br />
**LogicalName**: connectionroleassociationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ConnectionRoleId"></a> ConnectionRoleId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: connectionroleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


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


### <a name="BKMK_userentityinstancedata_connectionroleassociation"></a> userentityinstancedata_connectionroleassociation

Same as userentityinstancedata entity [userentityinstancedata_connectionroleassociation](userentityinstancedata.md#BKMK_userentityinstancedata_connectionroleassociation) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_connectionroleassociation<br />
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

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the ConnectionRoleAssociation entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_connectionroleassociation_association"></a> connectionroleassociation_association

See connectionrole Entity [connectionroleassociation_association](connectionrole.md#BKMK_connectionroleassociation_association) Many-To-Many Relationship.
connectionroleassociation

