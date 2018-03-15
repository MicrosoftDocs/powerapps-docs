---
title: "ActivityMimeAttachment Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the ActivityMimeAttachment entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# ActivityMimeAttachment Entity Reference

MIME attachment for an activity.

## Entity Properties

**DisplayName**: Attachment<br />
**DisplayCollectionName**: Attachments<br />
**SchemaName**: ActivityMimeAttachment<br />
**CollectionSchemaName**: ActivityMimeAttachments<br />
**LogicalName**: activitymimeattachment<br />
**LogicalCollectionName**: activitymimeattachments<br />
**EntitySetName**: activitymimeattachments<br />
**PrimaryIdAttribute**: activitymimeattachmentid<br />
**PrimaryNameAttribute**: filename<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Unique identifier of the activity with which the attachment is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: activityid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: activitypointer


### <a name="BKMK_ActivityMimeAttachmentId"></a> ActivityMimeAttachmentId

**Description**: Unique identifier of the attachment.<br />
**DisplayName**: Activity Mime Attachment<br />
**LogicalName**: activitymimeattachmentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ActivityMimeAttachmentIdUnique"></a> ActivityMimeAttachmentIdUnique

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: activitymimeattachmentidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_AttachmentContentId"></a> AttachmentContentId

**Description**: For internal use only<br />
**DisplayName**: Content Id<br />
**LogicalName**: attachmentcontentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_AttachmentId"></a> AttachmentId

**Description**: Unique identifier of the attachment with which this activitymimeattachment is associated.<br />
**DisplayName**: Attachment<br />
**LogicalName**: attachmentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: attachment


### <a name="BKMK_AttachmentNumber"></a> AttachmentNumber

**Description**: Number of the attachment.<br />
**DisplayName**: Attachment Number<br />
**LogicalName**: attachmentnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_Body"></a> Body

**Description**: Contents of the attachment.<br />
**DisplayName**: Body<br />
**LogicalName**: body<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FileName"></a> FileName

**Description**: File name of the attachment.<br />
**DisplayName**: File Name<br />
**LogicalName**: filename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_MimeType"></a> MimeType

**Description**: MIME type of the attachment.<br />
**DisplayName**: Mime Type<br />
**LogicalName**: mimetype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Unique identifier of the record with which the attachment is associated<br />
**DisplayName**: Item<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: activitypointer,template


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Object Type Code of the entity that is associated with the attachment.<br />
**DisplayName**: Entity<br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_Subject"></a> Subject

**Description**: Descriptive subject for the attachment.<br />
**DisplayName**: Subject<br />
**LogicalName**: subject<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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

**Description**: Descriptive subject for the activity.<br />
**DisplayName**: ActivitySubject<br />
**LogicalName**: activitysubject<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_AnonymousLink"></a> AnonymousLink

**Description**: anonymous link<br />
**DisplayName**: For internal use only.<br />
**LogicalName**: anonymouslink<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_FileSize"></a> FileSize

**Description**: File size of the attachment.<br />
**DisplayName**: File Size (Bytes)<br />
**LogicalName**: filesize<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_IsFollowed"></a> IsFollowed

**Description**: Indicates if this attachment is followed.<br />
**DisplayName**: Followed<br />
**LogicalName**: isfollowed<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Indicates whether the solution component is part of a managed solution.<br />
**DisplayName**: Is Managed<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: For internal use only.<br />
**DisplayName**: Record Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the activity_mime_attachment.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the activity mime attachment.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the activity mime attachment.<br />
**DisplayName**: Owner<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the activity mime attachment.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [ActivityMimeAttachment_AsyncOperations](#BKMK_ActivityMimeAttachment_AsyncOperations)
- [ActivityMimeAttachment_BulkDeleteFailures](#BKMK_ActivityMimeAttachment_BulkDeleteFailures)
- [userentityinstancedata_activitymimeattachment](#BKMK_userentityinstancedata_activitymimeattachment)
- [ActivityMimeAttachment_SyncErrors](#BKMK_ActivityMimeAttachment_SyncErrors)


### <a name="BKMK_ActivityMimeAttachment_AsyncOperations"></a> ActivityMimeAttachment_AsyncOperations

Same as asyncoperation entity [ActivityMimeAttachment_AsyncOperations](asyncoperation.md#BKMK_ActivityMimeAttachment_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ActivityMimeAttachment_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ActivityMimeAttachment_BulkDeleteFailures"></a> ActivityMimeAttachment_BulkDeleteFailures

Same as bulkdeletefailure entity [ActivityMimeAttachment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ActivityMimeAttachment_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ActivityMimeAttachment_BulkDeleteFailures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityinstancedata_activitymimeattachment"></a> userentityinstancedata_activitymimeattachment

Same as userentityinstancedata entity [userentityinstancedata_activitymimeattachment](userentityinstancedata.md#BKMK_userentityinstancedata_activitymimeattachment) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_activitymimeattachment<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

Same as syncerror entity [ActivityMimeAttachment_SyncErrors](syncerror.md#BKMK_ActivityMimeAttachment_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: ActivityMimeAttachment_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [appointment_activity_mime_attachment](#BKMK_appointment_activity_mime_attachment)
- [template_activity_mime_attachments](#BKMK_template_activity_mime_attachments)
- [email_activity_mime_attachment](#BKMK_email_activity_mime_attachment)
- [activity_pointer_activity_mime_attachment](#BKMK_activity_pointer_activity_mime_attachment)


### <a name="BKMK_appointment_activity_mime_attachment"></a> appointment_activity_mime_attachment

See appointment Entity [appointment_activity_mime_attachment](appointment.md#BKMK_appointment_activity_mime_attachment) One-To-Many relationship.

### <a name="BKMK_template_activity_mime_attachments"></a> template_activity_mime_attachments

See template Entity [template_activity_mime_attachments](template.md#BKMK_template_activity_mime_attachments) One-To-Many relationship.

### <a name="BKMK_email_activity_mime_attachment"></a> email_activity_mime_attachment

See email Entity [email_activity_mime_attachment](email.md#BKMK_email_activity_mime_attachment) One-To-Many relationship.

### <a name="BKMK_activity_pointer_activity_mime_attachment"></a> activity_pointer_activity_mime_attachment

See activitypointer Entity [activity_pointer_activity_mime_attachment](activitypointer.md#BKMK_activity_pointer_activity_mime_attachment) One-To-Many relationship.
activitymimeattachment

