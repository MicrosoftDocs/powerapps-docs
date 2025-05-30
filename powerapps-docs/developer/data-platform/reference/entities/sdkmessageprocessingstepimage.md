---
title: "Sdk Message Processing Step Image (SdkMessageProcessingStepImage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sdk Message Processing Step Image (SdkMessageProcessingStepImage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sdk Message Processing Step Image (SdkMessageProcessingStepImage) table/entity reference (Microsoft Dataverse)

Copy of an entity's attributes before or after the core system operation.

## Messages

The following table lists the messages for the Sdk Message Processing Step Image (SdkMessageProcessingStepImage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /sdkmessageprocessingstepimages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /sdkmessageprocessingstepimages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /sdkmessageprocessingstepimages(*sdkmessageprocessingstepimageid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Sdk Message Processing Step Image (SdkMessageProcessingStepImage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sdk Message Processing Step Image** |
| **DisplayCollectionName** | **Sdk Message Processing Step Images** |
| **SchemaName** | `SdkMessageProcessingStepImage` |
| **CollectionSchemaName** | `SdkMessageProcessingStepImages` |
| **EntitySetName** | `sdkmessageprocessingstepimages`|
| **LogicalName** | `sdkmessageprocessingstepimage` |
| **LogicalCollectionName** | `sdkmessageprocessingstepimages` |
| **PrimaryIdAttribute** | `sdkmessageprocessingstepimageid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

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
|---|---|
|Description|**Comma-separated list of attributes that are to be passed into the SDK message processing step image.**|
|DisplayName|**Attributes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the SDK message processing step image.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_EntityAlias"></a> EntityAlias

|Property|Value|
|---|---|
|Description|**Key name used to access the pre-image or post-image property bags in a step.**|
|DisplayName|**Entity Alias**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityalias`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_ImageType"></a> ImageType

|Property|Value|
|---|---|
|Description|**Type of image requested.**|
|DisplayName|**Image Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`imagetype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sdkmessageprocessingstepimage_imagetype`|

#### ImageType Choices/Options

|Value|Label|
|---|---|
|0|**PreImage**|
|1|**PostImage**|
|2|**Both**|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_MessagePropertyName"></a> MessagePropertyName

|Property|Value|
|---|---|
|Description|**Name of the property on the Request message.**|
|DisplayName|**Message Property Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`messagepropertyname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of SdkMessage processing step image.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_RelatedAttributeName"></a> RelatedAttributeName

|Property|Value|
|---|---|
|Description|**Name of the related entity.**|
|DisplayName|**Related Attribute Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relatedattributename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SdkMessageProcessingStepId"></a> SdkMessageProcessingStepId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step.**|
|DisplayName|**SDK Message Processing Step**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sdkmessageprocessingstep|

### <a name="BKMK_SdkMessageProcessingStepImageId"></a> SdkMessageProcessingStepImageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step image entity.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepimageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SdkMessageProcessingStepImageIdUnique](#BKMK_SdkMessageProcessingStepImageIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the SDK message processing step image.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the SDK message processing step image was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the sdkmessageprocessingstepimage.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|---|---|
|Description|**Customization level of the SDK message processing step image.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|-255|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the SDK message processing step.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the SDK message processing step was last modified.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who last modified the sdkmessageprocessingstepimage.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
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

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_SdkMessageProcessingStepImageIdUnique"></a> SdkMessageProcessingStepImageIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step image.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepimageidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Number that identifies a specific revision of the step image.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_sdkmessageprocessingstepimage](#BKMK_createdby_sdkmessageprocessingstepimage)
- [lk_sdkmessageprocessingstepimage_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby)
- [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby)
- [modifiedby_sdkmessageprocessingstepimage](#BKMK_modifiedby_sdkmessageprocessingstepimage)
- [organization_sdkmessageprocessingstepimage](#BKMK_organization_sdkmessageprocessingstepimage)
- [sdkmessageprocessingstepid_sdkmessageprocessingstepimage](#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage)

### <a name="BKMK_createdby_sdkmessageprocessingstepimage"></a> createdby_sdkmessageprocessingstepimage

One-To-Many Relationship: [systemuser createdby_sdkmessageprocessingstepimage](systemuser.md#BKMK_createdby_sdkmessageprocessingstepimage)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby"></a> lk_sdkmessageprocessingstepimage_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessageprocessingstepimage_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepimage_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessageprocessingstepimage_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_sdkmessageprocessingstepimage"></a> modifiedby_sdkmessageprocessingstepimage

One-To-Many Relationship: [systemuser modifiedby_sdkmessageprocessingstepimage](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstepimage)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sdkmessageprocessingstepimage"></a> organization_sdkmessageprocessingstepimage

One-To-Many Relationship: [organization organization_sdkmessageprocessingstepimage](organization.md#BKMK_organization_sdkmessageprocessingstepimage)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage"></a> sdkmessageprocessingstepid_sdkmessageprocessingstepimage

One-To-Many Relationship: [sdkmessageprocessingstep sdkmessageprocessingstepid_sdkmessageprocessingstepimage](sdkmessageprocessingstep.md#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessageprocessingstep`|
|ReferencedAttribute|`sdkmessageprocessingstepid`|
|ReferencingAttribute|`sdkmessageprocessingstepid`|
|ReferencingEntityNavigationPropertyName|`sdkmessageprocessingstepid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sdkmessageprocessingstepimage?displayProperty=fullName>
