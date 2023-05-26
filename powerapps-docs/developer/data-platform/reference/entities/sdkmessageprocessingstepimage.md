---
title: "SdkMessageProcessingStepImage table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the SdkMessageProcessingStepImage table/entity."
ms.date: 05/23/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# SdkMessageProcessingStepImage table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Copy of an entity's attributes before or after the core system operation.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.2/sdkmessageprocessingstepimages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.2/sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.2/sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.2/sdkmessageprocessingstepimages<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.2/sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SdkMessageProcessingStepImages|
|DisplayCollectionName|Sdk Message Processing Step Images|
|DisplayName|Sdk Message Processing Step Image|
|EntitySetName|sdkmessageprocessingstepimages|
|IsBPFEntity|False|
|LogicalCollectionName|sdkmessageprocessingstepimages|
|LogicalName|sdkmessageprocessingstepimage|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|sdkmessageprocessingstepimageid|
|PrimaryNameAttribute|name|
|SchemaName|SdkMessageProcessingStepImage|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Attributes](#BKMK_Attributes)
- [Description](#BKMK_Description)
- [EntityAlias](#BKMK_EntityAlias)
- [ImageType](#BKMK_ImageType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [MessagePropertyName](#BKMK_MessagePropertyName)
- [Name](#BKMK_Name)
- [RelatedAttributeName](#BKMK_RelatedAttributeName)
- [SdkMessageProcessingStepId](#BKMK_SdkMessageProcessingStepId)
- [SdkMessageProcessingStepImageId](#BKMK_SdkMessageProcessingStepImageId)


### <a name="BKMK_Attributes"></a> Attributes

|Property|Value|
|--------|-----|
|Description|Comma-separated list of attributes that are to be passed into the SDK message processing step image.|
|DisplayName|Attributes|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|attributes|
|MaxLength|100000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the SDK message processing step image.|
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityAlias"></a> EntityAlias

|Property|Value|
|--------|-----|
|Description|Key name used to access the pre-image or post-image property bags in a step.|
|DisplayName|Entity Alias|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityalias|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ImageType"></a> ImageType

|Property|Value|
|--------|-----|
|Description|Type of image requested.|
|DisplayName|Image Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|imagetype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ImageType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|PreImage||
|1|PostImage||
|2|Both||



### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the form is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_MessagePropertyName"></a> MessagePropertyName

|Property|Value|
|--------|-----|
|Description|Name of the property on the Request message.|
|DisplayName|Message Property Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|messagepropertyname|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of SdkMessage processing step image.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|256|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_RelatedAttributeName"></a> RelatedAttributeName

|Property|Value|
|--------|-----|
|Description|Name of the related entity.|
|DisplayName|Related Attribute Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|relatedattributename|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SdkMessageProcessingStepId"></a> SdkMessageProcessingStepId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SDK message processing step.|
|DisplayName|SDK Message Processing Step|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sdkmessageprocessingstepid|
|RequiredLevel|None|
|Targets|sdkmessageprocessingstep|
|Type|Lookup|


### <a name="BKMK_SdkMessageProcessingStepImageId"></a> SdkMessageProcessingStepImageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SDK message processing step image entity.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|sdkmessageprocessingstepimageid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SdkMessageProcessingStepImageIdUnique](#BKMK_SdkMessageProcessingStepImageIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


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

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the SDK message processing step image.|
|DisplayName|Created By|
|IsValidForForm|False|
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
|Description|Date and time when the SDK message processing step image was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the sdkmessageprocessingstepimage.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|False|
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
|Description|Customization level of the SDK message processing step image.|
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|customizationlevel|
|MaxValue|255|
|MinValue|-255|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the SDK message processing step.|
|DisplayName|Modified By|
|IsValidForForm|False|
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
|DisplayName|Modified By|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the sdkmessageprocessingstepimage.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|False|
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


### <a name="BKMK_SdkMessageProcessingStepImageIdUnique"></a> SdkMessageProcessingStepImageIdUnique

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SDK message processing step image.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sdkmessageprocessingstepimageidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Number that identifies a specific revision of the step image. |
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_sdkmessageprocessingstepimage_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby)
- [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby)
- [sdkmessageprocessingstepid_sdkmessageprocessingstepimage](#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage)
- [createdby_sdkmessageprocessingstepimage](#BKMK_createdby_sdkmessageprocessingstepimage)
- [organization_sdkmessageprocessingstepimage](#BKMK_organization_sdkmessageprocessingstepimage)
- [modifiedby_sdkmessageprocessingstepimage](#BKMK_modifiedby_sdkmessageprocessingstepimage)


### <a name="BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby"></a> lk_sdkmessageprocessingstepimage_createdonbehalfby

See the [lk_sdkmessageprocessingstepimage_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepimage_modifiedonbehalfby

See the [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage"></a> sdkmessageprocessingstepid_sdkmessageprocessingstepimage

See the [sdkmessageprocessingstepid_sdkmessageprocessingstepimage](sdkmessageprocessingstep.md#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage) one-to-many relationship for the [sdkmessageprocessingstep](sdkmessageprocessingstep.md) table/entity.

### <a name="BKMK_createdby_sdkmessageprocessingstepimage"></a> createdby_sdkmessageprocessingstepimage

See the [createdby_sdkmessageprocessingstepimage](systemuser.md#BKMK_createdby_sdkmessageprocessingstepimage) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_sdkmessageprocessingstepimage"></a> organization_sdkmessageprocessingstepimage

See the [organization_sdkmessageprocessingstepimage](organization.md#BKMK_organization_sdkmessageprocessingstepimage) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_modifiedby_sdkmessageprocessingstepimage"></a> modifiedby_sdkmessageprocessingstepimage

See the [modifiedby_sdkmessageprocessingstepimage](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstepimage) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.sdkmessageprocessingstepimage?text=sdkmessageprocessingstepimage EntityType" />