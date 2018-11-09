---
title: "ConvertRule Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ConvertRule entity."
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
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# ConvertRule Entity Reference

Defines the settings for automatic record creation.

## Entity Properties

**DisplayName**: Record Creation and Update Rule<br />
**DisplayCollectionName**: Record Creation and Update Rules<br />
**SchemaName**: ConvertRule<br />
**CollectionSchemaName**: ConvertRules<br />
**LogicalName**: convertrule<br />
**LogicalCollectionName**: convertrules<br />
**EntitySetName**: convertrules<br />
**PrimaryIdAttribute**: convertruleid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllowUnknownSender](#BKMK_AllowUnknownSender)
- [ChannelPropertyGroupId](#BKMK_ChannelPropertyGroupId)
- [ChannelPropertyGroupIdName](#BKMK_ChannelPropertyGroupIdName)
- [CheckActiveEntitlement](#BKMK_CheckActiveEntitlement)
- [CheckBlockedSocialProfile](#BKMK_CheckBlockedSocialProfile)
- [CheckDirectMessages](#BKMK_CheckDirectMessages)
- [CheckIfResolved](#BKMK_CheckIfResolved)
- [ConvertRuleId](#BKMK_ConvertRuleId)
- [Description](#BKMK_Description)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [QueueId](#BKMK_QueueId)
- [ResolvedSince](#BKMK_ResolvedSince)
- [ResponseTemplateId](#BKMK_ResponseTemplateId)
- [SendAutomaticResponse](#BKMK_SendAutomaticResponse)
- [SourceChannelTypeCode](#BKMK_SourceChannelTypeCode)
- [SourceTypeCode](#BKMK_SourceTypeCode)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [WorkflowId](#BKMK_WorkflowId)


### <a name="BKMK_AllowUnknownSender"></a> AllowUnknownSender

**Description**: Choose whether items from unknown senders should be converted to records.<br />
**DisplayName**: Allow Unknown Sender<br />
**LogicalName**: allowunknownsender<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ChannelPropertyGroupId"></a> ChannelPropertyGroupId

**Description**: channel property group associated with the convert rule.<br />
**DisplayName**: Channel Property Group<br />
**LogicalName**: channelpropertygroupid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: channelpropertygroup


### <a name="BKMK_ChannelPropertyGroupIdName"></a> ChannelPropertyGroupIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: channelpropertygroupidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_CheckActiveEntitlement"></a> CheckActiveEntitlement

**Description**: Choose whether cases should be created for customers with active entitlements.<br />
**DisplayName**: Check Active SLA<br />
**LogicalName**: checkactiveentitlement<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CheckBlockedSocialProfile"></a> CheckBlockedSocialProfile

**Description**: Information whether record needs to be created for black listed social profiles.<br />
**DisplayName**: Check black listed social profiles<br />
**LogicalName**: checkblockedsocialprofile<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CheckDirectMessages"></a> CheckDirectMessages

**Description**: Information whether record needs to be created for direct messages.<br />
**DisplayName**: Create records for private messages only<br />
**LogicalName**: checkdirectmessages<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_CheckIfResolved"></a> CheckIfResolved

**Description**: Choose whether an item related to a resolved case should be converted to a case.<br />
**DisplayName**: Check If Resolved<br />
**LogicalName**: checkifresolved<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ConvertRuleId"></a> ConvertRuleId

**Description**: Unique identifier for entity instances<br />
**DisplayName**: Convert Rule<br />
**LogicalName**: convertruleid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Description"></a> Description

**Description**: Type additional information to describe the rule for creating records automatically.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_Name"></a> Name

**Description**: Type a title or name of the queue for which the setting is defined.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Owner Id<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Owner name of the routing rule.<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier for the team that owns the record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier for the user that owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_QueueId"></a> QueueId

**Description**: Choose the queue that the rule is assigned to.<br />
**DisplayName**: Queue<br />
**LogicalName**: queueid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: queue


### <a name="BKMK_ResolvedSince"></a> ResolvedSince

**Description**: If you want to create a new case for an item associated with a resolved case, type how long a case must remain resolved before a new case is created for the associated item.<br />
**DisplayName**: Resolved Since<br />
**LogicalName**: resolvedsince<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: Duration<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_ResponseTemplateId"></a> ResponseTemplateId

**Description**: Choose the email template to use to create an automatic response to the customer.<br />
**DisplayName**: Response Email Template<br />
**LogicalName**: responsetemplateid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: template


### <a name="BKMK_SendAutomaticResponse"></a> SendAutomaticResponse

**Description**: Choose whether to send an automatic email response to the customer after a record is created.<br />
**DisplayName**: Send Automatic Response<br />
**LogicalName**: sendautomaticresponse<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SourceChannelTypeCode"></a> SourceChannelTypeCode

**Description**: Identifies the Dynamics 365 activity that's the source of the record.<br />
**DisplayName**: Source Type<br />
**LogicalName**: sourcechanneltypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_SourceTypeCode"></a> SourceTypeCode

**Description**: Source of the record.<br />
**DisplayName**: Source Type<br />
**LogicalName**: sourcetypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Social Monitoring
- **Value**: 2 **Label**: Email



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Status of the Convert Rule<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Draft **DefaultStatus**: 1 **InvariantName**: Draft
- **Value**: 1 **Label**: Active **DefaultStatus**: 2 **InvariantName**: Active



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Reason for the status of the Convert Rule<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Draft **State**: 0
- **Value**: 2 **Label**: Active **State**: 1



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the queue.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_WorkflowId"></a> WorkflowId

**Description**: Shows the workflow for this rule.<br />
**DisplayName**: Workflow<br />
**LogicalName**: workflowid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: workflow

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [ConvertRuleIdUnique](#BKMK_ConvertRuleIdUnique)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [QueueIdName](#BKMK_QueueIdName)
- [RecordVersion](#BKMK_RecordVersion)
- [ResponseTemplateIdName](#BKMK_ResponseTemplateIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkflowIdName](#BKMK_WorkflowIdName)


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



### <a name="BKMK_ConvertRuleIdUnique"></a> ConvertRuleIdUnique

**Description**: For internal use only.<br />
**DisplayName**: Unique Id<br />
**LogicalName**: convertruleidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Date and time when the record was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the queue with respect to the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: For internal use only.<br />
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

**Description**: Unique identifier of the user who modified the record.<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Date and time when the record was modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the record.<br />
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
**RequiredLevel**: SystemRequired<br />
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


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Shows the business unit that the convert rule owner belongs to.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_QueueIdName"></a> QueueIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: queueidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_RecordVersion"></a> RecordVersion

**Description**: Record Version<br />
**DisplayName**: Record Version<br />
**LogicalName**: recordversion<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_ResponseTemplateIdName"></a> ResponseTemplateIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: responsetemplateidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the convert rule.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_WorkflowIdName"></a> WorkflowIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: workflowidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [ConvertRule_ProcessSessions](#BKMK_ConvertRule_ProcessSessions)
- [ConvertRule_userentityinstancedatas](#BKMK_ConvertRule_userentityinstancedatas)
- [convertrule_convertruleitem](#BKMK_convertrule_convertruleitem)
- [ConvertRule_Annotation](#BKMK_ConvertRule_Annotation)
- [Convertrule_AsyncOperations](#BKMK_Convertrule_AsyncOperations)


### <a name="BKMK_ConvertRule_ProcessSessions"></a> ConvertRule_ProcessSessions

Same as processsession entity [ConvertRule_ProcessSessions](processsession.md#BKMK_ConvertRule_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ConvertRule_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ConvertRule_userentityinstancedatas"></a> ConvertRule_userentityinstancedatas

Same as userentityinstancedata entity [ConvertRule_userentityinstancedatas](userentityinstancedata.md#BKMK_ConvertRule_userentityinstancedatas) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ConvertRule_userentityinstancedatas<br />
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


### <a name="BKMK_convertrule_convertruleitem"></a> convertrule_convertruleitem

Same as convertruleitem entity [convertrule_convertruleitem](convertruleitem.md#BKMK_convertrule_convertruleitem) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: convertruleid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: convertrule_convertruleitem<br />
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


### <a name="BKMK_ConvertRule_Annotation"></a> ConvertRule_Annotation

Same as annotation entity [ConvertRule_Annotation](annotation.md#BKMK_ConvertRule_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ConvertRule_Annotation<br />
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


### <a name="BKMK_Convertrule_AsyncOperations"></a> Convertrule_AsyncOperations

Same as asyncoperation entity [Convertrule_AsyncOperations](asyncoperation.md#BKMK_Convertrule_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Convertrule_AsyncOperations<br />
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

- [emailtemplate_convertrule](#BKMK_emailtemplate_convertrule)
- [convertrule_queue](#BKMK_convertrule_queue)
- [lk_ConvertRule_modifiedonbehalfby](#BKMK_lk_ConvertRule_modifiedonbehalfby)
- [user_convertrule](#BKMK_user_convertrule)
- [team_convertrule](#BKMK_team_convertrule)
- [business_unit_convertrule](#BKMK_business_unit_convertrule)
- [lk_ConvertRule_createdonbehalfby](#BKMK_lk_ConvertRule_createdonbehalfby)
- [TransactionCurrency_ConvertRule](#BKMK_TransactionCurrency_ConvertRule)
- [lk_convertrule_createdby](#BKMK_lk_convertrule_createdby)
- [lk_ConvertRule_modifiedby](#BKMK_lk_ConvertRule_modifiedby)
- [workflowid_convertrule](#BKMK_workflowid_convertrule)
- [channelpropertygroup_convertrule](#BKMK_channelpropertygroup_convertrule)


### <a name="BKMK_emailtemplate_convertrule"></a> emailtemplate_convertrule

See template Entity [emailtemplate_convertrule](template.md#BKMK_emailtemplate_convertrule) One-To-Many relationship.

### <a name="BKMK_convertrule_queue"></a> convertrule_queue

See queue Entity [convertrule_queue](queue.md#BKMK_convertrule_queue) One-To-Many relationship.

### <a name="BKMK_lk_ConvertRule_modifiedonbehalfby"></a> lk_ConvertRule_modifiedonbehalfby

See systemuser Entity [lk_ConvertRule_modifiedonbehalfby](systemuser.md#BKMK_lk_ConvertRule_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_user_convertrule"></a> user_convertrule

See systemuser Entity [user_convertrule](systemuser.md#BKMK_user_convertrule) One-To-Many relationship.

### <a name="BKMK_team_convertrule"></a> team_convertrule

See team Entity [team_convertrule](team.md#BKMK_team_convertrule) One-To-Many relationship.

### <a name="BKMK_business_unit_convertrule"></a> business_unit_convertrule

See businessunit Entity [business_unit_convertrule](businessunit.md#BKMK_business_unit_convertrule) One-To-Many relationship.

### <a name="BKMK_lk_ConvertRule_createdonbehalfby"></a> lk_ConvertRule_createdonbehalfby

See systemuser Entity [lk_ConvertRule_createdonbehalfby](systemuser.md#BKMK_lk_ConvertRule_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_ConvertRule"></a> TransactionCurrency_ConvertRule

See transactioncurrency Entity [TransactionCurrency_ConvertRule](transactioncurrency.md#BKMK_TransactionCurrency_ConvertRule) One-To-Many relationship.

### <a name="BKMK_lk_convertrule_createdby"></a> lk_convertrule_createdby

See systemuser Entity [lk_convertrule_createdby](systemuser.md#BKMK_lk_convertrule_createdby) One-To-Many relationship.

### <a name="BKMK_lk_ConvertRule_modifiedby"></a> lk_ConvertRule_modifiedby

See systemuser Entity [lk_ConvertRule_modifiedby](systemuser.md#BKMK_lk_ConvertRule_modifiedby) One-To-Many relationship.

### <a name="BKMK_workflowid_convertrule"></a> workflowid_convertrule

See workflow Entity [workflowid_convertrule](workflow.md#BKMK_workflowid_convertrule) One-To-Many relationship.

### <a name="BKMK_channelpropertygroup_convertrule"></a> channelpropertygroup_convertrule

See channelpropertygroup Entity [channelpropertygroup_convertrule](channelpropertygroup.md#BKMK_channelpropertygroup_convertrule) One-To-Many relationship.
convertrule

