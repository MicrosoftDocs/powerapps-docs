---
title: "Customer Voice survey email template (msfp_emailtemplate)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Customer Voice survey email template (msfp_emailtemplate)  table/entity."
ms.date: 10/27/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Customer Voice survey email template (msfp_emailtemplate)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Template for an email message that contains the survey invitation link.

**Added by**: Dynamics 365 Customer Voice Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msfp_emailtemplates(*msfp_emailtemplateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msfp_emailtemplates<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple|<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msfp_emailtemplates(*msfp_emailtemplateid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msfp_emailtemplates(*msfp_emailtemplateid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msfp_emailtemplates<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msfp_emailtemplates(*msfp_emailtemplateid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msfp_emailtemplates(*msfp_emailtemplateid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple|<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msfp_emailtemplates|
|DisplayCollectionName|Customer Voice survey email templates|
|DisplayName|Customer Voice survey email template|
|EntitySetName|msfp_emailtemplates|
|IsBPFEntity|False|
|LogicalCollectionName|msfp_emailtemplates|
|LogicalName|msfp_emailtemplate|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msfp_emailtemplateid|
|PrimaryNameAttribute|msfp_name|
|SchemaName|msfp_emailtemplate|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_Candelete](#BKMK_msfp_Candelete)
- [msfp_Canedit](#BKMK_msfp_Canedit)
- [msfp_Canrename](#BKMK_msfp_Canrename)
- [msfp_emailtemplatebody](#BKMK_msfp_emailtemplatebody)
- [msfp_emailtemplateId](#BKMK_msfp_emailtemplateId)
- [msfp_emailtemplatesubject](#BKMK_msfp_emailtemplatesubject)
- [msfp_language](#BKMK_msfp_language)
- [msfp_name](#BKMK_msfp_name)
- [msfp_sourcesurveyidentifier](#BKMK_msfp_sourcesurveyidentifier)
- [msfp_survey](#BKMK_msfp_survey)
- [msfp_tags](#BKMK_msfp_tags)
- [msfp_templatetype](#BKMK_msfp_templatetype)
- [msfp_version](#BKMK_msfp_version)
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


### <a name="BKMK_msfp_Candelete"></a> msfp_Candelete

|Property|Value|
|--------|-----|
|Description|Specifies if the email template can be deleted.|
|DisplayName|Is deletable|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_candelete|
|RequiredLevel|None|
|Type|Boolean|

#### msfp_Candelete Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_msfp_Canedit"></a> msfp_Canedit

|Property|Value|
|--------|-----|
|Description|Specifies if the email template can be edited.|
|DisplayName|Is editable|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_canedit|
|RequiredLevel|None|
|Type|Boolean|

#### msfp_Canedit Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_msfp_Canrename"></a> msfp_Canrename

|Property|Value|
|--------|-----|
|Description|Specifies if the email template can be renamed.|
|DisplayName|Is renamable|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_canrename|
|RequiredLevel|None|
|Type|Boolean|

#### msfp_Canrename Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 1



### <a name="BKMK_msfp_emailtemplatebody"></a> msfp_emailtemplatebody

|Property|Value|
|--------|-----|
|Description|Stores body of the email template.|
|DisplayName|Email template body|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_emailtemplatebody|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_emailtemplateId"></a> msfp_emailtemplateId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Survey email template|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msfp_emailtemplateid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msfp_emailtemplatesubject"></a> msfp_emailtemplatesubject

|Property|Value|
|--------|-----|
|Description|Stores subject of the email template.|
|DisplayName|Email template subject|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_emailtemplatesubject|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_language"></a> msfp_language

|Property|Value|
|--------|-----|
|Description|Language of the email message template|
|DisplayName|Language|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_language|
|MaxLength|400|
|RequiredLevel|None|
|Type|String|


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
|MaxLength|250|
|RequiredLevel|ApplicationRequired|
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


### <a name="BKMK_msfp_survey"></a> msfp_survey

|Property|Value|
|--------|-----|
|Description|Unique identifier for Customer Voice survey associated with Customer Voice survey email template.|
|DisplayName|survey email template|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_survey|
|RequiredLevel|None|
|Targets|msfp_survey|
|Type|Lookup|


### <a name="BKMK_msfp_tags"></a> msfp_tags

|Property|Value|
|--------|-----|
|Description|Stores tags added to the email template.|
|DisplayName|Tags|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_tags|
|MaxLength|1000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_templatetype"></a> msfp_templatetype

|Property|Value|
|--------|-----|
|Description|Determines the type of template.|
|DisplayName|Template type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_templatetype|
|RequiredLevel|None|
|Type|Picklist|

#### msfp_templatetype Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|647390000|User||
|647390001|Survey||



### <a name="BKMK_msfp_version"></a> msfp_version

|Property|Value|
|--------|-----|
|Description|Version of the email message template|
|DisplayName|Version|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_version|
|MaxLength|400|
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
|Description|Status of the Survey email template|
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
|Description|Reason for the status of the Survey email template|
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
- [msfp_surveyName](#BKMK_msfp_surveyName)
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


### <a name="BKMK_msfp_surveyName"></a> msfp_surveyName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_surveyname|
|MaxLength|450|
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

- [msfp_emailtemplate_SyncErrors](#BKMK_msfp_emailtemplate_SyncErrors)
- [msfp_emailtemplate_AsyncOperations](#BKMK_msfp_emailtemplate_AsyncOperations)
- [msfp_emailtemplate_MailboxTrackingFolders](#BKMK_msfp_emailtemplate_MailboxTrackingFolders)
- [msfp_emailtemplate_ProcessSession](#BKMK_msfp_emailtemplate_ProcessSession)
- [msfp_emailtemplate_BulkDeleteFailures](#BKMK_msfp_emailtemplate_BulkDeleteFailures)
- [msfp_emailtemplate_PrincipalObjectAttributeAccesses](#BKMK_msfp_emailtemplate_PrincipalObjectAttributeAccesses)
- [msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate](#BKMK_msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate)
- [msfp_msfp_emailtemplate_msfp_localizedemailtem](#BKMK_msfp_msfp_emailtemplate_msfp_localizedemailtem)


### <a name="BKMK_msfp_emailtemplate_SyncErrors"></a> msfp_emailtemplate_SyncErrors

**Added by**: System Solution Solution

Same as the [msfp_emailtemplate_SyncErrors](syncerror.md#BKMK_msfp_emailtemplate_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_emailtemplate_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_emailtemplate_AsyncOperations"></a> msfp_emailtemplate_AsyncOperations

**Added by**: System Solution Solution

Same as the [msfp_emailtemplate_AsyncOperations](asyncoperation.md#BKMK_msfp_emailtemplate_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_emailtemplate_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_emailtemplate_MailboxTrackingFolders"></a> msfp_emailtemplate_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msfp_emailtemplate_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_emailtemplate_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_emailtemplate_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_emailtemplate_ProcessSession"></a> msfp_emailtemplate_ProcessSession

**Added by**: System Solution Solution

Same as the [msfp_emailtemplate_ProcessSession](processsession.md#BKMK_msfp_emailtemplate_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_emailtemplate_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_emailtemplate_BulkDeleteFailures"></a> msfp_emailtemplate_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msfp_emailtemplate_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_emailtemplate_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_emailtemplate_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_emailtemplate_PrincipalObjectAttributeAccesses"></a> msfp_emailtemplate_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msfp_emailtemplate_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_emailtemplate_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_emailtemplate_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate"></a> msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate

Same as the [msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate](msfp_surveyreminder.md#BKMK_msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate) many-to-one relationship for the [msfp_surveyreminder](msfp_surveyreminder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msfp_surveyreminder|
|ReferencingAttribute|msfp_emailtemplate|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_msfp_emailtemplate_msfp_surveyreminder_emailtemplate|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_msfp_emailtemplate_msfp_localizedemailtem"></a> msfp_msfp_emailtemplate_msfp_localizedemailtem

Same as the [msfp_msfp_emailtemplate_msfp_localizedemailtem](msfp_localizedemailtemplate.md#BKMK_msfp_msfp_emailtemplate_msfp_localizedemailtem) many-to-one relationship for the [msfp_localizedemailtemplate](msfp_localizedemailtemplate.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msfp_localizedemailtemplate|
|ReferencingAttribute|msfp_emailtemplateid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_msfp_emailtemplate_msfp_localizedemailtem|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msfp_emailtemplate_createdby](#BKMK_lk_msfp_emailtemplate_createdby)
- [lk_msfp_emailtemplate_createdonbehalfby](#BKMK_lk_msfp_emailtemplate_createdonbehalfby)
- [lk_msfp_emailtemplate_modifiedby](#BKMK_lk_msfp_emailtemplate_modifiedby)
- [lk_msfp_emailtemplate_modifiedonbehalfby](#BKMK_lk_msfp_emailtemplate_modifiedonbehalfby)
- [user_msfp_emailtemplate](#BKMK_user_msfp_emailtemplate)
- [team_msfp_emailtemplate](#BKMK_team_msfp_emailtemplate)
- [business_unit_msfp_emailtemplate](#BKMK_business_unit_msfp_emailtemplate)
- [msfp_msfp_survey_msfp_emailtemplate_surveyid](#BKMK_msfp_msfp_survey_msfp_emailtemplate_surveyid)


### <a name="BKMK_lk_msfp_emailtemplate_createdby"></a> lk_msfp_emailtemplate_createdby

**Added by**: System Solution Solution

See the [lk_msfp_emailtemplate_createdby](systemuser.md#BKMK_lk_msfp_emailtemplate_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_emailtemplate_createdonbehalfby"></a> lk_msfp_emailtemplate_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_emailtemplate_createdonbehalfby](systemuser.md#BKMK_lk_msfp_emailtemplate_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_emailtemplate_modifiedby"></a> lk_msfp_emailtemplate_modifiedby

**Added by**: System Solution Solution

See the [lk_msfp_emailtemplate_modifiedby](systemuser.md#BKMK_lk_msfp_emailtemplate_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_emailtemplate_modifiedonbehalfby"></a> lk_msfp_emailtemplate_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_emailtemplate_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_emailtemplate_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msfp_emailtemplate"></a> user_msfp_emailtemplate

**Added by**: System Solution Solution

See the [user_msfp_emailtemplate](systemuser.md#BKMK_user_msfp_emailtemplate) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msfp_emailtemplate"></a> team_msfp_emailtemplate

**Added by**: System Solution Solution

See the [team_msfp_emailtemplate](team.md#BKMK_team_msfp_emailtemplate) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msfp_emailtemplate"></a> business_unit_msfp_emailtemplate

**Added by**: System Solution Solution

See the [business_unit_msfp_emailtemplate](businessunit.md#BKMK_business_unit_msfp_emailtemplate) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msfp_msfp_survey_msfp_emailtemplate_surveyid"></a> msfp_msfp_survey_msfp_emailtemplate_surveyid

See the [msfp_msfp_survey_msfp_emailtemplate_surveyid](msfp_survey.md#BKMK_msfp_msfp_survey_msfp_emailtemplate_surveyid) one-to-many relationship for the [msfp_survey](msfp_survey.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msfp_emailtemplate?text=msfp_emailtemplate EntityType" />