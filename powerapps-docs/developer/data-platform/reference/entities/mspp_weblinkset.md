---
title: "Web Link Set (mspp_weblinkset) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Web Link Set (mspp_weblinkset) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Web Link Set (mspp_weblinkset) table/entity reference (Microsoft Dataverse)

A grouping of web links.

## Messages

The following table lists the messages for the Web Link Set (mspp_weblinkset) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_weblinksets<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_weblinksets<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_weblinksets(*mspp_weblinksetid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Web Link Set (mspp_weblinkset) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Web Link Set (mspp_weblinkset) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Web Link Set** |
| **DisplayCollectionName** | **Web Link Sets** |
| **SchemaName** | `mspp_weblinkset` |
| **CollectionSchemaName** | `mspp_weblinksets` |
| **EntitySetName** | `mspp_weblinksets`|
| **LogicalName** | `mspp_weblinkset` |
| **LogicalCollectionName** | `mspp_weblinksets` |
| **PrimaryIdAttribute** | `mspp_weblinksetid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_copy](#BKMK_mspp_copy)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_display_name](#BKMK_mspp_display_name)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_title](#BKMK_mspp_title)
- [mspp_weblinksetId](#BKMK_mspp_weblinksetId)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_websitelanguageid](#BKMK_mspp_websitelanguageid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_copy"></a> mspp_copy

|Property|Value|
|---|---|
|Description||
|DisplayName|**Copy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_copy`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

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
|MaxLength|100|

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

### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Publishing State associated with Web Link Set.**|
|DisplayName|**Publishing State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_publishingstateid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_publishingstate|

### <a name="BKMK_mspp_title"></a> mspp_title

|Property|Value|
|---|---|
|Description||
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_title`|
|RequiredLevel|Recommended|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_mspp_weblinksetId"></a> mspp_weblinksetId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Web Link Set**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_weblinksetid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Web Link Set.**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_mspp_websitelanguageid"></a> mspp_websitelanguageid

|Property|Value|
|---|---|
|Description|**Optional language to associate with web link sets for language-specific primary navigation**|
|DisplayName|**Web Link Set Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websitelanguageid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_websitelanguage|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Web Link Set**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_weblinkset_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Web Link Set**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_weblinkset_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_publishingstate_weblinkset](#BKMK_mspp_publishingstate_weblinkset)
- [mspp_systemuser_mspp_weblinkset_createdby](#BKMK_mspp_systemuser_mspp_weblinkset_createdby)
- [mspp_systemuser_mspp_weblinkset_modifiedby](#BKMK_mspp_systemuser_mspp_weblinkset_modifiedby)
- [mspp_website_weblinkset](#BKMK_mspp_website_weblinkset)
- [mspp_websitelanguage_weblinkset](#BKMK_mspp_websitelanguage_weblinkset)

### <a name="BKMK_mspp_publishingstate_weblinkset"></a> mspp_publishingstate_weblinkset

One-To-Many Relationship: [mspp_publishingstate mspp_publishingstate_weblinkset](mspp_publishingstate.md#BKMK_mspp_publishingstate_weblinkset)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencingEntityNavigationPropertyName|`mspp_publishingstateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_weblinkset_createdby"></a> mspp_systemuser_mspp_weblinkset_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_weblinkset_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_weblinkset_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_weblinkset_modifiedby"></a> mspp_systemuser_mspp_weblinkset_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_weblinkset_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_weblinkset_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_weblinkset"></a> mspp_website_weblinkset

One-To-Many Relationship: [mspp_website mspp_website_weblinkset](mspp_website.md#BKMK_mspp_website_weblinkset)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_websitelanguage_weblinkset"></a> mspp_websitelanguage_weblinkset

One-To-Many Relationship: [mspp_websitelanguage mspp_websitelanguage_weblinkset](mspp_websitelanguage.md#BKMK_mspp_websitelanguage_weblinkset)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_websitelanguage`|
|ReferencedAttribute|`mspp_websitelanguageid`|
|ReferencingAttribute|`mspp_websitelanguageid`|
|ReferencingEntityNavigationPropertyName|`mspp_websitelanguageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_weblinkset_weblink](#BKMK_mspp_weblinkset_weblink)
- [mspp_webpage_navigation_weblinkset](#BKMK_mspp_webpage_navigation_weblinkset)

### <a name="BKMK_mspp_weblinkset_weblink"></a> mspp_weblinkset_weblink

Many-To-One Relationship: [mspp_weblink mspp_weblinkset_weblink](mspp_weblink.md#BKMK_mspp_weblinkset_weblink)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblink`|
|ReferencingAttribute|`mspp_weblinksetid`|
|ReferencedEntityNavigationPropertyName|`mspp_weblinkset_weblink`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_navigation_weblinkset"></a> mspp_webpage_navigation_weblinkset

Many-To-One Relationship: [mspp_webpage mspp_webpage_navigation_weblinkset](mspp_webpage.md#BKMK_mspp_webpage_navigation_weblinkset)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_navigation`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_navigation_weblinkset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_weblinkset?displayProperty=fullName>
