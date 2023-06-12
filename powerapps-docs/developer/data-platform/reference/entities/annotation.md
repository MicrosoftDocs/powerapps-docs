---
title: "Note (Annotation)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Note (Annotation)  table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Note (Annotation)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Note that is attached to one or more objects, including other notes.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /annotations(*annotationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST /annotations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /annotations(*annotationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET /annotations(*annotationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /annotations<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|Rollup|<xref:Microsoft.Dynamics.CRM.Rollup?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RollupRequest>|
|Update|PATCH /annotations(*annotationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Annotations|
|DisplayCollectionName|Notes|
|DisplayName|Note|
|EntitySetName|annotations|
|IsBPFEntity|False|
|LogicalCollectionName|annotations|
|LogicalName|annotation|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|annotationid|
|PrimaryNameAttribute|subject|
|SchemaName|Annotation|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AnnotationId](#BKMK_AnnotationId)
- [DocumentBody](#BKMK_DocumentBody)
- [FileName](#BKMK_FileName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsDocument](#BKMK_IsDocument)
- [LangId](#BKMK_LangId)
- [MimeType](#BKMK_MimeType)
- [NoteText](#BKMK_NoteText)
- [ObjectId](#BKMK_ObjectId)
- [ObjectIdTypeCode](#BKMK_ObjectIdTypeCode)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [StepId](#BKMK_StepId)
- [Subject](#BKMK_Subject)


### <a name="BKMK_AnnotationId"></a> AnnotationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the note.|
|DisplayName|Note|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|annotationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_DocumentBody"></a> DocumentBody

|Property|Value|
|--------|-----|
|Description|Contents of the note's attachment.|
|DisplayName|Document|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|documentbody|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_FileName"></a> FileName

|Property|Value|
|--------|-----|
|Description|File name of the note.|
|DisplayName|File Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filename|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Unique identifier of the data import or data migration that created this record.|
|DisplayName|Import Sequence Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|importsequencenumber|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsDocument"></a> IsDocument

|Property|Value|
|--------|-----|
|Description|Specifies whether the note is an attachment.|
|DisplayName|Is Document|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|isdocument|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDocument Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_LangId"></a> LangId

|Property|Value|
|--------|-----|
|Description|Language identifier for the note.|
|DisplayName|Language ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|langid|
|MaxLength|2|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_MimeType"></a> MimeType

|Property|Value|
|--------|-----|
|Description|MIME type of the note's attachment.|
|DisplayName|Mime Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|mimetype|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_NoteText"></a> NoteText

|Property|Value|
|--------|-----|
|Description|Text of the note.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|notetext|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ObjectId"></a> ObjectId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the object with which the note is associated.|
|DisplayName|Regarding|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectid|
|RequiredLevel|None|
|Targets|account,appointment,calendar,channelaccessprofile,channelaccessprofilerule,channelaccessprofileruleitem,chat,contact,convertrule,duplicaterule,email,emailserverprofile,fax,goal,kbarticle,knowledgearticle,knowledgebaserecord,letter,mailbox,msdyn_aifptrainingdocument,msdyn_aimodel,msdyn_aiodimage,mspcat_catalogsubmissionfiles,phonecall,recurringappointmentmaster,routingrule,routingruleitem,sharepointdocument,sla,socialactivity,task,workflow|
|Type|Lookup|


### <a name="BKMK_ObjectIdTypeCode"></a> ObjectIdTypeCode

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Regarding Object Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objectidtypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of entity with which the note is associated.|
|DisplayName|Object Type |
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|objecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time that the record was migrated.|
|DisplayName|Record Created On|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|overriddencreatedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the note.|
|DisplayName|Owner|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


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


### <a name="BKMK_StepId"></a> StepId

|Property|Value|
|--------|-----|
|Description|workflow step id associated with the note.|
|DisplayName|Step Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stepid|
|MaxLength|32|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_Subject"></a> Subject

|Property|Value|
|--------|-----|
|Description|Subject associated with the note.|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subject|
|MaxLength|500|
|RequiredLevel|ApplicationRequired|
|Type|String|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DummyFileName](#BKMK_DummyFileName)
- [DummyRegarding](#BKMK_DummyRegarding)
- [FilePointer](#BKMK_FilePointer)
- [FileSize](#BKMK_FileSize)
- [IsPrivate](#BKMK_IsPrivate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Prefix](#BKMK_Prefix)
- [StoragePointer](#BKMK_StoragePointer)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the note.|
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


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createdbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the note was created.|
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
|Description|Unique identifier of the delegate user who created the annotation.|
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


### <a name="BKMK_DummyFileName"></a> DummyFileName

**Added by**: Activities Patch Solution

|Property|Value|
|--------|-----|
|Description|Dummy attribute associated with the note attachment|
|DisplayName|File Name(deprecated)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|dummyfilename|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_DummyRegarding"></a> DummyRegarding

**Added by**: Activities Patch Solution

|Property|Value|
|--------|-----|
|Description|Dummy attribute associated with the note regarding|
|DisplayName|Regarding(deprecated)|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|False|
|LogicalName|dummyregarding|
|MaxLength|500|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_FileSize"></a> FileSize

|Property|Value|
|--------|-----|
|Description|File size of the note.|
|DisplayName|File Size (Bytes)|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|filesize|
|MaxValue|1000000000|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_IsPrivate"></a> IsPrivate

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|isprivate|
|RequiredLevel|None|
|Type|Boolean|

#### IsPrivate Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the note.|
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


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedbyyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the note was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the annotation.|
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


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridyominame|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the note.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the note.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the note.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_Prefix"></a> Prefix

|Property|Value|
|--------|-----|
|Description|Prefix of the file pointer in blob storage.|
|DisplayName|Prefix|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
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
|Description|Version number of the note.|
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

- [Annotation_SyncErrors](#BKMK_Annotation_SyncErrors)
- [Annotation_AsyncOperations](#BKMK_Annotation_AsyncOperations)
- [Annotation_BulkDeleteFailures](#BKMK_Annotation_BulkDeleteFailures)
- [Annotation_ProcessSessions](#BKMK_Annotation_ProcessSessions)


### <a name="BKMK_Annotation_SyncErrors"></a> Annotation_SyncErrors

Same as the [Annotation_SyncErrors](syncerror.md#BKMK_Annotation_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Annotation_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_Annotation_AsyncOperations"></a> Annotation_AsyncOperations

Same as the [Annotation_AsyncOperations](asyncoperation.md#BKMK_Annotation_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Annotation_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Annotation_BulkDeleteFailures"></a> Annotation_BulkDeleteFailures

Same as the [Annotation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Annotation_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Annotation_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Annotation_ProcessSessions"></a> Annotation_ProcessSessions

Same as the [Annotation_ProcessSessions](processsession.md#BKMK_Annotation_ProcessSessions) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Annotation_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [knowledgearticle_Annotations](#BKMK_knowledgearticle_Annotations)
- [KnowledgeBaseRecord_Annotations](#BKMK_KnowledgeBaseRecord_Annotations)
- [lk_annotationbase_modifiedonbehalfby](#BKMK_lk_annotationbase_modifiedonbehalfby)
- [Mailbox_Annotation](#BKMK_Mailbox_Annotation)
- [team_annotations](#BKMK_team_annotations)
- [annotation_owning_user](#BKMK_annotation_owning_user)
- [PhoneCall_Annotation](#BKMK_PhoneCall_Annotation)
- [Contact_Annotation](#BKMK_Contact_Annotation)
- [SocialActivity_Annotation](#BKMK_SocialActivity_Annotation)
- [sla_Annotation](#BKMK_sla_Annotation)
- [Calendar_Annotation](#BKMK_Calendar_Annotation)
- [Email_Annotation](#BKMK_Email_Annotation)
- [Task_Annotation](#BKMK_Task_Annotation)
- [lk_annotationbase_createdby](#BKMK_lk_annotationbase_createdby)
- [EmailServerProfile_Annotation](#BKMK_EmailServerProfile_Annotation)
- [Account_Annotation](#BKMK_Account_Annotation)
- [RecurringAppointmentMaster_Annotation](#BKMK_RecurringAppointmentMaster_Annotation)
- [business_unit_annotations](#BKMK_business_unit_annotations)
- [lk_annotationbase_modifiedby](#BKMK_lk_annotationbase_modifiedby)
- [Letter_Annotation](#BKMK_Letter_Annotation)
- [Fax_Annotation](#BKMK_Fax_Annotation)
- [Workflow_Annotation](#BKMK_Workflow_Annotation)
- [Appointment_Annotation](#BKMK_Appointment_Annotation)
- [lk_annotationbase_createdonbehalfby](#BKMK_lk_annotationbase_createdonbehalfby)
- [Goal_Annotation](#BKMK_Goal_Annotation)
- [KbArticle_Annotation](#BKMK_KbArticle_Annotation)
- [DuplicateRule_Annotation](#BKMK_DuplicateRule_Annotation)
- [chat_Annotations](#BKMK_chat_Annotations)
- [msdyn_aimodel_Annotations](#BKMK_msdyn_aimodel_Annotations)
- [msdyn_aifptrainingdocument_Annotations](#BKMK_msdyn_aifptrainingdocument_Annotations)
- [msdyn_aiodimage_Annotations](#BKMK_msdyn_aiodimage_Annotations)
- [mspcat_catalogsubmissionfiles_Annotations](#BKMK_mspcat_catalogsubmissionfiles_Annotations)


### <a name="BKMK_knowledgearticle_Annotations"></a> knowledgearticle_Annotations

See the [knowledgearticle_Annotations](knowledgearticle.md#BKMK_knowledgearticle_Annotations) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_KnowledgeBaseRecord_Annotations"></a> KnowledgeBaseRecord_Annotations

See the [KnowledgeBaseRecord_Annotations](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Annotations) one-to-many relationship for the [knowledgebaserecord](knowledgebaserecord.md) table/entity.

### <a name="BKMK_lk_annotationbase_modifiedonbehalfby"></a> lk_annotationbase_modifiedonbehalfby

See the [lk_annotationbase_modifiedonbehalfby](systemuser.md#BKMK_lk_annotationbase_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Mailbox_Annotation"></a> Mailbox_Annotation

See the [Mailbox_Annotation](mailbox.md#BKMK_Mailbox_Annotation) one-to-many relationship for the [mailbox](mailbox.md) table/entity.

### <a name="BKMK_team_annotations"></a> team_annotations

See the [team_annotations](team.md#BKMK_team_annotations) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_annotation_owning_user"></a> annotation_owning_user

See the [annotation_owning_user](systemuser.md#BKMK_annotation_owning_user) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_PhoneCall_Annotation"></a> PhoneCall_Annotation

See the [PhoneCall_Annotation](phonecall.md#BKMK_PhoneCall_Annotation) one-to-many relationship for the [phonecall](phonecall.md) table/entity.

### <a name="BKMK_Contact_Annotation"></a> Contact_Annotation

See the [Contact_Annotation](contact.md#BKMK_Contact_Annotation) one-to-many relationship for the [contact](contact.md) table/entity.

### <a name="BKMK_SocialActivity_Annotation"></a> SocialActivity_Annotation

See the [SocialActivity_Annotation](socialactivity.md#BKMK_SocialActivity_Annotation) one-to-many relationship for the [socialactivity](socialactivity.md) table/entity.

### <a name="BKMK_sla_Annotation"></a> sla_Annotation

See the [sla_Annotation](sla.md#BKMK_sla_Annotation) one-to-many relationship for the [sla](sla.md) table/entity.

### <a name="BKMK_Calendar_Annotation"></a> Calendar_Annotation

See the [Calendar_Annotation](calendar.md#BKMK_Calendar_Annotation) one-to-many relationship for the [calendar](calendar.md) table/entity.

### <a name="BKMK_Email_Annotation"></a> Email_Annotation

See the [Email_Annotation](email.md#BKMK_Email_Annotation) one-to-many relationship for the [email](email.md) table/entity.

### <a name="BKMK_Task_Annotation"></a> Task_Annotation

See the [Task_Annotation](task.md#BKMK_Task_Annotation) one-to-many relationship for the [task](task.md) table/entity.

### <a name="BKMK_lk_annotationbase_createdby"></a> lk_annotationbase_createdby

See the [lk_annotationbase_createdby](systemuser.md#BKMK_lk_annotationbase_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_EmailServerProfile_Annotation"></a> EmailServerProfile_Annotation

See the [EmailServerProfile_Annotation](emailserverprofile.md#BKMK_EmailServerProfile_Annotation) one-to-many relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

### <a name="BKMK_Account_Annotation"></a> Account_Annotation

See the [Account_Annotation](account.md#BKMK_Account_Annotation) one-to-many relationship for the [account](account.md) table/entity.

### <a name="BKMK_RecurringAppointmentMaster_Annotation"></a> RecurringAppointmentMaster_Annotation

See the [RecurringAppointmentMaster_Annotation](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_Annotation) one-to-many relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

### <a name="BKMK_business_unit_annotations"></a> business_unit_annotations

See the [business_unit_annotations](businessunit.md#BKMK_business_unit_annotations) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_lk_annotationbase_modifiedby"></a> lk_annotationbase_modifiedby

See the [lk_annotationbase_modifiedby](systemuser.md#BKMK_lk_annotationbase_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Letter_Annotation"></a> Letter_Annotation

See the [Letter_Annotation](letter.md#BKMK_Letter_Annotation) one-to-many relationship for the [letter](letter.md) table/entity.

### <a name="BKMK_Fax_Annotation"></a> Fax_Annotation

See the [Fax_Annotation](fax.md#BKMK_Fax_Annotation) one-to-many relationship for the [fax](fax.md) table/entity.

### <a name="BKMK_Workflow_Annotation"></a> Workflow_Annotation

See the [Workflow_Annotation](workflow.md#BKMK_Workflow_Annotation) one-to-many relationship for the [workflow](workflow.md) table/entity.

### <a name="BKMK_Appointment_Annotation"></a> Appointment_Annotation

See the [Appointment_Annotation](appointment.md#BKMK_Appointment_Annotation) one-to-many relationship for the [appointment](appointment.md) table/entity.

### <a name="BKMK_lk_annotationbase_createdonbehalfby"></a> lk_annotationbase_createdonbehalfby

See the [lk_annotationbase_createdonbehalfby](systemuser.md#BKMK_lk_annotationbase_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_Goal_Annotation"></a> Goal_Annotation

See the [Goal_Annotation](goal.md#BKMK_Goal_Annotation) one-to-many relationship for the [goal](goal.md) table/entity.

### <a name="BKMK_KbArticle_Annotation"></a> KbArticle_Annotation

See the [KbArticle_Annotation](kbarticle.md#BKMK_KbArticle_Annotation) one-to-many relationship for the [kbarticle](kbarticle.md) table/entity.

### <a name="BKMK_DuplicateRule_Annotation"></a> DuplicateRule_Annotation

See the [DuplicateRule_Annotation](duplicaterule.md#BKMK_DuplicateRule_Annotation) one-to-many relationship for the [duplicaterule](duplicaterule.md) table/entity.

### <a name="BKMK_chat_Annotations"></a> chat_Annotations

**Added by**: Activities Patch Solution

See the [chat_Annotations](chat.md#BKMK_chat_Annotations) one-to-many relationship for the [chat](chat.md) table/entity.

### <a name="BKMK_msdyn_aimodel_Annotations"></a> msdyn_aimodel_Annotations

**Added by**: AISolution Solution

See the [msdyn_aimodel_Annotations](msdyn_aimodel.md#BKMK_msdyn_aimodel_Annotations) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### <a name="BKMK_msdyn_aifptrainingdocument_Annotations"></a> msdyn_aifptrainingdocument_Annotations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aifptrainingdocument_Annotations](msdyn_aifptrainingdocument.md#BKMK_msdyn_aifptrainingdocument_Annotations) one-to-many relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

### <a name="BKMK_msdyn_aiodimage_Annotations"></a> msdyn_aiodimage_Annotations

**Added by**: AI Solution deprecated templates Solution

See the [msdyn_aiodimage_Annotations](msdyn_aiodimage.md#BKMK_msdyn_aiodimage_Annotations) one-to-many relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

### <a name="BKMK_mspcat_catalogsubmissionfiles_Annotations"></a> mspcat_catalogsubmissionfiles_Annotations

**Added by**: Power Platform Catalog Client Packaging Solution

See the [mspcat_catalogsubmissionfiles_Annotations](mspcat_catalogsubmissionfiles.md#BKMK_mspcat_catalogsubmissionfiles_Annotations) one-to-many relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.annotation?text=annotation EntityType" />