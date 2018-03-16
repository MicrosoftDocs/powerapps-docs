---
title: "Team Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Team entity."

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
# Team Entity Reference

Collection of system users that routinely collaborate. Teams can be used to simplify record sharing and provide team members with common access to organization data when team members belong to different Business Units.

## Entity Properties

**DisplayName**: Team<br />
**DisplayCollectionName**: Teams<br />
**SchemaName**: Team<br />
**CollectionSchemaName**: Teams<br />
**LogicalName**: team<br />
**LogicalCollectionName**: teams<br />
**EntitySetName**: teams<br />
**PrimaryIdAttribute**: teamid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: BusinessOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdministratorId](#BKMK_AdministratorId)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [Description](#BKMK_Description)
- [EMailAddress](#BKMK_EMailAddress)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ProcessId](#BKMK_ProcessId)
- [QueueId](#BKMK_QueueId)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [StageId](#BKMK_StageId)
- [TeamId](#BKMK_TeamId)
- [TeamTemplateId](#BKMK_TeamTemplateId)
- [TeamType](#BKMK_TeamType)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [YomiName](#BKMK_YomiName)


### <a name="BKMK_AdministratorId"></a> AdministratorId

**Description**: Unique identifier of the user primary responsible for the team.<br />
**DisplayName**: Administrator<br />
**LogicalName**: administratorid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

**Description**: Unique identifier of the business unit with which the team is associated.<br />
**DisplayName**: Business Unit<br />
**LogicalName**: businessunitid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_Description"></a> Description

**Description**: Description of the team.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_EMailAddress"></a> EMailAddress

**Description**: Email address for the team.<br />
**DisplayName**: Email<br />
**LogicalName**: emailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_Name"></a> Name

**Description**: Name of the team.<br />
**DisplayName**: Team Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


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


### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Shows the ID of the process.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_QueueId"></a> QueueId

**Description**: Unique identifier of the default queue for the team.<br />
**DisplayName**: Default Queue<br />
**LogicalName**: queueid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: queue


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Choose the record that the team relates to.<br />
**DisplayName**: Regarding Object Id<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: knowledgearticle


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

**Description**: Type of the associated record for team - used for system managed access teams only.<br />
**DisplayName**: Regarding Object Type<br />
**LogicalName**: regardingobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_StageId"></a> StageId

**Description**: Shows the ID of the stage.<br />
**DisplayName**: Process Stage<br />
**LogicalName**: stageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TeamId"></a> TeamId

**Description**: Unique identifier for the team.<br />
**DisplayName**: Team<br />
**LogicalName**: teamid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TeamTemplateId"></a> TeamTemplateId

**Description**: Shows the team template that is associated with the team.<br />
**DisplayName**: Team Template Identifier<br />
**LogicalName**: teamtemplateid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: teamtemplate


### <a name="BKMK_TeamType"></a> TeamType

**Description**: Select the team type.<br />
**DisplayName**: Team Type<br />
**LogicalName**: teamtype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Owner
- **Value**: 1 **Label**: Access



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the team.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_TraversedPath"></a> TraversedPath

**Description**: For internal use only.<br />
**DisplayName**: Traversed Path<br />
**LogicalName**: traversedpath<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1250


### <a name="BKMK_YomiName"></a> YomiName

**Description**: Pronunciation of the full name of the team, written in phonetic hiragana or katakana characters.<br />
**DisplayName**: Yomi Name<br />
**LogicalName**: yominame<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: PhoneticGuide<br />
**IsLocalizable**: False<br />
**MaxLength**: 160

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [AdministratorIdName](#BKMK_AdministratorIdName)
- [AdministratorIdYomiName](#BKMK_AdministratorIdYomiName)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsDefault](#BKMK_IsDefault)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [QueueIdName](#BKMK_QueueIdName)
- [SystemManaged](#BKMK_SystemManaged)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_AdministratorIdName"></a> AdministratorIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: administratoridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_AdministratorIdYomiName"></a> AdministratorIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: administratoridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businessunitidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the team.<br />
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

**Description**: Date and time when the team was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the team.<br />
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the team with respect to the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_IsDefault"></a> IsDefault

**Description**: Information about whether the team is a default business unit team.<br />
**DisplayName**: Is Default<br />
**LogicalName**: isdefault<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the team.<br />
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

**Description**: Date and time when the team was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the team.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the team.<br />
**DisplayName**: Organization <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_QueueIdName"></a> QueueIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: queueidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_SystemManaged"></a> SystemManaged

**Description**: Select whether the team will be managed by the system.<br />
**DisplayName**: Is System Managed<br />
**LogicalName**: systemmanaged<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the team.<br />
**DisplayName**: Version number<br />
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

- [team_principalobjectattributeaccess_principalid](#BKMK_team_principalobjectattributeaccess_principalid)
- [team_exchangesyncidmapping](#BKMK_team_exchangesyncidmapping)
- [team_interactionforemail](#BKMK_team_interactionforemail)
- [team_knowledgearticle](#BKMK_team_knowledgearticle)
- [team_sharepointsite](#BKMK_team_sharepointsite)
- [team_sharepointdocumentlocation](#BKMK_team_sharepointdocumentlocation)
- [team_goal](#BKMK_team_goal)
- [team_goalrollupquery](#BKMK_team_goalrollupquery)
- [team_mailbox](#BKMK_team_mailbox)
- [team_channelaccessprofile](#BKMK_team_channelaccessprofile)
- [team_externalparty](#BKMK_team_externalparty)
- [team_profilerule](#BKMK_team_profilerule)
- [team_connections2](#BKMK_team_connections2)
- [team_slaBase](#BKMK_team_slaBase)
- [team_goal_goalowner](#BKMK_team_goal_goalowner)
- [team_principalobjectattributeaccess](#BKMK_team_principalobjectattributeaccess)
- [team_routingrule](#BKMK_team_routingrule)
- [OwningTeam_postfollows](#BKMK_OwningTeam_postfollows)
- [team_ImportMaps](#BKMK_team_ImportMaps)
- [team_recurringappointmentmaster](#BKMK_team_recurringappointmentmaster)
- [team_userentityinstancedata](#BKMK_team_userentityinstancedata)
- [team_queueitembase_workerid](#BKMK_team_queueitembase_workerid)
- [team_phonecall](#BKMK_team_phonecall)
- [team_emailserverprofile](#BKMK_team_emailserverprofile)
- [team_connections1](#BKMK_team_connections1)
- [team_actioncardusersettings](#BKMK_team_actioncardusersettings)
- [team_userqueryvisualizations](#BKMK_team_userqueryvisualizations)
- [team_userform](#BKMK_team_userform)
- [team_socialactivity](#BKMK_team_socialactivity)
- [Team_ProcessSessions](#BKMK_Team_ProcessSessions)
- [Team_DuplicateMatchingRecord](#BKMK_Team_DuplicateMatchingRecord)
- [team_userentityuisettings](#BKMK_team_userentityuisettings)
- [team_contacts](#BKMK_team_contacts)
- [Team_AsyncOperations](#BKMK_Team_AsyncOperations)
- [team_ImportLogs](#BKMK_team_ImportLogs)
- [team_workflowlog](#BKMK_team_workflowlog)
- [team_Imports](#BKMK_team_Imports)
- [team_processsession](#BKMK_team_processsession)
- [team_SyncError](#BKMK_team_SyncError)
- [team_letter](#BKMK_team_letter)
- [team_annotations](#BKMK_team_annotations)
- [team_appointment](#BKMK_team_appointment)
- [team_asyncoperation](#BKMK_team_asyncoperation)
- [userentityinstancedata_team](#BKMK_userentityinstancedata_team)
- [Team_BulkDeleteFailures](#BKMK_Team_BulkDeleteFailures)
- [team_customer_relationship](#BKMK_team_customer_relationship)
- [Team_SyncErrors](#BKMK_Team_SyncErrors)
- [team_convertrule](#BKMK_team_convertrule)
- [team_mailboxtrackingfolder](#BKMK_team_mailboxtrackingfolder)
- [team_task](#BKMK_team_task)
- [team_activity](#BKMK_team_activity)
- [Team_DuplicateBaseRecord](#BKMK_Team_DuplicateBaseRecord)
- [team_accounts](#BKMK_team_accounts)
- [team_userquery](#BKMK_team_userquery)
- [team_email](#BKMK_team_email)
- [ImportFile_Team](#BKMK_ImportFile_Team)
- [team_ImportFiles](#BKMK_team_ImportFiles)
- [team_email_templates](#BKMK_team_email_templates)
- [team_fax](#BKMK_team_fax)
- [team_routingruleitem](#BKMK_team_routingruleitem)
- [team_DuplicateRules](#BKMK_team_DuplicateRules)
- [team_workflow](#BKMK_team_workflow)


### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

Same as principalobjectattributeaccess entity [team_principalobjectattributeaccess_principalid](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess_principalid) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: principalid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_principalobjectattributeaccess_principalid<br />
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


### <a name="BKMK_team_exchangesyncidmapping"></a> team_exchangesyncidmapping

Same as exchangesyncidmapping entity [team_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_team_exchangesyncidmapping) Many-To-One relationship.

**ReferencingEntity**: exchangesyncidmapping<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_exchangesyncidmapping<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_team_interactionforemail"></a> team_interactionforemail

Same as interactionforemail entity [team_interactionforemail](interactionforemail.md#BKMK_team_interactionforemail) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_new_interactionforemail<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_team_knowledgearticle"></a> team_knowledgearticle

Same as knowledgearticle entity [team_knowledgearticle](knowledgearticle.md#BKMK_team_knowledgearticle) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_knowledgearticle<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_team_sharepointsite"></a> team_sharepointsite

Same as sharepointsite entity [team_sharepointsite](sharepointsite.md#BKMK_team_sharepointsite) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_sharepointsite<br />
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


### <a name="BKMK_team_sharepointdocumentlocation"></a> team_sharepointdocumentlocation

Same as sharepointdocumentlocation entity [team_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_team_sharepointdocumentlocation) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_sharepointdocumentlocation<br />
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


### <a name="BKMK_team_goal"></a> team_goal

Same as goal entity [team_goal](goal.md#BKMK_team_goal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_goal<br />
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


### <a name="BKMK_team_goalrollupquery"></a> team_goalrollupquery

Same as goalrollupquery entity [team_goalrollupquery](goalrollupquery.md#BKMK_team_goalrollupquery) Many-To-One relationship.

**ReferencingEntity**: goalrollupquery<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_goalrollupquery<br />
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


### <a name="BKMK_team_mailbox"></a> team_mailbox

Same as mailbox entity [team_mailbox](mailbox.md#BKMK_team_mailbox) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_mailbox<br />
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


### <a name="BKMK_team_channelaccessprofile"></a> team_channelaccessprofile

Same as channelaccessprofile entity [team_channelaccessprofile](channelaccessprofile.md#BKMK_team_channelaccessprofile) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_channelaccessprofile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_team_externalparty"></a> team_externalparty

Same as externalparty entity [team_externalparty](externalparty.md#BKMK_team_externalparty) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_externalparty<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_team_profilerule"></a> team_profilerule

Same as channelaccessprofilerule entity [team_profilerule](channelaccessprofilerule.md#BKMK_team_profilerule) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_profilerule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_team_connections2"></a> team_connections2

Same as connection entity [team_connections2](connection.md#BKMK_team_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_connections2<br />
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


### <a name="BKMK_team_slaBase"></a> team_slaBase

Same as sla entity [team_slaBase](sla.md#BKMK_team_slaBase) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_slaBase<br />
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


### <a name="BKMK_team_goal_goalowner"></a> team_goal_goalowner

Same as goal entity [team_goal_goalowner](goal.md#BKMK_team_goal_goalowner) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: goalownerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_goal_goalowner<br />
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


### <a name="BKMK_team_principalobjectattributeaccess"></a> team_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [team_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_principalobjectattributeaccess<br />
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


### <a name="BKMK_team_routingrule"></a> team_routingrule

Same as routingrule entity [team_routingrule](routingrule.md#BKMK_team_routingrule) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_routingrule<br />
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


### <a name="BKMK_OwningTeam_postfollows"></a> OwningTeam_postfollows

Same as postfollow entity [OwningTeam_postfollows](postfollow.md#BKMK_OwningTeam_postfollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: OwningTeam_postfollows<br />
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


### <a name="BKMK_team_ImportMaps"></a> team_ImportMaps

Same as importmap entity [team_ImportMaps](importmap.md#BKMK_team_ImportMaps) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_ImportMaps<br />
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


### <a name="BKMK_team_recurringappointmentmaster"></a> team_recurringappointmentmaster

Same as recurringappointmentmaster entity [team_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_team_recurringappointmentmaster) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_recurringappointmentmaster<br />
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


### <a name="BKMK_team_userentityinstancedata"></a> team_userentityinstancedata

Same as userentityinstancedata entity [team_userentityinstancedata](userentityinstancedata.md#BKMK_team_userentityinstancedata) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_userentityinstancedata<br />
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


### <a name="BKMK_team_queueitembase_workerid"></a> team_queueitembase_workerid

Same as queueitem entity [team_queueitembase_workerid](queueitem.md#BKMK_team_queueitembase_workerid) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: workerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_queueitembase_workerid<br />
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


### <a name="BKMK_team_phonecall"></a> team_phonecall

Same as phonecall entity [team_phonecall](phonecall.md#BKMK_team_phonecall) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_phonecall<br />
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


### <a name="BKMK_team_emailserverprofile"></a> team_emailserverprofile

Same as emailserverprofile entity [team_emailserverprofile](emailserverprofile.md#BKMK_team_emailserverprofile) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_emailserverprofile<br />
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


### <a name="BKMK_team_connections1"></a> team_connections1

Same as connection entity [team_connections1](connection.md#BKMK_team_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_connections1<br />
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


### <a name="BKMK_team_actioncardusersettings"></a> team_actioncardusersettings

Same as actioncardusersettings entity [team_actioncardusersettings](actioncardusersettings.md#BKMK_team_actioncardusersettings) Many-To-One relationship.

**ReferencingEntity**: actioncardusersettings<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_actioncardusersettings<br />
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


### <a name="BKMK_team_userqueryvisualizations"></a> team_userqueryvisualizations

Same as userqueryvisualization entity [team_userqueryvisualizations](userqueryvisualization.md#BKMK_team_userqueryvisualizations) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_userqueryvisualizations<br />
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


### <a name="BKMK_team_userform"></a> team_userform

Same as userform entity [team_userform](userform.md#BKMK_team_userform) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_userform<br />
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


### <a name="BKMK_team_socialactivity"></a> team_socialactivity

Same as socialactivity entity [team_socialactivity](socialactivity.md#BKMK_team_socialactivity) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_socialactivity<br />
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


### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

Same as processsession entity [Team_ProcessSessions](processsession.md#BKMK_Team_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Team_ProcessSessions<br />
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


### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

Same as duplicaterecord entity [Team_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Team_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Team_DuplicateMatchingRecord<br />
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


### <a name="BKMK_team_userentityuisettings"></a> team_userentityuisettings

Same as userentityuisettings entity [team_userentityuisettings](userentityuisettings.md#BKMK_team_userentityuisettings) Many-To-One relationship.

**ReferencingEntity**: userentityuisettings<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_userentityuisettings<br />
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


### <a name="BKMK_team_contacts"></a> team_contacts

Same as contact entity [team_contacts](contact.md#BKMK_team_contacts) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_contacts<br />
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


### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

Same as asyncoperation entity [Team_AsyncOperations](asyncoperation.md#BKMK_Team_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Team_AsyncOperations<br />
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


### <a name="BKMK_team_ImportLogs"></a> team_ImportLogs

Same as importlog entity [team_ImportLogs](importlog.md#BKMK_team_ImportLogs) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_ImportLogs<br />
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


### <a name="BKMK_team_workflowlog"></a> team_workflowlog

Same as workflowlog entity [team_workflowlog](workflowlog.md#BKMK_team_workflowlog) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_workflowlog<br />
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


### <a name="BKMK_team_Imports"></a> team_Imports

Same as import entity [team_Imports](import.md#BKMK_team_Imports) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_Imports<br />
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


### <a name="BKMK_team_processsession"></a> team_processsession

Same as processsession entity [team_processsession](processsession.md#BKMK_team_processsession) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_processsession<br />
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


### <a name="BKMK_team_SyncError"></a> team_SyncError

Same as syncerror entity [team_SyncError](syncerror.md#BKMK_team_SyncError) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_SyncError<br />
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


### <a name="BKMK_team_letter"></a> team_letter

Same as letter entity [team_letter](letter.md#BKMK_team_letter) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_letter<br />
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


### <a name="BKMK_team_annotations"></a> team_annotations

Same as annotation entity [team_annotations](annotation.md#BKMK_team_annotations) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_annotations<br />
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


### <a name="BKMK_team_appointment"></a> team_appointment

Same as appointment entity [team_appointment](appointment.md#BKMK_team_appointment) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_appointment<br />
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


### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

Same as asyncoperation entity [team_asyncoperation](asyncoperation.md#BKMK_team_asyncoperation) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_asyncoperation<br />
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


### <a name="BKMK_userentityinstancedata_team"></a> userentityinstancedata_team

Same as userentityinstancedata entity [userentityinstancedata_team](userentityinstancedata.md#BKMK_userentityinstancedata_team) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_team<br />
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


### <a name="BKMK_Team_BulkDeleteFailures"></a> Team_BulkDeleteFailures

Same as bulkdeletefailure entity [Team_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Team_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Team_BulkDeleteFailures<br />
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


### <a name="BKMK_team_customer_relationship"></a> team_customer_relationship

Same as customerrelationship entity [team_customer_relationship](customerrelationship.md#BKMK_team_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_customer_relationship<br />
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


### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

Same as syncerror entity [Team_SyncErrors](syncerror.md#BKMK_Team_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Team_SyncErrors<br />
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


### <a name="BKMK_team_convertrule"></a> team_convertrule

Same as convertrule entity [team_convertrule](convertrule.md#BKMK_team_convertrule) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_convertrule<br />
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


### <a name="BKMK_team_mailboxtrackingfolder"></a> team_mailboxtrackingfolder

Same as mailboxtrackingfolder entity [team_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_team_mailboxtrackingfolder) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_mailboxtrackingfolder<br />
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


### <a name="BKMK_team_task"></a> team_task

Same as task entity [team_task](task.md#BKMK_team_task) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_task<br />
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


### <a name="BKMK_team_activity"></a> team_activity

Same as activitypointer entity [team_activity](activitypointer.md#BKMK_team_activity) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_activity<br />
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


### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

Same as duplicaterecord entity [Team_DuplicateBaseRecord](duplicaterecord.md#BKMK_Team_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Team_DuplicateBaseRecord<br />
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


### <a name="BKMK_team_accounts"></a> team_accounts

Same as account entity [team_accounts](account.md#BKMK_team_accounts) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_accounts<br />
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


### <a name="BKMK_team_userquery"></a> team_userquery

Same as userquery entity [team_userquery](userquery.md#BKMK_team_userquery) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_userquery<br />
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


### <a name="BKMK_team_email"></a> team_email

Same as email entity [team_email](email.md#BKMK_team_email) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_email<br />
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


### <a name="BKMK_ImportFile_Team"></a> ImportFile_Team

Same as importfile entity [ImportFile_Team](importfile.md#BKMK_ImportFile_Team) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: recordsownerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportFile_Team<br />
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


### <a name="BKMK_team_ImportFiles"></a> team_ImportFiles

Same as importfile entity [team_ImportFiles](importfile.md#BKMK_team_ImportFiles) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_ImportFiles<br />
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


### <a name="BKMK_team_email_templates"></a> team_email_templates

Same as template entity [team_email_templates](template.md#BKMK_team_email_templates) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_email_templates<br />
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


### <a name="BKMK_team_fax"></a> team_fax

Same as fax entity [team_fax](fax.md#BKMK_team_fax) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: team_fax<br />
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


### <a name="BKMK_team_routingruleitem"></a> team_routingruleitem

Same as routingruleitem entity [team_routingruleitem](routingruleitem.md#BKMK_team_routingruleitem) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: assignobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_routingruleitem<br />
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


### <a name="BKMK_team_DuplicateRules"></a> team_DuplicateRules

Same as duplicaterule entity [team_DuplicateRules](duplicaterule.md#BKMK_team_DuplicateRules) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_DuplicateRules<br />
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


### <a name="BKMK_team_workflow"></a> team_workflow

Same as workflow entity [team_workflow](workflow.md#BKMK_team_workflow) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: owningteam<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: team_workflow<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [knowledgearticle_Teams](#BKMK_knowledgearticle_Teams)
- [teamtemplate_Teams](#BKMK_teamtemplate_Teams)
- [lk_teambase_administratorid](#BKMK_lk_teambase_administratorid)
- [processstage_teams](#BKMK_processstage_teams)
- [lk_teambase_modifiedby](#BKMK_lk_teambase_modifiedby)
- [lk_teambase_createdby](#BKMK_lk_teambase_createdby)
- [queue_team](#BKMK_queue_team)
- [TransactionCurrency_Team](#BKMK_TransactionCurrency_Team)
- [business_unit_teams](#BKMK_business_unit_teams)
- [organization_teams](#BKMK_organization_teams)
- [lk_team_modifiedonbehalfby](#BKMK_lk_team_modifiedonbehalfby)
- [lk_team_createdonbehalfby](#BKMK_lk_team_createdonbehalfby)


### <a name="BKMK_knowledgearticle_Teams"></a> knowledgearticle_Teams

See knowledgearticle Entity [knowledgearticle_Teams](knowledgearticle.md#BKMK_knowledgearticle_Teams) One-To-Many relationship.

### <a name="BKMK_teamtemplate_Teams"></a> teamtemplate_Teams

See teamtemplate Entity [teamtemplate_Teams](teamtemplate.md#BKMK_teamtemplate_Teams) One-To-Many relationship.

### <a name="BKMK_lk_teambase_administratorid"></a> lk_teambase_administratorid

See systemuser Entity [lk_teambase_administratorid](systemuser.md#BKMK_lk_teambase_administratorid) One-To-Many relationship.

### <a name="BKMK_processstage_teams"></a> processstage_teams

See processstage Entity [processstage_teams](processstage.md#BKMK_processstage_teams) One-To-Many relationship.

### <a name="BKMK_lk_teambase_modifiedby"></a> lk_teambase_modifiedby

See systemuser Entity [lk_teambase_modifiedby](systemuser.md#BKMK_lk_teambase_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_teambase_createdby"></a> lk_teambase_createdby

See systemuser Entity [lk_teambase_createdby](systemuser.md#BKMK_lk_teambase_createdby) One-To-Many relationship.

### <a name="BKMK_queue_team"></a> queue_team

See queue Entity [queue_team](queue.md#BKMK_queue_team) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Team"></a> TransactionCurrency_Team

See transactioncurrency Entity [TransactionCurrency_Team](transactioncurrency.md#BKMK_TransactionCurrency_Team) One-To-Many relationship.

### <a name="BKMK_business_unit_teams"></a> business_unit_teams

See businessunit Entity [business_unit_teams](businessunit.md#BKMK_business_unit_teams) One-To-Many relationship.

### <a name="BKMK_organization_teams"></a> organization_teams

See organization Entity [organization_teams](organization.md#BKMK_organization_teams) One-To-Many relationship.

### <a name="BKMK_lk_team_modifiedonbehalfby"></a> lk_team_modifiedonbehalfby

See systemuser Entity [lk_team_modifiedonbehalfby](systemuser.md#BKMK_lk_team_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_team_createdonbehalfby"></a> lk_team_createdonbehalfby

See systemuser Entity [lk_team_createdonbehalfby](systemuser.md#BKMK_lk_team_createdonbehalfby) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Team entity is the first entity in the relationship. Listed by **SchemaName**.

- [teamroles_association](#BKMK_teamroles_association)
- [teammembership_association](#BKMK_teammembership_association)
- [teamprofiles_association](#BKMK_teamprofiles_association)


### <a name="BKMK_teamroles_association"></a> teamroles_association

**IntersectEntityName**: teamroles<br />
**Entity1LogicalName**: team<br />

- **Entity1IntersectAttribute**: teamid
- **Entity1NavigationPropertyName**: teamroles_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [role](role.md)<br />

- **Entity2IntersectAttribute**: roleid
- **Entity2NavigationPropertyName**: teamroles_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />

### <a name="BKMK_teammembership_association"></a> teammembership_association

**IntersectEntityName**: teammembership<br />
**Entity1LogicalName**: team<br />

- **Entity1IntersectAttribute**: teamid
- **Entity1NavigationPropertyName**: teammembership_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [systemuser](systemuser.md)<br />

- **Entity2IntersectAttribute**: systemuserid
- **Entity2NavigationPropertyName**: teammembership_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />

### <a name="BKMK_teamprofiles_association"></a> teamprofiles_association

**IntersectEntityName**: teamprofiles<br />
**Entity1LogicalName**: team<br />

- **Entity1IntersectAttribute**: teamid
- **Entity1NavigationPropertyName**: teamprofiles_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: UseCollectionName
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [fieldsecurityprofile](fieldsecurityprofile.md)<br />

- **Entity2IntersectAttribute**: fieldsecurityprofileid
- **Entity2NavigationPropertyName**: teamprofiles_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: UseCollectionName
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />
team

