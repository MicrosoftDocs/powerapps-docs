---
title: "Web Page Access Control Rule (mspp_webpageaccesscontrolrule) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Web Page Access Control Rule (mspp_webpageaccesscontrolrule) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Web Page Access Control Rule (mspp_webpageaccesscontrolrule) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Web Page Access Control Rule (mspp_webpageaccesscontrolrule) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_webpageaccesscontrolrules<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_webpageaccesscontrolrules<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_webpageaccesscontrolrules(*mspp_webpageaccesscontrolruleid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Web Page Access Control Rule (mspp_webpageaccesscontrolrule) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Web Page Access Control Rule (mspp_webpageaccesscontrolrule) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Web Page Access Control Rule** |
| **DisplayCollectionName** | **Web Page Access Control Rules** |
| **SchemaName** | `mspp_webpageaccesscontrolrule` |
| **CollectionSchemaName** | `mspp_webpageaccesscontrolrules` |
| **EntitySetName** | `mspp_webpageaccesscontrolrules`|
| **LogicalName** | `mspp_webpageaccesscontrolrule` |
| **LogicalCollectionName** | `mspp_webpageaccesscontrolrules` |
| **PrimaryIdAttribute** | `mspp_webpageaccesscontrolruleid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_description](#BKMK_mspp_description)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_right](#BKMK_mspp_right)
- [mspp_scope](#BKMK_mspp_scope)
- [mspp_webpageaccesscontrolruleId](#BKMK_mspp_webpageaccesscontrolruleId)
- [mspp_webpageid](#BKMK_mspp_webpageid)
- [mspp_websiteid](#BKMK_mspp_websiteid)
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
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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
|MaxLength|200|

### <a name="BKMK_mspp_right"></a> mspp_right

|Property|Value|
|---|---|
|Description||
|DisplayName|**Right**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_right`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_webpageaccesscontrolrule_mspp_right`|

#### mspp_right Choices/Options

|Value|Label|
|---|---|
|1|**Grant Change**|
|2|**Restrict Read**|

### <a name="BKMK_mspp_scope"></a> mspp_scope

|Property|Value|
|---|---|
|Description|**All child web files directly related to this web page will be excluded from security validation. This does not exclude the children's descendants.**|
|DisplayName|**Access Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_scope`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`mspp_webpageaccesscontrolrule_mspp_scope`|

#### mspp_scope Choices/Options

|Value|Label|
|---|---|
|1|**All content**|
|2|**Exclude direct child web files**|

### <a name="BKMK_mspp_webpageaccesscontrolruleId"></a> mspp_webpageaccesscontrolruleId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Webpage Access Control Rule**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_webpageaccesscontrolruleid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_webpageid"></a> mspp_webpageid

|Property|Value|
|---|---|
|Description|**Unique identifier for Web Page associated with Web Page Access Control Rule.**|
|DisplayName|**Web Page**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_webpageid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_webpage|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Web Page Access Control Rule.**|
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
|Description|**Status of the Web Page Access Control Rule**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webpageaccesscontrolrule_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Web Page Access Control Rule**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_webpageaccesscontrolrule_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_systemuser_mspp_webpageaccesscontrolrule_createdby](#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_createdby)
- [mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby](#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby)
- [mspp_webpage_webpageaccesscontrolrule](#BKMK_mspp_webpage_webpageaccesscontrolrule)
- [mspp_website_webpageaccesscontrolrule](#BKMK_mspp_website_webpageaccesscontrolrule)

### <a name="BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_createdby"></a> mspp_systemuser_mspp_webpageaccesscontrolrule_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webpageaccesscontrolrule_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby"></a> mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_webpageaccesscontrolrule_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_webpage_webpageaccesscontrolrule"></a> mspp_webpage_webpageaccesscontrolrule

One-To-Many Relationship: [mspp_webpage mspp_webpage_webpageaccesscontrolrule](mspp_webpage.md#BKMK_mspp_webpage_webpageaccesscontrolrule)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_webpage`|
|ReferencedAttribute|`mspp_webpageid`|
|ReferencingAttribute|`mspp_webpageid`|
|ReferencingEntityNavigationPropertyName|`mspp_webpageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_webpageaccesscontrolrule"></a> mspp_website_webpageaccesscontrolrule

One-To-Many Relationship: [mspp_website mspp_website_webpageaccesscontrolrule](mspp_website.md#BKMK_mspp_website_webpageaccesscontrolrule)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_website`|
|ReferencedAttribute|`mspp_websiteid`|
|ReferencingAttribute|`mspp_websiteid`|
|ReferencingEntityNavigationPropertyName|`mspp_websiteid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [mspp_accesscontrolrule_publishingstate](#BKMK_mspp_accesscontrolrule_publishingstate)
- [mspp_webpageaccesscontrolrule_webrole](#BKMK_mspp_webpageaccesscontrolrule_webrole)

### <a name="BKMK_mspp_accesscontrolrule_publishingstate"></a> mspp_accesscontrolrule_publishingstate

See [mspp_publishingstate mspp_accesscontrolrule_publishingstate Many-To-Many Relationship](mspp_publishingstate.md#BKMK_mspp_accesscontrolrule_publishingstate)

|Property|Value|
|---|---|
|IntersectEntityName|`mspp_accesscontrolrule_publishingstate`|
|IsCustomizable|False|
|SchemaName|`mspp_accesscontrolrule_publishingstate`|
|IntersectAttribute|`mspp_webpageaccesscontrolruleid`|
|NavigationPropertyName|`mspp_accesscontrolrule_publishingstate`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_webpageaccesscontrolrule_webrole"></a> mspp_webpageaccesscontrolrule_webrole

See [mspp_webrole mspp_webpageaccesscontrolrule_webrole Many-To-Many Relationship](mspp_webrole.md#BKMK_mspp_webpageaccesscontrolrule_webrole)

|Property|Value|
|---|---|
|IntersectEntityName|`mspp_webpageaccesscontrolrule_webrole`|
|IsCustomizable|False|
|SchemaName|`mspp_webpageaccesscontrolrule_webrole`|
|IntersectAttribute|`mspp_webpageaccesscontrolruleid`|
|NavigationPropertyName|`mspp_webpageaccesscontrolrule_webrole`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_webpageaccesscontrolrule?displayProperty=fullName>
