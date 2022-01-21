---
title: "msdyn_solutioncomponentcountsummary table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_solutioncomponentcountsummary table/entity."
ms.date: 10/05/2021
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

# msdyn_solutioncomponentcountsummary table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Microsoft Dynamics 365 Settings APIs Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_solutioncomponentcountsummaries<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_solutioncomponentcountsummaries<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_solutioncomponentcountsummaries(*msdyn_solutioncomponentcountsummaryid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_solutioncomponentcountsummaries|
|DisplayCollectionName|Solution Component Count Summaries|
|DisplayName|Solution Component Count Summary|
|EntitySetName|msdyn_solutioncomponentcountsummaries|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_solutioncomponentcountsummaries|
|LogicalName|msdyn_solutioncomponentcountsummary|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|msdyn_solutioncomponentcountsummaryid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_solutioncomponentcountsummary|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [msdyn_componentlogicalname](#BKMK_msdyn_componentlogicalname)
- [msdyn_componenttype](#BKMK_msdyn_componenttype)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_solutioncomponentcountsummaryId](#BKMK_msdyn_solutioncomponentcountsummaryId)
- [msdyn_solutionid](#BKMK_msdyn_solutionid)
- [msdyn_subtype](#BKMK_msdyn_subtype)
- [msdyn_total](#BKMK_msdyn_total)
- [msdyn_workflowcategory](#BKMK_msdyn_workflowcategory)


### <a name="BKMK_msdyn_componentlogicalname"></a> msdyn_componentlogicalname

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componentlogicalname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_componenttype"></a> msdyn_componenttype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_componenttype|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componenttype|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|msdyn_name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_solutioncomponentcountsummaryId"></a> msdyn_solutioncomponentcountsummaryId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|SolutionComponentCountSummary|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_solutioncomponentcountsummaryid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_solutionid"></a> msdyn_solutionid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_solutionid|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_solutionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_subtype"></a> msdyn_subtype

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_subtype|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_subtype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_total"></a> msdyn_total

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_total|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_total|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_msdyn_workflowcategory"></a> msdyn_workflowcategory

|Property|Value|
|--------|-----|
|Description||
|DisplayName|msdyn_workflowcategory|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_workflowcategory|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets||
|Type|Lookup|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_solutioncomponentcountsummary?text=msdyn_solutioncomponentcountsummary EntityType" />