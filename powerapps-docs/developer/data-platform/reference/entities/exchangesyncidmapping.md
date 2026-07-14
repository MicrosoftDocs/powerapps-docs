---
title: "Exchange Sync Id Mapping (ExchangeSyncIdMapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Exchange Sync Id Mapping (ExchangeSyncIdMapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Exchange Sync Id Mapping (ExchangeSyncIdMapping) table/entity reference (Microsoft Dataverse)

The mapping used to keep track of the IDs for items synced between CRM and Exchange.

## Messages

The following table lists the messages for the Exchange Sync Id Mapping (ExchangeSyncIdMapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /exchangesyncidmappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /exchangesyncidmappings(*exchangesyncidmappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /exchangesyncidmappings(*exchangesyncidmappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /exchangesyncidmappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /exchangesyncidmappings(*exchangesyncidmappingid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /exchangesyncidmappings(*exchangesyncidmappingid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Exchange Sync Id Mapping (ExchangeSyncIdMapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Exchange Sync Id Mapping** |
| **DisplayCollectionName** | **Exchange Sync Id Mappings** |
| **SchemaName** | `ExchangeSyncIdMapping` |
| **CollectionSchemaName** | `ExchangeSyncIdMappings` |
| **EntitySetName** | `exchangesyncidmappings`|
| **LogicalName** | `exchangesyncidmapping` |
| **LogicalCollectionName** | `exchangesyncidmappings` |
| **PrimaryIdAttribute** | `exchangesyncidmappingid` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ExchangeEntryId](#BKMK_ExchangeEntryId)
- [ExchangeSyncIdmappingId](#BKMK_ExchangeSyncIdmappingId)
- [FromCrmChangeType](#BKMK_FromCrmChangeType)
- [IsDeletedInExchange](#BKMK_IsDeletedInExchange)
- [IsUnlinkedInCRM](#BKMK_IsUnlinkedInCRM)
- [ItemSubject](#BKMK_ItemSubject)
- [LastSyncError](#BKMK_LastSyncError)
- [LastSyncErrorCode](#BKMK_LastSyncErrorCode)
- [LastSyncErrorOccurredOn](#BKMK_LastSyncErrorOccurredOn)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Retries](#BKMK_Retries)
- [ToCrmChangeType](#BKMK_ToCrmChangeType)
- [UserDecision](#BKMK_UserDecision)

### <a name="BKMK_ExchangeEntryId"></a> ExchangeEntryId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Exchange Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangeentryid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_ExchangeSyncIdmappingId"></a> ExchangeSyncIdmappingId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`exchangesyncidmappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_FromCrmChangeType"></a> FromCrmChangeType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fromcrmchangetype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IsDeletedInExchange"></a> IsDeletedInExchange

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdeletedinexchange`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`exchangesyncidmapping_isdeletedinexchange`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsUnlinkedInCRM"></a> IsUnlinkedInCRM

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isunlinkedincrm`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`exchangesyncidmapping_isunlinkedincrm`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ItemSubject"></a> ItemSubject

|Property|Value|
|---|---|
|Description||
|DisplayName|**Item Subject**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`itemsubject`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_LastSyncError"></a> LastSyncError

|Property|Value|
|---|---|
|Description||
|DisplayName|**Sync Error**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerror`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_LastSyncErrorCode"></a> LastSyncErrorCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerrorcode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_LastSyncErrorOccurredOn"></a> LastSyncErrorOccurredOn

|Property|Value|
|---|---|
|Description|**Last Sync Error Time**|
|DisplayName|**Last Sync Error Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`lastsyncerroroccurredon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Crm Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Retries"></a> Retries

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`retries`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ToCrmChangeType"></a> ToCrmChangeType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`tocrmchangetype`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_UserDecision"></a> UserDecision

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`userdecision`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedOn](#BKMK_CreatedOn)
- [ModifiedOn](#BKMK_ModifiedOn)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_exchangesyncidmapping](#BKMK_business_unit_exchangesyncidmapping)
- [owner_exchangesyncidmapping](#BKMK_owner_exchangesyncidmapping)
- [team_exchangesyncidmapping](#BKMK_team_exchangesyncidmapping)
- [user_exchangesyncidmapping](#BKMK_user_exchangesyncidmapping)

### <a name="BKMK_business_unit_exchangesyncidmapping"></a> business_unit_exchangesyncidmapping

One-To-Many Relationship: [businessunit business_unit_exchangesyncidmapping](businessunit.md#BKMK_business_unit_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_exchangesyncidmapping"></a> owner_exchangesyncidmapping

One-To-Many Relationship: [owner owner_exchangesyncidmapping](owner.md#BKMK_owner_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_exchangesyncidmapping"></a> team_exchangesyncidmapping

One-To-Many Relationship: [team team_exchangesyncidmapping](team.md#BKMK_team_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_exchangesyncidmapping"></a> user_exchangesyncidmapping

One-To-Many Relationship: [systemuser user_exchangesyncidmapping](systemuser.md#BKMK_user_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.exchangesyncidmapping?displayProperty=fullName>
