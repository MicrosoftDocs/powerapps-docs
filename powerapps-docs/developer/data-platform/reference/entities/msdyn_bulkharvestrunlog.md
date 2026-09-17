---
title: "Bulk Harvest Run Log (msdyn_bulkharvestrunlog) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Bulk Harvest Run Log (msdyn_bulkharvestrunlog) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Bulk Harvest Run Log (msdyn_bulkharvestrunlog) table/entity reference (Microsoft Dataverse)

Stores the run log for bulk harvesting operations

## Messages

The following table lists the messages for the Bulk Harvest Run Log (msdyn_bulkharvestrunlog) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_bulkharvestrunlogs(*msdyn_bulkharvestrunlogid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_bulkharvestrunlogs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_bulkharvestrunlogs(*msdyn_bulkharvestrunlogid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /msdyn_bulkharvestrunlogs(*msdyn_bulkharvestrunlogid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_bulkharvestrunlogs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_bulkharvestrunlogs(*msdyn_bulkharvestrunlogid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_bulkharvestrunlogs(*msdyn_bulkharvestrunlogid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_bulkharvestrunlogs(*msdyn_bulkharvestrunlogid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Bulk Harvest Run Log (msdyn_bulkharvestrunlog) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Bulk Harvest Run Log** |
| **DisplayCollectionName** | **Bulk Harvest Run Logs** |
| **SchemaName** | `msdyn_bulkharvestrunlog` |
| **CollectionSchemaName** | `msdyn_bulkharvestrunlogs` |
| **EntitySetName** | `msdyn_bulkharvestrunlogs`|
| **LogicalName** | `msdyn_bulkharvestrunlog` |
| **LogicalCollectionName** | `msdyn_bulkharvestrunlogs` |
| **PrimaryIdAttribute** | `msdyn_bulkharvestrunlogid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_bulkharvestrunlogId](#BKMK_msdyn_bulkharvestrunlogId)
- [msdyn_entityid](#BKMK_msdyn_entityid)
- [msdyn_entitylogicalname](#BKMK_msdyn_entitylogicalname)
- [msdyn_harvestbatchid](#BKMK_msdyn_harvestbatchid)
- [msdyn_harvestrunid](#BKMK_msdyn_harvestrunid)
- [msdyn_knowledgearticleid](#BKMK_msdyn_knowledgearticleid)
- [msdyn_knowledgeharvestjobrecordid](#BKMK_msdyn_knowledgeharvestjobrecordid)
- [msdyn_knowledgeharvestplanid](#BKMK_msdyn_knowledgeharvestplanid)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_outcome](#BKMK_msdyn_outcome)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_bulkharvestrunlogId"></a> msdyn_bulkharvestrunlogId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Bulk Harvest Run Log**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_bulkharvestrunlogid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_entityid"></a> msdyn_entityid

|Property|Value|
|---|---|
|Description|**GUID of the source entity record**|
|DisplayName|**Entity ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_entityid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_entitylogicalname"></a> msdyn_entitylogicalname

|Property|Value|
|---|---|
|Description|**Logical name of the source entity (e.g., incident, msdyn\_ocliveworkitem)**|
|DisplayName|**Entity Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_entitylogicalname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_harvestbatchid"></a> msdyn_harvestbatchid

|Property|Value|
|---|---|
|Description|**Identifier for the harvest batch**|
|DisplayName|**Harvest Batch ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestbatchid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_harvestrunid"></a> msdyn_harvestrunid

|Property|Value|
|---|---|
|Description|**Identifier for the harvest run**|
|DisplayName|**Harvest Run ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestrunid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_knowledgearticleid"></a> msdyn_knowledgearticleid

|Property|Value|
|---|---|
|Description|**Reference to Knowledge Article**|
|DisplayName|**Knowledge Article ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgearticleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_msdyn_knowledgeharvestjobrecordid"></a> msdyn_knowledgeharvestjobrecordid

|Property|Value|
|---|---|
|Description|**The unique identifier for the knowledge harvest job record associated with this run log**|
|DisplayName|**Knowledge Harvest Job Record Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgeharvestjobrecordid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_knowledgeharvestplanid"></a> msdyn_knowledgeharvestplanid

|Property|Value|
|---|---|
|Description|**The unique identitifier for the knowledge harvest plan that is the source for this record**|
|DisplayName|**Knowledge Harvest Plan Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgeharvestplanid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**Primary name field (auto-generated)**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_outcome"></a> msdyn_outcome

|Property|Value|
|---|---|
|Description|**Result status of the harvest**|
|DisplayName|**Outcome**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_outcome`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_bulkharvestrunlog_outcome`|

#### msdyn_outcome Choices/Options

|Value|Label|
|---|---|
|100000101|**Created knowledge article**|
|100000102|**Updated knowledge article**|
|100000103|**Created knowledge article but not linked**|
|100000104|**Classified as not relevant**|
|100000105|**Quality check rejected**|
|100000106|**Processing error**|
|100000107|**Knowledge article existed**|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Bulk Harvest Run Log**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_bulkharvestrunlog_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Bulk Harvest Run Log**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_bulkharvestrunlog_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
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

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
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

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
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
|Description|**Yomi name of the owner**|
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
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_msdyn_bulkharvestrunlog](#BKMK_business_unit_msdyn_bulkharvestrunlog)
- [lk_msdyn_bulkharvestrunlog_createdby](#BKMK_lk_msdyn_bulkharvestrunlog_createdby)
- [lk_msdyn_bulkharvestrunlog_createdonbehalfby](#BKMK_lk_msdyn_bulkharvestrunlog_createdonbehalfby)
- [lk_msdyn_bulkharvestrunlog_modifiedby](#BKMK_lk_msdyn_bulkharvestrunlog_modifiedby)
- [lk_msdyn_bulkharvestrunlog_modifiedonbehalfby](#BKMK_lk_msdyn_bulkharvestrunlog_modifiedonbehalfby)
- [msdyn_bulkharvestrunlog_knowledgearticle](#BKMK_msdyn_bulkharvestrunlog_knowledgearticle)
- [owner_msdyn_bulkharvestrunlog](#BKMK_owner_msdyn_bulkharvestrunlog)
- [team_msdyn_bulkharvestrunlog](#BKMK_team_msdyn_bulkharvestrunlog)
- [user_msdyn_bulkharvestrunlog](#BKMK_user_msdyn_bulkharvestrunlog)

### <a name="BKMK_business_unit_msdyn_bulkharvestrunlog"></a> business_unit_msdyn_bulkharvestrunlog

One-To-Many Relationship: [businessunit business_unit_msdyn_bulkharvestrunlog](businessunit.md#BKMK_business_unit_msdyn_bulkharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_bulkharvestrunlog_createdby"></a> lk_msdyn_bulkharvestrunlog_createdby

One-To-Many Relationship: [systemuser lk_msdyn_bulkharvestrunlog_createdby](systemuser.md#BKMK_lk_msdyn_bulkharvestrunlog_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_bulkharvestrunlog_createdonbehalfby"></a> lk_msdyn_bulkharvestrunlog_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_bulkharvestrunlog_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_bulkharvestrunlog_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_bulkharvestrunlog_modifiedby"></a> lk_msdyn_bulkharvestrunlog_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_bulkharvestrunlog_modifiedby](systemuser.md#BKMK_lk_msdyn_bulkharvestrunlog_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_bulkharvestrunlog_modifiedonbehalfby"></a> lk_msdyn_bulkharvestrunlog_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_bulkharvestrunlog_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_bulkharvestrunlog_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_bulkharvestrunlog_knowledgearticle"></a> msdyn_bulkharvestrunlog_knowledgearticle

One-To-Many Relationship: [knowledgearticle msdyn_bulkharvestrunlog_knowledgearticle](knowledgearticle.md#BKMK_msdyn_bulkharvestrunlog_knowledgearticle)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`msdyn_knowledgearticleid`|
|ReferencingEntityNavigationPropertyName|`msdyn_knowledgearticleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_bulkharvestrunlog"></a> owner_msdyn_bulkharvestrunlog

One-To-Many Relationship: [owner owner_msdyn_bulkharvestrunlog](owner.md#BKMK_owner_msdyn_bulkharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_bulkharvestrunlog"></a> team_msdyn_bulkharvestrunlog

One-To-Many Relationship: [team team_msdyn_bulkharvestrunlog](team.md#BKMK_team_msdyn_bulkharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_bulkharvestrunlog"></a> user_msdyn_bulkharvestrunlog

One-To-Many Relationship: [systemuser user_msdyn_bulkharvestrunlog](systemuser.md#BKMK_user_msdyn_bulkharvestrunlog)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_bulkharvestrunlog_AsyncOperations](#BKMK_msdyn_bulkharvestrunlog_AsyncOperations)
- [msdyn_bulkharvestrunlog_BulkDeleteFailures](#BKMK_msdyn_bulkharvestrunlog_BulkDeleteFailures)
- [msdyn_bulkharvestrunlog_DeletedItemReferences](#BKMK_msdyn_bulkharvestrunlog_DeletedItemReferences)
- [msdyn_bulkharvestrunlog_MailboxTrackingFolders](#BKMK_msdyn_bulkharvestrunlog_MailboxTrackingFolders)
- [msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses](#BKMK_msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses)
- [msdyn_bulkharvestrunlog_ProcessSession](#BKMK_msdyn_bulkharvestrunlog_ProcessSession)
- [msdyn_bulkharvestrunlog_SyncErrors](#BKMK_msdyn_bulkharvestrunlog_SyncErrors)

### <a name="BKMK_msdyn_bulkharvestrunlog_AsyncOperations"></a> msdyn_bulkharvestrunlog_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_bulkharvestrunlog_AsyncOperations](asyncoperation.md#BKMK_msdyn_bulkharvestrunlog_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_bulkharvestrunlog_BulkDeleteFailures"></a> msdyn_bulkharvestrunlog_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_bulkharvestrunlog_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_bulkharvestrunlog_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_bulkharvestrunlog_DeletedItemReferences"></a> msdyn_bulkharvestrunlog_DeletedItemReferences

Many-To-One Relationship: [deleteditemreference msdyn_bulkharvestrunlog_DeletedItemReferences](deleteditemreference.md#BKMK_msdyn_bulkharvestrunlog_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencingEntity|`deleteditemreference`|
|ReferencingAttribute|`deletedobject`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_DeletedItemReferences`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_bulkharvestrunlog_MailboxTrackingFolders"></a> msdyn_bulkharvestrunlog_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_bulkharvestrunlog_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_bulkharvestrunlog_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses"></a> msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_bulkharvestrunlog_ProcessSession"></a> msdyn_bulkharvestrunlog_ProcessSession

Many-To-One Relationship: [processsession msdyn_bulkharvestrunlog_ProcessSession](processsession.md#BKMK_msdyn_bulkharvestrunlog_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_bulkharvestrunlog_SyncErrors"></a> msdyn_bulkharvestrunlog_SyncErrors

Many-To-One Relationship: [syncerror msdyn_bulkharvestrunlog_SyncErrors](syncerror.md#BKMK_msdyn_bulkharvestrunlog_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_bulkharvestrunlog_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_bulkharvestrunlog?displayProperty=fullName>
