---
title: "Web File (mspp_webfile) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Web File (mspp_webfile) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Web File (mspp_webfile) table/entity reference (Microsoft Dataverse)

Storage of files used in the web Portals.

## Messages

The following table lists the messages for the Web File (mspp_webfile) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_webfiles<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_webfiles(*mspp_webfileid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_webfiles(*mspp_webfileid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_webfiles<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_webfiles(*mspp_webfileid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_webfiles(*mspp_webfileid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Web File (mspp_webfile) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Web File (mspp_webfile) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Web File** |
| **DisplayCollectionName** | **Web Files** |
| **SchemaName** | `mspp_webfile` |
| **CollectionSchemaName** | `mspp_webfiles` |
| **EntitySetName** | `mspp_webfiles`|
| **LogicalName** | `mspp_webfile` |
| **LogicalCollectionName** | `mspp_webfiles` |
| **PrimaryIdAttribute** | `mspp_webfileid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_alloworigin](#BKMK_mspp_alloworigin)
- [mspp_cloudblobaddress](#BKMK_mspp_cloudblobaddress)
- [mspp_contentdisposition](#BKMK_mspp_contentdisposition)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_displaydate](#BKMK_mspp_displaydate)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_excludefromsearch](#BKMK_mspp_excludefromsearch)
- [mspp_expirationdate](#BKMK_mspp_expirationdate)
- [mspp_hiddenfromsitemap](#BKMK_mspp_hiddenfromsitemap)
- [mspp_masterwebfileid](#BKMK_mspp_masterwebfileid)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_parentpageid](#BKMK_mspp_parentpageid)
- [mspp_partialurl](#BKMK_mspp_partialurl)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_releasedate](#BKMK_mspp_releasedate)
- [mspp_summary](#BKMK_mspp_summary)
- [mspp_title](#BKMK_mspp_title)
- [mspp_webfileId](#BKMK_mspp_webfileId)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_alloworigin"></a> mspp_alloworigin

|Property|Value|
|---|---|
|Description|**Defines CORS header Access-Control-Allow-Origin for cross origin requests.**|
|DisplayName|**Allow Origin**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_alloworigin`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_mspp_cloudblobaddress"></a> mspp_cloudblobaddress

|Property|Value|
|---|---|
|Description||
|DisplayName|**Cloud Blob Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_cloudblobaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_mspp_contentdisposition"></a> mspp_contentdisposition

|Property|Value|
|---|---|
|Description|**Shows the value to be applied to the HTTP Response Headers Content-Disposition.**|
|DisplayName|**Content-Disposition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_contentdisposition`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_webfile_mspp_contentdisposition`|

#### mspp_contentdisposition Choices/Options

|Value|Label|
|---|---|
|756150000|**inline**|
|756150001|**attachment**|

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

### <a name="BKMK_mspp_displaydate"></a> mspp_displaydate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displaydate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_mspp_displayorder"></a> mspp_displayorder

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displayorder`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_excludefromsearch"></a> mspp_excludefromsearch

|Property|Value|
|---|---|
|Description|**Shows whether the web file is excluded from the portal search.**|
|DisplayName|**Exclude From Search**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_excludefromsearch`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webfile_mspp_excludefromsearch`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_expirationdate"></a> mspp_expirationdate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Expiration Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_expirationdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_mspp_hiddenfromsitemap"></a> mspp_hiddenfromsitemap

|Property|Value|
|---|---|
|Description||
|DisplayName|**Hidden From Sitemap**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_hiddenfromsitemap`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_webfile_mspp_hiddenfromsitemap`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_masterwebfileid"></a> mspp_masterwebfileid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web File associated with Web File.**|
|DisplayName|**Master Web File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_masterwebfileid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webfile|

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

### <a name="BKMK_mspp_parentpageid"></a> mspp_parentpageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Web File.**|
|DisplayName|**Parent Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_parentpageid`|
|RequiredLevel|Recommended|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_partialurl"></a> mspp_partialurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Partial URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_partialurl`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Publishing State associated with Web File.**|
|DisplayName|**Publishing State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_publishingstateid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_publishingstate|

### <a name="BKMK_mspp_releasedate"></a> mspp_releasedate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Release Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_releasedate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_mspp_summary"></a> mspp_summary

|Property|Value|
|---|---|
|Description||
|DisplayName|**Summary**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_summary`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25000|

### <a name="BKMK_mspp_title"></a> mspp_title

|Property|Value|
|---|---|
|Description||
|DisplayName|**Title**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_title`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_mspp_webfileId"></a> mspp_webfileId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Web File**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_webfileid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Web File.**|
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
|Description|**Status of the Web File**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webfile_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Web File**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webfile_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_publishingstate_webfile](#BKMK_mspp_publishingstate_webfile)
- [mspp_systemuser_mspp_webfile_createdby](#BKMK_mspp_systemuser_mspp_webfile_createdby)
- [mspp_systemuser_mspp_webfile_modifiedby](#BKMK_mspp_systemuser_mspp_webfile_modifiedby)
- [mspp_webfile_masterwebfile](#BKMK_mspp_webfile_masterwebfile-many-to-one)
- [mspp_webpage_webfile](#BKMK_mspp_webpage_webfile)
- [mspp_website_webfile](#BKMK_mspp_website_webfile)

### <a name="BKMK_mspp_publishingstate_webfile"></a> mspp_publishingstate_webfile

One-To-Many Relationship: [mspp_publishingstate mspp_publishingstate_webfile](mspp_publishingstate.md#BKMK_mspp_publishingstate_webfile)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencingEntityNavigationPropertyName|`mspp_publishingstateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webfile_createdby"></a> mspp_systemuser_mspp_webfile_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webfile_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webfile_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webfile_modifiedby"></a> mspp_systemuser_mspp_webfile_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webfile_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webfile_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webfile_masterwebfile-many-to-one"></a> mspp_webfile_masterwebfile

One-To-Many Relationship: [mspp_webfile mspp_webfile_masterwebfile](#BKMK_mspp_webfile_masterwebfile-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webfile`|
|ReferencedAttribute|`mspp_webfileid`|
|ReferencingAttribute|`mspp_masterwebfileid`|
|ReferencingEntityNavigationPropertyName|`mspp_masterwebfileid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_webfile"></a> mspp_webpage_webfile

One-To-Many Relationship: [mspp_webpage mspp_webpage_webfile](mspp_webpage.md#BKMK_mspp_webpage_webfile)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_parentpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_parentpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_webfile"></a> mspp_website_webfile

One-To-Many Relationship: [mspp_website mspp_website_webfile](mspp_website.md#BKMK_mspp_website_webfile)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_webfile_masterwebfile](#BKMK_mspp_webfile_masterwebfile-one-to-many)
- [mspp_webfile_shortcut](#BKMK_mspp_webfile_shortcut)
- [mspp_webfile_webpage_image](#BKMK_mspp_webfile_webpage_image)

### <a name="BKMK_mspp_webfile_masterwebfile-one-to-many"></a> mspp_webfile_masterwebfile

Many-To-One Relationship: [mspp_webfile mspp_webfile_masterwebfile](#BKMK_mspp_webfile_masterwebfile-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webfile`|
|ReferencingAttribute|`mspp_masterwebfileid`|
|ReferencedEntityNavigationPropertyName|`mspp_webfile_masterwebfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Subscriber Web Files<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webfile_shortcut"></a> mspp_webfile_shortcut

Many-To-One Relationship: [mspp_shortcut mspp_webfile_shortcut](mspp_shortcut.md#BKMK_mspp_webfile_shortcut)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_shortcut`|
|ReferencingAttribute|`mspp_webfileid`|
|ReferencedEntityNavigationPropertyName|`mspp_webfile_shortcut`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webfile_webpage_image"></a> mspp_webfile_webpage_image

Many-To-One Relationship: [mspp_webpage mspp_webfile_webpage_image](mspp_webpage.md#BKMK_mspp_webfile_webpage_image)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_image`|
|ReferencedEntityNavigationPropertyName|`mspp_webfile_webpage_image`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_webfile?displayProperty=fullName>
