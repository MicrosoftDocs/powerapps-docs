---
title: "Content Snippet (mspp_contentsnippet) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Content Snippet (mspp_contentsnippet) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Content Snippet (mspp_contentsnippet) table/entity reference (Microsoft Dataverse)

Content snippets are inserted in page templates so that any label, text string or image in the template can be content-managed.

## Messages

The following table lists the messages for the Content Snippet (mspp_contentsnippet) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_contentsnippets<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_contentsnippets<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_contentsnippets(*mspp_contentsnippetid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Content Snippet (mspp_contentsnippet) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Content Snippet (mspp_contentsnippet) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Content Snippet** |
| **DisplayCollectionName** | **Content Snippets** |
| **SchemaName** | `mspp_contentsnippet` |
| **CollectionSchemaName** | `mspp_contentsnippets` |
| **EntitySetName** | `mspp_contentsnippets`|
| **LogicalName** | `mspp_contentsnippet` |
| **LogicalCollectionName** | `mspp_contentsnippets` |
| **PrimaryIdAttribute** | `mspp_contentsnippetid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_contentsnippetId](#BKMK_mspp_contentsnippetId)
- [mspp_contentsnippetlanguageid](#BKMK_mspp_contentsnippetlanguageid)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_display_name](#BKMK_mspp_display_name)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_type](#BKMK_mspp_type)
- [mspp_value](#BKMK_mspp_value)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_contentsnippetId"></a> mspp_contentsnippetId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Content Snippet**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_contentsnippetid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_contentsnippetlanguageid"></a> mspp_contentsnippetlanguageid

|Property|Value|
|---|---|
|Description|**Option to make content snippets language specific**|
|DisplayName|**Content Snippet Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_contentsnippetlanguageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_websitelanguage|

### <a name="BKMK_mspp_createdby"></a> mspp_createdby

|Property|Value|
|---|---|
|Description|**Shows who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_createdbyipaddress"></a> mspp_createdbyipaddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**Created By IP Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdbyipaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_createdbyusername"></a> mspp_createdbyusername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Created By Username**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdbyusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_createdon"></a> mspp_createdon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_display_name"></a> mspp_display_name

|Property|Value|
|---|---|
|Description|**Stores the label that is shown on the user interface (UI) in the data editing mode.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_display_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_mspp_modifiedby"></a> mspp_modifiedby

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_mspp_modifiedbyipaddress"></a> mspp_modifiedbyipaddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**Modified By IP Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedbyipaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_modifiedbyusername"></a> mspp_modifiedbyusername

|Property|Value|
|---|---|
|Description||
|DisplayName|**Modified By Username**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedbyusername`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_modifiedon"></a> mspp_modifiedon

|Property|Value|
|---|---|
|Description|**Shows the date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_mspp_name"></a> mspp_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_type"></a> mspp_type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_type`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_contentsnippet_mspp_type`|

#### mspp_type Choices/Options

|Value|Label|
|---|---|
|756150000|**Text**|
|756150001|**HTML**|

### <a name="BKMK_mspp_value"></a> mspp_value

|Property|Value|
|---|---|
|Description||
|DisplayName|**Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_value`|
|RequiredLevel|Recommended|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Content Snippet.**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Content Snippet**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_contentsnippet_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Content Snippet**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_contentsnippet_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_systemuser_mspp_contentsnippet_createdby](#BKMK_mspp_systemuser_mspp_contentsnippet_createdby)
- [mspp_systemuser_mspp_contentsnippet_modifiedby](#BKMK_mspp_systemuser_mspp_contentsnippet_modifiedby)
- [mspp_website_contentsnippet](#BKMK_mspp_website_contentsnippet)
- [mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid)

### <a name="BKMK_mspp_systemuser_mspp_contentsnippet_createdby"></a> mspp_systemuser_mspp_contentsnippet_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_contentsnippet_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_contentsnippet_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_contentsnippet_modifiedby"></a> mspp_systemuser_mspp_contentsnippet_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_contentsnippet_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_contentsnippet_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_contentsnippet"></a> mspp_website_contentsnippet

One-To-Many Relationship: [mspp_website mspp_website_contentsnippet](mspp_website.md#BKMK_mspp_website_contentsnippet)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid"></a> mspp_websitelanguage_contentsnippet_contentsnippetlanguageid

One-To-Many Relationship: [mspp_websitelanguage mspp_websitelanguage_contentsnippet_contentsnippetlanguageid](mspp_websitelanguage.md#BKMK_mspp_websitelanguage_contentsnippet_contentsnippetlanguageid)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_websitelanguage`|
|ReferencedAttribute|`mspp_websitelanguageid`|
|ReferencingAttribute|`mspp_contentsnippetlanguageid`|
|ReferencingEntityNavigationPropertyName|`mspp_contentsnippetlanguageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_contentsnippet?displayProperty=fullName>
