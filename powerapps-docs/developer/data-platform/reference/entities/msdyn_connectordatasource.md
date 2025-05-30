---
title: "Virtual Connector Data Source (msdyn_connectordatasource) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Virtual Connector Data Source (msdyn_connectordatasource) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Virtual Connector Data Source (msdyn_connectordatasource) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Virtual Connector Data Source (msdyn_connectordatasource) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_connectordatasources<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_connectordatasources<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Virtual Connector Data Source (msdyn_connectordatasource) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Virtual Connector Data Source (msdyn_connectordatasource) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Virtual Connector Data Source** |
| **DisplayCollectionName** | **Virtual Connector Data Sources** |
| **SchemaName** | `msdyn_connectordatasource` |
| **CollectionSchemaName** | `msdyn_connectordatasources` |
| **EntitySetName** | `msdyn_connectordatasources`|
| **LogicalName** | `msdyn_connectordatasource` |
| **LogicalCollectionName** | `msdyn_connectordatasources` |
| **PrimaryIdAttribute** | `msdyn_connectordatasourceid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Virtual` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_appsenvironment](#BKMK_msdyn_appsenvironment)
- [msdyn_clientid](#BKMK_msdyn_clientid)
- [msdyn_clientsecret](#BKMK_msdyn_clientsecret)
- [msdyn_connectionreference](#BKMK_msdyn_connectionreference)
- [msdyn_ConnectionReferenceId](#BKMK_msdyn_ConnectionReferenceId)
- [msdyn_connectordatasourceId](#BKMK_msdyn_connectordatasourceId)
- [msdyn_connectortype](#BKMK_msdyn_connectortype)
- [msdyn_dataset_unresolvedvalue](#BKMK_msdyn_dataset_unresolvedvalue)
- [msdyn_dataset_value](#BKMK_msdyn_dataset_value)
- [msdyn_hasacling](#BKMK_msdyn_hasacling)
- [msdyn_host](#BKMK_msdyn_host)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_resource](#BKMK_msdyn_resource)
- [msdyn_tenant](#BKMK_msdyn_tenant)
- [msdyn_userauth](#BKMK_msdyn_userauth)

### <a name="BKMK_msdyn_appsenvironment"></a> msdyn_appsenvironment

|Property|Value|
|---|---|
|Description||
|DisplayName|**appsenvironment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_appsenvironment`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_clientid"></a> msdyn_clientid

|Property|Value|
|---|---|
|Description||
|DisplayName|**clientid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_clientid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_clientsecret"></a> msdyn_clientsecret

|Property|Value|
|---|---|
|Description||
|DisplayName|**clientsecret**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_clientsecret`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_connectionreference"></a> msdyn_connectionreference

|Property|Value|
|---|---|
|Description||
|DisplayName|**connectionreference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_connectionreference`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_ConnectionReferenceId"></a> msdyn_ConnectionReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for Connection Reference associated with ConnectorDataSource.**|
|DisplayName|**Connection Reference**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_connectionreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connectionreference|

### <a name="BKMK_msdyn_connectordatasourceId"></a> msdyn_connectordatasourceId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**ConnectorDataSource**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_connectordatasourceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_connectortype"></a> msdyn_connectortype

|Property|Value|
|---|---|
|Description||
|DisplayName|**Connector Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_connectortype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_dataset_unresolvedvalue"></a> msdyn_dataset_unresolvedvalue

|Property|Value|
|---|---|
|Description||
|DisplayName|**Dataset Unresolved Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_dataset_unresolvedvalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_dataset_value"></a> msdyn_dataset_value

|Property|Value|
|---|---|
|Description||
|DisplayName|**Dataset Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_dataset_value`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_hasacling"></a> msdyn_hasacling

|Property|Value|
|---|---|
|Description|**Boolean that indicates if the ACLing is done.**|
|DisplayName|**Has Acling**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_hasacling`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_connectordatasource_msdyn_hasacling`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_host"></a> msdyn_host

|Property|Value|
|---|---|
|Description||
|DisplayName|**host**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_host`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_resource"></a> msdyn_resource

|Property|Value|
|---|---|
|Description||
|DisplayName|**resource**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_resource`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_tenant"></a> msdyn_tenant

|Property|Value|
|---|---|
|Description||
|DisplayName|**tenant**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_tenant`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_userauth"></a> msdyn_userauth

|Property|Value|
|---|---|
|Description||
|DisplayName|**User authentication**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_userauth`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_connectordatasource_msdyn_userauth`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|


## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

### <a name="BKMK_msdyn_connreference_msdyn_connectordatasource"></a> msdyn_connreference_msdyn_connectordatasource

One-To-Many Relationship: [connectionreference msdyn_connreference_msdyn_connectordatasource](connectionreference.md#BKMK_msdyn_connreference_msdyn_connectordatasource)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`msdyn_connectionreferenceid`|
|ReferencingEntityNavigationPropertyName|`msdyn_ConnectionReferenceId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_msdyn_connectordatasource_environmentvariable"></a> msdyn_connectordatasource_environmentvariable

See [environmentvariabledefinition msdyn_connectordatasource_environmentvariable Many-To-Many Relationship](environmentvariabledefinition.md#BKMK_msdyn_connectordatasource_environmentvariable)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_connectordatasource_environmentva`|
|IsCustomizable|True|
|SchemaName|`msdyn_connectordatasource_environmentvariable`|
|IntersectAttribute|`msdyn_connectordatasourceid`|
|NavigationPropertyName|`msdyn_connectordatasource_environmentvari`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_connectordatasource?displayProperty=fullName>
