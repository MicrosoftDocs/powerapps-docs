---
title: "msdyn_nonrelationalds entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_nonrelationalds table."
ms.date: 11/14/2020
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# msdyn_nonrelationalds entity reference

> [!NOTE]
> Effective Nov 2020, Common Data Service has been renamed to [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro).



**Added by**: NonRelational DataProvider Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_nonrelationaldses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_nonrelationaldses<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_nonrelationaldses(*msdyn_nonrelationaldsid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity properties

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

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

[About entity reference](../about-entity-reference.md)<br />
[Web API reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_nonrelationalds?text=msdyn_nonrelationalds EntityType" />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]