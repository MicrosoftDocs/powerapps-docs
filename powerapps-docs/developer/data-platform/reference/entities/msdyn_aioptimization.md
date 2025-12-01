---
title: "AI Optimization (msdyn_AIOptimization) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AI Optimization (msdyn_AIOptimization) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AI Optimization (msdyn_AIOptimization) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the AI Optimization (msdyn_AIOptimization) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_aioptimizations(*msdyn_aioptimizationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_aioptimizations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_aioptimizations(*msdyn_aioptimizationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_aioptimizations(*msdyn_aioptimizationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_aioptimizations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_aioptimizations(*msdyn_aioptimizationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_aioptimizations(*msdyn_aioptimizationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_aioptimizations(*msdyn_aioptimizationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AI Optimization (msdyn_AIOptimization) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AI Optimization** |
| **DisplayCollectionName** | **AI Optimizations** |
| **SchemaName** | `msdyn_AIOptimization` |
| **CollectionSchemaName** | `msdyn_AIOptimizations` |
| **EntitySetName** | `msdyn_aioptimizations`|
| **LogicalName** | `msdyn_aioptimization` |
| **LogicalCollectionName** | `msdyn_aioptimizations` |
| **PrimaryIdAttribute** | `msdyn_aioptimizationid` |
| **PrimaryNameAttribute** |`msdyn_aiobjectid` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AIModelId](#BKMK_msdyn_AIModelId)
- [msdyn_AIObjectId](#BKMK_msdyn_AIObjectId)
- [msdyn_AIOptimizationId](#BKMK_msdyn_AIOptimizationId)
- [msdyn_AIOptimizationPrivateDataId](#BKMK_msdyn_AIOptimizationPrivateDataId)
- [msdyn_CurrentIteration](#BKMK_msdyn_CurrentIteration)
- [msdyn_CurrentPrompt](#BKMK_msdyn_CurrentPrompt)
- [msdyn_CurrentScore](#BKMK_msdyn_CurrentScore)
- [msdyn_EndDate](#BKMK_msdyn_EndDate)
- [msdyn_EvaluationCriteria](#BKMK_msdyn_EvaluationCriteria)
- [msdyn_Explanation](#BKMK_msdyn_Explanation)
- [msdyn_ModelSettings](#BKMK_msdyn_ModelSettings)
- [msdyn_OldScore](#BKMK_msdyn_OldScore)
- [msdyn_PromptHistory](#BKMK_msdyn_PromptHistory)
- [msdyn_RunStatus](#BKMK_msdyn_RunStatus)
- [msdyn_StartDate](#BKMK_msdyn_StartDate)
- [msdyn_TotalIterations](#BKMK_msdyn_TotalIterations)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_AIModelId"></a> msdyn_AIModelId

|Property|Value|
|---|---|
|Description||
|DisplayName|**AI Model Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aimodelid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_aimodel|

### <a name="BKMK_msdyn_AIObjectId"></a> msdyn_AIObjectId

|Property|Value|
|---|---|
|Description||
|DisplayName|**AIObjectId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aiobjectid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|850|

### <a name="BKMK_msdyn_AIOptimizationId"></a> msdyn_AIOptimizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AI Optimization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aioptimizationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_AIOptimizationPrivateDataId"></a> msdyn_AIOptimizationPrivateDataId

|Property|Value|
|---|---|
|Description||
|DisplayName|**AI Optimization Private Data Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aioptimizationprivatedataid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_aioptimizationprivatedata|

### <a name="BKMK_msdyn_CurrentIteration"></a> msdyn_CurrentIteration

|Property|Value|
|---|---|
|Description||
|DisplayName|**Current Iteration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_currentiteration`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_CurrentPrompt"></a> msdyn_CurrentPrompt

|Property|Value|
|---|---|
|Description||
|DisplayName|**Current Prompt**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_currentprompt`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_CurrentScore"></a> msdyn_CurrentScore

|Property|Value|
|---|---|
|Description||
|DisplayName|**Current Score**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_currentscore`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_msdyn_EndDate"></a> msdyn_EndDate

|Property|Value|
|---|---|
|Description||
|DisplayName|**End Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_enddate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_EvaluationCriteria"></a> msdyn_EvaluationCriteria

|Property|Value|
|---|---|
|Description||
|DisplayName|**Evaluation Criteria**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_evaluationcriteria`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_Explanation"></a> msdyn_Explanation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Explanation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_explanation`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_ModelSettings"></a> msdyn_ModelSettings

|Property|Value|
|---|---|
|Description||
|DisplayName|**Model Settings**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelsettings`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_OldScore"></a> msdyn_OldScore

|Property|Value|
|---|---|
|Description||
|DisplayName|**Old Score**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_oldscore`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_msdyn_PromptHistory"></a> msdyn_PromptHistory

|Property|Value|
|---|---|
|Description||
|DisplayName|**Prompt History**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_prompthistory`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_RunStatus"></a> msdyn_RunStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**RunStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_runstatus`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`new_msdyn_aioptimization_msdyn_runstatus`|

#### msdyn_RunStatus Choices/Options

|Value|Label|
|---|---|
|0|**Creating**|
|1|**Created**|
|2|**Running**|
|3|**Success**|
|4|**Failed**|

### <a name="BKMK_msdyn_StartDate"></a> msdyn_StartDate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Start Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_startdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_TotalIterations"></a> msdyn_TotalIterations

|Property|Value|
|---|---|
|Description||
|DisplayName|**Total Iterations**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_totaliterations`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the AI Optimization**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aioptimization_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AI Optimization**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aioptimization_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
|DisplayName|**Created By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was created.**|
|DisplayName|**Created On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
|DisplayName|**Modified By**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the record was modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

|Property|Value|
|---|---|
|Description|**Yomi name of the owner**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridyominame`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|---|---|
|Description|**Unique identifier for the team that owns the record.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|team|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
|DisplayName|**Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_msdyn_aioptimization](#BKMK_business_unit_msdyn_aioptimization)
- [lk_msdyn_aioptimization_createdby](#BKMK_lk_msdyn_aioptimization_createdby)
- [lk_msdyn_aioptimization_createdonbehalfby](#BKMK_lk_msdyn_aioptimization_createdonbehalfby)
- [lk_msdyn_aioptimization_modifiedby](#BKMK_lk_msdyn_aioptimization_modifiedby)
- [lk_msdyn_aioptimization_modifiedonbehalfby](#BKMK_lk_msdyn_aioptimization_modifiedonbehalfby)
- [msdyn_aioptimization_aimodelid_msdyn_aimodel](#BKMK_msdyn_aioptimization_aimodelid_msdyn_aimodel)
- [msdyn_aioptimizationprivatedata_msdyn_aioptimization](#BKMK_msdyn_aioptimizationprivatedata_msdyn_aioptimization)
- [owner_msdyn_aioptimization](#BKMK_owner_msdyn_aioptimization)
- [team_msdyn_aioptimization](#BKMK_team_msdyn_aioptimization)
- [user_msdyn_aioptimization](#BKMK_user_msdyn_aioptimization)

### <a name="BKMK_business_unit_msdyn_aioptimization"></a> business_unit_msdyn_aioptimization

One-To-Many Relationship: [businessunit business_unit_msdyn_aioptimization](businessunit.md#BKMK_business_unit_msdyn_aioptimization)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aioptimization_createdby"></a> lk_msdyn_aioptimization_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aioptimization_createdby](systemuser.md#BKMK_lk_msdyn_aioptimization_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aioptimization_createdonbehalfby"></a> lk_msdyn_aioptimization_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aioptimization_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aioptimization_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aioptimization_modifiedby"></a> lk_msdyn_aioptimization_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aioptimization_modifiedby](systemuser.md#BKMK_lk_msdyn_aioptimization_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aioptimization_modifiedonbehalfby"></a> lk_msdyn_aioptimization_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aioptimization_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aioptimization_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aioptimization_aimodelid_msdyn_aimodel"></a> msdyn_aioptimization_aimodelid_msdyn_aimodel

One-To-Many Relationship: [msdyn_aimodel msdyn_aioptimization_aimodelid_msdyn_aimodel](msdyn_aimodel.md#BKMK_msdyn_aioptimization_aimodelid_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`msdyn_aimodelid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIModelId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Cascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_msdyn_aioptimizationprivatedata_msdyn_aioptimization"></a> msdyn_aioptimizationprivatedata_msdyn_aioptimization

One-To-Many Relationship: [msdyn_aioptimizationprivatedata msdyn_aioptimizationprivatedata_msdyn_aioptimization](msdyn_aioptimizationprivatedata.md#BKMK_msdyn_aioptimizationprivatedata_msdyn_aioptimization)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aioptimizationprivatedata`|
|ReferencedAttribute|`msdyn_aioptimizationprivatedataid`|
|ReferencingAttribute|`msdyn_aioptimizationprivatedataid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIOptimizationPrivateDataId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_aioptimization"></a> owner_msdyn_aioptimization

One-To-Many Relationship: [owner owner_msdyn_aioptimization](owner.md#BKMK_owner_msdyn_aioptimization)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_aioptimization"></a> team_msdyn_aioptimization

One-To-Many Relationship: [team team_msdyn_aioptimization](team.md#BKMK_team_msdyn_aioptimization)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_aioptimization"></a> user_msdyn_aioptimization

One-To-Many Relationship: [systemuser user_msdyn_aioptimization](systemuser.md#BKMK_user_msdyn_aioptimization)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_aioptimization_AsyncOperations](#BKMK_msdyn_aioptimization_AsyncOperations)
- [msdyn_aioptimization_BulkDeleteFailures](#BKMK_msdyn_aioptimization_BulkDeleteFailures)
- [msdyn_aioptimization_DuplicateBaseRecord](#BKMK_msdyn_aioptimization_DuplicateBaseRecord)
- [msdyn_aioptimization_DuplicateMatchingRecord](#BKMK_msdyn_aioptimization_DuplicateMatchingRecord)
- [msdyn_aioptimization_MailboxTrackingFolders](#BKMK_msdyn_aioptimization_MailboxTrackingFolders)
- [msdyn_aioptimization_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aioptimization_PrincipalObjectAttributeAccesses)
- [msdyn_aioptimization_ProcessSession](#BKMK_msdyn_aioptimization_ProcessSession)
- [msdyn_aioptimization_SyncErrors](#BKMK_msdyn_aioptimization_SyncErrors)

### <a name="BKMK_msdyn_aioptimization_AsyncOperations"></a> msdyn_aioptimization_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_aioptimization_AsyncOperations](asyncoperation.md#BKMK_msdyn_aioptimization_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_BulkDeleteFailures"></a> msdyn_aioptimization_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_aioptimization_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aioptimization_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_DuplicateBaseRecord"></a> msdyn_aioptimization_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_aioptimization_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_aioptimization_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_DuplicateMatchingRecord"></a> msdyn_aioptimization_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_aioptimization_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_aioptimization_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_MailboxTrackingFolders"></a> msdyn_aioptimization_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_aioptimization_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aioptimization_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_PrincipalObjectAttributeAccesses"></a> msdyn_aioptimization_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_aioptimization_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aioptimization_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_ProcessSession"></a> msdyn_aioptimization_ProcessSession

Many-To-One Relationship: [processsession msdyn_aioptimization_ProcessSession](processsession.md#BKMK_msdyn_aioptimization_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aioptimization_SyncErrors"></a> msdyn_aioptimization_SyncErrors

Many-To-One Relationship: [syncerror msdyn_aioptimization_SyncErrors](syncerror.md#BKMK_msdyn_aioptimization_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aioptimization_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

