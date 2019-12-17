---
title: "Workflow Entity Reference (Common Data Service)| MicrosoftDocs"
description: "Includes schema information and supported messages for the Workflow entity in Common Data Service."
ms.date: 11/07/2019
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
---
# Workflow Entity Reference

Set of logical rules that define the steps necessary to automate a specific business process, task, or set of actions to be performed.


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/workflows(*workflowid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/workflows<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|CreateWorkflowFromTemplate|<xref href="Microsoft.Dynamics.CRM.CreateWorkflowFromTemplate?text=CreateWorkflowFromTemplate Action" />|<xref:Microsoft.Crm.Sdk.Messages.CreateWorkflowFromTemplateRequest>|
|Delete|DELETE [*org URI*]/api/data/v9.0/workflows(*workflowid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|ExecuteWorkflow|<xref href="Microsoft.Dynamics.CRM.ExecuteWorkflow?text=ExecuteWorkflow Action" />|<xref:Microsoft.Crm.Sdk.Messages.ExecuteWorkflowRequest>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/workflows(*workflowid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/workflows<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|SetState|PATCH [*org URI*]/api/data/v9.0/workflows(*workflowid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `statecode` and `statuscode` properties.|<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/workflows(*workflowid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Entity Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|Workflows|
|DisplayCollectionName|Processes|
|DisplayName|Process|
|EntitySetName|workflows|
|IsBPFEntity|False|
|LogicalCollectionName|workflows|
|LogicalName|workflow|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|workflowid|
|PrimaryNameAttribute|name|
|SchemaName|Workflow|

<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncAutoDelete](#BKMK_AsyncAutoDelete)
- [BusinessProcessType](#BKMK_BusinessProcessType)
- [Category](#BKMK_Category)
- [ClientData](#BKMK_ClientData)
- [CreateStage](#BKMK_CreateStage)
- [DeleteStage](#BKMK_DeleteStage)
- [Description](#BKMK_Description)
- [EntityImage](#BKMK_EntityImage)
- [FormId](#BKMK_FormId)
- [InputParameters](#BKMK_InputParameters)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsTransacted](#BKMK_IsTransacted)
- [LanguageCode](#BKMK_LanguageCode)
- [Mode](#BKMK_Mode)
- [Name](#BKMK_Name)
- [OnDemand](#BKMK_OnDemand)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [PrimaryEntity](#BKMK_PrimaryEntity)
- [ProcessOrder](#BKMK_ProcessOrder)
- [ProcessRoleAssignment](#BKMK_ProcessRoleAssignment)
- [Rank](#BKMK_Rank)
- [RendererObjectTypeCode](#BKMK_RendererObjectTypeCode)
- [RunAs](#BKMK_RunAs)
- [Scope](#BKMK_Scope)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [Subprocess](#BKMK_Subprocess)
- [SyncWorkflowLogOnFailure](#BKMK_SyncWorkflowLogOnFailure)
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
|--------|-----|
|Description|Indicates whether the asynchronous system job is automatically deleted on completion.|
|DisplayName|Delete Job On Completion|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|asyncautodelete|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### AsyncAutoDelete Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_BusinessProcessType"></a> BusinessProcessType

|Property|Value|
|--------|-----|
|Description|Business Process Type.|
|DisplayName|Business Process Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|businessprocesstype|
|RequiredLevel|None|
|Type|Picklist|

#### BusinessProcessType Options

|Value|Label|
|-----|-----|
|0|Business Flow|
|1|Task Flow|



### <a name="BKMK_Category"></a> Category

|Property|Value|
|--------|-----|
|Description|Category of the process.|
|DisplayName|Category|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|category|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Category Options

|Value|Label|
|-----|-----|
|0|Workflow|
|1|Dialog|
|2|Business Rule|
|3|Action|
|4|Business Process Flow|
|5|Modern Flow|
|6|Reserved|



### <a name="BKMK_ClientData"></a> ClientData

|Property|Value|
|--------|-----|
|Description|Business logic converted into client data|
|DisplayName|Client Data|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|clientdata|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_CreateStage"></a> CreateStage

|Property|Value|
|--------|-----|
|Description|Stage of the process when triggered on Create.|
|DisplayName|Create Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|createstage|
|RequiredLevel|None|
|Type|Picklist|

#### CreateStage Options

|Value|Label|
|-----|-----|
|20|Pre-operation|
|40|Post-operation|



### <a name="BKMK_DeleteStage"></a> DeleteStage

|Property|Value|
|--------|-----|
|Description|Stage of the process when triggered on Delete.|
|DisplayName|Delete stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|deletestage|
|RequiredLevel|None|
|Type|Picklist|

#### DeleteStage Options

|Value|Label|
|-----|-----|
|20|Pre-operation|
|40|Post-operation|



### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|Description of the process.|
|DisplayName|Description|
|Format|TextArea|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|100000|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|--------|-----|
|Description|Shows the default image for the record.|
|DisplayName|Default Image|
|IsPrimaryImage|True|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage|
|MaxHeight|144|
|MaxWidth|144|
|RequiredLevel|None|
|Type|Image|


### <a name="BKMK_FormId"></a> FormId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated form.|
|DisplayName|Form ID|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|formid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_InputParameters"></a> InputParameters

|Property|Value|
|--------|-----|
|Description|Input parameters to the process.|
|DisplayName|Input Parameters|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|inputparameters|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


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
|Description|Information that specifies whether this component can be customized.|
|DisplayName|Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_IsTransacted"></a> IsTransacted

|Property|Value|
|--------|-----|
|Description|Whether or not the steps in the process are executed in a single transaction.|
|DisplayName|Is Transacted|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|istransacted|
|RequiredLevel|None|
|Type|Boolean|

#### IsTransacted Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: True



### <a name="BKMK_LanguageCode"></a> LanguageCode

|Property|Value|
|--------|-----|
|Description|Language of the process.|
|DisplayName|Language|
|Format|Language|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|languagecode|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_Mode"></a> Mode

|Property|Value|
|--------|-----|
|Description|Shows the mode of the process.|
|DisplayName|Mode|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|mode|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Mode Options

|Value|Label|
|-----|-----|
|0|Background|
|1|Real-time|



### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Name of the process.|
|DisplayName|Process Name|
|FormatName|Text|
|IsLocalizable|True|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OnDemand"></a> OnDemand

|Property|Value|
|--------|-----|
|Description|Indicates whether the process is able to run as an on-demand process.|
|DisplayName|Run as On Demand|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ondemand|
|RequiredLevel|None|
|Type|Boolean|

#### OnDemand Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user or team who owns the process.|
|DisplayName|Owner|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|ownerid|
|RequiredLevel|SystemRequired|
|Targets|systemuser|
|Type|Owner|


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owneridtype|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_PrimaryEntity"></a> PrimaryEntity

|Property|Value|
|--------|-----|
|Description|Primary entity for the process. The process can be associated for one or more SDK operations defined on the primary entity.|
|DisplayName|Primary Entity|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|primaryentity|
|RequiredLevel|SystemRequired|
|Type|EntityName|


### <a name="BKMK_ProcessOrder"></a> ProcessOrder

|Property|Value|
|--------|-----|
|Description|Type the business process flow order.|
|DisplayName|Process Order|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processorder|
|MaxValue|2147483647|
|MinValue|0|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_ProcessRoleAssignment"></a> ProcessRoleAssignment

|Property|Value|
|--------|-----|
|Description|Contains the role assignment for the process.|
|DisplayName|Role assignment for Process|
|Format|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|processroleassignment|
|MaxLength|1048576|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Rank"></a> Rank

|Property|Value|
|--------|-----|
|Description|Indicates the rank for order of execution for the synchronous workflow.|
|DisplayName|Rank|
|Format|None|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rank|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_RendererObjectTypeCode"></a> RendererObjectTypeCode

|Property|Value|
|--------|-----|
|Description|The renderer type of Workflow|
|DisplayName|Renderer Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|rendererobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_RunAs"></a> RunAs

|Property|Value|
|--------|-----|
|Description|Specifies the system user account under which a workflow executes.|
|DisplayName|Run As User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|runas|
|RequiredLevel|None|
|Type|Picklist|

#### RunAs Options

|Value|Label|
|-----|-----|
|0|Owner|
|1|Calling User|



### <a name="BKMK_Scope"></a> Scope

|Property|Value|
|--------|-----|
|Description|Scope of the process.|
|DisplayName|Scope|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|scope|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Scope Options

|Value|Label|
|-----|-----|
|1|User|
|2|Business Unit|
|3|Parent: Child Business Units|
|4|Organization|



### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|--------|-----|
|Description|Status of the process.|
|DisplayName|Status|
|IsValidForCreate|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statecode|
|RequiredLevel|SystemRequired|
|Type|State|

#### StateCode Options

|Value|Label|DefaultStatus|InvariantName|
|-----|-----|-------------|-------------|
|0|Draft|1|Draft|
|1|Activated|2|Activated|



### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|--------|-----|
|Description|Additional information about status of the process.|
|DisplayName|Status Reason|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|statuscode|
|RequiredLevel|None|
|Type|Status|

#### StatusCode Options

|Value|Label|State|
|-----|-----|-----|
|1|Draft|0|
|2|Activated|1|



### <a name="BKMK_Subprocess"></a> Subprocess

|Property|Value|
|--------|-----|
|Description|Indicates whether the process can be included in other processes as a child process.|
|DisplayName|Is Child Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|subprocess|
|RequiredLevel|None|
|Type|Boolean|

#### Subprocess Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_SyncWorkflowLogOnFailure"></a> SyncWorkflowLogOnFailure

|Property|Value|
|--------|-----|
|Description|Select whether synchronous workflow failures will be saved to log files.|
|DisplayName|Log upon Failure|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|syncworkflowlogonfailure|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### SyncWorkflowLogOnFailure Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TriggerOnCreate"></a> TriggerOnCreate

|Property|Value|
|--------|-----|
|Description|Indicates whether the process will be triggered when the primary entity is created.|
|DisplayName|Trigger On Create|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|triggeroncreate|
|RequiredLevel|None|
|Type|Boolean|

#### TriggerOnCreate Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TriggerOnDelete"></a> TriggerOnDelete

|Property|Value|
|--------|-----|
|Description|Indicates whether the process will be triggered on deletion of the primary entity.|
|DisplayName|Trigger On Delete|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|triggerondelete|
|RequiredLevel|None|
|Type|Boolean|

#### TriggerOnDelete Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TriggerOnUpdateAttributeList"></a> TriggerOnUpdateAttributeList

|Property|Value|
|--------|-----|
|Description|Attributes that trigger the process when updated.|
|DisplayName|Trigger On Update Attribute List|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|triggeronupdateattributelist|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_Type"></a> Type

|Property|Value|
|--------|-----|
|Description|Type of the process.|
|DisplayName|Type|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|type|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### Type Options

|Value|Label|
|-----|-----|
|1|Definition|
|2|Activation|
|3|Template|



### <a name="BKMK_UIFlowType"></a> UIFlowType

|Property|Value|
|--------|-----|
|Description|Type of the UI Flow process.|
|DisplayName|UI Flow Type|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|uiflowtype|
|RequiredLevel|None|
|Type|Picklist|

#### UIFlowType Options

|Value|Label|
|-----|-----|
|0|Desktop|
|1|Selenium IDE|
|2|PowerShell|



### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|--------|-----|
|Description|Unique name of the process|
|DisplayName|Unique Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|uniquename|
|MaxLength|256|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_UpdateStage"></a> UpdateStage

|Property|Value|
|--------|-----|
|Description|Select the stage a process will be triggered on update.|
|DisplayName|Update Stage|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|updatestage|
|RequiredLevel|None|
|Type|Picklist|

#### UpdateStage Options

|Value|Label|
|-----|-----|
|20|Pre-operation|
|40|Post-operation|



### <a name="BKMK_WorkflowId"></a> WorkflowId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the process.|
|DisplayName|Process|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|workflowid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Xaml"></a> Xaml

|Property|Value|
|--------|-----|
|Description|XAML that defines the process.|
|DisplayName||
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|xaml|
|MaxLength|1073741823|
|RequiredLevel|ApplicationRequired|
|Type|Memo|

<a name="read-only-attributes"></a>

## Read-only attributes

These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActiveWorkflowId](#BKMK_ActiveWorkflowId)
- [ActiveWorkflowIdName](#BKMK_ActiveWorkflowIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IsCrmUIWorkflow](#BKMK_IsCrmUIWorkflow)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningBusinessUnitName](#BKMK_OwningBusinessUnitName)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [ParentWorkflowId](#BKMK_ParentWorkflowId)
- [ParentWorkflowIdName](#BKMK_ParentWorkflowIdName)
- [PluginTypeId](#BKMK_PluginTypeId)
- [SdkMessageId](#BKMK_SdkMessageId)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [UIData](#BKMK_UIData)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkflowIdUnique](#BKMK_WorkflowIdUnique)


### <a name="BKMK_ActiveWorkflowId"></a> ActiveWorkflowId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the latest activation record for the process.|
|DisplayName|Active Process ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|activeworkflowid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_ActiveWorkflowIdName"></a> ActiveWorkflowIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|activeworkflowidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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

#### ComponentState Options

|Value|Label|
|-----|-----|
|0|Published|
|1|Unpublished|
|2|Deleted|
|3|Deleted Unpublished|



### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who created the process.|
|DisplayName|Created By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedByName"></a> CreatedByName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the process was created.|
|DisplayName|Created On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who created the process.|
|DisplayName|Created By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|createdonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_timestamp|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Url|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimage_url|
|MaxLength|200|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Entity Image Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|entityimageid|
|RequiredLevel|None|
|Type|Uniqueidentifier|


### <a name="BKMK_IsCrmUIWorkflow"></a> IsCrmUIWorkflow

|Property|Value|
|--------|-----|
|Description|Indicates whether the process was created using the Microsoft Dynamics 365 Web application.|
|DisplayName|Is CRM Process|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscrmuiworkflow|
|RequiredLevel|None|
|Type|Boolean|

#### IsCrmUIWorkflow Options

|Value|Label|
|-----|-----|
|1|Yes|
|0|No|

**DefaultValue**: False



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

#### IsManaged Options

|Value|Label|
|-----|-----|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who last modified the process.|
|DisplayName|Modified By|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Date and time when the process was last modified.|
|DisplayName|Modified On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|--------|-----|
|Description|Unique identifier of the delegate user who last modified the process.|
|DisplayName|Modified By (Delegate)|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|modifiedonbehalfby|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|--------|-----|
|Description||
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

|Property|Value|
|--------|-----|
|Description||
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

|Property|Value|
|--------|-----|
|Description|Unique identifier of the business unit that owns the process.|
|DisplayName|Owning Business Unit|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

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
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|Unique identifier of the team who owns the process.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets|team|
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Unique identifier of the user who owns the process.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets|systemuser|
|Type|Lookup|


### <a name="BKMK_ParentWorkflowId"></a> ParentWorkflowId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the definition for process activation.|
|DisplayName|Parent Process ID|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|parentworkflowid|
|RequiredLevel|None|
|Targets|workflow|
|Type|Lookup|


### <a name="BKMK_ParentWorkflowIdName"></a> ParentWorkflowIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|parentworkflowidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_PluginTypeId"></a> PluginTypeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the plug-in type.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|plugintypeid|
|RequiredLevel|None|
|Targets|sdkmessagefilter|
|Type|Lookup|


### <a name="BKMK_SdkMessageId"></a> SdkMessageId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SDK Message associated with this workflow.|
|DisplayName|SDK Message|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|sdkmessageid|
|RequiredLevel|None|
|Targets|sdkmessage|
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


### <a name="BKMK_UIData"></a> UIData

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|UI Data|
|Format|TextArea|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|uidata|
|MaxLength|1073741823|
|RequiredLevel|None|
|Type|Memo|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|versionnumber|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|
|RequiredLevel|None|
|Type|BigInt|


### <a name="BKMK_WorkflowIdUnique"></a> WorkflowIdUnique

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|workflowidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [Workflow_Annotation](#BKMK_Workflow_Annotation)
- [process_processstage](#BKMK_process_processstage)
- [lk_asyncoperation_workflowactivationid](#BKMK_lk_asyncoperation_workflowactivationid)
- [process_processtrigger](#BKMK_process_processtrigger)
- [lk_expiredprocess_processid](#BKMK_lk_expiredprocess_processid)
- [workflow_parent_workflow](#BKMK_workflow_parent_workflow)
- [slaitembase_workflowid](#BKMK_slaitembase_workflowid)
- [slabase_workflowid](#BKMK_slabase_workflowid)
- [lk_processsession_processid](#BKMK_lk_processsession_processid)
- [lk_translationprocess_processid](#BKMK_lk_translationprocess_processid)
- [lk_newprocess_processid](#BKMK_lk_newprocess_processid)
- [Workflow_SyncErrors](#BKMK_Workflow_SyncErrors)
- [workflow_active_workflow](#BKMK_workflow_active_workflow)
- [regardingobjectid_process](#BKMK_regardingobjectid_process)
- [workflow_workflowbinary_Process](#BKMK_workflow_workflowbinary_Process)
- [msdyn_workflow_msdyn_solutionhealthrule_Workflow](#BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow)
- [msdyn_workflow_msdyn_solutionhealthrule_resolutionaction](#BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction)


### <a name="BKMK_Workflow_Annotation"></a> Workflow_Annotation

Same as annotation entity [Workflow_Annotation](annotation.md#BKMK_Workflow_Annotation) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|annotation|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Workflow_Annotation|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_process_processstage"></a> process_processstage

Same as processstage entity [process_processstage](processstage.md#BKMK_process_processstage) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processstage|
|ReferencingAttribute|processid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|process_processstage|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_asyncoperation_workflowactivationid"></a> lk_asyncoperation_workflowactivationid

Same as asyncoperation entity [lk_asyncoperation_workflowactivationid](asyncoperation.md#BKMK_lk_asyncoperation_workflowactivationid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|workflowactivationid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_asyncoperation_workflowactivationid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_process_processtrigger"></a> process_processtrigger

Same as processtrigger entity [process_processtrigger](processtrigger.md#BKMK_process_processtrigger) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processtrigger|
|ReferencingAttribute|processid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|process_processtrigger|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_expiredprocess_processid"></a> lk_expiredprocess_processid

Same as expiredprocess entity [lk_expiredprocess_processid](expiredprocess.md#BKMK_lk_expiredprocess_processid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|expiredprocess|
|ReferencingAttribute|processid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|workflow_expiredprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_workflow_parent_workflow"></a> workflow_parent_workflow

Same as workflow entity [workflow_parent_workflow](workflow.md#BKMK_workflow_parent_workflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|parentworkflowid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_parent_workflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slaitembase_workflowid"></a> slaitembase_workflowid

Same as slaitem entity [slaitembase_workflowid](slaitem.md#BKMK_slaitembase_workflowid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|slaitem|
|ReferencingAttribute|workflowid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|slaitembase_workflowid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_slabase_workflowid"></a> slabase_workflowid

Same as sla entity [slabase_workflowid](sla.md#BKMK_slabase_workflowid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|sla|
|ReferencingAttribute|workflowid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|slabase_workflowid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

Same as processsession entity [lk_processsession_processid](processsession.md#BKMK_lk_processsession_processid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|processsession|
|ReferencingAttribute|processid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|lk_processsession_processid|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_translationprocess_processid"></a> lk_translationprocess_processid

Same as translationprocess entity [lk_translationprocess_processid](translationprocess.md#BKMK_lk_translationprocess_processid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|translationprocess|
|ReferencingAttribute|processid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|workflow_translationprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_lk_newprocess_processid"></a> lk_newprocess_processid

Same as newprocess entity [lk_newprocess_processid](newprocess.md#BKMK_lk_newprocess_processid) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|newprocess|
|ReferencingAttribute|processid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|workflow_newprocess|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

Same as syncerror entity [Workflow_SyncErrors](syncerror.md#BKMK_Workflow_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|Workflow_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|


### <a name="BKMK_workflow_active_workflow"></a> workflow_active_workflow

Same as workflow entity [workflow_active_workflow](workflow.md#BKMK_workflow_active_workflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflow|
|ReferencingAttribute|activeworkflowid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_active_workflow|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Restrict<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_regardingobjectid_process"></a> regardingobjectid_process

**Added by**: Power Automate Extensions package Solution

Same as flowsession entity [regardingobjectid_process](flowsession.md#BKMK_regardingobjectid_process) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|flowsession|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|regardingobjectid_process|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_workflow_workflowbinary_Process"></a> workflow_workflowbinary_Process

**Added by**: Power Automate Extensions package Solution

Same as workflowbinary entity [workflow_workflowbinary_Process](workflowbinary.md#BKMK_workflow_workflowbinary_Process) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|workflowbinary|
|ReferencingAttribute|process|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|workflow_workflowbinary_Process|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow"></a> msdyn_workflow_msdyn_solutionhealthrule_Workflow

**Added by**: Power Apps Checker Solution

Same as msdyn_solutionhealthrule entity [msdyn_workflow_msdyn_solutionhealthrule_Workflow](msdyn_solutionhealthrule.md#BKMK_msdyn_workflow_msdyn_solutionhealthrule_Workflow) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|msdyn_workflow|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_workflow_msdyn_solutionhealthrule_Workflow|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction"></a> msdyn_workflow_msdyn_solutionhealthrule_resolutionaction

**Added by**: Power Apps Checker Solution

Same as msdyn_solutionhealthrule entity [msdyn_workflow_msdyn_solutionhealthrule_resolutionaction](msdyn_solutionhealthrule.md#BKMK_msdyn_workflow_msdyn_solutionhealthrule_resolutionaction) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|msdyn_solutionhealthrule|
|ReferencingAttribute|msdyn_resolutionaction|
|IsHierarchical|False|
|IsCustomizable|False|
|ReferencedEntityNavigationPropertyName|msdyn_workflow_msdyn_solutionhealthrule_resolutionaction|
|AssociatedMenuConfiguration|Behavior: UseCollectionName<br />Group: Details<br />Label: <br />Order: 10000|
|CascadeConfiguration|Assign: NoCascade<br />Delete: RemoveLink<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [workflow_active_workflow](#BKMK_workflow_active_workflow)
- [workflow_modifiedby](#BKMK_workflow_modifiedby)
- [workflow_createdonbehalfby](#BKMK_workflow_createdonbehalfby)
- [business_unit_workflow](#BKMK_business_unit_workflow)
- [system_user_workflow](#BKMK_system_user_workflow)
- [team_workflow](#BKMK_team_workflow)
- [workflow_createdby](#BKMK_workflow_createdby)
- [workflow_parent_workflow](#BKMK_workflow_parent_workflow)
- [workflow_modifiedonbehalfby](#BKMK_workflow_modifiedonbehalfby)


### <a name="BKMK_workflow_active_workflow"></a> workflow_active_workflow

See workflow Entity [workflow_active_workflow](workflow.md#BKMK_workflow_active_workflow) One-To-Many relationship.

### <a name="BKMK_workflow_modifiedby"></a> workflow_modifiedby

See systemuser Entity [workflow_modifiedby](systemuser.md#BKMK_workflow_modifiedby) One-To-Many relationship.

### <a name="BKMK_workflow_createdonbehalfby"></a> workflow_createdonbehalfby

See systemuser Entity [workflow_createdonbehalfby](systemuser.md#BKMK_workflow_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_workflow"></a> business_unit_workflow

See businessunit Entity [business_unit_workflow](businessunit.md#BKMK_business_unit_workflow) One-To-Many relationship.

### <a name="BKMK_system_user_workflow"></a> system_user_workflow

See systemuser Entity [system_user_workflow](systemuser.md#BKMK_system_user_workflow) One-To-Many relationship.

### <a name="BKMK_team_workflow"></a> team_workflow

See team Entity [team_workflow](team.md#BKMK_team_workflow) One-To-Many relationship.

### <a name="BKMK_workflow_createdby"></a> workflow_createdby

See systemuser Entity [workflow_createdby](systemuser.md#BKMK_workflow_createdby) One-To-Many relationship.

### <a name="BKMK_workflow_parent_workflow"></a> workflow_parent_workflow

See workflow Entity [workflow_parent_workflow](workflow.md#BKMK_workflow_parent_workflow) One-To-Many relationship.

### <a name="BKMK_workflow_modifiedonbehalfby"></a> workflow_modifiedonbehalfby

See systemuser Entity [workflow_modifiedonbehalfby](systemuser.md#BKMK_workflow_modifiedonbehalfby) One-To-Many relationship.

### See also

[About the Entity Reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.workflow?text=workflow EntityType" />