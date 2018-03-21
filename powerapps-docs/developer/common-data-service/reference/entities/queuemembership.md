---
title: "QueueMembership Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the QueueMembership entity."

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
# QueueMembership Entity Reference



## Entity Properties

**DisplayName**: <br />
**DisplayCollectionName**: <br />
**SchemaName**: QueueMembership<br />
**CollectionSchemaName**: <br />
**LogicalName**: queuemembership<br />
**LogicalCollectionName**: <br />
**EntitySetName**: queuememberships<br />
**PrimaryIdAttribute**: queuemembershipid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.


### <a name="BKMK_QueueMembershipId"></a> QueueMembershipId

**Description**: Unique identifier of the queue membership.<br />
**DisplayName**: <br />
**LogicalName**: queuemembershipid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [QueueId](#BKMK_QueueId)
- [SystemUserId](#BKMK_SystemUserId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_QueueId"></a> QueueId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: queueid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SystemUserId"></a> SystemUserId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: systemuserid<br />
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

<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the QueueMembership entity is the first entity in the relationship. Listed by **SchemaName**.


### <a name="BKMK_queuemembership_association"></a> queuemembership_association

See queue Entity [queuemembership_association](queue.md#BKMK_queuemembership_association) Many-To-Many Relationship.
queuemembership

