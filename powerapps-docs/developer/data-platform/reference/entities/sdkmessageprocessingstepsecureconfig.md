---
title: "Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Sdk Message Processing Step Secure Configuration (SdkMessageProcessingStepSecureConfig)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Non-public custom configuration that is passed to a plug-in's constructor.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST /sdkmessageprocessingstepsecureconfigs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /sdkmessageprocessingstepsecureconfigs<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH /sdkmessageprocessingstepsecureconfigs(*sdkmessageprocessingstepsecureconfigid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SdkMessageProcessingStepSecureConfigs|
|DisplayCollectionName|Sdk Message Processing Step Secure Configurations|
|DisplayName|Sdk Message Processing Step Secure Configuration|
|EntitySetName|sdkmessageprocessingstepsecureconfigs|
|IsBPFEntity|False|
|LogicalCollectionName|sdkmessageprocessingstepsecureconfigs|
|LogicalName|sdkmessageprocessingstepsecureconfig|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|sdkmessageprocessingstepsecureconfigid|
|PrimaryNameAttribute||
|SchemaName|SdkMessageProcessingStepSecureConfig|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [SdkMessageProcessingStepSecureConfigId](#BKMK_SdkMessageProcessingStepSecureConfigId)
- [SecureConfig](#BKMK_SecureConfig)


### <a name="BKMK_SdkMessageProcessingStepSecureConfigId"></a> SdkMessageProcessingStepSecureConfigId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SDK message processing step secure configuration.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sdkmessageprocessingstepsecureconfigid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SecureConfig"></a> SecureConfig

|Property|Value|
|--------|-----|
|Description|Secure step-specific configuration for the plug-in type that is passed to the plug-in's constructor at run time.|
|DisplayName|Secure Configuration|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|secureconfig|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [SdkMessageProcessingStepSecureConfigIdUnique](#BKMK_SdkMessageProcessingStepSecureConfigIdUnique)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the SDK message processing step.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the SDK message processing step was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the sdkmessageprocessingstepsecureconfig.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|--------|-----|
|Description|Customization level of the SDK message processing step secure configuration.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|customizationlevel|
|MaxValue|255|
|MinValue|-255|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the SDK message processing step.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the SDK message processing step was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the sdkmessageprocessingstepsecureconfig.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization with which the SDK message processing step is associated.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_SdkMessageProcessingStepSecureConfigIdUnique"></a> SdkMessageProcessingStepSecureConfigIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SDK message processing step.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sdkmessageprocessingstepsecureconfigidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep"></a> sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep

Same as the [sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep) many-to-one relationship for the [sdkmessageprocessingstep](sdkmessageprocessingstep.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|sdkmessageprocessingstep|
|ReferencingAttribute|sdkmessageprocessingstepsecureconfigid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby)
- [modifiedby_sdkmessageprocessingstepsecureconfig](#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig)
- [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby)
- [organization_sdkmessageprocessingstepsecureconfig](#BKMK_organization_sdkmessageprocessingstepsecureconfig)
- [createdby_sdkmessageprocessingstepsecureconfig](#BKMK_createdby_sdkmessageprocessingstepsecureconfig)


### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby

See the [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_modifiedby_sdkmessageprocessingstepsecureconfig"></a> modifiedby_sdkmessageprocessingstepsecureconfig

See the [modifiedby_sdkmessageprocessingstepsecureconfig](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby

See the [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_sdkmessageprocessingstepsecureconfig"></a> organization_sdkmessageprocessingstepsecureconfig

See the [organization_sdkmessageprocessingstepsecureconfig](organization.md#BKMK_organization_sdkmessageprocessingstepsecureconfig) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_createdby_sdkmessageprocessingstepsecureconfig"></a> createdby_sdkmessageprocessingstepsecureconfig

See the [createdby_sdkmessageprocessingstepsecureconfig](systemuser.md#BKMK_createdby_sdkmessageprocessingstepsecureconfig) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.sdkmessageprocessingstepsecureconfig?text=sdkmessageprocessingstepsecureconfig EntityType" />