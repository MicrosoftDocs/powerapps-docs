---
title: "Power Pages Site AI Feedback (PowerPagesSiteAIFeedback) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Power Pages Site AI Feedback (PowerPagesSiteAIFeedback) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Power Pages Site AI Feedback (PowerPagesSiteAIFeedback) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Power Pages Site AI Feedback (PowerPagesSiteAIFeedback) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /powerpagessiteaifeedbacks(*powerpagessiteaifeedbackid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /powerpagessiteaifeedbacks<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /powerpagessiteaifeedbacks(*powerpagessiteaifeedbackid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /powerpagessiteaifeedbacks(*powerpagessiteaifeedbackid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /powerpagessiteaifeedbacks<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `Update`<br />Event: True |`PATCH` /powerpagessiteaifeedbacks(*powerpagessiteaifeedbackid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /powerpagessiteaifeedbacks(*powerpagessiteaifeedbackid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Power Pages Site AI Feedback (PowerPagesSiteAIFeedback) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Power Pages Site AI Feedback (PowerPagesSiteAIFeedback) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Power Pages Site AI Feedback** |
| **DisplayCollectionName** | **Power Pages Site AI Feedbacks** |
| **SchemaName** | `PowerPagesSiteAIFeedback` |
| **CollectionSchemaName** | `PowerPagesSiteAIFeedbacks` |
| **EntitySetName** | `powerpagessiteaifeedbacks`|
| **LogicalName** | `powerpagessiteaifeedback` |
| **LogicalCollectionName** | `powerpagessiteaifeedbacks` |
| **PrimaryIdAttribute** | `powerpagessiteaifeedbackid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Contact](#BKMK_Contact)
- [Feedback](#BKMK_Feedback)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [Origin](#BKMK_Origin)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PartitionId](#BKMK_PartitionId)
- [PowerPagesSiteAIFeedbackId](#BKMK_PowerPagesSiteAIFeedbackId)
- [PowerPagesSiteAIFeedbackName](#BKMK_PowerPagesSiteAIFeedbackName)
- [Reason](#BKMK_Reason)
- [Response](#BKMK_Response)
- [TTLInSeconds](#BKMK_TTLInSeconds)
- [UserPrompt](#BKMK_UserPrompt)
- [WebsiteDomain](#BKMK_WebsiteDomain)
- [WebsiteId](#BKMK_WebsiteId)

### <a name="BKMK_Contact"></a> Contact

|Property|Value|
|---|---|
|Description||
|DisplayName|**Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`contact`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|contact|

### <a name="BKMK_Feedback"></a> Feedback

|Property|Value|
|---|---|
|Description||
|DisplayName|**Feedback**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`feedback`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`powerpagessiteaifeedback_feedback`|

#### Feedback Choices/Options

|Value|Label|
|---|---|
|195620000|**Up**|
|195620001|**Down**|

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

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Origin"></a> Origin

|Property|Value|
|---|---|
|Description||
|DisplayName|**Origin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`origin`|
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

### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|---|---|
|Description|**Logical partition id. A logical partition consists of a set of records with same partition id.**|
|DisplayName|**Partition Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_PowerPagesSiteAIFeedbackId"></a> PowerPagesSiteAIFeedbackId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Power Pages Site AI Feedback**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`powerpagessiteaifeedbackid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_PowerPagesSiteAIFeedbackName"></a> PowerPagesSiteAIFeedbackName

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Power Pages Site AI Feedback**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`powerpagessiteaifeedbackname`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Reason"></a> Reason

|Property|Value|
|---|---|
|Description|**Reason for down**|
|DisplayName|**Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`reason`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_Response"></a> Response

|Property|Value|
|---|---|
|Description||
|DisplayName|**Response**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`response`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|---|---|
|Description|**Time to live in seconds.**|
|DisplayName|**Time to live**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ttlinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_UserPrompt"></a> UserPrompt

|Property|Value|
|---|---|
|Description||
|DisplayName|**User Prompt**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`userprompt`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_WebsiteDomain"></a> WebsiteDomain

|Property|Value|
|---|---|
|Description||
|DisplayName|**Website Domain**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`websitedomain`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_WebsiteId"></a> WebsiteId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Website Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`websiteid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


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

- [business_unit_powerpagessiteaifeedback](#BKMK_business_unit_powerpagessiteaifeedback)
- [lk_powerpagessiteaifeedback_createdby](#BKMK_lk_powerpagessiteaifeedback_createdby)
- [lk_powerpagessiteaifeedback_createdonbehalfby](#BKMK_lk_powerpagessiteaifeedback_createdonbehalfby)
- [lk_powerpagessiteaifeedback_modifiedby](#BKMK_lk_powerpagessiteaifeedback_modifiedby)
- [lk_powerpagessiteaifeedback_modifiedonbehalfby](#BKMK_lk_powerpagessiteaifeedback_modifiedonbehalfby)
- [owner_powerpagessiteaifeedback](#BKMK_owner_powerpagessiteaifeedback)
- [PowerPagesSiteAIFeedback_Contact_Contact](#BKMK_PowerPagesSiteAIFeedback_Contact_Contact)
- [team_powerpagessiteaifeedback](#BKMK_team_powerpagessiteaifeedback)
- [user_powerpagessiteaifeedback](#BKMK_user_powerpagessiteaifeedback)

### <a name="BKMK_business_unit_powerpagessiteaifeedback"></a> business_unit_powerpagessiteaifeedback

One-To-Many Relationship: [businessunit business_unit_powerpagessiteaifeedback](businessunit.md#BKMK_business_unit_powerpagessiteaifeedback)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagessiteaifeedback_createdby"></a> lk_powerpagessiteaifeedback_createdby

One-To-Many Relationship: [systemuser lk_powerpagessiteaifeedback_createdby](systemuser.md#BKMK_lk_powerpagessiteaifeedback_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagessiteaifeedback_createdonbehalfby"></a> lk_powerpagessiteaifeedback_createdonbehalfby

One-To-Many Relationship: [systemuser lk_powerpagessiteaifeedback_createdonbehalfby](systemuser.md#BKMK_lk_powerpagessiteaifeedback_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagessiteaifeedback_modifiedby"></a> lk_powerpagessiteaifeedback_modifiedby

One-To-Many Relationship: [systemuser lk_powerpagessiteaifeedback_modifiedby](systemuser.md#BKMK_lk_powerpagessiteaifeedback_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_powerpagessiteaifeedback_modifiedonbehalfby"></a> lk_powerpagessiteaifeedback_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_powerpagessiteaifeedback_modifiedonbehalfby](systemuser.md#BKMK_lk_powerpagessiteaifeedback_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_powerpagessiteaifeedback"></a> owner_powerpagessiteaifeedback

One-To-Many Relationship: [owner owner_powerpagessiteaifeedback](owner.md#BKMK_owner_powerpagessiteaifeedback)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_PowerPagesSiteAIFeedback_Contact_Contact"></a> PowerPagesSiteAIFeedback_Contact_Contact

One-To-Many Relationship: [contact PowerPagesSiteAIFeedback_Contact_Contact](contact.md#BKMK_PowerPagesSiteAIFeedback_Contact_Contact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`contact`|
|ReferencingEntityNavigationPropertyName|`Contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_powerpagessiteaifeedback"></a> team_powerpagessiteaifeedback

One-To-Many Relationship: [team team_powerpagessiteaifeedback](team.md#BKMK_team_powerpagessiteaifeedback)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_powerpagessiteaifeedback"></a> user_powerpagessiteaifeedback

One-To-Many Relationship: [systemuser user_powerpagessiteaifeedback](systemuser.md#BKMK_user_powerpagessiteaifeedback)

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
<xref:Microsoft.Dynamics.CRM.powerpagessiteaifeedback?displayProperty=fullName>
