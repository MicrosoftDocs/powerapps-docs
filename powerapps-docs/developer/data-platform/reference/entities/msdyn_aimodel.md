---
title: "AI Model (msdyn_AIModel) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AI Model (msdyn_AIModel) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AI Model (msdyn_AIModel) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the AI Model (msdyn_AIModel) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddToFeedbackLoop`<br />Event: False |<xref:Microsoft.Dynamics.CRM.AddToFeedbackLoop?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Assign`<br />Event: True |`PATCH` /msdyn_aimodels(*msdyn_aimodelid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `BatchPrediction`<br />Event: False |<xref:Microsoft.Dynamics.CRM.BatchPrediction?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Create`<br />Event: False |`POST` /msdyn_aimodels<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /msdyn_aimodels(*msdyn_aimodelid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Predict`<br />Event: False |<xref:Microsoft.Dynamics.CRM.Predict?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PredictByReference`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PredictByReference?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PredictionSchema`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PredictionSchema?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: False |`GET` /msdyn_aimodels(*msdyn_aimodelid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /msdyn_aimodels<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SchedulePrediction`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SchedulePrediction?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ScheduleRetrain`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ScheduleRetrain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `SetState`<br />Event: True |`PATCH` /msdyn_aimodels(*msdyn_aimodelid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `UnschedulePrediction`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UnschedulePrediction?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Update`<br />Event: False |`PATCH` /msdyn_aimodels(*msdyn_aimodelid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_aimodels(*msdyn_aimodelid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AI Model (msdyn_AIModel) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AI Model** |
| **DisplayCollectionName** | **AI Models** |
| **SchemaName** | `msdyn_AIModel` |
| **CollectionSchemaName** | `msdyn_AIModels` |
| **EntitySetName** | `msdyn_aimodels`|
| **LogicalName** | `msdyn_aimodel` |
| **LogicalCollectionName** | `msdyn_aimodels` |
| **PrimaryIdAttribute** | `msdyn_aimodelid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_ActiveRunConfigurationId](#BKMK_msdyn_ActiveRunConfigurationId)
- [msdyn_AIModelCatalog](#BKMK_msdyn_AIModelCatalog)
- [msdyn_AIModelId](#BKMK_msdyn_AIModelId)
- [msdyn_ModelCreationContext](#BKMK_msdyn_ModelCreationContext)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_RetrainWorkflowId](#BKMK_msdyn_RetrainWorkflowId)
- [msdyn_ScheduleInferenceWorkflowId](#BKMK_msdyn_ScheduleInferenceWorkflowId)
- [msdyn_ShareWithOrganizationOnCreate](#BKMK_msdyn_ShareWithOrganizationOnCreate)
- [msdyn_TemplateId](#BKMK_msdyn_TemplateId)
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

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the form is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Tells whether the component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_msdyn_ActiveRunConfigurationId"></a> msdyn_ActiveRunConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the active run configuration id associated with AIModel.**|
|DisplayName|**ActiveRunConfigurationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_activerunconfigurationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_msdyn_AIModelCatalog"></a> msdyn_AIModelCatalog

|Property|Value|
|---|---|
|Description|**Lookup to AI Model Catalog**|
|DisplayName|**AI Model Catalog**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aimodelcatalog`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_aimodelcatalog|

### <a name="BKMK_msdyn_AIModelId"></a> msdyn_AIModelId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AIModel**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aimodelid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_ModelCreationContext"></a> msdyn_ModelCreationContext

|Property|Value|
|---|---|
|Description||
|DisplayName|**ModelCreationContext**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelcreationcontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_Name"></a> msdyn_Name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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
|MaxLength|100|

### <a name="BKMK_msdyn_RetrainWorkflowId"></a> msdyn_RetrainWorkflowId

|Property|Value|
|---|---|
|Description|**Unique identifier for Retrain Process associated with AI Model.**|
|DisplayName|**RetrainWorkflowId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_retrainworkflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_msdyn_ScheduleInferenceWorkflowId"></a> msdyn_ScheduleInferenceWorkflowId

|Property|Value|
|---|---|
|Description|**Unique identifier for Schedule Inference Process associated with AI Model.**|
|DisplayName|**ScheduleInferenceWorkflowId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_scheduleinferenceworkflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_msdyn_ShareWithOrganizationOnCreate"></a> msdyn_ShareWithOrganizationOnCreate

|Property|Value|
|---|---|
|Description||
|DisplayName|**ShareWithOrganizationOnCreate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sharewithorganizationoncreate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_aimodel_msdyn_sharewithorganizationoncreate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_TemplateId"></a> msdyn_TemplateId

|Property|Value|
|---|---|
|Description|**Unique identifier for AITemplate associated with AIModel.**|
|DisplayName|**Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_templateid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|msdyn_aitemplate|

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
|Description|**Status of the AIModel**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aimodel_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Inactive**<br />DefaultStatus: 0<br />InvariantName: `Inactive`|
|1|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AIModel**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aimodel_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Inactive**<br />State:0<br />TransitionData: None|
|1|Label: **Active**<br />State:1<br />TransitionData: None|

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

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [msdyn_AIModelIdUnique](#BKMK_msdyn_AIModelIdUnique)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentState"></a> ComponentState

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Component State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentstate`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`componentstate`|

#### ComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Published**|
|1|**Unpublished**|
|2|**Deleted**|
|3|**Deleted Unpublished**|

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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
|DisplayName|**Is Managed**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

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

### <a name="BKMK_msdyn_AIModelIdUnique"></a> msdyn_AIModelIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aimodelidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Record Overwrite Time**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overwritetime`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated solution.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Solution**|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`supportingsolutionid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

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

- [business_unit_msdyn_aimodel](#BKMK_business_unit_msdyn_aimodel)
- [lk_msdyn_aimodel_createdby](#BKMK_lk_msdyn_aimodel_createdby)
- [lk_msdyn_aimodel_createdonbehalfby](#BKMK_lk_msdyn_aimodel_createdonbehalfby)
- [lk_msdyn_aimodel_modifiedby](#BKMK_lk_msdyn_aimodel_modifiedby)
- [lk_msdyn_aimodel_modifiedonbehalfby](#BKMK_lk_msdyn_aimodel_modifiedonbehalfby)
- [msdyn_aitemplate_msdyn_aimodel](#BKMK_msdyn_aitemplate_msdyn_aimodel)
- [msdyn_retrainworkflow_msdyn_toaimodel](#BKMK_msdyn_retrainworkflow_msdyn_toaimodel)
- [msdyn_scheduleinferenceworkflow_msdyn_toaimodel](#BKMK_msdyn_scheduleinferenceworkflow_msdyn_toaimodel)
- [owner_msdyn_aimodel](#BKMK_owner_msdyn_aimodel)
- [team_msdyn_aimodel](#BKMK_team_msdyn_aimodel)
- [user_msdyn_aimodel](#BKMK_user_msdyn_aimodel)

### <a name="BKMK_business_unit_msdyn_aimodel"></a> business_unit_msdyn_aimodel

One-To-Many Relationship: [businessunit business_unit_msdyn_aimodel](businessunit.md#BKMK_business_unit_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aimodel_createdby"></a> lk_msdyn_aimodel_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aimodel_createdby](systemuser.md#BKMK_lk_msdyn_aimodel_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aimodel_createdonbehalfby"></a> lk_msdyn_aimodel_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aimodel_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aimodel_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aimodel_modifiedby"></a> lk_msdyn_aimodel_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aimodel_modifiedby](systemuser.md#BKMK_lk_msdyn_aimodel_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aimodel_modifiedonbehalfby"></a> lk_msdyn_aimodel_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aimodel_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aimodel_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aitemplate_msdyn_aimodel"></a> msdyn_aitemplate_msdyn_aimodel

One-To-Many Relationship: [msdyn_aitemplate msdyn_aitemplate_msdyn_aimodel](msdyn_aitemplate.md#BKMK_msdyn_aitemplate_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aitemplate`|
|ReferencedAttribute|`msdyn_aitemplateid`|
|ReferencingAttribute|`msdyn_templateid`|
|ReferencingEntityNavigationPropertyName|`msdyn_TemplateId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_retrainworkflow_msdyn_toaimodel"></a> msdyn_retrainworkflow_msdyn_toaimodel

One-To-Many Relationship: [workflow msdyn_retrainworkflow_msdyn_toaimodel](workflow.md#BKMK_msdyn_retrainworkflow_msdyn_toaimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`msdyn_retrainworkflowid`|
|ReferencingEntityNavigationPropertyName|`msdyn_retrainworkflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_scheduleinferenceworkflow_msdyn_toaimodel"></a> msdyn_scheduleinferenceworkflow_msdyn_toaimodel

One-To-Many Relationship: [workflow msdyn_scheduleinferenceworkflow_msdyn_toaimodel](workflow.md#BKMK_msdyn_scheduleinferenceworkflow_msdyn_toaimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`msdyn_scheduleinferenceworkflowid`|
|ReferencingEntityNavigationPropertyName|`msdyn_scheduleinferenceworkflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_aimodel"></a> owner_msdyn_aimodel

One-To-Many Relationship: [owner owner_msdyn_aimodel](owner.md#BKMK_owner_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_aimodel"></a> team_msdyn_aimodel

One-To-Many Relationship: [team team_msdyn_aimodel](team.md#BKMK_team_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_aimodel"></a> user_msdyn_aimodel

One-To-Many Relationship: [systemuser user_msdyn_aimodel](systemuser.md#BKMK_user_msdyn_aimodel)

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

- [msdyn_AIBDatasetsContainer_msdyn_AIModelI](#BKMK_msdyn_AIBDatasetsContainer_msdyn_AIModelI)
- [msdyn_AIBFeedbackLoop_msdyn_AIModel](#BKMK_msdyn_AIBFeedbackLoop_msdyn_AIModel)
- [msdyn_aimodel_Annotations](#BKMK_msdyn_aimodel_Annotations)
- [msdyn_aimodel_AsyncOperations](#BKMK_msdyn_aimodel_AsyncOperations)
- [msdyn_aimodel_BulkDeleteFailures](#BKMK_msdyn_aimodel_BulkDeleteFailures)
- [msdyn_aimodel_MailboxTrackingFolders](#BKMK_msdyn_aimodel_MailboxTrackingFolders)
- [msdyn_aimodel_msdyn_aiconfiguration](#BKMK_msdyn_aimodel_msdyn_aiconfiguration)
- [msdyn_aimodel_msdyn_aievent](#BKMK_msdyn_aimodel_msdyn_aievent)
- [msdyn_aimodel_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses)
- [msdyn_aimodel_ProcessSession](#BKMK_msdyn_aimodel_ProcessSession)
- [msdyn_aimodel_SyncErrors](#BKMK_msdyn_aimodel_SyncErrors)
- [msdyn_AIPluginOperation_AIModel](#BKMK_msdyn_AIPluginOperation_AIModel)

### <a name="BKMK_msdyn_AIBDatasetsContainer_msdyn_AIModelI"></a> msdyn_AIBDatasetsContainer_msdyn_AIModelI

Many-To-One Relationship: [msdyn_aibdatasetscontainer msdyn_AIBDatasetsContainer_msdyn_AIModelI](msdyn_aibdatasetscontainer.md#BKMK_msdyn_AIBDatasetsContainer_msdyn_AIModelI)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetscontainer`|
|ReferencingAttribute|`msdyn_aimodelid`|
|ReferencedEntityNavigationPropertyName|`msdyn_AIBDatasetsContainer_msdyn_AIModelI`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_AIBFeedbackLoop_msdyn_AIModel"></a> msdyn_AIBFeedbackLoop_msdyn_AIModel

Many-To-One Relationship: [msdyn_aibfeedbackloop msdyn_AIBFeedbackLoop_msdyn_AIModel](msdyn_aibfeedbackloop.md#BKMK_msdyn_AIBFeedbackLoop_msdyn_AIModel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfeedbackloop`|
|ReferencingAttribute|`msdyn_aimodelid`|
|ReferencedEntityNavigationPropertyName|`msdyn_AIBFeedbackLoop_msdyn_AIModel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_Annotations"></a> msdyn_aimodel_Annotations

Many-To-One Relationship: [annotation msdyn_aimodel_Annotations](annotation.md#BKMK_msdyn_aimodel_Annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_Annotations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_AsyncOperations"></a> msdyn_aimodel_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_aimodel_AsyncOperations](asyncoperation.md#BKMK_msdyn_aimodel_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_BulkDeleteFailures"></a> msdyn_aimodel_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_aimodel_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aimodel_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_MailboxTrackingFolders"></a> msdyn_aimodel_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_aimodel_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aimodel_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_msdyn_aiconfiguration"></a> msdyn_aimodel_msdyn_aiconfiguration

Many-To-One Relationship: [msdyn_aiconfiguration msdyn_aimodel_msdyn_aiconfiguration](msdyn_aiconfiguration.md#BKMK_msdyn_aimodel_msdyn_aiconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiconfiguration`|
|ReferencingAttribute|`msdyn_aimodelid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_msdyn_aiconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_msdyn_aievent"></a> msdyn_aimodel_msdyn_aievent

Many-To-One Relationship: [msdyn_aievent msdyn_aimodel_msdyn_aievent](msdyn_aievent.md#BKMK_msdyn_aimodel_msdyn_aievent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievent`|
|ReferencingAttribute|`msdyn_aimodelid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_msdyn_aievent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses"></a> msdyn_aimodel_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_aimodel_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aimodel_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_ProcessSession"></a> msdyn_aimodel_ProcessSession

Many-To-One Relationship: [processsession msdyn_aimodel_ProcessSession](processsession.md#BKMK_msdyn_aimodel_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aimodel_SyncErrors"></a> msdyn_aimodel_SyncErrors

Many-To-One Relationship: [syncerror msdyn_aimodel_SyncErrors](syncerror.md#BKMK_msdyn_aimodel_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aimodel_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_AIPluginOperation_AIModel"></a> msdyn_AIPluginOperation_AIModel

Many-To-One Relationship: [aipluginoperation msdyn_AIPluginOperation_AIModel](aipluginoperation.md#BKMK_msdyn_AIPluginOperation_AIModel)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`msdyn_aimodel`|
|ReferencedEntityNavigationPropertyName|`msdyn_AIPluginOperation_AIModel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

### <a name="BKMK_botcomponent_msdyn_aimodel"></a> botcomponent_msdyn_aimodel

See [botcomponent botcomponent_msdyn_aimodel Many-To-Many Relationship](botcomponent.md#BKMK_botcomponent_msdyn_aimodel)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_msdyn_aimodel`|
|IsCustomizable|False|
|SchemaName|`botcomponent_msdyn_aimodel`|
|IntersectAttribute|`msdyn_aimodelid`|
|NavigationPropertyName|`botcomponent_msdyn_aimodel`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_aimodel?displayProperty=fullName>
