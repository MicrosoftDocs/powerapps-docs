---
title: "Image Attribute Configuration (AttributeImageConfig) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Image Attribute Configuration (AttributeImageConfig) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Image Attribute Configuration (AttributeImageConfig) table/entity reference (Microsoft Dataverse)

Store configuration for each image attribute

## Messages

The following table lists the messages for the Image Attribute Configuration (AttributeImageConfig) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /attributeimageconfigs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /attributeimageconfigs(*attributeimageconfigid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /attributeimageconfigs(*attributeimageconfigid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /attributeimageconfigs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /attributeimageconfigs(*attributeimageconfigid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /attributeimageconfigs(*attributeimageconfigid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Image Attribute Configuration (AttributeImageConfig) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Image Attribute Configuration** |
| **DisplayCollectionName** | **Image Attribute Configurations** |
| **SchemaName** | `AttributeImageConfig` |
| **CollectionSchemaName** | `AttributeImageConfigs` |
| **EntitySetName** | `attributeimageconfigs`|
| **LogicalName** | `attributeimageconfig` |
| **LogicalCollectionName** | `attributeimageconfigs` |
| **PrimaryIdAttribute** | `attributeimageconfigid` |
| **PrimaryNameAttribute** |`attributelogicalname` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeImageConfigId](#BKMK_AttributeImageConfigId)
- [AttributeLogicalName](#BKMK_AttributeLogicalName)
- [CanStoreFullImage](#BKMK_CanStoreFullImage)
- [ParentEntityLogicalName](#BKMK_ParentEntityLogicalName)

### <a name="BKMK_AttributeImageConfigId"></a> AttributeImageConfigId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Image Attribute Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attributeimageconfigid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AttributeLogicalName"></a> AttributeLogicalName

|Property|Value|
|---|---|
|Description|**Logical Name of Image Attribute**|
|DisplayName|**Logical Name of Image Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributelogicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_CanStoreFullImage"></a> CanStoreFullImage

|Property|Value|
|---|---|
|Description|**Indicates if an image attribute can store full image**|
|DisplayName|**Can Store Full Image**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canstorefullimage`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`attributeimageconfig_canstorefullimage`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ParentEntityLogicalName"></a> ParentEntityLogicalName

|Property|Value|
|---|---|
|Description|**Parent Entity Logical Name**|
|DisplayName|**Parent Entity Logical Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parententitylogicalname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|DefaultFormValue||
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|Description|**Version number of Image Attribute Configuration.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [attributeimageconfig_AsyncOperations](#BKMK_attributeimageconfig_AsyncOperations)
- [attributeimageconfig_BulkDeleteFailures](#BKMK_attributeimageconfig_BulkDeleteFailures)
- [attributeimageconfig_MailboxTrackingFolders](#BKMK_attributeimageconfig_MailboxTrackingFolders)
- [attributeimageconfig_PrincipalObjectAttributeAccesses](#BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses)
- [attributeimageconfig_SyncErrors](#BKMK_attributeimageconfig_SyncErrors)

### <a name="BKMK_attributeimageconfig_AsyncOperations"></a> attributeimageconfig_AsyncOperations

Many-To-One Relationship: [asyncoperation attributeimageconfig_AsyncOperations](asyncoperation.md#BKMK_attributeimageconfig_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributeimageconfig_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributeimageconfig_BulkDeleteFailures"></a> attributeimageconfig_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure attributeimageconfig_BulkDeleteFailures](bulkdeletefailure.md#BKMK_attributeimageconfig_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributeimageconfig_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributeimageconfig_MailboxTrackingFolders"></a> attributeimageconfig_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder attributeimageconfig_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_attributeimageconfig_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributeimageconfig_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses"></a> attributeimageconfig_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess attributeimageconfig_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_attributeimageconfig_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`attributeimageconfig_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_attributeimageconfig_SyncErrors"></a> attributeimageconfig_SyncErrors

Many-To-One Relationship: [syncerror attributeimageconfig_SyncErrors](syncerror.md#BKMK_attributeimageconfig_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`attributeimageconfig_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.attributeimageconfig?displayProperty=fullName>
