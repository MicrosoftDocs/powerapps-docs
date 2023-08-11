---
title: "msdyn_connectordatasource table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_connectordatasource table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_connectordatasource table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Virtual Connector Provider Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msdyn_connectordatasources<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /msdyn_connectordatasources<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Update|PATCH /msdyn_connectordatasources(*msdyn_connectordatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_connectordatasources|
|DisplayCollectionName|Virtual Connector Data Sources|
|DisplayName|Virtual Connector Data Source|
|EntitySetName|msdyn_connectordatasources|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_connectordatasources|
|LogicalName|msdyn_connectordatasource|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_connectordatasourceid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_connectordatasource|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_appsenvironment](#BKMK_msdyn_appsenvironment)
- [msdyn_clientid](#BKMK_msdyn_clientid)
- [msdyn_clientsecret](#BKMK_msdyn_clientsecret)
- [msdyn_connectionreference](#BKMK_msdyn_connectionreference)
- [msdyn_ConnectionReferenceId](#BKMK_msdyn_ConnectionReferenceId)
- [msdyn_connectordatasourceId](#BKMK_msdyn_connectordatasourceId)
- [msdyn_connectortype](#BKMK_msdyn_connectortype)
- [msdyn_dataset_value](#BKMK_msdyn_dataset_value)
- [msdyn_host](#BKMK_msdyn_host)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_resource](#BKMK_msdyn_resource)
- [msdyn_tenant](#BKMK_msdyn_tenant)
- [msdyn_userauth](#BKMK_msdyn_userauth)


### <a name="BKMK_msdyn_appsenvironment"></a> msdyn_appsenvironment

|Property|Value|
|--------|-----|
|Description||
|DisplayName|appsenvironment|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_appsenvironment|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_clientid"></a> msdyn_clientid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|clientid|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_clientid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_clientsecret"></a> msdyn_clientsecret

|Property|Value|
|--------|-----|
|Description||
|DisplayName|clientsecret|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_clientsecret|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_connectionreference"></a> msdyn_connectionreference

|Property|Value|
|--------|-----|
|Description||
|DisplayName|connectionreference|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_connectionreference|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ConnectionReferenceId"></a> msdyn_ConnectionReferenceId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Connection Reference associated with ConnectorDataSource.|
|DisplayName|Connection Reference|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_connectionreferenceid|
|RequiredLevel|None|
|Targets|connectionreference|
|Type|Lookup|


### <a name="BKMK_msdyn_connectordatasourceId"></a> msdyn_connectordatasourceId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|ConnectorDataSource|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_connectordatasourceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_connectortype"></a> msdyn_connectortype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Connector Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_connectortype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_dataset_value"></a> msdyn_dataset_value

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Dataset Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_dataset_value|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_host"></a> msdyn_host

|Property|Value|
|--------|-----|
|Description||
|DisplayName|host|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_host|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_resource"></a> msdyn_resource

|Property|Value|
|--------|-----|
|Description||
|DisplayName|resource|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resource|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_tenant"></a> msdyn_tenant

|Property|Value|
|--------|-----|
|Description||
|DisplayName|tenant|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_tenant|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_userauth"></a> msdyn_userauth

|Property|Value|
|--------|-----|
|Description||
|DisplayName|User authentication|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_userauth|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_userauth Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


### <a name="BKMK_msdyn_ConnectionReferenceIdName"></a> msdyn_ConnectionReferenceIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_connectionreferenceidname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.


### <a name="BKMK_msdyn_connreference_msdyn_connectordatasource"></a> msdyn_connreference_msdyn_connectordatasource

**Added by**: Power Platform Connection References Solution

See the [msdyn_connreference_msdyn_connectordatasource](connectionreference.md#BKMK_msdyn_connreference_msdyn_connectordatasource) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_connectordatasource?text=msdyn_connectordatasource EntityType" />