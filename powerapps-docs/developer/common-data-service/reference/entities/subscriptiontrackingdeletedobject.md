---
title: "SubscriptionTrackingDeletedObject Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SubscriptionTrackingDeletedObject entity."
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
# SubscriptionTrackingDeletedObject Entity Reference

For internal use only.

## Entity Properties

**DisplayName**: Tracking information for deleted entities<br />
**DisplayCollectionName**: Tracking information for deleted entities<br />
**SchemaName**: SubscriptionTrackingDeletedObject<br />
**CollectionSchemaName**: SubscriptionTrackingDeletedObjects<br />
**LogicalName**: subscriptiontrackingdeletedobject<br />
**LogicalCollectionName**: subscriptiontrackingdeletedobjects<br />
**EntitySetName**: subscriptiontrackingdeletedobjects<br />
**PrimaryIdAttribute**: timestamp<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DeleteTime](#BKMK_DeleteTime)
- [IsLogicalDelete](#BKMK_IsLogicalDelete)


### <a name="BKMK_DeleteTime"></a> DeleteTime

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: deletetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_IsLogicalDelete"></a> IsLogicalDelete

**Description**: Indicates whether solution aware entity record is logical delete or not<br />
**DisplayName**: Is Logical Delete<br />
**LogicalName**: islogicaldelete<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [TimeStamp](#BKMK_TimeStamp)


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Type of entity that was deleted.<br />
**DisplayName**: <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_TimeStamp"></a> TimeStamp

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: timestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


subscriptiontrackingdeletedobject

