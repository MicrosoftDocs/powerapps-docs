---
title: "msdyn_solutionhistorydatasource Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_solutionhistorydatasource entity."
ms.date: 04/12/2020
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# msdyn_solutionhistorydatasource Entity Reference



**Added by**: Microsoft Dynamics 365 Solution History APIs Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple|<xref href="Microsoft.Dynamics.CRM.CreateMultiple?text=CreateMultiple Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources(*msdyn_solutionhistorydatasourceid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources(*msdyn_solutionhistorydatasourceid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_solutionhistorydatasources(*msdyn_solutionhistorydatasourceid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple|<xref href="Microsoft.Dynamics.CRM.UpdateMultiple?text=UpdateMultiple Action" />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Entity Properties

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

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_msdyn_solutionhistorydatasource_Annotations"></a> msdyn_solutionhistorydatasource_Annotations

**Added by**: System Solution Solution

Same as annotation entity [msdyn_solutionhistorydatasource_Annotations](annotation.md#BKMK_msdyn_solutionhistorydatasource_Annotations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhistorydatasource_Annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_solutionhistorydatasource?text=msdyn_solutionhistorydatasource EntityType" />