---
title: "Knowledge Harvest Plan (msdyn_knowledgeharvestplan) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Knowledge Harvest Plan (msdyn_knowledgeharvestplan) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Knowledge Harvest Plan (msdyn_knowledgeharvestplan) table/entity reference (Microsoft Dataverse)

Stores configuration settings for knowledge harvesting per source entity.

## Messages

The following table lists the messages for the Knowledge Harvest Plan (msdyn_knowledgeharvestplan) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_knowledgeharvestplans(*msdyn_knowledgeharvestplanid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_knowledgeharvestplans<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_knowledgeharvestplans(*msdyn_knowledgeharvestplanid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_knowledgeharvestplans(*msdyn_knowledgeharvestplanid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_knowledgeharvestplans<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_knowledgeharvestplans(*msdyn_knowledgeharvestplanid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_knowledgeharvestplans(*msdyn_knowledgeharvestplanid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_knowledgeharvestplans(*msdyn_knowledgeharvestplanid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Knowledge Harvest Plan (msdyn_knowledgeharvestplan) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Knowledge Harvest Plan (msdyn_knowledgeharvestplan) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Knowledge Harvest Plan** |
| **DisplayCollectionName** | **Knowledge Harvest Plans** |
| **SchemaName** | `msdyn_knowledgeharvestplan` |
| **CollectionSchemaName** | `msdyn_knowledgeharvestplans` |
| **EntitySetName** | `msdyn_knowledgeharvestplans`|
| **LogicalName** | `msdyn_knowledgeharvestplan` |
| **LogicalCollectionName** | `msdyn_knowledgeharvestplans` |
| **PrimaryIdAttribute** | `msdyn_knowledgeharvestplanid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_additionaldetails](#BKMK_msdyn_additionaldetails)
- [msdyn_backfillfromoption](#BKMK_msdyn_backfillfromoption)
- [msdyn_conditions](#BKMK_msdyn_conditions)
- [msdyn_fieldmappings](#BKMK_msdyn_fieldmappings)
- [msdyn_frequencytype](#BKMK_msdyn_frequencytype)
- [msdyn_harvesteligibilityconditionid](#BKMK_msdyn_harvesteligibilityconditionid)
- [msdyn_harvestingdatatype](#BKMK_msdyn_harvestingdatatype)
- [msdyn_harvestsourceentity](#BKMK_msdyn_harvestsourceentity)
- [msdyn_harvesttype](#BKMK_msdyn_harvesttype)
- [msdyn_isautopublishenabled](#BKMK_msdyn_isautopublishenabled)
- [msdyn_isinternal](#BKMK_msdyn_isinternal)
- [msdyn_isupdatekbarticleenabled](#BKMK_msdyn_isupdatekbarticleenabled)
- [msdyn_keeprunningoption](#BKMK_msdyn_keeprunningoption)
- [msdyn_knowledgearticletemplateid](#BKMK_msdyn_knowledgearticletemplateid)
- [msdyn_knowledgeharvestplanId](#BKMK_msdyn_knowledgeharvestplanId)
- [msdyn_lastruntime](#BKMK_msdyn_lastruntime)
- [msdyn_localizationlanguagecode](#BKMK_msdyn_localizationlanguagecode)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_nextruntime](#BKMK_msdyn_nextruntime)
- [msdyn_priorityorder](#BKMK_msdyn_priorityorder)
- [msdyn_recurringtype](#BKMK_msdyn_recurringtype)
- [msdyn_versioning](#BKMK_msdyn_versioning)
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

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_msdyn_additionaldetails"></a> msdyn_additionaldetails

|Property|Value|
|---|---|
|Description||
|DisplayName|**Additional details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_additionaldetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_backfillfromoption"></a> msdyn_backfillfromoption

|Property|Value|
|---|---|
|Description|**Time range for backfilling records when the harvest plan starts.**|
|DisplayName|**Backfill From Option**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_backfillfromoption`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|100000100|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_backfillfromoption`|

#### msdyn_backfillfromoption Choices/Options

|Value|Label|
|---|---|
|100000100|**All available records**|
|100000200|**Last 30 days**|
|100000300|**Last 60 days**|
|100000400|**Last 3 months**|
|100000500|**Last 6 months**|
|100000600|**No backfill**|

### <a name="BKMK_msdyn_conditions"></a> msdyn_conditions

|Property|Value|
|---|---|
|Description|**JSON-serialized KnowledgeHarvestConditionsSetting containing condition expressions and FetchXML filters.**|
|DisplayName|**Conditions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_conditions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_fieldmappings"></a> msdyn_fieldmappings

|Property|Value|
|---|---|
|Description|**JSON-serialized field mapping configuration that maps source entity fields to knowledge article fields.**|
|DisplayName|**Field Mappings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_fieldmappings`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_frequencytype"></a> msdyn_frequencytype

|Property|Value|
|---|---|
|Description|**Defines the schedule type for harvesting: Realtime, Once, or Recurring.**|
|DisplayName|**Frequency Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_frequencytype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_frequencytype`|

#### msdyn_frequencytype Choices/Options

|Value|Label|
|---|---|
|0|**Realtime**|
|1|**Once**|
|2|**Recurring**|

### <a name="BKMK_msdyn_harvesteligibilityconditionid"></a> msdyn_harvesteligibilityconditionid

|Property|Value|
|---|---|
|Description|**Reference to the harvest eligibility condition for this plan.**|
|DisplayName|**Harvest Eligibility Condition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvesteligibilityconditionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_harvestingdatatype"></a> msdyn_harvestingdatatype

|Property|Value|
|---|---|
|Description|**Indicates what type of entity this harvest plan is harvesting from**|
|DisplayName|**harvestingdatatype**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestingdatatype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_harvestingdatatype`|

#### msdyn_harvestingdatatype Choices/Options

|Value|Label|
|---|---|
|0|**Case**|
|1|**Conversation**|
|2|**Custom Entity**|

### <a name="BKMK_msdyn_harvestsourceentity"></a> msdyn_harvestsourceentity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Knowledge Harvest Source Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvestsourceentity`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_harvesttype"></a> msdyn_harvesttype

|Property|Value|
|---|---|
|Description|**Defines the schedule types for harvesting. Multiple values can be combined (for example Realtime \+ Once, or Recurring \+ Once).**|
|DisplayName|**Harvest Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_harvesttype`|
|RequiredLevel|ApplicationRequired|
|Type|MultiSelectPicklist|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_harvesttype`|

#### msdyn_harvesttype Choices/Options

|Value|Label|
|---|---|
|0|**Realtime**|
|1|**Once**|
|2|**Recurring**|

### <a name="BKMK_msdyn_isautopublishenabled"></a> msdyn_isautopublishenabled

|Property|Value|
|---|---|
|Description|**Indicates whether harvested articles are automatically published without manual review.**|
|DisplayName|**Is Auto Publish Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isautopublishenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_isautopublishenabled`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_msdyn_isinternal"></a> msdyn_isinternal

|Property|Value|
|---|---|
|Description|**Indicates whether harvested articles are marked as internal.**|
|DisplayName|**Is Internal**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isinternal`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_isinternal`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_msdyn_isupdatekbarticleenabled"></a> msdyn_isupdatekbarticleenabled

|Property|Value|
|---|---|
|Description|**Indicates whether existing knowledge articles can be updated (versioned) during harvesting.**|
|DisplayName|**Is Update KB Article Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isupdatekbarticleenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_isupdatekbarticleenabled`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_msdyn_keeprunningoption"></a> msdyn_keeprunningoption

|Property|Value|
|---|---|
|Description|**Ongoing execution behavior for the harvest plan.**|
|DisplayName|**Keep Running Option**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_keeprunningoption`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|100000100|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_keeprunningoption`|

#### msdyn_keeprunningoption Choices/Options

|Value|Label|
|---|---|
|100000100|**For every record (realtime)**|
|100000600|**Just once**|

### <a name="BKMK_msdyn_knowledgearticletemplateid"></a> msdyn_knowledgearticletemplateid

|Property|Value|
|---|---|
|Description|**Reference to the knowledge article template used for harvesting.**|
|DisplayName|**Knowledge Article Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgearticletemplateid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_knowledgeharvestplanId"></a> msdyn_knowledgeharvestplanId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Knowledge Harvest Plan Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_knowledgeharvestplanid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_lastruntime"></a> msdyn_lastruntime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Last Run Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lastruntime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_localizationlanguagecode"></a> msdyn_localizationlanguagecode

|Property|Value|
|---|---|
|Description|**language code used for harvested knowledge articles (e.g. en-US).**|
|DisplayName|**Localization Language Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_localizationlanguagecode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**Name of the harvest plan.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_nextruntime"></a> msdyn_nextruntime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Next Run Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_nextruntime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_priorityorder"></a> msdyn_priorityorder

|Property|Value|
|---|---|
|Description||
|DisplayName|**Priority Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_priorityorder`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_recurringtype"></a> msdyn_recurringtype

|Property|Value|
|---|---|
|Description|**Defines the recurring schedule pattern: Daily, Weekly, Bi-weekly, or Monthly.**|
|DisplayName|**Recurring Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_recurringtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_knowledgeharvestplan_msdyn_recurringtype`|

#### msdyn_recurringtype Choices/Options

|Value|Label|
|---|---|
|0|**Daily**|
|1|**Weekly**|
|2|**Bi-weekly**|
|3|**Monthly**|
|100000100|**Hourly**|
|100000200|**Daily**|
|100000300|**Weekly**|
|100000400|**Bi-weekly**|

### <a name="BKMK_msdyn_versioning"></a> msdyn_versioning

|Property|Value|
|---|---|
|Description|**Version identifier for tracking customer edits to this harvest plan.**|
|DisplayName|**Versioning**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_versioning`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

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
|Format|DateAndTime|
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
|Description||
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgeharvestplan_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **InProgress**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|
|2|Label: **Paused**<br />DefaultStatus: 3<br />InvariantName: `Paused`|
|3|Label: **Completed**<br />DefaultStatus: 5<br />InvariantName: `Stopped`|
|4|Label: **Completed**<br />DefaultStatus: 6<br />InvariantName: `Completed`|
|5|Label: **Failed**<br />DefaultStatus: 7<br />InvariantName: `Failed`|
|6|Label: **Draft**<br />DefaultStatus: 8<br />InvariantName: `Draft`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_knowledgeharvestplan_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Draft**<br />State:0<br />TransitionData: None|
|2|Label: **InProgress**<br />State:1<br />TransitionData: None|
|3|Label: **Paused**<br />State:2<br />TransitionData: None|
|4|Label: **Completed**<br />State:2<br />TransitionData: None|
|5|Label: **Stopped**<br />State:3<br />TransitionData: None|
|6|Label: **Completed**<br />State:4<br />TransitionData: None|
|7|Label: **Failed**<br />State:5<br />TransitionData: None|
|8|Label: **Draft**<br />State:6<br />TransitionData: None|

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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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
|Description|**Date and time when the record was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|RequiredLevel|None|
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

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [business_unit_msdyn_knowledgeharvestplan](#BKMK_business_unit_msdyn_knowledgeharvestplan)
- [lk_msdyn_knowledgeharvestplan_createdby](#BKMK_lk_msdyn_knowledgeharvestplan_createdby)
- [lk_msdyn_knowledgeharvestplan_createdonbehalfby](#BKMK_lk_msdyn_knowledgeharvestplan_createdonbehalfby)
- [lk_msdyn_knowledgeharvestplan_modifiedby](#BKMK_lk_msdyn_knowledgeharvestplan_modifiedby)
- [lk_msdyn_knowledgeharvestplan_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgeharvestplan_modifiedonbehalfby)
- [owner_msdyn_knowledgeharvestplan](#BKMK_owner_msdyn_knowledgeharvestplan)
- [team_msdyn_knowledgeharvestplan](#BKMK_team_msdyn_knowledgeharvestplan)
- [user_msdyn_knowledgeharvestplan](#BKMK_user_msdyn_knowledgeharvestplan)

### <a name="BKMK_business_unit_msdyn_knowledgeharvestplan"></a> business_unit_msdyn_knowledgeharvestplan

One-To-Many Relationship: [businessunit business_unit_msdyn_knowledgeharvestplan](businessunit.md#BKMK_business_unit_msdyn_knowledgeharvestplan)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgeharvestplan_createdby"></a> lk_msdyn_knowledgeharvestplan_createdby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgeharvestplan_createdby](systemuser.md#BKMK_lk_msdyn_knowledgeharvestplan_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgeharvestplan_createdonbehalfby"></a> lk_msdyn_knowledgeharvestplan_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgeharvestplan_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgeharvestplan_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgeharvestplan_modifiedby"></a> lk_msdyn_knowledgeharvestplan_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgeharvestplan_modifiedby](systemuser.md#BKMK_lk_msdyn_knowledgeharvestplan_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_knowledgeharvestplan_modifiedonbehalfby"></a> lk_msdyn_knowledgeharvestplan_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_knowledgeharvestplan_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgeharvestplan_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_knowledgeharvestplan"></a> owner_msdyn_knowledgeharvestplan

One-To-Many Relationship: [owner owner_msdyn_knowledgeharvestplan](owner.md#BKMK_owner_msdyn_knowledgeharvestplan)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_knowledgeharvestplan"></a> team_msdyn_knowledgeharvestplan

One-To-Many Relationship: [team team_msdyn_knowledgeharvestplan](team.md#BKMK_team_msdyn_knowledgeharvestplan)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_knowledgeharvestplan"></a> user_msdyn_knowledgeharvestplan

One-To-Many Relationship: [systemuser user_msdyn_knowledgeharvestplan](systemuser.md#BKMK_user_msdyn_knowledgeharvestplan)

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

- [msdyn_knowledgeharvestplan_AsyncOperations](#BKMK_msdyn_knowledgeharvestplan_AsyncOperations)
- [msdyn_knowledgeharvestplan_BulkDeleteFailures](#BKMK_msdyn_knowledgeharvestplan_BulkDeleteFailures)
- [msdyn_knowledgeharvestplan_historicalcaseharvestrun](#BKMK_msdyn_knowledgeharvestplan_historicalcaseharvestrun)
- [msdyn_knowledgeharvestplan_MailboxTrackingFolders](#BKMK_msdyn_knowledgeharvestplan_MailboxTrackingFolders)
- [msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgeharvestplan_ProcessSession](#BKMK_msdyn_knowledgeharvestplan_ProcessSession)
- [msdyn_knowledgeharvestplan_SyncErrors](#BKMK_msdyn_knowledgeharvestplan_SyncErrors)

### <a name="BKMK_msdyn_knowledgeharvestplan_AsyncOperations"></a> msdyn_knowledgeharvestplan_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_knowledgeharvestplan_AsyncOperations](asyncoperation.md#BKMK_msdyn_knowledgeharvestplan_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeharvestplan_BulkDeleteFailures"></a> msdyn_knowledgeharvestplan_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_knowledgeharvestplan_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_knowledgeharvestplan_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeharvestplan_historicalcaseharvestrun"></a> msdyn_knowledgeharvestplan_historicalcaseharvestrun

Many-To-One Relationship: [msdyn_historicalcaseharvestrun msdyn_knowledgeharvestplan_historicalcaseharvestrun](msdyn_historicalcaseharvestrun.md#BKMK_msdyn_knowledgeharvestplan_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_historicalcaseharvestrun`|
|ReferencingAttribute|`msdyn_knowledgeharvestplanid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_historicalcaseharvestrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeharvestplan_MailboxTrackingFolders"></a> msdyn_knowledgeharvestplan_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_knowledgeharvestplan_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_knowledgeharvestplan_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeharvestplan_ProcessSession"></a> msdyn_knowledgeharvestplan_ProcessSession

Many-To-One Relationship: [processsession msdyn_knowledgeharvestplan_ProcessSession](processsession.md#BKMK_msdyn_knowledgeharvestplan_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_knowledgeharvestplan_SyncErrors"></a> msdyn_knowledgeharvestplan_SyncErrors

Many-To-One Relationship: [syncerror msdyn_knowledgeharvestplan_SyncErrors](syncerror.md#BKMK_msdyn_knowledgeharvestplan_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_knowledgeharvestplan_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_knowledgeharvestplan?displayProperty=fullName>
