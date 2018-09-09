---
title: "ProcessSession Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ProcessSession entity."
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
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ProcessSession Entity Reference

Information that is generated when a dialog is run. Every time that you run a dialog, a dialog session is created.

## Entity Properties

**DisplayName**: Process Session<br />
**DisplayCollectionName**: Process Sessions<br />
**SchemaName**: ProcessSession<br />
**CollectionSchemaName**: ProcessSession<br />
**LogicalName**: processsession<br />
**LogicalCollectionName**: processsessions<br />
**EntitySetName**: processsessions<br />
**PrimaryIdAttribute**: processsessionid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActivityName](#BKMK_ActivityName)
- [CanceledOn](#BKMK_CanceledOn)
- [Comments](#BKMK_Comments)
- [CompletedOn](#BKMK_CompletedOn)
- [ErrorCode](#BKMK_ErrorCode)
- [ExecutedBy](#BKMK_ExecutedBy)
- [InputArguments](#BKMK_InputArguments)
- [Name](#BKMK_Name)
- [NextLinkedSessionId](#BKMK_NextLinkedSessionId)
- [OriginatingSessionId](#BKMK_OriginatingSessionId)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PreviousLinkedSessionId](#BKMK_PreviousLinkedSessionId)
- [ProcessId](#BKMK_ProcessId)
- [ProcessSessionId](#BKMK_ProcessSessionId)
- [ProcessStageName](#BKMK_ProcessStageName)
- [ProcessState](#BKMK_ProcessState)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RegardingObjectIdYomiName](#BKMK_RegardingObjectIdYomiName)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [StartedOn](#BKMK_StartedOn)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [StepName](#BKMK_StepName)


### <a name="BKMK_ActivityName"></a> ActivityName

**Description**: Name of the activity that is being executed.<br />
**DisplayName**: Activity Name<br />
**LogicalName**: activityname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_CanceledOn"></a> CanceledOn

**Description**: Date and time when the dialog session was canceled.<br />
**DisplayName**: Canceled On<br />
**LogicalName**: canceledon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_Comments"></a> Comments

**Description**: User comments.<br />
**DisplayName**: Comments<br />
**LogicalName**: comments<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_CompletedOn"></a> CompletedOn

**Description**: Date and time when the dialog session was completed.<br />
**DisplayName**: Completed On<br />
**LogicalName**: completedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ErrorCode"></a> ErrorCode

**Description**: Error code related to the dialog session.<br />
**DisplayName**: Error Code<br />
**LogicalName**: errorcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ExecutedBy"></a> ExecutedBy

**Description**: Unique identifier of the user who ran the dialog process.<br />
**DisplayName**: Executed By<br />
**LogicalName**: executedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_InputArguments"></a> InputArguments

**Description**: Input arguments for the child dialog process.<br />
**DisplayName**: Input Arguments<br />
**LogicalName**: inputarguments<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Name"></a> Name

**Description**: Name of the dialog session.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_NextLinkedSessionId"></a> NextLinkedSessionId

**Description**: Unique identifier of the succeeding linked dialog session.<br />
**DisplayName**: Next Linked Session<br />
**LogicalName**: nextlinkedsessionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: processsession


### <a name="BKMK_OriginatingSessionId"></a> OriginatingSessionId

**Description**: Unique identifier of the originating dialog session.<br />
**DisplayName**: Originating Session<br />
**LogicalName**: originatingsessionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: processsession


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the dialog session.<br />
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


### <a name="BKMK_PreviousLinkedSessionId"></a> PreviousLinkedSessionId

**Description**: Unique identifier of the preceding linked dialog session.<br />
**DisplayName**: Previous Linked Session<br />
**LogicalName**: previouslinkedsessionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: processsession


### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Select the process activation record that is related to the dialog session.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: workflow


### <a name="BKMK_ProcessSessionId"></a> ProcessSessionId

**Description**: Unique identifier of the dialog session.<br />
**DisplayName**: Dialog Session<br />
**LogicalName**: processsessionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ProcessStageName"></a> ProcessStageName

**Description**: Name of the dialog stage.<br />
**DisplayName**: Dialog Stage<br />
**LogicalName**: processstagename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ProcessState"></a> ProcessState

**Description**: State of the dialog process.<br />
**DisplayName**: Process State<br />
**LogicalName**: processstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Unique identifier of the object with which the dialog session is associated.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: account,annotation,appointment,businessunit,businessunitnewsarticle,channelaccessprofile,channelaccessprofilerule,connection,connectionrole,contact,convertrule,customeraddress,customerrelationship,email,expiredprocess,externalparty,externalpartyitem,fax,goal,goalrollupquery,kbarticle,kbarticlecomment,kbarticletemplate,knowledgearticle,knowledgebaserecord,letter,mailbox,mailmergetemplate,metric,newprocess,phonecall,position,queue,queueitem,recurringappointmentmaster,relationshiprole,report,rollupfield,routingrule,routingruleitem,sharepointdocumentlocation,sharepointsite,sla,socialactivity,socialprofile,subject,systemuser,task,team,template,territory,theme,transactioncurrency,translationprocess,usermapping


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
**MaxLength**: 400


### <a name="BKMK_RegardingObjectIdYomiName"></a> RegardingObjectIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_StartedOn"></a> StartedOn

**Description**: Date and time when the dialog session was started.<br />
**DisplayName**: Started On<br />
**LogicalName**: startedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the dialog session.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Incomplete **DefaultStatus**: 1 **InvariantName**: Incomplete
- **Value**: 1 **Label**: Complete **DefaultStatus**: 2 **InvariantName**: Complete



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the dialog session.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Not Started **State**: 0
- **Value**: 2 **Label**: In Progress **State**: 0
- **Value**: 3 **Label**: Paused **State**: 0
- **Value**: 4 **Label**: Completed **State**: 1
- **Value**: 5 **Label**: Canceled **State**: 1
- **Value**: 6 **Label**: Failed **State**: 1



### <a name="BKMK_StepName"></a> StepName

**Description**: Name of the dialog step.<br />
**DisplayName**: Step Name<br />
**LogicalName**: stepname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CanceledBy](#BKMK_CanceledBy)
- [CanceledByName](#BKMK_CanceledByName)
- [CanceledByYomiName](#BKMK_CanceledByYomiName)
- [CompletedBy](#BKMK_CompletedBy)
- [CompletedByName](#BKMK_CompletedByName)
- [CompletedByYomiName](#BKMK_CompletedByYomiName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExecutedByName](#BKMK_ExecutedByName)
- [ExecutedByYomiName](#BKMK_ExecutedByYomiName)
- [ExecutedOn](#BKMK_ExecutedOn)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [NextLinkedSessionIdName](#BKMK_NextLinkedSessionIdName)
- [OriginatingSessionIdName](#BKMK_OriginatingSessionIdName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PreviousLinkedSessionIdName](#BKMK_PreviousLinkedSessionIdName)
- [ProcessIdName](#BKMK_ProcessIdName)
- [ProtectionKey](#BKMK_ProtectionKey)
- [StartedBy](#BKMK_StartedBy)
- [StartedByName](#BKMK_StartedByName)
- [StartedByYomiName](#BKMK_StartedByYomiName)


### <a name="BKMK_CanceledBy"></a> CanceledBy

**Description**: Unique identifier of the user who canceled the dialog session.<br />
**DisplayName**: Canceled By<br />
**LogicalName**: canceledby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CanceledByName"></a> CanceledByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: canceledbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CanceledByYomiName"></a> CanceledByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: canceledbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CompletedBy"></a> CompletedBy

**Description**: Unique identifier of the user who completed the dialog session.<br />
**DisplayName**: Completed By<br />
**LogicalName**: completedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CompletedByName"></a> CompletedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: completedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CompletedByYomiName"></a> CompletedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: completedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who started the dialog session.<br />
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

**Description**: Date and time when the dialog session was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the dialog session.<br />
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


### <a name="BKMK_ExecutedByName"></a> ExecutedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: executedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExecutedByYomiName"></a> ExecutedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: executedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExecutedOn"></a> ExecutedOn

**Description**: Date and time when the dialog process was run.<br />
**DisplayName**: Executed On<br />
**LogicalName**: executedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the dialog session.<br />
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

**Description**: Date and time when the dialog session was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the dialog session.<br />
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


### <a name="BKMK_NextLinkedSessionIdName"></a> NextLinkedSessionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: nextlinkedsessionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OriginatingSessionIdName"></a> OriginatingSessionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: originatingsessionidname<br />
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

**Description**: Unique identifier of the business unit that owns the dialog session.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the dialog session.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the dialog session.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_PreviousLinkedSessionIdName"></a> PreviousLinkedSessionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: previouslinkedsessionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ProcessIdName"></a> ProcessIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: processidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_ProtectionKey"></a> ProtectionKey

**Description**: For internal use only.<br />
**DisplayName**: Protection Key<br />
**LogicalName**: protectionkey<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_StartedBy"></a> StartedBy

**Description**: Unique identifier of the user who started the dialog session.<br />
**DisplayName**: Started By<br />
**LogicalName**: startedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_StartedByName"></a> StartedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: startedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_StartedByYomiName"></a> StartedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: startedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [lk_workflowlog_processsession](#BKMK_lk_workflowlog_processsession)
- [lk_workflowlog_processsession_childworkflow](#BKMK_lk_workflowlog_processsession_childworkflow)
- [lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid)
- [lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid)
- [lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid)
- [processsession_connections2](#BKMK_processsession_connections2)
- [ProcessSession_SyncErrors](#BKMK_ProcessSession_SyncErrors)
- [processsession_connections1](#BKMK_processsession_connections1)
- [processsession_PostFollows](#BKMK_processsession_PostFollows)
- [userentityinstancedata_processsession](#BKMK_userentityinstancedata_processsession)


### <a name="BKMK_lk_workflowlog_processsession"></a> lk_workflowlog_processsession

Same as workflowlog entity [lk_workflowlog_processsession](workflowlog.md#BKMK_lk_workflowlog_processsession) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: asyncoperationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_processsession<br />
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


### <a name="BKMK_lk_workflowlog_processsession_childworkflow"></a> lk_workflowlog_processsession_childworkflow

Same as workflowlog entity [lk_workflowlog_processsession_childworkflow](workflowlog.md#BKMK_lk_workflowlog_processsession_childworkflow) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: childworkflowinstanceid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_processsession_childworkflow<br />
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


### <a name="BKMK_lk_processsession_previouslinkedsessionid"></a> lk_processsession_previouslinkedsessionid

Same as processsession entity [lk_processsession_previouslinkedsessionid](processsession.md#BKMK_lk_processsession_previouslinkedsessionid) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: previouslinkedsessionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_previouslinkedsessionid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_processsession_nextlinkedsessionid"></a> lk_processsession_nextlinkedsessionid

Same as processsession entity [lk_processsession_nextlinkedsessionid](processsession.md#BKMK_lk_processsession_nextlinkedsessionid) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: nextlinkedsessionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_nextlinkedsessionid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_processsession_originatingsessionid"></a> lk_processsession_originatingsessionid

Same as processsession entity [lk_processsession_originatingsessionid](processsession.md#BKMK_lk_processsession_originatingsessionid) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: originatingsessionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_originatingsessionid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processsession_connections2"></a> processsession_connections2

Same as connection entity [processsession_connections2](connection.md#BKMK_processsession_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: processsession_connections2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ProcessSession_SyncErrors"></a> ProcessSession_SyncErrors

Same as syncerror entity [ProcessSession_SyncErrors](syncerror.md#BKMK_ProcessSession_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: ProcessSession_SyncErrors<br />
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


### <a name="BKMK_processsession_connections1"></a> processsession_connections1

Same as connection entity [processsession_connections1](connection.md#BKMK_processsession_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: processsession_connections1<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_processsession_PostFollows"></a> processsession_PostFollows

Same as postfollow entity [processsession_PostFollows](postfollow.md#BKMK_processsession_PostFollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: processsession_PostFollows<br />
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


### <a name="BKMK_userentityinstancedata_processsession"></a> userentityinstancedata_processsession

Same as userentityinstancedata entity [userentityinstancedata_processsession](userentityinstancedata.md#BKMK_userentityinstancedata_processsession) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_processsession<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [Territory_ProcessSessions](#BKMK_Territory_ProcessSessions)
- [theme_ProcessSession](#BKMK_theme_ProcessSession)
- [usermapping_ProcessSession](#BKMK_usermapping_ProcessSession)
- [knowledgearticle_ProcessSession](#BKMK_knowledgearticle_ProcessSession)
- [position_ProcessSession](#BKMK_position_ProcessSession)
- [channelaccessprofile_ProcessSession](#BKMK_channelaccessprofile_ProcessSession)
- [externalparty_ProcessSession](#BKMK_externalparty_ProcessSession)
- [profilerule_ProcessSession](#BKMK_profilerule_ProcessSession)
- [KnowledgeBaseRecord_ProcessSession](#BKMK_KnowledgeBaseRecord_ProcessSession)
- [SharePointSite_ProcessSessions](#BKMK_SharePointSite_ProcessSessions)
- [MailMergeTemplate_ProcessSessions](#BKMK_MailMergeTemplate_ProcessSessions)
- [Annotation_ProcessSessions](#BKMK_Annotation_ProcessSessions)
- [routingrule_ProcessSessions](#BKMK_routingrule_ProcessSessions)
- [BusinessUnitNewsArticle_ProcessSessions](#BKMK_BusinessUnitNewsArticle_ProcessSessions)
- [Appointment_ProcessSessions](#BKMK_Appointment_ProcessSessions)
- [QueueItem_ProcessSessions](#BKMK_QueueItem_ProcessSessions)
- [lk_processsession_previouslinkedsessionid](#BKMK_lk_processsession_previouslinkedsessionid)
- [lk_processsession_nextlinkedsessionid](#BKMK_lk_processsession_nextlinkedsessionid)
- [lk_processsession_originatingsessionid](#BKMK_lk_processsession_originatingsessionid)
- [Team_ProcessSessions](#BKMK_Team_ProcessSessions)
- [Goal_ProcessSessions](#BKMK_Goal_ProcessSessions)
- [mailbox_processsessions](#BKMK_mailbox_processsessions)
- [TranslationProcess_ProcessSessions](#BKMK_TranslationProcess_ProcessSessions)
- [SystemUser_ProcessSessions](#BKMK_SystemUser_ProcessSessions)
- [BusinessUnit_ProcessSessions](#BKMK_BusinessUnit_ProcessSessions)
- [KbArticleComment_ProcessSessions](#BKMK_KbArticleComment_ProcessSessions)
- [lk_processsession_canceledby](#BKMK_lk_processsession_canceledby)
- [goalrollupquery_ProcessSessions](#BKMK_goalrollupquery_ProcessSessions)
- [rollupfield_ProcessSessions](#BKMK_rollupfield_ProcessSessions)
- [ConvertRule_ProcessSessions](#BKMK_ConvertRule_ProcessSessions)
- [SharePointDocumentLocation_ProcessSessions](#BKMK_SharePointDocumentLocation_ProcessSessions)
- [lk_processsession_startedby](#BKMK_lk_processsession_startedby)
- [Account_ProcessSessions](#BKMK_Account_ProcessSessions)
- [PhoneCall_ProcessSessions](#BKMK_PhoneCall_ProcessSessions)
- [externalpartyitem_ProcessSession](#BKMK_externalpartyitem_ProcessSession)
- [slabase_ProcessSessions](#BKMK_slabase_ProcessSessions)
- [lk_processsession_createdby](#BKMK_lk_processsession_createdby)
- [lk_processsessionbase_modifiedonbehalfby](#BKMK_lk_processsessionbase_modifiedonbehalfby)
- [Template_ProcessSessions](#BKMK_Template_ProcessSessions)
- [NewProcess_ProcessSessions](#BKMK_NewProcess_ProcessSessions)
- [Report_ProcessSessions](#BKMK_Report_ProcessSessions)
- [Owning_businessunit_processsessions](#BKMK_Owning_businessunit_processsessions)
- [CustomerAddress_ProcessSessions](#BKMK_CustomerAddress_ProcessSessions)
- [Connection_ProcessSessions](#BKMK_Connection_ProcessSessions)
- [lk_processsession_executedby](#BKMK_lk_processsession_executedby)
- [team_processsession](#BKMK_team_processsession)
- [metric_ProcessSessions](#BKMK_metric_ProcessSessions)
- [ExpiredProcess_ProcessSessions](#BKMK_ExpiredProcess_ProcessSessions)
- [KbArticle_ProcessSessions](#BKMK_KbArticle_ProcessSessions)
- [SocialActivity_ProcessSessions](#BKMK_SocialActivity_ProcessSessions)
- [Task_ProcessSessions](#BKMK_Task_ProcessSessions)
- [lk_processsession_processid](#BKMK_lk_processsession_processid)
- [lk_processsession_modifiedby](#BKMK_lk_processsession_modifiedby)
- [ConnectionRole_ProcessSessions](#BKMK_ConnectionRole_ProcessSessions)
- [TransactionCurrency_ProcessSessions](#BKMK_TransactionCurrency_ProcessSessions)
- [Fax_ProcessSessions](#BKMK_Fax_ProcessSessions)
- [KbArticleTemplate_ProcessSessions](#BKMK_KbArticleTemplate_ProcessSessions)
- [Letter_ProcessSessions](#BKMK_Letter_ProcessSessions)
- [RelationshipRole_ProcessSessions](#BKMK_RelationshipRole_ProcessSessions)
- [CustomerRelationship_ProcessSessions](#BKMK_CustomerRelationship_ProcessSessions)
- [RecurringAppointmentMaster_ProcessSessions](#BKMK_RecurringAppointmentMaster_ProcessSessions)
- [Email_ProcessSessions](#BKMK_Email_ProcessSessions)
- [lk_processsession_completedby](#BKMK_lk_processsession_completedby)
- [Contact_ProcessSessions](#BKMK_Contact_ProcessSessions)
- [Queue_ProcessSessions](#BKMK_Queue_ProcessSessions)
- [lk_processsessionbase_createdonbehalfby](#BKMK_lk_processsessionbase_createdonbehalfby)
- [routingruleitem_ProcessSessions](#BKMK_routingruleitem_ProcessSessions)
- [Subject_ProcessSessions](#BKMK_Subject_ProcessSessions)
- [SocialProfile_ProcessSessions](#BKMK_SocialProfile_ProcessSessions)


### <a name="BKMK_Territory_ProcessSessions"></a> Territory_ProcessSessions

See territory Entity [Territory_ProcessSessions](territory.md#BKMK_Territory_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_theme_ProcessSession"></a> theme_ProcessSession

See theme Entity [theme_ProcessSession](theme.md#BKMK_theme_ProcessSession) One-To-Many relationship.

### <a name="BKMK_usermapping_ProcessSession"></a> usermapping_ProcessSession

See usermapping Entity [usermapping_ProcessSession](usermapping.md#BKMK_usermapping_ProcessSession) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_ProcessSession"></a> knowledgearticle_ProcessSession

See knowledgearticle Entity [knowledgearticle_ProcessSession](knowledgearticle.md#BKMK_knowledgearticle_ProcessSession) One-To-Many relationship.

### <a name="BKMK_position_ProcessSession"></a> position_ProcessSession

See position Entity [position_ProcessSession](position.md#BKMK_position_ProcessSession) One-To-Many relationship.

### <a name="BKMK_channelaccessprofile_ProcessSession"></a> channelaccessprofile_ProcessSession

See channelaccessprofile Entity [channelaccessprofile_ProcessSession](channelaccessprofile.md#BKMK_channelaccessprofile_ProcessSession) One-To-Many relationship.

### <a name="BKMK_externalparty_ProcessSession"></a> externalparty_ProcessSession

See externalparty Entity [externalparty_ProcessSession](externalparty.md#BKMK_externalparty_ProcessSession) One-To-Many relationship.

### <a name="BKMK_profilerule_ProcessSession"></a> profilerule_ProcessSession

See channelaccessprofilerule Entity [profilerule_ProcessSession](channelaccessprofilerule.md#BKMK_profilerule_ProcessSession) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_ProcessSession"></a> KnowledgeBaseRecord_ProcessSession

See knowledgebaserecord Entity [KnowledgeBaseRecord_ProcessSession](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_ProcessSession) One-To-Many relationship.

### <a name="BKMK_SharePointSite_ProcessSessions"></a> SharePointSite_ProcessSessions

See sharepointsite Entity [SharePointSite_ProcessSessions](sharepointsite.md#BKMK_SharePointSite_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_MailMergeTemplate_ProcessSessions"></a> MailMergeTemplate_ProcessSessions

See mailmergetemplate Entity [MailMergeTemplate_ProcessSessions](mailmergetemplate.md#BKMK_MailMergeTemplate_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Annotation_ProcessSessions"></a> Annotation_ProcessSessions

See annotation Entity [Annotation_ProcessSessions](annotation.md#BKMK_Annotation_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_routingrule_ProcessSessions"></a> routingrule_ProcessSessions

See routingrule Entity [routingrule_ProcessSessions](routingrule.md#BKMK_routingrule_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_BusinessUnitNewsArticle_ProcessSessions"></a> BusinessUnitNewsArticle_ProcessSessions

See businessunitnewsarticle Entity [BusinessUnitNewsArticle_ProcessSessions](businessunitnewsarticle.md#BKMK_BusinessUnitNewsArticle_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Appointment_ProcessSessions"></a> Appointment_ProcessSessions

See appointment Entity [Appointment_ProcessSessions](appointment.md#BKMK_Appointment_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_QueueItem_ProcessSessions"></a> QueueItem_ProcessSessions

See queueitem Entity [QueueItem_ProcessSessions](queueitem.md#BKMK_QueueItem_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_previouslinkedsessionid"></a> lk_processsession_previouslinkedsessionid

See processsession Entity [lk_processsession_previouslinkedsessionid](processsession.md#BKMK_lk_processsession_previouslinkedsessionid) One-To-Many relationship.

### <a name="BKMK_lk_processsession_nextlinkedsessionid"></a> lk_processsession_nextlinkedsessionid

See processsession Entity [lk_processsession_nextlinkedsessionid](processsession.md#BKMK_lk_processsession_nextlinkedsessionid) One-To-Many relationship.

### <a name="BKMK_lk_processsession_originatingsessionid"></a> lk_processsession_originatingsessionid

See processsession Entity [lk_processsession_originatingsessionid](processsession.md#BKMK_lk_processsession_originatingsessionid) One-To-Many relationship.

### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

See team Entity [Team_ProcessSessions](team.md#BKMK_Team_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Goal_ProcessSessions"></a> Goal_ProcessSessions

See goal Entity [Goal_ProcessSessions](goal.md#BKMK_Goal_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_mailbox_processsessions"></a> mailbox_processsessions

See mailbox Entity [mailbox_processsessions](mailbox.md#BKMK_mailbox_processsessions) One-To-Many relationship.

### <a name="BKMK_TranslationProcess_ProcessSessions"></a> TranslationProcess_ProcessSessions

See translationprocess Entity [TranslationProcess_ProcessSessions](translationprocess.md#BKMK_TranslationProcess_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SystemUser_ProcessSessions"></a> SystemUser_ProcessSessions

See systemuser Entity [SystemUser_ProcessSessions](systemuser.md#BKMK_SystemUser_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

See businessunit Entity [BusinessUnit_ProcessSessions](businessunit.md#BKMK_BusinessUnit_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_KbArticleComment_ProcessSessions"></a> KbArticleComment_ProcessSessions

See kbarticlecomment Entity [KbArticleComment_ProcessSessions](kbarticlecomment.md#BKMK_KbArticleComment_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_canceledby"></a> lk_processsession_canceledby

See systemuser Entity [lk_processsession_canceledby](systemuser.md#BKMK_lk_processsession_canceledby) One-To-Many relationship.

### <a name="BKMK_goalrollupquery_ProcessSessions"></a> goalrollupquery_ProcessSessions

See goalrollupquery Entity [goalrollupquery_ProcessSessions](goalrollupquery.md#BKMK_goalrollupquery_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_rollupfield_ProcessSessions"></a> rollupfield_ProcessSessions

See rollupfield Entity [rollupfield_ProcessSessions](rollupfield.md#BKMK_rollupfield_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_ConvertRule_ProcessSessions"></a> ConvertRule_ProcessSessions

See convertrule Entity [ConvertRule_ProcessSessions](convertrule.md#BKMK_ConvertRule_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SharePointDocumentLocation_ProcessSessions"></a> SharePointDocumentLocation_ProcessSessions

See sharepointdocumentlocation Entity [SharePointDocumentLocation_ProcessSessions](sharepointdocumentlocation.md#BKMK_SharePointDocumentLocation_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_startedby"></a> lk_processsession_startedby

See systemuser Entity [lk_processsession_startedby](systemuser.md#BKMK_lk_processsession_startedby) One-To-Many relationship.

### <a name="BKMK_Account_ProcessSessions"></a> Account_ProcessSessions

See account Entity [Account_ProcessSessions](account.md#BKMK_Account_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_PhoneCall_ProcessSessions"></a> PhoneCall_ProcessSessions

See phonecall Entity [PhoneCall_ProcessSessions](phonecall.md#BKMK_PhoneCall_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_externalpartyitem_ProcessSession"></a> externalpartyitem_ProcessSession

See externalpartyitem Entity [externalpartyitem_ProcessSession](externalpartyitem.md#BKMK_externalpartyitem_ProcessSession) One-To-Many relationship.

### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

See sla Entity [slabase_ProcessSessions](sla.md#BKMK_slabase_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_createdby"></a> lk_processsession_createdby

See systemuser Entity [lk_processsession_createdby](systemuser.md#BKMK_lk_processsession_createdby) One-To-Many relationship.

### <a name="BKMK_lk_processsessionbase_modifiedonbehalfby"></a> lk_processsessionbase_modifiedonbehalfby

See systemuser Entity [lk_processsessionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_processsessionbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_Template_ProcessSessions"></a> Template_ProcessSessions

See template Entity [Template_ProcessSessions](template.md#BKMK_Template_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_NewProcess_ProcessSessions"></a> NewProcess_ProcessSessions

See newprocess Entity [NewProcess_ProcessSessions](newprocess.md#BKMK_NewProcess_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Report_ProcessSessions"></a> Report_ProcessSessions

See report Entity [Report_ProcessSessions](report.md#BKMK_Report_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

See businessunit Entity [Owning_businessunit_processsessions](businessunit.md#BKMK_Owning_businessunit_processsessions) One-To-Many relationship.

### <a name="BKMK_CustomerAddress_ProcessSessions"></a> CustomerAddress_ProcessSessions

See customeraddress Entity [CustomerAddress_ProcessSessions](customeraddress.md#BKMK_CustomerAddress_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

See connection Entity [Connection_ProcessSessions](connection.md#BKMK_Connection_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_executedby"></a> lk_processsession_executedby

See systemuser Entity [lk_processsession_executedby](systemuser.md#BKMK_lk_processsession_executedby) One-To-Many relationship.

### <a name="BKMK_team_processsession"></a> team_processsession

See team Entity [team_processsession](team.md#BKMK_team_processsession) One-To-Many relationship.

### <a name="BKMK_metric_ProcessSessions"></a> metric_ProcessSessions

See metric Entity [metric_ProcessSessions](metric.md#BKMK_metric_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_ExpiredProcess_ProcessSessions"></a> ExpiredProcess_ProcessSessions

See expiredprocess Entity [ExpiredProcess_ProcessSessions](expiredprocess.md#BKMK_ExpiredProcess_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_KbArticle_ProcessSessions"></a> KbArticle_ProcessSessions

See kbarticle Entity [KbArticle_ProcessSessions](kbarticle.md#BKMK_KbArticle_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SocialActivity_ProcessSessions"></a> SocialActivity_ProcessSessions

See socialactivity Entity [SocialActivity_ProcessSessions](socialactivity.md#BKMK_SocialActivity_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Task_ProcessSessions"></a> Task_ProcessSessions

See task Entity [Task_ProcessSessions](task.md#BKMK_Task_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

See workflow Entity [lk_processsession_processid](workflow.md#BKMK_lk_processsession_processid) One-To-Many relationship.

### <a name="BKMK_lk_processsession_modifiedby"></a> lk_processsession_modifiedby

See systemuser Entity [lk_processsession_modifiedby](systemuser.md#BKMK_lk_processsession_modifiedby) One-To-Many relationship.

### <a name="BKMK_ConnectionRole_ProcessSessions"></a> ConnectionRole_ProcessSessions

See connectionrole Entity [ConnectionRole_ProcessSessions](connectionrole.md#BKMK_ConnectionRole_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_ProcessSessions"></a> TransactionCurrency_ProcessSessions

See transactioncurrency Entity [TransactionCurrency_ProcessSessions](transactioncurrency.md#BKMK_TransactionCurrency_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Fax_ProcessSessions"></a> Fax_ProcessSessions

See fax Entity [Fax_ProcessSessions](fax.md#BKMK_Fax_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_KbArticleTemplate_ProcessSessions"></a> KbArticleTemplate_ProcessSessions

See kbarticletemplate Entity [KbArticleTemplate_ProcessSessions](kbarticletemplate.md#BKMK_KbArticleTemplate_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Letter_ProcessSessions"></a> Letter_ProcessSessions

See letter Entity [Letter_ProcessSessions](letter.md#BKMK_Letter_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_RelationshipRole_ProcessSessions"></a> RelationshipRole_ProcessSessions

See relationshiprole Entity [RelationshipRole_ProcessSessions](relationshiprole.md#BKMK_RelationshipRole_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_CustomerRelationship_ProcessSessions"></a> CustomerRelationship_ProcessSessions

See customerrelationship Entity [CustomerRelationship_ProcessSessions](customerrelationship.md#BKMK_CustomerRelationship_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_RecurringAppointmentMaster_ProcessSessions"></a> RecurringAppointmentMaster_ProcessSessions

See recurringappointmentmaster Entity [RecurringAppointmentMaster_ProcessSessions](recurringappointmentmaster.md#BKMK_RecurringAppointmentMaster_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Email_ProcessSessions"></a> Email_ProcessSessions

See email Entity [Email_ProcessSessions](email.md#BKMK_Email_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsession_completedby"></a> lk_processsession_completedby

See systemuser Entity [lk_processsession_completedby](systemuser.md#BKMK_lk_processsession_completedby) One-To-Many relationship.

### <a name="BKMK_Contact_ProcessSessions"></a> Contact_ProcessSessions

See contact Entity [Contact_ProcessSessions](contact.md#BKMK_Contact_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Queue_ProcessSessions"></a> Queue_ProcessSessions

See queue Entity [Queue_ProcessSessions](queue.md#BKMK_Queue_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_lk_processsessionbase_createdonbehalfby"></a> lk_processsessionbase_createdonbehalfby

See systemuser Entity [lk_processsessionbase_createdonbehalfby](systemuser.md#BKMK_lk_processsessionbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_routingruleitem_ProcessSessions"></a> routingruleitem_ProcessSessions

See routingruleitem Entity [routingruleitem_ProcessSessions](routingruleitem.md#BKMK_routingruleitem_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_Subject_ProcessSessions"></a> Subject_ProcessSessions

See subject Entity [Subject_ProcessSessions](subject.md#BKMK_Subject_ProcessSessions) One-To-Many relationship.

### <a name="BKMK_SocialProfile_ProcessSessions"></a> SocialProfile_ProcessSessions

See socialprofile Entity [SocialProfile_ProcessSessions](socialprofile.md#BKMK_SocialProfile_ProcessSessions) One-To-Many relationship.
processsession

