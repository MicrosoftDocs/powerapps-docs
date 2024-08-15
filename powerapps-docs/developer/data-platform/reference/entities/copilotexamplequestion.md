---
title: "CopilotExampleQuestion table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the CopilotExampleQuestion table/entity."
ms.date: 06/04/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# CopilotExampleQuestion table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

CopilotExampleQuestions Component

**Added by**: msdyn_RelevanceSearch Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /copilotexamplequestions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /copilotexamplequestions<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /copilotexamplequestions(*copilotexamplequestionid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /copilotexamplequestions(*copilotexamplequestionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|CopilotExampleQuestions|
|DisplayCollectionName|CopilotExampleQuestions|
|DisplayName|CopilotExampleQuestion|
|EntitySetName|copilotexamplequestions|
|IsBPFEntity|False|
|LogicalCollectionName|copilotexamplequestions|
|LogicalName|copilotexamplequestion|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|copilotexamplequestionid|
|PrimaryNameAttribute|question|
|SchemaName|CopilotExampleQuestion|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppContext](#BKMK_AppContext)
- [Comment](#BKMK_Comment)
- [CopilotExampleQuestionId](#BKMK_CopilotExampleQuestionId)
- [CustomDimension](#BKMK_CustomDimension)
- [CustomField](#BKMK_CustomField)
- [EntityScope](#BKMK_EntityScope)
- [EntityScopeColumn](#BKMK_EntityScopeColumn)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [Knowledge](#BKMK_Knowledge)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [Question](#BKMK_Question)
- [Rephrase](#BKMK_Rephrase)
- [Skill](#BKMK_Skill)
- [SkillId](#BKMK_SkillId)
- [SQLCorrectness](#BKMK_SQLCorrectness)
- [StandardSQL](#BKMK_StandardSQL)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)


### <a name="BKMK_AppContext"></a> AppContext

|Property|Value|
|--------|-----|
|Description|AppContext for distinguishing between apps within the organization.|
|DisplayName|AppContext|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|appcontext|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Comment"></a> Comment

|Property|Value|
|--------|-----|
|Description|Explanation of the question.|
|DisplayName|Comment|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|comment|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CopilotExampleQuestionId"></a> CopilotExampleQuestionId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Copilot Example Question|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|copilotexamplequestionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_CustomDimension"></a> CustomDimension

|Property|Value|
|--------|-----|
|Description|CustomDimension.|
|DisplayName|CustomDimension|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customdimension|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CustomField"></a> CustomField

|Property|Value|
|--------|-----|
|Description|CustomField.|
|DisplayName|CustomField|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|customfield|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EntityScope"></a> EntityScope

|Property|Value|
|--------|-----|
|Description|EntityScope that can be used to extract results. Format: [entityscopeA], [entityscopeB]|
|DisplayName|EntityScope|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entityscope|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EntityScopeColumn"></a> EntityScopeColumn

|Property|Value|
|--------|-----|
|Description|EntityScopeColumn within the EntityScope specified above.Format: [EntityScopeA].[EntityScopeColumnA1], [EntityScopeB].[EntityScopeColumnB2]|
|DisplayName|EntityScopeColumn|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|entityscopecolumn|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Added by**: Basic Solution Solution

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


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_Knowledge"></a> Knowledge

|Property|Value|
|--------|-----|
|Description|The information and understanding that the model has acquired through its training data.|
|DisplayName|Knowledge|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|knowledge|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


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


### <a name="BKMK_Question"></a> Question

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Question|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|question|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_Rephrase"></a> Rephrase

|Property|Value|
|--------|-----|
|Description|Rephrase generated by NL2SQ.|
|DisplayName|Rephrase|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|rephrase|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Skill"></a> Skill

|Property|Value|
|--------|-----|
|Description|skill name for distinguishing between apps within the organization.|
|DisplayName|Skill|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|skill|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_SkillId"></a> SkillId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|SkillId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|skillid|
|RequiredLevel|None|
|Targets|dvtablesearch|
|Type|Lookup|


### <a name="BKMK_SQLCorrectness"></a> SQLCorrectness

|Property|Value|
|--------|-----|
|Description|Feedback by the maker after they validate the standard sql.|
|DisplayName|SQLCorrectness|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sqlcorrectness|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### SQLCorrectness Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Pending Validation||
|1|Valid||
|2|Invalid||
|3|NotSure||



### <a name="BKMK_StandardSQL"></a> StandardSQL

|Property|Value|
|--------|-----|
|Description|Updated by the NL2SQ service/ Maker. This is for the maker to validate.|
|DisplayName|Standard SQL|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|standardsql|
|MaxLength|20000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the CopilotExampleQuestion|
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
|Description|Reason for the status of the CopilotExampleQuestion|
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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [skillidName](#BKMK_skillidName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



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


### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Added by**: Active Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Added by**: Active Solution Solution

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


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Unique identifier for the business unit that owns the record|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_skillidName"></a> skillidName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|skillidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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

- [copilotexamplequestion_SyncErrors](#BKMK_copilotexamplequestion_SyncErrors)
- [copilotexamplequestion_AsyncOperations](#BKMK_copilotexamplequestion_AsyncOperations)
- [copilotexamplequestion_MailboxTrackingFolders](#BKMK_copilotexamplequestion_MailboxTrackingFolders)
- [copilotexamplequestion_ProcessSession](#BKMK_copilotexamplequestion_ProcessSession)
- [copilotexamplequestion_BulkDeleteFailures](#BKMK_copilotexamplequestion_BulkDeleteFailures)
- [copilotexamplequestion_PrincipalObjectAttributeAccesses](#BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses)


### <a name="BKMK_copilotexamplequestion_SyncErrors"></a> copilotexamplequestion_SyncErrors

**Added by**: System Solution Solution

Same as the [copilotexamplequestion_SyncErrors](syncerror.md#BKMK_copilotexamplequestion_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|copilotexamplequestion_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_copilotexamplequestion_AsyncOperations"></a> copilotexamplequestion_AsyncOperations

**Added by**: System Solution Solution

Same as the [copilotexamplequestion_AsyncOperations](asyncoperation.md#BKMK_copilotexamplequestion_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|copilotexamplequestion_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_copilotexamplequestion_MailboxTrackingFolders"></a> copilotexamplequestion_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [copilotexamplequestion_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_copilotexamplequestion_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|copilotexamplequestion_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_copilotexamplequestion_ProcessSession"></a> copilotexamplequestion_ProcessSession

**Added by**: System Solution Solution

Same as the [copilotexamplequestion_ProcessSession](processsession.md#BKMK_copilotexamplequestion_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|copilotexamplequestion_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_copilotexamplequestion_BulkDeleteFailures"></a> copilotexamplequestion_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [copilotexamplequestion_BulkDeleteFailures](bulkdeletefailure.md#BKMK_copilotexamplequestion_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|copilotexamplequestion_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses"></a> copilotexamplequestion_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [copilotexamplequestion_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_copilotexamplequestion_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|copilotexamplequestion_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_copilotexamplequestion_createdby](#BKMK_lk_copilotexamplequestion_createdby)
- [lk_copilotexamplequestion_createdonbehalfby](#BKMK_lk_copilotexamplequestion_createdonbehalfby)
- [lk_copilotexamplequestion_modifiedby](#BKMK_lk_copilotexamplequestion_modifiedby)
- [lk_copilotexamplequestion_modifiedonbehalfby](#BKMK_lk_copilotexamplequestion_modifiedonbehalfby)
- [organization_copilotexamplequestion](#BKMK_organization_copilotexamplequestion)
- [CopilotExampleQuestion_DVTableSearch](#BKMK_CopilotExampleQuestion_DVTableSearch)


### <a name="BKMK_lk_copilotexamplequestion_createdby"></a> lk_copilotexamplequestion_createdby

**Added by**: System Solution Solution

See the [lk_copilotexamplequestion_createdby](systemuser.md#BKMK_lk_copilotexamplequestion_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_copilotexamplequestion_createdonbehalfby"></a> lk_copilotexamplequestion_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_copilotexamplequestion_createdonbehalfby](systemuser.md#BKMK_lk_copilotexamplequestion_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_copilotexamplequestion_modifiedby"></a> lk_copilotexamplequestion_modifiedby

**Added by**: System Solution Solution

See the [lk_copilotexamplequestion_modifiedby](systemuser.md#BKMK_lk_copilotexamplequestion_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_copilotexamplequestion_modifiedonbehalfby"></a> lk_copilotexamplequestion_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_copilotexamplequestion_modifiedonbehalfby](systemuser.md#BKMK_lk_copilotexamplequestion_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_organization_copilotexamplequestion"></a> organization_copilotexamplequestion

**Added by**: System Solution Solution

See the [organization_copilotexamplequestion](organization.md#BKMK_organization_copilotexamplequestion) one-to-many relationship for the [organization](organization.md) table/entity.

### <a name="BKMK_CopilotExampleQuestion_DVTableSearch"></a> CopilotExampleQuestion_DVTableSearch

**Added by**: AIPlatformExtensionsComponents Solution Solution

See the [CopilotExampleQuestion_DVTableSearch](dvtablesearch.md#BKMK_CopilotExampleQuestion_DVTableSearch) one-to-many relationship for the [dvtablesearch](dvtablesearch.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.copilotexamplequestion?text=copilotexamplequestion EntityType" />