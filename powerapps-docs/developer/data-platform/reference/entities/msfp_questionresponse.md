---
title: "Customer Voice survey question response (msfp_questionresponse)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Customer Voice survey question response (msfp_questionresponse)  table/entity."
ms.date: 10/27/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Customer Voice survey question response (msfp_questionresponse)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Response to a question in a survey.

**Added by**: Dynamics 365 Customer Voice Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msfp_questionresponses(*msfp_questionresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msfp_questionresponses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple|<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msfp_questionresponses(*msfp_questionresponseid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msfp_questionresponses(*msfp_questionresponseid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msfp_questionresponses<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msfp_questionresponses(*msfp_questionresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msfp_questionresponses(*msfp_questionresponseid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple|<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msfp_questionresponses|
|DisplayCollectionName|Customer Voice survey question responses|
|DisplayName|Customer Voice survey question response|
|EntitySetName|msfp_questionresponses|
|IsBPFEntity|False|
|LogicalCollectionName|msfp_questionresponses|
|LogicalName|msfp_questionresponse|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msfp_questionresponseid|
|PrimaryNameAttribute|msfp_name|
|SchemaName|msfp_questionresponse|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_keyphrases](#BKMK_msfp_keyphrases)
- [msfp_name](#BKMK_msfp_name)
- [msfp_otherproperties](#BKMK_msfp_otherproperties)
- [msfp_questionid](#BKMK_msfp_questionid)
- [msfp_questionresponseId](#BKMK_msfp_questionresponseId)
- [msfp_response](#BKMK_msfp_response)
- [msfp_Sentimentvalue](#BKMK_msfp_Sentimentvalue)
- [msfp_sourcequestionidentifier](#BKMK_msfp_sourcequestionidentifier)
- [msfp_sourceresponseidentifier](#BKMK_msfp_sourceresponseidentifier)
- [msfp_sourcesurveyidentifier](#BKMK_msfp_sourcesurveyidentifier)
- [msfp_surveyresponseid](#BKMK_msfp_surveyresponseid)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|--------|-----|
|Description|Sequence number of the import that created this record.|
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


### <a name="BKMK_msfp_keyphrases"></a> msfp_keyphrases

|Property|Value|
|--------|-----|
|Description|Stores key Phrases from text response.|
|DisplayName|Key phrases|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_keyphrases|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_name"></a> msfp_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msfp_otherproperties"></a> msfp_otherproperties

|Property|Value|
|--------|-----|
|Description|Other question response properties in JSON format.|
|DisplayName|Other properties|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_otherproperties|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_questionid"></a> msfp_questionid

|Property|Value|
|--------|-----|
|Description|Question associated with the question response.|
|DisplayName|Question|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_questionid|
|RequiredLevel|None|
|Targets|msfp_question|
|Type|Lookup|


### <a name="BKMK_msfp_questionresponseId"></a> msfp_questionresponseId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Survey question response|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msfp_questionresponseid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msfp_response"></a> msfp_response

|Property|Value|
|--------|-----|
|Description|Question response value as string.|
|DisplayName|Response|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_response|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_Sentimentvalue"></a> msfp_Sentimentvalue

|Property|Value|
|--------|-----|
|Description|Sentiment of the question response.|
|DisplayName|Sentiment value|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_sentimentvalue|
|MaxValue|100000000000|
|MinValue|-100000000000|
|Precision|2|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_msfp_sourcequestionidentifier"></a> msfp_sourcequestionidentifier

|Property|Value|
|--------|-----|
|Description|Unique identifier for the question in the source application.|
|DisplayName|Source question identifier|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_sourcequestionidentifier|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_sourceresponseidentifier"></a> msfp_sourceresponseidentifier

|Property|Value|
|--------|-----|
|Description|Unique identifier for the response in the source application.|
|DisplayName|Source response identifier|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_sourceresponseidentifier|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_sourcesurveyidentifier"></a> msfp_sourcesurveyidentifier

|Property|Value|
|--------|-----|
|Description|Unique identifier for the survey in the source application.|
|DisplayName|Source survey identifier|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_sourcesurveyidentifier|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_surveyresponseid"></a> msfp_surveyresponseid

|Property|Value|
|--------|-----|
|Description|Survey response associated with the question response.|
|DisplayName|Survey response|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_surveyresponseid|
|RequiredLevel|None|
|Targets|msfp_surveyresponse|
|Type|Lookup|


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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser,team|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Owner Id Type|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the Survey question response|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|1|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Survey question response|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Active|0|
|2|Inactive|1|



### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Time Zone Rule Version Number|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|timezoneruleversionnumber|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|--------|-----|
|Description|Time zone code that was in use when the record was created.|
|DisplayName|UTC Conversion Time Zone Code|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|utcconversiontimezonecode|
|MaxValue|2147483647|
|MinValue|-1|
|RequiredLevel|None|
|Type|Integer|

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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msfp_questionidName](#BKMK_msfp_questionidName)
- [msfp_surveyresponseidName](#BKMK_msfp_surveyresponseidName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the record.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the record.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who modified the record.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the record was modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who modified the record.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Added by**: Active Solution Solution

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

**Added by**: Active Solution Solution

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_msfp_questionidName"></a> msfp_questionidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_questionidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_surveyresponseidName"></a> msfp_surveyresponseidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_surveyresponseidname|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Name of the owner|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Yomi name of the owner|
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

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunitname|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the team that owns the record.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the user that owns the record.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Version Number|
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

- [msfp_questionresponse_SyncErrors](#BKMK_msfp_questionresponse_SyncErrors)
- [msfp_questionresponse_AsyncOperations](#BKMK_msfp_questionresponse_AsyncOperations)
- [msfp_questionresponse_MailboxTrackingFolders](#BKMK_msfp_questionresponse_MailboxTrackingFolders)
- [msfp_questionresponse_ProcessSession](#BKMK_msfp_questionresponse_ProcessSession)
- [msfp_questionresponse_BulkDeleteFailures](#BKMK_msfp_questionresponse_BulkDeleteFailures)
- [msfp_questionresponse_PrincipalObjectAttributeAccesses](#BKMK_msfp_questionresponse_PrincipalObjectAttributeAccesses)
- [msfp_msfp_questionresponse_msfp_fileresponse_questionresponse](#BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse)


### <a name="BKMK_msfp_questionresponse_SyncErrors"></a> msfp_questionresponse_SyncErrors

**Added by**: System Solution Solution

Same as the [msfp_questionresponse_SyncErrors](syncerror.md#BKMK_msfp_questionresponse_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_questionresponse_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_questionresponse_AsyncOperations"></a> msfp_questionresponse_AsyncOperations

**Added by**: System Solution Solution

Same as the [msfp_questionresponse_AsyncOperations](asyncoperation.md#BKMK_msfp_questionresponse_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_questionresponse_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_questionresponse_MailboxTrackingFolders"></a> msfp_questionresponse_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msfp_questionresponse_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_questionresponse_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_questionresponse_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_questionresponse_ProcessSession"></a> msfp_questionresponse_ProcessSession

**Added by**: System Solution Solution

Same as the [msfp_questionresponse_ProcessSession](processsession.md#BKMK_msfp_questionresponse_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_questionresponse_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_questionresponse_BulkDeleteFailures"></a> msfp_questionresponse_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msfp_questionresponse_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_questionresponse_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_questionresponse_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_questionresponse_PrincipalObjectAttributeAccesses"></a> msfp_questionresponse_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msfp_questionresponse_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_questionresponse_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_questionresponse_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse"></a> msfp_msfp_questionresponse_msfp_fileresponse_questionresponse

Same as the [msfp_msfp_questionresponse_msfp_fileresponse_questionresponse](msfp_fileresponse.md#BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse) many-to-one relationship for the [msfp_fileresponse](msfp_fileresponse.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msfp_fileresponse|
|ReferencingAttribute|msfp_questionresponse|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_msfp_questionresponse_msfp_fileresponse_questionresponse|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msfp_questionresponse_createdby](#BKMK_lk_msfp_questionresponse_createdby)
- [lk_msfp_questionresponse_createdonbehalfby](#BKMK_lk_msfp_questionresponse_createdonbehalfby)
- [lk_msfp_questionresponse_modifiedby](#BKMK_lk_msfp_questionresponse_modifiedby)
- [lk_msfp_questionresponse_modifiedonbehalfby](#BKMK_lk_msfp_questionresponse_modifiedonbehalfby)
- [user_msfp_questionresponse](#BKMK_user_msfp_questionresponse)
- [team_msfp_questionresponse](#BKMK_team_msfp_questionresponse)
- [business_unit_msfp_questionresponse](#BKMK_business_unit_msfp_questionresponse)
- [msfp_msfp_question_msfp_questionresponse_questionid](#BKMK_msfp_msfp_question_msfp_questionresponse_questionid)
- [msfp_msfp_surveyresponse_msfp_questionresponse_surveyresponseid](#BKMK_msfp_msfp_surveyresponse_msfp_questionresponse_surveyresponseid)


### <a name="BKMK_lk_msfp_questionresponse_createdby"></a> lk_msfp_questionresponse_createdby

**Added by**: System Solution Solution

See the [lk_msfp_questionresponse_createdby](systemuser.md#BKMK_lk_msfp_questionresponse_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_questionresponse_createdonbehalfby"></a> lk_msfp_questionresponse_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_questionresponse_createdonbehalfby](systemuser.md#BKMK_lk_msfp_questionresponse_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_questionresponse_modifiedby"></a> lk_msfp_questionresponse_modifiedby

**Added by**: System Solution Solution

See the [lk_msfp_questionresponse_modifiedby](systemuser.md#BKMK_lk_msfp_questionresponse_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_questionresponse_modifiedonbehalfby"></a> lk_msfp_questionresponse_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_questionresponse_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_questionresponse_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msfp_questionresponse"></a> user_msfp_questionresponse

**Added by**: System Solution Solution

See the [user_msfp_questionresponse](systemuser.md#BKMK_user_msfp_questionresponse) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msfp_questionresponse"></a> team_msfp_questionresponse

**Added by**: System Solution Solution

See the [team_msfp_questionresponse](team.md#BKMK_team_msfp_questionresponse) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msfp_questionresponse"></a> business_unit_msfp_questionresponse

**Added by**: System Solution Solution

See the [business_unit_msfp_questionresponse](businessunit.md#BKMK_business_unit_msfp_questionresponse) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msfp_msfp_question_msfp_questionresponse_questionid"></a> msfp_msfp_question_msfp_questionresponse_questionid

See the [msfp_msfp_question_msfp_questionresponse_questionid](msfp_question.md#BKMK_msfp_msfp_question_msfp_questionresponse_questionid) one-to-many relationship for the [msfp_question](msfp_question.md) table/entity.

### <a name="BKMK_msfp_msfp_surveyresponse_msfp_questionresponse_surveyresponseid"></a> msfp_msfp_surveyresponse_msfp_questionresponse_surveyresponseid

**Added by**: Active Solution Solution

See the [msfp_msfp_surveyresponse_msfp_questionresponse_surveyresponseid](msfp_surveyresponse.md#BKMK_msfp_msfp_surveyresponse_msfp_questionresponse_surveyresponseid) one-to-many relationship for the [msfp_surveyresponse](msfp_surveyresponse.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msfp_questionresponse?text=msfp_questionresponse EntityType" />