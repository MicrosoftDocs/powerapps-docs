---
title: "msdyn_knowledgearticletemplate table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_knowledgearticletemplate table/entity."
ms.date: 05/20/2021
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

# msdyn_knowledgearticletemplate table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Organizational Knowledge Article Template for Internal and external creation of Knowledge Articles.

**Added by**: Knowledge Management Features Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_knowledgearticletemplates(*msdyn_knowledgearticletemplateid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_knowledgearticletemplates|
|DisplayCollectionName|Knowledge Article Templates|
|DisplayName|Knowledge Article Template|
|EntitySetName|msdyn_knowledgearticletemplates|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_knowledgearticletemplates|
|LogicalName|msdyn_knowledgearticletemplate|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_knowledgearticletemplateid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_knowledgearticletemplate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_Content](#BKMK_msdyn_Content)
- [msdyn_Description](#BKMK_msdyn_Description)
- [msdyn_isinternal](#BKMK_msdyn_isinternal)
- [msdyn_keywords](#BKMK_msdyn_keywords)
- [msdyn_knowledgearticletemplateId](#BKMK_msdyn_knowledgearticletemplateId)
- [msdyn_languagelocaleid](#BKMK_msdyn_languagelocaleid)
- [msdyn_LanguageLocaleIdName](#BKMK_msdyn_LanguageLocaleIdName)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_subjectid](#BKMK_msdyn_subjectid)
- [msdyn_title](#BKMK_msdyn_title)
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


### <a name="BKMK_msdyn_Content"></a> msdyn_Content

|Property|Value|
|--------|-----|
|Description|Shows the body of the article stored in HTML format.|
|DisplayName|Content|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_content|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_Description"></a> msdyn_Description

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Description|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_description|
|MaxLength|155|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_isinternal"></a> msdyn_isinternal

|Property|Value|
|--------|-----|
|Description|Shows whether this article is only visible internally.|
|DisplayName|Internal|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_isinternal|
|RequiredLevel|None|
|Type|Boolean|

#### msdyn_isinternal Choices/Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_msdyn_keywords"></a> msdyn_keywords

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Keywords|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_keywords|
|MaxLength|4000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_knowledgearticletemplateId"></a> msdyn_knowledgearticletemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Knowledge Article Template|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_knowledgearticletemplateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_languagelocaleid"></a> msdyn_languagelocaleid

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Article Template Language Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_languagelocaleid|
|MaxLength|36|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_LanguageLocaleIdName"></a> msdyn_LanguageLocaleIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Article Language Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_LanguageLocaleIdName|
|MaxLength|320|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|Type a name for the Knowledge Article Template|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|4000|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_subjectid"></a> msdyn_subjectid

|Property|Value|
|--------|-----|
|Description|Choose the subject of the article to assist with article searches. You can configure subjects under Business Management in the Settings area.|
|DisplayName|Subject|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_subjectid|
|RequiredLevel|None|
|Targets|subject|
|Type|Lookup|


### <a name="BKMK_msdyn_title"></a> msdyn_title

|Property|Value|
|--------|-----|
|Description|Type a title for the Knowledge Article Template|
|DisplayName|Title|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_title|
|MaxLength|4000|
|RequiredLevel|None|
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
|Description|Status of the Knowledge Article Template|
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
|Description|Reason for the status of the Knowledge Article Template|
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
- [msdyn_subjectidName](#BKMK_msdyn_subjectidName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
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


### <a name="BKMK_msdyn_subjectidName"></a> msdyn_subjectidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_subjectidname|
|MaxLength|500|
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
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


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

- [msdyn_knowledgearticletemplate_SyncErrors](#BKMK_msdyn_knowledgearticletemplate_SyncErrors)
- [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord)
- [msdyn_knowledgearticletemplate_DuplicateBaseRecord](#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord)
- [msdyn_knowledgearticletemplate_SharePointDocumentLocations](#BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations)
- [msdyn_knowledgearticletemplate_AsyncOperations](#BKMK_msdyn_knowledgearticletemplate_AsyncOperations)
- [msdyn_knowledgearticletemplate_MailboxTrackingFolders](#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders)
- [msdyn_knowledgearticletemplate_ProcessSession](#BKMK_msdyn_knowledgearticletemplate_ProcessSession)
- [msdyn_knowledgearticletemplate_BulkDeleteFailures](#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures)
- [msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses)
- [msdyn_knowledgearticletemplate_QueueItems](#BKMK_msdyn_knowledgearticletemplate_QueueItems)


### <a name="BKMK_msdyn_knowledgearticletemplate_SyncErrors"></a> msdyn_knowledgearticletemplate_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [msdyn_knowledgearticletemplate_SyncErrors](syncerror.md#BKMK_msdyn_knowledgearticletemplate_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord"></a> msdyn_knowledgearticletemplate_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_knowledgearticletemplate_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_knowledgearticletemplate_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord"></a> msdyn_knowledgearticletemplate_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_knowledgearticletemplate_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_knowledgearticletemplate_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations"></a> msdyn_knowledgearticletemplate_SharePointDocumentLocations

**Added by**: System Solution Solution

Same as sharepointdocumentlocation table [msdyn_knowledgearticletemplate_SharePointDocumentLocations](sharepointdocumentlocation.md#BKMK_msdyn_knowledgearticletemplate_SharePointDocumentLocations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sharepointdocumentlocation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_SharePointDocumentLocations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_AsyncOperations"></a> msdyn_knowledgearticletemplate_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [msdyn_knowledgearticletemplate_AsyncOperations](asyncoperation.md#BKMK_msdyn_knowledgearticletemplate_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders"></a> msdyn_knowledgearticletemplate_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [msdyn_knowledgearticletemplate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_knowledgearticletemplate_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_ProcessSession"></a> msdyn_knowledgearticletemplate_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [msdyn_knowledgearticletemplate_ProcessSession](processsession.md#BKMK_msdyn_knowledgearticletemplate_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures"></a> msdyn_knowledgearticletemplate_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [msdyn_knowledgearticletemplate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_knowledgearticletemplate_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses"></a> msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_knowledgearticletemplate_QueueItems"></a> msdyn_knowledgearticletemplate_QueueItems

**Added by**: System Solution Solution

Same as queueitem table [msdyn_knowledgearticletemplate_QueueItems](queueitem.md#BKMK_msdyn_knowledgearticletemplate_QueueItems) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|queueitem|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_knowledgearticletemplate_QueueItems|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_knowledgearticletemplate_createdby](#BKMK_lk_msdyn_knowledgearticletemplate_createdby)
- [lk_msdyn_knowledgearticletemplate_createdonbehalfby](#BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby)
- [lk_msdyn_knowledgearticletemplate_modifiedby](#BKMK_lk_msdyn_knowledgearticletemplate_modifiedby)
- [lk_msdyn_knowledgearticletemplate_modifiedonbehalfby](#BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby)
- [user_msdyn_knowledgearticletemplate](#BKMK_user_msdyn_knowledgearticletemplate)
- [team_msdyn_knowledgearticletemplate](#BKMK_team_msdyn_knowledgearticletemplate)
- [business_unit_msdyn_knowledgearticletemplate](#BKMK_business_unit_msdyn_knowledgearticletemplate)
- [msdyn_subject_knowledgearticletemplate_subjectid](#BKMK_msdyn_subject_knowledgearticletemplate_subjectid)


### <a name="BKMK_lk_msdyn_knowledgearticletemplate_createdby"></a> lk_msdyn_knowledgearticletemplate_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgearticletemplate_createdby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_createdby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby"></a> lk_msdyn_knowledgearticletemplate_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgearticletemplate_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_modifiedby"></a> lk_msdyn_knowledgearticletemplate_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgearticletemplate_modifiedby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby"></a> lk_msdyn_knowledgearticletemplate_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_knowledgearticletemplate_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_knowledgearticletemplate_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_msdyn_knowledgearticletemplate"></a> user_msdyn_knowledgearticletemplate

**Added by**: System Solution Solution

See systemuser Table [user_msdyn_knowledgearticletemplate](systemuser.md#BKMK_user_msdyn_knowledgearticletemplate) One-To-Many relationship.

### <a name="BKMK_team_msdyn_knowledgearticletemplate"></a> team_msdyn_knowledgearticletemplate

**Added by**: System Solution Solution

See team Table [team_msdyn_knowledgearticletemplate](team.md#BKMK_team_msdyn_knowledgearticletemplate) One-To-Many relationship.

### <a name="BKMK_business_unit_msdyn_knowledgearticletemplate"></a> business_unit_msdyn_knowledgearticletemplate

**Added by**: System Solution Solution

See businessunit Table [business_unit_msdyn_knowledgearticletemplate](businessunit.md#BKMK_business_unit_msdyn_knowledgearticletemplate) One-To-Many relationship.

### <a name="BKMK_msdyn_subject_knowledgearticletemplate_subjectid"></a> msdyn_subject_knowledgearticletemplate_subjectid

**Added by**: System Solution Solution

See subject Table [msdyn_subject_knowledgearticletemplate_subjectid](subject.md#BKMK_msdyn_subject_knowledgearticletemplate_subjectid) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_knowledgearticletemplate?text=msdyn_knowledgearticletemplate EntityType" />