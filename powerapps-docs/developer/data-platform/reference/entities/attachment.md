---
title: "Attachment table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Attachment table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Attachment table/entity reference (Microsoft Dataverse)

Attachment for an email activity.

## Messages

The following table lists the messages for the Attachment table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|

## Properties

The following table lists selected properties for the Attachment table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Attachment** |
| **DisplayCollectionName** | **Attachments** |
| **SchemaName** | `Attachment` |
| **CollectionSchemaName** | `Attachments` |
| **EntitySetName** | `attachments`|
| **LogicalName** | `attachment` |
| **LogicalCollectionName** | `attachments` |
| **PrimaryIdAttribute** | `attachmentid` |
| **PrimaryNameAttribute** |`filename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttachmentId](#BKMK_AttachmentId)
- [Body](#BKMK_Body)
- [FileName](#BKMK_FileName)
- [MimeType](#BKMK_MimeType)
- [Subject](#BKMK_Subject)

### <a name="BKMK_AttachmentId"></a> AttachmentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the attachment.**|
|DisplayName|**Attachment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Body"></a> Body

|Property|Value|
|---|---|
|Description|**Contents of the attachment.**|
|DisplayName|**Body**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`body`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_FileName"></a> FileName

|Property|Value|
|---|---|
|Description|**File name of the attachment.**|
|DisplayName|**File Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|---|---|
|Description|**MIME type of the attachment.**|
|DisplayName|**MIME Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mimetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|---|---|
|Description|**Subject associated with the attachment.**|
|DisplayName|**Subject**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subject`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [FilePointer](#BKMK_FilePointer)
- [FileSize](#BKMK_FileSize)
- [Prefix](#BKMK_Prefix)
- [StoragePointer](#BKMK_StoragePointer)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_FilePointer"></a> FilePointer

|Property|Value|
|---|---|
|Description|**File pointer of the attachment.**|
|DisplayName|**File Pointer**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`filepointer`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|

### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|---|---|
|Description|**File size of the attachment.**|
|DisplayName|**File Size (Bytes)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filesize`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_Prefix"></a> Prefix

|Property|Value|
|---|---|
|Description|**Prefix of the file pointer in blob storage.**|
|DisplayName|**Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`prefix`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_StoragePointer"></a> StoragePointer

|Property|Value|
|---|---|
|Description|**Storage pointer.**|
|DisplayName|**Storage Pointer**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`storagepointer`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the attachment.**|
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

- [attachment_activity_mime_attachments](#BKMK_attachment_activity_mime_attachments)
- [Attachment_SyncErrors](#BKMK_Attachment_SyncErrors)

### <a name="BKMK_attachment_activity_mime_attachments"></a> attachment_activity_mime_attachments

Many-To-One Relationship: [activitymimeattachment attachment_activity_mime_attachments](activitymimeattachment.md#BKMK_attachment_activity_mime_attachments)

|Property|Value|
|---|---|
|ReferencingEntity|`activitymimeattachment`|
|ReferencingAttribute|`attachmentid`|
|ReferencedEntityNavigationPropertyName|`attachment_activity_mime_attachments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Attachment_SyncErrors"></a> Attachment_SyncErrors

Many-To-One Relationship: [syncerror Attachment_SyncErrors](syncerror.md#BKMK_Attachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Attachment_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.attachment?displayProperty=fullName>
