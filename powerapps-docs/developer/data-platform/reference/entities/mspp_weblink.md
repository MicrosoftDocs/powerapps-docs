---
title: "Web Link (mspp_weblink) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Web Link (mspp_weblink) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Web Link (mspp_weblink) table/entity reference (Microsoft Dataverse)

A textual or imaged based link to an interal or external URL.

## Messages

The following table lists the messages for the Web Link (mspp_weblink) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_weblinks<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_weblinks(*mspp_weblinkid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_weblinks(*mspp_weblinkid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_weblinks<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_weblinks(*mspp_weblinkid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_weblinks(*mspp_weblinkid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Web Link (mspp_weblink) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Web Link (mspp_weblink) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Web Link** |
| **DisplayCollectionName** | **Web Links** |
| **SchemaName** | `mspp_weblink` |
| **CollectionSchemaName** | `mspp_weblinks` |
| **EntitySetName** | `mspp_weblinks`|
| **LogicalName** | `mspp_weblink` |
| **LogicalCollectionName** | `mspp_weblinks` |
| **PrimaryIdAttribute** | `mspp_weblinkid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdbyipaddress](#BKMK_mspp_createdbyipaddress)
- [mspp_createdbyusername](#BKMK_mspp_createdbyusername)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_disablepagevalidation](#BKMK_mspp_disablepagevalidation)
- [mspp_displayimageonly](#BKMK_mspp_displayimageonly)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_displaypagechildlinks](#BKMK_mspp_displaypagechildlinks)
- [mspp_externalurl](#BKMK_mspp_externalurl)
- [mspp_imagealttext](#BKMK_mspp_imagealttext)
- [mspp_imageheight](#BKMK_mspp_imageheight)
- [mspp_imageurl](#BKMK_mspp_imageurl)
- [mspp_imagewidth](#BKMK_mspp_imagewidth)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedbyipaddress](#BKMK_mspp_modifiedbyipaddress)
- [mspp_modifiedbyusername](#BKMK_mspp_modifiedbyusername)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_openinnewwindow](#BKMK_mspp_openinnewwindow)
- [mspp_pageid](#BKMK_mspp_pageid)
- [mspp_parentweblinkid](#BKMK_mspp_parentweblinkid)
- [mspp_publishingstateid](#BKMK_mspp_publishingstateid)
- [mspp_robotsfollowlink](#BKMK_mspp_robotsfollowlink)
- [mspp_weblinkId](#BKMK_mspp_weblinkId)
- [mspp_weblinksetid](#BKMK_mspp_weblinksetid)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

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

### <a name="BKMK_mspp_description"></a> mspp_description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_disablepagevalidation"></a> mspp_disablepagevalidation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Disable Page Validation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_disablepagevalidation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_weblink_mspp_disablepagevalidation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_displayimageonly"></a> mspp_displayimageonly

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Image Only**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displayimageonly`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_weblink_mspp_displayimageonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_displayorder"></a> mspp_displayorder

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displayorder`|
|RequiredLevel|Recommended|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_displaypagechildlinks"></a> mspp_displaypagechildlinks

|Property|Value|
|---|---|
|Description|**Select whether to display the children of the page as child links for this link.**|
|DisplayName|**Display Page Child Links**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displaypagechildlinks`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_weblink_mspp_displaypagechildlinks`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_externalurl"></a> mspp_externalurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**External Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_externalurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2048|

### <a name="BKMK_mspp_imagealttext"></a> mspp_imagealttext

|Property|Value|
|---|---|
|Description||
|DisplayName|**Image Alt Text**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_imagealttext`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_mspp_imageheight"></a> mspp_imageheight

|Property|Value|
|---|---|
|Description||
|DisplayName|**Image Height**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_imageheight`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_mspp_imageurl"></a> mspp_imageurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Image Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_imageurl`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_mspp_imagewidth"></a> mspp_imagewidth

|Property|Value|
|---|---|
|Description||
|DisplayName|**Image Width**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_imagewidth`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_mspp_openinnewwindow"></a> mspp_openinnewwindow

|Property|Value|
|---|---|
|Description||
|DisplayName|**Open In New Window**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_openinnewwindow`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_weblink_mspp_openinnewwindow`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_pageid"></a> mspp_pageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Web Link.**|
|DisplayName|**Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_pageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_parentweblinkid"></a> mspp_parentweblinkid

|Property|Value|
|---|---|
|Description|**Unique identifier for parent Web Link associated with Web Link.**|
|DisplayName|**Parent Web Link**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_parentweblinkid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_weblink|

### <a name="BKMK_mspp_publishingstateid"></a> mspp_publishingstateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Publishing State associated with Web Link.**|
|DisplayName|**Publishing State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_publishingstateid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_publishingstate|

### <a name="BKMK_mspp_robotsfollowlink"></a> mspp_robotsfollowlink

|Property|Value|
|---|---|
|Description||
|DisplayName|**Robots Follow Link**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_robotsfollowlink`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_weblink_mspp_robotsfollowlink`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_weblinkId"></a> mspp_weblinkId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Web Link**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_weblinkid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_weblinksetid"></a> mspp_weblinksetid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Link Set associated with Web Link.**|
|DisplayName|**Web Link Set**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_weblinksetid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_weblinkset|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Web Link**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_weblink_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Web Link**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_weblink_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_publishingstate_weblink](#BKMK_mspp_publishingstate_weblink)
- [mspp_systemuser_mspp_weblink_createdby](#BKMK_mspp_systemuser_mspp_weblink_createdby)
- [mspp_systemuser_mspp_weblink_modifiedby](#BKMK_mspp_systemuser_mspp_weblink_modifiedby)
- [mspp_weblink_weblink](#BKMK_mspp_weblink_weblink-many-to-one)
- [mspp_weblinkset_weblink](#BKMK_mspp_weblinkset_weblink)
- [mspp_webpage_weblink](#BKMK_mspp_webpage_weblink)

### <a name="BKMK_mspp_publishingstate_weblink"></a> mspp_publishingstate_weblink

One-To-Many Relationship: [mspp_publishingstate mspp_publishingstate_weblink](mspp_publishingstate.md#BKMK_mspp_publishingstate_weblink)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_publishingstate`|
|ReferencedAttribute|`mspp_publishingstateid`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencingEntityNavigationPropertyName|`mspp_publishingstateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_weblink_createdby"></a> mspp_systemuser_mspp_weblink_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_weblink_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_weblink_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_weblink_modifiedby"></a> mspp_systemuser_mspp_weblink_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_weblink_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_weblink_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_weblink_weblink-many-to-one"></a> mspp_weblink_weblink

One-To-Many Relationship: [mspp_weblink mspp_weblink_weblink](#BKMK_mspp_weblink_weblink-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_weblink`|
|ReferencedAttribute|`mspp_weblinkid`|
|ReferencingAttribute|`mspp_parentweblinkid`|
|ReferencingEntityNavigationPropertyName|`mspp_parentweblinkid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_weblinkset_weblink"></a> mspp_weblinkset_weblink

One-To-Many Relationship: [mspp_weblinkset mspp_weblinkset_weblink](mspp_weblinkset.md#BKMK_mspp_weblinkset_weblink)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_weblinkset`|
|ReferencedAttribute|`mspp_weblinksetid`|
|ReferencingAttribute|`mspp_weblinksetid`|
|ReferencingEntityNavigationPropertyName|`mspp_weblinksetid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_weblink"></a> mspp_webpage_weblink

One-To-Many Relationship: [mspp_webpage mspp_webpage_weblink](mspp_webpage.md#BKMK_mspp_webpage_weblink)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_pageid`|
|ReferencingEntityNavigationPropertyName|`mspp_pageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_mspp_weblink_weblink-one-to-many"></a> mspp_weblink_weblink

Many-To-One Relationship: [mspp_weblink mspp_weblink_weblink](#BKMK_mspp_weblink_weblink-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblink`|
|ReferencingAttribute|`mspp_parentweblinkid`|
|ReferencedEntityNavigationPropertyName|`mspp_weblink_weblink`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseLabel`<br />Group: `Details`<br />Label: Child Links<br />MenuId: null<br />Order: 100500<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_weblink?displayProperty=fullName>
