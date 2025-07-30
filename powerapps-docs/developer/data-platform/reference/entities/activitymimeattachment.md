---
title: "Attachment (ActivityMimeAttachment) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Attachment (ActivityMimeAttachment) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Attachment (ActivityMimeAttachment) table/entity reference (Microsoft Dataverse)

MIME attachment for an activity.

## Messages

The following table lists the messages for the Attachment (ActivityMimeAttachment) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /activitymimeattachments<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /activitymimeattachments(*activitymimeattachmentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /activitymimeattachments(*activitymimeattachmentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /activitymimeattachments<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /activitymimeattachments(*activitymimeattachmentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /activitymimeattachments(*activitymimeattachmentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Attachment (ActivityMimeAttachment) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Attachment** |
| **DisplayCollectionName** | **Attachments** |
| **SchemaName** | `ActivityMimeAttachment` |
| **CollectionSchemaName** | `ActivityMimeAttachments` |
| **EntitySetName** | `activitymimeattachments`|
| **LogicalName** | `activitymimeattachment` |
| **LogicalCollectionName** | `activitymimeattachments` |
| **PrimaryIdAttribute** | `activitymimeattachmentid` |
| **PrimaryNameAttribute** |`filename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityId](#BKMK_ActivityId)
- [ActivityMimeAttachmentId](#BKMK_ActivityMimeAttachmentId)
- [ActivityMimeAttachmentIdUnique](#BKMK_ActivityMimeAttachmentIdUnique)
- [AttachmentContentId](#BKMK_AttachmentContentId)
- [AttachmentId](#BKMK_AttachmentId)
- [AttachmentNumber](#BKMK_AttachmentNumber)
- [Body](#BKMK_Body)
- [FileName](#BKMK_FileName)
- [MimeType](#BKMK_MimeType)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [Subject](#BKMK_Subject)

### <a name="BKMK_ActivityId"></a> ActivityId

|Property|Value|
|---|---|
|Description|**Unique identifier of the activity with which the attachment is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|activitypointer|

### <a name="BKMK_ActivityMimeAttachmentId"></a> ActivityMimeAttachmentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the attachment.**|
|DisplayName|**Activity Mime Attachment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitymimeattachmentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ActivityMimeAttachmentIdUnique"></a> ActivityMimeAttachmentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitymimeattachmentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_AttachmentContentId"></a> AttachmentContentId

|Property|Value|
|---|---|
|Description|**For internal use only**|
|DisplayName|**Content Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentcontentid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_AttachmentId"></a> AttachmentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the attachment with which this activitymimeattachment is associated.**|
|DisplayName|**Attachment**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|attachment|

### <a name="BKMK_AttachmentNumber"></a> AttachmentNumber

|Property|Value|
|---|---|
|Description|**Number of the attachment.**|
|DisplayName|**Attachment Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`attachmentnumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

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
|DisplayName|**Mime Type**|
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

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the record with which the attachment is associated**|
|DisplayName|**Item**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|activitypointer, template|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Object Type Code of the entity that is associated with the attachment.**|
|DisplayName|**Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|---|---|
|Description|**Descriptive subject for the attachment.**|
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

- [ActivitySubject](#BKMK_ActivitySubject)
- [AnonymousLink](#BKMK_AnonymousLink)
- [ComponentState](#BKMK_ComponentState)
- [FileSize](#BKMK_FileSize)
- [IsFollowed](#BKMK_IsFollowed)
- [IsManaged](#BKMK_IsManaged)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ActivitySubject"></a> ActivitySubject

|Property|Value|
|---|---|
|Description|**Descriptive subject for the activity.**|
|DisplayName|**ActivitySubject**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`activitysubject`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_AnonymousLink"></a> AnonymousLink

|Property|Value|
|---|---|
|Description|**anonymous link**|
|DisplayName|**For internal use only.**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`anonymouslink`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

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

### <a name="BKMK_IsFollowed"></a> IsFollowed

|Property|Value|
|---|---|
|Description|**Indicates if this attachment is followed.**|
|DisplayName|**Followed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isfollowed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`activitymimeattachment_isfollowed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the activity\_mime\_attachment.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit that owns the activity mime attachment.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the activity mime attachment.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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
|Description|**Version number of the activity mime attachment.**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [activity_pointer_activity_mime_attachment](#BKMK_activity_pointer_activity_mime_attachment)
- [appointment_activity_mime_attachment](#BKMK_appointment_activity_mime_attachment)
- [attachment_activity_mime_attachments](#BKMK_attachment_activity_mime_attachments)
- [email_activity_mime_attachment](#BKMK_email_activity_mime_attachment)
- [template_activity_mime_attachments](#BKMK_template_activity_mime_attachments)

### <a name="BKMK_activity_pointer_activity_mime_attachment"></a> activity_pointer_activity_mime_attachment

One-To-Many Relationship: [activitypointer activity_pointer_activity_mime_attachment](activitypointer.md#BKMK_activity_pointer_activity_mime_attachment)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_appointment_activity_mime_attachment"></a> appointment_activity_mime_attachment

One-To-Many Relationship: [appointment appointment_activity_mime_attachment](appointment.md#BKMK_appointment_activity_mime_attachment)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_attachment_activity_mime_attachments"></a> attachment_activity_mime_attachments

One-To-Many Relationship: [attachment attachment_activity_mime_attachments](attachment.md#BKMK_attachment_activity_mime_attachments)

|Property|Value|
|---|---|
|ReferencedEntity|`attachment`|
|ReferencedAttribute|`attachmentid`|
|ReferencingAttribute|`attachmentid`|
|ReferencingEntityNavigationPropertyName|`attachmentid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_activity_mime_attachment"></a> email_activity_mime_attachment

One-To-Many Relationship: [email email_activity_mime_attachment](email.md#BKMK_email_activity_mime_attachment)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_template_activity_mime_attachments"></a> template_activity_mime_attachments

One-To-Many Relationship: [template template_activity_mime_attachments](template.md#BKMK_template_activity_mime_attachments)

|Property|Value|
|---|---|
|ReferencedEntity|`template`|
|ReferencedAttribute|`templateid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_template`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [ActivityMimeAttachment_AsyncOperations](#BKMK_ActivityMimeAttachment_AsyncOperations)
- [ActivityMimeAttachment_BulkDeleteFailures](#BKMK_ActivityMimeAttachment_BulkDeleteFailures)
- [ActivityMimeAttachment_SyncErrors](#BKMK_ActivityMimeAttachment_SyncErrors)

### <a name="BKMK_ActivityMimeAttachment_AsyncOperations"></a> ActivityMimeAttachment_AsyncOperations

Many-To-One Relationship: [asyncoperation ActivityMimeAttachment_AsyncOperations](asyncoperation.md#BKMK_ActivityMimeAttachment_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ActivityMimeAttachment_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ActivityMimeAttachment_BulkDeleteFailures"></a> ActivityMimeAttachment_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure ActivityMimeAttachment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ActivityMimeAttachment_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ActivityMimeAttachment_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

Many-To-One Relationship: [syncerror ActivityMimeAttachment_SyncErrors](syncerror.md#BKMK_ActivityMimeAttachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ActivityMimeAttachment_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.activitymimeattachment?displayProperty=fullName>
