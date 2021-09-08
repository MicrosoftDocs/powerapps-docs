---
title: "FileAttachment table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the FileAttachment table/entity."
ms.date: 03/04/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# FileAttachment table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

File Attachment


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|RetrieveEntityChanges||<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|FileAttachments|
|DisplayCollectionName|FileAttachments|
|DisplayName|FileAttachment|
|EntitySetName|fileattachments|
|IsBPFEntity|False|
|LogicalCollectionName|fileattachments|
|LogicalName|fileattachment|
|OwnershipType|None|
|PrimaryIdAttribute|fileattachmentid|
|PrimaryNameAttribute|filename|
|SchemaName|FileAttachment|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [FileAttachmentId](#BKMK_FileAttachmentId)
- [FileName](#BKMK_FileName)
- [MimeType](#BKMK_MimeType)
- [ObjectId](#BKMK_ObjectId)
- [ObjectIdTypeCode](#BKMK_ObjectIdTypeCode)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [RegardingFieldName](#BKMK_RegardingFieldName)


### <a name="BKMK_FileAttachmentId"></a> FileAttachmentId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the file attachment.|
|DisplayName|FileAttachmentId|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|fileattachmentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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
|DisplayName|MIME Type|
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
|Description|Unique identifier of the object with which the attachment is associated.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|None|
|Targets|asyncoperation,canvasapp,cascadegrantrevokeaccessrecordstracker,exportsolutionupload,flowsession,imagedescriptor,mailbox,msdyn_aibfile,msdyn_aiconfiguration,msdyn_knowledgearticleimage,revokeinheritedaccessrecordstracker,solution,stagesolutionupload,webresource,workflowbinary,workflowlog|
|Type|Lookup|


### <a name="BKMK_ObjectIdTypeCode"></a> ObjectIdTypeCode

|Property|Value|
|--------|-----|
|Description|Type of entity with which the file attachment is associated.|
|DisplayName|Object Id Type Code|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectidtypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of entity with which the file attachment is associated.|
|DisplayName|Object Type |
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RegardingFieldName"></a> RegardingFieldName

|Property|Value|
|--------|-----|
|Description|Regarding attribute schema name of the attachment.|
|DisplayName|Regarding Attribute Schema Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingfieldname|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [Body](#BKMK_Body)
- [CreatedOn](#BKMK_CreatedOn)
- [FilePointer](#BKMK_FilePointer)
- [FileSizeInBytes](#BKMK_FileSizeInBytes)
- [IsCommitted](#BKMK_IsCommitted)
- [Prefix](#BKMK_Prefix)
- [StoragePointer](#BKMK_StoragePointer)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_Body"></a> Body

**Added by**: File Store Service Extension Solution

|Property|Value|
|--------|-----|
|Description|Body|
|DisplayName|Body|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|body|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the attachment was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_FilePointer"></a> FilePointer

|Property|Value|
|--------|-----|
|Description|File pointer of the attachment.|
|DisplayName|File Pointer|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|filepointer|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileSizeInBytes"></a> FileSizeInBytes

|Property|Value|
|--------|-----|
|Description|File size of the attachment in bytes.|
|DisplayName|File Size (Bytes)|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filesizeinbytes|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_IsCommitted"></a> IsCommitted

**Added by**: File Store Service Extension Solution

|Property|Value|
|--------|-----|
|Description|IsCommitted|
|DisplayName|IsCommitted|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|iscommitted|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsCommitted Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_Prefix"></a> Prefix

|Property|Value|
|--------|-----|
|Description|Prefix of the file pointer in blob storage.|
|DisplayName|Prefix|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|prefix|
|MaxLength|10|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_StoragePointer"></a> StoragePointer

|Property|Value|
|--------|-----|
|Description|Storage pointer.|
|DisplayName|Storage Pointer|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|storagepointer|
|MaxLength|10|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the file attachment.|
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

- [FileAttachment_SyncErrors](#BKMK_FileAttachment_SyncErrors)
- [fileattachment_solution_fileid]()
- [FileAttachment_StageSolutionUpload_SolutionFile]()
- [FileAttachment_ExportSolutionUpload_SolutionFile]()
- [FileAttachment_AsyncOperation_DataBlobId]()
- [FileAttachment_CanvasApp_BackgroundImage]()
- [FileAttachment_CanvasApp_SmallIcon]()
- [FileAttachment_CanvasApp_MediumIcon]()
- [FileAttachment_CanvasApp_LargeIcon]()
- [FileAttachment_CanvasApp_WideIcon]()
- [FileAttachment_CanvasApp_TeamsIcon]()
- [FileAttachment_CanvasApp_Document]()
- [FileAttachment_CanvasApp_Assets]()
- [FileAttachment_WorkflowLog_Inputs]()
- [FileAttachment_WorkflowLog_Outputs]()
- [FileAttachment_FlowSession_AdditionalContext]()
- [FileAttachment_FlowSession_Outputs]()
- [FileAttachment_workflowbinary_Data]()
- [FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile]()
- [FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef]()
- [FileAttachment_WebResource_ContentFileRef]()
- [FileAttachment_WebResource_ContentJsonFileRef]()
- [FileAttachment_msdyn_AIConfiguration_msdyn_Model]()
- [FileAttachment_msdyn_AIBFile_msdyn_File]()


### <a name="BKMK_FileAttachment_SyncErrors"></a> FileAttachment_SyncErrors

Same as syncerror table [FileAttachment_SyncErrors](syncerror.md) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|FileAttachment_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [FileAttachment_Solution](#BKMK_FileAttachment_Solution)
- [stagesolutionupload_FileAttachments](#BKMK_stagesolutionupload_FileAttachments)
- [exportsolutionupload_FileAttachments](#BKMK_exportsolutionupload_FileAttachments)
- [asyncoperation_FileAttachments](#BKMK_asyncoperation_FileAttachments)
- [canvasapp_FileAttachments](#BKMK_canvasapp_FileAttachments)
- [workflowlog_FileAttachments](#BKMK_workflowlog_FileAttachments)
- [flowsession_FileAttachments](#BKMK_flowsession_FileAttachments)
- [workflowbinary_FileAttachments](#BKMK_workflowbinary_FileAttachments)
- [msdyn_knowledgearticleimage_FileAttachments](#BKMK_msdyn_knowledgearticleimage_FileAttachments)
- [mailbox_FileAttachments](#BKMK_mailbox_FileAttachments)
- [webresource_FileAttachments](#BKMK_webresource_FileAttachments)
- [msdyn_aiconfiguration_FileAttachments](#BKMK_msdyn_aiconfiguration_FileAttachments)
- [msdyn_aibfile_FileAttachments](#BKMK_msdyn_aibfile_FileAttachments)


### <a name="BKMK_FileAttachment_Solution"></a> FileAttachment_Solution

See solution Table [FileAttachment_Solution](solution.md) One-To-Many relationship.

### <a name="BKMK_stagesolutionupload_FileAttachments"></a> stagesolutionupload_FileAttachments

**Added by**: StageSolutionUpload Solution

See stagesolutionupload Table [stagesolutionupload_FileAttachments](stagesolutionupload.md) One-To-Many relationship.

### <a name="BKMK_exportsolutionupload_FileAttachments"></a> exportsolutionupload_FileAttachments

**Added by**: ExportSolutionUpload Solution

See exportsolutionupload Table [exportsolutionupload_FileAttachments](exportsolutionupload.md) One-To-Many relationship.

### <a name="BKMK_asyncoperation_FileAttachments"></a> asyncoperation_FileAttachments

See asyncoperation Table [asyncoperation_FileAttachments](asyncoperation.md) One-To-Many relationship.

### <a name="BKMK_canvasapp_FileAttachments"></a> canvasapp_FileAttachments

See canvasapp Table [canvasapp_FileAttachments](canvasapp.md) One-To-Many relationship.

### <a name="BKMK_workflowlog_FileAttachments"></a> workflowlog_FileAttachments

See workflowlog Table [workflowlog_FileAttachments](workflowlog.md) One-To-Many relationship.

### <a name="BKMK_flowsession_FileAttachments"></a> flowsession_FileAttachments

**Added by**: Power Automate Extensions core package Solution

See flowsession Table [flowsession_FileAttachments](flowsession.md) One-To-Many relationship.

### <a name="BKMK_workflowbinary_FileAttachments"></a> workflowbinary_FileAttachments

**Added by**: Power Automate Extensions core package Solution

See workflowbinary Table [workflowbinary_FileAttachments](workflowbinary.md) One-To-Many relationship.

### <a name="BKMK_msdyn_knowledgearticleimage_FileAttachments"></a> msdyn_knowledgearticleimage_FileAttachments

**Added by**: Knowledge Management Online Features Solution

See msdyn_knowledgearticleimage Table [msdyn_knowledgearticleimage_FileAttachments](msdyn_knowledgearticleimage.md) One-To-Many relationship.

### <a name="BKMK_mailbox_FileAttachments"></a> mailbox_FileAttachments

See mailbox Table [mailbox_FileAttachments](mailbox.md) One-To-Many relationship.

### <a name="BKMK_webresource_FileAttachments"></a> webresource_FileAttachments

See webresource Table [webresource_FileAttachments](webresource.md) One-To-Many relationship.

### <a name="BKMK_msdyn_aiconfiguration_FileAttachments"></a> msdyn_aiconfiguration_FileAttachments

**Added by**: AISolution Solution

See msdyn_aiconfiguration Table [msdyn_aiconfiguration_FileAttachments](msdyn_aiconfiguration.md) One-To-Many relationship.

### <a name="BKMK_msdyn_aibfile_FileAttachments"></a> msdyn_aibfile_FileAttachments

**Added by**: AI Solution default templates Solution

See msdyn_aibfile Table [msdyn_aibfile_FileAttachments](msdyn_aibfile.md) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.fileattachment?text=fileattachment EntityType" />