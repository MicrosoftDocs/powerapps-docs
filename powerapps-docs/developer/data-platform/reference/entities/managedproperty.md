---
title: "ManagedProperty table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ManagedProperty table/entity."
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

# ManagedProperty table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).




## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ManagedProperties|
|DisplayCollectionName|Managed Properties|
|DisplayName|Managed Property|
|EntitySetName|managedproperties|
|IsBPFEntity|False|
|LogicalCollectionName|managedproperties|
|LogicalName|managedproperty|
|OwnershipType|None|
|PrimaryIdAttribute|managedpropertyid|
|PrimaryNameAttribute|logicalname|
|SchemaName|ManagedProperty|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [EnablesAttributeName](#BKMK_EnablesAttributeName)
- [EnablesEntityName](#BKMK_EnablesEntityName)
- [LogicalName](#BKMK_LogicalName)
- [ManagedPropertyId](#BKMK_ManagedPropertyId)
- [ManagedPropertyRowId](#BKMK_ManagedPropertyRowId)


### <a name="BKMK_EnablesAttributeName"></a> EnablesAttributeName

|Property|Value|
|--------|-----|
|Description|Enables Attribute Name of this Managed Property.|
|DisplayName|Enables Atrribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|enablesattributename|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EnablesEntityName"></a> EnablesEntityName

|Property|Value|
|--------|-----|
|Description|Enables Entity Name of this Managed Property.|
|DisplayName|Enables Entity Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|enablesentityname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_LogicalName"></a> LogicalName

|Property|Value|
|--------|-----|
|Description|The logical name of this Managed Property.|
|DisplayName|Logical Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|logicalname|
|MaxLength|128|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ManagedPropertyId"></a> ManagedPropertyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the managed property key.|
|DisplayName|Managed Property Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|managedpropertyid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ManagedPropertyRowId"></a> ManagedPropertyRowId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the Managed Property|
|DisplayName|Managed Property Row Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|managedpropertyrowid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)


### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.managedproperty?text=managedproperty EntityType" />