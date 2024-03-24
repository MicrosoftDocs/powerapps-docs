---
title: "msdyn_AIEvent table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_AIEvent table/entity."
ms.date: 02/22/2024
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_AIEvent table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: AISolution Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|Assign|PATCH /msdyn_aievents(*msdyn_aieventid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|BulkRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Create|POST /msdyn_aievents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple|<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE /msdyn_aievents(*msdyn_aieventid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|ModifyAccess|<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|PurgeRetainedContent|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|Retrieve|GET /msdyn_aievents(*msdyn_aieventid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET /msdyn_aievents<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|RollbackRetain|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||
|SetState|PATCH /msdyn_aievents(*msdyn_aieventid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH /msdyn_aievents(*msdyn_aieventid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple|<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
|ValidateRetentionConfig|This message is to be executed only by Dataverse to trigger registered plug-ins and flows.||

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_AIEvents|
|DisplayCollectionName|AI Events|
|DisplayName|AI Event|
|EntitySetName|msdyn_aievents|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_aievents|
|LogicalName|msdyn_aievent|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|msdyn_aieventid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_AIEvent|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AIEventId](#BKMK_msdyn_AIEventId)
- [msdyn_AIModelId](#BKMK_msdyn_AIModelId)
- [msdyn_ApprovalId](#BKMK_msdyn_ApprovalId)
- [msdyn_AutomationLink](#BKMK_msdyn_AutomationLink)
- [msdyn_AutomationName](#BKMK_msdyn_AutomationName)
- [msdyn_ConsumptionSource](#BKMK_msdyn_ConsumptionSource)
- [msdyn_CreditConsumed](#BKMK_msdyn_CreditConsumed)
- [msdyn_DataInfo](#BKMK_msdyn_DataInfo)
- [msdyn_DataType](#BKMK_msdyn_DataType)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_Output](#BKMK_msdyn_Output)
- [msdyn_PartnerSource](#BKMK_msdyn_PartnerSource)
- [msdyn_ProcessingDate](#BKMK_msdyn_ProcessingDate)
- [msdyn_ProcessingStatus](#BKMK_msdyn_ProcessingStatus)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [QuickTest](#BKMK_QuickTest)
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


### <a name="BKMK_msdyn_AIEventId"></a> msdyn_AIEventId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|AI Event|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_aieventid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_AIModelId"></a> msdyn_AIModelId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|AI Model|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_aimodelid|
|RequiredLevel|None|
|Targets|msdyn_aimodel|
|Type|Lookup|


### <a name="BKMK_msdyn_ApprovalId"></a> msdyn_ApprovalId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Approval Id|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_approvalid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_AutomationLink"></a> msdyn_AutomationLink

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Automation Link|
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_automationlink|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_AutomationName"></a> msdyn_AutomationName

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Automation Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_automationname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ConsumptionSource"></a> msdyn_ConsumptionSource

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Consumption Source|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_consumptionsource|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_ConsumptionSource Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|PowerAutomation||
|1|PowerApps||
|2|API||



### <a name="BKMK_msdyn_CreditConsumed"></a> msdyn_CreditConsumed

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Credit Consumed|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_creditconsumed|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|ApplicationRequired|
|Type|Integer|


### <a name="BKMK_msdyn_DataInfo"></a> msdyn_DataInfo

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Data Info|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_datainfo|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_DataType"></a> msdyn_DataType

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Data Type|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_datatype|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_name|
|MaxLength|100|
|RequiredLevel|ApplicationRequired|
|Type|String|


### <a name="BKMK_msdyn_Output"></a> msdyn_Output

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Output|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_output|
|MaxLength|4000|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_PartnerSource"></a> msdyn_PartnerSource

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Partner Source|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_partnersource|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_ProcessingDate"></a> msdyn_ProcessingDate

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Processing Date|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_processingdate|
|RequiredLevel|ApplicationRequired|
|Type|DateTime|


### <a name="BKMK_msdyn_ProcessingStatus"></a> msdyn_ProcessingStatus

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Processing Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_processingstatus|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|

#### msdyn_ProcessingStatus Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Processed||
|1|Failed||
|2|Processing||



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


### <a name="BKMK_QuickTest"></a> QuickTest

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Quick Test|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_quicktest|
|RequiredLevel|None|
|Type|Boolean|

#### QuickTest Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes||
|0|No||

**DefaultValue**: 0



### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the AI Event|
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
|Description|Reason for the status of the AI Event|
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
- [msdyn_AIModelIdName](#BKMK_msdyn_AIModelIdName)
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


### <a name="BKMK_msdyn_AIModelIdName"></a> msdyn_AIModelIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_aimodelidname|
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

- [msdyn_aievent_SyncErrors](#BKMK_msdyn_aievent_SyncErrors)
- [msdyn_aievent_DuplicateMatchingRecord](#BKMK_msdyn_aievent_DuplicateMatchingRecord)
- [msdyn_aievent_DuplicateBaseRecord](#BKMK_msdyn_aievent_DuplicateBaseRecord)
- [msdyn_aievent_AsyncOperations](#BKMK_msdyn_aievent_AsyncOperations)
- [msdyn_aievent_MailboxTrackingFolders](#BKMK_msdyn_aievent_MailboxTrackingFolders)
- [msdyn_aievent_ProcessSession](#BKMK_msdyn_aievent_ProcessSession)
- [msdyn_aievent_BulkDeleteFailures](#BKMK_msdyn_aievent_BulkDeleteFailures)
- [msdyn_aievent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses)


### <a name="BKMK_msdyn_aievent_SyncErrors"></a> msdyn_aievent_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_aievent_SyncErrors](syncerror.md#BKMK_msdyn_aievent_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_DuplicateMatchingRecord"></a> msdyn_aievent_DuplicateMatchingRecord

**Added by**: System Solution Solution

Same as the [msdyn_aievent_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_aievent_DuplicateMatchingRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|duplicaterecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_DuplicateMatchingRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_DuplicateBaseRecord"></a> msdyn_aievent_DuplicateBaseRecord

**Added by**: System Solution Solution

Same as the [msdyn_aievent_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_aievent_DuplicateBaseRecord) many-to-one relationship for the [duplicaterecord](duplicaterecord.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|duplicaterecord|
|ReferencingAttribute|baserecordid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_DuplicateBaseRecord|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_AsyncOperations"></a> msdyn_aievent_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_aievent_AsyncOperations](asyncoperation.md#BKMK_msdyn_aievent_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_MailboxTrackingFolders"></a> msdyn_aievent_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_aievent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aievent_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_ProcessSession"></a> msdyn_aievent_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_aievent_ProcessSession](processsession.md#BKMK_msdyn_aievent_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_BulkDeleteFailures"></a> msdyn_aievent_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_aievent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aievent_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses"></a> msdyn_aievent_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_aievent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aievent_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aievent_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_aievent_createdby](#BKMK_lk_msdyn_aievent_createdby)
- [lk_msdyn_aievent_createdonbehalfby](#BKMK_lk_msdyn_aievent_createdonbehalfby)
- [lk_msdyn_aievent_modifiedby](#BKMK_lk_msdyn_aievent_modifiedby)
- [lk_msdyn_aievent_modifiedonbehalfby](#BKMK_lk_msdyn_aievent_modifiedonbehalfby)
- [user_msdyn_aievent](#BKMK_user_msdyn_aievent)
- [team_msdyn_aievent](#BKMK_team_msdyn_aievent)
- [business_unit_msdyn_aievent](#BKMK_business_unit_msdyn_aievent)
- [msdyn_aimodel_msdyn_aievent](#BKMK_msdyn_aimodel_msdyn_aievent)


### <a name="BKMK_lk_msdyn_aievent_createdby"></a> lk_msdyn_aievent_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_aievent_createdby](systemuser.md#BKMK_lk_msdyn_aievent_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_aievent_createdonbehalfby"></a> lk_msdyn_aievent_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_aievent_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aievent_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_aievent_modifiedby"></a> lk_msdyn_aievent_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_aievent_modifiedby](systemuser.md#BKMK_lk_msdyn_aievent_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_aievent_modifiedonbehalfby"></a> lk_msdyn_aievent_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_aievent_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aievent_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_user_msdyn_aievent"></a> user_msdyn_aievent

**Added by**: System Solution Solution

See the [user_msdyn_aievent](systemuser.md#BKMK_user_msdyn_aievent) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_team_msdyn_aievent"></a> team_msdyn_aievent

**Added by**: System Solution Solution

See the [team_msdyn_aievent](team.md#BKMK_team_msdyn_aievent) one-to-many relationship for the [team](team.md) table/entity.

### <a name="BKMK_business_unit_msdyn_aievent"></a> business_unit_msdyn_aievent

**Added by**: System Solution Solution

See the [business_unit_msdyn_aievent](businessunit.md#BKMK_business_unit_msdyn_aievent) one-to-many relationship for the [businessunit](businessunit.md) table/entity.

### <a name="BKMK_msdyn_aimodel_msdyn_aievent"></a> msdyn_aimodel_msdyn_aievent

See the [msdyn_aimodel_msdyn_aievent](msdyn_aimodel.md#BKMK_msdyn_aimodel_msdyn_aievent) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_aievent?text=msdyn_aievent EntityType" />