---
title: "msdyn_AIConfiguration table/entity reference (Microsoft Dataverse) | Microsoft Docs"
description: "Includes schema information and supported messages for the msdyn_AIConfiguration table/entity."
ms.date: 05/23/2023
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "phecke"
ms.author: "pehecke"
search.audienceType: 
  - developer
---

# msdyn_AIConfiguration table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).



**Added by**: AISolution Solution


## Messages

|Message|Web API Operation|SDK class or method|
|-|-|-|
|CancelTraining|<xref:Microsoft.Dynamics.CRM.CancelTraining?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="CancelTraining"|
|Create|POST [*org URI*]/api/data/v9.2/msdyn_aiconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
|Delete|DELETE [*org URI*]/api/data/v9.2/msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|IsValidStateTransition|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType />|<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
|PublishAIConfiguration|<xref:Microsoft.Dynamics.CRM.PublishAIConfiguration?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="PublishAIConfiguration"|
|QuickTest|<xref:Microsoft.Dynamics.CRM.QuickTest?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="QuickTest"|
|Retrieve|GET [*org URI*]/api/data/v9.2/msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.2/msdyn_aiconfigurations<br />See [Query Data](/powerapps/developer/data-platform/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|ScheduleTraining|<xref:Microsoft.Dynamics.CRM.ScheduleTraining?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="ScheduleTraining"|
|SetState|PATCH [*org URI*]/api/data/v9.2/msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Train|<xref:Microsoft.Dynamics.CRM.Train?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="Train"|
|UnpublishAIConfiguration|<xref:Microsoft.Dynamics.CRM.UnpublishAIConfiguration?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="UnpublishAIConfiguration"|
|UnscheduleTraining|<xref:Microsoft.Dynamics.CRM.UnscheduleTraining?displayProperty=nameWithType />|<xref:Microsoft.Xrm.Sdk.OrganizationRequest><br/> where <xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName>="UnscheduleTraining"|
|Update|PATCH [*org URI*]/api/data/v9.2/msdyn_aiconfigurations(*msdyn_aiconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|
|UpdateMultiple||<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|msdyn_AIConfigurations|
|DisplayCollectionName|AI Configurations|
|DisplayName|AI Configuration|
|EntitySetName|msdyn_aiconfigurations|
|IsBPFEntity|False|
|LogicalCollectionName|msdyn_aiconfigurations|
|LogicalName|msdyn_aiconfiguration|
|OwnershipType|None|
|PrimaryIdAttribute|msdyn_aiconfigurationid|
|PrimaryNameAttribute|msdyn_name|
|SchemaName|msdyn_AIConfiguration|

<a name="writable-attributes"></a>

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

**Added by**: Basic Solution Solution

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


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|--------|-----|
|Description|Version in which the form is introduced.|
|DisplayName|Introduced Version|
|FormatName|VersionNumber|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|introducedversion|
|MaxLength|48|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|--------|-----|
|Description|Tells whether the component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_msdyn_AIConfigurationId"></a> msdyn_AIConfigurationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for entity instances|
|DisplayName|AIConfiguration|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|msdyn_aiconfigurationid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_msdyn_AIModelId"></a> msdyn_AIModelId

|Property|Value|
|--------|-----|
|Description|Unique identifier for AIModel associated with AIConfiguration.|
|DisplayName|AIModel|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_aimodelid|
|RequiredLevel|SystemRequired|
|Targets|msdyn_aimodel|
|Type|Lookup|


### <a name="BKMK_msdyn_ConnectionReferenceId"></a> msdyn_ConnectionReferenceId

|Property|Value|
|--------|-----|
|Description|Unique identifier for Connection Reference associated with AIConfiguration.|
|DisplayName|Connection Reference Id|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_connectionreferenceid|
|RequiredLevel|None|
|Targets|connectionreference|
|Type|Lookup|


### <a name="BKMK_msdyn_CreatedFromConfigurationId"></a> msdyn_CreatedFromConfigurationId

|Property|Value|
|--------|-----|
|Description||
|DisplayName|CreatedFromConfigurationId|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_createdfromconfigurationid|
|RequiredLevel|None|
|Targets|msdyn_aiconfiguration|
|Type|Lookup|


### <a name="BKMK_msdyn_CustomConfiguration"></a> msdyn_CustomConfiguration

|Property|Value|
|--------|-----|
|Description||
|DisplayName|CustomConfiguration|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_customconfiguration|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_DataBinding"></a> msdyn_DataBinding

|Property|Value|
|--------|-----|
|Description||
|DisplayName|DataBinding|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_databinding|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_lasterrors"></a> msdyn_lasterrors

|Property|Value|
|--------|-----|
|Description||
|DisplayName|LastErrors|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_lasterrors|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_lasttrainorrundate"></a> msdyn_lasttrainorrundate

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description||
|DisplayName|LastTrainOrRunDate|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_lasttrainorrundate|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_msdyn_MajorIterationNumber"></a> msdyn_MajorIterationNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName|MajorIterationNumber|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_majoriterationnumber|
|MaxValue|2147483647|
|MinValue|1|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_msdyn_MinorIterationNumber"></a> msdyn_MinorIterationNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName|MinorIterationNumber|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_minoriterationnumber|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_msdyn_ModelAction"></a> msdyn_ModelAction

|Property|Value|
|--------|-----|
|Description|Model Action|
|DisplayName|ModelAction|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modelaction|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_ModelData"></a> msdyn_ModelData

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ModelData|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modeldata|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_modelglobalexplainability"></a> msdyn_modelglobalexplainability

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ModelGlobalExplainability|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modelglobalexplainability|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_ModelPerformance"></a> msdyn_ModelPerformance

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ModelPerformance|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modelperformance|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_ModelProvisioningMetadata"></a> msdyn_ModelProvisioningMetadata

|Property|Value|
|--------|-----|
|Description|Model Provisioning Metadata|
|DisplayName|ModelProvisioningMetadata|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modelprovisioningmetadata|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_ModelProvisioningStatus"></a> msdyn_ModelProvisioningStatus

|Property|Value|
|--------|-----|
|Description|Model Provisioning Status|
|DisplayName|ModelProvisioningStatus|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modelprovisioningstatus|
|MaxLength|1000000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_ModelRunDataSpecification"></a> msdyn_ModelRunDataSpecification

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ModelRunDataSpecification|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_modelrundataspecification|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_Name"></a> msdyn_Name

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
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_msdyn_ResourceInfo"></a> msdyn_ResourceInfo

|Property|Value|
|--------|-----|
|Description||
|DisplayName|ResourceInfo|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_resourceinfo|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_RunConfiguration"></a> msdyn_RunConfiguration

|Property|Value|
|--------|-----|
|Description|Run Configuration|
|DisplayName|RunConfiguration|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_runconfiguration|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_SchedulingOptions"></a> msdyn_SchedulingOptions

|Property|Value|
|--------|-----|
|Description||
|DisplayName|SchedulingOptions|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_schedulingoptions|
|MaxLength|5000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_msdyn_TemplateVersion"></a> msdyn_TemplateVersion

|Property|Value|
|--------|-----|
|Description|Template Version|
|DisplayName|TemplateVersion|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_templateversion|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|SystemRequired|
|Type|Integer|


### <a name="BKMK_msdyn_TrainedModelAIConfigurationPareId"></a> msdyn_TrainedModelAIConfigurationPareId

|Property|Value|
|--------|-----|
|Description|Unique identifier for AIConfiguration associated with AIConfiguration.|
|DisplayName|TrainedModelAIConfigurationParent|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_trainedmodelaiconfigurationpareid|
|RequiredLevel|None|
|Targets|msdyn_aiconfiguration|
|Type|Lookup|


### <a name="BKMK_msdyn_Type"></a> msdyn_Type

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Type|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_type|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### msdyn_Type Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|190690000|TrainingConfiguration||
|190690001|RunConfiguration||



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


### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|--------|-----|
|Description|Status of the AIConfiguration|
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
|0|Draft|0|Draft|
|1|InProgress|1|InProgress|
|2|Done|6|Done|
|3|Failed|9|Failed|



### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|--------|-----|
|Description|Reason for the status of the AIConfiguration|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|SystemRequired|
|Type|Status|

#### statuscode Choices/Options

|Value|Label|State|
|-----|-----|-----|
|0|Draft|0|
|1|Training|1|
|2|Cancelling|1|
|3|Publishing|1|
|4|Unpublishing|1|
|5|Deleting|1|
|6|Trained|2|
|7|Published|2|
|8|Scheduled|2|
|9|TrainFailed|3|
|10|PublishFailed|3|
|11|UnpublishFailed|3|
|12|CancelFailed|3|
|13|DeleteFailed|3|
|14|UnsuccessfulTraining|2|



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

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msdyn_AIConfigurationIdUnique](#BKMK_msdyn_AIConfigurationIdUnique)
- [msdyn_AIModelIdName](#BKMK_msdyn_AIModelIdName)
- [msdyn_ConnectionReferenceIdName](#BKMK_msdyn_ConnectionReferenceIdName)
- [msdyn_CreatedFromConfigurationIdName](#BKMK_msdyn_CreatedFromConfigurationIdName)
- [msdyn_Model](#BKMK_msdyn_Model)
- [msdyn_Model_Name](#BKMK_msdyn_Model_Name)
- [msdyn_TrainedModelAIConfigurationPareIdName](#BKMK_msdyn_TrainedModelAIConfigurationPareIdName)
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
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



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


### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed||
|0|Unmanaged||

**DefaultValue**: 0



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


### <a name="BKMK_msdyn_AIConfigurationIdUnique"></a> msdyn_AIConfigurationIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_aiconfigurationidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


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


### <a name="BKMK_msdyn_ConnectionReferenceIdName"></a> msdyn_ConnectionReferenceIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_connectionreferenceidname|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_CreatedFromConfigurationIdName"></a> msdyn_CreatedFromConfigurationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_createdfromconfigurationidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_Model"></a> msdyn_Model

|Property|Value|
|--------|-----|
|Description|This is a file type attribute to store Ai builder Model.|
|DisplayName|msdyn_Model|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_model|
|RequiredLevel|None|
|Type|File|


### <a name="BKMK_msdyn_Model_Name"></a> msdyn_Model_Name

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_model_name|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_TrainedModelAIConfigurationPareIdName"></a> msdyn_TrainedModelAIConfigurationPareIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_trainedmodelaiconfigurationpareidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateOnly|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
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
|Description||
|DisplayName||
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|SystemRequired|
|Type|Integer|


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


### <a name="BKMK_SolutionId"></a> SolutionId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


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

- [msdyn_aiconfiguration_SyncErrors](#BKMK_msdyn_aiconfiguration_SyncErrors)
- [msdyn_aiconfiguration_AsyncOperations](#BKMK_msdyn_aiconfiguration_AsyncOperations)
- [msdyn_aiconfiguration_MailboxTrackingFolders](#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders)
- [msdyn_aiconfiguration_ProcessSession](#BKMK_msdyn_aiconfiguration_ProcessSession)
- [msdyn_aiconfiguration_BulkDeleteFailures](#BKMK_msdyn_aiconfiguration_BulkDeleteFailures)
- [msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses)
- [msdyn_aiconfiguration_msdyn_aiconfiguration](#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration)
- [msdyn_createdfromconfiguration_msdyn_toconfiguration](#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration)
- [msdyn_aiconfiguration_msdyn_aiodtrainingimage](#BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage)
- [msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId](#BKMK_msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId)


### <a name="BKMK_msdyn_aiconfiguration_SyncErrors"></a> msdyn_aiconfiguration_SyncErrors

**Added by**: System Solution Solution

Same as the [msdyn_aiconfiguration_SyncErrors](syncerror.md#BKMK_msdyn_aiconfiguration_SyncErrors) many-to-one relationship for the [syncerror](syncerror.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_AsyncOperations"></a> msdyn_aiconfiguration_AsyncOperations

**Added by**: System Solution Solution

Same as the [msdyn_aiconfiguration_AsyncOperations](asyncoperation.md#BKMK_msdyn_aiconfiguration_AsyncOperations) many-to-one relationship for the [asyncoperation](asyncoperation.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_MailboxTrackingFolders"></a> msdyn_aiconfiguration_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as the [msdyn_aiconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_aiconfiguration_MailboxTrackingFolders) many-to-one relationship for the [mailboxtrackingfolder](mailboxtrackingfolder.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_ProcessSession"></a> msdyn_aiconfiguration_ProcessSession

**Added by**: System Solution Solution

Same as the [msdyn_aiconfiguration_ProcessSession](processsession.md#BKMK_msdyn_aiconfiguration_ProcessSession) many-to-one relationship for the [processsession](processsession.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_ProcessSession|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_BulkDeleteFailures"></a> msdyn_aiconfiguration_BulkDeleteFailures

**Added by**: System Solution Solution

Same as the [msdyn_aiconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_aiconfiguration_BulkDeleteFailures) many-to-one relationship for the [bulkdeletefailure](bulkdeletefailure.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses"></a> msdyn_aiconfiguration_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as the [msdyn_aiconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_aiconfiguration_PrincipalObjectAttributeAccesses) many-to-one relationship for the [principalobjectattributeaccess](principalobjectattributeaccess.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration"></a> msdyn_aiconfiguration_msdyn_aiconfiguration

Same as the [msdyn_aiconfiguration_msdyn_aiconfiguration](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration) many-to-one relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|msdyn_trainedmodelaiconfigurationpareid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_msdyn_aiconfiguration|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration"></a> msdyn_createdfromconfiguration_msdyn_toconfiguration

Same as the [msdyn_createdfromconfiguration_msdyn_toconfiguration](msdyn_aiconfiguration.md#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration) many-to-one relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiconfiguration|
|ReferencingAttribute|msdyn_createdfromconfigurationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_createdfromconfiguration_msdyn_toconfiguration|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage"></a> msdyn_aiconfiguration_msdyn_aiodtrainingimage

**Added by**: AI Solution deprecated templates Solution

Same as the [msdyn_aiconfiguration_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_msdyn_aiconfiguration_msdyn_aiodtrainingimage) many-to-one relationship for the [msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aiodtrainingimage|
|ReferencingAttribute|msdyn_aiconfigurationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_aiconfiguration_msdyn_aiodtrainingimage|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId"></a> msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId

**Added by**: AI Solution deprecated templates Solution

Same as the [msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId](msdyn_aifptrainingdocument.md#BKMK_msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId) many-to-one relationship for the [msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md) table/entity.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_aifptrainingdocument|
|ReferencingAttribute|msdyn_aiconfigurationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_msdyn_aiconfiguration_msdyn_aifptrainingdocument_AIConfigurationId|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [lk_msdyn_aiconfiguration_createdby](#BKMK_lk_msdyn_aiconfiguration_createdby)
- [lk_msdyn_aiconfiguration_createdonbehalfby](#BKMK_lk_msdyn_aiconfiguration_createdonbehalfby)
- [lk_msdyn_aiconfiguration_modifiedby](#BKMK_lk_msdyn_aiconfiguration_modifiedby)
- [lk_msdyn_aiconfiguration_modifiedonbehalfby](#BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby)
- [msdyn_aiconfiguration_msdyn_aiconfiguration](#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration)
- [msdyn_AIConfiguration_ConnectionReference](#BKMK_msdyn_AIConfiguration_ConnectionReference)
- [msdyn_createdfromconfiguration_msdyn_toconfiguration](#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration)
- [msdyn_aimodel_msdyn_aiconfiguration](#BKMK_msdyn_aimodel_msdyn_aiconfiguration)


### <a name="BKMK_lk_msdyn_aiconfiguration_createdby"></a> lk_msdyn_aiconfiguration_createdby

**Added by**: System Solution Solution

See the [lk_msdyn_aiconfiguration_createdby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_createdby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_aiconfiguration_createdonbehalfby"></a> lk_msdyn_aiconfiguration_createdonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_aiconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_createdonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_aiconfiguration_modifiedby"></a> lk_msdyn_aiconfiguration_modifiedby

**Added by**: System Solution Solution

See the [lk_msdyn_aiconfiguration_modifiedby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_modifiedby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby"></a> lk_msdyn_aiconfiguration_modifiedonbehalfby

**Added by**: System Solution Solution

See the [lk_msdyn_aiconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aiconfiguration_modifiedonbehalfby) one-to-many relationship for the [systemuser](systemuser.md) table/entity.

### <a name="BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration"></a> msdyn_aiconfiguration_msdyn_aiconfiguration

See the [msdyn_aiconfiguration_msdyn_aiconfiguration](msdyn_aiconfiguration.md#BKMK_msdyn_aiconfiguration_msdyn_aiconfiguration) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_AIConfiguration_ConnectionReference"></a> msdyn_AIConfiguration_ConnectionReference

**Added by**: Power Platform Connection References Solution

See the [msdyn_AIConfiguration_ConnectionReference](connectionreference.md#BKMK_msdyn_AIConfiguration_ConnectionReference) one-to-many relationship for the [connectionreference](connectionreference.md) table/entity.

### <a name="BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration"></a> msdyn_createdfromconfiguration_msdyn_toconfiguration

See the [msdyn_createdfromconfiguration_msdyn_toconfiguration](msdyn_aiconfiguration.md#BKMK_msdyn_createdfromconfiguration_msdyn_toconfiguration) one-to-many relationship for the [msdyn_aiconfiguration](msdyn_aiconfiguration.md) table/entity.

### <a name="BKMK_msdyn_aimodel_msdyn_aiconfiguration"></a> msdyn_aimodel_msdyn_aiconfiguration

See the [msdyn_aimodel_msdyn_aiconfiguration](msdyn_aimodel.md#BKMK_msdyn_aimodel_msdyn_aiconfiguration) one-to-many relationship for the [msdyn_aimodel](msdyn_aimodel.md) table/entity.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the msdyn_AIConfiguration table is the first table in the relationship. Listed by **SchemaName**.


### <a name="BKMK_msdyn_aiodlabel_msdyn_aiconfiguration"></a> msdyn_aiodlabel_msdyn_aiconfiguration

See the [msdyn_aiodlabel_msdyn_aiconfiguration](msdyn_aiodlabel.md#BKMK_msdyn_aiodlabel_msdyn_aiconfiguration) many-to-many relationship for the [msdyn_aiodlabel](msdyn_aiodlabel.md) table/entity.

### See also

[Dataverse table/entity reference](../about-entity-reference.md)  
[Web API Reference](/dynamics365/customer-engagement/web-api/about)  
<xref href="Microsoft.Dynamics.CRM.msdyn_aiconfiguration?text=msdyn_aiconfiguration EntityType" />