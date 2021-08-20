---
title: "msdyn_solutionhealthrule table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the msdyn_solutionhealthrule table/entity."
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

# msdyn_solutionhealthrule table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: Power Apps Checker Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules(*msdyn_solutionhealthruleid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules(*msdyn_solutionhealthruleid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref href="Microsoft.Dynamics.CRM.IsValidStateTransition?text=IsValidStateTransition Function" />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules(*msdyn_solutionhealthruleid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules(*msdyn_solutionhealthruleid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/msdyn_solutionhealthrules(*msdyn_solutionhealthruleid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_solutionhealthrules|
|DisplayCollectionName|Solution Health Rules|
|DisplayName|Solution Health Rule|
|EntitySetName|msdyn_solutionhealthrules|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_solutionhealthrules|
|LogicalName|msdyn_solutionhealthrule|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_solutionhealthruleid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_solutionhealthrule|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_ComponentType](#BKMK_msdyn_ComponentType)
- [msdyn_Description](#BKMK_msdyn_Description)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_OwningSolutionId](#BKMK_msdyn_OwningSolutionId)
- [msdyn_ResolutionAction](#BKMK_msdyn_ResolutionAction)
- [msdyn_resolutionmessage](#BKMK_msdyn_resolutionmessage)
- [msdyn_ResolutionType](#BKMK_msdyn_ResolutionType)
- [msdyn_solutionhealthruleId](#BKMK_msdyn_solutionhealthruleId)
- [msdyn_solutionhealthrulesetId](#BKMK_msdyn_solutionhealthrulesetId)
- [msdyn_uniquename](#BKMK_msdyn_uniquename)
- [msdyn_Workflow](#BKMK_msdyn_Workflow)
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


### <a name="BKMK_msdyn_ComponentType"></a> msdyn_ComponentType

|Property|Value|
|--------|-----|
|Description|Type of the Component being diagnosed like appmodule, sitemap, systemform etc.|
|DisplayName|Component Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_componenttype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_Description"></a> msdyn_Description

|Property|Value|
|--------|-----|
|Description|Rule description.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_description|
|MaxLength|2000|
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


### <a name="BKMK_msdyn_OwningSolutionId"></a> msdyn_OwningSolutionId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|OwningSolutionId|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_owningsolutionid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ResolutionAction"></a> msdyn_ResolutionAction

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ResolutionAction|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resolutionaction|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_msdyn_resolutionmessage"></a> msdyn_resolutionmessage

|Property|Value|
|--------|-----|
|Description|This message will be visible to end use when he/she tried to resolve rule failure.|
|DisplayName|Resolution Message|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resolutionmessage|
|MaxLength|2000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ResolutionType"></a> msdyn_ResolutionType

|Property|Value|
|--------|-----|
|Description|Type of Resolution action.|
|DisplayName|Resolution Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resolutiontype|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_ResolutionType Choices/Options

|Value|Label|
|-----|-----|
|192350000|Auto Heal|
|192350001|Customer Action Required|
|192350002|Documenation|
|192350003|None|



### <a name="BKMK_msdyn_solutionhealthruleId"></a> msdyn_solutionhealthruleId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Solution Health Rule|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_solutionhealthruleid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_solutionhealthrulesetId"></a> msdyn_solutionhealthrulesetId

|Property|Value|
|--------|-----|
|Description|Rule set to which the rule belongs to.|
|DisplayName|Solution Health Rule Set|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_solutionhealthrulesetid|
|RequiredLevel|Recommended|
|Targets|msdyn_solutionhealthruleset|
|Type|Lookup|


### <a name="BKMK_msdyn_uniquename"></a> msdyn_uniquename

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_uniquename|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_Workflow"></a> msdyn_Workflow

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Workflow|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_workflow|
|RequiredLevel|ApplicationRequired|
|Targets|workflow|
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
|Description|Status of the Solution Health Rule|
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
|Description|Reason for the status of the Solution Health Rule|
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
- [msdyn_resolutionactionName](#BKMK_msdyn_resolutionactionName)
- [msdyn_solutionhealthrulesetIdName](#BKMK_msdyn_solutionhealthrulesetIdName)
- [msdyn_WorkflowName](#BKMK_msdyn_WorkflowName)
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


### <a name="BKMK_msdyn_resolutionactionName"></a> msdyn_resolutionactionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_resolutionactionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_solutionhealthrulesetIdName"></a> msdyn_solutionhealthrulesetIdName

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


### <a name="BKMK_msdyn_WorkflowName"></a> msdyn_WorkflowName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_workflowname|
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

- [msdyn_solutionhealthrule_SyncErrors](#BKMK_msdyn_solutionhealthrule_SyncErrors)
- [msdyn_solutionhealthrule_DuplicateMatchingRecord](#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord)
- [msdyn_solutionhealthrule_DuplicateBaseRecord](#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord)
- [msdyn_solutionhealthrule_AsyncOperations](#BKMK_msdyn_solutionhealthrule_AsyncOperations)
- [msdyn_solutionhealthrule_MailboxTrackingFolders](#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders)
- [msdyn_solutionhealthrule_ProcessSession](#BKMK_msdyn_solutionhealthrule_ProcessSession)
- [msdyn_solutionhealthrule_BulkDeleteFailures](#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures)
- [msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses](#BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses)
- [msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule](#BKMK_msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule)


### <a name="BKMK_msdyn_solutionhealthrule_SyncErrors"></a> msdyn_solutionhealthrule_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [msdyn_solutionhealthrule_SyncErrors](syncerror.md#BKMK_msdyn_solutionhealthrule_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord"></a> msdyn_solutionhealthrule_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_solutionhealthrule_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_solutionhealthrule_DuplicateMatchingRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord"></a> msdyn_solutionhealthrule_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as duplicaterecord table [msdyn_solutionhealthrule_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_solutionhealthrule_DuplicateBaseRecord) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_AsyncOperations"></a> msdyn_solutionhealthrule_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [msdyn_solutionhealthrule_AsyncOperations](asyncoperation.md#BKMK_msdyn_solutionhealthrule_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders"></a> msdyn_solutionhealthrule_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [msdyn_solutionhealthrule_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_solutionhealthrule_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_ProcessSession"></a> msdyn_solutionhealthrule_ProcessSession

**Added by**: System Solution Solution

Same as processsession table [msdyn_solutionhealthrule_ProcessSession](processsession.md#BKMK_msdyn_solutionhealthrule_ProcessSession) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_BulkDeleteFailures"></a> msdyn_solutionhealthrule_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [msdyn_solutionhealthrule_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_solutionhealthrule_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses"></a> msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_solutionhealthrule_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule"></a> msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule

Same as msdyn_solutionhealthruleargument table [msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule](msdyn_solutionhealthruleargument.md#BKMK_msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthruleargument|
|ReferencingAttribute|msdyn_solutionhealthrule|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_msdyn_solutionhealthrule_msdyn_solutionhealthruleargument_SolutionHealthRule|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_solutionhealthrule_createdby](#BKMK_lk_msdyn_solutionhealthrule_createdby)
- [lk_msdyn_solutionhealthrule_createdonbehalfby](#BKMK_lk_msdyn_solutionhealthrule_createdonbehalfby)
- [lk_msdyn_solutionhealthrule_modifiedby](#BKMK_lk_msdyn_solutionhealthrule_modifiedby)
- [lk_msdyn_solutionhealthrule_modifiedonbehalfby](#BKMK_lk_msdyn_solutionhealthrule_modifiedonbehalfby)
- [user_msdyn_solutionhealthrule](#BKMK_user_msdyn_solutionhealthrule)
- [team_msdyn_solutionhealthrule](#BKMK_team_msdyn_solutionhealthrule)
- [business_unit_msdyn_solutionhealthrule](#BKMK_business_unit_msdyn_solutionhealthrule)
- [msdyn_msdyn_solutionhealthruleset_msdyn_solutio](#BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_solutio)
- [msdyn_workflow_msdyn_solutionhealthrule_Workflow](#BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow)
- [msdyn_workflow_msdyn_solutionhealthrule_resolutionaction](#BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction)


### <a name="BKMK_lk_msdyn_solutionhealthrule_createdby"></a> lk_msdyn_solutionhealthrule_createdby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_solutionhealthrule_createdby](systemuser.md#BKMK_lk_msdyn_solutionhealthrule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_solutionhealthrule_createdonbehalfby"></a> lk_msdyn_solutionhealthrule_createdonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_solutionhealthrule_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_solutionhealthrule_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_solutionhealthrule_modifiedby"></a> lk_msdyn_solutionhealthrule_modifiedby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_solutionhealthrule_modifiedby](systemuser.md#BKMK_lk_msdyn_solutionhealthrule_modifiedby) One-To-Many relationship.

### <a name="BKMK_lk_msdyn_solutionhealthrule_modifiedonbehalfby"></a> lk_msdyn_solutionhealthrule_modifiedonbehalfby

**Added by**: System Solution Solution

See systemuser Table [lk_msdyn_solutionhealthrule_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_solutionhealthrule_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_msdyn_solutionhealthrule"></a> user_msdyn_solutionhealthrule

**Added by**: System Solution Solution

See systemuser Table [user_msdyn_solutionhealthrule](systemuser.md#BKMK_user_msdyn_solutionhealthrule) One-To-Many relationship.

### <a name="BKMK_team_msdyn_solutionhealthrule"></a> team_msdyn_solutionhealthrule

**Added by**: System Solution Solution

See team Table [team_msdyn_solutionhealthrule](team.md#BKMK_team_msdyn_solutionhealthrule) One-To-Many relationship.

### <a name="BKMK_business_unit_msdyn_solutionhealthrule"></a> business_unit_msdyn_solutionhealthrule

**Added by**: System Solution Solution

See businessunit Table [business_unit_msdyn_solutionhealthrule](businessunit.md#BKMK_business_unit_msdyn_solutionhealthrule) One-To-Many relationship.

### <a name="BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_solutio"></a> msdyn_msdyn_solutionhealthruleset_msdyn_solutio

See msdyn_solutionhealthruleset Table [msdyn_msdyn_solutionhealthruleset_msdyn_solutio](msdyn_solutionhealthruleset.md#BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_solutio) One-To-Many relationship.

### <a name="BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow"></a> msdyn_workflow_msdyn_solutionhealthrule_Workflow

**Added by**: System Solution Solution

See workflow Table [msdyn_workflow_msdyn_solutionhealthrule_Workflow](workflow.md#BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow) One-To-Many relationship.

### <a name="BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction"></a> msdyn_workflow_msdyn_solutionhealthrule_resolutionaction

**Added by**: System Solution Solution

See workflow Table [msdyn_workflow_msdyn_solutionhealthrule_resolutionaction](workflow.md#BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.msdyn_solutionhealthrule?text=msdyn_solutionhealthrule EntityType" />