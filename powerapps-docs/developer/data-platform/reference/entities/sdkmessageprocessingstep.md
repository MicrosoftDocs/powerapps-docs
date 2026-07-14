---
title: "Sdk Message Processing Step (SdkMessageProcessingStep) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sdk Message Processing Step (SdkMessageProcessingStep) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sdk Message Processing Step (SdkMessageProcessingStep) table/entity reference (Microsoft Dataverse)

Stage in the execution pipeline that a plug-in is to execute.

## Messages

The following table lists the messages for the Sdk Message Processing Step (SdkMessageProcessingStep) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /sdkmessageprocessingsteps<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /sdkmessageprocessingsteps(*sdkmessageprocessingstepid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sdkmessageprocessingsteps(*sdkmessageprocessingstepid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /sdkmessageprocessingsteps<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: False |`PATCH` /sdkmessageprocessingsteps(*sdkmessageprocessingstepid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /sdkmessageprocessingsteps(*sdkmessageprocessingstepid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /sdkmessageprocessingsteps(*sdkmessageprocessingstepid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Sdk Message Processing Step (SdkMessageProcessingStep) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sdk Message Processing Step** |
| **DisplayCollectionName** | **Sdk Message Processing Steps** |
| **SchemaName** | `SdkMessageProcessingStep` |
| **CollectionSchemaName** | `SdkMessageProcessingSteps` |
| **EntitySetName** | `sdkmessageprocessingsteps`|
| **LogicalName** | `sdkmessageprocessingstep` |
| **LogicalCollectionName** | `sdkmessageprocessingsteps` |
| **PrimaryIdAttribute** | `sdkmessageprocessingstepid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncAutoDelete](#BKMK_AsyncAutoDelete)
- [CanBeBypassed](#BKMK_CanBeBypassed)
- [CanUseReadOnlyConnection](#BKMK_CanUseReadOnlyConnection)
- [Category](#BKMK_Category)
- [Configuration](#BKMK_Configuration)
- [Description](#BKMK_Description)
- [EnablePluginProfiler](#BKMK_EnablePluginProfiler)
- [EventExpander](#BKMK_EventExpander)
- [EventHandler](#BKMK_EventHandler)
- [EventHandlerTypeCode](#BKMK_EventHandlerTypeCode)
- [FilteringAttributes](#BKMK_FilteringAttributes)
- [FxExpressionId](#BKMK_FxExpressionId)
- [ImpersonatingUserId](#BKMK_ImpersonatingUserId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [InvocationSource](#BKMK_InvocationSource)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsHidden](#BKMK_IsHidden)
- [Mode](#BKMK_Mode)
- [Name](#BKMK_Name)
- [PluginTypeId](#BKMK_PluginTypeId)
- [PowerfxRuleId](#BKMK_PowerfxRuleId)
- [Rank](#BKMK_Rank)
- [RuntimeIntegrationProperties](#BKMK_RuntimeIntegrationProperties)
- [SdkMessageFilterId](#BKMK_SdkMessageFilterId)
- [SdkMessageId](#BKMK_SdkMessageId)
- [SdkMessageProcessingStepId](#BKMK_SdkMessageProcessingStepId)
- [SdkMessageProcessingStepSecureConfigId](#BKMK_SdkMessageProcessingStepSecureConfigId)
- [Stage](#BKMK_Stage)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SupportedDeployment](#BKMK_SupportedDeployment)

### <a name="BKMK_AsyncAutoDelete"></a> AsyncAutoDelete

|Property|Value|
|---|---|
|Description|**Indicates whether the asynchronous system job is automatically deleted on completion.**|
|DisplayName|**Asynchronous Automatic Delete**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`asyncautodelete`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`sdkmessageprocessingstep_asyncautodelete`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanBeBypassed"></a> CanBeBypassed

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`canbebypassed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`sdkmessageprocessingstep_canbebypassed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CanUseReadOnlyConnection"></a> CanUseReadOnlyConnection

|Property|Value|
|---|---|
|Description|**Identifies whether a SDK Message Processing Step type will be ReadOnly or Read Write. false - ReadWrite, true - ReadOnly**|
|DisplayName|**Intent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`canusereadonlyconnection`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`isoperationintentreadonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Category"></a> Category

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`category`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Configuration"></a> Configuration

|Property|Value|
|---|---|
|Description|**Step-specific configuration for the plug-in type. Passed to the plug-in constructor at run time.**|
|DisplayName|**Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`configuration`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the SDK message processing step.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_EnablePluginProfiler"></a> EnablePluginProfiler

|Property|Value|
|---|---|
|Description|**EnablePluginProfiler**|
|DisplayName|**EnablePluginProfiler**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enablepluginprofiler`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessageprocessingstep_enablepluginprofiler`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EventExpander"></a> EventExpander

|Property|Value|
|---|---|
|Description|**Configuration for sending pipeline events to the Event Expander service.**|
|DisplayName|**EventExpander**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`eventexpander`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_EventHandler"></a> EventHandler

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated event handler.**|
|DisplayName|**Event Handler**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`eventhandler`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|plugintype, serviceendpoint|

### <a name="BKMK_EventHandlerTypeCode"></a> EventHandlerTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`eventhandlertypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_FilteringAttributes"></a> FilteringAttributes

|Property|Value|
|---|---|
|Description|**Comma-separated list of attributes. If at least one of these attributes is modified, the plug-in should execute.**|
|DisplayName|**Filtering Attributes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filteringattributes`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_FxExpressionId"></a> FxExpressionId

|Property|Value|
|---|---|
|Description|**Unique identifier for fxexpression associated with SdkMessageProcessingStep.**|
|DisplayName|**fxexpressionid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fxexpressionid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|fxexpression|

### <a name="BKMK_ImpersonatingUserId"></a> ImpersonatingUserId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user to impersonate context when step is executed.**|
|DisplayName|**Impersonating User**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`impersonatinguserid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_InvocationSource"></a> InvocationSource

|Property|Value|
|---|---|
|Description|**Identifies if a plug-in should be executed from a parent pipeline, a child pipeline, or both.**|
|DisplayName|**Invocation Source**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`invocationsource`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sdkmessageprocessingstep_invocationsource`|

#### InvocationSource Choices/Options

|Value|Label|
|---|---|
|-1|**Internal**|
|0|**Parent**|
|1|**Child**|

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsHidden"></a> IsHidden

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component should be hidden.**|
|DisplayName|**Hidden**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ishidden`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_Mode"></a> Mode

|Property|Value|
|---|---|
|Description|**Run-time mode of execution, for example, synchronous or asynchronous.**|
|DisplayName|**Execution Mode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sdkmessageprocessingstep_mode`|

#### Mode Choices/Options

|Value|Label|
|---|---|
|0|**Synchronous**|
|1|**Asynchronous**|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of SdkMessage processing step.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in type associated with the step.**|
|DisplayName|**Plug-In Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`plugintypeid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|sdkmessagefilter|

### <a name="BKMK_PowerfxRuleId"></a> PowerfxRuleId

|Property|Value|
|---|---|
|Description|**Unique identifier for powerfxrule associated with SdkMessageProcessingStep.**|
|DisplayName|**powerfxruleid**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`powerfxruleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|powerfxrule|

### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|---|---|
|Description|**Processing order within the stage.**|
|DisplayName|**Execution Order**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rank`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_RuntimeIntegrationProperties"></a> RuntimeIntegrationProperties

|Property|Value|
|---|---|
|Description|**For internal use only. Holds miscellaneous properties related to runtime integration.**|
|DisplayName|**Runtime Integration Properties**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`runtimeintegrationproperties`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_SdkMessageFilterId"></a> SdkMessageFilterId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message filter.**|
|DisplayName|**SdkMessage Filter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessagefilterid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sdkmessagefilter|

### <a name="BKMK_SdkMessageId"></a> SdkMessageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message.**|
|DisplayName|**SDK Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sdkmessageid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|sdkmessage|

### <a name="BKMK_SdkMessageProcessingStepId"></a> SdkMessageProcessingStepId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step entity.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SdkMessageProcessingStepSecureConfigId"></a> SdkMessageProcessingStepSecureConfigId

|Property|Value|
|---|---|
|Description|**Unique identifier of the Sdk message processing step secure configuration.**|
|DisplayName|**SDK Message Processing Step Secure Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepsecureconfigid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|sdkmessageprocessingstepsecureconfig|

### <a name="BKMK_Stage"></a> Stage

|Property|Value|
|---|---|
|Description|**Stage in the execution pipeline that the SDK message processing step is in.**|
|DisplayName|**Execution Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stage`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|10|
|GlobalChoiceName|`sdkmessageprocessingstep_stage`|

#### Stage Choices/Options

|Value|Label|
|---|---|
|5|**Initial Pre-operation (For internal use only)**|
|10|**Pre-validation**|
|15|**Internal Pre-operation Before External Plugins (For internal use only)**|
|20|**Pre-operation**|
|25|**Internal Pre-operation After External Plugins (For internal use only)**|
|30|**Main Operation (For internal use only)**|
|35|**Internal Post-operation Before External Plugins (For internal use only)**|
|40|**Post-operation**|
|45|**Internal Post-operation After External Plugins (For internal use only)**|
|50|**Post-operation (Deprecated)**|
|55|**Final Post-operation (For internal use only)**|
|80|**Pre-Commit stage fired before transaction commit (For internal use only)**|
|90|**Post-Commit stage fired after transaction commit (For internal use only)**|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the SDK message processing step.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`sdkmessageprocessingstep_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Enabled**<br />DefaultStatus: 1<br />InvariantName: `Enabled`|
|1|Label: **Disabled**<br />DefaultStatus: 2<br />InvariantName: `Disabled`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the SDK message processing step.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`sdkmessageprocessingstep_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Enabled**<br />State:0<br />TransitionData: None|
|2|Label: **Disabled**<br />State:1<br />TransitionData: None|

### <a name="BKMK_SupportedDeployment"></a> SupportedDeployment

|Property|Value|
|---|---|
|Description|**Deployment that the SDK message processing step should be executed on; server, client, or both.**|
|DisplayName|**Deployment**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supporteddeployment`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sdkmessageprocessingstep_supporteddeployment`|

#### SupportedDeployment Choices/Options

|Value|Label|
|---|---|
|0|**Server Only**|
|1|**Microsoft Dynamics 365 Client for Outlook Only**|
|2|**Both**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SdkMessageProcessingStepIdUnique](#BKMK_SdkMessageProcessingStepIdUnique)
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
|Description|**Unique identifier of the user who created the SDK message processing step.**|
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
|Description|**Date and time when the SDK message processing step was created.**|
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
|Description|**Unique identifier of the delegate user who created the sdkmessageprocessingstep.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|---|---|
|Description|**Customization level of the SDK message processing step.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|-255|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
|DisplayName|**State**|
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
|Description|**Unique identifier of the user who last modified the SDK message processing step.**|
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
|Description|**Date and time when the SDK message processing step was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the sdkmessageprocessingstep.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the SDK message processing step is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

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

### <a name="BKMK_SdkMessageProcessingStepIdUnique"></a> SdkMessageProcessingStepIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message processing step.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageprocessingstepidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|Description|**Number that identifies a specific revision of the SDK message processing step.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_sdkmessageprocessingstep](#BKMK_createdby_sdkmessageprocessingstep)
- [fxexpression_sdkmessageprocessingstep](#BKMK_fxexpression_sdkmessageprocessingstep)
- [impersonatinguserid_sdkmessageprocessingstep](#BKMK_impersonatinguserid_sdkmessageprocessingstep)
- [lk_sdkmessageprocessingstep_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby)
- [lk_sdkmessageprocessingstep_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby)
- [modifiedby_sdkmessageprocessingstep](#BKMK_modifiedby_sdkmessageprocessingstep)
- [organization_sdkmessageprocessingstep](#BKMK_organization_sdkmessageprocessingstep)
- [plugintype_sdkmessageprocessingstep](#BKMK_plugintype_sdkmessageprocessingstep)
- [plugintypeid_sdkmessageprocessingstep](#BKMK_plugintypeid_sdkmessageprocessingstep)
- [powerfxrule_sdkmessageprocessingstep](#BKMK_powerfxrule_sdkmessageprocessingstep)
- [sdkmessagefilterid_sdkmessageprocessingstep](#BKMK_sdkmessagefilterid_sdkmessageprocessingstep)
- [sdkmessageid_sdkmessageprocessingstep](#BKMK_sdkmessageid_sdkmessageprocessingstep)
- [sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep)
- [serviceendpoint_sdkmessageprocessingstep](#BKMK_serviceendpoint_sdkmessageprocessingstep)

### <a name="BKMK_createdby_sdkmessageprocessingstep"></a> createdby_sdkmessageprocessingstep

One-To-Many Relationship: [systemuser createdby_sdkmessageprocessingstep](systemuser.md#BKMK_createdby_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_fxexpression_sdkmessageprocessingstep"></a> fxexpression_sdkmessageprocessingstep

One-To-Many Relationship: [fxexpression fxexpression_sdkmessageprocessingstep](fxexpression.md#BKMK_fxexpression_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`fxexpression`|
|ReferencedAttribute|`fxexpressionid`|
|ReferencingAttribute|`fxexpressionid`|
|ReferencingEntityNavigationPropertyName|`fxexpression`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_impersonatinguserid_sdkmessageprocessingstep"></a> impersonatinguserid_sdkmessageprocessingstep

One-To-Many Relationship: [systemuser impersonatinguserid_sdkmessageprocessingstep](systemuser.md#BKMK_impersonatinguserid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`impersonatinguserid`|
|ReferencingEntityNavigationPropertyName|`impersonatinguserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessageprocessingstep_createdonbehalfby"></a> lk_sdkmessageprocessingstep_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessageprocessingstep_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby"></a> lk_sdkmessageprocessingstep_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessageprocessingstep_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_sdkmessageprocessingstep"></a> modifiedby_sdkmessageprocessingstep

One-To-Many Relationship: [systemuser modifiedby_sdkmessageprocessingstep](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sdkmessageprocessingstep"></a> organization_sdkmessageprocessingstep

One-To-Many Relationship: [organization organization_sdkmessageprocessingstep](organization.md#BKMK_organization_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugintype_sdkmessageprocessingstep"></a> plugintype_sdkmessageprocessingstep

One-To-Many Relationship: [plugintype plugintype_sdkmessageprocessingstep](plugintype.md#BKMK_plugintype_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`plugintype`|
|ReferencedAttribute|`plugintypeid`|
|ReferencingAttribute|`eventhandler`|
|ReferencingEntityNavigationPropertyName|`eventhandler_plugintype`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_plugintypeid_sdkmessageprocessingstep"></a> plugintypeid_sdkmessageprocessingstep

One-To-Many Relationship: [plugintype plugintypeid_sdkmessageprocessingstep](plugintype.md#BKMK_plugintypeid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`plugintype`|
|ReferencedAttribute|`plugintypeid`|
|ReferencingAttribute|`plugintypeid`|
|ReferencingEntityNavigationPropertyName|`plugintypeid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_powerfxrule_sdkmessageprocessingstep"></a> powerfxrule_sdkmessageprocessingstep

One-To-Many Relationship: [powerfxrule powerfxrule_sdkmessageprocessingstep](powerfxrule.md#BKMK_powerfxrule_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`powerfxrule`|
|ReferencedAttribute|`powerfxruleid`|
|ReferencingAttribute|`powerfxruleid`|
|ReferencingEntityNavigationPropertyName|`powerfxrule`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessagefilterid_sdkmessageprocessingstep"></a> sdkmessagefilterid_sdkmessageprocessingstep

One-To-Many Relationship: [sdkmessagefilter sdkmessagefilterid_sdkmessageprocessingstep](sdkmessagefilter.md#BKMK_sdkmessagefilterid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessagefilter`|
|ReferencedAttribute|`sdkmessagefilterid`|
|ReferencingAttribute|`sdkmessagefilterid`|
|ReferencingEntityNavigationPropertyName|`sdkmessagefilterid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessageid_sdkmessageprocessingstep"></a> sdkmessageid_sdkmessageprocessingstep

One-To-Many Relationship: [sdkmessage sdkmessageid_sdkmessageprocessingstep](sdkmessage.md#BKMK_sdkmessageid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessage`|
|ReferencedAttribute|`sdkmessageid`|
|ReferencingAttribute|`sdkmessageid`|
|ReferencingEntityNavigationPropertyName|`sdkmessageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep"></a> sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep

One-To-Many Relationship: [sdkmessageprocessingstepsecureconfig sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](sdkmessageprocessingstepsecureconfig.md#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessageprocessingstepsecureconfig`|
|ReferencedAttribute|`sdkmessageprocessingstepsecureconfigid`|
|ReferencingAttribute|`sdkmessageprocessingstepsecureconfigid`|
|ReferencingEntityNavigationPropertyName|`sdkmessageprocessingstepsecureconfigid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_serviceendpoint_sdkmessageprocessingstep"></a> serviceendpoint_sdkmessageprocessingstep

One-To-Many Relationship: [serviceendpoint serviceendpoint_sdkmessageprocessingstep](serviceendpoint.md#BKMK_serviceendpoint_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencedEntity|`serviceendpoint`|
|ReferencedAttribute|`serviceendpointid`|
|ReferencingAttribute|`eventhandler`|
|ReferencingEntityNavigationPropertyName|`eventhandler_serviceendpoint`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [SdkMessageProcessingStep_AsyncOperations](#BKMK_SdkMessageProcessingStep_AsyncOperations)
- [sdkmessageprocessingstep_plugin_SdkMessageProcessingStep](#BKMK_sdkmessageprocessingstep_plugin_SdkMessageProcessingStep)
- [sdkmessageprocessingstepid_sdkmessageprocessingstepimage](#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage)

### <a name="BKMK_SdkMessageProcessingStep_AsyncOperations"></a> SdkMessageProcessingStep_AsyncOperations

Many-To-One Relationship: [asyncoperation SdkMessageProcessingStep_AsyncOperations](asyncoperation.md#BKMK_SdkMessageProcessingStep_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`owningextensionid`|
|ReferencedEntityNavigationPropertyName|`SdkMessageProcessingStep_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sdkmessageprocessingstep_plugin_SdkMessageProcessingStep"></a> sdkmessageprocessingstep_plugin_SdkMessageProcessingStep

Many-To-One Relationship: [plugin sdkmessageprocessingstep_plugin_SdkMessageProcessingStep](plugin.md#BKMK_sdkmessageprocessingstep_plugin_SdkMessageProcessingStep)

|Property|Value|
|---|---|
|ReferencingEntity|`plugin`|
|ReferencingAttribute|`sdkmessageprocessingstep`|
|ReferencedEntityNavigationPropertyName|`sdkmessageprocessingstep_plugin_SdkMessageProcessingStep`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage"></a> sdkmessageprocessingstepid_sdkmessageprocessingstepimage

Many-To-One Relationship: [sdkmessageprocessingstepimage sdkmessageprocessingstepid_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstepimage`|
|ReferencingAttribute|`sdkmessageprocessingstepid`|
|ReferencedEntityNavigationPropertyName|`sdkmessageprocessingstepid_sdkmessageprocessingstepimage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sdkmessageprocessingstep?displayProperty=fullName>
