---
title: "Language Provisioning State (LanguageProvisioningState) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Language Provisioning State (LanguageProvisioningState) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Language Provisioning State (LanguageProvisioningState) table/entity reference (Microsoft Dataverse)

Container for language provisioning checkpoint states

## Messages

The following table lists the messages for the Language Provisioning State (LanguageProvisioningState) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Language Provisioning State (LanguageProvisioningState) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Language Provisioning State** |
| **DisplayCollectionName** | **Language Provisioning States** |
| **SchemaName** | `LanguageProvisioningState` |
| **CollectionSchemaName** | `LanguageProvisioningStates` |
| **EntitySetName** | `languageprovisioningstates`|
| **LogicalName** | `languageprovisioningstate` |
| **LogicalCollectionName** | `languageprovisioningstates` |
| **PrimaryIdAttribute** | `languageprovisioningstateid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Application Version**|
|DisplayName|**Application Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicationversion`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_LanguageId"></a> LanguageId

|Property|Value|
|---|---|
|Description|**Language Id**|
|DisplayName|**Language Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languageid`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|100000|
|MinValue|0|

### <a name="BKMK_LanguageProvisioningStateId"></a> LanguageProvisioningStateId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Language Provisioning State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`languageprovisioningstateid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ProvisioningStage"></a> ProvisioningStage

|Property|Value|
|---|---|
|Description|**Provisioning Stage**|
|DisplayName|**Provisioning Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`provisioningstage`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`languageprovisioningstates_provisioningstage`|

#### ProvisioningStage Choices/Options

|Value|Label|
|---|---|
|1|**FileBased**|
|2|**MetadataHelperDependent**|
|3|**SystemOnly**|
|4|**Other**|
|5|**Ribbon**|

### <a name="BKMK_SolutionFileVersion"></a> SolutionFileVersion

|Property|Value|
|---|---|
|Description|**Solution File Version**|
|DisplayName|**Solution File Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionfileversion`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SolutionUniqueName"></a> SolutionUniqueName

|Property|Value|
|---|---|
|Description|**Solution Unique Name**|
|DisplayName|**Solution Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutionuniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_languageprovisioningstate_DeletedItemReferences"></a> languageprovisioningstate_DeletedItemReferences

Many-To-One Relationship: [deleteditemreference languageprovisioningstate_DeletedItemReferences](deleteditemreference.md#BKMK_languageprovisioningstate_DeletedItemReferences)

|Property|Value|
|---|---|
|ReferencingEntity|`deleteditemreference`|
|ReferencingAttribute|`deletedobject`|
|ReferencedEntityNavigationPropertyName|`languageprovisioningstate_DeletedItemReferences`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.languageprovisioningstate?displayProperty=fullName>
