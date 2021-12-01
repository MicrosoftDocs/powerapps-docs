---
title: "Attachment (ActivityMimeAttachment) table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Attachment (ActivityMimeAttachment) table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Attachment (ActivityMimeAttachment) table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

MIME attachment for an activity.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Create|POST [*org URI*]/api/data/v9.0/activitymimeattachments<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/activitymimeattachments(*activitymimeattachmentid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|Retrieve|GET [*org URI*]/api/data/v9.0/activitymimeattachments(*activitymimeattachmentid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/activitymimeattachments<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|Update|PATCH [*org URI*]/api/data/v9.0/activitymimeattachments(*activitymimeattachmentid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|ActivityMimeAttachments|
|DisplayCollectionName|Attachments|
|DisplayName|Attachment|
|EntitySetName|activitymimeattachments|
|IsBPFEntity|False|
|LogicalCollectionName|activitymimeattachments|
|LogicalName|activitymimeattachment|
|OwnershipType|None|
|PrimaryIdAttribute|activitymimeattachmentid|
|PrimaryNameAttribute|filename|
|SchemaName|ActivityMimeAttachment|

<a name="writable-attributes"></a>

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
|--------|-----|
|Description|Unique identifier of the activity with which the attachment is associated.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activityid|
|RequiredLevel|None|
|Targets|activitypointer|
|Type|Lookup|


### <a name="BKMK_ActivityMimeAttachmentId"></a> ActivityMimeAttachmentId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the attachment.|
|DisplayName|Activity Mime Attachment|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activitymimeattachmentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ActivityMimeAttachmentIdUnique"></a> ActivityMimeAttachmentIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|activitymimeattachmentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_AttachmentContentId"></a> AttachmentContentId

|Property|Value|
|--------|-----|
|Description|For internal use only|
|DisplayName|Content Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attachmentcontentid|
|MaxLength|250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AttachmentId"></a> AttachmentId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the attachment with which this activitymimeattachment is associated.|
|DisplayName|Attachment|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attachmentid|
|RequiredLevel|ApplicationRequired|
|Targets|attachment|
|Type|Lookup|


### <a name="BKMK_AttachmentNumber"></a> AttachmentNumber

|Property|Value|
|--------|-----|
|Description|Number of the attachment.|
|DisplayName|Attachment Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|attachmentnumber|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_Body"></a> Body

|Property|Value|
|--------|-----|
|Description|Contents of the attachment.|
|DisplayName|Body|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|body|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileName"></a> FileName

|Property|Value|
|--------|-----|
|Description|File name of the attachment.|
|DisplayName|File Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filename|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|--------|-----|
|Description|MIME type of the attachment.|
|DisplayName|Mime Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mimetype|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the record with which the attachment is associated|
|DisplayName|Item|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|SystemRequired|
|Targets|activitypointer,template|
|Type|Lookup|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Object Type Code of the entity that is associated with the attachment.|
|DisplayName|Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|--------|-----|
|Description|Descriptive subject for the attachment.|
|DisplayName|Subject|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subject|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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
|--------|-----|
|Description|Descriptive subject for the activity.|
|DisplayName|ActivitySubject|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activitysubject|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AnonymousLink"></a> AnonymousLink

|Property|Value|
|--------|-----|
|Description|anonymous link|
|DisplayName|For internal use only.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|anonymouslink|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


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



### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|--------|-----|
|Description|File size of the attachment.|
|DisplayName|File Size (Bytes)|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filesize|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsFollowed"></a> IsFollowed

|Property|Value|
|--------|-----|
|Description|Indicates if this attachment is followed.|
|DisplayName|Followed|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isfollowed|
|RequiredLevel|None|
|Type|Boolean|

#### IsFollowed Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



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


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the activity_mime_attachment.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|ApplicationRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the activity mime attachment.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the activity mime attachment.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


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
|Description|Version number of the activity mime attachment.|
|DisplayName|Version Number|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [ActivityMimeAttachment_AsyncOperations](#BKMK_ActivityMimeAttachment_AsyncOperations)
- [ActivityMimeAttachment_BulkDeleteFailures](#BKMK_ActivityMimeAttachment_BulkDeleteFailures)
- [ActivityMimeAttachment_SyncErrors](#BKMK_ActivityMimeAttachment_SyncErrors)


### <a name="BKMK_ActivityMimeAttachment_AsyncOperations"></a> ActivityMimeAttachment_AsyncOperations

Same as asyncoperation table [ActivityMimeAttachment_AsyncOperations](asyncoperation.md#BKMK_ActivityMimeAttachment_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ActivityMimeAttachment_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ActivityMimeAttachment_BulkDeleteFailures"></a> ActivityMimeAttachment_BulkDeleteFailures

Same as bulkdeletefailure table [ActivityMimeAttachment_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ActivityMimeAttachment_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ActivityMimeAttachment_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

Same as syncerror table [ActivityMimeAttachment_SyncErrors](syncerror.md#BKMK_ActivityMimeAttachment_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|ActivityMimeAttachment_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [appointment_activity_mime_attachment](#BKMK_appointment_activity_mime_attachment)
- [template_activity_mime_attachments](#BKMK_template_activity_mime_attachments)
- [email_activity_mime_attachment](#BKMK_email_activity_mime_attachment)
- [activity_pointer_activity_mime_attachment](#BKMK_activity_pointer_activity_mime_attachment)


### <a name="BKMK_appointment_activity_mime_attachment"></a> appointment_activity_mime_attachment

See appointment Table [appointment_activity_mime_attachment](appointment.md#BKMK_appointment_activity_mime_attachment) One-To-Many relationship.

### <a name="BKMK_template_activity_mime_attachments"></a> template_activity_mime_attachments

See template Table [template_activity_mime_attachments](template.md#BKMK_template_activity_mime_attachments) One-To-Many relationship.

### <a name="BKMK_email_activity_mime_attachment"></a> email_activity_mime_attachment

See email Table [email_activity_mime_attachment](email.md#BKMK_email_activity_mime_attachment) One-To-Many relationship.

### <a name="BKMK_activity_pointer_activity_mime_attachment"></a> activity_pointer_activity_mime_attachment

See activitypointer Table [activity_pointer_activity_mime_attachment](activitypointer.md#BKMK_activity_pointer_activity_mime_attachment) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.activitymimeattachment?text=activitymimeattachment EntityType" />