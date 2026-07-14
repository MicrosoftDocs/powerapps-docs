---
title: "Publishing State (mspp_publishingstate) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Publishing State (mspp_publishingstate) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Publishing State (mspp_publishingstate) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Publishing State (mspp_publishingstate) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_publishingstates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_publishingstates<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_publishingstates(*mspp_publishingstateid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Publishing State (mspp_publishingstate) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Publishing State (mspp_publishingstate) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Publishing State** |
| **DisplayCollectionName** | **Publishing States** |
| **SchemaName** | `mspp_publishingstate` |
| **CollectionSchemaName** | `mspp_publishingstates` |
| **EntitySetName** | `mspp_publishingstates`|
| **LogicalName** | `mspp_publishingstate` |
| **LogicalCollectionName** | `mspp_publishingstates` |
| **PrimaryIdAttribute** | `mspp_publishingstateid` |
| **PrimaryNameAttribute** |`mspp_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_displayorder](#BKMK_mspp_displayorder)
- [mspp_isdefault](#BKMK_mspp_isdefault)
- [mspp_isvisible](#BKMK_mspp_isvisible)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_name](#BKMK_mspp_name)
- [mspp_publishingstateId](#BKMK_mspp_publishingstateId)
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

### <a name="BKMK_mspp_displayorder"></a> mspp_displayorder

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Order**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_displayorder`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_mspp_isdefault"></a> mspp_isdefault

|Property|Value|
|---|---|
|Description||
|DisplayName|**Is Default**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_isdefault`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_publishingstate_mspp_isdefault`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_isvisible"></a> mspp_isvisible

|Property|Value|
|---|---|
|Description||
|DisplayName|**Select whether the publishing state is visible.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_isvisible`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`mspp_publishingstate_mspp_isvisible`|
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

### <a name="BKMK_mspp_publishingstateId"></a> mspp_publishingstateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Publishing State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_publishingstateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Publishing State.**|
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
|Description|**Status of the Publishing State**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_publishingstate_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Publishing State**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_publishingstate_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_systemuser_mspp_publishingstate_createdby](#BKMK_mspp_systemuser_mspp_publishingstate_createdby)
- [mspp_systemuser_mspp_publishingstate_modifiedby](#BKMK_mspp_systemuser_mspp_publishingstate_modifiedby)
- [mspp_website_publishingstate](#BKMK_mspp_website_publishingstate)

### <a name="BKMK_mspp_systemuser_mspp_publishingstate_createdby"></a> mspp_systemuser_mspp_publishingstate_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_publishingstate_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstate_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_publishingstate_modifiedby"></a> mspp_systemuser_mspp_publishingstate_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_publishingstate_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_publishingstate_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_publishingstate"></a> mspp_website_publishingstate

One-To-Many Relationship: [mspp_website mspp_website_publishingstate](mspp_website.md#BKMK_mspp_website_publishingstate)

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

- [mspp_frompublishingstate_statetransition](#BKMK_mspp_frompublishingstate_statetransition)
- [mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState)
- [mspp_publishingstate_webfile](#BKMK_mspp_publishingstate_webfile)
- [mspp_publishingstate_weblink](#BKMK_mspp_publishingstate_weblink)
- [mspp_publishingstate_weblinkset](#BKMK_mspp_publishingstate_weblinkset)
- [mspp_publishingstate_webpage](#BKMK_mspp_publishingstate_webpage)
- [mspp_topublishingstate_statetransition](#BKMK_mspp_topublishingstate_statetransition)

### <a name="BKMK_mspp_frompublishingstate_statetransition"></a> mspp_frompublishingstate_statetransition

Many-To-One Relationship: [mspp_publishingstatetransitionrule mspp_frompublishingstate_statetransition](mspp_publishingstatetransitionrule.md#BKMK_mspp_frompublishingstate_statetransition)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_publishingstatetransitionrule`|
|ReferencingAttribute|`mspp_fromstate_publishingstateid`|
|ReferencedEntityNavigationPropertyName|`mspp_frompublishingstate_statetransition`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState"></a> mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState

Many-To-One Relationship: [mspp_websitelanguage mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState](mspp_websitelanguage.md#BKMK_mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_websitelanguage`|
|ReferencingAttribute|`mspp_publishingstate`|
|ReferencedEntityNavigationPropertyName|`mspp_mspp_publishingstate_mspp_websitelanguage_PublishingState`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstate_webfile"></a> mspp_publishingstate_webfile

Many-To-One Relationship: [mspp_webfile mspp_publishingstate_webfile](mspp_webfile.md#BKMK_mspp_publishingstate_webfile)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webfile`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstate_webfile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstate_weblink"></a> mspp_publishingstate_weblink

Many-To-One Relationship: [mspp_weblink mspp_publishingstate_weblink](mspp_weblink.md#BKMK_mspp_publishingstate_weblink)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblink`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstate_weblink`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstate_weblinkset"></a> mspp_publishingstate_weblinkset

Many-To-One Relationship: [mspp_weblinkset mspp_publishingstate_weblinkset](mspp_weblinkset.md#BKMK_mspp_publishingstate_weblinkset)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_weblinkset`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstate_weblinkset`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_publishingstate_webpage"></a> mspp_publishingstate_webpage

Many-To-One Relationship: [mspp_webpage mspp_publishingstate_webpage](mspp_webpage.md#BKMK_mspp_publishingstate_webpage)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_webpage`|
|ReferencingAttribute|`mspp_publishingstateid`|
|ReferencedEntityNavigationPropertyName|`mspp_publishingstate_webpage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_mspp_topublishingstate_statetransition"></a> mspp_topublishingstate_statetransition

Many-To-One Relationship: [mspp_publishingstatetransitionrule mspp_topublishingstate_statetransition](mspp_publishingstatetransitionrule.md#BKMK_mspp_topublishingstate_statetransition)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_publishingstatetransitionrule`|
|ReferencingAttribute|`mspp_tostate_publishingstateid`|
|ReferencedEntityNavigationPropertyName|`mspp_topublishingstate_statetransition`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_mspp_accesscontrolrule_publishingstate"></a> mspp_accesscontrolrule_publishingstate

See [mspp_webpageaccesscontrolrule mspp_accesscontrolrule_publishingstate Many-To-Many Relationship](mspp_webpageaccesscontrolrule.md#BKMK_mspp_accesscontrolrule_publishingstate)

|Property|Value|
|---|---|
|IntersectEntityName|`mspp_accesscontrolrule_publishingstate`|
|IsCustomizable|False|
|SchemaName|`mspp_accesscontrolrule_publishingstate`|
|IntersectAttribute|`mspp_publishingstateid`|
|NavigationPropertyName|`mspp_accesscontrolrule_publishingstate`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_publishingstate?displayProperty=fullName>
