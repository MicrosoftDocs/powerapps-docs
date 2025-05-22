---
title: "Process (Workflow) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Process (Workflow) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Process (Workflow) table/entity reference (Microsoft Dataverse)

Set of logical rules that define the steps necessary to automate a specific business process, task, or set of actions to be performed.

## Messages

The following table lists the messages for the Process (Workflow) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `AddRequiredDesktopFlowComponentsToSolutions`<br />Event: False |<xref:Microsoft.Dynamics.CRM.AddRequiredDesktopFlowComponentsToSolutions?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Assign`<br />Event: False |`PATCH` /workflows(*workflowid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `CancelAllCloudFlowRuns`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CancelAllCloudFlowRuns?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Create`<br />Event: False |`POST` /workflows<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateWorkflowFromTemplate`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateWorkflowFromTemplate?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.CreateWorkflowFromTemplateRequest>|
| `Delete`<br />Event: False |`DELETE` /workflows(*workflowid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `ExecuteWorkflow`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ExecuteWorkflow?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ExecuteWorkflowRequest>|
| `GrantAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `InitializeModernFlowFromAsyncWorkflow`<br />Event: False |<xref:Microsoft.Dynamics.CRM.InitializeModernFlowFromAsyncWorkflow?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.InitializeModernFlowFromAsyncWorkflowRequest>|
| `install`<br />Event: False |<xref:Microsoft.Dynamics.CRM.install?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ListChildDesktopFlows`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ListChildDesktopFlows?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ListConnectionReferences`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ListConnectionReferences?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ModifyAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /workflows(*workflowid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /workflows<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RetrieveUnpublished`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `RevokeAccess`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `RunDesktopFlow`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RunDesktopFlow?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `SaveAsDesktopFlow`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SaveAsDesktopFlow?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `SetState`<br />Event: True |`PATCH` /workflows(*workflowid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /workflows(*workflowid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /workflows(*workflowid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Process (Workflow) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Process** |
| **DisplayCollectionName** | **Processes** |
| **SchemaName** | `Workflow` |
| **CollectionSchemaName** | `Workflows` |
| **EntitySetName** | `workflows`|
| **LogicalName** | `workflow` |
| **LogicalCollectionName** | `workflows` |
| **PrimaryIdAttribute** | `workflowid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncAutoDelete](#BKMK_AsyncAutoDelete)
- [BillingContext](#BKMK_BillingContext)
- [BusinessProcessType](#BKMK_BusinessProcessType)
- [Category](#BKMK_Category)
- [Claims](#BKMK_Claims)
- [ClientData](#BKMK_ClientData)
- [ConnectionReferences](#BKMK_ConnectionReferences)
- [CreateMetadata](#BKMK_CreateMetadata)
- [CreateStage](#BKMK_CreateStage)
- [Credentials](#BKMK_Credentials)
- [Definition](#BKMK_Definition)
- [DeleteStage](#BKMK_DeleteStage)
- [Dependencies](#BKMK_Dependencies)
- [Description](#BKMK_Description)
- [DesktopFlowModules](#BKMK_DesktopFlowModules)
- [DynamicsSolutionContext](#BKMK_DynamicsSolutionContext)
- [EntityImage](#BKMK_EntityImage)
- [FormId](#BKMK_FormId)
- [InputParameters](#BKMK_InputParameters)
- [Inputs](#BKMK_Inputs)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsCustomProcessingStepAllowedForOtherPublishers](#BKMK_IsCustomProcessingStepAllowedForOtherPublishers)
- [IsTransacted](#BKMK_IsTransacted)
- [LanguageCode](#BKMK_LanguageCode)
- [Licensee](#BKMK_Licensee)
- [LicenseEntitledBy](#BKMK_LicenseEntitledBy)
- [Metadata](#BKMK_Metadata)
- [Mode](#BKMK_Mode)
- [ModernFlowType](#BKMK_ModernFlowType)
- [ModifyMetadata](#BKMK_ModifyMetadata)
- [Name](#BKMK_Name)
- [OnDemand](#BKMK_OnDemand)
- [Outputs](#BKMK_Outputs)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PlanVerified](#BKMK_PlanVerified)
- [PrimaryEntity](#BKMK_PrimaryEntity)
- [ProcessOrder](#BKMK_ProcessOrder)
- [ProcessRoleAssignment](#BKMK_ProcessRoleAssignment)
- [ProcessTriggerFormId](#BKMK_ProcessTriggerFormId)
- [ProcessTriggerScope](#BKMK_ProcessTriggerScope)
- [Rank](#BKMK_Rank)
- [RendererObjectTypeCode](#BKMK_RendererObjectTypeCode)
- [ResourceContainer](#BKMK_ResourceContainer)
- [ResourceId](#BKMK_ResourceId)
- [RunAs](#BKMK_RunAs)
- [SchemaVersion](#BKMK_SchemaVersion)
- [Scope](#BKMK_Scope)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subprocess](#BKMK_Subprocess)
- [SuspensionReasonDetails](#BKMK_SuspensionReasonDetails)
- [SyncWorkflowLogOnFailure](#BKMK_SyncWorkflowLogOnFailure)
- [ThrottlingBehavior](#BKMK_ThrottlingBehavior)
- [TriggerOnCreate](#BKMK_TriggerOnCreate)
- [TriggerOnDelete](#BKMK_TriggerOnDelete)
- [TriggerOnUpdateAttributeList](#BKMK_TriggerOnUpdateAttributeList)
- [Type](#BKMK_Type)
- [UIFlowType](#BKMK_UIFlowType)
- [UniqueName](#BKMK_UniqueName)
- [UpdateStage](#BKMK_UpdateStage)
- [WorkflowId](#BKMK_WorkflowId)
- [Xaml](#BKMK_Xaml)

### <a name="BKMK_AsyncAutoDelete"></a> AsyncAutoDelete

|Property|Value|
|---|---|
|Description|**Indicates whether the asynchronous system job is automatically deleted on completion.**|
|DisplayName|**Delete Job On Completion**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`asyncautodelete`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`workflow_asyncautodelete`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_BillingContext"></a> BillingContext

|Property|Value|
|---|---|
|Description|**Billing context this flow is in.**|
|DisplayName|**BillingContext**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`billingcontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_BusinessProcessType"></a> BusinessProcessType

|Property|Value|
|---|---|
|Description|**Business Process Type.**|
|DisplayName|**Business Process Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`businessprocesstype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`workflow_businessprocesstype`|

#### BusinessProcessType Choices/Options

|Value|Label|
|---|---|
|0|**Business Flow**|
|1|**Task Flow**|

### <a name="BKMK_Category"></a> Category

|Property|Value|
|---|---|
|Description|**Category of the process.**|
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`category`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_category`|

#### Category Choices/Options

|Value|Label|
|---|---|
|0|**Workflow**|
|1|**Dialog**|
|2|**Business Rule**|
|3|**Action**|
|4|**Business Process Flow**|
|5|**Modern Flow**|
|6|**Desktop Flow**|
|7|**AI Flow**|

### <a name="BKMK_Claims"></a> Claims

|Property|Value|
|---|---|
|Description|**Claims related to this workflow.**|
|DisplayName|**Claims**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`claims`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_ClientData"></a> ClientData

|Property|Value|
|---|---|
|Description|**Business logic converted into client data**|
|DisplayName|**Client Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`clientdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_ConnectionReferences"></a> ConnectionReferences

|Property|Value|
|---|---|
|Description|**Connection References related to this workflow.**|
|DisplayName|**Connection references**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connectionreferences`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_CreateMetadata"></a> CreateMetadata

|Property|Value|
|---|---|
|Description|**Create metadata for this workflow.**|
|DisplayName|**Create metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createmetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_CreateStage"></a> CreateStage

|Property|Value|
|---|---|
|Description|**Stage of the process when triggered on Create.**|
|DisplayName|**Create Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createstage`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_stage`|

#### CreateStage Choices/Options

|Value|Label|
|---|---|
|20|**Pre-operation**|
|40|**Post-operation**|

### <a name="BKMK_Credentials"></a> Credentials

|Property|Value|
|---|---|
|Description|**Credentials related to this workflow.**|
|DisplayName|**Credentials**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`credentials`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Definition"></a> Definition

|Property|Value|
|---|---|
|Description|**Definition of the business logic of this workflow instance.**|
|DisplayName|**Definition**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`definition`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|16777216|

### <a name="BKMK_DeleteStage"></a> DeleteStage

|Property|Value|
|---|---|
|Description|**Stage of the process when triggered on Delete.**|
|DisplayName|**Delete stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`deletestage`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_stage`|

#### DeleteStage Choices/Options

|Value|Label|
|---|---|
|20|**Pre-operation**|
|40|**Post-operation**|

### <a name="BKMK_Dependencies"></a> Dependencies

|Property|Value|
|---|---|
|Description|**Soft dependencies of this workflow instance.**|
|DisplayName|**Dependencies**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dependencies`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the process.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100000|

### <a name="BKMK_DesktopFlowModules"></a> DesktopFlowModules

|Property|Value|
|---|---|
|Description|**Desktop flow modules related to this workflow.**|
|DisplayName|**Desktop flow modules**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`desktopflowmodules`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_DynamicsSolutionContext"></a> DynamicsSolutionContext

|Property|Value|
|---|---|
|Description|**comma separated list of one or more Dynamics First Party Solution Unique names that this workflow is in context of.**|
|DisplayName|**DynamicsSolutionContext**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dynamicssolutioncontext`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|---|---|
|Description|**Shows the default image for the record.**|
|DisplayName|**Default Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|False|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_FormId"></a> FormId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated form.**|
|DisplayName|**Form ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`formid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_InputParameters"></a> InputParameters

|Property|Value|
|---|---|
|Description|**Input parameters to the process.**|
|DisplayName|**Input Parameters**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inputparameters`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Inputs"></a> Inputs

|Property|Value|
|---|---|
|Description|**Inputs definition for this workflow.**|
|DisplayName|**Inputs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`inputs`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

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
|Description|**Information that specifies whether this component can be customized.**|
|DisplayName|**Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsCustomProcessingStepAllowedForOtherPublishers"></a> IsCustomProcessingStepAllowedForOtherPublishers

|Property|Value|
|---|---|
|Description|**Defines whether other publishers can attach custom processing steps to this action**|
|DisplayName|**Allow custom processing step for other publishers**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscustomprocessingstepallowedforotherpublishers`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_IsTransacted"></a> IsTransacted

|Property|Value|
|---|---|
|Description|**Whether or not the steps in the process are executed in a single transaction.**|
|DisplayName|**Is Transacted**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`istransacted`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_autotransact`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|---|---|
|Description|**Language of the process.**|
|DisplayName|**Language**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`languagecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_Licensee"></a> Licensee

|Property|Value|
|---|---|
|Description|**The user object that should be used to establish the license the flow should operate under.**|
|DisplayName|**Licensee**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`licensee`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_LicenseEntitledBy"></a> LicenseEntitledBy

|Property|Value|
|---|---|
|Description|**The source of the license entitlements.**|
|DisplayName|**License entitled by**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`licenseentitledby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_Metadata"></a> Metadata

|Property|Value|
|---|---|
|Description|**Additional metadata for this workflow.**|
|DisplayName|**Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`metadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Mode"></a> Mode

|Property|Value|
|---|---|
|Description|**Shows the mode of the process.**|
|DisplayName|**Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`mode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`workflow_mode`|

#### Mode Choices/Options

|Value|Label|
|---|---|
|0|**Background**|
|1|**Real-time**|

### <a name="BKMK_ModernFlowType"></a> ModernFlowType

|Property|Value|
|---|---|
|Description|**Type of the Modern Flow.**|
|DisplayName|**Modern Flow Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modernflowtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`workflow_modernflowtype`|

#### ModernFlowType Choices/Options

|Value|Label|
|---|---|
|0|**PowerAutomateFlow**|
|1|**CopilotStudioFlow**|

### <a name="BKMK_ModifyMetadata"></a> ModifyMetadata

|Property|Value|
|---|---|
|Description|**Flow modify metadata used for telemetry, etc.**|
|DisplayName|**ModifyMetadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifymetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the process.**|
|DisplayName|**Process Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|100|

### <a name="BKMK_OnDemand"></a> OnDemand

|Property|Value|
|---|---|
|Description|**Indicates whether the process is able to run as an on-demand process.**|
|DisplayName|**Run as On Demand**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ondemand`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_ondemand`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Outputs"></a> Outputs

|Property|Value|
|---|---|
|Description|**Outputs definition for this workflow.**|
|DisplayName|**Outputs**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`outputs`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the process.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_PlanVerified"></a> PlanVerified

|Property|Value|
|---|---|
|Description|**For Internal Use Only.**|
|DisplayName|**Plan Verified**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`planverified`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_planverified`|
|DefaultValue|False|
|True Label|Verified|
|False Label|NotVerified|

### <a name="BKMK_PrimaryEntity"></a> PrimaryEntity

|Property|Value|
|---|---|
|Description|**Primary entity for the process. The process can be associated for one or more SDK operations defined on the primary entity.**|
|DisplayName|**Primary Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryentity`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ProcessOrder"></a> ProcessOrder

|Property|Value|
|---|---|
|Description|**Type the business process flow order.**|
|DisplayName|**Process Order**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processorder`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ProcessRoleAssignment"></a> ProcessRoleAssignment

|Property|Value|
|---|---|
|Description|**Contains the role assignment for the process.**|
|DisplayName|**Role assignment for Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processroleassignment`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_ProcessTriggerFormId"></a> ProcessTriggerFormId

|Property|Value|
|---|---|
|Description|**Unique identifier of the associated form for process trigger.**|
|DisplayName|**ProcessTriggerFormId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processtriggerformid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ProcessTriggerScope"></a> ProcessTriggerScope

|Property|Value|
|---|---|
|Description|**Scope of the process trigger.**|
|DisplayName|**ProcessTriggerScope**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processtriggerscope`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`processtrigger_scope`|

#### ProcessTriggerScope Choices/Options

|Value|Label|
|---|---|
|1|**Form**|
|2|**Entity**|

### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|---|---|
|Description|**Indicates the rank for order of execution for the synchronous workflow.**|
|DisplayName|**Rank**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rank`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_RendererObjectTypeCode"></a> RendererObjectTypeCode

|Property|Value|
|---|---|
|Description|**The renderer type of Workflow**|
|DisplayName|**Renderer Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`rendererobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_ResourceContainer"></a> ResourceContainer

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**ResourceContainer**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`resourcecontainer`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_ResourceId"></a> ResourceId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**ResourceId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`resourceid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_RunAs"></a> RunAs

|Property|Value|
|---|---|
|Description|**Specifies the system user account under which a workflow executes.**|
|DisplayName|**Run As User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`runas`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`workflow_runas`|

#### RunAs Choices/Options

|Value|Label|
|---|---|
|0|**Owner**|
|1|**Calling User**|

### <a name="BKMK_SchemaVersion"></a> SchemaVersion

|Property|Value|
|---|---|
|Description|**Schema version for this workflow.**|
|DisplayName|**Schema Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`schemaversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Scope"></a> Scope

|Property|Value|
|---|---|
|Description|**Scope of the process.**|
|DisplayName|**Scope**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`scope`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_scope`|

#### Scope Choices/Options

|Value|Label|
|---|---|
|1|**User**|
|2|**Business Unit**|
|3|**Parent: Child Business Units**|
|4|**Organization**|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Status of the workflow**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`workflow_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />DefaultStatus: 1<br />InvariantName: `Draft`|
|1|Label: **Activated**<br />DefaultStatus: 2<br />InvariantName: `Activated`|
|2|Label: **Suspended**<br />DefaultStatus: 3<br />InvariantName: `Suspended`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Reason for the status of the workflow**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Draft**<br />State:0<br />TransitionData: None|
|2|Label: **Activated**<br />State:1<br />TransitionData: None|
|3|Label: **CompanyDLPViolation**<br />State:2<br />TransitionData: None|

### <a name="BKMK_Subprocess"></a> Subprocess

|Property|Value|
|---|---|
|Description|**Indicates whether the process can be included in other processes as a child process.**|
|DisplayName|**Is Child Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`subprocess`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_subprocess`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SuspensionReasonDetails"></a> SuspensionReasonDetails

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`suspensionreasondetails`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_SyncWorkflowLogOnFailure"></a> SyncWorkflowLogOnFailure

|Property|Value|
|---|---|
|Description|**Select whether synchronous workflow failures will be saved to log files.**|
|DisplayName|**Log upon Failure**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`syncworkflowlogonfailure`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`workflow_syncworkflowlogonfailure`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ThrottlingBehavior"></a> ThrottlingBehavior

|Property|Value|
|---|---|
|Description|**The throttling behavior type.**|
|DisplayName|**Throttling behavior type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`throttlingbehavior`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_throttlingbehaviortype`|

#### ThrottlingBehavior Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**TenantPool**|
|2|**CopilotStudio**|

### <a name="BKMK_TriggerOnCreate"></a> TriggerOnCreate

|Property|Value|
|---|---|
|Description|**Indicates whether the process will be triggered when the primary entity is created.**|
|DisplayName|**Trigger On Create**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`triggeroncreate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_triggeroncreate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TriggerOnDelete"></a> TriggerOnDelete

|Property|Value|
|---|---|
|Description|**Indicates whether the process will be triggered on deletion of the primary entity.**|
|DisplayName|**Trigger On Delete**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`triggerondelete`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_triggerondelete`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TriggerOnUpdateAttributeList"></a> TriggerOnUpdateAttributeList

|Property|Value|
|---|---|
|Description|**Attributes that trigger the process when updated.**|
|DisplayName|**Trigger On Update Attribute List**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`triggeronupdateattributelist`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_Type"></a> Type

|Property|Value|
|---|---|
|Description|**Type of the process.**|
|DisplayName|**Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`type`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_type`|

#### Type Choices/Options

|Value|Label|
|---|---|
|1|**Definition**|
|2|**Activation**|
|3|**Template**|

### <a name="BKMK_UIFlowType"></a> UIFlowType

|Property|Value|
|---|---|
|Description|**Type of the UI Flow process.**|
|DisplayName|**UI Flow Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uiflowtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_uiflowtype`|

#### UIFlowType Choices/Options

|Value|Label|
|---|---|
|0|**Windows recorder (V1)**|
|1|**Selenium IDE**|
|2|**Power Automate Desktop**|
|3|**Test**|
|101|**Recording**|

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique name of the process**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_UpdateStage"></a> UpdateStage

|Property|Value|
|---|---|
|Description|**Select the stage a process will be triggered on update.**|
|DisplayName|**Update Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`updatestage`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`workflow_stage`|

#### UpdateStage Choices/Options

|Value|Label|
|---|---|
|20|**Pre-operation**|
|40|**Post-operation**|

### <a name="BKMK_WorkflowId"></a> WorkflowId

|Property|Value|
|---|---|
|Description|**Unique identifier of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Xaml"></a> Xaml

|Property|Value|
|---|---|
|Description|**XAML that defines the process.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`xaml`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ActiveWorkflowId](#BKMK_ActiveWorkflowId)
- [ClientDataIsCompressed](#BKMK_ClientDataIsCompressed)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IsCrmUIWorkflow](#BKMK_IsCrmUIWorkflow)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentWorkflowId](#BKMK_ParentWorkflowId)
- [PluginTypeId](#BKMK_PluginTypeId)
- [SdkMessageId](#BKMK_SdkMessageId)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TrustedAccess](#BKMK_TrustedAccess)
- [UIData](#BKMK_UIData)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkflowIdUnique](#BKMK_WorkflowIdUnique)

### <a name="BKMK_ActiveWorkflowId"></a> ActiveWorkflowId

|Property|Value|
|---|---|
|Description|**Unique identifier of the latest activation record for the process.**|
|DisplayName|**Active Process ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activeworkflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_ClientDataIsCompressed"></a> ClientDataIsCompressed

|Property|Value|
|---|---|
|Description|**For Internal Use Only.**|
|DisplayName|**Client Data Is Compressed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`clientdataiscompressed`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_clientdataiscompressed`|
|DefaultValue|False|
|True Label|Workflow has compressed client data|
|False Label|Workflow does not have compressed client data|

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
|Description|**Unique identifier of the user who created the process.**|
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
|Description|**Date and time when the process was created.**|
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
|Description|**Unique identifier of the delegate user who created the process.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Entity Image Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_IsCrmUIWorkflow"></a> IsCrmUIWorkflow

|Property|Value|
|---|---|
|Description|**Indicates whether the process was created using the Microsoft Dynamics 365 Web application.**|
|DisplayName|**Is CRM Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscrmuiworkflow`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_iscrmuiworkflow`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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
|Description|**Unique identifier of the user who last modified the process.**|
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
|Description|**Date and time when the process was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the process.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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
|Description||
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
|Description||
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
|Description|**Unique identifier of the business unit that owns the process.**|
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
|Description|**Unique identifier of the team who owns the process.**|
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
|Description|**Unique identifier of the user who owns the process.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ParentWorkflowId"></a> ParentWorkflowId

|Property|Value|
|---|---|
|Description|**Unique identifier of the definition for process activation.**|
|DisplayName|**Parent Process ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentworkflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the plug-in type.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`plugintypeid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sdkmessagefilter|

### <a name="BKMK_SdkMessageId"></a> SdkMessageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK Message associated with this workflow.**|
|DisplayName|**SDK Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sdkmessageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sdkmessage|

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

### <a name="BKMK_TrustedAccess"></a> TrustedAccess

|Property|Value|
|---|---|
|Description|**For Internal Use Only.**|
|DisplayName|**Trusted Access**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`trustedaccess`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`workflow_trustedaccess`|
|DefaultValue|False|
|True Label|Workflow has gone through access check|
|False Label|Workflow has not gone through access check|

### <a name="BKMK_UIData"></a> UIData

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**UI Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`uidata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_WorkflowIdUnique"></a> WorkflowIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_workflow](#BKMK_business_unit_workflow)
- [owner_workflows](#BKMK_owner_workflows)
- [system_user_workflow](#BKMK_system_user_workflow)
- [team_workflow](#BKMK_team_workflow)
- [workflow_active_workflow](#BKMK_workflow_active_workflow-many-to-one)
- [workflow_createdby](#BKMK_workflow_createdby)
- [workflow_createdonbehalfby](#BKMK_workflow_createdonbehalfby)
- [Workflow_licensee](#BKMK_Workflow_licensee)
- [Workflow_licenseentitledby](#BKMK_Workflow_licenseentitledby-many-to-one)
- [workflow_modifiedby](#BKMK_workflow_modifiedby)
- [workflow_modifiedonbehalfby](#BKMK_workflow_modifiedonbehalfby)
- [workflow_parent_workflow](#BKMK_workflow_parent_workflow-many-to-one)

### <a name="BKMK_business_unit_workflow"></a> business_unit_workflow

One-To-Many Relationship: [businessunit business_unit_workflow](businessunit.md#BKMK_business_unit_workflow)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_workflows"></a> owner_workflows

One-To-Many Relationship: [owner owner_workflows](owner.md#BKMK_owner_workflows)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_system_user_workflow"></a> system_user_workflow

One-To-Many Relationship: [systemuser system_user_workflow](systemuser.md#BKMK_system_user_workflow)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_workflow"></a> team_workflow

One-To-Many Relationship: [team team_workflow](team.md#BKMK_team_workflow)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_active_workflow-many-to-one"></a> workflow_active_workflow

One-To-Many Relationship: [workflow workflow_active_workflow](#BKMK_workflow_active_workflow-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`activeworkflowid`|
|ReferencingEntityNavigationPropertyName|`activeworkflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_createdby"></a> workflow_createdby

One-To-Many Relationship: [systemuser workflow_createdby](systemuser.md#BKMK_workflow_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_createdonbehalfby"></a> workflow_createdonbehalfby

One-To-Many Relationship: [systemuser workflow_createdonbehalfby](systemuser.md#BKMK_workflow_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Workflow_licensee"></a> Workflow_licensee

One-To-Many Relationship: [systemuser Workflow_licensee](systemuser.md#BKMK_Workflow_licensee)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`licensee`|
|ReferencingEntityNavigationPropertyName|`licensee_systemuserid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Workflow_licenseentitledby-many-to-one"></a> Workflow_licenseentitledby

One-To-Many Relationship: [workflow Workflow_licenseentitledby](#BKMK_Workflow_licenseentitledby-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`licenseentitledby`|
|ReferencingEntityNavigationPropertyName|`licenseentitledby_workflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_modifiedby"></a> workflow_modifiedby

One-To-Many Relationship: [systemuser workflow_modifiedby](systemuser.md#BKMK_workflow_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_modifiedonbehalfby"></a> workflow_modifiedonbehalfby

One-To-Many Relationship: [systemuser workflow_modifiedonbehalfby](systemuser.md#BKMK_workflow_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_workflow_parent_workflow-many-to-one"></a> workflow_parent_workflow

One-To-Many Relationship: [workflow workflow_parent_workflow](#BKMK_workflow_parent_workflow-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`parentworkflowid`|
|ReferencingEntityNavigationPropertyName|`parentworkflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [adx_invitation_redemptionworkflow](#BKMK_adx_invitation_redemptionworkflow)
- [AIPluginOperation_Workflow_Workflow](#BKMK_AIPluginOperation_Workflow_Workflow)
- [catalogassignment_workflow](#BKMK_catalogassignment_workflow)
- [flowcapacityassignment_workflow](#BKMK_flowcapacityassignment_workflow)
- [flowevent_workflow](#BKMK_flowevent_workflow)
- [lk_asyncoperation_workflowactivationid](#BKMK_lk_asyncoperation_workflowactivationid)
- [lk_expiredprocess_processid](#BKMK_lk_expiredprocess_processid)
- [lk_newprocess_processid](#BKMK_lk_newprocess_processid)
- [lk_processsession_processid](#BKMK_lk_processsession_processid)
- [lk_translationprocess_processid](#BKMK_lk_translationprocess_processid)
- [msdyn_retrainworkflow_msdyn_toaimodel](#BKMK_msdyn_retrainworkflow_msdyn_toaimodel)
- [msdyn_scheduleinferenceworkflow_msdyn_toaimodel](#BKMK_msdyn_scheduleinferenceworkflow_msdyn_toaimodel)
- [msdyn_workflow_msdyn_pmrecording](#BKMK_msdyn_workflow_msdyn_pmrecording)
- [msdyn_workflow_msdyn_solutionhealthrule_resolutionaction](#BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction)
- [msdyn_workflow_msdyn_solutionhealthrule_Workflow](#BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow)
- [msdyn_workflow_slaitem_customtimecalculationworkflowid](#BKMK_msdyn_workflow_slaitem_customtimecalculationworkflowid)
- [process_processstage](#BKMK_process_processstage)
- [process_processtrigger](#BKMK_process_processtrigger)
- [regardingobjectid_process](#BKMK_regardingobjectid_process)
- [savingrule_workflow](#BKMK_savingrule_workflow)
- [slabase_workflowid](#BKMK_slabase_workflowid)
- [slaitembase_workflowid](#BKMK_slaitembase_workflowid)
- [taggedprocess_Process_workflow](#BKMK_taggedprocess_Process_workflow)
- [workflow_active_workflow](#BKMK_workflow_active_workflow-one-to-many)
- [Workflow_Annotation](#BKMK_Workflow_Annotation)
- [workflow_businessprocess](#BKMK_workflow_businessprocess)
- [workflow_componentversionnrddatasourceset](#BKMK_workflow_componentversionnrddatasourceset)
- [workflow_componentversions](#BKMK_workflow_componentversions)
- [workflow_desktopflowbinary_Process](#BKMK_workflow_desktopflowbinary_Process)
- [workflow_flowaggregation_workflowid](#BKMK_workflow_flowaggregation_workflowid)
- [workflow_flowlog_cloudflowid](#BKMK_workflow_flowlog_cloudflowid)
- [workflow_flowlog_desktopflowid](#BKMK_workflow_flowlog_desktopflowid)
- [workflow_flowrun_Workflow](#BKMK_workflow_flowrun_Workflow)
- [Workflow_licenseentitledby](#BKMK_Workflow_licenseentitledby-one-to-many)
- [workflow_parent_workflow](#BKMK_workflow_parent_workflow-one-to-many)
- [Workflow_SyncErrors](#BKMK_Workflow_SyncErrors)
- [workflow_workflowbinary_Process](#BKMK_workflow_workflowbinary_Process)
- [workflowmetadata_WorkflowId_workflow](#BKMK_workflowmetadata_WorkflowId_workflow)

### <a name="BKMK_adx_invitation_redemptionworkflow"></a> adx_invitation_redemptionworkflow

Many-To-One Relationship: [adx_invitation adx_invitation_redemptionworkflow](adx_invitation.md#BKMK_adx_invitation_redemptionworkflow)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`adx_redemptionworkflow`|
|ReferencedEntityNavigationPropertyName|`adx_invitation_redemptionworkflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_AIPluginOperation_Workflow_Workflow"></a> AIPluginOperation_Workflow_Workflow

Many-To-One Relationship: [aipluginoperation AIPluginOperation_Workflow_Workflow](aipluginoperation.md#BKMK_AIPluginOperation_Workflow_Workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`workflow`|
|ReferencedEntityNavigationPropertyName|`AIPluginOperation_Workflow_Workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_catalogassignment_workflow"></a> catalogassignment_workflow

Many-To-One Relationship: [catalogassignment catalogassignment_workflow](catalogassignment.md#BKMK_catalogassignment_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`catalogassignment`|
|ReferencingAttribute|`object`|
|ReferencedEntityNavigationPropertyName|`CatalogAssignments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowcapacityassignment_workflow"></a> flowcapacityassignment_workflow

Many-To-One Relationship: [flowcapacityassignment flowcapacityassignment_workflow](flowcapacityassignment.md#BKMK_flowcapacityassignment_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_flowevent_workflow"></a> flowevent_workflow

Many-To-One Relationship: [flowevent flowevent_workflow](flowevent.md#BKMK_flowevent_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`parentobjectid`|
|ReferencedEntityNavigationPropertyName|`flowevent_workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_asyncoperation_workflowactivationid"></a> lk_asyncoperation_workflowactivationid

Many-To-One Relationship: [asyncoperation lk_asyncoperation_workflowactivationid](asyncoperation.md#BKMK_lk_asyncoperation_workflowactivationid)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`workflowactivationid`|
|ReferencedEntityNavigationPropertyName|`lk_asyncoperation_workflowactivationid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_expiredprocess_processid"></a> lk_expiredprocess_processid

Many-To-One Relationship: [expiredprocess lk_expiredprocess_processid](expiredprocess.md#BKMK_lk_expiredprocess_processid)

|Property|Value|
|---|---|
|ReferencingEntity|`expiredprocess`|
|ReferencingAttribute|`processid`|
|ReferencedEntityNavigationPropertyName|`workflow_expiredprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_newprocess_processid"></a> lk_newprocess_processid

Many-To-One Relationship: [newprocess lk_newprocess_processid](newprocess.md#BKMK_lk_newprocess_processid)

|Property|Value|
|---|---|
|ReferencingEntity|`newprocess`|
|ReferencingAttribute|`processid`|
|ReferencedEntityNavigationPropertyName|`workflow_newprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

Many-To-One Relationship: [processsession lk_processsession_processid](processsession.md#BKMK_lk_processsession_processid)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`processid`|
|ReferencedEntityNavigationPropertyName|`lk_processsession_processid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_translationprocess_processid"></a> lk_translationprocess_processid

Many-To-One Relationship: [translationprocess lk_translationprocess_processid](translationprocess.md#BKMK_lk_translationprocess_processid)

|Property|Value|
|---|---|
|ReferencingEntity|`translationprocess`|
|ReferencingAttribute|`processid`|
|ReferencedEntityNavigationPropertyName|`workflow_translationprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_retrainworkflow_msdyn_toaimodel"></a> msdyn_retrainworkflow_msdyn_toaimodel

Many-To-One Relationship: [msdyn_aimodel msdyn_retrainworkflow_msdyn_toaimodel](msdyn_aimodel.md#BKMK_msdyn_retrainworkflow_msdyn_toaimodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodel`|
|ReferencingAttribute|`msdyn_retrainworkflowid`|
|ReferencedEntityNavigationPropertyName|`msdyn_retrainworkflow_msdyn_toaimodel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_scheduleinferenceworkflow_msdyn_toaimodel"></a> msdyn_scheduleinferenceworkflow_msdyn_toaimodel

Many-To-One Relationship: [msdyn_aimodel msdyn_scheduleinferenceworkflow_msdyn_toaimodel](msdyn_aimodel.md#BKMK_msdyn_scheduleinferenceworkflow_msdyn_toaimodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodel`|
|ReferencingAttribute|`msdyn_scheduleinferenceworkflowid`|
|ReferencedEntityNavigationPropertyName|`msdyn_scheduleinferenceworkflow_msdyn_toaimodel`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_workflow_msdyn_pmrecording"></a> msdyn_workflow_msdyn_pmrecording

Many-To-One Relationship: [msdyn_pmrecording msdyn_workflow_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_msdyn_workflow_msdyn_pmrecording)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmrecording`|
|ReferencingAttribute|`msdyn_sourceworkflow`|
|ReferencedEntityNavigationPropertyName|`msdyn_workflow_msdyn_pmrecording`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction"></a> msdyn_workflow_msdyn_solutionhealthrule_resolutionaction

Many-To-One Relationship: [msdyn_solutionhealthrule msdyn_workflow_msdyn_solutionhealthrule_resolutionaction](msdyn_solutionhealthrule.md#BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthrule`|
|ReferencingAttribute|`msdyn_resolutionaction`|
|ReferencedEntityNavigationPropertyName|`msdyn_workflow_msdyn_solutionhealthrule_resolutionaction`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow"></a> msdyn_workflow_msdyn_solutionhealthrule_Workflow

Many-To-One Relationship: [msdyn_solutionhealthrule msdyn_workflow_msdyn_solutionhealthrule_Workflow](msdyn_solutionhealthrule.md#BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthrule`|
|ReferencingAttribute|`msdyn_workflow`|
|ReferencedEntityNavigationPropertyName|`msdyn_workflow_msdyn_solutionhealthrule_Workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_workflow_slaitem_customtimecalculationworkflowid"></a> msdyn_workflow_slaitem_customtimecalculationworkflowid

Many-To-One Relationship: [slaitem msdyn_workflow_slaitem_customtimecalculationworkflowid](slaitem.md#BKMK_msdyn_workflow_slaitem_customtimecalculationworkflowid)

|Property|Value|
|---|---|
|ReferencingEntity|`slaitem`|
|ReferencingAttribute|`msdyn_customtimecalculationworkflowid`|
|ReferencedEntityNavigationPropertyName|`msdyn_workflow_slaitem_customtimecalculationworkflowid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_process_processstage"></a> process_processstage

Many-To-One Relationship: [processstage process_processstage](processstage.md#BKMK_process_processstage)

|Property|Value|
|---|---|
|ReferencingEntity|`processstage`|
|ReferencingAttribute|`processid`|
|ReferencedEntityNavigationPropertyName|`process_processstage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_process_processtrigger"></a> process_processtrigger

Many-To-One Relationship: [processtrigger process_processtrigger](processtrigger.md#BKMK_process_processtrigger)

|Property|Value|
|---|---|
|ReferencingEntity|`processtrigger`|
|ReferencingAttribute|`processid`|
|ReferencedEntityNavigationPropertyName|`process_processtrigger`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_regardingobjectid_process"></a> regardingobjectid_process

Many-To-One Relationship: [flowsession regardingobjectid_process](flowsession.md#BKMK_regardingobjectid_process)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`regardingobjectid_process`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_savingrule_workflow"></a> savingrule_workflow

Many-To-One Relationship: [savingrule savingrule_workflow](savingrule.md#BKMK_savingrule_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`savingrule`|
|ReferencingAttribute|`workflowid`|
|ReferencedEntityNavigationPropertyName|`savingrule_Workflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slabase_workflowid"></a> slabase_workflowid

Many-To-One Relationship: [sla slabase_workflowid](sla.md#BKMK_slabase_workflowid)

|Property|Value|
|---|---|
|ReferencingEntity|`sla`|
|ReferencingAttribute|`workflowid`|
|ReferencedEntityNavigationPropertyName|`slabase_workflowid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_slaitembase_workflowid"></a> slaitembase_workflowid

Many-To-One Relationship: [slaitem slaitembase_workflowid](slaitem.md#BKMK_slaitembase_workflowid)

|Property|Value|
|---|---|
|ReferencingEntity|`slaitem`|
|ReferencingAttribute|`workflowid`|
|ReferencedEntityNavigationPropertyName|`slaitembase_workflowid`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_taggedprocess_Process_workflow"></a> taggedprocess_Process_workflow

Many-To-One Relationship: [taggedprocess taggedprocess_Process_workflow](taggedprocess.md#BKMK_taggedprocess_Process_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedprocess`|
|ReferencingAttribute|`process`|
|ReferencedEntityNavigationPropertyName|`taggedprocess_Process_workflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_active_workflow-one-to-many"></a> workflow_active_workflow

Many-To-One Relationship: [workflow workflow_active_workflow](#BKMK_workflow_active_workflow-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`workflow`|
|ReferencingAttribute|`activeworkflowid`|
|ReferencedEntityNavigationPropertyName|`workflow_active_workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Workflow_Annotation"></a> Workflow_Annotation

Many-To-One Relationship: [annotation Workflow_Annotation](annotation.md#BKMK_Workflow_Annotation)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`Workflow_Annotation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_businessprocess"></a> workflow_businessprocess

Many-To-One Relationship: [businessprocess workflow_businessprocess](businessprocess.md#BKMK_workflow_businessprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`businessprocess`|
|ReferencingAttribute|`rootworkflowid`|
|ReferencedEntityNavigationPropertyName|`workflow_businessprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: Root Process<br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_componentversionnrddatasourceset"></a> workflow_componentversionnrddatasourceset

Many-To-One Relationship: [componentversionnrddatasource workflow_componentversionnrddatasourceset](componentversionnrddatasource.md#BKMK_workflow_componentversionnrddatasourceset)

|Property|Value|
|---|---|
|ReferencingEntity|`componentversionnrddatasource`|
|ReferencingAttribute|`component`|
|ReferencedEntityNavigationPropertyName|`componentversionnrddatasourceset`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_componentversions"></a> workflow_componentversions

Many-To-One Relationship: [componentversion workflow_componentversions](componentversion.md#BKMK_workflow_componentversions)

|Property|Value|
|---|---|
|ReferencingEntity|`componentversion`|
|ReferencingAttribute|`component`|
|ReferencedEntityNavigationPropertyName|`componentversions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_desktopflowbinary_Process"></a> workflow_desktopflowbinary_Process

Many-To-One Relationship: [desktopflowbinary workflow_desktopflowbinary_Process](desktopflowbinary.md#BKMK_workflow_desktopflowbinary_Process)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowbinary`|
|ReferencingAttribute|`process`|
|ReferencedEntityNavigationPropertyName|`workflow_desktopflowbinary_Process`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_flowaggregation_workflowid"></a> workflow_flowaggregation_workflowid

Many-To-One Relationship: [flowaggregation workflow_flowaggregation_workflowid](flowaggregation.md#BKMK_workflow_flowaggregation_workflowid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowaggregation`|
|ReferencingAttribute|`workflowid`|
|ReferencedEntityNavigationPropertyName|`workflow_flowaggregation_workflowid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_flowlog_cloudflowid"></a> workflow_flowlog_cloudflowid

Many-To-One Relationship: [flowlog workflow_flowlog_cloudflowid](flowlog.md#BKMK_workflow_flowlog_cloudflowid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`cloudflowid`|
|ReferencedEntityNavigationPropertyName|`workflow_flowlog_cloudflowid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_flowlog_desktopflowid"></a> workflow_flowlog_desktopflowid

Many-To-One Relationship: [flowlog workflow_flowlog_desktopflowid](flowlog.md#BKMK_workflow_flowlog_desktopflowid)

|Property|Value|
|---|---|
|ReferencingEntity|`flowlog`|
|ReferencingAttribute|`desktopflowid`|
|ReferencedEntityNavigationPropertyName|`workflow_flowlog_desktopflowid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_flowrun_Workflow"></a> workflow_flowrun_Workflow

Many-To-One Relationship: [flowrun workflow_flowrun_Workflow](flowrun.md#BKMK_workflow_flowrun_Workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`flowrun`|
|ReferencingAttribute|`workflow`|
|ReferencedEntityNavigationPropertyName|`workflow_flowrun_Workflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Workflow_licenseentitledby-one-to-many"></a> Workflow_licenseentitledby

Many-To-One Relationship: [workflow Workflow_licenseentitledby](#BKMK_Workflow_licenseentitledby-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`workflow`|
|ReferencingAttribute|`licenseentitledby`|
|ReferencedEntityNavigationPropertyName|`Workflow_licenseentitledby`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_parent_workflow-one-to-many"></a> workflow_parent_workflow

Many-To-One Relationship: [workflow workflow_parent_workflow](#BKMK_workflow_parent_workflow-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`workflow`|
|ReferencingAttribute|`parentworkflowid`|
|ReferencedEntityNavigationPropertyName|`workflow_parent_workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

Many-To-One Relationship: [syncerror Workflow_SyncErrors](syncerror.md#BKMK_Workflow_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Workflow_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_workflowbinary_Process"></a> workflow_workflowbinary_Process

Many-To-One Relationship: [workflowbinary workflow_workflowbinary_Process](workflowbinary.md#BKMK_workflow_workflowbinary_Process)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowbinary`|
|ReferencingAttribute|`process`|
|ReferencedEntityNavigationPropertyName|`workflow_workflowbinary_Process`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflowmetadata_WorkflowId_workflow"></a> workflowmetadata_WorkflowId_workflow

Many-To-One Relationship: [workflowmetadata workflowmetadata_WorkflowId_workflow](workflowmetadata.md#BKMK_workflowmetadata_WorkflowId_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowmetadata`|
|ReferencingAttribute|`workflowid`|
|ReferencedEntityNavigationPropertyName|`workflowmetadata_WorkflowId_workflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|


## Many-to-Many relationships

These relationships are many-to-many. Listed by **SchemaName**.

- [botcomponent_workflow](#BKMK_botcomponent_workflow)
- [workflow_card_connections](#BKMK_workflow_card_connections)

### <a name="BKMK_botcomponent_workflow"></a> botcomponent_workflow

See [botcomponent botcomponent_workflow Many-To-Many Relationship](botcomponent.md#BKMK_botcomponent_workflow)

|Property|Value|
|---|---|
|IntersectEntityName|`botcomponent_workflow`|
|IsCustomizable|False|
|SchemaName|`botcomponent_workflow`|
|IntersectAttribute|`workflowid`|
|NavigationPropertyName|`botcomponent_workflow`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_workflow_card_connections"></a> workflow_card_connections

See [card workflow_card_connections Many-To-Many Relationship](card.md#BKMK_workflow_card_connections)

|Property|Value|
|---|---|
|IntersectEntityName|`workflowcardconnections`|
|IsCustomizable|False|
|SchemaName|`workflow_card_connections`|
|IntersectAttribute|`workflowid`|
|NavigationPropertyName|`workflow_card_connections`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.workflow?displayProperty=fullName>
