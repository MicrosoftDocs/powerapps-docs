---
title: "AI Evaluation Run (msdyn_AIEvaluationRun) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AI Evaluation Run (msdyn_AIEvaluationRun) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AI Evaluation Run (msdyn_AIEvaluationRun) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the AI Evaluation Run (msdyn_AIEvaluationRun) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_aievaluationruns(*msdyn_aievaluationrunid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_aievaluationruns<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_aievaluationruns(*msdyn_aievaluationrunid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_aievaluationruns(*msdyn_aievaluationrunid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_aievaluationruns<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_aievaluationruns(*msdyn_aievaluationrunid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_aievaluationruns(*msdyn_aievaluationrunid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_aievaluationruns(*msdyn_aievaluationrunid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AI Evaluation Run (msdyn_AIEvaluationRun) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AI Evaluation Run** |
| **DisplayCollectionName** | **AI Evaluation Run** |
| **SchemaName** | `msdyn_AIEvaluationRun` |
| **CollectionSchemaName** | `msdyn_AIEvaluationRuns` |
| **EntitySetName** | `msdyn_aievaluationruns`|
| **LogicalName** | `msdyn_aievaluationrun` |
| **LogicalCollectionName** | `msdyn_aievaluationruns` |
| **PrimaryIdAttribute** | `msdyn_aievaluationrunid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AdditionalResponseMetadata](#BKMK_msdyn_AdditionalResponseMetadata)
- [msdyn_AIEvaluationConfigurationId](#BKMK_msdyn_AIEvaluationConfigurationId)
- [msdyn_AIEvaluationRunId](#BKMK_msdyn_AIEvaluationRunId)
- [msdyn_AIRunObjectId](#BKMK_msdyn_AIRunObjectId)
- [msdyn_AIRunObjectType](#BKMK_msdyn_AIRunObjectType)
- [msdyn_Comment](#BKMK_msdyn_Comment)
- [msdyn_CompletedOn](#BKMK_msdyn_CompletedOn)
- [msdyn_ErrorMessage](#BKMK_msdyn_ErrorMessage)
- [msdyn_EvaluationResult](#BKMK_msdyn_EvaluationResult)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_RunDuration](#BKMK_msdyn_RunDuration)
- [msdyn_RunStatus](#BKMK_msdyn_RunStatus)
- [msdyn_StartedOn](#BKMK_msdyn_StartedOn)
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

### <a name="BKMK_msdyn_AdditionalResponseMetadata"></a> msdyn_AdditionalResponseMetadata

|Property|Value|
|---|---|
|Description|**Addition Response Metadata.**|
|DisplayName|**Addition Response Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_additionalresponsemetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_AIEvaluationConfigurationId"></a> msdyn_AIEvaluationConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for AIEvaluationConfiguration associated with AIEvaluationRun.**|
|DisplayName|**AIEvaluationConfiguration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aievaluationconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|msdyn_aievaluationconfiguration|

### <a name="BKMK_msdyn_AIEvaluationRunId"></a> msdyn_AIEvaluationRunId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AIEvaluationRun**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aievaluationrunid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_AIRunObjectId"></a> msdyn_AIRunObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier for AIRunObject associated with AIEvaluationRun.**|
|DisplayName|**AIRunObject**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_airunobjectid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_AIRunObjectType"></a> msdyn_AIRunObjectType

|Property|Value|
|---|---|
|Description|**The Run Object type.**|
|DisplayName|**AIRunObjectType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_airunobjecttype`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_Comment"></a> msdyn_Comment

|Property|Value|
|---|---|
|Description|**Comment**|
|DisplayName|**Comment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_comment`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|400|

### <a name="BKMK_msdyn_CompletedOn"></a> msdyn_CompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when the evaluation run was completed.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_ErrorMessage"></a> msdyn_ErrorMessage

|Property|Value|
|---|---|
|Description|**The error message of the evaluation run.**|
|DisplayName|**ErrorMessage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errormessage`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_EvaluationResult"></a> msdyn_EvaluationResult

|Property|Value|
|---|---|
|Description||
|DisplayName|**Evaluation result**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_evaluationresult`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description|**The name of the AI test run.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_RunDuration"></a> msdyn_RunDuration

|Property|Value|
|---|---|
|Description||
|DisplayName|**Run Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_runduration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_RunStatus"></a> msdyn_RunStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**EvaluationRun Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_runstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_aievaluationrun_msdyn_runstatus`|

#### msdyn_RunStatus Choices/Options

|Value|Label|
|---|---|
|0|**Created**|
|1|**InProgress**|
|2|**Paused**|
|3|**Blocked**|
|4|**Succeeded**|
|5|**Failed**|
|6|**Canceled**|

### <a name="BKMK_msdyn_StartedOn"></a> msdyn_StartedOn

|Property|Value|
|---|---|
|Description|**Date and time when the evaluation run was started.**|
|DisplayName|**Started On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_startedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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
|Description|**Status of the AI Evaluation Run**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aievaluationrun_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AI Evaluation Run**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aievaluationrun_statuscode`|

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

- [business_unit_msdyn_aievaluationrun](#BKMK_business_unit_msdyn_aievaluationrun)
- [lk_msdyn_aievaluationrun_createdby](#BKMK_lk_msdyn_aievaluationrun_createdby)
- [lk_msdyn_aievaluationrun_createdonbehalfby](#BKMK_lk_msdyn_aievaluationrun_createdonbehalfby)
- [lk_msdyn_aievaluationrun_modifiedby](#BKMK_lk_msdyn_aievaluationrun_modifiedby)
- [lk_msdyn_aievaluationrun_modifiedonbehalfby](#BKMK_lk_msdyn_aievaluationrun_modifiedonbehalfby)
- [msdyn_aievaluationconfiguration_msdyn_aievaluationrun](#BKMK_msdyn_aievaluationconfiguration_msdyn_aievaluationrun)
- [owner_msdyn_aievaluationrun](#BKMK_owner_msdyn_aievaluationrun)
- [team_msdyn_aievaluationrun](#BKMK_team_msdyn_aievaluationrun)
- [user_msdyn_aievaluationrun](#BKMK_user_msdyn_aievaluationrun)

### <a name="BKMK_business_unit_msdyn_aievaluationrun"></a> business_unit_msdyn_aievaluationrun

One-To-Many Relationship: [businessunit business_unit_msdyn_aievaluationrun](businessunit.md#BKMK_business_unit_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationrun_createdby"></a> lk_msdyn_aievaluationrun_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationrun_createdby](systemuser.md#BKMK_lk_msdyn_aievaluationrun_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationrun_createdonbehalfby"></a> lk_msdyn_aievaluationrun_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationrun_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aievaluationrun_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationrun_modifiedby"></a> lk_msdyn_aievaluationrun_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationrun_modifiedby](systemuser.md#BKMK_lk_msdyn_aievaluationrun_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationrun_modifiedonbehalfby"></a> lk_msdyn_aievaluationrun_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationrun_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aievaluationrun_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aievaluationconfiguration_msdyn_aievaluationrun"></a> msdyn_aievaluationconfiguration_msdyn_aievaluationrun

One-To-Many Relationship: [msdyn_aievaluationconfiguration msdyn_aievaluationconfiguration_msdyn_aievaluationrun](msdyn_aievaluationconfiguration.md#BKMK_msdyn_aievaluationconfiguration_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aievaluationconfiguration`|
|ReferencedAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingAttribute|`msdyn_aievaluationconfigurationid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIEvaluationConfigurationId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_aievaluationrun"></a> owner_msdyn_aievaluationrun

One-To-Many Relationship: [owner owner_msdyn_aievaluationrun](owner.md#BKMK_owner_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_aievaluationrun"></a> team_msdyn_aievaluationrun

One-To-Many Relationship: [team team_msdyn_aievaluationrun](team.md#BKMK_team_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_aievaluationrun"></a> user_msdyn_aievaluationrun

One-To-Many Relationship: [systemuser user_msdyn_aievaluationrun](systemuser.md#BKMK_user_msdyn_aievaluationrun)

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

- [msdyn_aievaluationrun_AsyncOperations](#BKMK_msdyn_aievaluationrun_AsyncOperations)
- [msdyn_aievaluationrun_BulkDeleteFailures](#BKMK_msdyn_aievaluationrun_BulkDeleteFailures)
- [msdyn_aievaluationrun_MailboxTrackingFolders](#BKMK_msdyn_aievaluationrun_MailboxTrackingFolders)
- [msdyn_aievaluationrun_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aievaluationrun_PrincipalObjectAttributeAccesses)
- [msdyn_aievaluationrun_ProcessSession](#BKMK_msdyn_aievaluationrun_ProcessSession)
- [msdyn_aievaluationrun_SyncErrors](#BKMK_msdyn_aievaluationrun_SyncErrors)

### <a name="BKMK_msdyn_aievaluationrun_AsyncOperations"></a> msdyn_aievaluationrun_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_aievaluationrun_AsyncOperations](asyncoperation.md#BKMK_msdyn_aievaluationrun_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aievaluationrun_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aievaluationrun_BulkDeleteFailures"></a> msdyn_aievaluationrun_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_aievaluationrun_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aievaluationrun_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aievaluationrun_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aievaluationrun_MailboxTrackingFolders"></a> msdyn_aievaluationrun_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_aievaluationrun_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aievaluationrun_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aievaluationrun_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aievaluationrun_PrincipalObjectAttributeAccesses"></a> msdyn_aievaluationrun_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_aievaluationrun_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aievaluationrun_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aievaluationrun_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aievaluationrun_ProcessSession"></a> msdyn_aievaluationrun_ProcessSession

Many-To-One Relationship: [processsession msdyn_aievaluationrun_ProcessSession](processsession.md#BKMK_msdyn_aievaluationrun_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aievaluationrun_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aievaluationrun_SyncErrors"></a> msdyn_aievaluationrun_SyncErrors

Many-To-One Relationship: [syncerror msdyn_aievaluationrun_SyncErrors](syncerror.md#BKMK_msdyn_aievaluationrun_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aievaluationrun_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_aievaluationrun?displayProperty=fullName>
