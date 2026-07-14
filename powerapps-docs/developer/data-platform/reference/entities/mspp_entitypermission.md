---
title: "Table Permission (mspp_entitypermission) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Table Permission (mspp_entitypermission) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Table Permission (mspp_entitypermission) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Table Permission (mspp_entitypermission) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /mspp_entitypermissions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /mspp_entitypermissions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /mspp_entitypermissions(*mspp_entitypermissionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Table Permission (mspp_entitypermission) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Table Permission (mspp_entitypermission) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Table Permission** |
| **DisplayCollectionName** | **Table Permissions** |
| **SchemaName** | `mspp_entitypermission` |
| **CollectionSchemaName** | `mspp_entitypermissions` |
| **EntitySetName** | `mspp_entitypermissions`|
| **LogicalName** | `mspp_entitypermission` |
| **LogicalCollectionName** | `mspp_entitypermissions` |
| **PrimaryIdAttribute** | `mspp_entitypermissionid` |
| **PrimaryNameAttribute** |`mspp_entityname` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [mspp_accountrelationship](#BKMK_mspp_accountrelationship)
- [mspp_append](#BKMK_mspp_append)
- [mspp_appendto](#BKMK_mspp_appendto)
- [mspp_contactrelationship](#BKMK_mspp_contactrelationship)
- [mspp_create](#BKMK_mspp_create)
- [mspp_createdby](#BKMK_mspp_createdby)
- [mspp_createdon](#BKMK_mspp_createdon)
- [mspp_delete](#BKMK_mspp_delete)
- [mspp_entitylogicalname](#BKMK_mspp_entitylogicalname)
- [mspp_entityname](#BKMK_mspp_entityname)
- [mspp_entitypermissionId](#BKMK_mspp_entitypermissionId)
- [mspp_modifiedby](#BKMK_mspp_modifiedby)
- [mspp_modifiedon](#BKMK_mspp_modifiedon)
- [mspp_parententitypermission](#BKMK_mspp_parententitypermission)
- [mspp_parentrelationship](#BKMK_mspp_parentrelationship)
- [mspp_read](#BKMK_mspp_read)
- [mspp_scope](#BKMK_mspp_scope)
- [mspp_websiteid](#BKMK_mspp_websiteid)
- [mspp_write](#BKMK_mspp_write)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)

### <a name="BKMK_mspp_accountrelationship"></a> mspp_accountrelationship

|Property|Value|
|---|---|
|Description||
|DisplayName|**Account Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_accountrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_append"></a> mspp_append

|Property|Value|
|---|---|
|Description|**Controls whether the user can attach another record to the specified record. The Append and Append To permissions work in combination.**|
|DisplayName|**Append**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_append`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitypermission_mspp_append`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_appendto"></a> mspp_appendto

|Property|Value|
|---|---|
|Description|**Controls whether the user can append the specified record to another record. The Append and Append To permissions work in combination.**|
|DisplayName|**Append To**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_appendto`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitypermission_mspp_appendto`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_contactrelationship"></a> mspp_contactrelationship

|Property|Value|
|---|---|
|Description||
|DisplayName|**Contact Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_contactrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_mspp_create"></a> mspp_create

|Property|Value|
|---|---|
|Description|**The Create privilege controls whether you can create a record.**|
|DisplayName|**Create**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_create`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitypermission_mspp_create`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_mspp_delete"></a> mspp_delete

|Property|Value|
|---|---|
|Description|**Controls whether the user can delete a record.**|
|DisplayName|**Delete**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_delete`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitypermission_mspp_delete`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_entitylogicalname"></a> mspp_entitylogicalname

|Property|Value|
|---|---|
|Description||
|DisplayName|**Table Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entitylogicalname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_mspp_entityname"></a> mspp_entityname

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_entityname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_mspp_entitypermissionId"></a> mspp_entitypermissionId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Table Permission**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mspp_entitypermissionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_mspp_parententitypermission"></a> mspp_parententitypermission

|Property|Value|
|---|---|
|Description||
|DisplayName|**Parent Table Permission**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_parententitypermission`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|mspp_entitypermission|

### <a name="BKMK_mspp_parentrelationship"></a> mspp_parentrelationship

|Property|Value|
|---|---|
|Description||
|DisplayName|**Parent Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_parentrelationship`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_mspp_read"></a> mspp_read

|Property|Value|
|---|---|
|Description|**Controls whether the user can read a record.**|
|DisplayName|**Read**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_read`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitypermission_mspp_read`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_mspp_scope"></a> mspp_scope

|Property|Value|
|---|---|
|Description||
|DisplayName|**Access Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_scope`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`mspp_entitypermission_mspp_scope`|

#### mspp_scope Choices/Options

|Value|Label|
|---|---|
|756150000|**Global**|
|756150001|**Contact**|
|756150002|**Account**|
|756150003|**Parent**|
|756150004|**Self**|

### <a name="BKMK_mspp_websiteid"></a> mspp_websiteid

|Property|Value|
|---|---|
|Description|**Unique identifier for Website associated with Entity Permission**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_websiteid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|mspp_website|

### <a name="BKMK_mspp_write"></a> mspp_write

|Property|Value|
|---|---|
|Description|**Controls whether the user can update a record.**|
|DisplayName|**Write**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mspp_write`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`mspp_entitypermission_mspp_write`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Table Permission**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`mspp_entitypermission_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Table Permission**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`mspp_entitypermission_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [mspp_entitypermission_parententitypermission](#BKMK_mspp_entitypermission_parententitypermission-many-to-one)
- [mspp_systemuser_mspp_entitypermission_createdby](#BKMK_mspp_systemuser_mspp_entitypermission_createdby)
- [mspp_systemuser_mspp_entitypermission_modifiedby](#BKMK_mspp_systemuser_mspp_entitypermission_modifiedby)
- [mspp_website_mspp_entitypermission](#BKMK_mspp_website_mspp_entitypermission)

### <a name="BKMK_mspp_entitypermission_parententitypermission-many-to-one"></a> mspp_entitypermission_parententitypermission

One-To-Many Relationship: [mspp_entitypermission mspp_entitypermission_parententitypermission](#BKMK_mspp_entitypermission_parententitypermission-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`mspp_entitypermission`|
|ReferencedAttribute|`mspp_entitypermissionid`|
|ReferencingAttribute|`mspp_parententitypermission`|
|ReferencingEntityNavigationPropertyName|`mspp_parententitypermission`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_entitypermission_createdby"></a> mspp_systemuser_mspp_entitypermission_createdby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_entitypermission_createdby](systemuser.md#BKMK_mspp_systemuser_mspp_entitypermission_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_createdby`|
|ReferencingEntityNavigationPropertyName|`mspp_createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_systemuser_mspp_entitypermission_modifiedby"></a> mspp_systemuser_mspp_entitypermission_modifiedby

One-To-Many Relationship: [systemuser mspp_systemuser_mspp_entitypermission_modifiedby](systemuser.md#BKMK_mspp_systemuser_mspp_entitypermission_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`mspp_modifiedby`|
|ReferencingEntityNavigationPropertyName|`mspp_modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspp_website_mspp_entitypermission"></a> mspp_website_mspp_entitypermission

One-To-Many Relationship: [mspp_website mspp_website_mspp_entitypermission](mspp_website.md#BKMK_mspp_website_mspp_entitypermission)

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

### <a name="BKMK_mspp_entitypermission_parententitypermission-one-to-many"></a> mspp_entitypermission_parententitypermission

Many-To-One Relationship: [mspp_entitypermission mspp_entitypermission_parententitypermission](#BKMK_mspp_entitypermission_parententitypermission-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`mspp_entitypermission`|
|ReferencingAttribute|`mspp_parententitypermission`|
|ReferencedEntityNavigationPropertyName|`mspp_entitypermission_parententitypermission`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_mspp_entitypermission_webrole"></a> mspp_entitypermission_webrole

See [mspp_webrole mspp_entitypermission_webrole Many-To-Many Relationship](mspp_webrole.md#BKMK_mspp_entitypermission_webrole)

|Property|Value|
|---|---|
|IntersectEntityName|`mspp_entitypermission_webrole`|
|IsCustomizable|False|
|SchemaName|`mspp_entitypermission_webrole`|
|IntersectAttribute|`mspp_entitypermissionid`|
|NavigationPropertyName|`mspp_entitypermission_webrole`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mspp_entitypermission?displayProperty=fullName>
