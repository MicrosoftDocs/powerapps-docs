---
title: "Customer Voice file response (msfp_fileresponse)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Customer Voice file response (msfp_fileresponse)  table/entity."
ms.date: 10/27/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Customer Voice file response (msfp_fileresponse)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Response to a file upload question.

**Added by**: Dynamics 365 Customer Voice Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msfp_fileresponses(*msfp_fileresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msfp_fileresponses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple|<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msfp_fileresponses<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msfp_fileresponses(*msfp_fileresponseid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msfp_fileresponses(*msfp_fileresponseid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple|<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msfp_fileresponses|
|DisplayCollectionName|Customer Voice file responses|
|DisplayName|Customer Voice file response|
|EntitySetName|msfp_fileresponses|
|IsBPFEntity|False|
|LogicalCollectionName|msfp_fileresponses|
|LogicalName|msfp_fileresponse|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msfp_fileresponseid|
|PrimaryNameAttribute|msfp_name|
|SchemaName|msfp_fileresponse|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_fileresponseId](#BKMK_msfp_fileresponseId)
- [msfp_name](#BKMK_msfp_name)
- [msfp_otherproperties](#BKMK_msfp_otherproperties)
- [msfp_question](#BKMK_msfp_question)
- [msfp_questionresponse](#BKMK_msfp_questionresponse)
- [msfp_sourcequestionidentifier](#BKMK_msfp_sourcequestionidentifier)
- [msfp_sourcesurveyidentifier](#BKMK_msfp_sourcesurveyidentifier)
- [msfp_survey](#BKMK_msfp_survey)
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


### <a name="BKMK_msfp_fileresponseId"></a> msfp_fileresponseId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Customer Voice file response|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msfp_fileresponseid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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
|Description|Stores other properties in JSON format.|
|DisplayName|Other properties|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_otherproperties|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_question"></a> msfp_question

|Property|Value|
|--------|-----|
|Description|(Deprecated) Question associated with the question response.|
|DisplayName|(Deprecated) Question|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_question|
|RequiredLevel|None|
|Targets|msfp_question|
|Type|Lookup|


### <a name="BKMK_msfp_questionresponse"></a> msfp_questionresponse

|Property|Value|
|--------|-----|
|Description|Question Response with which the File Response is associated.|
|DisplayName|Question Response|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_questionresponse|
|RequiredLevel|None|
|Targets|msfp_questionresponse|
|Type|Lookup|


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
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msfp_survey"></a> msfp_survey

|Property|Value|
|--------|-----|
|Description|(Deprecated) Unique identifier of the survey to which the question belongs.|
|DisplayName|(Deprecated) Survey|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_survey|
|RequiredLevel|None|
|Targets|msfp_survey|
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
|Description|Status of the Customer Voice file response|
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
|Description|Reason for the status of the Customer Voice file response|
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
- [msfp_file1](#BKMK_msfp_file1)
- [msfp_file1_Name](#BKMK_msfp_file1_Name)
- [msfp_file10](#BKMK_msfp_file10)
- [msfp_file10_Name](#BKMK_msfp_file10_Name)
- [msfp_file2](#BKMK_msfp_file2)
- [msfp_file2_Name](#BKMK_msfp_file2_Name)
- [msfp_file3](#BKMK_msfp_file3)
- [msfp_file3_Name](#BKMK_msfp_file3_Name)
- [msfp_file4](#BKMK_msfp_file4)
- [msfp_file4_Name](#BKMK_msfp_file4_Name)
- [msfp_file5](#BKMK_msfp_file5)
- [msfp_file5_Name](#BKMK_msfp_file5_Name)
- [msfp_file6](#BKMK_msfp_file6)
- [msfp_file6_Name](#BKMK_msfp_file6_Name)
- [msfp_file7](#BKMK_msfp_file7)
- [msfp_file7_Name](#BKMK_msfp_file7_Name)
- [msfp_file8](#BKMK_msfp_file8)
- [msfp_file8_Name](#BKMK_msfp_file8_Name)
- [msfp_file9](#BKMK_msfp_file9)
- [msfp_file9_Name](#BKMK_msfp_file9_Name)
- [msfp_questionName](#BKMK_msfp_questionName)
- [msfp_questionresponseName](#BKMK_msfp_questionresponseName)
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


### <a name="BKMK_msfp_file1"></a> msfp_file1

|Property|Value|
|--------|-----|
|Description|First uploaded file.|
|DisplayName|File 1|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file1|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file1_Name"></a> msfp_file1_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file1_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file10"></a> msfp_file10

|Property|Value|
|--------|-----|
|Description|Tenth uploaded file.|
|DisplayName|File 10|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file10|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file10_Name"></a> msfp_file10_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file10_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file2"></a> msfp_file2

|Property|Value|
|--------|-----|
|Description|Second uploaded file.|
|DisplayName|File 2|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file2|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file2_Name"></a> msfp_file2_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file2_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file3"></a> msfp_file3

|Property|Value|
|--------|-----|
|Description|Third uploaded file.|
|DisplayName|File 3|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file3|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file3_Name"></a> msfp_file3_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file3_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file4"></a> msfp_file4

|Property|Value|
|--------|-----|
|Description|Fourth uploaded file.|
|DisplayName|File 4|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file4|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file4_Name"></a> msfp_file4_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file4_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file5"></a> msfp_file5

|Property|Value|
|--------|-----|
|Description|Fifth uploaded file.|
|DisplayName|File 5|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file5|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file5_Name"></a> msfp_file5_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file5_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file6"></a> msfp_file6

|Property|Value|
|--------|-----|
|Description|Sixth uploaded file.|
|DisplayName|File 6|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file6|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file6_Name"></a> msfp_file6_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file6_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file7"></a> msfp_file7

|Property|Value|
|--------|-----|
|Description|Seventh uploaded file.|
|DisplayName|File 7|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file7|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file7_Name"></a> msfp_file7_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file7_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file8"></a> msfp_file8

|Property|Value|
|--------|-----|
|Description|Eighth uploaded file.|
|DisplayName|File 8|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file8|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file8_Name"></a> msfp_file8_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file8_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_file9"></a> msfp_file9

|Property|Value|
|--------|-----|
|Description|Ninth uploaded file.|
|DisplayName|File 9|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_file9|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msfp_file9_Name"></a> msfp_file9_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_file9_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_questionName"></a> msfp_questionName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_questionname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_questionresponseName"></a> msfp_questionresponseName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_questionresponsename|
|MaxLength|100|
|RequiredLevel|None|
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

- [msfp_fileresponse_SyncErrors](#BKMK_msfp_fileresponse_SyncErrors)
- [msfp_fileresponse_AsyncOperations](#BKMK_msfp_fileresponse_AsyncOperations)
- [msfp_fileresponse_MailboxTrackingFolders](#BKMK_msfp_fileresponse_MailboxTrackingFolders)
- [msfp_fileresponse_ProcessSession](#BKMK_msfp_fileresponse_ProcessSession)
- [msfp_fileresponse_BulkDeleteFailures](#BKMK_msfp_fileresponse_BulkDeleteFailures)
- [msfp_fileresponse_PrincipalObjectAttributeAccesses](#BKMK_msfp_fileresponse_PrincipalObjectAttributeAccesses)
- [msfp_fileresponse_DuplicateMatchingRecord](#BKMK_msfp_fileresponse_DuplicateMatchingRecord)
- [msfp_fileresponse_DuplicateBaseRecord](#BKMK_msfp_fileresponse_DuplicateBaseRecord)


### <a name="BKMK_msfp_fileresponse_SyncErrors"></a> msfp_fileresponse_SyncErrors

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_SyncErrors](syncerror.md#BKMK_msfp_fileresponse_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_AsyncOperations"></a> msfp_fileresponse_AsyncOperations

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_AsyncOperations](asyncoperation.md#BKMK_msfp_fileresponse_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_MailboxTrackingFolders"></a> msfp_fileresponse_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_fileresponse_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_ProcessSession"></a> msfp_fileresponse_ProcessSession

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_ProcessSession](processsession.md#BKMK_msfp_fileresponse_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_BulkDeleteFailures"></a> msfp_fileresponse_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_fileresponse_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_PrincipalObjectAttributeAccesses"></a> msfp_fileresponse_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_fileresponse_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_DuplicateMatchingRecord"></a> msfp_fileresponse_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msfp_fileresponse_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_fileresponse_DuplicateBaseRecord"></a> msfp_fileresponse_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msfp_fileresponse_DuplicateBaseRecord](duplicaterecord.md#BKMK_msfp_fileresponse_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_fileresponse_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msfp_fileresponse_createdby](#BKMK_lk_msfp_fileresponse_createdby)
- [lk_msfp_fileresponse_createdonbehalfby](#BKMK_lk_msfp_fileresponse_createdonbehalfby)
- [lk_msfp_fileresponse_modifiedby](#BKMK_lk_msfp_fileresponse_modifiedby)
- [lk_msfp_fileresponse_modifiedonbehalfby](#BKMK_lk_msfp_fileresponse_modifiedonbehalfby)
- [user_msfp_fileresponse](#BKMK_user_msfp_fileresponse)
- [team_msfp_fileresponse](#BKMK_team_msfp_fileresponse)
- [business_unit_msfp_fileresponse](#BKMK_business_unit_msfp_fileresponse)
- [msfp_msfp_question_msfp_fileresponse_question](#BKMK_msfp_msfp_question_msfp_fileresponse_question)
- [msfp_msfp_questionresponse_msfp_fileresponse_questionresponse](#BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse)
- [msfp_msfp_survey_msfp_fileresponse_survey](#BKMK_msfp_msfp_survey_msfp_fileresponse_survey)


### <a name="BKMK_lk_msfp_fileresponse_createdby"></a> lk_msfp_fileresponse_createdby

**Added by**: System Solution Solution

See the [lk_msfp_fileresponse_createdby](systemuser.md#BKMK_lk_msfp_fileresponse_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_fileresponse_createdonbehalfby"></a> lk_msfp_fileresponse_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_fileresponse_createdonbehalfby](systemuser.md#BKMK_lk_msfp_fileresponse_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_fileresponse_modifiedby"></a> lk_msfp_fileresponse_modifiedby

**Added by**: System Solution Solution

See the [lk_msfp_fileresponse_modifiedby](systemuser.md#BKMK_lk_msfp_fileresponse_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_fileresponse_modifiedonbehalfby"></a> lk_msfp_fileresponse_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_fileresponse_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_fileresponse_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msfp_fileresponse"></a> user_msfp_fileresponse

**Added by**: System Solution Solution

See the [user_msfp_fileresponse](systemuser.md#BKMK_user_msfp_fileresponse) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msfp_fileresponse"></a> team_msfp_fileresponse

**Added by**: System Solution Solution

See the [team_msfp_fileresponse](team.md#BKMK_team_msfp_fileresponse) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msfp_fileresponse"></a> business_unit_msfp_fileresponse

**Added by**: System Solution Solution

See the [business_unit_msfp_fileresponse](businessunit.md#BKMK_business_unit_msfp_fileresponse) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msfp_msfp_question_msfp_fileresponse_question"></a> msfp_msfp_question_msfp_fileresponse_question

See the [msfp_msfp_question_msfp_fileresponse_question](msfp_question.md#BKMK_msfp_msfp_question_msfp_fileresponse_question) one-to-many relationship for the [msfp_question](msfp_question.md) table/entity.

### <a name="BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse"></a> msfp_msfp_questionresponse_msfp_fileresponse_questionresponse

See the [msfp_msfp_questionresponse_msfp_fileresponse_questionresponse](msfp_questionresponse.md#BKMK_msfp_msfp_questionresponse_msfp_fileresponse_questionresponse) one-to-many relationship for the [msfp_questionresponse](msfp_questionresponse.md) table/entity.

### <a name="BKMK_msfp_msfp_survey_msfp_fileresponse_survey"></a> msfp_msfp_survey_msfp_fileresponse_survey

See the [msfp_msfp_survey_msfp_fileresponse_survey](msfp_survey.md#BKMK_msfp_msfp_survey_msfp_fileresponse_survey) one-to-many relationship for the [msfp_survey](msfp_survey.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msfp_fileresponse?text=msfp_fileresponse EntityType" />