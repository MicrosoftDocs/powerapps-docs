---
title: "Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig) table/entity reference (Microsoft Dataverse)

Non-public custom configuration that is passed to a plug-in's constructor.

## Messages

The following table lists the messages for the Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /sdkmessageprocessingstepsecureconfigs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /sdkmessageprocessingstepsecureconfigs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sdk Message Processing Step Secure Configuration** |
| **DisplayCollectionName** | **Sdk Message Processing Step Secure Configurations** |
| **SchemaName** | `SdkMessageProcessingStepSecureConfig` |
| **CollectionSchemaName** | `SdkMessageProcessingStepSecureConfigs` |
| **EntitySetName** | `sdkmessageprocessingstepsecureconfigs`|
| **LogicalName** | `sdkmessageprocessingstepsecureconfig` |
| **LogicalCollectionName** | `sdkmessageprocessingstepsecureconfigs` |
| **PrimaryIdAttribute** | `sdkmessageprocessingstepsecureconfigid` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [SdkMessageProcessingStepSecureConfigId](#BKMK_SdkMessageProcessingStepSecureConfigId)
- [SecureConfig](#BKMK_SecureConfig)

### <a name="BKMK_SdkMessageProcessingStepSecureConfigId"></a> SdkMessageProcessingStepSecureConfigId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step secure configuration.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepsecureconfigid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SecureConfig"></a> SecureConfig

|Property|Value|
|---|---|
|Description|**Secure step-specific configuration for the plug-in type that is passed to the plug-in's constructor at run time.**|
|DisplayName|**Secure Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`secureconfig`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [SdkMessageProcessingStepSecureConfigIdUnique](#BKMK_SdkMessageProcessingStepSecureConfigIdUnique)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the SDK message processing step.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the SDK message processing step was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the sdkmessageprocessingstepsecureconfig.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|---|---|
|Description|**Customization level of the SDK message processing step secure configuration.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|-255|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the SDK message processing step.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the SDK message processing step was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the sdkmessageprocessingstepsecureconfig.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the SDK message processing step is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_SdkMessageProcessingStepSecureConfigIdUnique"></a> SdkMessageProcessingStepSecureConfigIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepsecureconfigidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_sdkmessageprocessingstepsecureconfig](#BKMK_createdby_sdkmessageprocessingstepsecureconfig)
- [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby)
- [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby)
- [modifiedby_sdkmessageprocessingstepsecureconfig](#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig)
- [organization_sdkmessageprocessingstepsecureconfig](#BKMK_organization_sdkmessageprocessingstepsecureconfig)

### <a name="BKMK_createdby_sdkmessageprocessingstepsecureconfig"></a> createdby_sdkmessageprocessingstepsecureconfig

One-To-Many Relationship: [systemuser createdby_sdkmessageprocessingstepsecureconfig](systemuser.md#BKMK_createdby_sdkmessageprocessingstepsecureconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_sdkmessageprocessingstepsecureconfig"></a> modifiedby_sdkmessageprocessingstepsecureconfig

One-To-Many Relationship: [systemuser modifiedby_sdkmessageprocessingstepsecureconfig](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sdkmessageprocessingstepsecureconfig"></a> organization_sdkmessageprocessingstepsecureconfig

One-To-Many Relationship: [organization organization_sdkmessageprocessingstepsecureconfig](organization.md#BKMK_organization_sdkmessageprocessingstepsecureconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep"></a> sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`sdkmessageprocessingstepsecureconfigid`|
|ReferencedEntityNavigationPropertyName|`sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sdkmessageprocessingstepsecureconfig?displayProperty=fullName>
