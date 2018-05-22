---
title: "Annotation Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Annotation entity."

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
# Annotation Entity Reference

Note that is attached to one or more objects, including other notes.

## Entity Properties

**DisplayName**: Note<br />
**DisplayCollectionName**: Notes<br />
**SchemaName**: Annotation<br />
**CollectionSchemaName**: Annotations<br />
**LogicalName**: annotation<br />
**LogicalCollectionName**: annotations<br />
**EntitySetName**: annotations<br />
**PrimaryIdAttribute**: annotationid<br />
**PrimaryNameAttribute**: subject<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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

**Description**: Unique identifier of the note.<br />
**DisplayName**: Note<br />
**LogicalName**: annotationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_DocumentBody"></a> DocumentBody

**Description**: Contents of the note's attachment.<br />
**DisplayName**: Document<br />
**LogicalName**: documentbody<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_FileName"></a> FileName

**Description**: File name of the note.<br />
**DisplayName**: File Name<br />
**LogicalName**: filename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Unique identifier of the data import or data migration that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IsDocument"></a> IsDocument

**Description**: Specifies whether the note is an attachment.<br />
**DisplayName**: Is Document<br />
**LogicalName**: isdocument<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LangId"></a> LangId

**Description**: Language identifier for the note.<br />
**DisplayName**: Language ID<br />
**LogicalName**: langid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2


### <a name="BKMK_MimeType"></a> MimeType

**Description**: MIME type of the note's attachment.<br />
**DisplayName**: Mime Type<br />
**LogicalName**: mimetype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_NoteText"></a> NoteText

**Description**: Text of the note.<br />
**DisplayName**: Description<br />
**LogicalName**: notetext<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Unique identifier of the object with which the note is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: objectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,appointment,calendar,channelaccessprofile,channelaccessprofilerule,channelaccessprofileruleitem,contact,convertrule,duplicaterule,email,emailserverprofile,fax,goal,kbarticle,knowledgearticle,knowledgebaserecord,letter,mailbox,phonecall,recurringappointmentmaster,routingrule,routingruleitem,sharepointdocument,sla,socialactivity,task,workflow


### <a name="BKMK_ObjectIdTypeCode"></a> ObjectIdTypeCode

**Description**: <br />
**DisplayName**: Regarding Object Type<br />
**LogicalName**: objectidtypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Type of entity with which the note is associated.<br />
**DisplayName**: Object Type <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the note.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_StepId"></a> StepId

**Description**: workflow step id associated with the note.<br />
**DisplayName**: Step Id<br />
**LogicalName**: stepid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 32


### <a name="BKMK_Subject"></a> Subject

**Description**: Subject associated with the note.<br />
**DisplayName**: Title<br />
**LogicalName**: subject<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
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
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the note.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the note was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the annotation.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FileSize"></a> FileSize

**Description**: File size of the note.<br />
**DisplayName**: File Size (Bytes)<br />
**LogicalName**: filesize<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_IsPrivate"></a> IsPrivate

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: isprivate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the note.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the note was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the annotation.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the note.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the note.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the note.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the note.<br />
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

- [Annotation_SyncErrors](#BKMK_Annotation_SyncErrors)
- [Annotation_AsyncOperations](#BKMK_Annotation_AsyncOperations)
- [userentityinstancedata_annotation](#BKMK_userentityinstancedata_annotation)
- [Annotation_BulkDeleteFailures](#BKMK_Annotation_BulkDeleteFailures)
- [Annotation_ProcessSessions](#BKMK_Annotation_ProcessSessions)


### <a name="BKMK_Annotation_SyncErrors"></a> Annotation_SyncErrors

Same as syncerror entity [Annotation_SyncErrors](syncerror.md#BKMK_Annotation_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Annotation_SyncErrors<br />
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


### <a name="BKMK_Annotation_AsyncOperations"></a> Annotation_AsyncOperations

Same as asyncoperation entity [Annotation_AsyncOperations](asyncoperation.md#BKMK_Annotation_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Annotation_AsyncOperations<br />
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


### <a name="BKMK_userentityinstancedata_annotation"></a> userentityinstancedata_annotation

Same as userentityinstancedata entity [userentityinstancedata_annotation](userentityinstancedata.md#BKMK_userentityinstancedata_annotation) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_annotation<br />
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


### <a name="BKMK_Annotation_BulkDeleteFailures"></a> Annotation_BulkDeleteFailures

Same as bulkdeletefailure entity [Annotation_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Annotation_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Annotation_BulkDeleteFailures<br />
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


### <a name="BKMK_Annotation_ProcessSessions"></a> Annotation_ProcessSessions

Same as processsession entity [Annotation_ProcessSessions](processsession.md#BKMK_Annotation_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Annotation_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [knowledgearticle_Annotations](#BKMK_knowledgearticle_Annotations)
- [channelaccessprofile_Annotations](#BKMK_channelaccessprofile_Annotations)
- [profilerule_Annotations](#BKMK_profilerule_Annotations)
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
- [ConvertRule_Annotation](#BKMK_ConvertRule_Annotation)
- [lk_annotationbase_createdby](#BKMK_lk_annotationbase_createdby)
- [EmailServerProfile_Annotation](#BKMK_EmailServerProfile_Annotation)
- [Account_Annotation](#BKMK_Account_Annotation)
- [RecurringAppointmentMaster_Annotation](#BKMK_RecurringAppointmentMaster_Annotation)
- [routingrule_Annotation](#BKMK_routingrule_Annotation)
- [business_unit_annotations](#BKMK_business_unit_annotations)
- [lk_annotationbase_modifiedby](#BKMK_lk_annotationbase_modifiedby)
- [Letter_Annotation](#BKMK_Letter_Annotation)
- [Fax_Annotation](#BKMK_Fax_Annotation)
- [profileruleitem_Annotations](#BKMK_profileruleitem_Annotations)
- [Workflow_Annotation](#BKMK_Workflow_Annotation)
- [routingruleitem_Annotation](#BKMK_routingruleitem_Annotation)
- [Appointment_Annotation](#BKMK_Appointment_Annotation)
- [lk_annotationbase_createdonbehalfby](#BKMK_lk_annotationbase_createdonbehalfby)
- [Goal_Annotation](#BKMK_Goal_Annotation)
- [KbArticle_Annotation](#BKMK_KbArticle_Annotation)
- [SharePointDocument_Annotation](#BKMK_SharePointDocument_Annotation)
- [DuplicateRule_Annotation](#BKMK_DuplicateRule_Annotation)


### <a name="BKMK_knowledgearticle_Annotations"></a> knowledgearticle_Annotations

See knowledgearticle Entity [knowledgearticle_Annotations](knowledgearticle.md#BKMK_knowledgearticle_Annotations) One-To-Many relationship.

### <a name="BKMK_channelaccessprofile_Annotations"></a> channelaccessprofile_Annotations

See channelaccessprofile Entity [channelaccessprofile_Annotations](channelaccessprofile.md#BKMK_channelaccessprofile_Annotations) One-To-Many relationship.

### <a name="BKMK_profilerule_Annotations"></a> profilerule_Annotations

See channelaccessprofilerule Entity [profilerule_Annotations](channelaccessprofilerule.md#BKMK_profilerule_Annotations) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_Annotations"></a> KnowledgeBaseRecord_Annotations

See knowledgebaserecord Entity [KnowledgeBaseRecord_Annotations](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_Annotations) One-To-Many relationship.

### <a name="BKMK_lk_annotationbase_modifiedonbehalfby"></a> lk_annotationbase_modifiedonbehalfby

See systemuser Entity [lk_annotationbase_modifiedonbehalfby](systemuser.md#BKMK_lk_annotationbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Mailbox_Annotation"></a> Mailbox_Annotation

See mailbox Entity [Mailbox_Annotation](mailbox.md#BKMK_Mailbox_Annotation) One-To-Many relationship.

### <a name="BKMK_team_annotations"></a> team_annotations

See team Entity [team_annotations](team.md#BKMK_team_annotations) One-To-Many relationship.

### <a name="BKMK_annotation_owning_user"></a> annotation_owning_user

See systemuser Entity [annotation_owning_user](systemuser.md#BKMK_annotation_owning_user) One-To-Many relationship.

### <a name="BKMK_PhoneCall_Annotation"></a> PhoneCall_Annotation

See phonecall Entity [PhoneCall_Annotation](phonecall.md#BKMK_PhoneCall_Annotation) One-To-Many relationship.

### <a name="BKMK_Contact_Annotation"></a> Contact_Annotation

See contact Entity [Contact_Annotation](contact.md#BKMK_Contact_Annotation) One-To-Many relationship.

### <a name="BKMK_SocialActivity_Annotation"></a> SocialActivity_Annotation

See socialactivity Entity [SocialActivity_Annotation](socialactivity.md#BKMK_SocialActivity_Annotation) One-To-Many relationship.

### <a name="BKMK_sla_Annotation"></a> sla_Annotation

See sla Entity [sla_Annotation](sla.md#BKMK_sla_Annotation) One-To-Many relationship.

### <a name="BKMK_Calendar_Annotation"></a> Calendar_Annotation

See calendar Entity [Calendar_Annotation](calendar.md#BKMK_Calendar_Annotation) One-To-Many relationship.

### <a name="BKMK_Email_Annotation"></a> Email_Annotation

See email Entity [Email_Annotation](email.md#BKMK_Email_Annotation) One-To-Many relationship.

### <a name="BKMK_Task_Annotation"></a> Task_Annotation

See task Entity [Task_Annotation](task.md#BKMK_Task_Annotation) One-To-Many relationship.

### <a name="BKMK_ConvertRule_Annotation"></a> ConvertRule_Annotation

See convertrule Entity [ConvertRule_Annotation](convertrule.md#BKMK_ConvertRule_Annotation) One-To-Many relationship.

### <a name="BKMK_lk_annotationbase_createdby"></a> lk_annotationbase_createdby

See systemuser Entity [lk_annotationbase_createdby](systemuser.md#BKMK_lk_annotationbase_createdby) One-To-Many relationship.

### <a name="BKMK_EmailServerProfile_Annotation"></a> EmailServerProfile_Annotation

See emailserverprofile Entity [EmailServerProfile_Annotation](emailserverprofile.md#BKMK_EmailServerProfile_Annotation) One-To-Many relationship.

### <a name="BKMK_Account_Annotation"></a> Account_Annotation

See account Entity [Account_Annotation](account.md#BKMK_Account_Annotation) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_Annotation"></a> RecurringAppointmentMaster_Annotation

See recurringappointmentmaster Entity [RecurringAppointmentMaster_Annotation](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_Annotation) One-To-Many relationship.

### <a name="BKMK_routingrule_Annotation"></a> routingrule_Annotation

See routingrule Entity [routingrule_Annotation](routingrule.md#BKMK_routingrule_Annotation) One-To-Many relationship.

### <a name="BKMK_business_unit_annotations"></a> business_unit_annotations

See businessunit Entity [business_unit_annotations](businessunit.md#BKMK_business_unit_annotations) One-To-Many relationship.

### <a name="BKMK_lk_annotationbase_modifiedby"></a> lk_annotationbase_modifiedby

See systemuser Entity [lk_annotationbase_modifiedby](systemuser.md#BKMK_lk_annotationbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_Letter_Annotation"></a> Letter_Annotation

See letter Entity [Letter_Annotation](letter.md#BKMK_Letter_Annotation) One-To-Many relationship.

### <a name="BKMK_Fax_Annotation"></a> Fax_Annotation

See fax Entity [Fax_Annotation](fax.md#BKMK_Fax_Annotation) One-To-Many relationship.

### <a name="BKMK_profileruleitem_Annotations"></a> profileruleitem_Annotations

See channelaccessprofileruleitem Entity [profileruleitem_Annotations](channelaccessprofileruleitem.md#BKMK_profileruleitem_Annotations) One-To-Many relationship.

### <a name="BKMK_Workflow_Annotation"></a> Workflow_Annotation

See workflow Entity [Workflow_Annotation](workflow.md#BKMK_Workflow_Annotation) One-To-Many relationship.

### <a name="BKMK_routingruleitem_Annotation"></a> routingruleitem_Annotation

See routingruleitem Entity [routingruleitem_Annotation](routingruleitem.md#BKMK_routingruleitem_Annotation) One-To-Many relationship.

### <a name="BKMK_Appointment_Annotation"></a> Appointment_Annotation

See appointment Entity [Appointment_Annotation](appointment.md#BKMK_Appointment_Annotation) One-To-Many relationship.

### <a name="BKMK_lk_annotationbase_createdonbehalfby"></a> lk_annotationbase_createdonbehalfby

See systemuser Entity [lk_annotationbase_createdonbehalfby](systemuser.md#BKMK_lk_annotationbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_Goal_Annotation"></a> Goal_Annotation

See goal Entity [Goal_Annotation](goal.md#BKMK_Goal_Annotation) One-To-Many relationship.

### <a name="BKMK_KbArticle_Annotation"></a> KbArticle_Annotation

See kbarticle Entity [KbArticle_Annotation](kbarticle.md#BKMK_KbArticle_Annotation) One-To-Many relationship.

### <a name="BKMK_SharePointDocument_Annotation"></a> SharePointDocument_Annotation

See sharepointdocument Entity [SharePointDocument_Annotation](sharepointdocument.md#BKMK_SharePointDocument_Annotation) One-To-Many relationship.

### <a name="BKMK_DuplicateRule_Annotation"></a> DuplicateRule_Annotation

See duplicaterule Entity [DuplicateRule_Annotation](duplicaterule.md#BKMK_DuplicateRule_Annotation) One-To-Many relationship.
annotation

