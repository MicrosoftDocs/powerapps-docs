---
title: "Team Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Team entity."
ms.date: 09/16/2020
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
# Team Entity Reference

Collection of system users that routinely collaborate. Teams can be used to simplify record sharing and provide team members with common access to organization data when team members belong to different Business Units.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|AddMembersTeam|<xref href="Microsoft.Dynamics.CRM.AddMembersTeam?text=AddMembersTeam Action" />|<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest>|
|ConvertOwnerTeamToAccessTeam|<xref href="Microsoft.Dynamics.CRM.ConvertOwnerTeamToAccessTeam?text=ConvertOwnerTeamToAccessTeam Action" />|<xref:Microsoft.Crm.Sdk.Messages.ConvertOwnerTeamToAccessTeamRequest>|
|Create|POST [*org URI*]/api/data/v9.0/teams<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/teams(*teamid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|RemoveMembersTeam|<xref href="Microsoft.Dynamics.CRM.RemoveMembersTeam?text=RemoveMembersTeam Action" />|<xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/teams(*teamid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/teams<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetParentBusinessUnit|[Associate and disassociate entities](/powerapps/developer/common-data-service/webapi/associate-disassociate-entities-using-web-api)|<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|
|SetParentSystemUser|<xref href="Microsoft.Dynamics.CRM.SetParentSystemUser?text=SetParentSystemUser Action" />|<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|
|SetParentTeam|[Associate and disassociate entities](/powerapps/developer/common-data-service/webapi/associate-disassociate-entities-using-web-api)|<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/teams(*teamid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Teams|
|DisplayCollectionName|Teams|
|DisplayName|Team|
|EntitySetName|teams|
|IsBPFEntity|False|
|LogicalCollectionName|teams|
|LogicalName|team|
|OwnershipType|BusinessOwned|
|PrimaryIdAttribute|teamid|
|PrimaryNameAttribute|name|
|SchemaName|Team|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdministratorId](#BKMK_AdministratorId)
- [AzureActiveDirectoryObjectId](#BKMK_AzureActiveDirectoryObjectId)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [Description](#BKMK_Description)
- [EMailAddress](#BKMK_EMailAddress)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [MembershipType](#BKMK_MembershipType)
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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user primary responsible for the team.|
|DisplayName|Administrator|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|administratorid|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_AzureActiveDirectoryObjectId"></a> AzureActiveDirectoryObjectId

|Property|Value|
|--------|-----|
|Description|The Azure active directory object Id for a group.|
|DisplayName|Azure AD Object Id for a group|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|azureactivedirectoryobjectid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit with which the team is associated.|
|DisplayName|Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitid|
|RequiredLevel|SystemRequired|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the team.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|2000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|--------|-----|
|Description|Email address for the team.|
|DisplayName|Email|
|FormatName|Email|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|emailaddress|
|MaxLength|100|
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


### <a name="BKMK_MembershipType"></a> MembershipType

|Property|Value|
|--------|-----|
|Description|Information about team membership type.|
|DisplayName|Team Membership Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|membershiptype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### MembershipType Options

|Value|Label|
|-----|-----|
|0|Members and guests|
|1|Members|
|2|Owners|
|3|Guests|



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the team.|
|DisplayName|Team Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|160|
|RequiredLevel|SystemRequired|
|Type|String|


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


### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_QueueId"></a> QueueId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the default queue for the team.|
|DisplayName|Default Queue|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|queueid|
|RequiredLevel|None|
|Targets|queue|
|Type|Lookup|


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|--------|-----|
|Description|Choose the record that the team relates to.|
|DisplayName|Regarding Object Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjectid|
|RequiredLevel|None|
|Targets|knowledgearticle,opportunity|
|Type|Lookup|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description|Type of the associated record for team - used for system managed access teams only.|
|DisplayName|Regarding Object Type|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|--------|-----|
|Description|Shows the ID of the stage.|
|DisplayName|(Deprecated) Process Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|stageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_TeamId"></a> TeamId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team.|
|DisplayName|Team|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|teamid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_TeamTemplateId"></a> TeamTemplateId

|Property|Value|
|--------|-----|
|Description|Shows the team template that is associated with the team.|
|DisplayName|Team Template Identifier|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|teamtemplateid|
|RequiredLevel|None|
|Targets|teamtemplate|
|Type|Lookup|


### <a name="BKMK_TeamType"></a> TeamType

|Property|Value|
|--------|-----|
|Description|Select the team type.|
|DisplayName|Team Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|teamtype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### TeamType Options

|Value|Label|
|-----|-----|
|0|Owner|
|1|Access|
|2|AAD Security Group|
|3|AAD Office Group|



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the currency associated with the team.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|(Deprecated) Traversed Path|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|traversedpath|
|MaxLength|1250|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_YomiName"></a> YomiName

|Property|Value|
|--------|-----|
|Description|Pronunciation of the full name of the team, written in phonetic hiragana or katakana characters.|
|DisplayName|Yomi Name|
|FormatName|PhoneticGuide|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|yominame|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|

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

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|administratoridname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_AdministratorIdYomiName"></a> AdministratorIdYomiName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|administratoridyominame|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|businessunitidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the team.|
|DisplayName|Created By|
|IsValidForForm|True|
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
|Description|Date and time when the team was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the team.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|Exchange rate for the currency associated with the team with respect to the base currency.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.0000000001|
|Precision|10|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_IsDefault"></a> IsDefault

|Property|Value|
|--------|-----|
|Description|Information about whether the team is a default business unit team.|
|DisplayName|Is Default|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|isdefault|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsDefault Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the team.|
|DisplayName|Modified By|
|IsValidForForm|True|
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
|Description|Date and time when the team was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the team.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the organization associated with the team.|
|DisplayName|Organization |
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_QueueIdName"></a> QueueIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|queueidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SystemManaged"></a> SystemManaged

|Property|Value|
|--------|-----|
|Description|Select whether the team will be managed by the system.|
|DisplayName|Is System Managed|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|systemmanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### SystemManaged Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|Version number of the team.|
|DisplayName|Version number|
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

- [team_principalobjectattributeaccess_principalid](#BKMK_team_principalobjectattributeaccess_principalid)
- [team_exchangesyncidmapping](#BKMK_team_exchangesyncidmapping)
- [team_interactionforemail](#BKMK_team_interactionforemail)
- [team_knowledgearticle](#BKMK_team_knowledgearticle)
- [team_sharepointsite](#BKMK_team_sharepointsite)
- [team_sharepointdocumentlocation](#BKMK_team_sharepointdocumentlocation)
- [team_goal](#BKMK_team_goal)
- [team_goalrollupquery](#BKMK_team_goalrollupquery)
- [team_mailbox](#BKMK_team_mailbox)
- [team_connections2](#BKMK_team_connections2)
- [team_slaBase](#BKMK_team_slaBase)
- [team_goal_goalowner](#BKMK_team_goal_goalowner)
- [team_principalobjectattributeaccess](#BKMK_team_principalobjectattributeaccess)
- [OwningTeam_postfollows](#BKMK_OwningTeam_postfollows)
- [team_ImportMaps](#BKMK_team_ImportMaps)
- [team_recurringappointmentmaster](#BKMK_team_recurringappointmentmaster)
- [team_queueitembase_workerid](#BKMK_team_queueitembase_workerid)
- [team_phonecall](#BKMK_team_phonecall)
- [team_emailserverprofile](#BKMK_team_emailserverprofile)
- [team_connections1](#BKMK_team_connections1)
- [team_userqueryvisualizations](#BKMK_team_userqueryvisualizations)
- [team_userform](#BKMK_team_userform)
- [team_socialactivity](#BKMK_team_socialactivity)
- [Team_ProcessSessions](#BKMK_Team_ProcessSessions)
- [Team_DuplicateMatchingRecord](#BKMK_Team_DuplicateMatchingRecord)
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
- [Team_BulkDeleteFailures](#BKMK_Team_BulkDeleteFailures)
- [Team_SyncErrors](#BKMK_Team_SyncErrors)
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
- [team_DuplicateRules](#BKMK_team_DuplicateRules)
- [team_workflow](#BKMK_team_workflow)
- [team_stagesolutionupload](#BKMK_team_stagesolutionupload)
- [team_msdyn_knowledgearticleimage](#BKMK_team_msdyn_knowledgearticleimage)
- [team_msdyn_knowledgearticletemplate](#BKMK_team_msdyn_knowledgearticletemplate)
- [team_msdyn_dataflow](#BKMK_team_msdyn_dataflow)
- [team_connector](#BKMK_team_connector)
- [team_msdyn_aiconfiguration](#BKMK_team_msdyn_aiconfiguration)
- [team_msdyn_aimodel](#BKMK_team_msdyn_aimodel)
- [team_msdyn_aitemplate](#BKMK_team_msdyn_aitemplate)
- [team_msdyn_aibdataset](#BKMK_team_msdyn_aibdataset)
- [team_msdyn_aibdatasetfile](#BKMK_team_msdyn_aibdatasetfile)
- [team_msdyn_aibdatasetrecord](#BKMK_team_msdyn_aibdatasetrecord)
- [team_msdyn_aibdatasetscontainer](#BKMK_team_msdyn_aibdatasetscontainer)
- [team_msdyn_aibfile](#BKMK_team_msdyn_aibfile)
- [team_msdyn_aibfileattacheddata](#BKMK_team_msdyn_aibfileattacheddata)
- [team_msdyn_aifptrainingdocument](#BKMK_team_msdyn_aifptrainingdocument)
- [team_msdyn_aiodimage](#BKMK_team_msdyn_aiodimage)
- [team_msdyn_aiodlabel](#BKMK_team_msdyn_aiodlabel)
- [team_msdyn_aiodtrainingboundingbox](#BKMK_team_msdyn_aiodtrainingboundingbox)
- [team_msdyn_aiodtrainingimage](#BKMK_team_msdyn_aiodtrainingimage)
- [team_environmentvariabledefinition](#BKMK_team_environmentvariabledefinition)
- [team_environmentvariablevalue](#BKMK_team_environmentvariablevalue)
- [team_processstageparameter](#BKMK_team_processstageparameter)
- [team_flowsession](#BKMK_team_flowsession)
- [team_workflowbinary](#BKMK_team_workflowbinary)
- [team_connectionreference](#BKMK_team_connectionreference)
- [team_msdyn_analysiscomponent](#BKMK_team_msdyn_analysiscomponent)
- [team_msdyn_analysisjob](#BKMK_team_msdyn_analysisjob)
- [team_msdyn_analysisresult](#BKMK_team_msdyn_analysisresult)
- [team_msdyn_analysisresultdetail](#BKMK_team_msdyn_analysisresultdetail)
- [team_msdyn_solutionhealthrule](#BKMK_team_msdyn_solutionhealthrule)
- [team_msdyn_solutionhealthruleargument](#BKMK_team_msdyn_solutionhealthruleargument)


### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

Same as principalobjectattributeaccess entity [team_principalobjectattributeaccess_principalid](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess_principalid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|principalid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_principalobjectattributeaccess_principalid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_exchangesyncidmapping"></a> team_exchangesyncidmapping

Same as exchangesyncidmapping entity [team_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_team_exchangesyncidmapping) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|exchangesyncidmapping|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_exchangesyncidmapping|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_interactionforemail"></a> team_interactionforemail

Same as interactionforemail entity [team_interactionforemail](interactionforemail.md#BKMK_team_interactionforemail) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|interactionforemail|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_new_interactionforemail|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_knowledgearticle"></a> team_knowledgearticle

Same as knowledgearticle entity [team_knowledgearticle](knowledgearticle.md#BKMK_team_knowledgearticle) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|knowledgearticle|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_knowledgearticle|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_sharepointsite"></a> team_sharepointsite

Same as sharepointsite entity [team_sharepointsite](sharepointsite.md#BKMK_team_sharepointsite) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointsite|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_sharepointsite|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_sharepointdocumentlocation"></a> team_sharepointdocumentlocation

Same as sharepointdocumentlocation entity [team_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_team_sharepointdocumentlocation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_sharepointdocumentlocation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_goal"></a> team_goal

Same as goal entity [team_goal](goal.md#BKMK_team_goal) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_goal|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_goalrollupquery"></a> team_goalrollupquery

Same as goalrollupquery entity [team_goalrollupquery](goalrollupquery.md#BKMK_team_goalrollupquery) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goalrollupquery|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_goalrollupquery|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_mailbox"></a> team_mailbox

Same as mailbox entity [team_mailbox](mailbox.md#BKMK_team_mailbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailbox|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_mailbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connections2"></a> team_connections2

Same as connection entity [team_connections2](connection.md#BKMK_team_connections2) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record2id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_connections2|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_slaBase"></a> team_slaBase

Same as sla entity [team_slaBase](sla.md#BKMK_team_slaBase) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_slaBase|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_goal_goalowner"></a> team_goal_goalowner

Same as goal entity [team_goal_goalowner](goal.md#BKMK_team_goal_goalowner) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|goal|
|ReferencingAttribute|goalownerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_goal_goalowner|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_principalobjectattributeaccess"></a> team_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [team_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_principalobjectattributeaccess|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_OwningTeam_postfollows"></a> OwningTeam_postfollows

Same as postfollow entity [OwningTeam_postfollows](postfollow.md#BKMK_OwningTeam_postfollows) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|postfollow|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|OwningTeam_postfollows|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_ImportMaps"></a> team_ImportMaps

Same as importmap entity [team_ImportMaps](importmap.md#BKMK_team_ImportMaps) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importmap|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_ImportMaps|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_recurringappointmentmaster"></a> team_recurringappointmentmaster

Same as recurringappointmentmaster entity [team_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_team_recurringappointmentmaster) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|recurringappointmentmaster|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_recurringappointmentmaster|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_queueitembase_workerid"></a> team_queueitembase_workerid

Same as queueitem entity [team_queueitembase_workerid](queueitem.md#BKMK_team_queueitembase_workerid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|workerid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_queueitembase_workerid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_phonecall"></a> team_phonecall

Same as phonecall entity [team_phonecall](phonecall.md#BKMK_team_phonecall) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|phonecall|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_phonecall|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_emailserverprofile"></a> team_emailserverprofile

Same as emailserverprofile entity [team_emailserverprofile](emailserverprofile.md#BKMK_team_emailserverprofile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|emailserverprofile|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_emailserverprofile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connections1"></a> team_connections1

Same as connection entity [team_connections1](connection.md#BKMK_team_connections1) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connection|
|ReferencingAttribute|record1id|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_connections1|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 100|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_userqueryvisualizations"></a> team_userqueryvisualizations

Same as userqueryvisualization entity [team_userqueryvisualizations](userqueryvisualization.md#BKMK_team_userqueryvisualizations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userqueryvisualization|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_userqueryvisualizations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_userform"></a> team_userform

Same as userform entity [team_userform](userform.md#BKMK_team_userform) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userform|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_userform|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_socialactivity"></a> team_socialactivity

Same as socialactivity entity [team_socialactivity](socialactivity.md#BKMK_team_socialactivity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|socialactivity|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_socialactivity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Team_ProcessSessions"></a> Team_ProcessSessions

Same as processsession entity [Team_ProcessSessions](processsession.md#BKMK_Team_ProcessSessions) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Team_ProcessSessions|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 110|
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Team_DuplicateMatchingRecord"></a> Team_DuplicateMatchingRecord

Same as duplicaterecord entity [Team_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Team_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Team_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_contacts"></a> team_contacts

Same as contact entity [team_contacts](contact.md#BKMK_team_contacts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|contact|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_contacts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Team_AsyncOperations"></a> Team_AsyncOperations

Same as asyncoperation entity [Team_AsyncOperations](asyncoperation.md#BKMK_Team_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Team_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_ImportLogs"></a> team_ImportLogs

Same as importlog entity [team_ImportLogs](importlog.md#BKMK_team_ImportLogs) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importlog|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_ImportLogs|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_workflowlog"></a> team_workflowlog

Same as workflowlog entity [team_workflowlog](workflowlog.md#BKMK_team_workflowlog) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowlog|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_workflowlog|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_Imports"></a> team_Imports

Same as import entity [team_Imports](import.md#BKMK_team_Imports) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|import|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_Imports|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_processsession"></a> team_processsession

Same as processsession entity [team_processsession](processsession.md#BKMK_team_processsession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_processsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_SyncError"></a> team_SyncError

Same as syncerror entity [team_SyncError](syncerror.md#BKMK_team_SyncError) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_SyncError|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_letter"></a> team_letter

Same as letter entity [team_letter](letter.md#BKMK_team_letter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|letter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_letter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_annotations"></a> team_annotations

Same as annotation entity [team_annotations](annotation.md#BKMK_team_annotations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_annotations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_appointment"></a> team_appointment

Same as appointment entity [team_appointment](appointment.md#BKMK_team_appointment) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|appointment|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_appointment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_asyncoperation"></a> team_asyncoperation

Same as asyncoperation entity [team_asyncoperation](asyncoperation.md#BKMK_team_asyncoperation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_asyncoperation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Team_BulkDeleteFailures"></a> Team_BulkDeleteFailures

Same as bulkdeletefailure entity [Team_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Team_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Team_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Team_SyncErrors"></a> Team_SyncErrors

Same as syncerror entity [Team_SyncErrors](syncerror.md#BKMK_Team_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Team_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_team_mailboxtrackingfolder"></a> team_mailboxtrackingfolder

Same as mailboxtrackingfolder entity [team_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_team_mailboxtrackingfolder) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_mailboxtrackingfolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_task"></a> team_task

Same as task entity [team_task](task.md#BKMK_team_task) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|task|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_task|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_activity"></a> team_activity

Same as activitypointer entity [team_activity](activitypointer.md#BKMK_team_activity) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|activitypointer|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_activity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Team_DuplicateBaseRecord"></a> Team_DuplicateBaseRecord

Same as duplicaterecord entity [Team_DuplicateBaseRecord](duplicaterecord.md#BKMK_Team_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|Team_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_accounts"></a> team_accounts

Same as account entity [team_accounts](account.md#BKMK_team_accounts) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|account|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_accounts|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_userquery"></a> team_userquery

Same as userquery entity [team_userquery](userquery.md#BKMK_team_userquery) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|userquery|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_userquery|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_email"></a> team_email

Same as email entity [team_email](email.md#BKMK_team_email) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|email|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_email|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_ImportFile_Team"></a> ImportFile_Team

Same as importfile entity [ImportFile_Team](importfile.md#BKMK_ImportFile_Team) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|recordsownerid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|ImportFile_Team|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_ImportFiles"></a> team_ImportFiles

Same as importfile entity [team_ImportFiles](importfile.md#BKMK_team_ImportFiles) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|importfile|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_ImportFiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_email_templates"></a> team_email_templates

Same as template entity [team_email_templates](template.md#BKMK_team_email_templates) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|template|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_email_templates|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_fax"></a> team_fax

Same as fax entity [team_fax](fax.md#BKMK_team_fax) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|fax|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_fax|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_DuplicateRules"></a> team_DuplicateRules

Same as duplicaterule entity [team_DuplicateRules](duplicaterule.md#BKMK_team_DuplicateRules) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterule|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_DuplicateRules|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_workflow"></a> team_workflow

Same as workflow entity [team_workflow](workflow.md#BKMK_team_workflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_workflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_stagesolutionupload"></a> team_stagesolutionupload

**Added by**: Active Solution Solution

Same as stagesolutionupload entity [team_stagesolutionupload](stagesolutionupload.md#BKMK_team_stagesolutionupload) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_stagesolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgearticleimage"></a> team_msdyn_knowledgearticleimage

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticleimage entity [team_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_team_msdyn_knowledgearticleimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgearticleimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgearticletemplate"></a> team_msdyn_knowledgearticletemplate

**Added by**: Active Solution Solution

Same as msdyn_knowledgearticletemplate entity [team_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_team_msdyn_knowledgearticletemplate) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgearticletemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dataflow"></a> team_msdyn_dataflow

**Added by**: Active Solution Solution

Same as msdyn_dataflow entity [team_msdyn_dataflow](msdyn_dataflow.md#BKMK_team_msdyn_dataflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dataflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connector"></a> team_connector

**Added by**: Active Solution Solution

Same as connector entity [team_connector](connector.md#BKMK_team_connector) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_connector|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aiconfiguration"></a> team_msdyn_aiconfiguration

**Added by**: Active Solution Solution

Same as msdyn_aiconfiguration entity [team_msdyn_aiconfiguration](msdyn_aiconfiguration.md#BKMK_team_msdyn_aiconfiguration) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aiconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aimodel"></a> team_msdyn_aimodel

**Added by**: Active Solution Solution

Same as msdyn_aimodel entity [team_msdyn_aimodel](msdyn_aimodel.md#BKMK_team_msdyn_aimodel) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aimodel|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aimodel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aitemplate"></a> team_msdyn_aitemplate

**Added by**: Active Solution Solution

Same as msdyn_aitemplate entity [team_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_team_msdyn_aitemplate) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aitemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibdataset"></a> team_msdyn_aibdataset

**Added by**: Active Solution Solution

Same as msdyn_aibdataset entity [team_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_team_msdyn_aibdataset) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdataset|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibdataset|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibdatasetfile"></a> team_msdyn_aibdatasetfile

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetfile entity [team_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_team_msdyn_aibdatasetfile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetfile|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibdatasetfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibdatasetrecord"></a> team_msdyn_aibdatasetrecord

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetrecord entity [team_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_team_msdyn_aibdatasetrecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetrecord|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibdatasetrecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibdatasetscontainer"></a> team_msdyn_aibdatasetscontainer

**Added by**: Active Solution Solution

Same as msdyn_aibdatasetscontainer entity [team_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_team_msdyn_aibdatasetscontainer) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibdatasetscontainer|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibdatasetscontainer|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibfile"></a> team_msdyn_aibfile

**Added by**: Active Solution Solution

Same as msdyn_aibfile entity [team_msdyn_aibfile](msdyn_aibfile.md#BKMK_team_msdyn_aibfile) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfile|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibfileattacheddata"></a> team_msdyn_aibfileattacheddata

**Added by**: Active Solution Solution

Same as msdyn_aibfileattacheddata entity [team_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_team_msdyn_aibfileattacheddata) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibfileattacheddata|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aifptrainingdocument"></a> team_msdyn_aifptrainingdocument

**Added by**: Active Solution Solution

Same as msdyn_aifptrainingdocument entity [team_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_team_msdyn_aifptrainingdocument) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aifptrainingdocument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aiodimage"></a> team_msdyn_aiodimage

**Added by**: Active Solution Solution

Same as msdyn_aiodimage entity [team_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_team_msdyn_aiodimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodimage|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aiodimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aiodlabel"></a> team_msdyn_aiodlabel

**Added by**: Active Solution Solution

Same as msdyn_aiodlabel entity [team_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_team_msdyn_aiodlabel) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodlabel|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aiodlabel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aiodtrainingboundingbox"></a> team_msdyn_aiodtrainingboundingbox

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingboundingbox entity [team_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_team_msdyn_aiodtrainingboundingbox) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingboundingbox|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aiodtrainingboundingbox|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aiodtrainingimage"></a> team_msdyn_aiodtrainingimage

**Added by**: Active Solution Solution

Same as msdyn_aiodtrainingimage entity [team_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_team_msdyn_aiodtrainingimage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aiodtrainingimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_environmentvariabledefinition"></a> team_environmentvariabledefinition

**Added by**: Active Solution Solution

Same as environmentvariabledefinition entity [team_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_team_environmentvariabledefinition) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariabledefinition|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_environmentvariabledefinition|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_environmentvariablevalue"></a> team_environmentvariablevalue

**Added by**: Active Solution Solution

Same as environmentvariablevalue entity [team_environmentvariablevalue](environmentvariablevalue.md#BKMK_team_environmentvariablevalue) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_environmentvariablevalue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_processstageparameter"></a> team_processstageparameter

**Added by**: Active Solution Solution

Same as processstageparameter entity [team_processstageparameter](processstageparameter.md#BKMK_team_processstageparameter) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_processstageparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowsession"></a> team_flowsession

**Added by**: Active Solution Solution

Same as flowsession entity [team_flowsession](flowsession.md#BKMK_team_flowsession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_flowsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_workflowbinary"></a> team_workflowbinary

**Added by**: Active Solution Solution

Same as workflowbinary entity [team_workflowbinary](workflowbinary.md#BKMK_team_workflowbinary) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_workflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connectionreference"></a> team_connectionreference

**Added by**: Active Solution Solution

Same as connectionreference entity [team_connectionreference](connectionreference.md#BKMK_team_connectionreference) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_connectionreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysiscomponent"></a> team_msdyn_analysiscomponent

**Added by**: Active Solution Solution

Same as msdyn_analysiscomponent entity [team_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_team_msdyn_analysiscomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_analysiscomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysisjob"></a> team_msdyn_analysisjob

**Added by**: Active Solution Solution

Same as msdyn_analysisjob entity [team_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_team_msdyn_analysisjob) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_analysisjob|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysisresult"></a> team_msdyn_analysisresult

**Added by**: Active Solution Solution

Same as msdyn_analysisresult entity [team_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_team_msdyn_analysisresult) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_analysisresult|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysisresultdetail"></a> team_msdyn_analysisresultdetail

**Added by**: Active Solution Solution

Same as msdyn_analysisresultdetail entity [team_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_team_msdyn_analysisresultdetail) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresultdetail|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_analysisresultdetail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_solutionhealthrule"></a> team_msdyn_solutionhealthrule

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthrule entity [team_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_team_msdyn_solutionhealthrule) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_solutionhealthrule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_solutionhealthruleargument"></a> team_msdyn_solutionhealthruleargument

**Added by**: Active Solution Solution

Same as msdyn_solutionhealthruleargument entity [team_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_team_msdyn_solutionhealthruleargument) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_solutionhealthruleargument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

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

IntersectEntityName: teamroles<br />
#### Entity 1

|Property|Value|
|--------|-----|
|IntersectAttribute|teamid|
|IsCustomizable|False|
|LogicalName|team|
|NavigationPropertyName|teamroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Entity 2

|Property|Value|
|--------|-----|
|LogicalName|role|
|IntersectAttribute|roleid|
|NavigationPropertyName|teamroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_teammembership_association"></a> teammembership_association

IntersectEntityName: teammembership<br />
#### Entity 1

|Property|Value|
|--------|-----|
|IntersectAttribute|teamid|
|IsCustomizable|False|
|LogicalName|team|
|NavigationPropertyName|teammembership_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Entity 2

|Property|Value|
|--------|-----|
|LogicalName|systemuser|
|IntersectAttribute|systemuserid|
|NavigationPropertyName|teammembership_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_teamprofiles_association"></a> teamprofiles_association

IntersectEntityName: teamprofiles<br />
#### Entity 1

|Property|Value|
|--------|-----|
|IntersectAttribute|teamid|
|IsCustomizable|False|
|LogicalName|team|
|NavigationPropertyName|teamprofiles_association|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |

#### Entity 2

|Property|Value|
|--------|-----|
|LogicalName|fieldsecurityprofile|
|IntersectAttribute|fieldsecurityprofileid|
|NavigationPropertyName|teamprofiles_association|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |


### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.team?text=team EntityType" />