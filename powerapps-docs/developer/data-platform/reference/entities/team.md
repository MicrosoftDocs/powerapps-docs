---
title: "Team table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Team table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Team table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Collection of system users that routinely collaborate. Teams can be used to simplify record sharing and provide team members with common access to organization data when team members belong to different Business Units.


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|AddMembersTeam|<xref:Microsoft.Dynamics.CRM.AddMembersTeam?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.AddMembersTeamRequest>|
|ConvertOwnerTeamToAccessTeam|<xref:Microsoft.Dynamics.CRM.ConvertOwnerTeamToAccessTeam?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ConvertOwnerTeamToAccessTeamRequest>|
|Create|POST /teams<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE /teams(*teamid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|RemoveMembersTeam|<xref:Microsoft.Dynamics.CRM.RemoveMembersTeam?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RemoveMembersTeamRequest>|
|Retrieve|GET /teams(*teamid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /teams<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|SetParentBusinessUnit|[Associate and disassociate entities](/powerapps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api)|<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|
|SetParentSystemUser|<xref:Microsoft.Dynamics.CRM.SetParentSystemUser?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|
|SetParentTeam|<xref:Microsoft.Dynamics.CRM.SetParentTeam?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|
|Update|PATCH /teams(*teamid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

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

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AdministratorId](#BKMK_AdministratorId)
- [AzureActiveDirectoryObjectId](#BKMK_AzureActiveDirectoryObjectId)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [DelegatedAuthorizationId](#BKMK_DelegatedAuthorizationId)
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


### <a name="BKMK_DelegatedAuthorizationId"></a> DelegatedAuthorizationId

**Added by**: Delegated Authorization Solution

|Property|Value|
|--------|-----|
|Description|The delegated authorization context for the team.|
|DisplayName|Delegated authorization|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|delegatedauthorizationid|
|RequiredLevel|None|
|Targets|delegatedauthorization|
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

**Added by**: AuthorizationCore Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Membership Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|membershiptype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### MembershipType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Members and guests||
|1|Members||
|2|Owners||
|3|Guests||



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
|Targets|knowledgearticle|
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

#### TeamType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Owner||
|1|Access||
|2|AAD Security Group||
|3|AAD Office Group||



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

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

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
- [DelegatedAuthorizationIdName](#BKMK_DelegatedAuthorizationIdName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsDefault](#BKMK_IsDefault)
- [IsSasTokenSet](#BKMK_IsSasTokenSet)
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
- [SasToken](#BKMK_SasToken)
- [ShareLinkQualifier](#BKMK_ShareLinkQualifier)
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


### <a name="BKMK_DelegatedAuthorizationIdName"></a> DelegatedAuthorizationIdName

**Added by**: Delegated Authorization Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|delegatedauthorizationidname|
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
|MinValue|0.000000000001|
|Precision|12|
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

#### IsDefault Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_IsSasTokenSet"></a> IsSasTokenSet

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|issastokenset|
|RequiredLevel|None|
|Type|Boolean|

#### IsSasTokenSet Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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


### <a name="BKMK_SasToken"></a> SasToken

**Added by**: Access Team Solution

|Property|Value|
|--------|-----|
|Description|Sas Token for Team.|
|DisplayName|Sas Token|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|sastoken|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ShareLinkQualifier"></a> ShareLinkQualifier

**Added by**: Access Team Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Share Link Qualifier|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|sharelinkqualifier|
|MaxLength|1250|
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

#### SystemManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



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
- [team_solutioncomponentbatchconfiguration](#BKMK_team_solutioncomponentbatchconfiguration)
- [team_stagesolutionupload](#BKMK_team_stagesolutionupload)
- [team_exportsolutionupload](#BKMK_team_exportsolutionupload)
- [team_featurecontrolsetting](#BKMK_team_featurecontrolsetting)
- [team_customapi](#BKMK_team_customapi)
- [team_customapirequestparameter](#BKMK_team_customapirequestparameter)
- [team_customapiresponseproperty](#BKMK_team_customapiresponseproperty)
- [team_datalakefolder](#BKMK_team_datalakefolder)
- [team_exportedexcel](#BKMK_team_exportedexcel)
- [team_retaineddataexcel](#BKMK_team_retaineddataexcel)
- [team_synapsedatabase](#BKMK_team_synapsedatabase)
- [team_msdyn_dataflow](#BKMK_team_msdyn_dataflow)
- [team_msdyn_dataflowrefreshhistory](#BKMK_team_msdyn_dataflowrefreshhistory)
- [team_msdyn_entityrefreshhistory](#BKMK_team_msdyn_entityrefreshhistory)
- [team_connector](#BKMK_team_connector)
- [team_environmentvariabledefinition](#BKMK_team_environmentvariabledefinition)
- [team_environmentvariablevalue](#BKMK_team_environmentvariablevalue)
- [team_workflowbinary](#BKMK_team_workflowbinary)
- [team_desktopflowmodule](#BKMK_team_desktopflowmodule)
- [team_flowmachine](#BKMK_team_flowmachine)
- [team_flowmachinegroup](#BKMK_team_flowmachinegroup)
- [team_flowmachineimage](#BKMK_team_flowmachineimage)
- [team_flowmachineimageversion](#BKMK_team_flowmachineimageversion)
- [team_flowmachinenetwork](#BKMK_team_flowmachinenetwork)
- [team_processstageparameter](#BKMK_team_processstageparameter)
- [team_workqueue](#BKMK_team_workqueue)
- [team_workqueueitem](#BKMK_team_workqueueitem)
- [team_desktopflowbinary](#BKMK_team_desktopflowbinary)
- [team_flowsession](#BKMK_team_flowsession)
- [team_connectionreference](#BKMK_team_connectionreference)
- [team_connectioninstance](#BKMK_team_connectioninstance)
- [team_msdynce_botcontent](#BKMK_team_msdynce_botcontent)
- [team_conversationtranscript](#BKMK_team_conversationtranscript)
- [team_bot](#BKMK_team_bot)
- [team_botcomponent](#BKMK_team_botcomponent)
- [team_activityfileattachment](#BKMK_team_activityfileattachment)
- [chat_team_owningteam](#BKMK_chat_team_owningteam)
- [team_msdyn_serviceconfiguration](#BKMK_team_msdyn_serviceconfiguration)
- [team_msdyn_slakpi](#BKMK_team_msdyn_slakpi)
- [team_msdyn_knowledgemanagementsetting](#BKMK_team_msdyn_knowledgemanagementsetting)
- [team_msdyn_federatedarticle](#BKMK_team_msdyn_federatedarticle)
- [team_msdyn_integratedsearchprovider](#BKMK_team_msdyn_integratedsearchprovider)
- [team_msdyn_kmfederatedsearchconfig](#BKMK_team_msdyn_kmfederatedsearchconfig)
- [team_msdyn_knowledgearticleimage](#BKMK_team_msdyn_knowledgearticleimage)
- [team_msdyn_knowledgeinteractioninsight](#BKMK_team_msdyn_knowledgeinteractioninsight)
- [team_msdyn_knowledgesearchinsight](#BKMK_team_msdyn_knowledgesearchinsight)
- [team_msdyn_favoriteknowledgearticle](#BKMK_team_msdyn_favoriteknowledgearticle)
- [team_msdyn_kalanguagesetting](#BKMK_team_msdyn_kalanguagesetting)
- [team_msdyn_kbattachment](#BKMK_team_msdyn_kbattachment)
- [team_msdyn_knowledgearticletemplate](#BKMK_team_msdyn_knowledgearticletemplate)
- [team_msdyn_knowledgepersonalfilter](#BKMK_team_msdyn_knowledgepersonalfilter)
- [team_msdyn_knowledgesearchfilter](#BKMK_team_msdyn_knowledgesearchfilter)
- [team_fxexpression](#BKMK_team_fxexpression)
- [team_powerfxrule](#BKMK_team_powerfxrule)
- [team_keyvaultreference](#BKMK_team_keyvaultreference)
- [team_managedidentity](#BKMK_team_managedidentity)
- [team_teammobileofflineprofilemembership_TeamId](#BKMK_team_teammobileofflineprofilemembership_TeamId)
- [team_retentionconfig](#BKMK_team_retentionconfig)
- [team_retentionfailuredetail](#BKMK_team_retentionfailuredetail)
- [team_retentionoperation](#BKMK_team_retentionoperation)
- [team_msdyn_dataflowtemplate](#BKMK_team_msdyn_dataflowtemplate)
- [team_appnotification](#BKMK_team_appnotification)
- [team_msdyn_mobileapp](#BKMK_team_msdyn_mobileapp)
- [team_card](#BKMK_team_card)
- [team_msdyn_entitylinkchatconfiguration](#BKMK_team_msdyn_entitylinkchatconfiguration)
- [team_msdyn_richtextfile](#BKMK_team_msdyn_richtextfile)
- [team_msdyn_customcontrolextendedsettings](#BKMK_team_msdyn_customcontrolextendedsettings)
- [team_recentlyused](#BKMK_team_recentlyused)
- [team_msdyn_virtualtablecolumncandidate](#BKMK_team_msdyn_virtualtablecolumncandidate)
- [team_msdyn_aievent](#BKMK_team_msdyn_aievent)
- [team_msdyn_aimodel](#BKMK_team_msdyn_aimodel)
- [team_msdyn_aitemplate](#BKMK_team_msdyn_aitemplate)
- [team_msdyn_aibfeedbackloop](#BKMK_team_msdyn_aibfeedbackloop)
- [team_msdyn_aifptrainingdocument](#BKMK_team_msdyn_aifptrainingdocument)
- [team_msdyn_aiodimage](#BKMK_team_msdyn_aiodimage)
- [team_msdyn_aiodlabel](#BKMK_team_msdyn_aiodlabel)
- [team_msdyn_aiodtrainingboundingbox](#BKMK_team_msdyn_aiodtrainingboundingbox)
- [team_msdyn_aiodtrainingimage](#BKMK_team_msdyn_aiodtrainingimage)
- [team_msdyn_aibdataset](#BKMK_team_msdyn_aibdataset)
- [team_msdyn_aibdatasetfile](#BKMK_team_msdyn_aibdatasetfile)
- [team_msdyn_aibdatasetrecord](#BKMK_team_msdyn_aibdatasetrecord)
- [team_msdyn_aibdatasetscontainer](#BKMK_team_msdyn_aibdatasetscontainer)
- [team_msdyn_aibfile](#BKMK_team_msdyn_aibfile)
- [team_msdyn_aibfileattacheddata](#BKMK_team_msdyn_aibfileattacheddata)
- [team_msdyn_pmanalysishistory](#BKMK_team_msdyn_pmanalysishistory)
- [team_msdyn_pmcalendar](#BKMK_team_msdyn_pmcalendar)
- [team_msdyn_pmcalendarversion](#BKMK_team_msdyn_pmcalendarversion)
- [team_msdyn_pminferredtask](#BKMK_team_msdyn_pminferredtask)
- [team_msdyn_pmprocessextendedmetadataversion](#BKMK_team_msdyn_pmprocessextendedmetadataversion)
- [team_msdyn_pmprocesstemplate](#BKMK_team_msdyn_pmprocesstemplate)
- [team_msdyn_pmprocessusersettings](#BKMK_team_msdyn_pmprocessusersettings)
- [team_msdyn_pmprocessversion](#BKMK_team_msdyn_pmprocessversion)
- [team_msdyn_pmrecording](#BKMK_team_msdyn_pmrecording)
- [team_msdyn_pmtemplate](#BKMK_team_msdyn_pmtemplate)
- [team_msdyn_pmview](#BKMK_team_msdyn_pmview)
- [team_msdyn_analysiscomponent](#BKMK_team_msdyn_analysiscomponent)
- [team_msdyn_analysisjob](#BKMK_team_msdyn_analysisjob)
- [team_msdyn_analysisoverride](#BKMK_team_msdyn_analysisoverride)
- [team_msdyn_analysisresult](#BKMK_team_msdyn_analysisresult)
- [team_msdyn_analysisresultdetail](#BKMK_team_msdyn_analysisresultdetail)
- [team_msdyn_solutionhealthrule](#BKMK_team_msdyn_solutionhealthrule)
- [team_msdyn_solutionhealthruleargument](#BKMK_team_msdyn_solutionhealthruleargument)
- [team_powerbidataset](#BKMK_team_powerbidataset)
- [team_powerbimashupparameter](#BKMK_team_powerbimashupparameter)
- [team_powerbireport](#BKMK_team_powerbireport)
- [team_msdyn_fileupload](#BKMK_team_msdyn_fileupload)
- [team_mspcat_catalogsubmissionfiles](#BKMK_team_mspcat_catalogsubmissionfiles)
- [team_mspcat_packagestore](#BKMK_team_mspcat_packagestore)
- [team_msdyn_schedule](#BKMK_team_msdyn_schedule)
- [team_msdyn_dataflow_datalakefolder](#BKMK_team_msdyn_dataflow_datalakefolder)
- [team_msdyn_dmsrequest](#BKMK_team_msdyn_dmsrequest)
- [team_msdyn_dmsrequeststatus](#BKMK_team_msdyn_dmsrequeststatus)


### <a name="BKMK_team_principalobjectattributeaccess_principalid"></a> team_principalobjectattributeaccess_principalid

Same as the [team_principalobjectattributeaccess_principalid](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess_principalid) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

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

Same as the [team_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_team_exchangesyncidmapping) many-to-one relationship for the [exchangesyncidmapping](exchangesyncidmapping.md) table/entity.

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

Same as the [team_interactionforemail](interactionforemail.md#BKMK_team_interactionforemail) many-to-one relationship for the [interactionforemail](interactionforemail.md) table/entity.

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

Same as the [team_knowledgearticle](knowledgearticle.md#BKMK_team_knowledgearticle) many-to-one relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

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

Same as the [team_sharepointsite](sharepointsite.md#BKMK_team_sharepointsite) many-to-one relationship for the [sharepointsite](sharepointsite.md) table/entity.

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

Same as the [team_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_team_sharepointdocumentlocation) many-to-one relationship for the [sharepointdocumentlocation](sharepointdocumentlocation.md) table/entity.

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

Same as the [team_goal](goal.md#BKMK_team_goal) many-to-one relationship for the [goal](goal.md) table/entity.

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

Same as the [team_goalrollupquery](goalrollupquery.md#BKMK_team_goalrollupquery) many-to-one relationship for the [goalrollupquery](goalrollupquery.md) table/entity.

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

Same as the [team_mailbox](mailbox.md#BKMK_team_mailbox) many-to-one relationship for the [mailbox](mailbox.md) table/entity.

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

Same as the [team_connections2](connection.md#BKMK_team_connections2) many-to-one relationship for the [connection](connection.md) table/entity.

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

Same as the [team_slaBase](sla.md#BKMK_team_slaBase) many-to-one relationship for the [sla](sla.md) table/entity.

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

Same as the [team_goal_goalowner](goal.md#BKMK_team_goal_goalowner) many-to-one relationship for the [goal](goal.md) table/entity.

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

Same as the [team_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_team_principalobjectattributeaccess) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

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

Same as the [OwningTeam_postfollows](postfollow.md#BKMK_OwningTeam_postfollows) many-to-one relationship for the [postfollow](postfollow.md) table/entity.

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

Same as the [team_ImportMaps](importmap.md#BKMK_team_ImportMaps) many-to-one relationship for the [importmap](importmap.md) table/entity.

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

Same as the [team_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_team_recurringappointmentmaster) many-to-one relationship for the [recurringappointmentmaster](recurringappointmentmaster.md) table/entity.

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

Same as the [team_queueitembase_workerid](queueitem.md#BKMK_team_queueitembase_workerid) many-to-one relationship for the [queueitem](queueitem.md) table/entity.

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

Same as the [team_phonecall](phonecall.md#BKMK_team_phonecall) many-to-one relationship for the [phonecall](phonecall.md) table/entity.

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

Same as the [team_emailserverprofile](emailserverprofile.md#BKMK_team_emailserverprofile) many-to-one relationship for the [emailserverprofile](emailserverprofile.md) table/entity.

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

Same as the [team_connections1](connection.md#BKMK_team_connections1) many-to-one relationship for the [connection](connection.md) table/entity.

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

Same as the [team_userqueryvisualizations](userqueryvisualization.md#BKMK_team_userqueryvisualizations) many-to-one relationship for the [userqueryvisualization](userqueryvisualization.md) table/entity.

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

Same as the [team_userform](userform.md#BKMK_team_userform) many-to-one relationship for the [userform](userform.md) table/entity.

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

Same as the [team_socialactivity](socialactivity.md#BKMK_team_socialactivity) many-to-one relationship for the [socialactivity](socialactivity.md) table/entity.

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

Same as the [Team_ProcessSessions](processsession.md#BKMK_Team_ProcessSessions) many-to-one relationship for the [processsession](processsession.md) table/entity.

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

Same as the [Team_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Team_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

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

Same as the [team_contacts](contact.md#BKMK_team_contacts) many-to-one relationship for the [contact](contact.md) table/entity.

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

Same as the [Team_AsyncOperations](asyncoperation.md#BKMK_Team_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

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

Same as the [team_ImportLogs](importlog.md#BKMK_team_ImportLogs) many-to-one relationship for the [importlog](importlog.md) table/entity.

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

Same as the [team_workflowlog](workflowlog.md#BKMK_team_workflowlog) many-to-one relationship for the [workflowlog](workflowlog.md) table/entity.

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

Same as the [team_Imports](import.md#BKMK_team_Imports) many-to-one relationship for the [import](import.md) table/entity.

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

Same as the [team_processsession](processsession.md#BKMK_team_processsession) many-to-one relationship for the [processsession](processsession.md) table/entity.

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

Same as the [team_SyncError](syncerror.md#BKMK_team_SyncError) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

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

Same as the [team_letter](letter.md#BKMK_team_letter) many-to-one relationship for the [letter](letter.md) table/entity.

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

Same as the [team_annotations](annotation.md#BKMK_team_annotations) many-to-one relationship for the [annotation](annotation.md) table/entity.

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

Same as the [team_appointment](appointment.md#BKMK_team_appointment) many-to-one relationship for the [appointment](appointment.md) table/entity.

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

Same as the [team_asyncoperation](asyncoperation.md#BKMK_team_asyncoperation) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

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

Same as the [Team_BulkDeleteFailures](bulkdeletefailure.md#BKMK_Team_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

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

Same as the [Team_SyncErrors](syncerror.md#BKMK_Team_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

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

Same as the [team_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_team_mailboxtrackingfolder) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

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

Same as the [team_task](task.md#BKMK_team_task) many-to-one relationship for the [task](task.md) table/entity.

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

Same as the [team_activity](activitypointer.md#BKMK_team_activity) many-to-one relationship for the [activitypointer](activitypointer.md) table/entity.

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

Same as the [Team_DuplicateBaseRecord](duplicaterecord.md#BKMK_Team_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

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

Same as the [team_accounts](account.md#BKMK_team_accounts) many-to-one relationship for the [account](account.md) table/entity.

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

Same as the [team_userquery](userquery.md#BKMK_team_userquery) many-to-one relationship for the [userquery](userquery.md) table/entity.

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

Same as the [team_email](email.md#BKMK_team_email) many-to-one relationship for the [email](email.md) table/entity.

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

Same as the [ImportFile_Team](importfile.md#BKMK_ImportFile_Team) many-to-one relationship for the [importfile](importfile.md) table/entity.

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

Same as the [team_ImportFiles](importfile.md#BKMK_team_ImportFiles) many-to-one relationship for the [importfile](importfile.md) table/entity.

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

Same as the [team_email_templates](template.md#BKMK_team_email_templates) many-to-one relationship for the [template](template.md) table/entity.

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

Same as the [team_fax](fax.md#BKMK_team_fax) many-to-one relationship for the [fax](fax.md) table/entity.

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

Same as the [team_DuplicateRules](duplicaterule.md#BKMK_team_DuplicateRules) many-to-one relationship for the [duplicaterule](duplicaterule.md) table/entity.

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

Same as the [team_workflow](workflow.md#BKMK_team_workflow) many-to-one relationship for the [workflow](workflow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_workflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_solutioncomponentbatchconfiguration"></a> team_solutioncomponentbatchconfiguration

**Added by**: Active Solution Solution

Same as the [team_solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md#BKMK_team_solutioncomponentbatchconfiguration) many-to-one relationship for the [solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|solutioncomponentbatchconfiguration|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_solutioncomponentbatchconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_stagesolutionupload"></a> team_stagesolutionupload

**Added by**: Active Solution Solution

Same as the [team_stagesolutionupload](stagesolutionupload.md#BKMK_team_stagesolutionupload) many-to-one relationship for the [stagesolutionupload](stagesolutionupload.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|stagesolutionupload|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_stagesolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_exportsolutionupload"></a> team_exportsolutionupload

**Added by**: Active Solution Solution

Same as the [team_exportsolutionupload](exportsolutionupload.md#BKMK_team_exportsolutionupload) many-to-one relationship for the [exportsolutionupload](exportsolutionupload.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportsolutionupload|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_exportsolutionupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_featurecontrolsetting"></a> team_featurecontrolsetting

**Added by**: Active Solution Solution

Same as the [team_featurecontrolsetting](featurecontrolsetting.md#BKMK_team_featurecontrolsetting) many-to-one relationship for the [featurecontrolsetting](featurecontrolsetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|featurecontrolsetting|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_featurecontrolsetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_customapi"></a> team_customapi

**Added by**: Active Solution Solution

Same as the [team_customapi](customapi.md#BKMK_team_customapi) many-to-one relationship for the [customapi](customapi.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapi|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_customapi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_customapirequestparameter"></a> team_customapirequestparameter

**Added by**: Active Solution Solution

Same as the [team_customapirequestparameter](customapirequestparameter.md#BKMK_team_customapirequestparameter) many-to-one relationship for the [customapirequestparameter](customapirequestparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapirequestparameter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_customapirequestparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_customapiresponseproperty"></a> team_customapiresponseproperty

**Added by**: Active Solution Solution

Same as the [team_customapiresponseproperty](customapiresponseproperty.md#BKMK_team_customapiresponseproperty) many-to-one relationship for the [customapiresponseproperty](customapiresponseproperty.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|customapiresponseproperty|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_customapiresponseproperty|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_datalakefolder"></a> team_datalakefolder

**Added by**: Active Solution Solution

Same as the [team_datalakefolder](datalakefolder.md#BKMK_team_datalakefolder) many-to-one relationship for the [datalakefolder](datalakefolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|datalakefolder|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_datalakefolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_exportedexcel"></a> team_exportedexcel

**Added by**: Active Solution Solution

Same as the [team_exportedexcel](exportedexcel.md#BKMK_team_exportedexcel) many-to-one relationship for the [exportedexcel](exportedexcel.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|exportedexcel|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_exportedexcel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_retaineddataexcel"></a> team_retaineddataexcel

**Added by**: Active Solution Solution

Same as the [team_retaineddataexcel](retaineddataexcel.md#BKMK_team_retaineddataexcel) many-to-one relationship for the [retaineddataexcel](retaineddataexcel.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retaineddataexcel|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_retaineddataexcel|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_synapsedatabase"></a> team_synapsedatabase

**Added by**: Active Solution Solution

Same as the [team_synapsedatabase](synapsedatabase.md#BKMK_team_synapsedatabase) many-to-one relationship for the [synapsedatabase](synapsedatabase.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|synapsedatabase|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_synapsedatabase|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dataflow"></a> team_msdyn_dataflow

**Added by**: Active Solution Solution

Same as the [team_msdyn_dataflow](msdyn_dataflow.md#BKMK_team_msdyn_dataflow) many-to-one relationship for the [msdyn_dataflow](msdyn_dataflow.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dataflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dataflowrefreshhistory"></a> team_msdyn_dataflowrefreshhistory

**Added by**: Active Solution Solution

Same as the [team_msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md#BKMK_team_msdyn_dataflowrefreshhistory) many-to-one relationship for the [msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflowrefreshhistory|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dataflowrefreshhistory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_entityrefreshhistory"></a> team_msdyn_entityrefreshhistory

**Added by**: Active Solution Solution

Same as the [team_msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md#BKMK_team_msdyn_entityrefreshhistory) many-to-one relationship for the [msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_entityrefreshhistory|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_entityrefreshhistory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connector"></a> team_connector

**Added by**: Active Solution Solution

Same as the [team_connector](connector.md#BKMK_team_connector) many-to-one relationship for the [connector](connector.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connector|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_connector|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_environmentvariabledefinition"></a> team_environmentvariabledefinition

**Added by**: Active Solution Solution

Same as the [team_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_team_environmentvariabledefinition) many-to-one relationship for the [environmentvariabledefinition](environmentvariabledefinition.md) table/entity.

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

Same as the [team_environmentvariablevalue](environmentvariablevalue.md#BKMK_team_environmentvariablevalue) many-to-one relationship for the [environmentvariablevalue](environmentvariablevalue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|environmentvariablevalue|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_environmentvariablevalue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_workflowbinary"></a> team_workflowbinary

**Added by**: Active Solution Solution

Same as the [team_workflowbinary](workflowbinary.md#BKMK_team_workflowbinary) many-to-one relationship for the [workflowbinary](workflowbinary.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_workflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_desktopflowmodule"></a> team_desktopflowmodule

**Added by**: Active Solution Solution

Same as the [team_desktopflowmodule](desktopflowmodule.md#BKMK_team_desktopflowmodule) many-to-one relationship for the [desktopflowmodule](desktopflowmodule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|desktopflowmodule|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_desktopflowmodule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowmachine"></a> team_flowmachine

**Added by**: Active Solution Solution

Same as the [team_flowmachine](flowmachine.md#BKMK_team_flowmachine) many-to-one relationship for the [flowmachine](flowmachine.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachine|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_flowmachine|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowmachinegroup"></a> team_flowmachinegroup

**Added by**: Active Solution Solution

Same as the [team_flowmachinegroup](flowmachinegroup.md#BKMK_team_flowmachinegroup) many-to-one relationship for the [flowmachinegroup](flowmachinegroup.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinegroup|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_flowmachinegroup|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowmachineimage"></a> team_flowmachineimage

**Added by**: Active Solution Solution

Same as the [team_flowmachineimage](flowmachineimage.md#BKMK_team_flowmachineimage) many-to-one relationship for the [flowmachineimage](flowmachineimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachineimage|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_flowmachineimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowmachineimageversion"></a> team_flowmachineimageversion

**Added by**: Active Solution Solution

Same as the [team_flowmachineimageversion](flowmachineimageversion.md#BKMK_team_flowmachineimageversion) many-to-one relationship for the [flowmachineimageversion](flowmachineimageversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachineimageversion|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_flowmachineimageversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowmachinenetwork"></a> team_flowmachinenetwork

**Added by**: Active Solution Solution

Same as the [team_flowmachinenetwork](flowmachinenetwork.md#BKMK_team_flowmachinenetwork) many-to-one relationship for the [flowmachinenetwork](flowmachinenetwork.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowmachinenetwork|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_flowmachinenetwork|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_processstageparameter"></a> team_processstageparameter

**Added by**: Active Solution Solution

Same as the [team_processstageparameter](processstageparameter.md#BKMK_team_processstageparameter) many-to-one relationship for the [processstageparameter](processstageparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstageparameter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_processstageparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_workqueue"></a> team_workqueue

**Added by**: Active Solution Solution

Same as the [team_workqueue](workqueue.md#BKMK_team_workqueue) many-to-one relationship for the [workqueue](workqueue.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workqueue|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_workqueue|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_workqueueitem"></a> team_workqueueitem

**Added by**: Active Solution Solution

Same as the [team_workqueueitem](workqueueitem.md#BKMK_team_workqueueitem) many-to-one relationship for the [workqueueitem](workqueueitem.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|workqueueitem|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_workqueueitem|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_desktopflowbinary"></a> team_desktopflowbinary

**Added by**: Active Solution Solution

Same as the [team_desktopflowbinary](desktopflowbinary.md#BKMK_team_desktopflowbinary) many-to-one relationship for the [desktopflowbinary](desktopflowbinary.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|desktopflowbinary|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_desktopflowbinary|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_flowsession"></a> team_flowsession

**Added by**: Active Solution Solution

Same as the [team_flowsession](flowsession.md#BKMK_team_flowsession) many-to-one relationship for the [flowsession](flowsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_flowsession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connectionreference"></a> team_connectionreference

**Added by**: Active Solution Solution

Same as the [team_connectionreference](connectionreference.md#BKMK_team_connectionreference) many-to-one relationship for the [connectionreference](connectionreference.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectionreference|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_connectionreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_connectioninstance"></a> team_connectioninstance

**Added by**: Active Solution Solution

Same as the [team_connectioninstance](connectioninstance.md#BKMK_team_connectioninstance) many-to-one relationship for the [connectioninstance](connectioninstance.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|connectioninstance|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_connectioninstance|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdynce_botcontent"></a> team_msdynce_botcontent

**Added by**: Active Solution Solution

Same as the [team_msdynce_botcontent](msdynce_botcontent.md#BKMK_team_msdynce_botcontent) many-to-one relationship for the [msdynce_botcontent](msdynce_botcontent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdynce_botcontent|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdynce_botcontent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_conversationtranscript"></a> team_conversationtranscript

**Added by**: Active Solution Solution

Same as the [team_conversationtranscript](conversationtranscript.md#BKMK_team_conversationtranscript) many-to-one relationship for the [conversationtranscript](conversationtranscript.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|conversationtranscript|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_conversationtranscript|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_bot"></a> team_bot

**Added by**: Active Solution Solution

Same as the [team_bot](bot.md#BKMK_team_bot) many-to-one relationship for the [bot](bot.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bot|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_bot|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_botcomponent"></a> team_botcomponent

**Added by**: Active Solution Solution

Same as the [team_botcomponent](botcomponent.md#BKMK_team_botcomponent) many-to-one relationship for the [botcomponent](botcomponent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|botcomponent|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_botcomponent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_activityfileattachment"></a> team_activityfileattachment

**Added by**: Activities Patch Solution

Same as the [team_activityfileattachment](activityfileattachment.md#BKMK_team_activityfileattachment) many-to-one relationship for the [activityfileattachment](activityfileattachment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|activityfileattachment|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_activityfileattachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_chat_team_owningteam"></a> chat_team_owningteam

**Added by**: Activities Patch Solution

Same as the [chat_team_owningteam](chat.md#BKMK_chat_team_owningteam) many-to-one relationship for the [chat](chat.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|chat|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|chat_team_owningteam|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_serviceconfiguration"></a> team_msdyn_serviceconfiguration

**Added by**: Active Solution Solution

Same as the [team_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md#BKMK_team_msdyn_serviceconfiguration) many-to-one relationship for the [msdyn_serviceconfiguration](msdyn_serviceconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_serviceconfiguration|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_serviceconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_slakpi"></a> team_msdyn_slakpi

**Added by**: Active Solution Solution

Same as the [team_msdyn_slakpi](msdyn_slakpi.md#BKMK_team_msdyn_slakpi) many-to-one relationship for the [msdyn_slakpi](msdyn_slakpi.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_slakpi|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_slakpi|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgemanagementsetting"></a> team_msdyn_knowledgemanagementsetting

**Added by**: Knowledge Management Patch Solution

Same as the [team_msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md#BKMK_team_msdyn_knowledgemanagementsetting) many-to-one relationship for the [msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgemanagementsetting|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgemanagementsetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_federatedarticle"></a> team_msdyn_federatedarticle

**Added by**: Active Solution Solution

Same as the [team_msdyn_federatedarticle](msdyn_federatedarticle.md#BKMK_team_msdyn_federatedarticle) many-to-one relationship for the [msdyn_federatedarticle](msdyn_federatedarticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_federatedarticle|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_federatedarticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_integratedsearchprovider"></a> team_msdyn_integratedsearchprovider

**Added by**: Active Solution Solution

Same as the [team_msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md#BKMK_team_msdyn_integratedsearchprovider) many-to-one relationship for the [msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_integratedsearchprovider|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_integratedsearchprovider|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_kmfederatedsearchconfig"></a> team_msdyn_kmfederatedsearchconfig

**Added by**: Active Solution Solution

Same as the [team_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md#BKMK_team_msdyn_kmfederatedsearchconfig) many-to-one relationship for the [msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kmfederatedsearchconfig|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_kmfederatedsearchconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgearticleimage"></a> team_msdyn_knowledgearticleimage

**Added by**: Active Solution Solution

Same as the [team_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_team_msdyn_knowledgearticleimage) many-to-one relationship for the [msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticleimage|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgearticleimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgeinteractioninsight"></a> team_msdyn_knowledgeinteractioninsight

**Added by**: Active Solution Solution

Same as the [team_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md#BKMK_team_msdyn_knowledgeinteractioninsight) many-to-one relationship for the [msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgeinteractioninsight|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgeinteractioninsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgesearchinsight"></a> team_msdyn_knowledgesearchinsight

**Added by**: Active Solution Solution

Same as the [team_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md#BKMK_team_msdyn_knowledgesearchinsight) many-to-one relationship for the [msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchinsight|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgesearchinsight|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_favoriteknowledgearticle"></a> team_msdyn_favoriteknowledgearticle

**Added by**: Active Solution Solution

Same as the [team_msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md#BKMK_team_msdyn_favoriteknowledgearticle) many-to-one relationship for the [msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_favoriteknowledgearticle|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_favoriteknowledgearticle|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_kalanguagesetting"></a> team_msdyn_kalanguagesetting

**Added by**: Active Solution Solution

Same as the [team_msdyn_kalanguagesetting](msdyn_kalanguagesetting.md#BKMK_team_msdyn_kalanguagesetting) many-to-one relationship for the [msdyn_kalanguagesetting](msdyn_kalanguagesetting.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kalanguagesetting|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_kalanguagesetting|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_kbattachment"></a> team_msdyn_kbattachment

**Added by**: Active Solution Solution

Same as the [team_msdyn_kbattachment](msdyn_kbattachment.md#BKMK_team_msdyn_kbattachment) many-to-one relationship for the [msdyn_kbattachment](msdyn_kbattachment.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_kbattachment|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_kbattachment|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgearticletemplate"></a> team_msdyn_knowledgearticletemplate

**Added by**: Active Solution Solution

Same as the [team_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_team_msdyn_knowledgearticletemplate) many-to-one relationship for the [msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgearticletemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgearticletemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgepersonalfilter"></a> team_msdyn_knowledgepersonalfilter

**Added by**: Active Solution Solution

Same as the [team_msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md#BKMK_team_msdyn_knowledgepersonalfilter) many-to-one relationship for the [msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgepersonalfilter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgepersonalfilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_knowledgesearchfilter"></a> team_msdyn_knowledgesearchfilter

**Added by**: Active Solution Solution

Same as the [team_msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md#BKMK_team_msdyn_knowledgesearchfilter) many-to-one relationship for the [msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_knowledgesearchfilter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_knowledgesearchfilter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_fxexpression"></a> team_fxexpression

**Added by**: Active Solution Solution

Same as the [team_fxexpression](fxexpression.md#BKMK_team_fxexpression) many-to-one relationship for the [fxexpression](fxexpression.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|fxexpression|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_fxexpression|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_powerfxrule"></a> team_powerfxrule

**Added by**: Active Solution Solution

Same as the [team_powerfxrule](powerfxrule.md#BKMK_team_powerfxrule) many-to-one relationship for the [powerfxrule](powerfxrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerfxrule|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_powerfxrule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_keyvaultreference"></a> team_keyvaultreference

**Added by**: Active Solution Solution

Same as the [team_keyvaultreference](keyvaultreference.md#BKMK_team_keyvaultreference) many-to-one relationship for the [keyvaultreference](keyvaultreference.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|keyvaultreference|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_keyvaultreference|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_managedidentity"></a> team_managedidentity

**Added by**: Active Solution Solution

Same as the [team_managedidentity](managedidentity.md#BKMK_team_managedidentity) many-to-one relationship for the [managedidentity](managedidentity.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|managedidentity|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_managedidentity|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_teammobileofflineprofilemembership_TeamId"></a> team_teammobileofflineprofilemembership_TeamId

**Added by**: MobileOfflineMembership Solution

Same as the [team_teammobileofflineprofilemembership_TeamId](teammobileofflineprofilemembership.md#BKMK_team_teammobileofflineprofilemembership_TeamId) many-to-one relationship for the [teammobileofflineprofilemembership](teammobileofflineprofilemembership.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|teammobileofflineprofilemembership|
|ReferencingAttribute|teamid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_teammobileofflineprofilemembership_TeamId|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_retentionconfig"></a> team_retentionconfig

**Added by**: Active Solution Solution

Same as the [team_retentionconfig](retentionconfig.md#BKMK_team_retentionconfig) many-to-one relationship for the [retentionconfig](retentionconfig.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retentionconfig|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_retentionconfig|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_retentionfailuredetail"></a> team_retentionfailuredetail

**Added by**: Active Solution Solution

Same as the [team_retentionfailuredetail](retentionfailuredetail.md#BKMK_team_retentionfailuredetail) many-to-one relationship for the [retentionfailuredetail](retentionfailuredetail.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retentionfailuredetail|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_retentionfailuredetail|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_retentionoperation"></a> team_retentionoperation

**Added by**: Active Solution Solution

Same as the [team_retentionoperation](retentionoperation.md#BKMK_team_retentionoperation) many-to-one relationship for the [retentionoperation](retentionoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|retentionoperation|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_retentionoperation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dataflowtemplate"></a> team_msdyn_dataflowtemplate

**Added by**: Active Solution Solution

Same as the [team_msdyn_dataflowtemplate](msdyn_dataflowtemplate.md#BKMK_team_msdyn_dataflowtemplate) many-to-one relationship for the [msdyn_dataflowtemplate](msdyn_dataflowtemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflowtemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dataflowtemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_appnotification"></a> team_appnotification

**Added by**: Active Solution Solution

Same as the [team_appnotification](appnotification.md#BKMK_team_appnotification) many-to-one relationship for the [appnotification](appnotification.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|appnotification|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_appnotification|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_mobileapp"></a> team_msdyn_mobileapp

**Added by**: Active Solution Solution

Same as the [team_msdyn_mobileapp](msdyn_mobileapp.md#BKMK_team_msdyn_mobileapp) many-to-one relationship for the [msdyn_mobileapp](msdyn_mobileapp.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_mobileapp|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_mobileapp|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_card"></a> team_card

**Added by**: Active Solution Solution

Same as the [team_card](card.md#BKMK_team_card) many-to-one relationship for the [card](card.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|card|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_card|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_entitylinkchatconfiguration"></a> team_msdyn_entitylinkchatconfiguration

**Added by**: Active Solution Solution

Same as the [team_msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md#BKMK_team_msdyn_entitylinkchatconfiguration) many-to-one relationship for the [msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_entitylinkchatconfiguration|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_entitylinkchatconfiguration|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_richtextfile"></a> team_msdyn_richtextfile

**Added by**: Active Solution Solution

Same as the [team_msdyn_richtextfile](msdyn_richtextfile.md#BKMK_team_msdyn_richtextfile) many-to-one relationship for the [msdyn_richtextfile](msdyn_richtextfile.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_richtextfile|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_richtextfile|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_customcontrolextendedsettings"></a> team_msdyn_customcontrolextendedsettings

**Added by**: Active Solution Solution

Same as the [team_msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md#BKMK_team_msdyn_customcontrolextendedsettings) many-to-one relationship for the [msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_customcontrolextendedsettings|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_customcontrolextendedsettings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_recentlyused"></a> team_recentlyused

**Added by**: Active Solution Solution

Same as the [team_recentlyused](recentlyused.md#BKMK_team_recentlyused) many-to-one relationship for the [recentlyused](recentlyused.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|recentlyused|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_recentlyused|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_virtualtablecolumncandidate"></a> team_msdyn_virtualtablecolumncandidate

**Added by**: Active Solution Solution

Same as the [team_msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md#BKMK_team_msdyn_virtualtablecolumncandidate) many-to-one relationship for the [msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_virtualtablecolumncandidate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_virtualtablecolumncandidate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aievent"></a> team_msdyn_aievent

**Added by**: Active Solution Solution

Same as the [team_msdyn_aievent](msdyn_aievent.md#BKMK_team_msdyn_aievent) many-to-one relationship for the [msdyn_aievent](msdyn_aievent.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aievent|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_aievent|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aimodel"></a> team_msdyn_aimodel

**Added by**: Active Solution Solution

Same as the [team_msdyn_aimodel](msdyn_aimodel.md#BKMK_team_msdyn_aimodel) many-to-one relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

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

Same as the [team_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_team_msdyn_aitemplate) many-to-one relationship for the [msdyn_aitemplate](msdyn_aitemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aitemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aitemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibfeedbackloop"></a> team_msdyn_aibfeedbackloop

**Added by**: Active Solution Solution

Same as the [team_msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md#BKMK_team_msdyn_aibfeedbackloop) many-to-one relationship for the [msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfeedbackloop|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibfeedbackloop|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aifptrainingdocument"></a> team_msdyn_aifptrainingdocument

**Added by**: Active Solution Solution

Same as the [team_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_team_msdyn_aifptrainingdocument) many-to-one relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

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

Same as the [team_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_team_msdyn_aiodimage) many-to-one relationship for the [msdyn_aiodimage](msdyn_aiodimage.md) table/entity.

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

Same as the [team_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_team_msdyn_aiodlabel) many-to-one relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

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

Same as the [team_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_team_msdyn_aiodtrainingboundingbox) many-to-one relationship for the [msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md) table/entity.

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

Same as the [team_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_team_msdyn_aiodtrainingimage) many-to-one relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aiodtrainingimage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_aibdataset"></a> team_msdyn_aibdataset

**Added by**: Active Solution Solution

Same as the [team_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_team_msdyn_aibdataset) many-to-one relationship for the [msdyn_aibdataset](msdyn_aibdataset.md) table/entity.

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

Same as the [team_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_team_msdyn_aibdatasetfile) many-to-one relationship for the [msdyn_aibdatasetfile](msdyn_aibdatasetfile.md) table/entity.

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

Same as the [team_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_team_msdyn_aibdatasetrecord) many-to-one relationship for the [msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md) table/entity.

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

Same as the [team_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_team_msdyn_aibdatasetscontainer) many-to-one relationship for the [msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md) table/entity.

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

Same as the [team_msdyn_aibfile](msdyn_aibfile.md#BKMK_team_msdyn_aibfile) many-to-one relationship for the [msdyn_aibfile](msdyn_aibfile.md) table/entity.

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

Same as the [team_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_team_msdyn_aibfileattacheddata) many-to-one relationship for the [msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aibfileattacheddata|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_aibfileattacheddata|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmanalysishistory"></a> team_msdyn_pmanalysishistory

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmanalysishistory](msdyn_pmanalysishistory.md#BKMK_team_msdyn_pmanalysishistory) many-to-one relationship for the [msdyn_pmanalysishistory](msdyn_pmanalysishistory.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmanalysishistory|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmanalysishistory|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmcalendar"></a> team_msdyn_pmcalendar

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmcalendar](msdyn_pmcalendar.md#BKMK_team_msdyn_pmcalendar) many-to-one relationship for the [msdyn_pmcalendar](msdyn_pmcalendar.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmcalendar|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmcalendar|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmcalendarversion"></a> team_msdyn_pmcalendarversion

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmcalendarversion](msdyn_pmcalendarversion.md#BKMK_team_msdyn_pmcalendarversion) many-to-one relationship for the [msdyn_pmcalendarversion](msdyn_pmcalendarversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmcalendarversion|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmcalendarversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pminferredtask"></a> team_msdyn_pminferredtask

**Added by**: Active Solution Solution

Same as the [team_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_team_msdyn_pminferredtask) many-to-one relationship for the [msdyn_pminferredtask](msdyn_pminferredtask.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pminferredtask|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pminferredtask|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmprocessextendedmetadataversion"></a> team_msdyn_pmprocessextendedmetadataversion

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md#BKMK_team_msdyn_pmprocessextendedmetadataversion) many-to-one relationship for the [msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocessextendedmetadataversion|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmprocessextendedmetadataversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmprocesstemplate"></a> team_msdyn_pmprocesstemplate

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md#BKMK_team_msdyn_pmprocesstemplate) many-to-one relationship for the [msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocesstemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmprocesstemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmprocessusersettings"></a> team_msdyn_pmprocessusersettings

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md#BKMK_team_msdyn_pmprocessusersettings) many-to-one relationship for the [msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocessusersettings|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmprocessusersettings|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmprocessversion"></a> team_msdyn_pmprocessversion

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmprocessversion](msdyn_pmprocessversion.md#BKMK_team_msdyn_pmprocessversion) many-to-one relationship for the [msdyn_pmprocessversion](msdyn_pmprocessversion.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmprocessversion|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmprocessversion|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmrecording"></a> team_msdyn_pmrecording

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_team_msdyn_pmrecording) many-to-one relationship for the [msdyn_pmrecording](msdyn_pmrecording.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmrecording|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmrecording|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmtemplate"></a> team_msdyn_pmtemplate

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmtemplate](msdyn_pmtemplate.md#BKMK_team_msdyn_pmtemplate) many-to-one relationship for the [msdyn_pmtemplate](msdyn_pmtemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmtemplate|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmtemplate|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_pmview"></a> team_msdyn_pmview

**Added by**: Active Solution Solution

Same as the [team_msdyn_pmview](msdyn_pmview.md#BKMK_team_msdyn_pmview) many-to-one relationship for the [msdyn_pmview](msdyn_pmview.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_pmview|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_pmview|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysiscomponent"></a> team_msdyn_analysiscomponent

**Added by**: Active Solution Solution

Same as the [team_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_team_msdyn_analysiscomponent) many-to-one relationship for the [msdyn_analysiscomponent](msdyn_analysiscomponent.md) table/entity.

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

Same as the [team_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_team_msdyn_analysisjob) many-to-one relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisjob|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_analysisjob|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysisoverride"></a> team_msdyn_analysisoverride

**Added by**: Active Solution Solution

Same as the [team_msdyn_analysisoverride](msdyn_analysisoverride.md#BKMK_team_msdyn_analysisoverride) many-to-one relationship for the [msdyn_analysisoverride](msdyn_analysisoverride.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisoverride|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_analysisoverride|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_analysisresult"></a> team_msdyn_analysisresult

**Added by**: Active Solution Solution

Same as the [team_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_team_msdyn_analysisresult) many-to-one relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

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

Same as the [team_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_team_msdyn_analysisresultdetail) many-to-one relationship for the [msdyn_analysisresultdetail](msdyn_analysisresultdetail.md) table/entity.

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

Same as the [team_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_team_msdyn_solutionhealthrule) many-to-one relationship for the [msdyn_solutionhealthrule](msdyn_solutionhealthrule.md) table/entity.

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

Same as the [team_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_team_msdyn_solutionhealthruleargument) many-to-one relationship for the [msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_msdyn_solutionhealthruleargument|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_powerbidataset"></a> team_powerbidataset

**Added by**: Active Solution Solution

Same as the [team_powerbidataset](powerbidataset.md#BKMK_team_powerbidataset) many-to-one relationship for the [powerbidataset](powerbidataset.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbidataset|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_powerbidataset|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_powerbimashupparameter"></a> team_powerbimashupparameter

**Added by**: Active Solution Solution

Same as the [team_powerbimashupparameter](powerbimashupparameter.md#BKMK_team_powerbimashupparameter) many-to-one relationship for the [powerbimashupparameter](powerbimashupparameter.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbimashupparameter|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_powerbimashupparameter|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_powerbireport"></a> team_powerbireport

**Added by**: Active Solution Solution

Same as the [team_powerbireport](powerbireport.md#BKMK_team_powerbireport) many-to-one relationship for the [powerbireport](powerbireport.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|powerbireport|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|team_powerbireport|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_fileupload"></a> team_msdyn_fileupload

**Added by**: Active Solution Solution

Same as the [team_msdyn_fileupload](msdyn_fileupload.md#BKMK_team_msdyn_fileupload) many-to-one relationship for the [msdyn_fileupload](msdyn_fileupload.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_fileupload|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_fileupload|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_mspcat_catalogsubmissionfiles"></a> team_mspcat_catalogsubmissionfiles

**Added by**: Active Solution Solution

Same as the [team_mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md#BKMK_team_mspcat_catalogsubmissionfiles) many-to-one relationship for the [mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspcat_catalogsubmissionfiles|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_mspcat_catalogsubmissionfiles|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_mspcat_packagestore"></a> team_mspcat_packagestore

**Added by**: Active Solution Solution

Same as the [team_mspcat_packagestore](mspcat_packagestore.md#BKMK_team_mspcat_packagestore) many-to-one relationship for the [mspcat_packagestore](mspcat_packagestore.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mspcat_packagestore|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_mspcat_packagestore|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_schedule"></a> team_msdyn_schedule

**Added by**: Active Solution Solution

Same as the [team_msdyn_schedule](msdyn_schedule.md#BKMK_team_msdyn_schedule) many-to-one relationship for the [msdyn_schedule](msdyn_schedule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_schedule|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_schedule|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dataflow_datalakefolder"></a> team_msdyn_dataflow_datalakefolder

**Added by**: Active Solution Solution

Same as the [team_msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md#BKMK_team_msdyn_dataflow_datalakefolder) many-to-one relationship for the [msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dataflow_datalakefolder|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dataflow_datalakefolder|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dmsrequest"></a> team_msdyn_dmsrequest

**Added by**: Active Solution Solution

Same as the [team_msdyn_dmsrequest](msdyn_dmsrequest.md#BKMK_team_msdyn_dmsrequest) many-to-one relationship for the [msdyn_dmsrequest](msdyn_dmsrequest.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dmsrequest|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dmsrequest|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_team_msdyn_dmsrequeststatus"></a> team_msdyn_dmsrequeststatus

**Added by**: Active Solution Solution

Same as the [team_msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md#BKMK_team_msdyn_dmsrequeststatus) many-to-one relationship for the [msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_dmsrequeststatus|
|ReferencingAttribute|owningteam|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|team_msdyn_dmsrequeststatus|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

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
- [team_delegatedauthorization](#BKMK_team_delegatedauthorization)


### <a name="BKMK_knowledgearticle_Teams"></a> knowledgearticle_Teams

See the [knowledgearticle_Teams](knowledgearticle.md#BKMK_knowledgearticle_Teams) one-to-many relationship for the [knowledgearticle](knowledgearticle.md) table/entity.

### <a name="BKMK_teamtemplate_Teams"></a> teamtemplate_Teams

See the [teamtemplate_Teams](teamtemplate.md#BKMK_teamtemplate_Teams) one-to-many relationship for the [teamtemplate](teamtemplate.md) table/entity.

### <a name="BKMK_lk_teambase_administratorid"></a> lk_teambase_administratorid

See the [lk_teambase_administratorid](systemuser.md#BKMK_lk_teambase_administratorid) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_processstage_teams"></a> processstage_teams

See the [processstage_teams](processstage.md#BKMK_processstage_teams) one-to-many relationship for the [processstage](processstage.md) table/entity.

### <a name="BKMK_lk_teambase_modifiedby"></a> lk_teambase_modifiedby

See the [lk_teambase_modifiedby](systemuser.md#BKMK_lk_teambase_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_teambase_createdby"></a> lk_teambase_createdby

See the [lk_teambase_createdby](systemuser.md#BKMK_lk_teambase_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_queue_team"></a> queue_team

See the [queue_team](queue.md#BKMK_queue_team) one-to-many relationship for the [queue](queue.md) table/entity.

### <a name="BKMK_TransactionCurrency_Team"></a> TransactionCurrency_Team

See the [TransactionCurrency_Team](transactioncurrency.md#BKMK_TransactionCurrency_Team) one-to-many relationship for the [transactioncurrency](transactioncurrency.md) table/entity.

### <a name="BKMK_business_unit_teams"></a> business_unit_teams

See the [business_unit_teams](businessunit.md#BKMK_business_unit_teams) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_organization_teams"></a> organization_teams

See the [organization_teams](organization.md#BKMK_organization_teams) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_lk_team_modifiedonbehalfby"></a> lk_team_modifiedonbehalfby

See the [lk_team_modifiedonbehalfby](systemuser.md#BKMK_lk_team_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_team_createdonbehalfby"></a> lk_team_createdonbehalfby

See the [lk_team_createdonbehalfby](systemuser.md#BKMK_lk_team_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_delegatedauthorization"></a> team_delegatedauthorization

**Added by**: Delegated Authorization Solution

See the [team_delegatedauthorization](delegatedauthorization.md#BKMK_team_delegatedauthorization) one-to-many relationship for the [delegatedauthorization](delegatedauthorization.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the Team table is the first table in the relationship. Listed by **SchemaName**.

- [teamroles_association](#BKMK_teamroles_association)
- [teammembership_association](#BKMK_teammembership_association)
- [teamprofiles_association](#BKMK_teamprofiles_association)


### <a name="BKMK_teamroles_association"></a> teamroles_association

IntersectEntityName: teamroles<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|teamid|
|IsCustomizable|False|
|LogicalName|team|
|NavigationPropertyName|teamroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|role|
|IntersectAttribute|roleid|
|NavigationPropertyName|teamroles_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_teammembership_association"></a> teammembership_association

IntersectEntityName: teammembership<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|teamid|
|IsCustomizable|False|
|LogicalName|team|
|NavigationPropertyName|teammembership_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|systemuser|
|IntersectAttribute|systemuserid|
|NavigationPropertyName|teammembership_association|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |


### <a name="BKMK_teamprofiles_association"></a> teamprofiles_association

IntersectEntityName: teamprofiles<br />
#### Table 1

|Property|Value|
|--------|-----|
|IntersectAttribute|teamid|
|IsCustomizable|False|
|LogicalName|team|
|NavigationPropertyName|teamprofiles_association|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |

#### Table 2

|Property|Value|
|--------|-----|
|LogicalName|fieldsecurityprofile|
|IntersectAttribute|fieldsecurityprofileid|
|NavigationPropertyName|teamprofiles_association|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |


### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.team?text=team EntityType" />