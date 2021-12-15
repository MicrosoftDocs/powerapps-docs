---
title: "SLAKPIInstance table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the SLAKPIInstance table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# SLAKPIInstance table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Service level agreement (SLA) key performance indicator (KPI) instance that is tracked for an individual case


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Assign|PATCH [*org URI*]/api/data/v9.0/slakpiinstances(*slakpiinstanceid*)<br />[Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update) `ownerid` property.|<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
|Create|POST [*org URI*]/api/data/v9.0/slakpiinstances<br />See [Create](/powerapps/developer/common-data-service/webapi/create-entity-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*>|
|Delete|DELETE [*org URI*]/api/data/v9.0/slakpiinstances(*slakpiinstanceid*)<br />See [Delete](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-delete)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*>|
|GrantAccess|<xref href="Microsoft.Dynamics.CRM.GrantAccess?text=GrantAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
|ModifyAccess|<xref href="Microsoft.Dynamics.CRM.ModifyAccess?text=ModifyAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
|Retrieve|GET [*org URI*]/api/data/v9.0/slakpiinstances(*slakpiinstanceid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/slakpiinstances<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|
|RetrievePrincipalAccess|<xref href="Microsoft.Dynamics.CRM.RetrievePrincipalAccess?text=RetrievePrincipalAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
|RetrieveSharedPrincipalsAndAccess|<xref href="Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function" />|<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
|RevokeAccess|<xref href="Microsoft.Dynamics.CRM.RevokeAccess?text=RevokeAccess Action" />|<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
|Update|PATCH [*org URI*]/api/data/v9.0/slakpiinstances(*slakpiinstanceid*)<br />See [Update](/powerapps/developer/common-data-service/webapi/update-delete-entities-using-web-api#basic-update)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|SLAKPIInstances|
|DisplayCollectionName|SLA KPI Instances|
|DisplayName|SLA KPI Instance|
|EntitySetName|slakpiinstances|
|IsBPFEntity|False|
|LogicalCollectionName|slakpiinstances|
|LogicalName|slakpiinstance|
|OwnershipType|UserOwned|
|PrimaryIdAttribute|slakpiinstanceid|
|PrimaryNameAttribute|name|
|SchemaName|SLAKPIInstance|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ApplicableFromValue](#BKMK_ApplicableFromValue)
- [ComputedFailureTime](#BKMK_ComputedFailureTime)
- [ComputedWarningTime](#BKMK_ComputedWarningTime)
- [Description](#BKMK_Description)
- [ElapsedTime](#BKMK_ElapsedTime)
- [FailureTime](#BKMK_FailureTime)
- [LastResumeTime](#BKMK_LastResumeTime)
- [msdyn_ActionExecutionStatus](#BKMK_msdyn_ActionExecutionStatus)
- [msdyn_calendarid](#BKMK_msdyn_calendarid)
- [msdyn_prevslakpiinstanceid](#BKMK_msdyn_prevslakpiinstanceid)
- [msdyn_slaitemid](#BKMK_msdyn_slaitemid)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PausedOn](#BKMK_PausedOn)
- [Regarding](#BKMK_Regarding)
- [RegardingEntityID](#BKMK_RegardingEntityID)
- [RegardingObjectTypeCode](#BKMK_RegardingObjectTypeCode)
- [SLAKPIInstanceId](#BKMK_SLAKPIInstanceId)
- [Status](#BKMK_Status)
- [SucceededOn](#BKMK_SucceededOn)
- [SuccessCheckedAt](#BKMK_SuccessCheckedAt)
- [TerminalStateReached](#BKMK_TerminalStateReached)
- [TerminalStateTime](#BKMK_TerminalStateTime)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [WarningTime](#BKMK_WarningTime)
- [WarningTimeReached](#BKMK_WarningTimeReached)


### <a name="BKMK_ApplicableFromValue"></a> ApplicableFromValue

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Applicable From Value|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|applicablefromvalue|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ComputedFailureTime"></a> ComputedFailureTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Computed Failure Date and time|
|DisplayName|Computed Failure Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedfailuretime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_ComputedWarningTime"></a> ComputedWarningTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Computed Warning Date and time|
|DisplayName|Computed Warning Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|computedwarningtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Description"></a> Description

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Description|
|FormatName|TextArea|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|description|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ElapsedTime"></a> ElapsedTime

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Elapsed Time|
|Format|None|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|elapsedtime|
|MaxValue|2147483647|
|MinValue|-2147483648|
|RequiredLevel|None|
|Type|Integer|


### <a name="BKMK_FailureTime"></a> FailureTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the date and time when the service level agreement (SLA) key performance indicator (KPI) will expire.|
|DisplayName|Failure Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|failuretime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_LastResumeTime"></a> LastResumeTime

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Last Resume Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|lastresumetime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_msdyn_ActionExecutionStatus"></a> msdyn_ActionExecutionStatus

**Added by**: Service Level Agreement (SLA) Extension Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Action Execution Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_actionexecutionstatus|
|RequiredLevel|None|
|Type|Picklist|

#### msdyn_ActionExecutionStatus Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|None||
|1|Warning||
|2|Success||



### <a name="BKMK_msdyn_calendarid"></a> msdyn_calendarid

**Added by**: Service Level Agreement (SLA) Extension Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Applicable Calendar|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_calendarid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_prevslakpiinstanceid"></a> msdyn_prevslakpiinstanceid

**Added by**: Service Level Agreement (SLA) Extension Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Previous SLAKPI Instance|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_prevslakpiinstanceid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_msdyn_slaitemid"></a> msdyn_slaitemid

**Added by**: Service Level Agreement (SLA) Extension Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier for SLA KPI Instance associated with SLA Item.|
|DisplayName|SLAItem|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|msdyn_slaitemid|
|RequiredLevel|None|
|Targets|slaitem|
|Type|Lookup|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Type a descriptive name for the service level agreement (SLA) key performance indicator (KPI) instance.|
|DisplayName|Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|name|
|MaxLength|100|
|RequiredLevel|SystemRequired|
|Type|String|


### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|--------|-----|
|Description|Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user or team.|
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


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|--------|-----|
|Description|Owning Business Unit.|
|DisplayName|Owning Business Unit|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningbusinessunit|
|RequiredLevel|None|
|Targets|businessunit|
|Type|Lookup|


### <a name="BKMK_OwningTeam"></a> OwningTeam

|Property|Value|
|--------|-----|
|Description|OwningTeam.|
|DisplayName|Owning Team|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owningteam|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|--------|-----|
|Description|Owning User.|
|DisplayName|Owning User|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|owninguser|
|RequiredLevel|None|
|Targets||
|Type|Lookup|


### <a name="BKMK_PausedOn"></a> PausedOn

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Paused On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|pausedon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_Regarding"></a> Regarding

|Property|Value|
|--------|-----|
|Description|Unique identifier of the record that this service level agreement (SLA) key performance indicator (KPI) instance is associated with.|
|DisplayName|Regarding|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|regarding|
|RequiredLevel|None|
|Targets|account,activitypointer,appointment,contact,email,fax,letter,phonecall,socialactivity,task|
|Type|Lookup|


### <a name="BKMK_RegardingEntityID"></a> RegardingEntityID

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Regarding ID|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|regardingentityid|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|--------|-----|
|Description|RegardingObjectTypeCode|
|DisplayName|RegardingObjectTypeCode|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingobjecttypecode|
|RequiredLevel|None|
|Type|EntityName|


### <a name="BKMK_SLAKPIInstanceId"></a> SLAKPIInstanceId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the SLA KPI Instance.|
|DisplayName|SLA KPI InstanceId|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|slakpiinstanceid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_Status"></a> Status

|Property|Value|
|--------|-----|
|Description|Reason for the status of the service level agreement (SLA) key performance indicator (KPI) instance. For example, the SLA KPI could be Noncompliant or Succeeded.|
|DisplayName|Status|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|status|
|RequiredLevel|None|
|Type|Picklist|

#### Status Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|In Progress||
|1|Noncompliant||
|2|Nearing Noncompliance||
|3|Paused||
|4|Succeeded||
|5|Canceled||



### <a name="BKMK_SucceededOn"></a> SucceededOn

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Shows the date and time when the service level agreement (SLA) key performance indicator (KPI) success criteria was met.|
|DisplayName|Succeeded On|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|succeededon|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_SuccessCheckedAt"></a> SuccessCheckedAt

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|TimeZoneIndependent|
|Description||
|DisplayName|SuccessCheckedAt|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|successcheckedat|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_TerminalStateReached"></a> TerminalStateReached

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName|Terminal State Reached|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|terminalstatereached|
|RequiredLevel|None|
|Type|Boolean|

#### TerminalStateReached Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Yes|
|0|No|

**DefaultValue**: False



### <a name="BKMK_TerminalStateTime"></a> TerminalStateTime

**Added by**: Service Level Agreement (SLA) Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description||
|DisplayName|Terminal State Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|terminalstatetime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|--------|-----|
|Description|Choose the local currency for the record to make sure budgets are reported in the correct currency.|
|DisplayName|Currency|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|transactioncurrencyid|
|RequiredLevel|None|
|Targets|transactioncurrency|
|Type|Lookup|


### <a name="BKMK_WarningTime"></a> WarningTime

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|Enter the date and time when the service level agreement (SLA) key performance indicator (KPI)will go to a warning state.|
|DisplayName|Warning Time|
|Format|DateAndTime|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|warningtime|
|RequiredLevel|None|
|Type|DateTime|


### <a name="BKMK_WarningTimeReached"></a> WarningTimeReached

|Property|Value|
|--------|-----|
|Description|Shows information about whether the case has reached its warning time.|
|DisplayName|Warning Time Reached|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|warningtimereached|
|RequiredLevel|None|
|Type|Picklist|

#### WarningTimeReached Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|No||
|1|Yes||


<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [msdyn_slaitemidName](#BKMK_msdyn_slaitemidName)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [RegardingIdName](#BKMK_RegardingIdName)
- [RegardingYomiName](#BKMK_RegardingYomiName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|--------|-----|
|Description|For internal use only.|
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
|Description|For internal use only.|
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
|Description|For internal use only.|
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


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Exchange Rate|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|exchangerate|
|MaxValue|100000000000|
|MinValue|0.000000000001|
|Precision|12|
|RequiredLevel|None|
|Type|Decimal|


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|--------|-----|
|Description|For internal use only.|
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
|Description|For internal use only.|
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
|Description|For internal use only.|
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


### <a name="BKMK_msdyn_slaitemidName"></a> msdyn_slaitemidName

**Added by**: Service Level Agreement (SLA) Extension Solution

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|msdyn_slaitemidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


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


### <a name="BKMK_RegardingIdName"></a> RegardingIdName

|Property|Value|
|--------|-----|
|Description|RegardingName|
|DisplayName|RegardingName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingidname|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RegardingYomiName"></a> RegardingYomiName

|Property|Value|
|--------|-----|
|Description|RegardingYomiName|
|DisplayName|RegardingYomiName|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|regardingyominame|
|MaxLength|800|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|transactioncurrencyidname|
|MaxLength|100|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|--------|-----|
|Description|For internal use only.|
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


### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

Same as syncerror table [SLAKPIInstance_SyncErrors](syncerror.md#BKMK_SLAKPIInstance_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|SLAKPIInstance_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: Cascade<br />Delete: Cascade<br />Merge: Cascade<br />Reparent: Cascade<br />Share: Cascade<br />Unshare: Cascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [slakpiinstance_activitypointer](#BKMK_slakpiinstance_activitypointer)
- [slakpiinstance_email](#BKMK_slakpiinstance_email)
- [slakpiinstance_fax](#BKMK_slakpiinstance_fax)
- [lk_slakpiinstancebase_createdonbehalfby](#BKMK_lk_slakpiinstancebase_createdonbehalfby)
- [lk_slakpiinstancebase_modifiedonbehalfby](#BKMK_lk_slakpiinstancebase_modifiedonbehalfby)
- [slakpiinstance_account](#BKMK_slakpiinstance_account)
- [slakpiinstance_letter](#BKMK_slakpiinstance_letter)
- [slakpiinstance_phonecall](#BKMK_slakpiinstance_phonecall)
- [business_unit_slakpiinstance](#BKMK_business_unit_slakpiinstance)
- [slakpiinstance_socialactivity](#BKMK_slakpiinstance_socialactivity)
- [slakpiinstance_task](#BKMK_slakpiinstance_task)
- [lk_slakpiinstancebase_modifiedby](#BKMK_lk_slakpiinstancebase_modifiedby)
- [TransactionCurrency_slakpiinstance](#BKMK_TransactionCurrency_slakpiinstance)
- [slakpiinstance_contact](#BKMK_slakpiinstance_contact)
- [lk_slakpiinstancebase_createdby](#BKMK_lk_slakpiinstancebase_createdby)
- [slakpiinstance_appointment](#BKMK_slakpiinstance_appointment)
- [msdyn_slaitem_slakpiinstance](#BKMK_msdyn_slaitem_slakpiinstance)


### <a name="BKMK_slakpiinstance_activitypointer"></a> slakpiinstance_activitypointer

See activitypointer Table [slakpiinstance_activitypointer](activitypointer.md#BKMK_slakpiinstance_activitypointer) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_email"></a> slakpiinstance_email

See email Table [slakpiinstance_email](email.md#BKMK_slakpiinstance_email) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_fax"></a> slakpiinstance_fax

See fax Table [slakpiinstance_fax](fax.md#BKMK_slakpiinstance_fax) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_createdonbehalfby"></a> lk_slakpiinstancebase_createdonbehalfby

See systemuser Table [lk_slakpiinstancebase_createdonbehalfby](systemuser.md#BKMK_lk_slakpiinstancebase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_modifiedonbehalfby"></a> lk_slakpiinstancebase_modifiedonbehalfby

See systemuser Table [lk_slakpiinstancebase_modifiedonbehalfby](systemuser.md#BKMK_lk_slakpiinstancebase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_account"></a> slakpiinstance_account

See account Table [slakpiinstance_account](account.md#BKMK_slakpiinstance_account) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_letter"></a> slakpiinstance_letter

See letter Table [slakpiinstance_letter](letter.md#BKMK_slakpiinstance_letter) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_phonecall"></a> slakpiinstance_phonecall

See phonecall Table [slakpiinstance_phonecall](phonecall.md#BKMK_slakpiinstance_phonecall) One-To-Many relationship.

### <a name="BKMK_business_unit_slakpiinstance"></a> business_unit_slakpiinstance

See businessunit Table [business_unit_slakpiinstance](businessunit.md#BKMK_business_unit_slakpiinstance) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_socialactivity"></a> slakpiinstance_socialactivity

See socialactivity Table [slakpiinstance_socialactivity](socialactivity.md#BKMK_slakpiinstance_socialactivity) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_task"></a> slakpiinstance_task

See task Table [slakpiinstance_task](task.md#BKMK_slakpiinstance_task) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_modifiedby"></a> lk_slakpiinstancebase_modifiedby

See systemuser Table [lk_slakpiinstancebase_modifiedby](systemuser.md#BKMK_lk_slakpiinstancebase_modifiedby) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_slakpiinstance"></a> TransactionCurrency_slakpiinstance

See transactioncurrency Table [TransactionCurrency_slakpiinstance](transactioncurrency.md#BKMK_TransactionCurrency_slakpiinstance) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_contact"></a> slakpiinstance_contact

See contact Table [slakpiinstance_contact](contact.md#BKMK_slakpiinstance_contact) One-To-Many relationship.

### <a name="BKMK_lk_slakpiinstancebase_createdby"></a> lk_slakpiinstancebase_createdby

See systemuser Table [lk_slakpiinstancebase_createdby](systemuser.md#BKMK_lk_slakpiinstancebase_createdby) One-To-Many relationship.

### <a name="BKMK_slakpiinstance_appointment"></a> slakpiinstance_appointment

See appointment Table [slakpiinstance_appointment](appointment.md#BKMK_slakpiinstance_appointment) One-To-Many relationship.

### <a name="BKMK_msdyn_slaitem_slakpiinstance"></a> msdyn_slaitem_slakpiinstance

See slaitem Table [msdyn_slaitem_slakpiinstance](slaitem.md#BKMK_msdyn_slaitem_slakpiinstance) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.slakpiinstance?text=slakpiinstance EntityType" />