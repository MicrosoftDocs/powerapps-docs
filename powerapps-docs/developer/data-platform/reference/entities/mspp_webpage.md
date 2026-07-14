---
title: "Web Page (mspp_webpage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Web Page (mspp_webpage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Web Page (mspp_webpage) table/entity reference (Microsoft Dataverse)

Web Page

## Messages

The following table lists the messages for the Web Page (mspp_webpage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_webpages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_webpages(*mspp_webpageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_webpages(*mspp_webpageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_webpages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_webpages(*mspp_webpageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_webpages(*mspp_webpageid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Web Page (mspp_webpage) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Web Page (mspp_webpage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Web Page** |
| **DisplayCollectionName** | **Web Pages** |
| **SchemaName** | `mspp_webpage` |
| **CollectionSchemaName** | `mspp_webpages` |
| **EntitySetName** | `mspp_webpages`|
| **LogicalName** | `mspp_webpage` |
| **LogicalCollectionName** | `mspp_webpages` |
| **PrimaryIdAttribute** | `mspp_webpageid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_alloworigin](#BKMK_mspp_alloworigin)
- [mspp_category](#BKMK_mspp_category)
- [mspp_copy](#BKMK_mspp_copy)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_customcss](#BKMK_mspp_customcss)
- [mspp_customjavascript](#BKMK_mspp_customjavascript)
- [mspp_displaydate](#BKMK_mspp_displaydate)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_editorialcomments](#BKMK_mspp_editorialcomments)
- [mspp_enablerating](#BKMK_mspp_enablerating)
- [mspp_entityform](#BKMK_mspp_entityform)
- [mspp_entitylist](#BKMK_mspp_entitylist)
- [mspp_excludefromsearch](#BKMK_mspp_excludefromsearch)
- [mspp_expirationdate](#BKMK_mspp_expirationdate)
- [mspp_feedbackpolicy](#BKMK_mspp_feedbackpolicy)
- [mspp_hiddenfromsitemap](#BKMK_mspp_hiddenfromsitemap)
- [mspp_image](#BKMK_mspp_image)
- [mspp_imageurl](#BKMK_mspp_imageurl)
- [mspp_isofflinecached](#BKMK_mspp_isofflinecached)
- [mspp_isroot](#BKMK_mspp_isroot)
- [mspp_masterwebpageid](#BKMK_mspp_masterwebpageid)
- [mspp_meta_description](#BKMK_mspp_meta_description)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_navigation](#BKMK_mspp_navigation)
- [mspp_pagetemplateid](#BKMK_mspp_pagetemplateid)
- [mspp_parentpageid](#BKMK_mspp_parentpageid)
- [mspp_partialurl](#BKMK_mspp_partialurl)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_releasedate](#BKMK_mspp_releasedate)
- [mspp_rootwebpageid](#BKMK_mspp_rootwebpageid)
- [mspp_sharedpageconfiguration](#BKMK_mspp_sharedpageconfiguration)
- [mspp_summary](#BKMK_mspp_summary)
- [mspp_title](#BKMK_mspp_title)
- [mspp_webform](#BKMK_mspp_webform)
- [mspp_webpageId](#BKMK_mspp_webpageId)
- [mspp_webpagelanguageid](#BKMK_mspp_webpagelanguageid)
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

### <a name="BKMK_mspp_category"></a> mspp_category

|Property|Value|
|---|---|
|Description||
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_category`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_webpage_mspp_category`|

#### mspp_category Choices/Options

|Value|Label|
|---|---|
|1|**News**|

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
|MaxLength|1048576|

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

### <a name="BKMK_mspp_customcss"></a> mspp_customcss

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom CSS**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_customcss`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_mspp_customjavascript"></a> mspp_customjavascript

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom JavaScript**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_customjavascript`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

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

### <a name="BKMK_mspp_editorialcomments"></a> mspp_editorialcomments

|Property|Value|
|---|---|
|Description||
|DisplayName|**Editorial Comments**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_editorialcomments`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_enablerating"></a> mspp_enablerating

|Property|Value|
|---|---|
|Description|**Setting this value to 'Yes' will allow users to rate the web page.**|
|DisplayName|**Enable Ratings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_enablerating`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webpage_mspp_enablerating`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_entityform"></a> mspp_entityform

|Property|Value|
|---|---|
|Description|**Unique identifier for Entity Form associated with Web Page.**|
|DisplayName|**Basic Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entityform`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_entityform|

### <a name="BKMK_mspp_entitylist"></a> mspp_entitylist

|Property|Value|
|---|---|
|Description|**Unique identifier for Entity List associated with Web Page.**|
|DisplayName|**List**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitylist`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_entitylist|

### <a name="BKMK_mspp_excludefromsearch"></a> mspp_excludefromsearch

|Property|Value|
|---|---|
|Description|**Shows whether the webpage is excluded from the portal search.**|
|DisplayName|**Exclude From Search**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_excludefromsearch`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webpage_mspp_excludefromsearch`|
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

### <a name="BKMK_mspp_feedbackpolicy"></a> mspp_feedbackpolicy

|Property|Value|
|---|---|
|Description||
|DisplayName|**Comment Policy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_feedbackpolicy`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_webpage_mspp_feedbackpolicy`|

#### mspp_feedbackpolicy Choices/Options

|Value|Label|
|---|---|
|756150000|**Inherit**|
|756150001|**None**|
|756150002|**Open**|
|756150003|**Item**|
|756150004|**Moderated**|
|756150005|**Closed**|

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
|GlobalChoiceName|`mspp_webpage_mspp_hiddenfromsitemap`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_image"></a> mspp_image

|Property|Value|
|---|---|
|Description|**Unique identifier for Web File associated with Web Page.**|
|DisplayName|**Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_image`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webfile|

### <a name="BKMK_mspp_imageurl"></a> mspp_imageurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Image URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_imageurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_mspp_isofflinecached"></a> mspp_isofflinecached

|Property|Value|
|---|---|
|Description|**Define whether to cache this page for PWA.**|
|DisplayName|**isOfflineCached**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_isofflinecached`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_webpage_mspp_isofflinecached`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_isroot"></a> mspp_isroot

|Property|Value|
|---|---|
|Description|**Defines whether this is the "root" record of this translated group of Web Pages.**|
|DisplayName|**Is Root**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_isroot`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_webpage_mspp_isroot`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_masterwebpageid"></a> mspp_masterwebpageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Web Page.**|
|DisplayName|**Master Web Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_masterwebpageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_meta_description"></a> mspp_meta_description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_meta_description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

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

### <a name="BKMK_mspp_navigation"></a> mspp_navigation

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Link Set associated with Web Page.**|
|DisplayName|**Navigation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_navigation`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_weblinkset|

### <a name="BKMK_mspp_pagetemplateid"></a> mspp_pagetemplateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Page Template associated with Web Page.**|
|DisplayName|**Page Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_pagetemplateid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_pagetemplate|

### <a name="BKMK_mspp_parentpageid"></a> mspp_parentpageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Web Page.**|
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
|MaxLength|100|

### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Publishing State associated with Web Page.**|
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

### <a name="BKMK_mspp_rootwebpageid"></a> mspp_rootwebpageid

|Property|Value|
|---|---|
|Description|**Lookup to root WebPage.**|
|DisplayName|**Root Webpage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_rootwebpageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_sharedpageconfiguration"></a> mspp_sharedpageconfiguration

|Property|Value|
|---|---|
|Description|**Determines if the content page uses the root page configuration**|
|DisplayName|**Shared Page Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_sharedpageconfiguration`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_webpage_mspp_sharedpageconfiguration`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_mspp_webform"></a> mspp_webform

|Property|Value|
|---|---|
|Description|**Unique identifier for Multistep Form associated with Web Page.**|
|DisplayName|**Multistep Form**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webform`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webform|

### <a name="BKMK_mspp_webpageId"></a> mspp_webpageId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Web Page**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_webpageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_webpagelanguageid"></a> mspp_webpagelanguageid

|Property|Value|
|---|---|
|Description|**Language of this web page.**|
|DisplayName|**Webpage Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webpagelanguageid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_websitelanguage|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Web Page.**|
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
|Description|**Status of the Web Page**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webpage_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Web Page**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webpage_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_pagetemplate_webpage](#BKMK_mspp_pagetemplate_webpage)
- [mspp_publishingstate_webpage](#BKMK_mspp_publishingstate_webpage)
- [mspp_systemuser_mspp_webpage_createdby](#BKMK_mspp_systemuser_mspp_webpage_createdby)
- [mspp_systemuser_mspp_webpage_modifiedby](#BKMK_mspp_systemuser_mspp_webpage_modifiedby)
- [mspp_webfile_webpage_image](#BKMK_mspp_webfile_webpage_image)
- [mspp_webpage_entityform](#BKMK_mspp_webpage_entityform)
- [mspp_webpage_entitylist](#BKMK_mspp_webpage_entitylist)
- [mspp_webpage_masterwebpage](#BKMK_mspp_webpage_masterwebpage-many-to-one)
- [mspp_webpage_navigation_weblinkset](#BKMK_mspp_webpage_navigation_weblinkset)
- [mspp_webpage_webform](#BKMK_mspp_webpage_webform)
- [mspp_webpage_webpage](#BKMK_mspp_webpage_webpage-many-to-one)
- [mspp_webpage_webpage_rootwebpageid](#BKMK_mspp_webpage_webpage_rootwebpageid-many-to-one)
- [mspp_website_webpage](#BKMK_mspp_website_webpage)
- [mspp_websitelanguage_webpage_webpagelanguageid](#BKMK_mspp_websitelanguage_webpage_webpagelanguageid)

### <a name="BKMK_mspp_pagetemplate_webpage"></a> mspp_pagetemplate_webpage

One-To-Many Relationship: [mspp_pagetemplate mspp_pagetemplate_webpage](mspp_pagetemplate.md#BKMK_mspp_pagetemplate_webpage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_pagetemplate`|
|ReferencedAttribute|`mspp_pagetemplateid`|
|ReferencingAttribute|`mspp_pagetemplateid`|
|ReferencingEntityNavigationPropertyName|`mspp_pagetemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_publishingstate_webpage"></a> mspp_publishingstate_webpage

One-To-Many Relationship: [mspp_publishingstate mspp_publishingstate_webpage](mspp_publishingstate.md#BKMK_mspp_publishingstate_webpage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencingEntityNavigationPropertyName|`mspp_publishingstateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webpage_createdby"></a> mspp_systemuser_mspp_webpage_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webpage_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webpage_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webpage_modifiedby"></a> mspp_systemuser_mspp_webpage_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webpage_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webpage_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webfile_webpage_image"></a> mspp_webfile_webpage_image

One-To-Many Relationship: [mspp_webfile mspp_webfile_webpage_image](mspp_webfile.md#BKMK_mspp_webfile_webpage_image)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webfile`|
|ReferencedAttribute|`mspp_webfileid`|
|ReferencingAttribute|`mspp_image`|
|ReferencingEntityNavigationPropertyName|`mspp_image`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_entityform"></a> mspp_webpage_entityform

One-To-Many Relationship: [mspp_entityform mspp_webpage_entityform](mspp_entityform.md#BKMK_mspp_webpage_entityform)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_entityform`|
|ReferencedAttribute|`mspp_entityformid`|
|ReferencingAttribute|`mspp_entityform`|
|ReferencingEntityNavigationPropertyName|`mspp_entityform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_entitylist"></a> mspp_webpage_entitylist

One-To-Many Relationship: [mspp_entitylist mspp_webpage_entitylist](mspp_entitylist.md#BKMK_mspp_webpage_entitylist)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_entitylist`|
|ReferencedAttribute|`mspp_entitylistid`|
|ReferencingAttribute|`mspp_entitylist`|
|ReferencingEntityNavigationPropertyName|`mspp_entitylist`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_masterwebpage-many-to-one"></a> mspp_webpage_masterwebpage

One-To-Many Relationship: [mspp_webpage mspp_webpage_masterwebpage](#BKMK_mspp_webpage_masterwebpage-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_masterwebpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_masterwebpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_navigation_weblinkset"></a> mspp_webpage_navigation_weblinkset

One-To-Many Relationship: [mspp_weblinkset mspp_webpage_navigation_weblinkset](mspp_weblinkset.md#BKMK_mspp_webpage_navigation_weblinkset)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_weblinkset`|
|ReferencedAttribute|`mspp_weblinksetid`|
|ReferencingAttribute|`mspp_navigation`|
|ReferencingEntityNavigationPropertyName|`mspp_navigation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_webform"></a> mspp_webpage_webform

One-To-Many Relationship: [mspp_webform mspp_webpage_webform](mspp_webform.md#BKMK_mspp_webpage_webform)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webform`|
|ReferencedAttribute|`mspp_webformid`|
|ReferencingAttribute|`mspp_webform`|
|ReferencingEntityNavigationPropertyName|`mspp_webform`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_webpage-many-to-one"></a> mspp_webpage_webpage

One-To-Many Relationship: [mspp_webpage mspp_webpage_webpage](#BKMK_mspp_webpage_webpage-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_parentpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_parentpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_webpage_rootwebpageid-many-to-one"></a> mspp_webpage_webpage_rootwebpageid

One-To-Many Relationship: [mspp_webpage mspp_webpage_webpage_rootwebpageid](#BKMK_mspp_webpage_webpage_rootwebpageid-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_rootwebpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_rootwebpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_webpage"></a> mspp_website_webpage

One-To-Many Relationship: [mspp_website mspp_website_webpage](mspp_website.md#BKMK_mspp_website_webpage)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_websitelanguage_webpage_webpagelanguageid"></a> mspp_websitelanguage_webpage_webpagelanguageid

One-To-Many Relationship: [mspp_websitelanguage mspp_websitelanguage_webpage_webpagelanguageid](mspp_websitelanguage.md#BKMK_mspp_websitelanguage_webpage_webpagelanguageid)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_websitelanguage`|
|ReferencedAttribute|`mspp_websitelanguageid`|
|ReferencingAttribute|`mspp_webpagelanguageid`|
|ReferencingEntityNavigationPropertyName|`mspp_webpagelanguageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [mspp_entityform_redirectwebpage](#BKMK_mspp_entityform_redirectwebpage)
- [mspp_entitylist_webpageforcreate](#BKMK_mspp_entitylist_webpageforcreate)
- [mspp_entitylist_webpagefordetailsview](#BKMK_mspp_entitylist_webpagefordetailsview)
- [mspp_parentwebpage_shortcut](#BKMK_mspp_parentwebpage_shortcut)
- [mspp_webformstep_redirectwebpage](#BKMK_mspp_webformstep_redirectwebpage)
- [mspp_webpage_masterwebpage](#BKMK_mspp_webpage_masterwebpage-one-to-many)
- [mspp_webpage_redirect](#BKMK_mspp_webpage_redirect)
- [mspp_webpage_shortcut](#BKMK_mspp_webpage_shortcut)
- [mspp_webpage_sitemarker](#BKMK_mspp_webpage_sitemarker)
- [mspp_webpage_webfile](#BKMK_mspp_webpage_webfile)
- [mspp_webpage_weblink](#BKMK_mspp_webpage_weblink)
- [mspp_webpage_webpage](#BKMK_mspp_webpage_webpage-one-to-many)
- [mspp_webpage_webpage_rootwebpageid](#BKMK_mspp_webpage_webpage_rootwebpageid-one-to-many)
- [mspp_webpage_webpageaccesscontrolrule](#BKMK_mspp_webpage_webpageaccesscontrolrule)

### <a name="BKMK_mspp_entityform_redirectwebpage"></a> mspp_entityform_redirectwebpage

Many-To-One Relationship: [mspp_entityform mspp_entityform_redirectwebpage](mspp_entityform.md#BKMK_mspp_entityform_redirectwebpage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entityform`|
|ReferencingAttribute|`mspp_redirectwebpage`|
|ReferencedEntityNavigationPropertyName|`mspp_entityform_redirectwebpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_entitylist_webpageforcreate"></a> mspp_entitylist_webpageforcreate

Many-To-One Relationship: [mspp_entitylist mspp_entitylist_webpageforcreate](mspp_entitylist.md#BKMK_mspp_entitylist_webpageforcreate)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entitylist`|
|ReferencingAttribute|`mspp_webpageforcreate`|
|ReferencedEntityNavigationPropertyName|`mspp_entitylist_webpageforcreate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_entitylist_webpagefordetailsview"></a> mspp_entitylist_webpagefordetailsview

Many-To-One Relationship: [mspp_entitylist mspp_entitylist_webpagefordetailsview](mspp_entitylist.md#BKMK_mspp_entitylist_webpagefordetailsview)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entitylist`|
|ReferencingAttribute|`mspp_webpagefordetailsview`|
|ReferencedEntityNavigationPropertyName|`mspp_entitylist_webpagefordetailsview`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Entity List (Details View)<br />MenuId: null<br />Order: 100590<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_parentwebpage_shortcut"></a> mspp_parentwebpage_shortcut

Many-To-One Relationship: [mspp_shortcut mspp_parentwebpage_shortcut](mspp_shortcut.md#BKMK_mspp_parentwebpage_shortcut)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_shortcut`|
|ReferencingAttribute|`mspp_parentpage_webpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_parentwebpage_shortcut`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 101200<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webformstep_redirectwebpage"></a> mspp_webformstep_redirectwebpage

Many-To-One Relationship: [mspp_webformstep mspp_webformstep_redirectwebpage](mspp_webformstep.md#BKMK_mspp_webformstep_redirectwebpage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webformstep`|
|ReferencingAttribute|`mspp_redirectwebpage`|
|ReferencedEntityNavigationPropertyName|`mspp_webformstep_redirectwebpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_masterwebpage-one-to-many"></a> mspp_webpage_masterwebpage

Many-To-One Relationship: [mspp_webpage mspp_webpage_masterwebpage](#BKMK_mspp_webpage_masterwebpage-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_masterwebpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_masterwebpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Subscriber Web Pages<br />MenuId: null<br />Order: 101400<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_redirect"></a> mspp_webpage_redirect

Many-To-One Relationship: [mspp_redirect mspp_webpage_redirect](mspp_redirect.md#BKMK_mspp_webpage_redirect)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_redirect`|
|ReferencingAttribute|`mspp_webpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_redirect`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 101100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_shortcut"></a> mspp_webpage_shortcut

Many-To-One Relationship: [mspp_shortcut mspp_webpage_shortcut](mspp_shortcut.md#BKMK_mspp_webpage_shortcut)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_shortcut`|
|ReferencingAttribute|`mspp_webpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_shortcut`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 101200<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_sitemarker"></a> mspp_webpage_sitemarker

Many-To-One Relationship: [mspp_sitemarker mspp_webpage_sitemarker](mspp_sitemarker.md#BKMK_mspp_webpage_sitemarker)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_sitemarker`|
|ReferencingAttribute|`mspp_pageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_sitemarker`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100300<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_webfile"></a> mspp_webpage_webfile

Many-To-One Relationship: [mspp_webfile mspp_webpage_webfile](mspp_webfile.md#BKMK_mspp_webpage_webfile)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webfile`|
|ReferencingAttribute|`mspp_parentpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_webfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Child Files<br />MenuId: null<br />Order: 100100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_weblink"></a> mspp_webpage_weblink

Many-To-One Relationship: [mspp_weblink mspp_webpage_weblink](mspp_weblink.md#BKMK_mspp_webpage_weblink)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblink`|
|ReferencingAttribute|`mspp_pageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_weblink`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 100400<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_webpage-one-to-many"></a> mspp_webpage_webpage

Many-To-One Relationship: [mspp_webpage mspp_webpage_webpage](#BKMK_mspp_webpage_webpage-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_parentpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_webpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Child Pages<br />MenuId: null<br />Order: 100200<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_webpage_rootwebpageid-one-to-many"></a> mspp_webpage_webpage_rootwebpageid

Many-To-One Relationship: [mspp_webpage mspp_webpage_webpage_rootwebpageid](#BKMK_mspp_webpage_webpage_rootwebpageid-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_rootwebpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_webpage_rootwebpageid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpage_webpageaccesscontrolrule"></a> mspp_webpage_webpageaccesscontrolrule

Many-To-One Relationship: [mspp_webpageaccesscontrolrule mspp_webpage_webpageaccesscontrolrule](mspp_webpageaccesscontrolrule.md#BKMK_mspp_webpage_webpageaccesscontrolrule)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpageaccesscontrolrule`|
|ReferencingAttribute|`mspp_webpageid`|
|ReferencedEntityNavigationPropertyName|`mspp_webpage_webpageaccesscontrolrule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Access Control Rules<br />MenuId: null<br />Order: 100100<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_webpage?displayProperty=fullName>
