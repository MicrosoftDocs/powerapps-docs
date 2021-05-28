---
title: "LanguageProvisioningState table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the LanguageProvisioningState table/entity."
ms.date: 03/04/2021
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

# LanguageProvisioningState table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Container for language provisioning checkpoint states


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|LanguageProvisioningStates|
|DisplayCollectionName|Language Provisioning States|
|DisplayName|Language Provisioning State|
|EntitySetName|languageprovisioningstates|
|IsBPFEntity|False|
|LogicalCollectionName|languageprovisioningstates|
|LogicalName|languageprovisioningstate|
|OwnershipType|None|
|PrimaryIdAttribute|languageprovisioningstateid|
|PrimaryNameAttribute||
|SchemaName|LanguageProvisioningState|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicationVersion](#BKMK_ApplicationVersion)
- [LanguageId](#BKMK_LanguageId)
- [LanguageProvisioningStateId](#BKMK_LanguageProvisioningStateId)
- [ProvisioningStage](#BKMK_ProvisioningStage)
- [SolutionFileVersion](#BKMK_SolutionFileVersion)
- [SolutionUniqueName](#BKMK_SolutionUniqueName)


### <a name="BKMK_ApplicationVersion"></a> ApplicationVersion

|Property|Value|
|--------|-----|
|Description|Application Version|
|DisplayName|Application Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|applicationversion|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_LanguageId"></a> LanguageId

|Property|Value|
|--------|-----|
|Description|Language Id|
|DisplayName|Language Id|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|languageid|
|MaxValue|100000|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_LanguageProvisioningStateId"></a> LanguageProvisioningStateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Language Provisioning State|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|languageprovisioningstateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ProvisioningStage"></a> ProvisioningStage

|Property|Value|
|--------|-----|
|Description|Provisioning Stage|
|DisplayName|Provisioning Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|provisioningstage|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ProvisioningStage Choices/Options

|Value|Label|
|-----|-----|
|1|FileBased|
|2|MetadataHelperDependent|
|3|SystemOnly|
|4|Other|
|5|Ribbon|



### <a name="BKMK_SolutionFileVersion"></a> SolutionFileVersion

|Property|Value|
|--------|-----|
|Description|Solution File Version|
|DisplayName|Solution File Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutionfileversion|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_SolutionUniqueName"></a> SolutionUniqueName

|Property|Value|
|--------|-----|
|Description|Solution Unique Name|
|DisplayName|Solution Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|solutionuniquename|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.languageprovisioningstate?text=languageprovisioningstate EntityType" />