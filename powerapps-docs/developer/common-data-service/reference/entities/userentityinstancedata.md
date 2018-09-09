---
title: "UserEntityInstanceData Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the UserEntityInstanceData entity."
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
# UserEntityInstanceData Entity Reference

Per User item instance data

## Entity Properties

**DisplayName**: User Entity Instance Data<br />
**DisplayCollectionName**: User Entity Instance Data<br />
**SchemaName**: UserEntityInstanceData<br />
**CollectionSchemaName**: UserEntityInstanceDatas<br />
**LogicalName**: userentityinstancedata<br />
**LogicalCollectionName**: userentityinstancedatas<br />
**EntitySetName**: userentityinstancedataset<br />
**PrimaryIdAttribute**: userentityinstancedataid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CommonEnd](#BKMK_CommonEnd)
- [CommonStart](#BKMK_CommonStart)
- [DueDate](#BKMK_DueDate)
- [FlagDueBy](#BKMK_FlagDueBy)
- [FlagRequest](#BKMK_FlagRequest)
- [FlagStatus](#BKMK_FlagStatus)
- [ObjectId](#BKMK_ObjectId)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PersonalCategories](#BKMK_PersonalCategories)
- [ReminderSet](#BKMK_ReminderSet)
- [ReminderTime](#BKMK_ReminderTime)
- [StartTime](#BKMK_StartTime)
- [ToDoItemFlags](#BKMK_ToDoItemFlags)
- [ToDoOrdinalDate](#BKMK_ToDoOrdinalDate)
- [ToDoSubOrdinal](#BKMK_ToDoSubOrdinal)
- [ToDoTitle](#BKMK_ToDoTitle)
- [UserEntityInstanceDataId](#BKMK_UserEntityInstanceDataId)


### <a name="BKMK_CommonEnd"></a> CommonEnd

**Description**: Common end date<br />
**DisplayName**: Common end date<br />
**LogicalName**: commonend<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CommonStart"></a> CommonStart

**Description**: Common start date<br />
**DisplayName**: Common start date<br />
**LogicalName**: commonstart<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_DueDate"></a> DueDate

**Description**: Due Date<br />
**DisplayName**: Due Date<br />
**LogicalName**: duedate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_FlagDueBy"></a> FlagDueBy

**Description**: Flag due by<br />
**DisplayName**: Flag due by<br />
**LogicalName**: flagdueby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_FlagRequest"></a> FlagRequest

**Description**: Flag request<br />
**DisplayName**: Flag Request<br />
**LogicalName**: flagrequest<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_FlagStatus"></a> FlagStatus

**Description**: Flag status.<br />
**DisplayName**: <br />
**LogicalName**: flagstatus<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ObjectId"></a> ObjectId

**Description**: Unique identifier of the source record.<br />
**DisplayName**: Object Id<br />
**LogicalName**: objectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: account,activitymimeattachment,activityparty,annotation,appointment,asyncoperation,attachment,attributemap,audit,bulkdeletefailure,bulkdeleteoperation,businessunitmap,businessunitnewsarticle,calendar,calendarrule,channelaccessprofile,channelaccessprofilerule,clientupdate,columnmapping,connection,connectionrole,connectionroleassociation,connectionroleobjecttypecode,contact,convertrule,customeraddress,customerrelationship,dependency,dependencynode,displaystring,displaystringmap,documentindex,duplicaterecord,duplicaterule,duplicaterulecondition,email,emailhash,emailsearch,entitymap,externalparty,fax,fieldpermission,fieldsecurityprofile,filtertemplate,goal,goalrollupquery,import,importdata,importentitymapping,importfile,importjob,importlog,importmap,internaladdress,invaliddependency,isvconfig,kbarticle,kbarticlecomment,kbarticletemplate,knowledgearticle,knowledgebaserecord,letter,license,lookupmapping,mailbox,mailmergetemplate,metric,notification,organization,organizationstatistic,ownermapping,phonecall,picklistmapping,pluginassembly,plugintype,plugintypestatistic,principalattributeaccessmap,principalentitymap,principalobjectaccess,principalobjectattributeaccess,privilege,processsession,publisher,publisheraddress,queue,queueitem,recurringappointmentmaster,relationshiprole,relationshiprolemap,report,reportcategory,reportentity,reportlink,reportvisibility,ribboncommand,ribboncontextgroup,ribboncustomization,ribbondiff,ribbonrule,ribbontabtocommandmap,role,roletemplate,rollupfield,routingrule,routingruleitem,savedquery,savedqueryvisualization,sdkmessage,sdkmessagefilter,sdkmessagepair,sdkmessageprocessingstep,sdkmessageprocessingstepimage,sdkmessageprocessingstepsecureconfig,sdkmessagerequest,sdkmessagerequestfield,sdkmessageresponse,sdkmessageresponsefield,serviceendpoint,sharepointdocumentlocation,sharepointsite,sitemap,sla,socialactivity,solution,solutioncomponent,statusmap,stringmap,subject,subscription,subscriptionmanuallytrackedobject,subscriptionsyncinfo,systemuser,systemuserbusinessunitentitymap,task,team,teammembership,template,territory,theme,timezonedefinition,timezonelocalizedname,timezonerule,transactioncurrency,transformationmapping,transformationparametermapping,unresolvedaddress,userentityuisettings,userfiscalcalendar,userform,usermapping,userquery,userqueryvisualization,webresource,webwizard,wizardaccessprivilege,wizardpage,workflow,workflowdependency,workflowlog,workflowwaitsubscription


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Object Type Code<br />
**DisplayName**: <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the user entity instance data.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Type of the owner of the object.<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_PersonalCategories"></a> PersonalCategories

**Description**: Personal categories<br />
**DisplayName**: personal categories<br />
**LogicalName**: personalcategories<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_ReminderSet"></a> ReminderSet

**Description**: Indicates whether a reminder is set on this object.<br />
**DisplayName**: Is Reminder set<br />
**LogicalName**: reminderset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Remind Set
- **FalseOption Value**: 0 **Label**: Reminder Not Set

**DefaultValue**: False


### <a name="BKMK_ReminderTime"></a> ReminderTime

**Description**: Reminder time<br />
**DisplayName**: Reminder time<br />
**LogicalName**: remindertime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_StartTime"></a> StartTime

**Description**: Start Time<br />
**DisplayName**: Start Time<br />
**LogicalName**: starttime<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ToDoItemFlags"></a> ToDoItemFlags

**Description**: To Do item flags.<br />
**DisplayName**: <br />
**LogicalName**: todoitemflags<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_ToDoOrdinalDate"></a> ToDoOrdinalDate

**Description**: For internal use only.<br />
**DisplayName**: To Do Primary Sort Date<br />
**LogicalName**: todoordinaldate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ToDoSubOrdinal"></a> ToDoSubOrdinal

**Description**: For internal use only.<br />
**DisplayName**: To Do Sort Tie Breaker<br />
**LogicalName**: todosubordinal<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_ToDoTitle"></a> ToDoTitle

**Description**: For internal use only.<br />
**DisplayName**: To Do Title<br />
**LogicalName**: todotitle<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4000


### <a name="BKMK_UserEntityInstanceDataId"></a> UserEntityInstanceDataId

**Description**: Unique identifier user entity<br />
**DisplayName**: <br />
**LogicalName**: userentityinstancedataid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner of the object.<br />
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

**Description**: Unique identifier of the business unit that owns this.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns this object.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns this object.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [userentityinstancedata_territory](#BKMK_userentityinstancedata_territory)
- [theme_UserEntityInstanceDatas](#BKMK_theme_UserEntityInstanceDatas)
- [usermapping_UserEntityInstanceDatas](#BKMK_usermapping_UserEntityInstanceDatas)
- [knowledgearticle_UserEntityInstanceDatas](#BKMK_knowledgearticle_UserEntityInstanceDatas)
- [mailbox_userentityinstancedatas](#BKMK_mailbox_userentityinstancedatas)
- [channelaccessprofile_UserEntityInstanceDatas](#BKMK_channelaccessprofile_UserEntityInstanceDatas)
- [externalparty_UserEntityInstanceDatas](#BKMK_externalparty_UserEntityInstanceDatas)
- [profilerule_UserEntityInstanceDatas](#BKMK_profilerule_UserEntityInstanceDatas)
- [KnowledgeBaseRecord_UserEntityInstanceDatas](#BKMK_KnowledgeBaseRecord_UserEntityInstanceDatas)
- [userentityinstancedata_pluginassembly](#BKMK_userentityinstancedata_pluginassembly)
- [userentityinstancedata_letter](#BKMK_userentityinstancedata_letter)
- [userentityinstancedata_organization](#BKMK_userentityinstancedata_organization)
- [userentityinstancedata_owning_user](#BKMK_userentityinstancedata_owning_user)
- [userentityinstancedata_kbarticlecomment](#BKMK_userentityinstancedata_kbarticlecomment)
- [userentityinstancedata_processsession](#BKMK_userentityinstancedata_processsession)
- [userentityinstancedata_relationshiprolemap](#BKMK_userentityinstancedata_relationshiprolemap)
- [userentityinstancedata_sdkmessage](#BKMK_userentityinstancedata_sdkmessage)
- [userentityinstancedata_appointment](#BKMK_userentityinstancedata_appointment)
- [userentityinstancedata_contact](#BKMK_userentityinstancedata_contact)
- [userentityinstancedata_picklistmapping](#BKMK_userentityinstancedata_picklistmapping)
- [userentityinstancedata_workflow](#BKMK_userentityinstancedata_workflow)
- [userentityinstancedata_connectionrole](#BKMK_userentityinstancedata_connectionrole)
- [userentityinstancedata_sdkmessagepair](#BKMK_userentityinstancedata_sdkmessagepair)
- [userentityinstancedata_timezonelocalizedname](#BKMK_userentityinstancedata_timezonelocalizedname)
- [userentityinstancedata_savedquery](#BKMK_userentityinstancedata_savedquery)
- [userentityinstancedata_connection](#BKMK_userentityinstancedata_connection)
- [userentityinstancedata_socialactivity](#BKMK_userentityinstancedata_socialactivity)
- [userentityinstancedata_transactioncurrency](#BKMK_userentityinstancedata_transactioncurrency)
- [userentityinstancedata_importfile](#BKMK_userentityinstancedata_importfile)
- [userentityinstancedata_solution](#BKMK_userentityinstancedata_solution)
- [userentityinstancedata_transformationparametermapping](#BKMK_userentityinstancedata_transformationparametermapping)
- [userentityinstancedata_plugintype](#BKMK_userentityinstancedata_plugintype)
- [userentityinstancedata_userentityuisettings](#BKMK_userentityinstancedata_userentityuisettings)
- [userentityinstancedata_phonecall](#BKMK_userentityinstancedata_phonecall)
- [userentityinstancedata_sdkmessagerequest](#BKMK_userentityinstancedata_sdkmessagerequest)
- [userentityinstancedata_sdkmessageprocessingstepsecureconfig](#BKMK_userentityinstancedata_sdkmessageprocessingstepsecureconfig)
- [userentityinstancedata_customeraddress](#BKMK_userentityinstancedata_customeraddress)
- [userentityinstancedata_invaliddependency](#BKMK_userentityinstancedata_invaliddependency)
- [userentityinstancedata_recurringappointmentmaster](#BKMK_userentityinstancedata_recurringappointmentmaster)
- [userentityinstancedata_queueitem](#BKMK_userentityinstancedata_queueitem)
- [userentityinstancedata_reportvisibility](#BKMK_userentityinstancedata_reportvisibility)
- [userentityinstancedata_import](#BKMK_userentityinstancedata_import)
- [userentityinstancedata_goalrollupquery](#BKMK_userentityinstancedata_goalrollupquery)
- [userentityinstancedata_workflowlog](#BKMK_userentityinstancedata_workflowlog)
- [ConvertRule_userentityinstancedatas](#BKMK_ConvertRule_userentityinstancedatas)
- [userentityinstancedata_team](#BKMK_userentityinstancedata_team)
- [userentityinstancedata_ribboncustomization](#BKMK_userentityinstancedata_ribboncustomization)
- [userentityinstancedata_userqueryvisualization](#BKMK_userentityinstancedata_userqueryvisualization)
- [userentityinstancedata_businessunitnewsarticle](#BKMK_userentityinstancedata_businessunitnewsarticle)
- [userentityinstancedata_kbarticletemplate](#BKMK_userentityinstancedata_kbarticletemplate)
- [userentityinstancedata_connectionroleobjecttypecode](#BKMK_userentityinstancedata_connectionroleobjecttypecode)
- [userentityinstancedata_email](#BKMK_userentityinstancedata_email)
- [userentityinstancedata_sitemap](#BKMK_userentityinstancedata_sitemap)
- [userentityinstancedata_transformationmapping](#BKMK_userentityinstancedata_transformationmapping)
- [userentityinstancedata_fieldpermission](#BKMK_userentityinstancedata_fieldpermission)
- [userentityinstancedata_task](#BKMK_userentityinstancedata_task)
- [userentityinstancedata_savedqueryvisualization](#BKMK_userentityinstancedata_savedqueryvisualization)
- [userentityinstancedata_importlog](#BKMK_userentityinstancedata_importlog)
- [userentityinstancedata_connectionroleassociation](#BKMK_userentityinstancedata_connectionroleassociation)
- [userentityinstancedata_metric](#BKMK_userentityinstancedata_metric)
- [slabase_userentityinstancedatas](#BKMK_slabase_userentityinstancedatas)
- [userentityinstancedata_kbarticle](#BKMK_userentityinstancedata_kbarticle)
- [userentityinstancedata_annotation](#BKMK_userentityinstancedata_annotation)
- [userentityinstancedata_importentitymapping](#BKMK_userentityinstancedata_importentitymapping)
- [team_userentityinstancedata](#BKMK_team_userentityinstancedata)
- [userentityinstancedata_dependency](#BKMK_userentityinstancedata_dependency)
- [userentityinstancedata_duplicaterecord](#BKMK_userentityinstancedata_duplicaterecord)
- [userentityinstancedata_timezonedefinition](#BKMK_userentityinstancedata_timezonedefinition)
- [userentityinstancedata_calendar](#BKMK_userentityinstancedata_calendar)
- [userentityinstancedata_sdkmessageprocessingstep](#BKMK_userentityinstancedata_sdkmessageprocessingstep)
- [userentityinstancedata_systemuser](#BKMK_userentityinstancedata_systemuser)
- [userentityinstancedata_sdkmessagerequestfield](#BKMK_userentityinstancedata_sdkmessagerequestfield)
- [userentityinstancedata_plugintypestatistic](#BKMK_userentityinstancedata_plugintypestatistic)
- [userentityinstancedata_rollupfield](#BKMK_userentityinstancedata_rollupfield)
- [userentityinstancedata_relationshiprole](#BKMK_userentityinstancedata_relationshiprole)
- [userentityinstancedata_activitymimeattachment](#BKMK_userentityinstancedata_activitymimeattachment)
- [userentityinstancedata_role](#BKMK_userentityinstancedata_role)
- [userentityinstancedata_columnmapping](#BKMK_userentityinstancedata_columnmapping)
- [userentityinstancedata_publisheraddress](#BKMK_userentityinstancedata_publisheraddress)
- [userentityinstancedata_audit](#BKMK_userentityinstancedata_audit)
- [userentityinstancedata_subject](#BKMK_userentityinstancedata_subject)
- [userentityinstancedata_attributemap](#BKMK_userentityinstancedata_attributemap)
- [userentityinstancedata_lookupmapping](#BKMK_userentityinstancedata_lookupmapping)
- [userentityinstancedata_account](#BKMK_userentityinstancedata_account)
- [userentityinstancedata_sdkmessageresponsefield](#BKMK_userentityinstancedata_sdkmessageresponsefield)
- [userentityinstancedata_teammembership](#BKMK_userentityinstancedata_teammembership)
- [routingrule_userentityinstancedatas](#BKMK_routingrule_userentityinstancedatas)
- [userentityinstancedata_principalobjectattributeaccess](#BKMK_userentityinstancedata_principalobjectattributeaccess)
- [userentityinstancedata_duplicaterule](#BKMK_userentityinstancedata_duplicaterule)
- [userentityinstancedata_report](#BKMK_userentityinstancedata_report)
- [userentityinstancedata_isvconfig](#BKMK_userentityinstancedata_isvconfig)
- [userentityinstancedata_goal](#BKMK_userentityinstancedata_goal)
- [userentityinstancedata_mailmergetemplate](#BKMK_userentityinstancedata_mailmergetemplate)
- [userentityinstancedata_bulkdeleteoperation](#BKMK_userentityinstancedata_bulkdeleteoperation)
- [userentityinstancedata_sharepointsite](#BKMK_userentityinstancedata_sharepointsite)
- [userentityinstancedata_publisher](#BKMK_userentityinstancedata_publisher)
- [userentityinstancedata_businessunit](#BKMK_userentityinstancedata_businessunit)
- [userentityinstancedata_userform](#BKMK_userentityinstancedata_userform)
- [userentityinstancedata_license](#BKMK_userentityinstancedata_license)
- [userentityinstancedata_solutioncomponent](#BKMK_userentityinstancedata_solutioncomponent)
- [userentityinstancedata_reportcategory](#BKMK_userentityinstancedata_reportcategory)
- [userentityinstancedata_queue](#BKMK_userentityinstancedata_queue)
- [userentityinstancedata_duplicaterulecondition](#BKMK_userentityinstancedata_duplicaterulecondition)
- [userentityinstancedata_webresource](#BKMK_userentityinstancedata_webresource)
- [userentityinstancedata_workflowdependency](#BKMK_userentityinstancedata_workflowdependency)
- [routingruleitem_userentityinstancedatas](#BKMK_routingruleitem_userentityinstancedatas)
- [userentityinstancedata_customerrelationship](#BKMK_userentityinstancedata_customerrelationship)
- [userentityinstancedata_entitymap](#BKMK_userentityinstancedata_entitymap)
- [userentityinstancedata_fieldsecurityprofile](#BKMK_userentityinstancedata_fieldsecurityprofile)
- [userentityinstancedata_asyncoperation](#BKMK_userentityinstancedata_asyncoperation)
- [userentityinstancedata_timezonerule](#BKMK_userentityinstancedata_timezonerule)
- [userentityinstancedata_ownermapping](#BKMK_userentityinstancedata_ownermapping)
- [userentityinstancedata_activityparty](#BKMK_userentityinstancedata_activityparty)
- [userentityinstancedata_displaystring](#BKMK_userentityinstancedata_displaystring)
- [userentityinstancedata_importjob](#BKMK_userentityinstancedata_importjob)
- [userentityinstancedata_sdkmessageprocessingstepimage](#BKMK_userentityinstancedata_sdkmessageprocessingstepimage)
- [userentityinstancedata_template](#BKMK_userentityinstancedata_template)
- [userentityinstancedata_userquery](#BKMK_userentityinstancedata_userquery)
- [userentityinstancedata_bulkdeletefailure](#BKMK_userentityinstancedata_bulkdeletefailure)
- [userentityinstancedata_sharepointdocumentlocation](#BKMK_userentityinstancedata_sharepointdocumentlocation)
- [userentityinstancedata_sdkmessageresponse](#BKMK_userentityinstancedata_sdkmessageresponse)
- [userentityinstancedata_serviceendpoint](#BKMK_userentityinstancedata_serviceendpoint)
- [userentityinstancedata_reportentity](#BKMK_userentityinstancedata_reportentity)
- [userentityinstancedata_importmap](#BKMK_userentityinstancedata_importmap)
- [userentityinstancedata_fax](#BKMK_userentityinstancedata_fax)
- [userentityinstancedata_privilege](#BKMK_userentityinstancedata_privilege)
- [userentityinstancedata_sdkmessagefilter](#BKMK_userentityinstancedata_sdkmessagefilter)
- [userentityinstancedata_reportlink](#BKMK_userentityinstancedata_reportlink)


### <a name="BKMK_userentityinstancedata_territory"></a> userentityinstancedata_territory

See territory Entity [userentityinstancedata_territory](territory.md#BKMK_userentityinstancedata_territory) One-To-Many relationship.

### <a name="BKMK_theme_UserEntityInstanceDatas"></a> theme_UserEntityInstanceDatas

See theme Entity [theme_UserEntityInstanceDatas](theme.md#BKMK_theme_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_usermapping_UserEntityInstanceDatas"></a> usermapping_UserEntityInstanceDatas

See usermapping Entity [usermapping_UserEntityInstanceDatas](usermapping.md#BKMK_usermapping_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_UserEntityInstanceDatas"></a> knowledgearticle_UserEntityInstanceDatas

See knowledgearticle Entity [knowledgearticle_UserEntityInstanceDatas](knowledgearticle.md#BKMK_knowledgearticle_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_mailbox_userentityinstancedatas"></a> mailbox_userentityinstancedatas

See mailbox Entity [mailbox_userentityinstancedatas](mailbox.md#BKMK_mailbox_userentityinstancedatas) One-To-Many relationship.

### <a name="BKMK_channelaccessprofile_UserEntityInstanceDatas"></a> channelaccessprofile_UserEntityInstanceDatas

See channelaccessprofile Entity [channelaccessprofile_UserEntityInstanceDatas](channelaccessprofile.md#BKMK_channelaccessprofile_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_externalparty_UserEntityInstanceDatas"></a> externalparty_UserEntityInstanceDatas

See externalparty Entity [externalparty_UserEntityInstanceDatas](externalparty.md#BKMK_externalparty_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_profilerule_UserEntityInstanceDatas"></a> profilerule_UserEntityInstanceDatas

See channelaccessprofilerule Entity [profilerule_UserEntityInstanceDatas](channelaccessprofilerule.md#BKMK_profilerule_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_UserEntityInstanceDatas"></a> KnowledgeBaseRecord_UserEntityInstanceDatas

See knowledgebaserecord Entity [KnowledgeBaseRecord_UserEntityInstanceDatas](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_UserEntityInstanceDatas) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_pluginassembly"></a> userentityinstancedata_pluginassembly

See pluginassembly Entity [userentityinstancedata_pluginassembly](pluginassembly.md#BKMK_userentityinstancedata_pluginassembly) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_letter"></a> userentityinstancedata_letter

See letter Entity [userentityinstancedata_letter](letter.md#BKMK_userentityinstancedata_letter) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_organization"></a> userentityinstancedata_organization

See organization Entity [userentityinstancedata_organization](organization.md#BKMK_userentityinstancedata_organization) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_owning_user"></a> userentityinstancedata_owning_user

See systemuser Entity [userentityinstancedata_owning_user](systemuser.md#BKMK_userentityinstancedata_owning_user) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_kbarticlecomment"></a> userentityinstancedata_kbarticlecomment

See kbarticlecomment Entity [userentityinstancedata_kbarticlecomment](kbarticlecomment.md#BKMK_userentityinstancedata_kbarticlecomment) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_processsession"></a> userentityinstancedata_processsession

See processsession Entity [userentityinstancedata_processsession](processsession.md#BKMK_userentityinstancedata_processsession) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_relationshiprolemap"></a> userentityinstancedata_relationshiprolemap

See relationshiprolemap Entity [userentityinstancedata_relationshiprolemap](relationshiprolemap.md#BKMK_userentityinstancedata_relationshiprolemap) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessage"></a> userentityinstancedata_sdkmessage

See sdkmessage Entity [userentityinstancedata_sdkmessage](sdkmessage.md#BKMK_userentityinstancedata_sdkmessage) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_appointment"></a> userentityinstancedata_appointment

See appointment Entity [userentityinstancedata_appointment](appointment.md#BKMK_userentityinstancedata_appointment) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_contact"></a> userentityinstancedata_contact

See contact Entity [userentityinstancedata_contact](contact.md#BKMK_userentityinstancedata_contact) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_picklistmapping"></a> userentityinstancedata_picklistmapping

See picklistmapping Entity [userentityinstancedata_picklistmapping](picklistmapping.md#BKMK_userentityinstancedata_picklistmapping) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_workflow"></a> userentityinstancedata_workflow

See workflow Entity [userentityinstancedata_workflow](workflow.md#BKMK_userentityinstancedata_workflow) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_connectionrole"></a> userentityinstancedata_connectionrole

See connectionrole Entity [userentityinstancedata_connectionrole](connectionrole.md#BKMK_userentityinstancedata_connectionrole) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessagepair"></a> userentityinstancedata_sdkmessagepair

See sdkmessagepair Entity [userentityinstancedata_sdkmessagepair](sdkmessagepair.md#BKMK_userentityinstancedata_sdkmessagepair) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_timezonelocalizedname"></a> userentityinstancedata_timezonelocalizedname

See timezonelocalizedname Entity [userentityinstancedata_timezonelocalizedname](timezonelocalizedname.md#BKMK_userentityinstancedata_timezonelocalizedname) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_savedquery"></a> userentityinstancedata_savedquery

See savedquery Entity [userentityinstancedata_savedquery](savedquery.md#BKMK_userentityinstancedata_savedquery) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_connection"></a> userentityinstancedata_connection

See connection Entity [userentityinstancedata_connection](connection.md#BKMK_userentityinstancedata_connection) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_socialactivity"></a> userentityinstancedata_socialactivity

See socialactivity Entity [userentityinstancedata_socialactivity](socialactivity.md#BKMK_userentityinstancedata_socialactivity) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_transactioncurrency"></a> userentityinstancedata_transactioncurrency

See transactioncurrency Entity [userentityinstancedata_transactioncurrency](transactioncurrency.md#BKMK_userentityinstancedata_transactioncurrency) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_importfile"></a> userentityinstancedata_importfile

See importfile Entity [userentityinstancedata_importfile](importfile.md#BKMK_userentityinstancedata_importfile) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_solution"></a> userentityinstancedata_solution

See solution Entity [userentityinstancedata_solution](solution.md#BKMK_userentityinstancedata_solution) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_transformationparametermapping"></a> userentityinstancedata_transformationparametermapping

See transformationparametermapping Entity [userentityinstancedata_transformationparametermapping](transformationparametermapping.md#BKMK_userentityinstancedata_transformationparametermapping) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_plugintype"></a> userentityinstancedata_plugintype

See plugintype Entity [userentityinstancedata_plugintype](plugintype.md#BKMK_userentityinstancedata_plugintype) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_userentityuisettings"></a> userentityinstancedata_userentityuisettings

See userentityuisettings Entity [userentityinstancedata_userentityuisettings](userentityuisettings.md#BKMK_userentityinstancedata_userentityuisettings) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_phonecall"></a> userentityinstancedata_phonecall

See phonecall Entity [userentityinstancedata_phonecall](phonecall.md#BKMK_userentityinstancedata_phonecall) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessagerequest"></a> userentityinstancedata_sdkmessagerequest

See sdkmessagerequest Entity [userentityinstancedata_sdkmessagerequest](sdkmessagerequest.md#BKMK_userentityinstancedata_sdkmessagerequest) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessageprocessingstepsecureconfig"></a> userentityinstancedata_sdkmessageprocessingstepsecureconfig

See sdkmessageprocessingstepsecureconfig Entity [userentityinstancedata_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_userentityinstancedata_sdkmessageprocessingstepsecureconfig) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_customeraddress"></a> userentityinstancedata_customeraddress

See customeraddress Entity [userentityinstancedata_customeraddress](customeraddress.md#BKMK_userentityinstancedata_customeraddress) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_invaliddependency"></a> userentityinstancedata_invaliddependency

See invaliddependency Entity [userentityinstancedata_invaliddependency](invaliddependency.md#BKMK_userentityinstancedata_invaliddependency) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_recurringappointmentmaster"></a> userentityinstancedata_recurringappointmentmaster

See recurringappointmentmaster Entity [userentityinstancedata_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_userentityinstancedata_recurringappointmentmaster) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_queueitem"></a> userentityinstancedata_queueitem

See queueitem Entity [userentityinstancedata_queueitem](queueitem.md#BKMK_userentityinstancedata_queueitem) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_reportvisibility"></a> userentityinstancedata_reportvisibility

See reportvisibility Entity [userentityinstancedata_reportvisibility](reportvisibility.md#BKMK_userentityinstancedata_reportvisibility) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_import"></a> userentityinstancedata_import

See import Entity [userentityinstancedata_import](import.md#BKMK_userentityinstancedata_import) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_goalrollupquery"></a> userentityinstancedata_goalrollupquery

See goalrollupquery Entity [userentityinstancedata_goalrollupquery](goalrollupquery.md#BKMK_userentityinstancedata_goalrollupquery) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_workflowlog"></a> userentityinstancedata_workflowlog

See workflowlog Entity [userentityinstancedata_workflowlog](workflowlog.md#BKMK_userentityinstancedata_workflowlog) One-To-Many relationship.

### <a name="BKMK_ConvertRule_userentityinstancedatas"></a> ConvertRule_userentityinstancedatas

See convertrule Entity [ConvertRule_userentityinstancedatas](convertrule.md#BKMK_ConvertRule_userentityinstancedatas) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_team"></a> userentityinstancedata_team

See team Entity [userentityinstancedata_team](team.md#BKMK_userentityinstancedata_team) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_ribboncustomization"></a> userentityinstancedata_ribboncustomization

See ribboncustomization Entity [userentityinstancedata_ribboncustomization](ribboncustomization.md#BKMK_userentityinstancedata_ribboncustomization) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_userqueryvisualization"></a> userentityinstancedata_userqueryvisualization

See userqueryvisualization Entity [userentityinstancedata_userqueryvisualization](userqueryvisualization.md#BKMK_userentityinstancedata_userqueryvisualization) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_businessunitnewsarticle"></a> userentityinstancedata_businessunitnewsarticle

See businessunitnewsarticle Entity [userentityinstancedata_businessunitnewsarticle](businessunitnewsarticle.md#BKMK_userentityinstancedata_businessunitnewsarticle) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_kbarticletemplate"></a> userentityinstancedata_kbarticletemplate

See kbarticletemplate Entity [userentityinstancedata_kbarticletemplate](kbarticletemplate.md#BKMK_userentityinstancedata_kbarticletemplate) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_connectionroleobjecttypecode"></a> userentityinstancedata_connectionroleobjecttypecode

See connectionroleobjecttypecode Entity [userentityinstancedata_connectionroleobjecttypecode](connectionroleobjecttypecode.md#BKMK_userentityinstancedata_connectionroleobjecttypecode) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_email"></a> userentityinstancedata_email

See email Entity [userentityinstancedata_email](email.md#BKMK_userentityinstancedata_email) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sitemap"></a> userentityinstancedata_sitemap

See sitemap Entity [userentityinstancedata_sitemap](sitemap.md#BKMK_userentityinstancedata_sitemap) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_transformationmapping"></a> userentityinstancedata_transformationmapping

See transformationmapping Entity [userentityinstancedata_transformationmapping](transformationmapping.md#BKMK_userentityinstancedata_transformationmapping) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_fieldpermission"></a> userentityinstancedata_fieldpermission

See fieldpermission Entity [userentityinstancedata_fieldpermission](fieldpermission.md#BKMK_userentityinstancedata_fieldpermission) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_task"></a> userentityinstancedata_task

See task Entity [userentityinstancedata_task](task.md#BKMK_userentityinstancedata_task) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_savedqueryvisualization"></a> userentityinstancedata_savedqueryvisualization

See savedqueryvisualization Entity [userentityinstancedata_savedqueryvisualization](savedqueryvisualization.md#BKMK_userentityinstancedata_savedqueryvisualization) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_importlog"></a> userentityinstancedata_importlog

See importlog Entity [userentityinstancedata_importlog](importlog.md#BKMK_userentityinstancedata_importlog) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_connectionroleassociation"></a> userentityinstancedata_connectionroleassociation

See connectionroleassociation Entity [userentityinstancedata_connectionroleassociation](connectionroleassociation.md#BKMK_userentityinstancedata_connectionroleassociation) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_metric"></a> userentityinstancedata_metric

See metric Entity [userentityinstancedata_metric](metric.md#BKMK_userentityinstancedata_metric) One-To-Many relationship.

### <a name="BKMK_slabase_userentityinstancedatas"></a> slabase_userentityinstancedatas

See sla Entity [slabase_userentityinstancedatas](sla.md#BKMK_slabase_userentityinstancedatas) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_kbarticle"></a> userentityinstancedata_kbarticle

See kbarticle Entity [userentityinstancedata_kbarticle](kbarticle.md#BKMK_userentityinstancedata_kbarticle) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_annotation"></a> userentityinstancedata_annotation

See annotation Entity [userentityinstancedata_annotation](annotation.md#BKMK_userentityinstancedata_annotation) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_importentitymapping"></a> userentityinstancedata_importentitymapping

See importentitymapping Entity [userentityinstancedata_importentitymapping](importentitymapping.md#BKMK_userentityinstancedata_importentitymapping) One-To-Many relationship.

### <a name="BKMK_team_userentityinstancedata"></a> team_userentityinstancedata

See team Entity [team_userentityinstancedata](team.md#BKMK_team_userentityinstancedata) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_dependency"></a> userentityinstancedata_dependency

See dependency Entity [userentityinstancedata_dependency](dependency.md#BKMK_userentityinstancedata_dependency) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_duplicaterecord"></a> userentityinstancedata_duplicaterecord

See duplicaterecord Entity [userentityinstancedata_duplicaterecord](duplicaterecord.md#BKMK_userentityinstancedata_duplicaterecord) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_timezonedefinition"></a> userentityinstancedata_timezonedefinition

See timezonedefinition Entity [userentityinstancedata_timezonedefinition](timezonedefinition.md#BKMK_userentityinstancedata_timezonedefinition) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_calendar"></a> userentityinstancedata_calendar

See calendar Entity [userentityinstancedata_calendar](calendar.md#BKMK_userentityinstancedata_calendar) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessageprocessingstep"></a> userentityinstancedata_sdkmessageprocessingstep

See sdkmessageprocessingstep Entity [userentityinstancedata_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_userentityinstancedata_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_systemuser"></a> userentityinstancedata_systemuser

See systemuser Entity [userentityinstancedata_systemuser](systemuser.md#BKMK_userentityinstancedata_systemuser) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessagerequestfield"></a> userentityinstancedata_sdkmessagerequestfield

See sdkmessagerequestfield Entity [userentityinstancedata_sdkmessagerequestfield](sdkmessagerequestfield.md#BKMK_userentityinstancedata_sdkmessagerequestfield) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_plugintypestatistic"></a> userentityinstancedata_plugintypestatistic

See plugintypestatistic Entity [userentityinstancedata_plugintypestatistic](plugintypestatistic.md#BKMK_userentityinstancedata_plugintypestatistic) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_rollupfield"></a> userentityinstancedata_rollupfield

See rollupfield Entity [userentityinstancedata_rollupfield](rollupfield.md#BKMK_userentityinstancedata_rollupfield) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_relationshiprole"></a> userentityinstancedata_relationshiprole

See relationshiprole Entity [userentityinstancedata_relationshiprole](relationshiprole.md#BKMK_userentityinstancedata_relationshiprole) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_activitymimeattachment"></a> userentityinstancedata_activitymimeattachment

See activitymimeattachment Entity [userentityinstancedata_activitymimeattachment](activitymimeattachment.md#BKMK_userentityinstancedata_activitymimeattachment) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_role"></a> userentityinstancedata_role

See role Entity [userentityinstancedata_role](role.md#BKMK_userentityinstancedata_role) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_columnmapping"></a> userentityinstancedata_columnmapping

See columnmapping Entity [userentityinstancedata_columnmapping](columnmapping.md#BKMK_userentityinstancedata_columnmapping) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_publisheraddress"></a> userentityinstancedata_publisheraddress

See publisheraddress Entity [userentityinstancedata_publisheraddress](publisheraddress.md#BKMK_userentityinstancedata_publisheraddress) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_audit"></a> userentityinstancedata_audit

See audit Entity [userentityinstancedata_audit](audit.md#BKMK_userentityinstancedata_audit) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_subject"></a> userentityinstancedata_subject

See subject Entity [userentityinstancedata_subject](subject.md#BKMK_userentityinstancedata_subject) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_attributemap"></a> userentityinstancedata_attributemap

See attributemap Entity [userentityinstancedata_attributemap](attributemap.md#BKMK_userentityinstancedata_attributemap) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_lookupmapping"></a> userentityinstancedata_lookupmapping

See lookupmapping Entity [userentityinstancedata_lookupmapping](lookupmapping.md#BKMK_userentityinstancedata_lookupmapping) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_account"></a> userentityinstancedata_account

See account Entity [userentityinstancedata_account](account.md#BKMK_userentityinstancedata_account) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessageresponsefield"></a> userentityinstancedata_sdkmessageresponsefield

See sdkmessageresponsefield Entity [userentityinstancedata_sdkmessageresponsefield](sdkmessageresponsefield.md#BKMK_userentityinstancedata_sdkmessageresponsefield) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_teammembership"></a> userentityinstancedata_teammembership

See teammembership Entity [userentityinstancedata_teammembership](teammembership.md#BKMK_userentityinstancedata_teammembership) One-To-Many relationship.

### <a name="BKMK_routingrule_userentityinstancedatas"></a> routingrule_userentityinstancedatas

See routingrule Entity [routingrule_userentityinstancedatas](routingrule.md#BKMK_routingrule_userentityinstancedatas) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_principalobjectattributeaccess"></a> userentityinstancedata_principalobjectattributeaccess

See principalobjectattributeaccess Entity [userentityinstancedata_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_userentityinstancedata_principalobjectattributeaccess) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_duplicaterule"></a> userentityinstancedata_duplicaterule

See duplicaterule Entity [userentityinstancedata_duplicaterule](duplicaterule.md#BKMK_userentityinstancedata_duplicaterule) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_report"></a> userentityinstancedata_report

See report Entity [userentityinstancedata_report](report.md#BKMK_userentityinstancedata_report) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_isvconfig"></a> userentityinstancedata_isvconfig

See isvconfig Entity [userentityinstancedata_isvconfig](isvconfig.md#BKMK_userentityinstancedata_isvconfig) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_goal"></a> userentityinstancedata_goal

See goal Entity [userentityinstancedata_goal](goal.md#BKMK_userentityinstancedata_goal) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_mailmergetemplate"></a> userentityinstancedata_mailmergetemplate

See mailmergetemplate Entity [userentityinstancedata_mailmergetemplate](mailmergetemplate.md#BKMK_userentityinstancedata_mailmergetemplate) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_bulkdeleteoperation"></a> userentityinstancedata_bulkdeleteoperation

See bulkdeleteoperation Entity [userentityinstancedata_bulkdeleteoperation](bulkdeleteoperation.md#BKMK_userentityinstancedata_bulkdeleteoperation) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sharepointsite"></a> userentityinstancedata_sharepointsite

See sharepointsite Entity [userentityinstancedata_sharepointsite](sharepointsite.md#BKMK_userentityinstancedata_sharepointsite) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_publisher"></a> userentityinstancedata_publisher

See publisher Entity [userentityinstancedata_publisher](publisher.md#BKMK_userentityinstancedata_publisher) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_businessunit"></a> userentityinstancedata_businessunit

See businessunit Entity [userentityinstancedata_businessunit](businessunit.md#BKMK_userentityinstancedata_businessunit) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_userform"></a> userentityinstancedata_userform

See userform Entity [userentityinstancedata_userform](userform.md#BKMK_userentityinstancedata_userform) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_license"></a> userentityinstancedata_license

See license Entity [userentityinstancedata_license](license.md#BKMK_userentityinstancedata_license) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_solutioncomponent"></a> userentityinstancedata_solutioncomponent

See solutioncomponent Entity [userentityinstancedata_solutioncomponent](solutioncomponent.md#BKMK_userentityinstancedata_solutioncomponent) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_reportcategory"></a> userentityinstancedata_reportcategory

See reportcategory Entity [userentityinstancedata_reportcategory](reportcategory.md#BKMK_userentityinstancedata_reportcategory) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_queue"></a> userentityinstancedata_queue

See queue Entity [userentityinstancedata_queue](queue.md#BKMK_userentityinstancedata_queue) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_duplicaterulecondition"></a> userentityinstancedata_duplicaterulecondition

See duplicaterulecondition Entity [userentityinstancedata_duplicaterulecondition](duplicaterulecondition.md#BKMK_userentityinstancedata_duplicaterulecondition) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_webresource"></a> userentityinstancedata_webresource

See webresource Entity [userentityinstancedata_webresource](webresource.md#BKMK_userentityinstancedata_webresource) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_workflowdependency"></a> userentityinstancedata_workflowdependency

See workflowdependency Entity [userentityinstancedata_workflowdependency](workflowdependency.md#BKMK_userentityinstancedata_workflowdependency) One-To-Many relationship.

### <a name="BKMK_routingruleitem_userentityinstancedatas"></a> routingruleitem_userentityinstancedatas

See routingruleitem Entity [routingruleitem_userentityinstancedatas](routingruleitem.md#BKMK_routingruleitem_userentityinstancedatas) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_customerrelationship"></a> userentityinstancedata_customerrelationship

See customerrelationship Entity [userentityinstancedata_customerrelationship](customerrelationship.md#BKMK_userentityinstancedata_customerrelationship) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_entitymap"></a> userentityinstancedata_entitymap

See entitymap Entity [userentityinstancedata_entitymap](entitymap.md#BKMK_userentityinstancedata_entitymap) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_fieldsecurityprofile"></a> userentityinstancedata_fieldsecurityprofile

See fieldsecurityprofile Entity [userentityinstancedata_fieldsecurityprofile](fieldsecurityprofile.md#BKMK_userentityinstancedata_fieldsecurityprofile) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_asyncoperation"></a> userentityinstancedata_asyncoperation

See asyncoperation Entity [userentityinstancedata_asyncoperation](asyncoperation.md#BKMK_userentityinstancedata_asyncoperation) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_timezonerule"></a> userentityinstancedata_timezonerule

See timezonerule Entity [userentityinstancedata_timezonerule](timezonerule.md#BKMK_userentityinstancedata_timezonerule) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_ownermapping"></a> userentityinstancedata_ownermapping

See ownermapping Entity [userentityinstancedata_ownermapping](ownermapping.md#BKMK_userentityinstancedata_ownermapping) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_activityparty"></a> userentityinstancedata_activityparty

See activityparty Entity [userentityinstancedata_activityparty](activityparty.md#BKMK_userentityinstancedata_activityparty) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_displaystring"></a> userentityinstancedata_displaystring

See displaystring Entity [userentityinstancedata_displaystring](displaystring.md#BKMK_userentityinstancedata_displaystring) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_importjob"></a> userentityinstancedata_importjob

See importjob Entity [userentityinstancedata_importjob](importjob.md#BKMK_userentityinstancedata_importjob) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessageprocessingstepimage"></a> userentityinstancedata_sdkmessageprocessingstepimage

See sdkmessageprocessingstepimage Entity [userentityinstancedata_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_userentityinstancedata_sdkmessageprocessingstepimage) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_template"></a> userentityinstancedata_template

See template Entity [userentityinstancedata_template](template.md#BKMK_userentityinstancedata_template) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_userquery"></a> userentityinstancedata_userquery

See userquery Entity [userentityinstancedata_userquery](userquery.md#BKMK_userentityinstancedata_userquery) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_bulkdeletefailure"></a> userentityinstancedata_bulkdeletefailure

See bulkdeletefailure Entity [userentityinstancedata_bulkdeletefailure](bulkdeletefailure.md#BKMK_userentityinstancedata_bulkdeletefailure) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sharepointdocumentlocation"></a> userentityinstancedata_sharepointdocumentlocation

See sharepointdocumentlocation Entity [userentityinstancedata_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_userentityinstancedata_sharepointdocumentlocation) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessageresponse"></a> userentityinstancedata_sdkmessageresponse

See sdkmessageresponse Entity [userentityinstancedata_sdkmessageresponse](sdkmessageresponse.md#BKMK_userentityinstancedata_sdkmessageresponse) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_serviceendpoint"></a> userentityinstancedata_serviceendpoint

See serviceendpoint Entity [userentityinstancedata_serviceendpoint](serviceendpoint.md#BKMK_userentityinstancedata_serviceendpoint) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_reportentity"></a> userentityinstancedata_reportentity

See reportentity Entity [userentityinstancedata_reportentity](reportentity.md#BKMK_userentityinstancedata_reportentity) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_importmap"></a> userentityinstancedata_importmap

See importmap Entity [userentityinstancedata_importmap](importmap.md#BKMK_userentityinstancedata_importmap) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_fax"></a> userentityinstancedata_fax

See fax Entity [userentityinstancedata_fax](fax.md#BKMK_userentityinstancedata_fax) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_privilege"></a> userentityinstancedata_privilege

See privilege Entity [userentityinstancedata_privilege](privilege.md#BKMK_userentityinstancedata_privilege) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_sdkmessagefilter"></a> userentityinstancedata_sdkmessagefilter

See sdkmessagefilter Entity [userentityinstancedata_sdkmessagefilter](sdkmessagefilter.md#BKMK_userentityinstancedata_sdkmessagefilter) One-To-Many relationship.

### <a name="BKMK_userentityinstancedata_reportlink"></a> userentityinstancedata_reportlink

See reportlink Entity [userentityinstancedata_reportlink](reportlink.md#BKMK_userentityinstancedata_reportlink) One-To-Many relationship.
userentityinstancedata

