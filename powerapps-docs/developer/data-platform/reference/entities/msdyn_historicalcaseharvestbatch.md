---
title: "msdyn_historicalcaseharvestbatch table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the msdyn_historicalcaseharvestbatch table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# msdyn_historicalcaseharvestbatch table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the msdyn_historicalcaseharvestbatch table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestbatches(*msdyn_historicalcaseharvestbatchid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_historicalcaseharvestbatches<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_historicalcaseharvestbatches(*msdyn_historicalcaseharvestbatchid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_historicalcaseharvestbatches(*msdyn_historicalcaseharvestbatchid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_historicalcaseharvestbatches<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestbatches(*msdyn_historicalcaseharvestbatchid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_historicalcaseharvestbatches(*msdyn_historicalcaseharvestbatchid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_historicalcaseharvestbatches(*msdyn_historicalcaseharvestbatchid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the msdyn_historicalcaseharvestbatch table.

|Property|Value|
| --- | --- |
| **DisplayName** | **msdyn_historicalcaseharvestbatch** |
| **DisplayCollectionName** | **msdyn_historicalcaseharvestbatches** |
| **SchemaName** | `msdyn_historicalcaseharvestbatch` |
| **CollectionSchemaName** | `msdyn_historicalcaseharvestbatchs` |
| **EntitySetName** | `msdyn_historicalcaseharvestbatches`|
| **LogicalName** | `msdyn_historicalcaseharvestbatch` |
| **LogicalCollectionName** | `msdyn_historicalcaseharvestbatchs` |
| **PrimaryIdAttribute** | `msdyn_historicalcaseharvestbatchid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_articlescreated](#BKMK_msdyn_articlescreated)
- [msdyn_batchprocessingcompletedon](#BKMK_msdyn_batchprocessingcompletedon)
- [msdyn_batchsize](#BKMK_msdyn_batchsize)
- [msdyn_casesskipped](#BKMK_msdyn_casesskipped)
- [msdyn_historicalcaseharvestbatchId](#BKMK_msdyn_historicalcaseharvestbatchId)
- [msdyn_historicalcaseharvestrunid](#BKMK_msdyn_historicalcaseharvestrunid)
- [msdyn_incidentids](#BKMK_msdyn_incidentids)
- [msdyn_name](#BKMK_msdyn_name)
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

### <a name="BKMK_msdyn_articlescreated"></a> msdyn_articlescreated

|Property|Value|
|---|---|
|Description||
|DisplayName|**Articles Created**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_articlescreated`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_batchprocessingcompletedon"></a> msdyn_batchprocessingcompletedon

|Property|Value|
|---|---|
|Description|**Timestamp when the batch was completed.**|
|DisplayName|**Batch Processing Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_batchprocessingcompletedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_batchsize"></a> msdyn_batchsize

|Property|Value|
|---|---|
|Description||
|DisplayName|**Batch Size**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_batchsize`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_casesskipped"></a> msdyn_casesskipped

|Property|Value|
|---|---|
|Description||
|DisplayName|**Cases Skipped**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_casesskipped`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_historicalcaseharvestbatchId"></a> msdyn_historicalcaseharvestbatchId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**msdyn\_historicalcaseharvestbatch**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_historicalcaseharvestbatchid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_historicalcaseharvestrunid"></a> msdyn_historicalcaseharvestrunid

|Property|Value|
|---|---|
|Description|**Unique Identifier of the run record the batch is linked to**|
|DisplayName|**Historical Case Harvest Run ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_historicalcaseharvestrunid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|msdyn_historicalcaseharvestrun|

### <a name="BKMK_msdyn_incidentids"></a> msdyn_incidentids

|Property|Value|
|---|---|
|Description||
|DisplayName|**Incident IDs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_incidentids`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|850|

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
|Description|**Status of the msdyn\_historicalcaseharvestbatch**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_historicalcaseharvestbatch_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Created**<br />DefaultStatus: 1<br />InvariantName: `Created`|
|1|Label: **Completed**<br />DefaultStatus: 2<br />InvariantName: `Completed`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the msdyn\_historicalcaseharvestbatch**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_historicalcaseharvestbatch_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Success**<br />State:1<br />TransitionData: None|
|3|Label: **Failed**<br />State:1<br />TransitionData: None|

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

- [business_unit_msdyn_historicalcaseharvestbatch](#BKMK_business_unit_msdyn_historicalcaseharvestbatch)
- [lk_msdyn_historicalcaseharvestbatch_createdby](#BKMK_lk_msdyn_historicalcaseharvestbatch_createdby)
- [lk_msdyn_historicalcaseharvestbatch_createdonbehalfby](#BKMK_lk_msdyn_historicalcaseharvestbatch_createdonbehalfby)
- [lk_msdyn_historicalcaseharvestbatch_modifiedby](#BKMK_lk_msdyn_historicalcaseharvestbatch_modifiedby)
- [lk_msdyn_historicalcaseharvestbatch_modifiedonbehalfby](#BKMK_lk_msdyn_historicalcaseharvestbatch_modifiedonbehalfby)
- [msdyn_historicalcaseharvestbatch_historicalcaseharvestrun](#BKMK_msdyn_historicalcaseharvestbatch_historicalcaseharvestrun)
- [owner_msdyn_historicalcaseharvestbatch](#BKMK_owner_msdyn_historicalcaseharvestbatch)
- [team_msdyn_historicalcaseharvestbatch](#BKMK_team_msdyn_historicalcaseharvestbatch)
- [user_msdyn_historicalcaseharvestbatch](#BKMK_user_msdyn_historicalcaseharvestbatch)

### <a name="BKMK_business_unit_msdyn_historicalcaseharvestbatch"></a> business_unit_msdyn_historicalcaseharvestbatch

One-To-Many Relationship: [businessunit business_unit_msdyn_historicalcaseharvestbatch](businessunit.md#BKMK_business_unit_msdyn_historicalcaseharvestbatch)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestbatch_createdby"></a> lk_msdyn_historicalcaseharvestbatch_createdby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestbatch_createdby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestbatch_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestbatch_createdonbehalfby"></a> lk_msdyn_historicalcaseharvestbatch_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestbatch_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestbatch_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestbatch_modifiedby"></a> lk_msdyn_historicalcaseharvestbatch_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestbatch_modifiedby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestbatch_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_historicalcaseharvestbatch_modifiedonbehalfby"></a> lk_msdyn_historicalcaseharvestbatch_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_historicalcaseharvestbatch_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_historicalcaseharvestbatch_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_historicalcaseharvestrun"></a> msdyn_historicalcaseharvestbatch_historicalcaseharvestrun

One-To-Many Relationship: [msdyn_historicalcaseharvestrun msdyn_historicalcaseharvestbatch_historicalcaseharvestrun](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_historicalcaseharvestbatch_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_historicalcaseharvestrun`|
|ReferencedAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingAttribute|`msdyn_historicalcaseharvestrunid`|
|ReferencingEntityNavigationPropertyName|`msdyn_historicalcaseharvestrunid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_historicalcaseharvestbatch"></a> owner_msdyn_historicalcaseharvestbatch

One-To-Many Relationship: [owner owner_msdyn_historicalcaseharvestbatch](owner.md#BKMK_owner_msdyn_historicalcaseharvestbatch)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_historicalcaseharvestbatch"></a> team_msdyn_historicalcaseharvestbatch

One-To-Many Relationship: [team team_msdyn_historicalcaseharvestbatch](team.md#BKMK_team_msdyn_historicalcaseharvestbatch)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_historicalcaseharvestbatch"></a> user_msdyn_historicalcaseharvestbatch

One-To-Many Relationship: [systemuser user_msdyn_historicalcaseharvestbatch](systemuser.md#BKMK_user_msdyn_historicalcaseharvestbatch)

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

- [msdyn_historicalcaseharvestbatch_AsyncOperations](#BKMK_msdyn_historicalcaseharvestbatch_AsyncOperations)
- [msdyn_historicalcaseharvestbatch_BulkDeleteFailures](#BKMK_msdyn_historicalcaseharvestbatch_BulkDeleteFailures)
- [msdyn_historicalcaseharvestbatch_MailboxTrackingFolders](#BKMK_msdyn_historicalcaseharvestbatch_MailboxTrackingFolders)
- [msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses](#BKMK_msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses)
- [msdyn_historicalcaseharvestbatch_ProcessSession](#BKMK_msdyn_historicalcaseharvestbatch_ProcessSession)
- [msdyn_historicalcaseharvestbatch_SyncErrors](#BKMK_msdyn_historicalcaseharvestbatch_SyncErrors)

### <a name="BKMK_msdyn_historicalcaseharvestbatch_AsyncOperations"></a> msdyn_historicalcaseharvestbatch_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_historicalcaseharvestbatch_AsyncOperations](asyncoperation.md#BKMK_msdyn_historicalcaseharvestbatch_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_BulkDeleteFailures"></a> msdyn_historicalcaseharvestbatch_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_historicalcaseharvestbatch_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_historicalcaseharvestbatch_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_MailboxTrackingFolders"></a> msdyn_historicalcaseharvestbatch_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_historicalcaseharvestbatch_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_historicalcaseharvestbatch_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses"></a> msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_ProcessSession"></a> msdyn_historicalcaseharvestbatch_ProcessSession

Many-To-One Relationship: [processsession msdyn_historicalcaseharvestbatch_ProcessSession](processsession.md#BKMK_msdyn_historicalcaseharvestbatch_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_historicalcaseharvestbatch_SyncErrors"></a> msdyn_historicalcaseharvestbatch_SyncErrors

Many-To-One Relationship: [syncerror msdyn_historicalcaseharvestbatch_SyncErrors](syncerror.md#BKMK_msdyn_historicalcaseharvestbatch_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_historicalcaseharvestbatch_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_historicalcaseharvestbatch?displayProperty=fullName>
