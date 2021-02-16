---
title: "msdyn_solutionhistorydatasource entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_solutionhistorydatasource table."
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
# msdyn_solutionhistorydatasource entity reference

> [!NOTE]
> Effective Nov 2020, Common Data Service has been renamed to [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro).



**Added by**: Microsoft Dynamics 365 Solution History APIs Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources(*msdyn_solutionhistorydatasourceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources(*msdyn_solutionhistorydatasourceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources(*msdyn_solutionhistorydatasourceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_solutionhistorydatasources|
|DisplayCollectionName|Solution History Data Sources|
|DisplayName|Solution History Data Source|
|EntitySetName|msdyn_solutionhistorydatasources|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_solutionhistorydatasources|
|LogicalName|msdyn_solutionhistorydatasource|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_solutionhistorydatasourceid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_solutionhistorydatasource|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_solutionhistorydatasourceId](#BKMK_msdyn_solutionhistorydatasourceId)


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_solutionhistorydatasourceId"></a> msdyn_solutionhistorydatasourceId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Solution History Data Source|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_solutionhistorydatasourceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|



### See also

[About entity reference](../about-entity-reference.md)<br />
[Web API reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_solutionhistorydatasource?text=msdyn_solutionhistorydatasource EntityType" />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]