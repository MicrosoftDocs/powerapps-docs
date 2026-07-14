---
title: "Page Template (mspp_pagetemplate) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Page Template (mspp_pagetemplate) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Page Template (mspp_pagetemplate) table/entity reference (Microsoft Dataverse)

URL of the .aspx page used to create new webpages.

## Messages

The following table lists the messages for the Page Template (mspp_pagetemplate) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_pagetemplates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_pagetemplates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_pagetemplates(*mspp_pagetemplateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Page Template (mspp_pagetemplate) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Page Template (mspp_pagetemplate) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Page Template** |
| **DisplayCollectionName** | **Page Templates** |
| **SchemaName** | `mspp_pagetemplate` |
| **CollectionSchemaName** | `mspp_pagetemplates` |
| **EntitySetName** | `mspp_pagetemplates`|
| **LogicalName** | `mspp_pagetemplate` |
| **LogicalCollectionName** | `mspp_pagetemplates` |
| **PrimaryIdAttribute** | `mspp_pagetemplateid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_entityname](#BKMK_mspp_entityname)
- [mspp_isdefault](#BKMK_mspp_isdefault)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_pagetemplateId](#BKMK_mspp_pagetemplateId)
- [mspp_rewriteurl](#BKMK_mspp_rewriteurl)
- [mspp_type](#BKMK_mspp_type)
- [mspp_usewebsiteheaderandfooter](#BKMK_mspp_usewebsiteheaderandfooter)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_webtemplateid](#BKMK_mspp_webtemplateid)
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
|RequiredLevel|Recommended|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_mspp_entityname"></a> mspp_entityname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Table Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_mspp_isdefault"></a> mspp_isdefault

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_isdefault`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_pagetemplate_mspp_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_mspp_pagetemplateId"></a> mspp_pagetemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Page Template**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_pagetemplateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_rewriteurl"></a> mspp_rewriteurl

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rewrite Url**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_rewriteurl`|
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
|Description|**The type of the record.**|
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_type`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|756150000|
|GlobalChoiceName|`mspp_pagetemplate_mspp_type`|

#### mspp_type Choices/Options

|Value|Label|
|---|---|
|756150000|**Rewrite**|
|756150001|**Web Template**|

### <a name="BKMK_mspp_usewebsiteheaderandfooter"></a> mspp_usewebsiteheaderandfooter

|Property|Value|
|---|---|
|Description|**Control whether this web template page template will be rendered using the website header and footer, or control rendering of all page content.**|
|DisplayName|**Use Website Header and Footer**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_usewebsiteheaderandfooter`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_pagetemplate_mspp_usewebsiteheaderandfooter`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Page Template.**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_mspp_webtemplateid"></a> mspp_webtemplateid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Template associated with Page Template.**|
|DisplayName|**Web Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webtemplateid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_webtemplate|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Page Template**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_pagetemplate_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Page Template**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_pagetemplate_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_systemuser_mspp_pagetemplate_createdby](#BKMK_mspp_systemuser_mspp_pagetemplate_createdby)
- [mspp_systemuser_mspp_pagetemplate_modifiedby](#BKMK_mspp_systemuser_mspp_pagetemplate_modifiedby)
- [mspp_website_pagetemplate](#BKMK_mspp_website_pagetemplate)
- [mspp_webtemplate_pagetemplate](#BKMK_mspp_webtemplate_pagetemplate)

### <a name="BKMK_mspp_systemuser_mspp_pagetemplate_createdby"></a> mspp_systemuser_mspp_pagetemplate_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_pagetemplate_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_pagetemplate_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_pagetemplate_modifiedby"></a> mspp_systemuser_mspp_pagetemplate_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_pagetemplate_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_pagetemplate_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_pagetemplate"></a> mspp_website_pagetemplate

One-To-Many Relationship: [mspp_website mspp_website_pagetemplate](mspp_website.md#BKMK_mspp_website_pagetemplate)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webtemplate_pagetemplate"></a> mspp_webtemplate_pagetemplate

One-To-Many Relationship: [mspp_webtemplate mspp_webtemplate_pagetemplate](mspp_webtemplate.md#BKMK_mspp_webtemplate_pagetemplate)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webtemplate`|
|ReferencedAttribute|`mspp_webtemplateid`|
|ReferencingAttribute|`mspp_webtemplateid`|
|ReferencingEntityNavigationPropertyName|`mspp_webtemplateid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_mspp_pagetemplate_webpage"></a> mspp_pagetemplate_webpage

Many-To-One Relationship: [mspp_webpage mspp_pagetemplate_webpage](mspp_webpage.md#BKMK_mspp_pagetemplate_webpage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_pagetemplateid`|
|ReferencedEntityNavigationPropertyName|`mspp_pagetemplate_webpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_pagetemplate?displayProperty=fullName>
