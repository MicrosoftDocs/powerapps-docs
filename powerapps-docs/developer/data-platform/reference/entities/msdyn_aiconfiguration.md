---
title: "AI Configuration (msdyn_AIConfiguration) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AI Configuration (msdyn_AIConfiguration) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AI Configuration (msdyn_AIConfiguration) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the AI Configuration (msdyn_AIConfiguration) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `CancelTraining`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CancelTraining?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Create`<br />Event: False |`POST` /msdyn_aiconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `PublishAIConfiguration`<br />Event: False |<xref:Microsoft.Dynamics.CRM.PublishAIConfiguration?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `QuickTest`<br />Event: False |<xref:Microsoft.Dynamics.CRM.QuickTest?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: False |`GET` /msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /msdyn_aiconfigurations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `ScheduleTraining`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ScheduleTraining?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Train`<br />Event: False |<xref:Microsoft.Dynamics.CRM.Train?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `UnpublishAIConfiguration`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UnpublishAIConfiguration?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `UnscheduleTraining`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UnscheduleTraining?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Update`<br />Event: False |`PATCH` /msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the AI Configuration (msdyn_AIConfiguration) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AI Configuration** |
| **DisplayCollectionName** | **AI Configurations** |
| **SchemaName** | `msdyn_AIConfiguration` |
| **CollectionSchemaName** | `msdyn_AIConfigurations` |
| **EntitySetName** | `msdyn_aiconfigurations`|
| **LogicalName** | `msdyn_aiconfiguration` |
| **LogicalCollectionName** | `msdyn_aiconfigurations` |
| **PrimaryIdAttribute** | `msdyn_aiconfigurationid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_AIConfigurationId](#BKMK_msdyn_AIConfigurationId)
- [msdyn_AIModelId](#BKMK_msdyn_AIModelId)
- [msdyn_ConnectionReferenceId](#BKMK_msdyn_ConnectionReferenceId)
- [msdyn_CreatedFromConfigurationId](#BKMK_msdyn_CreatedFromConfigurationId)
- [msdyn_CustomConfiguration](#BKMK_msdyn_CustomConfiguration)
- [msdyn_DataBinding](#BKMK_msdyn_DataBinding)
- [msdyn_lasterrors](#BKMK_msdyn_lasterrors)
- [msdyn_lasttrainorrundate](#BKMK_msdyn_lasttrainorrundate)
- [msdyn_MajorIterationNumber](#BKMK_msdyn_MajorIterationNumber)
- [msdyn_MinorIterationNumber](#BKMK_msdyn_MinorIterationNumber)
- [msdyn_ModelAction](#BKMK_msdyn_ModelAction)
- [msdyn_ModelData](#BKMK_msdyn_ModelData)
- [msdyn_modelglobalexplainability](#BKMK_msdyn_modelglobalexplainability)
- [msdyn_ModelPerformance](#BKMK_msdyn_ModelPerformance)
- [msdyn_ModelProvisioningMetadata](#BKMK_msdyn_ModelProvisioningMetadata)
- [msdyn_ModelProvisioningStatus](#BKMK_msdyn_ModelProvisioningStatus)
- [msdyn_ModelRunDataSpecification](#BKMK_msdyn_ModelRunDataSpecification)
- [msdyn_Name](#BKMK_msdyn_Name)
- [msdyn_ResourceInfo](#BKMK_msdyn_ResourceInfo)
- [msdyn_RunConfiguration](#BKMK_msdyn_RunConfiguration)
- [msdyn_SchedulingOptions](#BKMK_msdyn_SchedulingOptions)
- [msdyn_TemplateVersion](#BKMK_msdyn_TemplateVersion)
- [msdyn_TrainedModelAIConfigurationPareId](#BKMK_msdyn_TrainedModelAIConfigurationPareId)
- [msdyn_Type](#BKMK_msdyn_Type)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
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

### <a name="BKMK_msdyn_AIConfigurationId"></a> msdyn_AIConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AIConfiguration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aiconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_AIModelId"></a> msdyn_AIModelId

|Property|Value|
|---|---|
|Description|**Unique identifier for AIModel associated with AIConfiguration.**|
|DisplayName|**AIModel**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aimodelid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|msdyn_aimodel|

### <a name="BKMK_msdyn_ConnectionReferenceId"></a> msdyn_ConnectionReferenceId

|Property|Value|
|---|---|
|Description|**Unique identifier for Connection Reference associated with AIConfiguration.**|
|DisplayName|**Connection Reference Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_connectionreferenceid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|connectionreference|

### <a name="BKMK_msdyn_CreatedFromConfigurationId"></a> msdyn_CreatedFromConfigurationId

|Property|Value|
|---|---|
|Description||
|DisplayName|**CreatedFromConfigurationId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_createdfromconfigurationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_aiconfiguration|

### <a name="BKMK_msdyn_CustomConfiguration"></a> msdyn_CustomConfiguration

|Property|Value|
|---|---|
|Description||
|DisplayName|**CustomConfiguration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_customconfiguration`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_DataBinding"></a> msdyn_DataBinding

|Property|Value|
|---|---|
|Description||
|DisplayName|**DataBinding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_databinding`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_msdyn_lasterrors"></a> msdyn_lasterrors

|Property|Value|
|---|---|
|Description||
|DisplayName|**LastErrors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lasterrors`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_msdyn_lasttrainorrundate"></a> msdyn_lasttrainorrundate

|Property|Value|
|---|---|
|Description||
|DisplayName|**LastTrainOrRunDate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lasttrainorrundate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_MajorIterationNumber"></a> msdyn_MajorIterationNumber

|Property|Value|
|---|---|
|Description||
|DisplayName|**MajorIterationNumber**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_majoriterationnumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_msdyn_MinorIterationNumber"></a> msdyn_MinorIterationNumber

|Property|Value|
|---|---|
|Description||
|DisplayName|**MinorIterationNumber**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_minoriterationnumber`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_ModelAction"></a> msdyn_ModelAction

|Property|Value|
|---|---|
|Description|**Model Action**|
|DisplayName|**ModelAction**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelaction`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_ModelData"></a> msdyn_ModelData

|Property|Value|
|---|---|
|Description||
|DisplayName|**ModelData**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modeldata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_modelglobalexplainability"></a> msdyn_modelglobalexplainability

|Property|Value|
|---|---|
|Description||
|DisplayName|**ModelGlobalExplainability**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelglobalexplainability`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_msdyn_ModelPerformance"></a> msdyn_ModelPerformance

|Property|Value|
|---|---|
|Description||
|DisplayName|**ModelPerformance**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelperformance`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msdyn_ModelProvisioningMetadata"></a> msdyn_ModelProvisioningMetadata

|Property|Value|
|---|---|
|Description|**Model Provisioning Metadata**|
|DisplayName|**ModelProvisioningMetadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelprovisioningmetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msdyn_ModelProvisioningStatus"></a> msdyn_ModelProvisioningStatus

|Property|Value|
|---|---|
|Description|**Model Provisioning Status**|
|DisplayName|**ModelProvisioningStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelprovisioningstatus`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000000|

### <a name="BKMK_msdyn_ModelRunDataSpecification"></a> msdyn_ModelRunDataSpecification

|Property|Value|
|---|---|
|Description||
|DisplayName|**ModelRunDataSpecification**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_modelrundataspecification`|
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

### <a name="BKMK_msdyn_ResourceInfo"></a> msdyn_ResourceInfo

|Property|Value|
|---|---|
|Description||
|DisplayName|**ResourceInfo**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_resourceinfo`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_msdyn_RunConfiguration"></a> msdyn_RunConfiguration

|Property|Value|
|---|---|
|Description|**Run Configuration**|
|DisplayName|**RunConfiguration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_runconfiguration`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_SchedulingOptions"></a> msdyn_SchedulingOptions

|Property|Value|
|---|---|
|Description||
|DisplayName|**SchedulingOptions**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_schedulingoptions`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|5000|

### <a name="BKMK_msdyn_TemplateVersion"></a> msdyn_TemplateVersion

|Property|Value|
|---|---|
|Description|**Template Version**|
|DisplayName|**TemplateVersion**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_templateversion`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_TrainedModelAIConfigurationPareId"></a> msdyn_TrainedModelAIConfigurationPareId

|Property|Value|
|---|---|
|Description|**Unique identifier for AIConfiguration associated with AIConfiguration.**|
|DisplayName|**TrainedModelAIConfigurationParent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_trainedmodelaiconfigurationpareid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_aiconfiguration|

### <a name="BKMK_msdyn_Type"></a> msdyn_Type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_type`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_aiconfiguration_msdyn_type`|

#### msdyn_Type Choices/Options

|Value|Label|
|---|---|
|190690000|**TrainingConfiguration**|
|190690001|**RunConfiguration**|

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

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the AIConfiguration**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aiconfiguration_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />DefaultStatus: 0<br />InvariantName: `Draft`|
|1|Label: **InProgress**<br />DefaultStatus: 1<br />InvariantName: `InProgress`|
|2|Label: **Done**<br />DefaultStatus: 6<br />InvariantName: `Done`|
|3|Label: **Failed**<br />DefaultStatus: 9<br />InvariantName: `Failed`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the AIConfiguration**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|SystemRequired|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_aiconfiguration_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />State:0<br />TransitionData: None|
|1|Label: **Training**<br />State:1<br />TransitionData: None|
|2|Label: **Cancelling**<br />State:1<br />TransitionData: None|
|3|Label: **Publishing**<br />State:1<br />TransitionData: None|
|4|Label: **Unpublishing**<br />State:1<br />TransitionData: None|
|5|Label: **Deleting**<br />State:1<br />TransitionData: None|
|6|Label: **Trained**<br />State:2<br />TransitionData: None|
|7|Label: **Published**<br />State:2<br />TransitionData: None|
|8|Label: **Scheduled**<br />State:2<br />TransitionData: None|
|9|Label: **TrainFailed**<br />State:3<br />TransitionData: None|
|10|Label: **PublishFailed**<br />State:3<br />TransitionData: None|
|11|Label: **UnpublishFailed**<br />State:3<br />TransitionData: None|
|12|Label: **CancelFailed**<br />State:3<br />TransitionData: None|
|13|Label: **DeleteFailed**<br />State:3<br />TransitionData: None|
|14|Label: **UnsuccessfulTraining**<br />State:2<br />TransitionData: None|

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
- [msdyn_AIConfigurationIdUnique](#BKMK_msdyn_AIConfigurationIdUnique)
- [msdyn_Model](#BKMK_msdyn_Model)
- [msdyn_Model_Name](#BKMK_msdyn_Model_Name)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
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

### <a name="BKMK_msdyn_AIConfigurationIdUnique"></a> msdyn_AIConfigurationIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aiconfigurationidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_Model"></a> msdyn_Model

|Property|Value|
|---|---|
|Description|**This is a file type attribute to store Ai builder Model.**|
|DisplayName|**msdyn\_Model**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_model`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_Model_Name"></a> msdyn_Model_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_model_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Unique identifier for the business unit that owns the record**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
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

- [FileAttachment_msdyn_AIConfiguration_msdyn_Model](#BKMK_FileAttachment_msdyn_AIConfiguration_msdyn_Model)
- [lk_msdyn_aiconfiguration_createdby](#BKMK_lk_msdyn_aiconfiguration_createdby)
- [lk_msdyn_aiconfiguration_createdonbehalfby](#BKMK_lk_msdyn_aiconfiguration_createdonbehalfby)
- [lk_msdyn_aiconfiguration_modifiedby](#BKMK_lk_msdyn_aiconfiguration_modifiedby)
- [lk_msdyn_aiconfiguration_modifiedonbehalfby](#BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby)
- [msdyn_AIConfiguration_ConnectionReference](#BKMK_msdyn_AIConfiguration_ConnectionReference)
- [msdyn_aiconfiguration_msdyn_aiconfiguration](#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration-many-to-one)
- [msdyn_aimodel_msdyn_aiconfiguration](#BKMK_msdyn_aimodel_msdyn_aiconfiguration)
- [msdyn_createdfromconfiguration_msdyn_toconfiguration](#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration-many-to-one)

### <a name="BKMK_FileAttachment_msdyn_AIConfiguration_msdyn_Model"></a> FileAttachment_msdyn_AIConfiguration_msdyn_Model

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_AIConfiguration_msdyn_Model](fileattachment.md#BKMK_FileAttachment_msdyn_AIConfiguration_msdyn_Model)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_model`|
|ReferencingEntityNavigationPropertyName|`msdyn_model`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiconfiguration_createdby"></a> lk_msdyn_aiconfiguration_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aiconfiguration_createdby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiconfiguration_createdonbehalfby"></a> lk_msdyn_aiconfiguration_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aiconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiconfiguration_modifiedby"></a> lk_msdyn_aiconfiguration_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aiconfiguration_modifiedby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby"></a> lk_msdyn_aiconfiguration_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aiconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_AIConfiguration_ConnectionReference"></a> msdyn_AIConfiguration_ConnectionReference

One-To-Many Relationship: [connectionreference msdyn_AIConfiguration_ConnectionReference](connectionreference.md#BKMK_msdyn_AIConfiguration_ConnectionReference)

|Property|Value|
|---|---|
|ReferencedEntity|`connectionreference`|
|ReferencedAttribute|`connectionreferenceid`|
|ReferencingAttribute|`msdyn_connectionreferenceid`|
|ReferencingEntityNavigationPropertyName|`msdyn_ConnectionReferenceId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration-many-to-one"></a> msdyn_aiconfiguration_msdyn_aiconfiguration

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_msdyn_aiconfiguration](#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`msdyn_trainedmodelaiconfigurationpareid`|
|ReferencingEntityNavigationPropertyName|`msdyn_TrainedModelAIConfigurationPareId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_aimodel_msdyn_aiconfiguration"></a> msdyn_aimodel_msdyn_aiconfiguration

One-To-Many Relationship: [msdyn_aimodel msdyn_aimodel_msdyn_aiconfiguration](msdyn_aimodel.md#BKMK_msdyn_aimodel_msdyn_aiconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aimodel`|
|ReferencedAttribute|`msdyn_aimodelid`|
|ReferencingAttribute|`msdyn_aimodelid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AIModelId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration-many-to-one"></a> msdyn_createdfromconfiguration_msdyn_toconfiguration

One-To-Many Relationship: [msdyn_aiconfiguration msdyn_createdfromconfiguration_msdyn_toconfiguration](#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_aiconfiguration`|
|ReferencedAttribute|`msdyn_aiconfigurationid`|
|ReferencingAttribute|`msdyn_createdfromconfigurationid`|
|ReferencingEntityNavigationPropertyName|`msdyn_CreatedFromConfigurationId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_aiconfiguration_AsyncOperations](#BKMK_msdyn_aiconfiguration_AsyncOperations)
- [msdyn_aiconfiguration_BulkDeleteFailures](#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)
- [msdyn_aiconfiguration_FileAttachments](#BKMK_msdyn_aiconfiguration_FileAttachments)
- [msdyn_aiconfiguration_MailboxTrackingFolders](#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)
- [msdyn_aiconfiguration_msdyn_aiconfiguration](#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration-one-to-many)
- [msdyn_aiconfiguration_msdyn_aiconfigurationsearch](#BKMK_msdyn_aiconfiguration_msdyn_aiconfigurationsearch)
- [msdyn_aiconfiguration_msdyn_aievent](#BKMK_msdyn_aiconfiguration_msdyn_aievent)
- [msdyn_aiconfiguration_msdyn_aiodtrainingimage](#BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage)
- [msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_aiconfiguration_ProcessSession](#BKMK_msdyn_aiconfiguration_ProcessSession)
- [msdyn_aiconfiguration_SyncErrors](#BKMK_msdyn_aiconfiguration_SyncErrors)
- [msdyn_createdfromconfiguration_msdyn_toconfiguration](#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration-one-to-many)
- [msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId](#BKMK_msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId)

### <a name="BKMK_msdyn_aiconfiguration_AsyncOperations"></a> msdyn_aiconfiguration_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_aiconfiguration_AsyncOperations](asyncoperation.md#BKMK_msdyn_aiconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_BulkDeleteFailures"></a> msdyn_aiconfiguration_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_aiconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_FileAttachments"></a> msdyn_aiconfiguration_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_aiconfiguration_FileAttachments](fileattachment.md#BKMK_msdyn_aiconfiguration_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_MailboxTrackingFolders"></a> msdyn_aiconfiguration_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_aiconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration-one-to-many"></a> msdyn_aiconfiguration_msdyn_aiconfiguration

Many-To-One Relationship: [msdyn_aiconfiguration msdyn_aiconfiguration_msdyn_aiconfiguration](#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiconfiguration`|
|ReferencingAttribute|`msdyn_trainedmodelaiconfigurationpareid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_msdyn_aiconfiguration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiconfigurationsearch"></a> msdyn_aiconfiguration_msdyn_aiconfigurationsearch

Many-To-One Relationship: [msdyn_aiconfigurationsearch msdyn_aiconfiguration_msdyn_aiconfigurationsearch](msdyn_aiconfigurationsearch.md#BKMK_msdyn_aiconfiguration_msdyn_aiconfigurationsearch)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiconfigurationsearch`|
|ReferencingAttribute|`msdyn_aiconfiguration`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_msdyn_aiconfigurationsearch`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aievent"></a> msdyn_aiconfiguration_msdyn_aievent

Many-To-One Relationship: [msdyn_aievent msdyn_aiconfiguration_msdyn_aievent](msdyn_aievent.md#BKMK_msdyn_aiconfiguration_msdyn_aievent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievent`|
|ReferencingAttribute|`msdyn_aiconfigurationid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_msdyn_aievent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage"></a> msdyn_aiconfiguration_msdyn_aiodtrainingimage

Many-To-One Relationship: [msdyn_aiodtrainingimage msdyn_aiconfiguration_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingimage`|
|ReferencingAttribute|`msdyn_aiconfigurationid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_msdyn_aiodtrainingimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_aiconfiguration_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_ProcessSession"></a> msdyn_aiconfiguration_ProcessSession

Many-To-One Relationship: [processsession msdyn_aiconfiguration_ProcessSession](processsession.md#BKMK_msdyn_aiconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiconfiguration_SyncErrors"></a> msdyn_aiconfiguration_SyncErrors

Many-To-One Relationship: [syncerror msdyn_aiconfiguration_SyncErrors](syncerror.md#BKMK_msdyn_aiconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_aiconfiguration_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration-one-to-many"></a> msdyn_createdfromconfiguration_msdyn_toconfiguration

Many-To-One Relationship: [msdyn_aiconfiguration msdyn_createdfromconfiguration_msdyn_toconfiguration](#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiconfiguration`|
|ReferencingAttribute|`msdyn_createdfromconfigurationid`|
|ReferencedEntityNavigationPropertyName|`msdyn_createdfromconfiguration_msdyn_toconfiguration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId"></a> msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId

Many-To-One Relationship: [msdyn_aifptrainingdocument msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId](msdyn_aifptrainingdocument.md#BKMK_msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aifptrainingdocument`|
|ReferencingAttribute|`msdyn_aiconfigurationid`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [msdyn_aidocumenttemplate_msdyn_aiconfig](#BKMK_msdyn_aidocumenttemplate_msdyn_aiconfig)
- [msdyn_aiodlabel_msdyn_aiconfiguration](#BKMK_msdyn_aiodlabel_msdyn_aiconfiguration)

### <a name="BKMK_msdyn_aidocumenttemplate_msdyn_aiconfig"></a> msdyn_aidocumenttemplate_msdyn_aiconfig

See [msdyn_aidocumenttemplate msdyn_aidocumenttemplate_msdyn_aiconfig Many-To-Many Relationship](msdyn_aidocumenttemplate.md#BKMK_msdyn_aidocumenttemplate_msdyn_aiconfig)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_aiconfiguration_documenttemplate`|
|IsCustomizable|False|
|SchemaName|`msdyn_aidocumenttemplate_msdyn_aiconfig`|
|IntersectAttribute|`msdyn_aiconfigurationid`|
|NavigationPropertyName|`msdyn_aidocumenttemplate_msdyn_aiconfig`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_aiodlabel_msdyn_aiconfiguration"></a> msdyn_aiodlabel_msdyn_aiconfiguration

See [msdyn_aiodlabel msdyn_aiodlabel_msdyn_aiconfiguration Many-To-Many Relationship](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_msdyn_aiconfiguration)

|Property|Value|
|---|---|
|IntersectEntityName|`msdyn_aiodlabel_msdyn_aiconfiguration`|
|IsCustomizable|False|
|SchemaName|`msdyn_aiodlabel_msdyn_aiconfiguration`|
|IntersectAttribute|`msdyn_aiconfigurationid`|
|NavigationPropertyName|`msdyn_aiodlabel_msdyn_aiconfiguration`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_aiconfiguration?displayProperty=fullName>
