---
title: "msdyn_nonrelationalds table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_nonrelationalds table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_nonrelationalds table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: NonRelational DataProvider Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /msdyn_nonrelationaldses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET /msdyn_nonrelationaldses<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_nonrelationaldses|
|DisplayCollectionName|NonRelational Data Source|
|DisplayName|NonRelational Data Source|
|EntitySetName|msdyn_nonrelationaldses|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_nonrelationaldses|
|LogicalName|msdyn_nonrelationalds|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_nonrelationaldsid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_nonrelationalds|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_nonrelationaldsId](#BKMK_msdyn_nonrelationaldsId)


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_nonrelationaldsId"></a> msdyn_nonrelationaldsId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|NonRelational Data Source|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_nonrelationaldsid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_nonrelationalds?text=msdyn_nonrelationalds EntityType" />