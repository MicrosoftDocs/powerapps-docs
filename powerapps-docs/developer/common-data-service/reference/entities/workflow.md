---
title: "Workflow Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Workflow entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# Workflow Entity Reference

Set of logical rules that define the steps necessary to automate a specific business process, task, or set of actions to be performed.

## Entity Properties

**DisplayName**: Process<br />
**DisplayCollectionName**: Processes<br />
**SchemaName**: Workflow<br />
**CollectionSchemaName**: Workflows<br />
**LogicalName**: workflow<br />
**LogicalCollectionName**: workflows<br />
**EntitySetName**: workflows<br />
**PrimaryIdAttribute**: workflowid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncAutoDelete](#BKMK_AsyncAutoDelete)
- [BusinessProcessType](#BKMK_BusinessProcessType)
- [Category](#BKMK_Category)
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
- [UniqueName](#BKMK_UniqueName)
- [UpdateStage](#BKMK_UpdateStage)
- [WorkflowId](#BKMK_WorkflowId)
- [Xaml](#BKMK_Xaml)


### <a name="BKMK_AsyncAutoDelete"></a> AsyncAutoDelete

**Description**: Indicates whether the asynchronous system job is automatically deleted on completion.<br />
**DisplayName**: Delete Job On Completion<br />
**LogicalName**: asyncautodelete<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_BusinessProcessType"></a> BusinessProcessType

**Description**: Business Process Type.<br />
**DisplayName**: Business Process Type<br />
**LogicalName**: businessprocesstype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Business Flow
- **Value**: 1 **Label**: Task Flow



### <a name="BKMK_Category"></a> Category

**Description**: Category of the process.<br />
**DisplayName**: Category<br />
**LogicalName**: category<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Workflow
- **Value**: 1 **Label**: Dialog
- **Value**: 2 **Label**: Business Rule
- **Value**: 3 **Label**: Action
- **Value**: 4 **Label**: Business Process Flow



### <a name="BKMK_CreateStage"></a> CreateStage

**Description**: Stage of the process when triggered on Create.<br />
**DisplayName**: Create Stage<br />
**LogicalName**: createstage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 20 **Label**: Pre-operation
- **Value**: 40 **Label**: Post-operation



### <a name="BKMK_DeleteStage"></a> DeleteStage

**Description**: Stage of the process when triggered on Delete.<br />
**DisplayName**: Delete stage<br />
**LogicalName**: deletestage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 20 **Label**: Pre-operation
- **Value**: 40 **Label**: Post-operation



### <a name="BKMK_Description"></a> Description

**Description**: Description of the process.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: True<br />
**MaxLength**: 100000


### <a name="BKMK_EntityImage"></a> EntityImage

**Description**: Shows the default image for the record.<br />
**DisplayName**: Default Image<br />
**LogicalName**: entityimage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Image<br />
**IsPrimaryImage**: True<br />
**MaxHeight**: 144<br />
**MaxWidth**: 144


### <a name="BKMK_FormId"></a> FormId

**Description**: Unique identifier of the associated form.<br />
**DisplayName**: Form ID<br />
**LogicalName**: formid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_InputParameters"></a> InputParameters

**Description**: Input parameters to the process.<br />
**DisplayName**: Input Parameters<br />
**LogicalName**: inputparameters<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the form is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Description**: Information that specifies whether this component can be customized.<br />
**DisplayName**: Customizable<br />
**LogicalName**: iscustomizable<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_IsTransacted"></a> IsTransacted

**Description**: Whether or not the steps in the process are executed in a single transaction.<br />
**DisplayName**: Is Transacted<br />
**LogicalName**: istransacted<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_LanguageCode"></a> LanguageCode

**Description**: Language of the process.<br />
**DisplayName**: Language<br />
**LogicalName**: languagecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: Language<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_Mode"></a> Mode

**Description**: Shows the mode of the process.<br />
**DisplayName**: Mode<br />
**LogicalName**: mode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Background
- **Value**: 1 **Label**: Real-time



### <a name="BKMK_Name"></a> Name

**Description**: Name of the process.<br />
**DisplayName**: Process Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: True<br />
**MaxLength**: 100


### <a name="BKMK_OnDemand"></a> OnDemand

**Description**: Indicates whether the process is able to run as an on-demand process.<br />
**DisplayName**: Run as On Demand<br />
**LogicalName**: ondemand<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the process.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_PrimaryEntity"></a> PrimaryEntity

**Description**: Primary entity for the process. The process can be associated for one or more SDK operations defined on the primary entity.<br />
**DisplayName**: Primary Entity<br />
**LogicalName**: primaryentity<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_ProcessOrder"></a> ProcessOrder

**Description**: Type the business process flow order.<br />
**DisplayName**: Process Order<br />
**LogicalName**: processorder<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ProcessRoleAssignment"></a> ProcessRoleAssignment

**Description**: Contains the role assignment for the process.<br />
**DisplayName**: Role assignment for Process<br />
**LogicalName**: processroleassignment<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1048576


### <a name="BKMK_Rank"></a> Rank

**Description**: Indicates the rank for order of execution for the synchronous workflow.<br />
**DisplayName**: Rank<br />
**LogicalName**: rank<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_RendererObjectTypeCode"></a> RendererObjectTypeCode

**Description**: The renderer type of Workflow<br />
**DisplayName**: Renderer Type<br />
**LogicalName**: rendererobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_RunAs"></a> RunAs

**Description**: Specifies the system user account under which a workflow executes.<br />
**DisplayName**: Run As User<br />
**LogicalName**: runas<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Owner
- **Value**: 1 **Label**: Calling User



### <a name="BKMK_Scope"></a> Scope

**Description**: Scope of the process.<br />
**DisplayName**: Scope<br />
**LogicalName**: scope<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: User
- **Value**: 2 **Label**: Business Unit
- **Value**: 3 **Label**: Parent: Child Business Units
- **Value**: 4 **Label**: Organization



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the process.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Draft **DefaultStatus**: 1 **InvariantName**: Draft
- **Value**: 1 **Label**: Activated **DefaultStatus**: 2 **InvariantName**: Activated



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Additional information about status of the process.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Draft **State**: 0
- **Value**: 2 **Label**: Activated **State**: 1



### <a name="BKMK_Subprocess"></a> Subprocess

**Description**: Indicates whether the process can be included in other processes as a child process.<br />
**DisplayName**: Is Child Process<br />
**LogicalName**: subprocess<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SyncWorkflowLogOnFailure"></a> SyncWorkflowLogOnFailure

**Description**: Select whether synchronous workflow failures will be saved to log files.<br />
**DisplayName**: Log upon Failure<br />
**LogicalName**: syncworkflowlogonfailure<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TriggerOnCreate"></a> TriggerOnCreate

**Description**: Indicates whether the process will be triggered when the primary entity is created.<br />
**DisplayName**: Trigger On Create<br />
**LogicalName**: triggeroncreate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TriggerOnDelete"></a> TriggerOnDelete

**Description**: Indicates whether the process will be triggered on deletion of the primary entity.<br />
**DisplayName**: Trigger On Delete<br />
**LogicalName**: triggerondelete<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_TriggerOnUpdateAttributeList"></a> TriggerOnUpdateAttributeList

**Description**: Attributes that trigger the process when updated.<br />
**DisplayName**: Trigger On Update Attribute List<br />
**LogicalName**: triggeronupdateattributelist<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Type"></a> Type

**Description**: Type of the process.<br />
**DisplayName**: Type<br />
**LogicalName**: type<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Definition
- **Value**: 2 **Label**: Activation
- **Value**: 3 **Label**: Template



### <a name="BKMK_UniqueName"></a> UniqueName

**Description**: Unique name of the process<br />
**DisplayName**: Unique Name<br />
**LogicalName**: uniquename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_UpdateStage"></a> UpdateStage

**Description**: Select the stage a process will be triggered on update.<br />
**DisplayName**: Update Stage<br />
**LogicalName**: updatestage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 20 **Label**: Pre-operation
- **Value**: 40 **Label**: Post-operation



### <a name="BKMK_WorkflowId"></a> WorkflowId

**Description**: Unique identifier of the process.<br />
**DisplayName**: Process<br />
**LogicalName**: workflowid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Xaml"></a> Xaml

**Description**: XAML that defines the process.<br />
**DisplayName**: <br />
**LogicalName**: xaml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActiveWorkflowId](#BKMK_ActiveWorkflowId)
- [ActiveWorkflowIdName](#BKMK_ActiveWorkflowIdName)
- [ClientData](#BKMK_ClientData)
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

**Description**: Unique identifier of the latest activation record for the process.<br />
**DisplayName**: Active Process ID<br />
**LogicalName**: activeworkflowid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: workflow


### <a name="BKMK_ActiveWorkflowIdName"></a> ActiveWorkflowIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: activeworkflowidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ClientData"></a> ClientData

**Description**: Business logic converted into client data<br />
**DisplayName**: Client Data<br />
**LogicalName**: clientdata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the process.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the process was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the process.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_timestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_url<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EntityImageId"></a> EntityImageId

**Description**: For internal use only.<br />
**DisplayName**: Entity Image Id<br />
**LogicalName**: entityimageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IsCrmUIWorkflow"></a> IsCrmUIWorkflow

**Description**: Indicates whether the process was created using the Microsoft Dynamics 365 Web application.<br />
**DisplayName**: Is CRM Process<br />
**LogicalName**: iscrmuiworkflow<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Indicates whether the solution component is part of a managed solution.<br />
**DisplayName**: Is Managed<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the process.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the process was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the process.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: For internal use only.<br />
**DisplayName**: Record Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns the process.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningBusinessUnitName"></a> OwningBusinessUnitName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owningbusinessunitname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the process.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the process.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ParentWorkflowId"></a> ParentWorkflowId

**Description**: Unique identifier of the definition for process activation.<br />
**DisplayName**: Parent Process ID<br />
**LogicalName**: parentworkflowid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: workflow


### <a name="BKMK_ParentWorkflowIdName"></a> ParentWorkflowIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentworkflowidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PluginTypeId"></a> PluginTypeId

**Description**: Unique identifier of the plug-in type.<br />
**DisplayName**: <br />
**LogicalName**: plugintypeid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sdkmessagefilter


### <a name="BKMK_SdkMessageId"></a> SdkMessageId

**Description**: Unique identifier of the SDK Message associated with this workflow.<br />
**DisplayName**: SDK Message<br />
**LogicalName**: sdkmessageid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sdkmessage


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_UIData"></a> UIData

**Description**: For internal use only.<br />
**DisplayName**: UI Data<br />
**LogicalName**: uidata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_WorkflowIdUnique"></a> WorkflowIdUnique

**Description**: For internal use only.<br />
**DisplayName**: <br />
**LogicalName**: workflowidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [Workflow_Annotation](#BKMK_Workflow_Annotation)
- [workflowid_profilerule](#BKMK_workflowid_profilerule)
- [process_processstage](#BKMK_process_processstage)
- [Workflow_routingrule](#BKMK_Workflow_routingrule)
- [lk_asyncoperation_workflowactivationid](#BKMK_lk_asyncoperation_workflowactivationid)
- [process_processtrigger](#BKMK_process_processtrigger)
- [lk_expiredprocess_processid](#BKMK_lk_expiredprocess_processid)
- [workflow_parent_workflow](#BKMK_workflow_parent_workflow)
- [userentityinstancedata_workflow](#BKMK_userentityinstancedata_workflow)
- [slaitembase_workflowid](#BKMK_slaitembase_workflowid)
- [slabase_workflowid](#BKMK_slabase_workflowid)
- [lk_processsession_processid](#BKMK_lk_processsession_processid)
- [workflow_dependencies](#BKMK_workflow_dependencies)
- [lk_translationprocess_processid](#BKMK_lk_translationprocess_processid)
- [lk_newprocess_processid](#BKMK_lk_newprocess_processid)
- [Workflow_SyncErrors](#BKMK_Workflow_SyncErrors)
- [workflow_active_workflow](#BKMK_workflow_active_workflow)
- [workflowid_convertrule](#BKMK_workflowid_convertrule)
- [convertruleitembase_workflowid](#BKMK_convertruleitembase_workflowid)


### <a name="BKMK_Workflow_Annotation"></a> Workflow_Annotation

Same as annotation entity [Workflow_Annotation](annotation.md#BKMK_Workflow_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Workflow_Annotation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_workflowid_profilerule"></a> workflowid_profilerule

Same as channelaccessprofilerule entity [workflowid_profilerule](channelaccessprofilerule.md#BKMK_workflowid_profilerule) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflowid_profilerule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_process_processstage"></a> process_processstage

Same as processstage entity [process_processstage](processstage.md#BKMK_process_processstage) Many-To-One relationship.

**ReferencingEntity**: processstage<br />
**ReferencingAttribute**: processid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: process_processstage<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Workflow_routingrule"></a> Workflow_routingrule

Same as routingrule entity [Workflow_routingrule](routingrule.md#BKMK_Workflow_routingrule) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Workflow_routingrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_asyncoperation_workflowactivationid"></a> lk_asyncoperation_workflowactivationid

Same as asyncoperation entity [lk_asyncoperation_workflowactivationid](asyncoperation.md#BKMK_lk_asyncoperation_workflowactivationid) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: workflowactivationid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_asyncoperation_workflowactivationid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_process_processtrigger"></a> process_processtrigger

Same as processtrigger entity [process_processtrigger](processtrigger.md#BKMK_process_processtrigger) Many-To-One relationship.

**ReferencingEntity**: processtrigger<br />
**ReferencingAttribute**: processid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: process_processtrigger<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_expiredprocess_processid"></a> lk_expiredprocess_processid

Same as expiredprocess entity [lk_expiredprocess_processid](expiredprocess.md#BKMK_lk_expiredprocess_processid) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: processid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: workflow_expiredprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_workflow_parent_workflow"></a> workflow_parent_workflow

Same as workflow entity [workflow_parent_workflow](workflow.md#BKMK_workflow_parent_workflow) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: parentworkflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_parent_workflow<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityinstancedata_workflow"></a> userentityinstancedata_workflow

Same as userentityinstancedata entity [userentityinstancedata_workflow](userentityinstancedata.md#BKMK_userentityinstancedata_workflow) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_workflow<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_slaitembase_workflowid"></a> slaitembase_workflowid

Same as slaitem entity [slaitembase_workflowid](slaitem.md#BKMK_slaitembase_workflowid) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: slaitembase_workflowid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_slabase_workflowid"></a> slabase_workflowid

Same as sla entity [slabase_workflowid](sla.md#BKMK_slabase_workflowid) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: slabase_workflowid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_processsession_processid"></a> lk_processsession_processid

Same as processsession entity [lk_processsession_processid](processsession.md#BKMK_lk_processsession_processid) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: processid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_processid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_workflow_dependencies"></a> workflow_dependencies

Same as workflowdependency entity [workflow_dependencies](workflowdependency.md#BKMK_workflow_dependencies) Many-To-One relationship.

**ReferencingEntity**: workflowdependency<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_dependencies<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_translationprocess_processid"></a> lk_translationprocess_processid

Same as translationprocess entity [lk_translationprocess_processid](translationprocess.md#BKMK_lk_translationprocess_processid) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: processid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: workflow_translationprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_newprocess_processid"></a> lk_newprocess_processid

Same as newprocess entity [lk_newprocess_processid](newprocess.md#BKMK_lk_newprocess_processid) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: processid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: workflow_newprocess<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Workflow_SyncErrors"></a> Workflow_SyncErrors

Same as syncerror entity [Workflow_SyncErrors](syncerror.md#BKMK_Workflow_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Workflow_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_workflow_active_workflow"></a> workflow_active_workflow

Same as workflow entity [workflow_active_workflow](workflow.md#BKMK_workflow_active_workflow) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: activeworkflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_active_workflow<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_workflowid_convertrule"></a> workflowid_convertrule

Same as convertrule entity [workflowid_convertrule](convertrule.md#BKMK_workflowid_convertrule) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflowid_convertrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_convertruleitembase_workflowid"></a> convertruleitembase_workflowid

Same as convertruleitem entity [convertruleitembase_workflowid](convertruleitem.md#BKMK_convertruleitembase_workflowid) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: workflowid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: convertruleitembase_workflowid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

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
workflow

