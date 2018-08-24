---
title: "SdkMessageProcessingStep Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SdkMessageProcessingStep entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SdkMessageProcessingStep Entity Reference

Stage in the execution pipeline that a plug-in is to execute.

## Entity Properties

**DisplayName**: Sdk Message Processing Step<br />
**DisplayCollectionName**: Sdk Message Processing Steps<br />
**SchemaName**: SdkMessageProcessingStep<br />
**CollectionSchemaName**: SdkMessageProcessingSteps<br />
**LogicalName**: sdkmessageprocessingstep<br />
**LogicalCollectionName**: sdkmessageprocessingsteps<br />
**EntitySetName**: sdkmessageprocessingsteps<br />
**PrimaryIdAttribute**: sdkmessageprocessingstepid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AsyncAutoDelete](#BKMK_AsyncAutoDelete)
- [CanUseReadOnlyConnection](#BKMK_CanUseReadOnlyConnection)
- [Configuration](#BKMK_Configuration)
- [Description](#BKMK_Description)
- [EventExpander](#BKMK_EventExpander)
- [EventHandler](#BKMK_EventHandler)
- [EventHandlerTypeCode](#BKMK_EventHandlerTypeCode)
- [FilteringAttributes](#BKMK_FilteringAttributes)
- [ImpersonatingUserId](#BKMK_ImpersonatingUserId)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [InvocationSource](#BKMK_InvocationSource)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsHidden](#BKMK_IsHidden)
- [Mode](#BKMK_Mode)
- [Name](#BKMK_Name)
- [PluginTypeId](#BKMK_PluginTypeId)
- [Rank](#BKMK_Rank)
- [SdkMessageFilterId](#BKMK_SdkMessageFilterId)
- [SdkMessageId](#BKMK_SdkMessageId)
- [SdkMessageProcessingStepId](#BKMK_SdkMessageProcessingStepId)
- [SdkMessageProcessingStepSecureConfigId](#BKMK_SdkMessageProcessingStepSecureConfigId)
- [Stage](#BKMK_Stage)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [SupportedDeployment](#BKMK_SupportedDeployment)


### <a name="BKMK_AsyncAutoDelete"></a> AsyncAutoDelete

**Description**: Indicates whether the asynchronous system job is automatically deleted on completion.<br />
**DisplayName**: Asynchronous Automatic Delete<br />
**LogicalName**: asyncautodelete<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CanUseReadOnlyConnection"></a> CanUseReadOnlyConnection

**Description**: Identifies whether a SDK Message Processing Step type will be ReadOnly or Read Write. false - ReadWrite, true - ReadOnly <br />
**DisplayName**: Intent<br />
**LogicalName**: canusereadonlyconnection<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Configuration"></a> Configuration

**Description**: Step-specific configuration for the plug-in type. Passed to the plug-in constructor at run time.<br />
**DisplayName**: Configuration<br />
**LogicalName**: configuration<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Description"></a> Description

**Description**: Description of the SDK message processing step.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_EventExpander"></a> EventExpander

**Description**: Configuration for sending pipeline events to the Event Expander service.<br />
**DisplayName**: EventExpander<br />
**LogicalName**: eventexpander<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_EventHandler"></a> EventHandler

**Description**: Unique identifier of the associated event handler.<br />
**DisplayName**: Event Handler<br />
**LogicalName**: eventhandler<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: plugintype,serviceendpoint


### <a name="BKMK_EventHandlerTypeCode"></a> EventHandlerTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: eventhandlertypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_FilteringAttributes"></a> FilteringAttributes

**Description**: Comma-separated list of attributes. If at least one of these attributes is modified, the plug-in should execute.<br />
**DisplayName**: Filtering Attributes<br />
**LogicalName**: filteringattributes<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100000


### <a name="BKMK_ImpersonatingUserId"></a> ImpersonatingUserId

**Description**: Unique identifier of the user to impersonate context when step is executed.<br />
**DisplayName**: Impersonating User<br />
**LogicalName**: impersonatinguserid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


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


### <a name="BKMK_InvocationSource"></a> InvocationSource

**Description**: Identifies if a plug-in should be executed from a parent pipeline, a child pipeline, or both.<br />
**DisplayName**: Invocation Source<br />
**LogicalName**: invocationsource<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: -1 **Label**: Internal
- **Value**: 0 **Label**: Parent
- **Value**: 1 **Label**: Child



### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Description**: Information that specifies whether this component can be customized.<br />
**DisplayName**: Customizable<br />
**LogicalName**: iscustomizable<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_IsHidden"></a> IsHidden

**Description**: Information that specifies whether this component should be hidden.<br />
**DisplayName**: Hidden<br />
**LogicalName**: ishidden<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: ManagedProperty<br />


### <a name="BKMK_Mode"></a> Mode

**Description**: Run-time mode of execution, for example, synchronous or asynchronous.<br />
**DisplayName**: Execution Mode<br />
**LogicalName**: mode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Synchronous
- **Value**: 1 **Label**: Asynchronous



### <a name="BKMK_Name"></a> Name

**Description**: Name of SdkMessage processing step.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_PluginTypeId"></a> PluginTypeId

**Description**: Unique identifier of the plug-in type associated with the step.<br />
**DisplayName**: Plug-In Type<br />
**LogicalName**: plugintypeid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: sdkmessagefilter


### <a name="BKMK_Rank"></a> Rank

**Description**: Processing order within the stage.<br />
**DisplayName**: Execution Order<br />
**LogicalName**: rank<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_SdkMessageFilterId"></a> SdkMessageFilterId

**Description**: Unique identifier of the SDK message filter.<br />
**DisplayName**: SdkMessage Filter<br />
**LogicalName**: sdkmessagefilterid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: sdkmessagefilter


### <a name="BKMK_SdkMessageId"></a> SdkMessageId

**Description**: Unique identifier of the SDK message.<br />
**DisplayName**: SDK Message<br />
**LogicalName**: sdkmessageid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: sdkmessage


### <a name="BKMK_SdkMessageProcessingStepId"></a> SdkMessageProcessingStepId

**Description**: Unique identifier of the SDK message processing step entity.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageprocessingstepid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SdkMessageProcessingStepSecureConfigId"></a> SdkMessageProcessingStepSecureConfigId

**Description**: Unique identifier of the Sdk message processing step secure configuration.<br />
**DisplayName**: SDK Message Processing Step Secure Configuration<br />
**LogicalName**: sdkmessageprocessingstepsecureconfigid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: sdkmessageprocessingstepsecureconfig


### <a name="BKMK_Stage"></a> Stage

**Description**: Stage in the execution pipeline that the SDK message processing step is in.<br />
**DisplayName**: Execution Stage<br />
**LogicalName**: stage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 5 **Label**: Initial Pre-operation (For internal use only)
- **Value**: 10 **Label**: Pre-validation
- **Value**: 15 **Label**: Internal Pre-operation Before External Plugins (For internal use only)
- **Value**: 20 **Label**: Pre-operation
- **Value**: 25 **Label**: Internal Pre-operation After External Plugins (For internal use only)
- **Value**: 30 **Label**: Main Operation (For internal use only)
- **Value**: 35 **Label**: Internal Post-operation Before External Plugins (For internal use only)
- **Value**: 40 **Label**: Post-operation
- **Value**: 45 **Label**: Internal Post-operation After External Plugins (For internal use only)
- **Value**: 50 **Label**: Post-operation (Deprecated)
- **Value**: 55 **Label**: Final Post-operation (For internal use only)



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the SDK message processing step.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Enabled **DefaultStatus**: 1 **InvariantName**: Enabled
- **Value**: 1 **Label**: Disabled **DefaultStatus**: 2 **InvariantName**: Disabled



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the SDK message processing step.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Enabled **State**: 0
- **Value**: 2 **Label**: Disabled **State**: 1



### <a name="BKMK_SupportedDeployment"></a> SupportedDeployment

**Description**: Deployment that the SDK message processing step should be executed on; server, client, or both.<br />
**DisplayName**: Deployment<br />
**LogicalName**: supporteddeployment<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Server Only
- **Value**: 1 **Label**: Microsoft Dynamics 365 Client for Outlook Only
- **Value**: 2 **Label**: Both


<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [EventHandlerName](#BKMK_EventHandlerName)
- [ImpersonatingUserIdName](#BKMK_ImpersonatingUserIdName)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PluginTypeIdName](#BKMK_PluginTypeIdName)
- [SdkMessageIdName](#BKMK_SdkMessageIdName)
- [SdkMessageProcessingStepIdUnique](#BKMK_SdkMessageProcessingStepIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


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

**Description**: Unique identifier of the user who created the SDK message processing step.<br />
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


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the SDK message processing step was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the sdkmessageprocessingstep.<br />
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


### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

**Description**: Customization level of the SDK message processing step.<br />
**DisplayName**: <br />
**LogicalName**: customizationlevel<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 255<br />
**MinValue**: -255


### <a name="BKMK_EventHandlerName"></a> EventHandlerName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: eventhandlername<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 256


### <a name="BKMK_ImpersonatingUserIdName"></a> ImpersonatingUserIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: impersonatinguseridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Information that specifies whether this component is managed.<br />
**DisplayName**: State<br />
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

**Description**: Unique identifier of the user who last modified the SDK message processing step.<br />
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


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the SDK message processing step was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the sdkmessageprocessingstep.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization with which the SDK message processing step is associated.<br />
**DisplayName**: <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


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


### <a name="BKMK_PluginTypeIdName"></a> PluginTypeIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: plugintypeidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SdkMessageIdName"></a> SdkMessageIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: sdkmessageidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_SdkMessageProcessingStepIdUnique"></a> SdkMessageProcessingStepIdUnique

**Description**: Unique identifier of the SDK message processing step.<br />
**DisplayName**: <br />
**LogicalName**: sdkmessageprocessingstepidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Number that identifies a specific revision of the SDK message processing step. <br />
**DisplayName**: <br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [SdkMessageProcessingStep_AsyncOperations](#BKMK_SdkMessageProcessingStep_AsyncOperations)
- [sdkmessageprocessingstepid_sdkmessageprocessingstepimage](#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage)
- [userentityinstancedata_sdkmessageprocessingstep](#BKMK_userentityinstancedata_sdkmessageprocessingstep)


### <a name="BKMK_SdkMessageProcessingStep_AsyncOperations"></a> SdkMessageProcessingStep_AsyncOperations

Same as asyncoperation entity [SdkMessageProcessingStep_AsyncOperations](asyncoperation.md#BKMK_SdkMessageProcessingStep_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: owningextensionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SdkMessageProcessingStep_AsyncOperations<br />
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


### <a name="BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage"></a> sdkmessageprocessingstepid_sdkmessageprocessingstepimage

Same as sdkmessageprocessingstepimage entity [sdkmessageprocessingstepid_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_sdkmessageprocessingstepid_sdkmessageprocessingstepimage) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepimage<br />
**ReferencingAttribute**: sdkmessageprocessingstepid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: sdkmessageprocessingstepid_sdkmessageprocessingstepimage<br />
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


### <a name="BKMK_userentityinstancedata_sdkmessageprocessingstep"></a> userentityinstancedata_sdkmessageprocessingstep

Same as userentityinstancedata entity [userentityinstancedata_sdkmessageprocessingstep](userentityinstancedata.md#BKMK_userentityinstancedata_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_sdkmessageprocessingstep<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [plugintype_sdkmessageprocessingstep](#BKMK_plugintype_sdkmessageprocessingstep)
- [sdkmessagefilterid_sdkmessageprocessingstep](#BKMK_sdkmessagefilterid_sdkmessageprocessingstep)
- [serviceendpoint_sdkmessageprocessingstep](#BKMK_serviceendpoint_sdkmessageprocessingstep)
- [lk_sdkmessageprocessingstep_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby)
- [organization_sdkmessageprocessingstep](#BKMK_organization_sdkmessageprocessingstep)
- [impersonatinguserid_sdkmessageprocessingstep](#BKMK_impersonatinguserid_sdkmessageprocessingstep)
- [lk_sdkmessageprocessingstep_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby)
- [modifiedby_sdkmessageprocessingstep](#BKMK_modifiedby_sdkmessageprocessingstep)
- [sdkmessageid_sdkmessageprocessingstep](#BKMK_sdkmessageid_sdkmessageprocessingstep)
- [sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep)
- [createdby_sdkmessageprocessingstep](#BKMK_createdby_sdkmessageprocessingstep)
- [plugintypeid_sdkmessageprocessingstep](#BKMK_plugintypeid_sdkmessageprocessingstep)


### <a name="BKMK_plugintype_sdkmessageprocessingstep"></a> plugintype_sdkmessageprocessingstep

See plugintype Entity [plugintype_sdkmessageprocessingstep](plugintype.md#BKMK_plugintype_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_sdkmessagefilterid_sdkmessageprocessingstep"></a> sdkmessagefilterid_sdkmessageprocessingstep

See sdkmessagefilter Entity [sdkmessagefilterid_sdkmessageprocessingstep](sdkmessagefilter.md#BKMK_sdkmessagefilterid_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_serviceendpoint_sdkmessageprocessingstep"></a> serviceendpoint_sdkmessageprocessingstep

See serviceendpoint Entity [serviceendpoint_sdkmessageprocessingstep](serviceendpoint.md#BKMK_serviceendpoint_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessageprocessingstep_createdonbehalfby"></a> lk_sdkmessageprocessingstep_createdonbehalfby

See systemuser Entity [lk_sdkmessageprocessingstep_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_organization_sdkmessageprocessingstep"></a> organization_sdkmessageprocessingstep

See organization Entity [organization_sdkmessageprocessingstep](organization.md#BKMK_organization_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_impersonatinguserid_sdkmessageprocessingstep"></a> impersonatinguserid_sdkmessageprocessingstep

See systemuser Entity [impersonatinguserid_sdkmessageprocessingstep](systemuser.md#BKMK_impersonatinguserid_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby"></a> lk_sdkmessageprocessingstep_modifiedonbehalfby

See systemuser Entity [lk_sdkmessageprocessingstep_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_modifiedby_sdkmessageprocessingstep"></a> modifiedby_sdkmessageprocessingstep

See systemuser Entity [modifiedby_sdkmessageprocessingstep](systemuser.md#BKMK_modifiedby_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_sdkmessageid_sdkmessageprocessingstep"></a> sdkmessageid_sdkmessageprocessingstep

See sdkmessage Entity [sdkmessageid_sdkmessageprocessingstep](sdkmessage.md#BKMK_sdkmessageid_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep"></a> sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep

See sdkmessageprocessingstepsecureconfig Entity [sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep](sdkmessageprocessingstepsecureconfig.md#BKMK_sdkmessageprocessingstepsecureconfigid_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_createdby_sdkmessageprocessingstep"></a> createdby_sdkmessageprocessingstep

See systemuser Entity [createdby_sdkmessageprocessingstep](systemuser.md#BKMK_createdby_sdkmessageprocessingstep) One-To-Many relationship.

### <a name="BKMK_plugintypeid_sdkmessageprocessingstep"></a> plugintypeid_sdkmessageprocessingstep

See plugintype Entity [plugintypeid_sdkmessageprocessingstep](plugintype.md#BKMK_plugintypeid_sdkmessageprocessingstep) One-To-Many relationship.
sdkmessageprocessingstep

