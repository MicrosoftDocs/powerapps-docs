---
title: "RuntimeDependency table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the RuntimeDependency table/entity."
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

# RuntimeDependency table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Form Level dependencies in CRM.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RuntimeDependencies|
|DisplayCollectionName|RuntimeDependencies|
|DisplayName|RuntimeDependency|
|EntitySetName|runtimedependencies|
|IsBPFEntity|False|
|LogicalCollectionName|runtimedependencies|
|LogicalName|runtimedependency|
|OwnershipType|None|
|PrimaryIdAttribute|dependencyid|
|PrimaryNameAttribute||
|SchemaName|RuntimeDependency|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [DependentComponentNodeId](#BKMK_DependentComponentNodeId)
- [DependentComponentType](#BKMK_DependentComponentType)
- [IsPublished](#BKMK_IsPublished)
- [RequiredComponentNodeId](#BKMK_RequiredComponentNodeId)
- [RequiredComponentType](#BKMK_RequiredComponentType)


### <a name="BKMK_DependentComponentNodeId"></a> DependentComponentNodeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the dependent component's node.|
|DisplayName|Dependent Component|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dependentcomponentnodeid|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_DependentComponentType"></a> DependentComponentType

|Property|Value|
|--------|-----|
|Description|Dependent Component Node Type|
|DisplayName|Dependent Component Node Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dependentcomponenttype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsPublished"></a> IsPublished

|Property|Value|
|--------|-----|
|Description|Determines whether required component is published|
|DisplayName|IsPublished|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ispublished|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_RequiredComponentNodeId"></a> RequiredComponentNodeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the required component's node|
|DisplayName|Required Component|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|requiredcomponentnodeid|
|MaxLength|300|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_RequiredComponentType"></a> RequiredComponentType

|Property|Value|
|--------|-----|
|Description|Required Component Node Type|
|DisplayName|Required Component Node Type|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|requiredcomponenttype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedTime](#BKMK_CreatedTime)
- [DependencyId](#BKMK_DependencyId)
- [RequiredComponentModifiedTime](#BKMK_RequiredComponentModifiedTime)


### <a name="BKMK_CreatedTime"></a> CreatedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_DependencyId"></a> DependencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of a dependency.|
|DisplayName|Dependency Identifier|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|dependencyid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_RequiredComponentModifiedTime"></a> RequiredComponentModifiedTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the required component was modified.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|requiredcomponentmodifiedtime|
|RequiredLevel|None|
|Type|DateTime|



### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.runtimedependency?text=runtimedependency EntityType" />