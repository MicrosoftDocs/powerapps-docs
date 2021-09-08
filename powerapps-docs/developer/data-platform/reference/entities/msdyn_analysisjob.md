---
title: "msdyn_analysisjob table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_analysisjob table/entity."
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

# msdyn_analysisjob table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Apps Checker Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/msdyn_analysisjobs(*msdyn_analysisjobid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_analysisjobs<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_analysisjobs<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/msdyn_analysisjobs(*msdyn_analysisjobid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_analysisjobs|
|DisplayCollectionName|Analysis Jobs|
|DisplayName|Analysis Job|
|EntitySetName|msdyn_analysisjobs|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_analysisjobs|
|LogicalName|msdyn_analysisjob|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_analysisjobid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_analysisjob|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_analysisjobId](#BKMK_msdyn_analysisjobId)
- [msdyn_CustomDetails](#BKMK_msdyn_CustomDetails)
- [msdyn_DisplayStatus](#BKMK_msdyn_DisplayStatus)
- [msdyn_EndTime](#BKMK_msdyn_EndTime)
- [msdyn_ErrorCount](#BKMK_msdyn_ErrorCount)
- [msdyn_Exception](#BKMK_msdyn_Exception)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_RuleFailCount](#BKMK_msdyn_RuleFailCount)
- [msdyn_RulePassCount](#BKMK_msdyn_RulePassCount)
- [msdyn_RuleRunCount](#BKMK_msdyn_RuleRunCount)
- [msdyn_RunCorrelationId](#BKMK_msdyn_RunCorrelationId)
- [msdyn_sevcriticalcount](#BKMK_msdyn_sevcriticalcount)
- [msdyn_sevhighcount](#BKMK_msdyn_sevhighcount)
- [msdyn_sevlowcount](#BKMK_msdyn_sevlowcount)
- [msdyn_sevmediumcount](#BKMK_msdyn_sevmediumcount)
- [msdyn_StartTime](#BKMK_msdyn_StartTime)
- [msdyn_SuggestionCount](#BKMK_msdyn_SuggestionCount)
- [msdyn_TenantId](#BKMK_msdyn_TenantId)
- [msdyn_TriggerType](#BKMK_msdyn_TriggerType)
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


### <a name="BKMK_msdyn_analysisjobId"></a> msdyn_analysisjobId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Analysis Job|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_analysisjobid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_CustomDetails"></a> msdyn_CustomDetails

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Custom Details|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_customdetails|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_DisplayStatus"></a> msdyn_DisplayStatus

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Display Status|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_displaystatus|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_EndTime"></a> msdyn_EndTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|End Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_endtime|
|RequiredLevel|None|
|Type|DateTime|


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


### <a name="BKMK_msdyn_Exception"></a> msdyn_Exception

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Exception|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_exception|
|MaxLength|10000|
|RequiredLevel|None|
|Type|Memo|


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
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


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


### <a name="BKMK_msdyn_RuleRunCount"></a> msdyn_RuleRunCount

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Rule Run Count|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_ruleruncount|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msdyn_RunCorrelationId"></a> msdyn_RunCorrelationId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Run Correlation Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_runcorrelationid|
|MaxLength|50|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_msdyn_StartTime"></a> msdyn_StartTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Start Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_starttime|
|RequiredLevel|None|
|Type|DateTime|


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


### <a name="BKMK_msdyn_TenantId"></a> msdyn_TenantId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Tenant Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_tenantid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_TriggerType"></a> msdyn_TriggerType

|Property|Value|
|--------|-----|
|Description|Health rule set Trigger Type.|
|DisplayName|Health rule set Trigger Type.|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_triggertype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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
|Description|Status of the Analysis Job|
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
|Description|Reason for the status of the Analysis Job|
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

- [msdyn_analysisjob_SyncErrors](#BKMK_msdyn_analysisjob_SyncErrors)
- [msdyn_analysisjob_DuplicateMatchingRecord](#BKMK_msdyn_analysisjob_DuplicateMatchingRecord)
- [msdyn_analysisjob_DuplicateBaseRecord](#BKMK_msdyn_analysisjob_DuplicateBaseRecord)
- [msdyn_analysisjob_AsyncOperations](#BKMK_msdyn_analysisjob_AsyncOperations)
- [msdyn_analysisjob_MailboxTrackingFolders](#BKMK_msdyn_analysisjob_MailboxTrackingFolders)
- [msdyn_analysisjob_ProcessSession](#BKMK_msdyn_analysisjob_ProcessSession)
- [msdyn_analysisjob_BulkDeleteFailures](#BKMK_msdyn_analysisjob_BulkDeleteFailures)
- [msdyn_analysisjob_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses)
- [msdyn_analysisjob_msdyn_analysiscomponent](#BKMK_msdyn_analysisjob_msdyn_analysiscomponent)
- [msdyn_analysisjob_msdyn_analysisresult](#BKMK_msdyn_analysisjob_msdyn_analysisresult)


### <a name="BKMK_msdyn_analysisjob_SyncErrors"></a> msdyn_analysisjob_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [msdyn_analysisjob_SyncErrors](syncerror.md#BKMK_msdyn_analysisjob_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_DuplicateMatchingRecord"></a> msdyn_analysisjob_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_analysisjob_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_analysisjob_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_DuplicateBaseRecord"></a> msdyn_analysisjob_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_analysisjob_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_analysisjob_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_AsyncOperations"></a> msdyn_analysisjob_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [msdyn_analysisjob_AsyncOperations](asyncoperation.md#BKMK_msdyn_analysisjob_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_MailboxTrackingFolders"></a> msdyn_analysisjob_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [msdyn_analysisjob_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_analysisjob_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_ProcessSession"></a> msdyn_analysisjob_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [msdyn_analysisjob_ProcessSession](processsession.md#BKMK_msdyn_analysisjob_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_BulkDeleteFailures"></a> msdyn_analysisjob_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [msdyn_analysisjob_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_analysisjob_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses"></a> msdyn_analysisjob_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [msdyn_analysisjob_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_analysisjob_msdyn_analysiscomponent"></a> msdyn_analysisjob_msdyn_analysiscomponent

Same as msdyn_analysiscomponent table [msdyn_analysisjob_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_msdyn_analysisjob_msdyn_analysiscomponent) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysiscomponent|
|ReferencingAttribute|msdyn_analysisjobid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_msdyn_analysiscomponent|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_msdyn_analysisjob_msdyn_analysisresult"></a> msdyn_analysisjob_msdyn_analysisresult

Same as msdyn_analysisresult table [msdyn_analysisjob_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_msdyn_analysisjob_msdyn_analysisresult) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_analysisresult|
|ReferencingAttribute|msdyn_analysisjobid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_analysisjob_msdyn_analysisresult|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_analysisjob_createdby](#BKMK_lk_msdyn_analysisjob_createdby)
- [lk_msdyn_analysisjob_createdonbehalfby](#BKMK_lk_msdyn_analysisjob_createdonbehalfby)
- [lk_msdyn_analysisjob_modifiedby](#BKMK_lk_msdyn_analysisjob_modifiedby)
- [lk_msdyn_analysisjob_modifiedonbehalfby](#BKMK_lk_msdyn_analysisjob_modifiedonbehalfby)
- [user_msdyn_analysisjob](#BKMK_user_msdyn_analysisjob)
- [team_msdyn_analysisjob](#BKMK_team_msdyn_analysisjob)
- [business_unit_msdyn_analysisjob](#BKMK_business_unit_msdyn_analysisjob)


### <a name="BKMK_lk_msdyn_analysisjob_createdby"></a> lk_msdyn_analysisjob_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_analysisjob_createdby](systemuser.md#BKMK_lk_msdyn_analysisjob_createdby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_analysisjob_createdonbehalfby"></a> lk_msdyn_analysisjob_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_analysisjob_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_analysisjob_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_analysisjob_modifiedby"></a> lk_msdyn_analysisjob_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_analysisjob_modifiedby](systemuser.md#BKMK_lk_msdyn_analysisjob_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_analysisjob_modifiedonbehalfby"></a> lk_msdyn_analysisjob_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_analysisjob_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_analysisjob_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_msdyn_analysisjob"></a> user_msdyn_analysisjob

**Added by**: System Solution Solution

See systemuser Table [user_msdyn_analysisjob](systemuser.md#BKMK_user_msdyn_analysisjob) One-To-Many relationship.

### <a name="BKMK_team_msdyn_analysisjob"></a> team_msdyn_analysisjob

**Added by**: System Solution Solution

See team Table [team_msdyn_analysisjob](team.md#BKMK_team_msdyn_analysisjob) One-To-Many relationship.

### <a name="BKMK_business_unit_msdyn_analysisjob"></a> business_unit_msdyn_analysisjob

**Added by**: System Solution Solution

See businessunit Table [business_unit_msdyn_analysisjob](businessunit.md#BKMK_business_unit_msdyn_analysisjob) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_analysisjob?text=msdyn_analysisjob EntityType" />