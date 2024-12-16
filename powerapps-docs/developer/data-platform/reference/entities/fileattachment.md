---
title: "FileAttachment table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the FileAttachment table/entity with Microsoft Dataverse."
ms.date: 11/09/2024
ms.service: powerapps
ms.topic: reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# FileAttachment table/entity reference

File Attachment

## Properties

The following table lists selected properties for the FileAttachment table.

|Property|Value|
| --- | --- |
| **DisplayName** | **FileAttachment** |
| **DisplayCollectionName** | **FileAttachments** |
| **SchemaName** | `FileAttachment` |
| **CollectionSchemaName** | `FileAttachments` |
| **EntitySetName** | `fileattachments`|
| **LogicalName** | `fileattachment` |
| **LogicalCollectionName** | `fileattachments` |
| **PrimaryIdAttribute** | `fileattachmentid` |
| **PrimaryNameAttribute** |`filename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

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
|---|---|
|Description|**Unique identifier of the file attachment.**|
|DisplayName|**FileAttachmentId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`fileattachmentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the attachment is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|activityfileattachment, activitypointer, asyncoperation, botcomponent, canvasapp, cascadegrantrevokeaccessrecordstracker, deleteditemreference, desktopflowbinary, desktopflowmodule, email, exportedexcel, exportsolutionupload, flowsession, imagedescriptor, knowledgearticle, mailbox, msdyn_aibfeedbackloop, msdyn_aibfile, msdyn_aiconfiguration, msdyn_analysisjob, msdyn_fileupload, msdyn_integratedsearchprovider, msdyn_kbattachment, msdyn_knowledgearticleimage, msdyn_mobileapp, msdyn_pminferredtask, msdyn_richtextfile, mspcat_catalogsubmissionfiles, mspcat_packagestore, package, packagehistory, pluginpackage, powerbidataset, powerbireport, powerpagecomponent, powerpagesitepublished, powerpagesscanreport, report, retaineddataexcel, revokeinheritedaccessrecordstracker, ribbonclientmetadata, searchcustomanalyzer, solution, stagesolutionupload, webresource, workflowbinary, workflowlog|

### <a name="BKMK_ObjectIdTypeCode"></a> ObjectIdTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the file attachment is associated.**|
|DisplayName|**Object Id Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objectidtypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the file attachment is associated.**|
|DisplayName|**Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_RegardingFieldName"></a> RegardingFieldName

|Property|Value|
|---|---|
|Description|**Regarding attribute schema name of the attachment.**|
|DisplayName|**Regarding Attribute Schema Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingfieldname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|255|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Body](#BKMK_Body)
- [CreatedOn](#BKMK_CreatedOn)
- [FilePointer](#BKMK_FilePointer)
- [FileSizeInBytes](#BKMK_FileSizeInBytes)
- [IsCommitted](#BKMK_IsCommitted)
- [Prefix](#BKMK_Prefix)
- [StoragePointer](#BKMK_StoragePointer)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_Body"></a> Body

|Property|Value|
|---|---|
|Description|**Body**|
|DisplayName|**Body**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`body`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the attachment was created.**|
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

### <a name="BKMK_FileSizeInBytes"></a> FileSizeInBytes

|Property|Value|
|---|---|
|Description|**File size of the attachment in bytes.**|
|DisplayName|**File Size (Bytes)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`filesizeinbytes`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_IsCommitted"></a> IsCommitted

|Property|Value|
|---|---|
|Description|**IsCommitted**|
|DisplayName|**IsCommitted**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`iscommitted`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`fileattachment_iscommitted`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Prefix"></a> Prefix

|Property|Value|
|---|---|
|Description|**Prefix of the file pointer in blob storage.**|
|DisplayName|**Prefix**|
|IsValidForForm|False|
|IsValidForRead|False|
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
|Description|**Version number of the file attachment.**|
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

- [activityfileattachment_FileAttachments](#BKMK_activityfileattachment_FileAttachments)
- [activitypointer_FileAttachments](#BKMK_activitypointer_FileAttachments)
- [asyncoperation_FileAttachments](#BKMK_asyncoperation_FileAttachments)
- [botcomponent_FileAttachments](#BKMK_botcomponent_FileAttachments)
- [canvasapp_FileAttachments](#BKMK_canvasapp_FileAttachments)
- [desktopflowbinary_FileAttachments](#BKMK_desktopflowbinary_FileAttachments)
- [desktopflowmodule_FileAttachments](#BKMK_desktopflowmodule_FileAttachments)
- [email_FileAttachments](#BKMK_email_FileAttachments)
- [exportedexcel_FileAttachments](#BKMK_exportedexcel_FileAttachments)
- [exportsolutionupload_FileAttachments](#BKMK_exportsolutionupload_FileAttachments)
- [FileAttachment_Solution](#BKMK_FileAttachment_Solution)
- [flowsession_FileAttachments](#BKMK_flowsession_FileAttachments)
- [knowledgearticle_FileAttachments](#BKMK_knowledgearticle_FileAttachments)
- [mailbox_FileAttachments](#BKMK_mailbox_FileAttachments)
- [msdyn_aibfeedbackloop_FileAttachments](#BKMK_msdyn_aibfeedbackloop_FileAttachments)
- [msdyn_aibfile_FileAttachments](#BKMK_msdyn_aibfile_FileAttachments)
- [msdyn_aiconfiguration_FileAttachments](#BKMK_msdyn_aiconfiguration_FileAttachments)
- [msdyn_analysisjob_FileAttachments](#BKMK_msdyn_analysisjob_FileAttachments)
- [msdyn_fileupload_FileAttachments](#BKMK_msdyn_fileupload_FileAttachments)
- [msdyn_integratedsearchprovider_FileAttachments](#BKMK_msdyn_integratedsearchprovider_FileAttachments)
- [msdyn_kbattachment_FileAttachments](#BKMK_msdyn_kbattachment_FileAttachments)
- [msdyn_knowledgearticleimage_FileAttachments](#BKMK_msdyn_knowledgearticleimage_FileAttachments)
- [msdyn_mobileapp_FileAttachments](#BKMK_msdyn_mobileapp_FileAttachments)
- [msdyn_pminferredtask_FileAttachments](#BKMK_msdyn_pminferredtask_FileAttachments)
- [msdyn_richtextfile_FileAttachments](#BKMK_msdyn_richtextfile_FileAttachments)
- [mspcat_catalogsubmissionfiles_FileAttachments](#BKMK_mspcat_catalogsubmissionfiles_FileAttachments)
- [mspcat_packagestore_FileAttachments](#BKMK_mspcat_packagestore_FileAttachments)
- [package_FileAttachments](#BKMK_package_FileAttachments)
- [packagehistory_FileAttachments](#BKMK_packagehistory_FileAttachments)
- [pluginpackage_FileAttachments](#BKMK_pluginpackage_FileAttachments)
- [powerbidataset_FileAttachments](#BKMK_powerbidataset_FileAttachments)
- [powerbireport_FileAttachments](#BKMK_powerbireport_FileAttachments)
- [powerpagecomponent_FileAttachments](#BKMK_powerpagecomponent_FileAttachments)
- [powerpagesitepublished_FileAttachments](#BKMK_powerpagesitepublished_FileAttachments)
- [powerpagesscanreport_FileAttachments](#BKMK_powerpagesscanreport_FileAttachments)
- [report_FileAttachments](#BKMK_report_FileAttachments)
- [retaineddataexcel_FileAttachments](#BKMK_retaineddataexcel_FileAttachments)
- [searchcustomanalyzer_FileAttachments](#BKMK_searchcustomanalyzer_FileAttachments)
- [stagesolutionupload_FileAttachments](#BKMK_stagesolutionupload_FileAttachments)
- [webresource_FileAttachments](#BKMK_webresource_FileAttachments)
- [workflowbinary_FileAttachments](#BKMK_workflowbinary_FileAttachments)
- [workflowlog_FileAttachments](#BKMK_workflowlog_FileAttachments)

### <a name="BKMK_activityfileattachment_FileAttachments"></a> activityfileattachment_FileAttachments

One-To-Many Relationship: [activityfileattachment activityfileattachment_FileAttachments](activityfileattachment.md#BKMK_activityfileattachment_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`activityfileattachment`|
|ReferencedAttribute|`activityfileattachmentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_activityfileattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_activitypointer_FileAttachments"></a> activitypointer_FileAttachments

One-To-Many Relationship: [activitypointer activitypointer_FileAttachments](activitypointer.md#BKMK_activitypointer_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_asyncoperation_FileAttachments"></a> asyncoperation_FileAttachments

One-To-Many Relationship: [asyncoperation asyncoperation_FileAttachments](asyncoperation.md#BKMK_asyncoperation_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`asyncoperation`|
|ReferencedAttribute|`asyncoperationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_asyncoperation`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_botcomponent_FileAttachments"></a> botcomponent_FileAttachments

One-To-Many Relationship: [botcomponent botcomponent_FileAttachments](botcomponent.md#BKMK_botcomponent_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`botcomponent`|
|ReferencedAttribute|`botcomponentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_botcomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_canvasapp_FileAttachments"></a> canvasapp_FileAttachments

One-To-Many Relationship: [canvasapp canvasapp_FileAttachments](canvasapp.md#BKMK_canvasapp_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`canvasapp`|
|ReferencedAttribute|`canvasappid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_canvasapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowbinary_FileAttachments"></a> desktopflowbinary_FileAttachments

One-To-Many Relationship: [desktopflowbinary desktopflowbinary_FileAttachments](desktopflowbinary.md#BKMK_desktopflowbinary_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowbinary`|
|ReferencedAttribute|`desktopflowbinaryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_desktopflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_desktopflowmodule_FileAttachments"></a> desktopflowmodule_FileAttachments

One-To-Many Relationship: [desktopflowmodule desktopflowmodule_FileAttachments](desktopflowmodule.md#BKMK_desktopflowmodule_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`desktopflowmodule`|
|ReferencedAttribute|`desktopflowmoduleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_desktopflowmodule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_email_FileAttachments"></a> email_FileAttachments

One-To-Many Relationship: [email email_FileAttachments](email.md#BKMK_email_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportedexcel_FileAttachments"></a> exportedexcel_FileAttachments

One-To-Many Relationship: [exportedexcel exportedexcel_FileAttachments](exportedexcel.md#BKMK_exportedexcel_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`exportedexcel`|
|ReferencedAttribute|`exportedexcelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_exportedexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_exportsolutionupload_FileAttachments"></a> exportsolutionupload_FileAttachments

One-To-Many Relationship: [exportsolutionupload exportsolutionupload_FileAttachments](exportsolutionupload.md#BKMK_exportsolutionupload_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`exportsolutionupload`|
|ReferencedAttribute|`exportsolutionuploadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_exportsolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_Solution"></a> FileAttachment_Solution

One-To-Many Relationship: [solution FileAttachment_Solution](solution.md#BKMK_FileAttachment_Solution)

|Property|Value|
|---|---|
|ReferencedEntity|`solution`|
|ReferencedAttribute|`solutionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`FileAttachment_Solution`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_flowsession_FileAttachments"></a> flowsession_FileAttachments

One-To-Many Relationship: [flowsession flowsession_FileAttachments](flowsession.md#BKMK_flowsession_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`flowsession`|
|ReferencedAttribute|`flowsessionid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_flowsession`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_knowledgearticle_FileAttachments"></a> knowledgearticle_FileAttachments

One-To-Many Relationship: [knowledgearticle knowledgearticle_FileAttachments](knowledgearticle.md#BKMK_knowledgearticle_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_knowledgearticle`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mailbox_FileAttachments"></a> mailbox_FileAttachments

One-To-Many Relationship: [mailbox mailbox_FileAttachments](mailbox.md#BKMK_mailbox_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`mailbox`|
|ReferencedAttribute|`mailboxid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mailbox`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfeedbackloop_FileAttachments"></a> msdyn_aibfeedbackloop_FileAttachments

One-To-Many Relationship: [msdyn_aibfeedbackloop msdyn_aibfeedbackloop_FileAttachments](msdyn_aibfeedbackloop.md#BKMK_msdyn_aibfeedbackloop_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfeedbackloop`|
|ReferencedAttribute|`msdyn_aibfeedbackloopid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibfeedbackloop`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aibfile_FileAttachments"></a> msdyn_aibfile_FileAttachments

One-To-Many Relationship: [msdyn_aibfile msdyn_aibfile_FileAttachments](msdyn_aibfile.md#BKMK_msdyn_aibfile_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aibfile`|
|ReferencedAttribute|`msdyn_aibfileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aibfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_FileAttachments"></a> msdyn_aiconfiguration_FileAttachments

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_FileAttachments](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_aiconfiguration`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_FileAttachments"></a> msdyn_analysisjob_FileAttachments

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_FileAttachments](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_analysisjob`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_fileupload_FileAttachments"></a> msdyn_fileupload_FileAttachments

One-To-Many Relationship: [msdyn_fileupload msdyn_fileupload_FileAttachments](msdyn_fileupload.md#BKMK_msdyn_fileupload_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_fileupload`|
|ReferencedAttribute|`msdyn_fileuploadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_fileupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_integratedsearchprovider_FileAttachments"></a> msdyn_integratedsearchprovider_FileAttachments

One-To-Many Relationship: [msdyn_integratedsearchprovider msdyn_integratedsearchprovider_FileAttachments](msdyn_integratedsearchprovider.md#BKMK_msdyn_integratedsearchprovider_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_integratedsearchprovider`|
|ReferencedAttribute|`msdyn_integratedsearchproviderid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_integratedsearchprovider`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_kbattachment_FileAttachments"></a> msdyn_kbattachment_FileAttachments

One-To-Many Relationship: [msdyn_kbattachment msdyn_kbattachment_FileAttachments](msdyn_kbattachment.md#BKMK_msdyn_kbattachment_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_kbattachment`|
|ReferencedAttribute|`msdyn_kbattachmentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_kbattachment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_knowledgearticleimage_FileAttachments"></a> msdyn_knowledgearticleimage_FileAttachments

One-To-Many Relationship: [msdyn_knowledgearticleimage msdyn_knowledgearticleimage_FileAttachments](msdyn_knowledgearticleimage.md#BKMK_msdyn_knowledgearticleimage_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_knowledgearticleimage`|
|ReferencedAttribute|`msdyn_knowledgearticleimageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_knowledgearticleimage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_mobileapp_FileAttachments"></a> msdyn_mobileapp_FileAttachments

One-To-Many Relationship: [msdyn_mobileapp msdyn_mobileapp_FileAttachments](msdyn_mobileapp.md#BKMK_msdyn_mobileapp_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_mobileapp`|
|ReferencedAttribute|`msdyn_mobileappid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_mobileapp`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_pminferredtask_FileAttachments"></a> msdyn_pminferredtask_FileAttachments

One-To-Many Relationship: [msdyn_pminferredtask msdyn_pminferredtask_FileAttachments](msdyn_pminferredtask.md#BKMK_msdyn_pminferredtask_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_pminferredtask`|
|ReferencedAttribute|`msdyn_pminferredtaskid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_pminferredtask`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_richtextfile_FileAttachments"></a> msdyn_richtextfile_FileAttachments

One-To-Many Relationship: [msdyn_richtextfile msdyn_richtextfile_FileAttachments](msdyn_richtextfile.md#BKMK_msdyn_richtextfile_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_richtextfile`|
|ReferencedAttribute|`msdyn_richtextfileid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_msdyn_richtextfile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_catalogsubmissionfiles_FileAttachments"></a> mspcat_catalogsubmissionfiles_FileAttachments

One-To-Many Relationship: [mspcat_catalogsubmissionfiles mspcat_catalogsubmissionfiles_FileAttachments](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_catalogsubmissionfiles`|
|ReferencedAttribute|`mspcat_catalogsubmissionfilesid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mspcat_catalogsubmissionfiles`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_mspcat_packagestore_FileAttachments"></a> mspcat_packagestore_FileAttachments

One-To-Many Relationship: [mspcat_packagestore mspcat_packagestore_FileAttachments](mspcat_packagestore.md#BKMK_mspcat_packagestore_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`mspcat_packagestore`|
|ReferencedAttribute|`mspcat_packagestoreid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_mspcat_packagestore`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_package_FileAttachments"></a> package_FileAttachments

One-To-Many Relationship: [package package_FileAttachments](package.md#BKMK_package_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`package`|
|ReferencedAttribute|`packageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_package`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_packagehistory_FileAttachments"></a> packagehistory_FileAttachments

One-To-Many Relationship: [packagehistory packagehistory_FileAttachments](packagehistory.md#BKMK_packagehistory_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`packagehistory`|
|ReferencedAttribute|`packagehistoryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_packagehistory`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_pluginpackage_FileAttachments"></a> pluginpackage_FileAttachments

One-To-Many Relationship: [pluginpackage pluginpackage_FileAttachments](pluginpackage.md#BKMK_pluginpackage_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`pluginpackage`|
|ReferencedAttribute|`pluginpackageid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_pluginpackage`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbidataset_FileAttachments"></a> powerbidataset_FileAttachments

One-To-Many Relationship: [powerbidataset powerbidataset_FileAttachments](powerbidataset.md#BKMK_powerbidataset_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbidataset`|
|ReferencedAttribute|`powerbidatasetid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbidataset`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerbireport_FileAttachments"></a> powerbireport_FileAttachments

One-To-Many Relationship: [powerbireport powerbireport_FileAttachments](powerbireport.md#BKMK_powerbireport_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`powerbireport`|
|ReferencedAttribute|`powerbireportid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerbireport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagecomponent_FileAttachments"></a> powerpagecomponent_FileAttachments

One-To-Many Relationship: [powerpagecomponent powerpagecomponent_FileAttachments](powerpagecomponent.md#BKMK_powerpagecomponent_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagecomponent`|
|ReferencedAttribute|`powerpagecomponentid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagecomponent`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesitepublished_FileAttachments"></a> powerpagesitepublished_FileAttachments

One-To-Many Relationship: [powerpagesitepublished powerpagesitepublished_FileAttachments](powerpagesitepublished.md#BKMK_powerpagesitepublished_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesitepublished`|
|ReferencedAttribute|`powerpagesitepublishedid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesitepublished`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerpagesscanreport_FileAttachments"></a> powerpagesscanreport_FileAttachments

One-To-Many Relationship: [powerpagesscanreport powerpagesscanreport_FileAttachments](powerpagesscanreport.md#BKMK_powerpagesscanreport_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`powerpagesscanreport`|
|ReferencedAttribute|`powerpagesscanreportid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_powerpagesscanreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_report_FileAttachments"></a> report_FileAttachments

One-To-Many Relationship: [report report_FileAttachments](report.md#BKMK_report_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`report`|
|ReferencedAttribute|`reportid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_report`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_retaineddataexcel_FileAttachments"></a> retaineddataexcel_FileAttachments

One-To-Many Relationship: [retaineddataexcel retaineddataexcel_FileAttachments](retaineddataexcel.md#BKMK_retaineddataexcel_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`retaineddataexcel`|
|ReferencedAttribute|`retaineddataexcelid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_retaineddataexcel`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_searchcustomanalyzer_FileAttachments"></a> searchcustomanalyzer_FileAttachments

One-To-Many Relationship: [searchcustomanalyzer searchcustomanalyzer_FileAttachments](searchcustomanalyzer.md#BKMK_searchcustomanalyzer_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`searchcustomanalyzer`|
|ReferencedAttribute|`searchcustomanalyzerid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_searchcustomanalyzer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_stagesolutionupload_FileAttachments"></a> stagesolutionupload_FileAttachments

One-To-Many Relationship: [stagesolutionupload stagesolutionupload_FileAttachments](stagesolutionupload.md#BKMK_stagesolutionupload_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`stagesolutionupload`|
|ReferencedAttribute|`stagesolutionuploadid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_stagesolutionupload`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_webresource_FileAttachments"></a> webresource_FileAttachments

One-To-Many Relationship: [webresource webresource_FileAttachments](webresource.md#BKMK_webresource_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`webresource`|
|ReferencedAttribute|`webresourceid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_webresource`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowbinary_FileAttachments"></a> workflowbinary_FileAttachments

One-To-Many Relationship: [workflowbinary workflowbinary_FileAttachments](workflowbinary.md#BKMK_workflowbinary_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowbinary`|
|ReferencedAttribute|`workflowbinaryid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_workflowbinary`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflowlog_FileAttachments"></a> workflowlog_FileAttachments

One-To-Many Relationship: [workflowlog workflowlog_FileAttachments](workflowlog.md#BKMK_workflowlog_FileAttachments)

|Property|Value|
|---|---|
|ReferencedEntity|`workflowlog`|
|ReferencedAttribute|`workflowlogid`|
|ReferencingAttribute|`objectid`|
|ReferencingEntityNavigationPropertyName|`objectid_workflowlog`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [FileAttachment_activityfileattachment_FileContent](#BKMK_FileAttachment_activityfileattachment_FileContent)
- [FileAttachment_ActivityPointer_DescriptionBlobId](#BKMK_FileAttachment_ActivityPointer_DescriptionBlobId)
- [FileAttachment_AsyncOperation_DataBlobId](#BKMK_FileAttachment_AsyncOperation_DataBlobId)
- [FileAttachment_botcomponent_FileData](#BKMK_FileAttachment_botcomponent_FileData)
- [FileAttachment_CanvasApp_Assets](#BKMK_FileAttachment_CanvasApp_Assets)
- [FileAttachment_CanvasApp_BackgroundImage](#BKMK_FileAttachment_CanvasApp_BackgroundImage)
- [FileAttachment_CanvasApp_Document](#BKMK_FileAttachment_CanvasApp_Document)
- [FileAttachment_CanvasApp_LargeIcon](#BKMK_FileAttachment_CanvasApp_LargeIcon)
- [FileAttachment_CanvasApp_MediumIcon](#BKMK_FileAttachment_CanvasApp_MediumIcon)
- [FileAttachment_CanvasApp_SmallIcon](#BKMK_FileAttachment_CanvasApp_SmallIcon)
- [FileAttachment_CanvasApp_TeamsIcon](#BKMK_FileAttachment_CanvasApp_TeamsIcon)
- [FileAttachment_CanvasApp_WideIcon](#BKMK_FileAttachment_CanvasApp_WideIcon)
- [FileAttachment_desktopflowbinary_Data](#BKMK_FileAttachment_desktopflowbinary_Data)
- [FileAttachment_desktopflowmodule_Data](#BKMK_FileAttachment_desktopflowmodule_Data)
- [FileAttachment_Email_DescriptionBlobId](#BKMK_FileAttachment_Email_DescriptionBlobId)
- [FileAttachment_exportedexcel_ExcelContent](#BKMK_FileAttachment_exportedexcel_ExcelContent)
- [FileAttachment_ExportSolutionUpload_SolutionFile](#BKMK_FileAttachment_ExportSolutionUpload_SolutionFile)
- [FileAttachment_FlowSession_AdditionalContext](#BKMK_FileAttachment_FlowSession_AdditionalContext)
- [FileAttachment_FlowSession_Inputs](#BKMK_FileAttachment_FlowSession_Inputs)
- [FileAttachment_FlowSession_Outputs](#BKMK_FileAttachment_FlowSession_Outputs)
- [FileAttachment_KnowledgeArticle_msdyn_contentstore](#BKMK_FileAttachment_KnowledgeArticle_msdyn_contentstore)
- [FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef](#BKMK_FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef)
- [FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput](#BKMK_FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput)
- [FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult](#BKMK_FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult)
- [FileAttachment_msdyn_AIBFile_msdyn_File](#BKMK_FileAttachment_msdyn_AIBFile_msdyn_File)
- [FileAttachment_msdyn_AIConfiguration_msdyn_Model](#BKMK_FileAttachment_msdyn_AIConfiguration_msdyn_Model)
- [FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport](#BKMK_FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport)
- [FileAttachment_msdyn_FileUpload_msdyn_ErrorLog](#BKMK_FileAttachment_msdyn_FileUpload_msdyn_ErrorLog)
- [FileAttachment_msdyn_FileUpload_msdyn_FileContent](#BKMK_FileAttachment_msdyn_FileUpload_msdyn_FileContent)
- [FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample](#BKMK_FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample)
- [FileAttachment_msdyn_kbattachment_msdyn_fileattachment](#BKMK_FileAttachment_msdyn_kbattachment_msdyn_fileattachment)
- [FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile](#BKMK_FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167)
- [FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi)
- [FileAttachment_msdyn_mobileapp_msdyn_launchAppResources](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_launchAppResources)
- [FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid)
- [FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS)
- [FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage)
- [FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson)
- [FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist)
- [FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage)
- [FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage](#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage)
- [FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport](#BKMK_FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport)
- [FileAttachment_msdyn_richtextfile_msdyn_fileblob](#BKMK_FileAttachment_msdyn_richtextfile_msdyn_fileblob)
- [FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File](#BKMK_FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File)
- [FileAttachment_mspcat_PackageStore_mspcat_PackageFile](#BKMK_FileAttachment_mspcat_PackageStore_mspcat_PackageFile)
- [FileAttachment_package_DeploymentLog](#BKMK_FileAttachment_package_DeploymentLog)
- [FileAttachment_packagehistory_DeploymentLog](#BKMK_FileAttachment_packagehistory_DeploymentLog)
- [FileAttachment_pluginpackage_FileId](#BKMK_FileAttachment_pluginpackage_FileId)
- [FileAttachment_pluginpackage_Package](#BKMK_FileAttachment_pluginpackage_Package)
- [FileAttachment_powerbidataset_Package](#BKMK_FileAttachment_powerbidataset_Package)
- [FileAttachment_powerbireport_Package](#BKMK_FileAttachment_powerbireport_Package)
- [FileAttachment_powerpagecomponent_filecontent](#BKMK_FileAttachment_powerpagecomponent_filecontent)
- [FileAttachment_powerpagesitepublished_publishedmetadata](#BKMK_FileAttachment_powerpagesitepublished_publishedmetadata)
- [FileAttachment_powerpagesitepublished_publishedsource](#BKMK_FileAttachment_powerpagesitepublished_publishedsource)
- [FileAttachment_PowerPagesScanReport_FileContent](#BKMK_FileAttachment_PowerPagesScanReport_FileContent)
- [FileAttachment_Report_FileContent](#BKMK_FileAttachment_Report_FileContent)
- [FileAttachment_retaineddataexcel_ExcelContent](#BKMK_FileAttachment_retaineddataexcel_ExcelContent)
- [FileAttachment_searchcustomanalyzer_analyzers](#BKMK_FileAttachment_searchcustomanalyzer_analyzers)
- [fileattachment_solution_fileid](#BKMK_fileattachment_solution_fileid)
- [FileAttachment_StageSolutionUpload_SolutionFile](#BKMK_FileAttachment_StageSolutionUpload_SolutionFile)
- [FileAttachment_SyncErrors](#BKMK_FileAttachment_SyncErrors)
- [FileAttachment_WebResource_ContentFileRef](#BKMK_FileAttachment_WebResource_ContentFileRef)
- [FileAttachment_WebResource_ContentJsonFileRef](#BKMK_FileAttachment_WebResource_ContentJsonFileRef)
- [FileAttachment_workflowbinary_Data](#BKMK_FileAttachment_workflowbinary_Data)
- [FileAttachment_WorkflowLog_Inputs](#BKMK_FileAttachment_WorkflowLog_Inputs)
- [FileAttachment_WorkflowLog_Outputs](#BKMK_FileAttachment_WorkflowLog_Outputs)

### <a name="BKMK_FileAttachment_activityfileattachment_FileContent"></a> FileAttachment_activityfileattachment_FileContent

Many-To-One Relationship: [activityfileattachment FileAttachment_activityfileattachment_FileContent](activityfileattachment.md#BKMK_FileAttachment_activityfileattachment_FileContent)

|Property|Value|
|---|---|
|ReferencingEntity|`activityfileattachment`|
|ReferencingAttribute|`filecontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_activityfileattachment_FileContent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_ActivityPointer_DescriptionBlobId"></a> FileAttachment_ActivityPointer_DescriptionBlobId

Many-To-One Relationship: [activitypointer FileAttachment_ActivityPointer_DescriptionBlobId](activitypointer.md#BKMK_FileAttachment_ActivityPointer_DescriptionBlobId)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`descriptionblobid`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_ActivityPointer_DescriptionBlobId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_AsyncOperation_DataBlobId"></a> FileAttachment_AsyncOperation_DataBlobId

Many-To-One Relationship: [asyncoperation FileAttachment_AsyncOperation_DataBlobId](asyncoperation.md#BKMK_FileAttachment_AsyncOperation_DataBlobId)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`datablobid`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_AsyncOperation_DataBlobId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_botcomponent_FileData"></a> FileAttachment_botcomponent_FileData

Many-To-One Relationship: [botcomponent FileAttachment_botcomponent_FileData](botcomponent.md#BKMK_FileAttachment_botcomponent_FileData)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponent`|
|ReferencingAttribute|`filedata`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_botcomponent_FileData`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_Assets"></a> FileAttachment_CanvasApp_Assets

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_Assets](canvasapp.md#BKMK_FileAttachment_CanvasApp_Assets)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`assets`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_Assets`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_BackgroundImage"></a> FileAttachment_CanvasApp_BackgroundImage

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_BackgroundImage](canvasapp.md#BKMK_FileAttachment_CanvasApp_BackgroundImage)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`background_image`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_BackgroundImage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_Document"></a> FileAttachment_CanvasApp_Document

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_Document](canvasapp.md#BKMK_FileAttachment_CanvasApp_Document)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`document`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_Document`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_LargeIcon"></a> FileAttachment_CanvasApp_LargeIcon

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_LargeIcon](canvasapp.md#BKMK_FileAttachment_CanvasApp_LargeIcon)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`large_icon`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_LargeIcon`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_MediumIcon"></a> FileAttachment_CanvasApp_MediumIcon

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_MediumIcon](canvasapp.md#BKMK_FileAttachment_CanvasApp_MediumIcon)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`medium_icon`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_MediumIcon`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_SmallIcon"></a> FileAttachment_CanvasApp_SmallIcon

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_SmallIcon](canvasapp.md#BKMK_FileAttachment_CanvasApp_SmallIcon)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`small_icon`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_SmallIcon`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_TeamsIcon"></a> FileAttachment_CanvasApp_TeamsIcon

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_TeamsIcon](canvasapp.md#BKMK_FileAttachment_CanvasApp_TeamsIcon)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`teams_icon`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_TeamsIcon`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_CanvasApp_WideIcon"></a> FileAttachment_CanvasApp_WideIcon

Many-To-One Relationship: [canvasapp FileAttachment_CanvasApp_WideIcon](canvasapp.md#BKMK_FileAttachment_CanvasApp_WideIcon)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`wide_icon`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_CanvasApp_WideIcon`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_desktopflowbinary_Data"></a> FileAttachment_desktopflowbinary_Data

Many-To-One Relationship: [desktopflowbinary FileAttachment_desktopflowbinary_Data](desktopflowbinary.md#BKMK_FileAttachment_desktopflowbinary_Data)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowbinary`|
|ReferencingAttribute|`data`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_desktopflowbinary_Data`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_desktopflowmodule_Data"></a> FileAttachment_desktopflowmodule_Data

Many-To-One Relationship: [desktopflowmodule FileAttachment_desktopflowmodule_Data](desktopflowmodule.md#BKMK_FileAttachment_desktopflowmodule_Data)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowmodule`|
|ReferencingAttribute|`data`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_desktopflowmodule_Data`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_Email_DescriptionBlobId"></a> FileAttachment_Email_DescriptionBlobId

Many-To-One Relationship: [email FileAttachment_Email_DescriptionBlobId](email.md#BKMK_FileAttachment_Email_DescriptionBlobId)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`descriptionblobid`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_Email_DescriptionBlobId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_exportedexcel_ExcelContent"></a> FileAttachment_exportedexcel_ExcelContent

Many-To-One Relationship: [exportedexcel FileAttachment_exportedexcel_ExcelContent](exportedexcel.md#BKMK_FileAttachment_exportedexcel_ExcelContent)

|Property|Value|
|---|---|
|ReferencingEntity|`exportedexcel`|
|ReferencingAttribute|`excelcontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_exportedexcel_ExcelContent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_ExportSolutionUpload_SolutionFile"></a> FileAttachment_ExportSolutionUpload_SolutionFile

Many-To-One Relationship: [exportsolutionupload FileAttachment_ExportSolutionUpload_SolutionFile](exportsolutionupload.md#BKMK_FileAttachment_ExportSolutionUpload_SolutionFile)

|Property|Value|
|---|---|
|ReferencingEntity|`exportsolutionupload`|
|ReferencingAttribute|`solutionfile`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_ExportSolutionUpload_SolutionFile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_FlowSession_AdditionalContext"></a> FileAttachment_FlowSession_AdditionalContext

Many-To-One Relationship: [flowsession FileAttachment_FlowSession_AdditionalContext](flowsession.md#BKMK_FileAttachment_FlowSession_AdditionalContext)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`additionalcontext`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_flowsession_AdditionalContext`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_FlowSession_Inputs"></a> FileAttachment_FlowSession_Inputs

Many-To-One Relationship: [flowsession FileAttachment_FlowSession_Inputs](flowsession.md#BKMK_FileAttachment_FlowSession_Inputs)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`inputs`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_FlowSession_Inputs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_FlowSession_Outputs"></a> FileAttachment_FlowSession_Outputs

Many-To-One Relationship: [flowsession FileAttachment_FlowSession_Outputs](flowsession.md#BKMK_FileAttachment_FlowSession_Outputs)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`outputs`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_flowsession_Outputs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_KnowledgeArticle_msdyn_contentstore"></a> FileAttachment_KnowledgeArticle_msdyn_contentstore

Many-To-One Relationship: [knowledgearticle FileAttachment_KnowledgeArticle_msdyn_contentstore](knowledgearticle.md#BKMK_FileAttachment_KnowledgeArticle_msdyn_contentstore)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`msdyn_contentstore`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_KnowledgeArticle_msdyn_contentstore`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef"></a> FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef

Many-To-One Relationship: [mailbox FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef](mailbox.md#BKMK_FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`exchangesyncstatexmlfileref`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_Mailbox_ExchangeSyncStateXmlFileRef`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput"></a> FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput

Many-To-One Relationship: [msdyn_aibfeedbackloop FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput](msdyn_aibfeedbackloop.md#BKMK_FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfeedbackloop`|
|ReferencingAttribute|`msdyn_predictioninput`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionInput`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult"></a> FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult

Many-To-One Relationship: [msdyn_aibfeedbackloop FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult](msdyn_aibfeedbackloop.md#BKMK_FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfeedbackloop`|
|ReferencingAttribute|`msdyn_predictionresult`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_AIBFeedbackLoop_msdyn_PredictionResult`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_AIBFile_msdyn_File"></a> FileAttachment_msdyn_AIBFile_msdyn_File

Many-To-One Relationship: [msdyn_aibfile FileAttachment_msdyn_AIBFile_msdyn_File](msdyn_aibfile.md#BKMK_FileAttachment_msdyn_AIBFile_msdyn_File)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfile`|
|ReferencingAttribute|`msdyn_file`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_AIBFile_msdyn_File`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_AIConfiguration_msdyn_Model"></a> FileAttachment_msdyn_AIConfiguration_msdyn_Model

Many-To-One Relationship: [msdyn_aiconfiguration FileAttachment_msdyn_AIConfiguration_msdyn_Model](msdyn_aiconfiguration.md#BKMK_FileAttachment_msdyn_AIConfiguration_msdyn_Model)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiconfiguration`|
|ReferencingAttribute|`msdyn_model`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_AIConfiguration_msdyn_Model`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport"></a> FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport

Many-To-One Relationship: [msdyn_analysisjob FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport](msdyn_analysisjob.md#BKMK_FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisjob`|
|ReferencingAttribute|`msdyn_analysisjobsreport`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_FileUpload_msdyn_ErrorLog"></a> FileAttachment_msdyn_FileUpload_msdyn_ErrorLog

Many-To-One Relationship: [msdyn_fileupload FileAttachment_msdyn_FileUpload_msdyn_ErrorLog](msdyn_fileupload.md#BKMK_FileAttachment_msdyn_FileUpload_msdyn_ErrorLog)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_fileupload`|
|ReferencingAttribute|`msdyn_errorlog`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_FileUpload_msdyn_ErrorLog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_FileUpload_msdyn_FileContent"></a> FileAttachment_msdyn_FileUpload_msdyn_FileContent

Many-To-One Relationship: [msdyn_fileupload FileAttachment_msdyn_FileUpload_msdyn_FileContent](msdyn_fileupload.md#BKMK_FileAttachment_msdyn_FileUpload_msdyn_FileContent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_fileupload`|
|ReferencingAttribute|`msdyn_filecontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_FileUpload_msdyn_FileContent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample"></a> FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample

Many-To-One Relationship: [msdyn_integratedsearchprovider FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample](msdyn_integratedsearchprovider.md#BKMK_FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_integratedsearchprovider`|
|ReferencingAttribute|`msdyn_htmlsample`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_integratedsearchprovider_msdyn_htmlsample`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_kbattachment_msdyn_fileattachment"></a> FileAttachment_msdyn_kbattachment_msdyn_fileattachment

Many-To-One Relationship: [msdyn_kbattachment FileAttachment_msdyn_kbattachment_msdyn_fileattachment](msdyn_kbattachment.md#BKMK_FileAttachment_msdyn_kbattachment_msdyn_fileattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kbattachment`|
|ReferencingAttribute|`msdyn_fileattachment`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_kbattachment_msdyn_fileattachment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile"></a> FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile

Many-To-One Relationship: [msdyn_knowledgearticleimage FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile](msdyn_knowledgearticleimage.md#BKMK_FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticleimage`|
|ReferencingAttribute|`msdyn_blobfile`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_knowledgearticleimage_msdyn_BlobFile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appicon1024x1024`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIcon1024x1024`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appicon120x120`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIcon120x120`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appicon152x152`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIcon152x152`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appicon167x167`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIcon167x167`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180"></a> FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appicon180x180`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIcon180x180`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appiconhdpi`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIconHdpi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appiconmdpi`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIconMdpi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appiconxdpi`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIconXdpi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appiconxxhdpi`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIconXxhdpi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi"></a> FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_appiconxxxhdpi`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_appIconXxxhdpi`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_launchAppResources"></a> FileAttachment_msdyn_mobileapp_msdyn_launchAppResources

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_launchAppResources](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_launchAppResources)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_launchappresources`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_launchAppResources`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid"></a> FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_mobileappdefinitionandroid`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionAndroid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS"></a> FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_mobileappdefinitionios`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_mobileAppDefinitionIOS`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage"></a> FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_prodev_custompackage`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_proDev_customPackage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson"></a> FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_pushnotificationsandroidjson`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsAndroidJson`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist"></a> FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_pushnotificationsiosplist`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_pushNotificationsIosPlist`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage"></a> FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_tenantsplashimage`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_tenantSplashImage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage"></a> FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage

Many-To-One Relationship: [msdyn_mobileapp FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage](msdyn_mobileapp.md#BKMK_FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`msdyn_tenantwelcomeimage`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_mobileapp_msdyn_tenantWelcomeImage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport"></a> FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport

Many-To-One Relationship: [msdyn_pminferredtask FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport](msdyn_pminferredtask.md#BKMK_FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pminferredtask`|
|ReferencingAttribute|`msdyn_lasterrorsreport`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_msdyn_richtextfile_msdyn_fileblob"></a> FileAttachment_msdyn_richtextfile_msdyn_fileblob

Many-To-One Relationship: [msdyn_richtextfile FileAttachment_msdyn_richtextfile_msdyn_fileblob](msdyn_richtextfile.md#BKMK_FileAttachment_msdyn_richtextfile_msdyn_fileblob)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_richtextfile`|
|ReferencingAttribute|`msdyn_fileblob`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_msdyn_richtextfile_msdyn_fileblob`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File"></a> FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File

Many-To-One Relationship: [mspcat_catalogsubmissionfiles FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File](mspcat_catalogsubmissionfiles.md#BKMK_FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_catalogsubmissionfiles`|
|ReferencingAttribute|`mspcat_file`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_mspcat_CatalogSubmissionFiles_mspcat_File`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_mspcat_PackageStore_mspcat_PackageFile"></a> FileAttachment_mspcat_PackageStore_mspcat_PackageFile

Many-To-One Relationship: [mspcat_packagestore FileAttachment_mspcat_PackageStore_mspcat_PackageFile](mspcat_packagestore.md#BKMK_FileAttachment_mspcat_PackageStore_mspcat_PackageFile)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_packagestore`|
|ReferencingAttribute|`mspcat_packagefile`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_mspcat_PackageStore_mspcat_PackageFile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_package_DeploymentLog"></a> FileAttachment_package_DeploymentLog

Many-To-One Relationship: [package FileAttachment_package_DeploymentLog](package.md#BKMK_FileAttachment_package_DeploymentLog)

|Property|Value|
|---|---|
|ReferencingEntity|`package`|
|ReferencingAttribute|`deploymentlog`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_package_DeploymentLog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_packagehistory_DeploymentLog"></a> FileAttachment_packagehistory_DeploymentLog

Many-To-One Relationship: [packagehistory FileAttachment_packagehistory_DeploymentLog](packagehistory.md#BKMK_FileAttachment_packagehistory_DeploymentLog)

|Property|Value|
|---|---|
|ReferencingEntity|`packagehistory`|
|ReferencingAttribute|`deploymentlog`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_packagehistory_DeploymentLog`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_pluginpackage_FileId"></a> FileAttachment_pluginpackage_FileId

Many-To-One Relationship: [pluginpackage FileAttachment_pluginpackage_FileId](pluginpackage.md#BKMK_FileAttachment_pluginpackage_FileId)

|Property|Value|
|---|---|
|ReferencingEntity|`pluginpackage`|
|ReferencingAttribute|`fileid`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_pluginpackage_FileId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_pluginpackage_Package"></a> FileAttachment_pluginpackage_Package

Many-To-One Relationship: [pluginpackage FileAttachment_pluginpackage_Package](pluginpackage.md#BKMK_FileAttachment_pluginpackage_Package)

|Property|Value|
|---|---|
|ReferencingEntity|`pluginpackage`|
|ReferencingAttribute|`package`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_pluginpackage_Package`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_powerbidataset_Package"></a> FileAttachment_powerbidataset_Package

Many-To-One Relationship: [powerbidataset FileAttachment_powerbidataset_Package](powerbidataset.md#BKMK_FileAttachment_powerbidataset_Package)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidataset`|
|ReferencingAttribute|`package`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_powerbidataset_Package`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_powerbireport_Package"></a> FileAttachment_powerbireport_Package

Many-To-One Relationship: [powerbireport FileAttachment_powerbireport_Package](powerbireport.md#BKMK_FileAttachment_powerbireport_Package)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireport`|
|ReferencingAttribute|`package`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_powerbireport_Package`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_powerpagecomponent_filecontent"></a> FileAttachment_powerpagecomponent_filecontent

Many-To-One Relationship: [powerpagecomponent FileAttachment_powerpagecomponent_filecontent](powerpagecomponent.md#BKMK_FileAttachment_powerpagecomponent_filecontent)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagecomponent`|
|ReferencingAttribute|`filecontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_powerpagecomponent_filecontent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_powerpagesitepublished_publishedmetadata"></a> FileAttachment_powerpagesitepublished_publishedmetadata

Many-To-One Relationship: [powerpagesitepublished FileAttachment_powerpagesitepublished_publishedmetadata](powerpagesitepublished.md#BKMK_FileAttachment_powerpagesitepublished_publishedmetadata)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitepublished`|
|ReferencingAttribute|`publishedmetadata`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_powerpagesitepublished_publishedmetadata`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_powerpagesitepublished_publishedsource"></a> FileAttachment_powerpagesitepublished_publishedsource

Many-To-One Relationship: [powerpagesitepublished FileAttachment_powerpagesitepublished_publishedsource](powerpagesitepublished.md#BKMK_FileAttachment_powerpagesitepublished_publishedsource)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitepublished`|
|ReferencingAttribute|`publishedsource`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_powerpagesitepublished_publishedsource`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_PowerPagesScanReport_FileContent"></a> FileAttachment_PowerPagesScanReport_FileContent

Many-To-One Relationship: [powerpagesscanreport FileAttachment_PowerPagesScanReport_FileContent](powerpagesscanreport.md#BKMK_FileAttachment_PowerPagesScanReport_FileContent)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesscanreport`|
|ReferencingAttribute|`filecontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_PowerPagesScanReport_FileContent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_Report_FileContent"></a> FileAttachment_Report_FileContent

Many-To-One Relationship: [report FileAttachment_Report_FileContent](report.md#BKMK_FileAttachment_Report_FileContent)

|Property|Value|
|---|---|
|ReferencingEntity|`report`|
|ReferencingAttribute|`filecontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_Report_FileContent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_retaineddataexcel_ExcelContent"></a> FileAttachment_retaineddataexcel_ExcelContent

Many-To-One Relationship: [retaineddataexcel FileAttachment_retaineddataexcel_ExcelContent](retaineddataexcel.md#BKMK_FileAttachment_retaineddataexcel_ExcelContent)

|Property|Value|
|---|---|
|ReferencingEntity|`retaineddataexcel`|
|ReferencingAttribute|`excelcontent`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_retaineddataexcel_ExcelContent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_searchcustomanalyzer_analyzers"></a> FileAttachment_searchcustomanalyzer_analyzers

Many-To-One Relationship: [searchcustomanalyzer FileAttachment_searchcustomanalyzer_analyzers](searchcustomanalyzer.md#BKMK_FileAttachment_searchcustomanalyzer_analyzers)

|Property|Value|
|---|---|
|ReferencingEntity|`searchcustomanalyzer`|
|ReferencingAttribute|`analyzers`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_searchcustomanalyzer_analyzers`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_fileattachment_solution_fileid"></a> fileattachment_solution_fileid

Many-To-One Relationship: [solution fileattachment_solution_fileid](solution.md#BKMK_fileattachment_solution_fileid)

|Property|Value|
|---|---|
|ReferencingEntity|`solution`|
|ReferencingAttribute|`fileid`|
|ReferencedEntityNavigationPropertyName|`solution_fileid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_StageSolutionUpload_SolutionFile"></a> FileAttachment_StageSolutionUpload_SolutionFile

Many-To-One Relationship: [stagesolutionupload FileAttachment_StageSolutionUpload_SolutionFile](stagesolutionupload.md#BKMK_FileAttachment_StageSolutionUpload_SolutionFile)

|Property|Value|
|---|---|
|ReferencingEntity|`stagesolutionupload`|
|ReferencingAttribute|`solutionfile`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_StageSolutionUpload_SolutionFile`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_SyncErrors"></a> FileAttachment_SyncErrors

Many-To-One Relationship: [syncerror FileAttachment_SyncErrors](syncerror.md#BKMK_FileAttachment_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_WebResource_ContentFileRef"></a> FileAttachment_WebResource_ContentFileRef

Many-To-One Relationship: [webresource FileAttachment_WebResource_ContentFileRef](webresource.md#BKMK_FileAttachment_WebResource_ContentFileRef)

|Property|Value|
|---|---|
|ReferencingEntity|`webresource`|
|ReferencingAttribute|`contentfileref`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_WebResource_ContentFileRef`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_WebResource_ContentJsonFileRef"></a> FileAttachment_WebResource_ContentJsonFileRef

Many-To-One Relationship: [webresource FileAttachment_WebResource_ContentJsonFileRef](webresource.md#BKMK_FileAttachment_WebResource_ContentJsonFileRef)

|Property|Value|
|---|---|
|ReferencingEntity|`webresource`|
|ReferencingAttribute|`contentjsonfileref`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_WebResource_ContentJsonFileRef`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_workflowbinary_Data"></a> FileAttachment_workflowbinary_Data

Many-To-One Relationship: [workflowbinary FileAttachment_workflowbinary_Data](workflowbinary.md#BKMK_FileAttachment_workflowbinary_Data)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowbinary`|
|ReferencingAttribute|`data`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_workflowbinary_Data`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_WorkflowLog_Inputs"></a> FileAttachment_WorkflowLog_Inputs

Many-To-One Relationship: [workflowlog FileAttachment_WorkflowLog_Inputs](workflowlog.md#BKMK_FileAttachment_WorkflowLog_Inputs)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`inputs`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_workflowlog_Inputs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_FileAttachment_WorkflowLog_Outputs"></a> FileAttachment_WorkflowLog_Outputs

Many-To-One Relationship: [workflowlog FileAttachment_WorkflowLog_Outputs](workflowlog.md#BKMK_FileAttachment_WorkflowLog_Outputs)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`outputs`|
|ReferencedEntityNavigationPropertyName|`FileAttachment_workflowlog_Outputs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.fileattachment?displayProperty=fullName>
