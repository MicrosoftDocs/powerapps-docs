---
title: "Customer Voice satisfaction metric (msfp_satisfactionmetric)  table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the Customer Voice satisfaction metric (msfp_satisfactionmetric)  table/entity."
ms.date: 10/27/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# Customer Voice satisfaction metric (msfp_satisfactionmetric)  table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Satisfaction metric defined for a project.

**Added by**: Dynamics 365 Customer Voice Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msfp_satisfactionmetrics<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple|<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msfp_satisfactionmetrics<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msfp_satisfactionmetrics(*msfp_satisfactionmetricid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple|<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msfp_satisfactionmetrics|
|DisplayCollectionName|Customer Voice satisfaction metrics|
|DisplayName|Customer Voice satisfaction metric|
|EntitySetName|msfp_satisfactionmetrics|
|IsBPFEntity|False|
|LogicalCollectionName|msfp_satisfactionmetrics|
|LogicalName|msfp_satisfactionmetric|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msfp_satisfactionmetricid|
|PrimaryNameAttribute|msfp_name|
|SchemaName|msfp_satisfactionmetric|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msfp_description](#BKMK_msfp_description)
- [msfp_historicalcomputedvalue](#BKMK_msfp_historicalcomputedvalue)
- [msfp_issystemkpi](#BKMK_msfp_issystemkpi)
- [msfp_lastcomputedon](#BKMK_msfp_lastcomputedon)
- [msfp_lastcomputedvalue](#BKMK_msfp_lastcomputedvalue)
- [msfp_maximumvalue](#BKMK_msfp_maximumvalue)
- [msfp_minimumvalue](#BKMK_msfp_minimumvalue)
- [msfp_name](#BKMK_msfp_name)
- [msfp_project](#BKMK_msfp_project)
- [msfp_questions](#BKMK_msfp_questions)
- [msfp_satisfactionmetricId](#BKMK_msfp_satisfactionmetricId)
- [msfp_status](#BKMK_msfp_status)
- [msfp_threshold](#BKMK_msfp_threshold)
- [msfp_type](#BKMK_msfp_type)
- [msfp_versionnumber](#BKMK_msfp_versionnumber)
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


### <a name="BKMK_msfp_description"></a> msfp_description

|Property|Value|
|--------|-----|
|Description|Description of the satisfaction metric.|
|DisplayName|Description|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_description|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_historicalcomputedvalue"></a> msfp_historicalcomputedvalue

|Property|Value|
|--------|-----|
|Description|Historical computed value of the satisfaction metric.|
|DisplayName|Historical computed value|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_historicalcomputedvalue|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_issystemkpi"></a> msfp_issystemkpi

|Property|Value|
|--------|-----|
|Description|Indicates if the satisfaction metric is system defined or user defined.|
|DisplayName|Is system KPI|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_issystemkpi|
|RequiredLevel|None|
|Type|Boolean|

#### msfp_issystemkpi Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|True||
|0|False||

**DefaultValue**: 0



### <a name="BKMK_msfp_lastcomputedon"></a> msfp_lastcomputedon

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the satisfaction metric was last computed.|
|DisplayName|Last computed on|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_lastcomputedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_msfp_lastcomputedvalue"></a> msfp_lastcomputedvalue

|Property|Value|
|--------|-----|
|Description|Last computed value of the satisfaction metric.|
|DisplayName|Last Computed Value|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_lastcomputedvalue|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_maximumvalue"></a> msfp_maximumvalue

|Property|Value|
|--------|-----|
|Description|Maximum value of the satisfaction metric.|
|DisplayName|Maximum value|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_maximumvalue|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msfp_minimumvalue"></a> msfp_minimumvalue

|Property|Value|
|--------|-----|
|Description|Minimum value of the satisfaction metric.|
|DisplayName|Minimum value|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_minimumvalue|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_msfp_name"></a> msfp_name

|Property|Value|
|--------|-----|
|Description|Name of the satisfaction metric.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_name|
|MaxLength|550|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msfp_project"></a> msfp_project

|Property|Value|
|--------|-----|
|Description|Project to which the satisfaction metric belongs.|
|DisplayName|Project|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_project|
|RequiredLevel|ApplicationRequired|
|Targets|msfp_project|
|Type|Lookup|


### <a name="BKMK_msfp_questions"></a> msfp_questions

|Property|Value|
|--------|-----|
|Description|Questions on which the satisfaction metric is calculated.|
|DisplayName|Questions|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_questions|
|MaxLength|50000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msfp_satisfactionmetricId"></a> msfp_satisfactionmetricId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|Customer Voice satisfaction metric|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msfp_satisfactionmetricid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msfp_status"></a> msfp_status

|Property|Value|
|--------|-----|
|Description|Status of the satisfaction metric.|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_status|
|RequiredLevel|None|
|Type|Picklist|

#### msfp_status Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|647390000|Active||
|647390001|InActive||



### <a name="BKMK_msfp_threshold"></a> msfp_threshold

|Property|Value|
|--------|-----|
|Description|Threshold value of the satisfaction metric.|
|DisplayName|Threshold|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_threshold|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_msfp_type"></a> msfp_type

|Property|Value|
|--------|-----|
|Description|Type of the satisfaction metric.|
|DisplayName|Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_type|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msfp_versionnumber"></a> msfp_versionnumber

|Property|Value|
|--------|-----|
|Description|Version number of the satisfaction metric.|
|DisplayName|Version number|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msfp_versionnumber|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
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
|Description|User who owns the satisfaction metric.|
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
|Description|Status of the Satisfaction metric|
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
|Description|Reason for the status of the Satisfaction metric|
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
- [msfp_projectName](#BKMK_msfp_projectName)
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


### <a name="BKMK_msfp_projectName"></a> msfp_projectName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msfp_projectname|
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

- [msfp_satisfactionmetric_SyncErrors](#BKMK_msfp_satisfactionmetric_SyncErrors)
- [msfp_satisfactionmetric_AsyncOperations](#BKMK_msfp_satisfactionmetric_AsyncOperations)
- [msfp_satisfactionmetric_MailboxTrackingFolders](#BKMK_msfp_satisfactionmetric_MailboxTrackingFolders)
- [msfp_satisfactionmetric_ProcessSession](#BKMK_msfp_satisfactionmetric_ProcessSession)
- [msfp_satisfactionmetric_BulkDeleteFailures](#BKMK_msfp_satisfactionmetric_BulkDeleteFailures)
- [msfp_satisfactionmetric_PrincipalObjectAttributeAccesses](#BKMK_msfp_satisfactionmetric_PrincipalObjectAttributeAccesses)
- [msfp_msfp_satisfactionmetric_msfp_alertrule](#BKMK_msfp_msfp_satisfactionmetric_msfp_alertrule)
- [msfp_msfp_satisfactionmetric_msfp_alert](#BKMK_msfp_msfp_satisfactionmetric_msfp_alert)


### <a name="BKMK_msfp_satisfactionmetric_SyncErrors"></a> msfp_satisfactionmetric_SyncErrors

**Added by**: System Solution Solution

Same as the [msfp_satisfactionmetric_SyncErrors](syncerror.md#BKMK_msfp_satisfactionmetric_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_satisfactionmetric_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_satisfactionmetric_AsyncOperations"></a> msfp_satisfactionmetric_AsyncOperations

**Added by**: System Solution Solution

Same as the [msfp_satisfactionmetric_AsyncOperations](asyncoperation.md#BKMK_msfp_satisfactionmetric_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_satisfactionmetric_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_satisfactionmetric_MailboxTrackingFolders"></a> msfp_satisfactionmetric_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msfp_satisfactionmetric_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msfp_satisfactionmetric_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_satisfactionmetric_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_satisfactionmetric_ProcessSession"></a> msfp_satisfactionmetric_ProcessSession

**Added by**: System Solution Solution

Same as the [msfp_satisfactionmetric_ProcessSession](processsession.md#BKMK_msfp_satisfactionmetric_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_satisfactionmetric_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_satisfactionmetric_BulkDeleteFailures"></a> msfp_satisfactionmetric_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msfp_satisfactionmetric_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msfp_satisfactionmetric_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_satisfactionmetric_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_satisfactionmetric_PrincipalObjectAttributeAccesses"></a> msfp_satisfactionmetric_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msfp_satisfactionmetric_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msfp_satisfactionmetric_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_satisfactionmetric_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_msfp_satisfactionmetric_msfp_alertrule"></a> msfp_msfp_satisfactionmetric_msfp_alertrule

Same as the [msfp_msfp_satisfactionmetric_msfp_alertrule](msfp_alertrule.md#BKMK_msfp_msfp_satisfactionmetric_msfp_alertrule) many-to-one relationship for the [msfp_alertrule](msfp_alertrule.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msfp_alertrule|
|ReferencingAttribute|msfp_satisfactionmetric|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_msfp_satisfactionmetric_msfp_alertrule|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msfp_msfp_satisfactionmetric_msfp_alert"></a> msfp_msfp_satisfactionmetric_msfp_alert

Same as the [msfp_msfp_satisfactionmetric_msfp_alert](msfp_alert.md#BKMK_msfp_msfp_satisfactionmetric_msfp_alert) many-to-one relationship for the [msfp_alert](msfp_alert.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msfp_alert|
|ReferencingAttribute|msfp_satisfactionmetric|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msfp_msfp_satisfactionmetric_msfp_alert|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msfp_satisfactionmetric_createdby](#BKMK_lk_msfp_satisfactionmetric_createdby)
- [lk_msfp_satisfactionmetric_createdonbehalfby](#BKMK_lk_msfp_satisfactionmetric_createdonbehalfby)
- [lk_msfp_satisfactionmetric_modifiedby](#BKMK_lk_msfp_satisfactionmetric_modifiedby)
- [lk_msfp_satisfactionmetric_modifiedonbehalfby](#BKMK_lk_msfp_satisfactionmetric_modifiedonbehalfby)
- [user_msfp_satisfactionmetric](#BKMK_user_msfp_satisfactionmetric)
- [team_msfp_satisfactionmetric](#BKMK_team_msfp_satisfactionmetric)
- [business_unit_msfp_satisfactionmetric](#BKMK_business_unit_msfp_satisfactionmetric)
- [msfp_msfp_project_msfp_satisfactionmetric_project](#BKMK_msfp_msfp_project_msfp_satisfactionmetric_project)


### <a name="BKMK_lk_msfp_satisfactionmetric_createdby"></a> lk_msfp_satisfactionmetric_createdby

**Added by**: System Solution Solution

See the [lk_msfp_satisfactionmetric_createdby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_satisfactionmetric_createdonbehalfby"></a> lk_msfp_satisfactionmetric_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_satisfactionmetric_createdonbehalfby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_satisfactionmetric_modifiedby"></a> lk_msfp_satisfactionmetric_modifiedby

**Added by**: System Solution Solution

See the [lk_msfp_satisfactionmetric_modifiedby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msfp_satisfactionmetric_modifiedonbehalfby"></a> lk_msfp_satisfactionmetric_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msfp_satisfactionmetric_modifiedonbehalfby](systemuser.md#BKMK_lk_msfp_satisfactionmetric_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msfp_satisfactionmetric"></a> user_msfp_satisfactionmetric

**Added by**: System Solution Solution

See the [user_msfp_satisfactionmetric](systemuser.md#BKMK_user_msfp_satisfactionmetric) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msfp_satisfactionmetric"></a> team_msfp_satisfactionmetric

**Added by**: System Solution Solution

See the [team_msfp_satisfactionmetric](team.md#BKMK_team_msfp_satisfactionmetric) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msfp_satisfactionmetric"></a> business_unit_msfp_satisfactionmetric

**Added by**: System Solution Solution

See the [business_unit_msfp_satisfactionmetric](businessunit.md#BKMK_business_unit_msfp_satisfactionmetric) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msfp_msfp_project_msfp_satisfactionmetric_project"></a> msfp_msfp_project_msfp_satisfactionmetric_project

See the [msfp_msfp_project_msfp_satisfactionmetric_project](msfp_project.md#BKMK_msfp_msfp_project_msfp_satisfactionmetric_project) one-to-many relationship for the [msfp_project](msfp_project.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msfp_satisfactionmetric?text=msfp_satisfactionmetric EntityType" />