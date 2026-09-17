---
title: "Time Stamp Date Mapping (TimeStampDateMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Time Stamp Date Mapping (TimeStampDateMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Time Stamp Date Mapping (TimeStampDateMapping) table/entity reference (Microsoft Dataverse)

For internal use only.`

## Messages

The following table lists the messages for the Time Stamp Date Mapping (TimeStampDateMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Time Stamp Date Mapping (TimeStampDateMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Time Stamp Date Mapping** |
| **DisplayCollectionName** | **Time Stamp Date Mappings** |
| **SchemaName** | `TimeStampDateMapping` |
| **CollectionSchemaName** | `TimeStampDateMappings` |
| **EntitySetName** | `timestampdatemappings`|
| **LogicalName** | `timestampdatemapping` |
| **LogicalCollectionName** | `timestampdatemappings` |
| **PrimaryIdAttribute** | `timestampdatemappingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

### <a name="BKMK_TimeStampDateMappingId"></a> TimeStampDateMappingId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timestampdatemappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Date](#BKMK_Date)
- [TimeStamp](#BKMK_TimeStamp)

### <a name="BKMK_Date"></a> Date

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`date`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_TimeStamp"></a> TimeStamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timestamp`|
|RequiredLevel|SystemRequired|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_timestampdatemapping_DeletedItemReferences"></a> timestampdatemapping_DeletedItemReferences

Many-To-One Relationship: [deleteditemreference timestampdatemapping_DeletedItemReferences](deleteditemreference.md#BKMK_timestampdatemapping_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencingEntity|`deleteditemreference`|
|ReferencingAttribute|`deletedobject`|
|ReferencedEntityNavigationPropertyName|`timestampdatemapping_DeletedItemReferences`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.timestampdatemapping?displayProperty=fullName>
