---
title: "msdyn_analysiscomponent table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_analysiscomponent table/entity."
ms.date: 06/06/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_analysiscomponent table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Apps Checker Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msdyn_analysiscomponents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msdyn_analysiscomponents<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_analysiscomponents|
|DisplayCollectionName|Analysis Components|
|DisplayName|Analysis Component|
|EntitySetName|msdyn_analysiscomponents|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_analysiscomponents|
|LogicalName|msdyn_analysiscomponent|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_analysiscomponentid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_analysiscomponent|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_analysiscomponentId](#BKMK_msdyn_analysiscomponentId)
- [msdyn_AnalysisComponentType](#BKMK_msdyn_AnalysisComponentType)
- [msdyn_AnalysisJobId](#BKMK_msdyn_AnalysisJobId)
- [msdyn_ComponentId](#BKMK_msdyn_ComponentId)
- [msdyn_ComponentName](#BKMK_msdyn_ComponentName)
- [msdyn_ComponentType](#BKMK_msdyn_ComponentType)
- [msdyn_ComponentVersion](#BKMK_msdyn_ComponentVersion)
- [msdyn_ErrorCount](#BKMK_msdyn_ErrorCount)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_RetryCount](#BKMK_msdyn_RetryCount)
- [msdyn_RuleFailCount](#BKMK_msdyn_RuleFailCount)
- [msdyn_RulePassCount](#BKMK_msdyn_RulePassCount)
- [msdyn_RulePassRate](#BKMK_msdyn_RulePassRate)
- [msdyn_sevcriticalcount](#BKMK_msdyn_sevcriticalcount)
- [msdyn_sevhighcount](#BKMK_msdyn_sevhighcount)
- [msdyn_sevlowcount](#BKMK_msdyn_sevlowcount)
- [msdyn_sevmediumcount](#BKMK_msdyn_sevmediumcount)
- [msdyn_SolutionHealthRuleSetId](#BKMK_msdyn_SolutionHealthRuleSetId)
- [msdyn_SuggestionCount](#BKMK_msdyn_SuggestionCount)
- [msdyn_WarningCount](#BKMK_msdyn_WarningCount)
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


### <a name="BKMK_msdyn_analysiscomponentId"></a> msdyn_analysiscomponentId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Analysis Component|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_analysiscomponentid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_AnalysisComponentType"></a> msdyn_AnalysisComponentType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Analysis Component Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_analysiscomponenttype|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### msdyn_AnalysisComponentType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|192350000|Organization Health||
|192350001|Component Health||
|192350002|Object Health||



### <a name="BKMK_msdyn_AnalysisJobId"></a> msdyn_AnalysisJobId

|Property|Value|
|--------|-----|
|Description|The parent Analysis Job that analyzed this particular Analysis Component.|
|DisplayName|Analysis Job|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_analysisjobid|
|RequiredLevel|None|
|Targets|msdyn_analysisjob|
|Type|Lookup|


### <a name="BKMK_msdyn_ComponentId"></a> msdyn_ComponentId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componentid|
|MaxLength|50|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_ComponentName"></a> msdyn_ComponentName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componentname|
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_ComponentType"></a> msdyn_ComponentType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componenttype|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### msdyn_ComponentType Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|192350000|Solution||
|192350001|Entity||
|192350002|View||
|192350003|Form||
|192350004|Plugin||
|192350005|Configuration||



### <a name="BKMK_msdyn_ComponentVersion"></a> msdyn_ComponentVersion

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Component Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componentversion|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ErrorCount"></a> msdyn_ErrorCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Error Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_errorcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|--------|-----|
|Description|The name of the custom entity.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|200|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_RetryCount"></a> msdyn_RetryCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Retry Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_retrycount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_RuleFailCount"></a> msdyn_RuleFailCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Rule Fail Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_rulefailcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_RulePassCount"></a> msdyn_RulePassCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Rule Pass Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_rulepasscount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_RulePassRate"></a> msdyn_RulePassRate

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Rule Pass Rate|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_rulepassrate|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_sevcriticalcount"></a> msdyn_sevcriticalcount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Critical Severity Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_sevcriticalcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_sevhighcount"></a> msdyn_sevhighcount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|High Severity Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_sevhighcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_sevlowcount"></a> msdyn_sevlowcount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Low Severity Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_sevlowcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_sevmediumcount"></a> msdyn_sevmediumcount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Medium Severity Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_sevmediumcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_SolutionHealthRuleSetId"></a> msdyn_SolutionHealthRuleSetId

|Property|Value|
|--------|-----|
|Description|The Solution Health Rule Set for which this is analysis component is for.|
|DisplayName|Solution Health Rule Set|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_solutionhealthrulesetid|
|RequiredLevel|None|
|Targets|msdyn_solutionhealthruleset|
|Type|Lookup|


### <a name="BKMK_msdyn_SuggestionCount"></a> msdyn_SuggestionCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Suggestion Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_suggestioncount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_WarningCount"></a> msdyn_WarningCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Warning Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_warningcount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


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
|Description|Status of the Analysis Component|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### statecode Choices/Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Active|192350000|Active|
|1|Inactive|2|Inactive|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the Analysis Component|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|1|Pending|0|
|2|Canceled|1|
|192350000|Running|0|
|192350001|Complete|0|
|192350002|Exception|0|
|192350003|Completed With Exceptions|0|



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
- [msdyn_AnalysisJobIdName](#BKMK_msdyn_AnalysisJobIdName)
- [msdyn_SolutionHealthRuleSetIdName](#BKMK_msdyn_SolutionHealthRuleSetIdName)
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


### <a name="BKMK_msdyn_AnalysisJobIdName"></a> msdyn_AnalysisJobIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_analysisjobidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_SolutionHealthRuleSetIdName"></a> msdyn_SolutionHealthRuleSetIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_solutionhealthrulesetidname|
|MaxLength|100|
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

- [msdyn_analysiscomponent_SyncErrors](#BKMK_msdyn_analysiscomponent_SyncErrors)
- [msdyn_analysiscomponent_DuplicateMatchingRecord](#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord)
- [msdyn_analysiscomponent_DuplicateBaseRecord](#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord)
- [msdyn_analysiscomponent_AsyncOperations](#BKMK_msdyn_analysiscomponent_AsyncOperations)
- [msdyn_analysiscomponent_MailboxTrackingFolders](#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)
- [msdyn_analysiscomponent_ProcessSession](#BKMK_msdyn_analysiscomponent_ProcessSession)
- [msdyn_analysiscomponent_BulkDeleteFailures](#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)
- [msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses)
- [msdyn_analysiscomponent_msdyn_analysisresult](#BKMK_msdyn_analysiscomponent_msdyn_analysisresult)


### <a name="BKMK_msdyn_analysiscomponent_SyncErrors"></a> msdyn_analysiscomponent_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_SyncErrors](syncerror.md#BKMK_msdyn_analysiscomponent_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord"></a> msdyn_analysiscomponent_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_DuplicateBaseRecord"></a> msdyn_analysiscomponent_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_AsyncOperations"></a> msdyn_analysiscomponent_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_AsyncOperations](asyncoperation.md#BKMK_msdyn_analysiscomponent_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_MailboxTrackingFolders"></a> msdyn_analysiscomponent_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_ProcessSession"></a> msdyn_analysiscomponent_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_ProcessSession](processsession.md#BKMK_msdyn_analysiscomponent_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_BulkDeleteFailures"></a> msdyn_analysiscomponent_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_analysiscomponent_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses"></a> msdyn_analysiscomponent_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysiscomponent_msdyn_analysisresult"></a> msdyn_analysiscomponent_msdyn_analysisresult

Same as the [msdyn_analysiscomponent_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_msdyn_analysiscomponent_msdyn_analysisresult) many-to-one relationship for the [msdyn_analysisresult](msdyn_analysisresult.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|msdyn_analysiscomponentid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_analysiscomponent_msdyn_analysisresult|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_analysiscomponent_createdby](#BKMK_lk_msdyn_analysiscomponent_createdby)
- [lk_msdyn_analysiscomponent_createdonbehalfby](#BKMK_lk_msdyn_analysiscomponent_createdonbehalfby)
- [lk_msdyn_analysiscomponent_modifiedby](#BKMK_lk_msdyn_analysiscomponent_modifiedby)
- [lk_msdyn_analysiscomponent_modifiedonbehalfby](#BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby)
- [user_msdyn_analysiscomponent](#BKMK_user_msdyn_analysiscomponent)
- [team_msdyn_analysiscomponent](#BKMK_team_msdyn_analysiscomponent)
- [business_unit_msdyn_analysiscomponent](#BKMK_business_unit_msdyn_analysiscomponent)
- [msdyn_analysisjob_msdyn_analysiscomponent](#BKMK_msdyn_analysisjob_msdyn_analysiscomponent)
- [msdyn_msdyn_solutionhealthruleset_msdyn_analysi](#BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_analysi)


### <a name="BKMK_lk_msdyn_analysiscomponent_createdby"></a> lk_msdyn_analysiscomponent_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_analysiscomponent_createdby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_analysiscomponent_createdonbehalfby"></a> lk_msdyn_analysiscomponent_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_analysiscomponent_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_analysiscomponent_modifiedby"></a> lk_msdyn_analysiscomponent_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_analysiscomponent_modifiedby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby"></a> lk_msdyn_analysiscomponent_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_analysiscomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_analysiscomponent"></a> user_msdyn_analysiscomponent

**Added by**: System Solution Solution

See the [user_msdyn_analysiscomponent](systemuser.md#BKMK_user_msdyn_analysiscomponent) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_analysiscomponent"></a> team_msdyn_analysiscomponent

**Added by**: System Solution Solution

See the [team_msdyn_analysiscomponent](team.md#BKMK_team_msdyn_analysiscomponent) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_analysiscomponent"></a> business_unit_msdyn_analysiscomponent

**Added by**: System Solution Solution

See the [business_unit_msdyn_analysiscomponent](businessunit.md#BKMK_business_unit_msdyn_analysiscomponent) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msdyn_analysisjob_msdyn_analysiscomponent"></a> msdyn_analysisjob_msdyn_analysiscomponent

See the [msdyn_analysisjob_msdyn_analysiscomponent](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_msdyn_analysiscomponent) one-to-many relationship for the [msdyn_analysisjob](msdyn_analysisjob.md) table/entity.

### <a name="BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_analysi"></a> msdyn_msdyn_solutionhealthruleset_msdyn_analysi

See the [msdyn_msdyn_solutionhealthruleset_msdyn_analysi](msdyn_solutionhealthruleset.md#BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_analysi) one-to-many relationship for the [msdyn_solutionhealthruleset](msdyn_solutionhealthruleset.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_analysiscomponent?text=msdyn_analysiscomponent EntityType" />