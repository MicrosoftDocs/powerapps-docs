---
title: "msdyn_datalakeds table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_datalakeds table/entity."
ms.date: 05/23/2022
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# msdyn_datalakeds table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Insights Store Data Provider Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_datalakedses<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_datalakedses(*msdyn_datalakedsid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_datalakedses(*msdyn_datalakedsid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_datalakedses<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_datalakedses(*msdyn_datalakedsid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_datalakedses|
|DisplayCollectionName|Insights Store Data Source|
|DisplayName|Insights Store Data Source|
|EntitySetName|msdyn_datalakedses|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_datalakedses|
|LogicalName|msdyn_datalakeds|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_datalakedsid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_datalakeds|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_datalakedsId](#BKMK_msdyn_datalakedsId)
- [msdyn_name](#BKMK_msdyn_name)


### <a name="BKMK_msdyn_datalakedsId"></a> msdyn_datalakedsId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Insights Store Data Source Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_datalakedsid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_datalakeds?text=msdyn_datalakeds EntityType" />