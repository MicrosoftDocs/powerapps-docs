---
title: "SyncError Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SyncError entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SyncError Entity Reference

Failure reason and other detailed information for a record that failed to sync.

## Entity Properties

**DisplayName**: Sync Error<br />
**DisplayCollectionName**: Sync Errors<br />
**SchemaName**: SyncError<br />
**CollectionSchemaName**: SyncErrors<br />
**LogicalName**: syncerror<br />
**LogicalCollectionName**: syncerrors<br />
**EntitySetName**: syncerrors<br />
**PrimaryIdAttribute**: syncerrorid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Action](#BKMK_Action)
- [ActionData](#BKMK_ActionData)
- [Description](#BKMK_Description)
- [ErrorCode](#BKMK_ErrorCode)
- [ErrorDetail](#BKMK_ErrorDetail)
- [ErrorMessage](#BKMK_ErrorMessage)
- [ErrorTime](#BKMK_ErrorTime)
- [ErrorType](#BKMK_ErrorType)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [RequestData](#BKMK_RequestData)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SyncErrorId](#BKMK_SyncErrorId)


### <a name="BKMK_Action"></a> Action

**Description**: Action Name for which sync error has occurred<br />
**DisplayName**: Action<br />
**LogicalName**: action<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ActionData"></a> ActionData

**Description**: Show the action data<br />
**DisplayName**: Action Data<br />
**LogicalName**: actiondata<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 10000


### <a name="BKMK_Description"></a> Description

**Description**: Enter a short description of the sync error.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_ErrorCode"></a> ErrorCode

**Description**: Displays the error code.<br />
**DisplayName**: Error Code<br />
**LogicalName**: errorcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ErrorDetail"></a> ErrorDetail

**Description**: Error description from the exception<br />
**DisplayName**: Error Detail<br />
**LogicalName**: errordetail<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ErrorMessage"></a> ErrorMessage

**Description**: Error Message of the exception<br />
**DisplayName**: Error Message<br />
**LogicalName**: errormessage<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_ErrorTime"></a> ErrorTime

**Description**: Date and time when the upsync request was executed on CRM server<br />
**DisplayName**: Error Time<br />
**LogicalName**: errortime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ErrorType"></a> ErrorType

**Description**: Select the preferred error type.<br />
**DisplayName**: Error Type<br />
**LogicalName**: errortype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Conflict
- **Value**: 1 **Label**: Record not found
- **Value**: 2 **Label**: Record already exists
- **Value**: 3 **Label**: Others



### <a name="BKMK_Name"></a> Name

**Description**: Entity name of the record for which sync error has occurred<br />
**DisplayName**: Entity<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the sync error.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the record that the sync error relates to.<br />
**DisplayName**: Record<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: account,activitymimeattachment,activityparty,annotation,appointment,attachment,businessdatalocalizedlabel,businessunit,category,channelaccessprofile,channelaccessprofilerule,channelaccessprofileruleitem,connection,connectionrole,contact,customeraddress,duplicaterule,duplicaterulecondition,email,emailserverprofile,expiredprocess,externalparty,externalpartyitem,fax,feedback,fieldpermission,fieldsecurityprofile,goal,goalrollupquery,importmap,internaladdress,kbarticle,kbarticletemplate,knowledgearticle,knowledgearticleviews,knowledgebaserecord,letter,mailbox,mailmergetemplate,metric,newprocess,offlinecommanddefinition,organization,phonecall,position,postfollow,processsession,processstage,processtrigger,publisher,queue,queueitem,recurringappointmentmaster,report,reportcategory,role,rollupfield,savedquery,savedqueryvisualization,sharepointdocumentlocation,sharepointsite,sla,slaitem,slakpiinstance,socialactivity,socialprofile,solution,subject,syncerror,systemuser,task,team,teamtemplate,template,territory,transactioncurrency,translationprocess,userquery,userqueryvisualization,workflow


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_RequestData"></a> RequestData

**Description**: Request data for the entity that had the sync error.<br />
**DisplayName**: Request Data<br />
**LogicalName**: requestdata<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the sync error is active or resolved.<br />
**DisplayName**: State<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 0 **InvariantName**: Active
- **Value**: 1 **Label**: Resolved **DefaultStatus**: 1 **InvariantName**: Resolved



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the sync error status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 0 **Label**: Active **State**: 0
- **Value**: 1 **Label**: Fixed **State**: 1



### <a name="BKMK_SyncErrorId"></a> SyncErrorId

**Description**: Unique identifier of the sync error.<br />
**DisplayName**: Sync Error Id<br />
**LogicalName**: syncerrorid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

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
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the sync error.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
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

**Description**: Date and time when the sync Error was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the sync error.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the sync error.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
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

**Description**: Date and time when the sync error was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the sync error.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
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

**Description**: Business unit that owns the sync error.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the sync error.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the sync error.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Shows the version number of the sync error.<br />
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


### <a name="BKMK_SyncError_SyncErrors"></a> SyncError_SyncErrors

Same as syncerror entity [SyncError_SyncErrors](syncerror.md#BKMK_SyncError_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: SyncError_SyncErrors<br />
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

- [Territory_SyncErrors](#BKMK_Territory_SyncErrors)
- [KnowledgeBaseRecord_SyncErrors](#BKMK_KnowledgeBaseRecord_SyncErrors)
- [SocialProfile_SyncErrors](#BKMK_SocialProfile_SyncErrors)
- [QueueItem_SyncErrors](#BKMK_QueueItem_SyncErrors)
- [PostFollow_SyncErrors](#BKMK_PostFollow_SyncErrors)
- [SharePointSite_SyncErrors](#BKMK_SharePointSite_SyncErrors)
- [Goal_SyncErrors](#BKMK_Goal_SyncErrors)
- [lk_syncerrorbase_createdby](#BKMK_lk_syncerrorbase_createdby)
- [TranslationProcess_SyncErrors](#BKMK_TranslationProcess_SyncErrors)
- [PhoneCall_SyncErrors](#BKMK_PhoneCall_SyncErrors)
- [RecurringAppointmentMaster_SyncErrors](#BKMK_RecurringAppointmentMaster_SyncErrors)
- [Publisher_SyncErrors](#BKMK_Publisher_SyncErrors)
- [DuplicateRule_SyncErrors](#BKMK_DuplicateRule_SyncErrors)
- [Subject_SyncErrors](#BKMK_Subject_SyncErrors)
- [ChannelAccessProfile_SyncErrors](#BKMK_ChannelAccessProfile_SyncErrors)
- [UserQuery_SyncErrors](#BKMK_UserQuery_SyncErrors)
- [MailMergeTemplate_SyncErrors](#BKMK_MailMergeTemplate_SyncErrors)
- [SyncError_SyncErrors](#BKMK_SyncError_SyncErrors)
- [SavedQuery_SyncErrors](#BKMK_SavedQuery_SyncErrors)
- [lk_syncerrorbase_modifiedby](#BKMK_lk_syncerrorbase_modifiedby)
- [lk_syncerrorbase_modifiedonbehalfby](#BKMK_lk_syncerrorbase_modifiedonbehalfby)
- [ChannelAccessProfileRule_SyncErrors](#BKMK_ChannelAccessProfileRule_SyncErrors)
- [TransactionCurrency_SyncErrors](#BKMK_TransactionCurrency_SyncErrors)
- [SocialActivity_SyncErrors](#BKMK_SocialActivity_SyncErrors)
- [CustomerAddress_SyncErrors](#BKMK_CustomerAddress_SyncErrors)
- [Solution_SyncErrors](#BKMK_Solution_SyncErrors)
- [team_SyncError](#BKMK_team_SyncError)
- [TeamTemplate_SyncErrors](#BKMK_TeamTemplate_SyncErrors)
- [ReportCategory_SyncErrors](#BKMK_ReportCategory_SyncErrors)
- [lk_syncerrorbase_createdonbehalfby](#BKMK_lk_syncerrorbase_createdonbehalfby)
- [KbArticle_SyncErrors](#BKMK_KbArticle_SyncErrors)
- [RollupField_SyncErrors](#BKMK_RollupField_SyncErrors)
- [KbArticleTemplate_SyncErrors](#BKMK_KbArticleTemplate_SyncErrors)
- [Account_SyncErrors](#BKMK_Account_SyncErrors)
- [OfflineCommandDefinition_SyncErrors](#BKMK_OfflineCommandDefinition_SyncErrors)
- [FieldSecurityProfile_SyncErrors](#BKMK_FieldSecurityProfile_SyncErrors)
- [UserQueryVisualization_SyncErrors](#BKMK_UserQueryVisualization_SyncErrors)
- [FieldPermission_SyncErrors](#BKMK_FieldPermission_SyncErrors)
- [DuplicateRuleCondition_SyncErrors](#BKMK_DuplicateRuleCondition_SyncErrors)
- [Team_SyncErrors](#BKMK_Team_SyncErrors)
- [SLAItem_SyncErrors](#BKMK_SLAItem_SyncErrors)
- [KnowledgeArticleViews_SyncErrors](#BKMK_KnowledgeArticleViews_SyncErrors)
- [Appointment_SyncErrors](#BKMK_Appointment_SyncErrors)
- [SystemUser_SyncError](#BKMK_SystemUser_SyncError)
- [ExternalParty_SyncErrors](#BKMK_ExternalParty_SyncErrors)
- [Contact_SyncErrors](#BKMK_Contact_SyncErrors)
- [ExpiredProcess_SyncErrors](#BKMK_ExpiredProcess_SyncErrors)
- [Workflow_SyncErrors](#BKMK_Workflow_SyncErrors)
- [NewProcess_SyncErrors](#BKMK_NewProcess_SyncErrors)
- [Feedback_SyncErrors](#BKMK_Feedback_SyncErrors)
- [ActivityParty_SyncErrors](#BKMK_ActivityParty_SyncErrors)
- [Annotation_SyncErrors](#BKMK_Annotation_SyncErrors)
- [Email_SyncErrors](#BKMK_Email_SyncErrors)
- [Organization_SyncErrors](#BKMK_Organization_SyncErrors)
- [ActivityMimeAttachment_SyncErrors](#BKMK_ActivityMimeAttachment_SyncErrors)
- [Task_SyncErrors](#BKMK_Task_SyncErrors)
- [Letter_SyncErrors](#BKMK_Letter_SyncErrors)
- [Template_SyncErrors](#BKMK_Template_SyncErrors)
- [ProcessStage_SyncErrors](#BKMK_ProcessStage_SyncErrors)
- [KnowledgeArticle_SyncErrors](#BKMK_KnowledgeArticle_SyncErrors)
- [Position_SyncErrors](#BKMK_Position_SyncErrors)
- [SharePointDocumentLocation_SyncErrors](#BKMK_SharePointDocumentLocation_SyncErrors)
- [Report_SyncErrors](#BKMK_Report_SyncErrors)
- [ExternalPartyItem_SyncErrors](#BKMK_ExternalPartyItem_SyncErrors)
- [Connection_SyncErrors](#BKMK_Connection_SyncErrors)
- [ChannelAccessProfileRuleItem_SyncErrors](#BKMK_ChannelAccessProfileRuleItem_SyncErrors)
- [ProcessSession_SyncErrors](#BKMK_ProcessSession_SyncErrors)
- [Category_SyncErrors](#BKMK_Category_SyncErrors)
- [ConnectionRole_SyncErrors](#BKMK_ConnectionRole_SyncErrors)
- [ProcessTrigger_SyncErrors](#BKMK_ProcessTrigger_SyncErrors)
- [Fax_SyncErrors](#BKMK_Fax_SyncErrors)
- [Mailbox_SyncErrors](#BKMK_Mailbox_SyncErrors)
- [BusinessUnit_SyncErrors](#BKMK_BusinessUnit_SyncErrors)
- [Queue_SyncErrors](#BKMK_Queue_SyncErrors)
- [Role_SyncErrors](#BKMK_Role_SyncErrors)
- [BusinessUnit_SyncError](#BKMK_BusinessUnit_SyncError)
- [SystemUser_SyncErrors](#BKMK_SystemUser_SyncErrors)
- [SLAKPIInstance_SyncErrors](#BKMK_SLAKPIInstance_SyncErrors)
- [SLA_SyncErrors](#BKMK_SLA_SyncErrors)
- [SavedQueryVisualization_SyncErrors](#BKMK_SavedQueryVisualization_SyncErrors)
- [GoalRollupQuery_SyncErrors](#BKMK_GoalRollupQuery_SyncErrors)
- [Metric_SyncErrors](#BKMK_Metric_SyncErrors)
- [ImportMap_SyncErrors](#BKMK_ImportMap_SyncErrors)
- [EmailServerProfile_SyncErrors](#BKMK_EmailServerProfile_SyncErrors)


### <a name="BKMK_Territory_SyncErrors"></a> Territory_SyncErrors

See territory Entity [Territory_SyncErrors](territory.md#BKMK_Territory_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_SyncErrors"></a> KnowledgeBaseRecord_SyncErrors

See knowledgebaserecord Entity [KnowledgeBaseRecord_SyncErrors](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SocialProfile_SyncErrors"></a> SocialProfile_SyncErrors

See socialprofile Entity [SocialProfile_SyncErrors](socialprofile.md#BKMK_SocialProfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_QueueItem_SyncErrors"></a> QueueItem_SyncErrors

See queueitem Entity [QueueItem_SyncErrors](queueitem.md#BKMK_QueueItem_SyncErrors) One-To-Many relationship.

### <a name="BKMK_PostFollow_SyncErrors"></a> PostFollow_SyncErrors

See postfollow Entity [PostFollow_SyncErrors](postfollow.md#BKMK_PostFollow_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SharePointSite_SyncErrors"></a> SharePointSite_SyncErrors

See sharepointsite Entity [SharePointSite_SyncErrors](sharepointsite.md#BKMK_SharePointSite_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Goal_SyncErrors"></a> Goal_SyncErrors

See goal Entity [Goal_SyncErrors](goal.md#BKMK_Goal_SyncErrors) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_createdby"></a> lk_syncerrorbase_createdby

See systemuser Entity [lk_syncerrorbase_createdby](systemuser.md#BKMK_lk_syncerrorbase_createdby) One-To-Many relationship.

### <a name="BKMK_TranslationProcess_SyncErrors"></a> TranslationProcess_SyncErrors

See translationprocess Entity [TranslationProcess_SyncErrors](translationprocess.md#BKMK_TranslationProcess_SyncErrors) One-To-Many relationship.

### <a name="BKMK_PhoneCall_SyncErrors"></a> PhoneCall_SyncErrors

See phonecall Entity [PhoneCall_SyncErrors](phonecall.md#BKMK_PhoneCall_SyncErrors) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_SyncErrors"></a> RecurringAppointmentMaster_SyncErrors

See recurringappointmentmaster Entity [RecurringAppointmentMaster_SyncErrors](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Publisher_SyncErrors"></a> Publisher_SyncErrors

See publisher Entity [Publisher_SyncErrors](publisher.md#BKMK_Publisher_SyncErrors) One-To-Many relationship.

### <a name="BKMK_DuplicateRule_SyncErrors"></a> DuplicateRule_SyncErrors

See duplicaterule Entity [DuplicateRule_SyncErrors](duplicaterule.md#BKMK_DuplicateRule_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Subject_SyncErrors"></a> Subject_SyncErrors

See subject Entity [Subject_SyncErrors](subject.md#BKMK_Subject_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ChannelAccessProfile_SyncErrors"></a> ChannelAccessProfile_SyncErrors

See channelaccessprofile Entity [ChannelAccessProfile_SyncErrors](channelaccessprofile.md#BKMK_ChannelAccessProfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_UserQuery_SyncErrors"></a> UserQuery_SyncErrors

See userquery Entity [UserQuery_SyncErrors](userquery.md#BKMK_UserQuery_SyncErrors) One-To-Many relationship.

### <a name="BKMK_MailMergeTemplate_SyncErrors"></a> MailMergeTemplate_SyncErrors

See mailmergetemplate Entity [MailMergeTemplate_SyncErrors](mailmergetemplate.md#BKMK_MailMergeTemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SyncError_SyncErrors"></a> SyncError_SyncErrors

See syncerror Entity [SyncError_SyncErrors](syncerror.md#BKMK_SyncError_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SavedQuery_SyncErrors"></a> SavedQuery_SyncErrors

See savedquery Entity [SavedQuery_SyncErrors](savedquery.md#BKMK_SavedQuery_SyncErrors) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_modifiedby"></a> lk_syncerrorbase_modifiedby

See systemuser Entity [lk_syncerrorbase_modifiedby](systemuser.md#BKMK_lk_syncerrorbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_modifiedonbehalfby"></a> lk_syncerrorbase_modifiedonbehalfby

See systemuser Entity [lk_syncerrorbase_modifiedonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_ChannelAccessProfileRule_SyncErrors"></a> ChannelAccessProfileRule_SyncErrors

See channelaccessprofilerule Entity [ChannelAccessProfileRule_SyncErrors](channelaccessprofilerule.md#BKMK_ChannelAccessProfileRule_SyncErrors) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SyncErrors"></a> TransactionCurrency_SyncErrors

See transactioncurrency Entity [TransactionCurrency_SyncErrors](transactioncurrency.md#BKMK_TransactionCurrency_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SocialActivity_SyncErrors"></a> SocialActivity_SyncErrors

See socialactivity Entity [SocialActivity_SyncErrors](socialactivity.md#BKMK_SocialActivity_SyncErrors) One-To-Many relationship.

### <a name="BKMK_CustomerAddress_SyncErrors"></a> CustomerAddress_SyncErrors

See customeraddress Entity [CustomerAddress_SyncErrors](customeraddress.md#BKMK_CustomerAddress_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Solution_SyncErrors"></a> Solution_SyncErrors

See solution Entity [Solution_SyncErrors](solution.md#BKMK_Solution_SyncErrors) One-To-Many relationship.

### <a name="BKMK_team_SyncError"></a> team_SyncError

See team Entity [team_SyncError](team.md#BKMK_team_SyncError) One-To-Many relationship.

### <a name="BKMK_TeamTemplate_SyncErrors"></a> TeamTemplate_SyncErrors

See teamtemplate Entity [TeamTemplate_SyncErrors](teamtemplate.md#BKMK_TeamTemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ReportCategory_SyncErrors"></a> ReportCategory_SyncErrors

See reportcategory Entity [ReportCategory_SyncErrors](reportcategory.md#BKMK_ReportCategory_SyncErrors) One-To-Many relationship.

### <a name="BKMK_lk_syncerrorbase_createdonbehalfby"></a> lk_syncerrorbase_createdonbehalfby

See systemuser Entity [lk_syncerrorbase_createdonbehalfby](systemuser.md#BKMK_lk_syncerrorbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_KbArticle_SyncErrors"></a> KbArticle_SyncErrors

See kbarticle Entity [KbArticle_SyncErrors](kbarticle.md#BKMK_KbArticle_SyncErrors) One-To-Many relationship.

### <a name="BKMK_RollupField_SyncErrors"></a> RollupField_SyncErrors

See rollupfield Entity [RollupField_SyncErrors](rollupfield.md#BKMK_RollupField_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_SyncErrors"></a> KbArticleTemplate_SyncErrors

See kbarticletemplate Entity [KbArticleTemplate_SyncErrors](kbarticletemplate.md#BKMK_KbArticleTemplate_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Account_SyncErrors"></a> Account_SyncErrors

See account Entity [Account_SyncErrors](account.md#BKMK_Account_SyncErrors) One-To-Many relationship.

### <a name="BKMK_OfflineCommandDefinition_SyncErrors"></a> OfflineCommandDefinition_SyncErrors

See offlinecommanddefinition Entity [OfflineCommandDefinition_SyncErrors](offlinecommanddefinition.md#BKMK_OfflineCommandDefinition_SyncErrors) One-To-Many relationship.

### <a name="BKMK_FieldSecurityProfile_SyncErrors"></a> FieldSecurityProfile_SyncErrors

See fieldsecurityprofile Entity [FieldSecurityProfile_SyncErrors](fieldsecurityprofile.md#BKMK_FieldSecurityProfile_SyncErrors) One-To-Many relationship.

### <a name="BKMK_UserQueryVisualization_SyncErrors"></a> UserQueryVisualization_SyncErrors

See userqueryvisualization Entity [UserQueryVisualization_SyncErrors](userqueryvisualization.md#BKMK_UserQueryVisualization_SyncErrors) One-To-Many relationship.

### <a name="BKMK_FieldPermission_SyncErrors"></a> FieldPermission_SyncErrors

See fieldpermission Entity [FieldPermission_SyncErrors](fieldpermission.md#BKMK_FieldPermission_SyncErrors) One-To-Many relationship.

### <a name="BKMK_DuplicateRuleCondition_SyncErrors"></a> DuplicateRuleCondition_SyncErrors

See duplicaterulecondition Entity [DuplicateRuleCondition_SyncErrors](duplicaterulecondition.md#BKMK_DuplicateRuleCondition_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

See team Entity [Team_SyncErrors](team.md#BKMK_Team_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SLAItem_SyncErrors"></a> SLAItem_SyncErrors

See slaitem Entity [SLAItem_SyncErrors](slaitem.md#BKMK_SLAItem_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticleViews_SyncErrors"></a> KnowledgeArticleViews_SyncErrors

See knowledgearticleviews Entity [KnowledgeArticleViews_SyncErrors](knowledgearticleviews.md#BKMK_KnowledgeArticleViews_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Appointment_SyncErrors"></a> Appointment_SyncErrors

See appointment Entity [Appointment_SyncErrors](appointment.md#BKMK_Appointment_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SystemUser_SyncError"></a> SystemUser_SyncError

See systemuser Entity [SystemUser_SyncError](systemuser.md#BKMK_SystemUser_SyncError) One-To-Many relationship.

### <a name="BKMK_ExternalParty_SyncErrors"></a> ExternalParty_SyncErrors

See externalparty Entity [ExternalParty_SyncErrors](externalparty.md#BKMK_ExternalParty_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Contact_SyncErrors"></a> Contact_SyncErrors

See contact Entity [Contact_SyncErrors](contact.md#BKMK_Contact_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ExpiredProcess_SyncErrors"></a> ExpiredProcess_SyncErrors

See expiredprocess Entity [ExpiredProcess_SyncErrors](expiredprocess.md#BKMK_ExpiredProcess_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

See workflow Entity [Workflow_SyncErrors](workflow.md#BKMK_Workflow_SyncErrors) One-To-Many relationship.

### <a name="BKMK_NewProcess_SyncErrors"></a> NewProcess_SyncErrors

See newprocess Entity [NewProcess_SyncErrors](newprocess.md#BKMK_NewProcess_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Feedback_SyncErrors"></a> Feedback_SyncErrors

See feedback Entity [Feedback_SyncErrors](feedback.md#BKMK_Feedback_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ActivityParty_SyncErrors"></a> ActivityParty_SyncErrors

See activityparty Entity [ActivityParty_SyncErrors](activityparty.md#BKMK_ActivityParty_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Annotation_SyncErrors"></a> Annotation_SyncErrors

See annotation Entity [Annotation_SyncErrors](annotation.md#BKMK_Annotation_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Email_SyncErrors"></a> Email_SyncErrors

See email Entity [Email_SyncErrors](email.md#BKMK_Email_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Organization_SyncErrors"></a> Organization_SyncErrors

See organization Entity [Organization_SyncErrors](organization.md#BKMK_Organization_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ActivityMimeAttachment_SyncErrors"></a> ActivityMimeAttachment_SyncErrors

See activitymimeattachment Entity [ActivityMimeAttachment_SyncErrors](activitymimeattachment.md#BKMK_ActivityMimeAttachment_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Task_SyncErrors"></a> Task_SyncErrors

See task Entity [Task_SyncErrors](task.md#BKMK_Task_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Letter_SyncErrors"></a> Letter_SyncErrors

See letter Entity [Letter_SyncErrors](letter.md#BKMK_Letter_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Template_SyncErrors"></a> Template_SyncErrors

See template Entity [Template_SyncErrors](template.md#BKMK_Template_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

See processstage Entity [ProcessStage_SyncErrors](processstage.md#BKMK_ProcessStage_SyncErrors) One-To-Many relationship.

### <a name="BKMK_KnowledgeArticle_SyncErrors"></a> KnowledgeArticle_SyncErrors

See knowledgearticle Entity [KnowledgeArticle_SyncErrors](knowledgearticle.md#BKMK_KnowledgeArticle_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Position_SyncErrors"></a> Position_SyncErrors

See position Entity [Position_SyncErrors](position.md#BKMK_Position_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_SyncErrors"></a> SharePointDocumentLocation_SyncErrors

See sharepointdocumentlocation Entity [SharePointDocumentLocation_SyncErrors](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Report_SyncErrors"></a> Report_SyncErrors

See report Entity [Report_SyncErrors](report.md#BKMK_Report_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ExternalPartyItem_SyncErrors"></a> ExternalPartyItem_SyncErrors

See externalpartyitem Entity [ExternalPartyItem_SyncErrors](externalpartyitem.md#BKMK_ExternalPartyItem_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

See connection Entity [Connection_SyncErrors](connection.md#BKMK_Connection_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ChannelAccessProfileRuleItem_SyncErrors"></a> ChannelAccessProfileRuleItem_SyncErrors

See channelaccessprofileruleitem Entity [ChannelAccessProfileRuleItem_SyncErrors](channelaccessprofileruleitem.md#BKMK_ChannelAccessProfileRuleItem_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

See processsession Entity [ProcessSession_SyncErrors](processsession.md#BKMK_ProcessSession_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Category_SyncErrors"></a> Category_SyncErrors

See category Entity [Category_SyncErrors](category.md#BKMK_Category_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ConnectionRole_SyncErrors"></a> ConnectionRole_SyncErrors

See connectionrole Entity [ConnectionRole_SyncErrors](connectionrole.md#BKMK_ConnectionRole_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ProcessTrigger_SyncErrors"></a> ProcessTrigger_SyncErrors

See processtrigger Entity [ProcessTrigger_SyncErrors](processtrigger.md#BKMK_ProcessTrigger_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Fax_SyncErrors"></a> Fax_SyncErrors

See fax Entity [Fax_SyncErrors](fax.md#BKMK_Fax_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Mailbox_SyncErrors"></a> Mailbox_SyncErrors

See mailbox Entity [Mailbox_SyncErrors](mailbox.md#BKMK_Mailbox_SyncErrors) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

See businessunit Entity [BusinessUnit_SyncErrors](businessunit.md#BKMK_BusinessUnit_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Queue_SyncErrors"></a> Queue_SyncErrors

See queue Entity [Queue_SyncErrors](queue.md#BKMK_Queue_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Role_SyncErrors"></a> Role_SyncErrors

See role Entity [Role_SyncErrors](role.md#BKMK_Role_SyncErrors) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

See businessunit Entity [BusinessUnit_SyncError](businessunit.md#BKMK_BusinessUnit_SyncError) One-To-Many relationship.

### <a name="BKMK_SystemUser_SyncErrors"></a> SystemUser_SyncErrors

See systemuser Entity [SystemUser_SyncErrors](systemuser.md#BKMK_SystemUser_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

See slakpiinstance Entity [SLAKPIInstance_SyncErrors](slakpiinstance.md#BKMK_SLAKPIInstance_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

See sla Entity [SLA_SyncErrors](sla.md#BKMK_SLA_SyncErrors) One-To-Many relationship.

### <a name="BKMK_SavedQueryVisualization_SyncErrors"></a> SavedQueryVisualization_SyncErrors

See savedqueryvisualization Entity [SavedQueryVisualization_SyncErrors](savedqueryvisualization.md#BKMK_SavedQueryVisualization_SyncErrors) One-To-Many relationship.

### <a name="BKMK_GoalRollupQuery_SyncErrors"></a> GoalRollupQuery_SyncErrors

See goalrollupquery Entity [GoalRollupQuery_SyncErrors](goalrollupquery.md#BKMK_GoalRollupQuery_SyncErrors) One-To-Many relationship.

### <a name="BKMK_Metric_SyncErrors"></a> Metric_SyncErrors

See metric Entity [Metric_SyncErrors](metric.md#BKMK_Metric_SyncErrors) One-To-Many relationship.

### <a name="BKMK_ImportMap_SyncErrors"></a> ImportMap_SyncErrors

See importmap Entity [ImportMap_SyncErrors](importmap.md#BKMK_ImportMap_SyncErrors) One-To-Many relationship.

### <a name="BKMK_EmailServerProfile_SyncErrors"></a> EmailServerProfile_SyncErrors

See emailserverprofile Entity [EmailServerProfile_SyncErrors](emailserverprofile.md#BKMK_EmailServerProfile_SyncErrors) One-To-Many relationship.
syncerror

