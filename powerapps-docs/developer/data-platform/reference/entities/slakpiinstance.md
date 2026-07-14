---
title: "SLA KPI Instance (SLAKPIInstance) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the SLA KPI Instance (SLAKPIInstance) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# SLA KPI Instance (SLAKPIInstance) table/entity reference (Microsoft Dataverse)

Service level agreement (SLA) key performance indicator (KPI) instance that is tracked for an individual case

## Messages

The following table lists the messages for the SLA KPI Instance (SLAKPIInstance) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /slakpiinstances(*slakpiinstanceid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /slakpiinstances<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /slakpiinstances(*slakpiinstanceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /slakpiinstances(*slakpiinstanceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /slakpiinstances<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `Update`<br />Event: True |`PATCH` /slakpiinstances(*slakpiinstanceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /slakpiinstances(*slakpiinstanceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the SLA KPI Instance (SLAKPIInstance) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SLA KPI Instance** |
| **DisplayCollectionName** | **SLA KPI Instances** |
| **SchemaName** | `SLAKPIInstance` |
| **CollectionSchemaName** | `SLAKPIInstances` |
| **EntitySetName** | `slakpiinstances`|
| **LogicalName** | `slakpiinstance` |
| **LogicalCollectionName** | `slakpiinstances` |
| **PrimaryIdAttribute** | `slakpiinstanceid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

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
- [msdyn_activeduration](#BKMK_msdyn_activeduration)
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

|Property|Value|
|---|---|
|Description||
|DisplayName|**Applicable From Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicablefromvalue`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ComputedFailureTime"></a> ComputedFailureTime

|Property|Value|
|---|---|
|Description|**Computed Failure Date and time**|
|DisplayName|**Computed Failure Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedfailuretime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_ComputedWarningTime"></a> ComputedWarningTime

|Property|Value|
|---|---|
|Description|**Computed Warning Date and time**|
|DisplayName|**Computed Warning Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`computedwarningtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ElapsedTime"></a> ElapsedTime

|Property|Value|
|---|---|
|Description|**Paused duration of a KPI in business hours**|
|DisplayName|**Elapsed Time (min)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`elapsedtime`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_FailureTime"></a> FailureTime

|Property|Value|
|---|---|
|Description|**Enter the date and time when the service level agreement (SLA) key performance indicator (KPI) will expire.**|
|DisplayName|**Failure Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`failuretime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_LastResumeTime"></a> LastResumeTime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Last Resume Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`lastresumetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_ActionExecutionStatus"></a> msdyn_ActionExecutionStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**Action Execution Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_actionexecutionstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_slakpiinstance_msdyn_actionexecutionstatus`|

#### msdyn_ActionExecutionStatus Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Warning**|
|2|**Success**|

### <a name="BKMK_msdyn_activeduration"></a> msdyn_activeduration

|Property|Value|
|---|---|
|Description|**Time taken in business hours by a KPI instance to reach the Success or failed state**|
|DisplayName|**Active Duration (min)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_activeduration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_calendarid"></a> msdyn_calendarid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Applicable Calendar**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_calendarid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_prevslakpiinstanceid"></a> msdyn_prevslakpiinstanceid

|Property|Value|
|---|---|
|Description||
|DisplayName|**Previous SLAKPI Instance**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_prevslakpiinstanceid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_slaitemid"></a> msdyn_slaitemid

|Property|Value|
|---|---|
|Description|**Unique identifier for SLA KPI Instance associated with SLA Item.**|
|DisplayName|**SLAItem**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_slaitemid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|slaitem|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a descriptive name for the service level agreement (SLA) key performance indicator (KPI) instance.**|
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
|MaxLength|100|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user or team.**|
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

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Owning Business Unit.**|
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
|Description|**OwningTeam.**|
|DisplayName|**Owning Team**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningteam`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Owning User.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_PausedOn"></a> PausedOn

|Property|Value|
|---|---|
|Description||
|DisplayName|**Paused On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`pausedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_Regarding"></a> Regarding

|Property|Value|
|---|---|
|Description|**Unique identifier of the record that this service level agreement (SLA) key performance indicator (KPI) instance is associated with.**|
|DisplayName|**Regarding**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regarding`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|account, activitypointer, appointment, contact, email, fax, letter, phonecall, socialactivity, task|

### <a name="BKMK_RegardingEntityID"></a> RegardingEntityID

|Property|Value|
|---|---|
|Description||
|DisplayName|**Regarding ID**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`regardingentityid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_RegardingObjectTypeCode"></a> RegardingObjectTypeCode

|Property|Value|
|---|---|
|Description|**RegardingObjectTypeCode**|
|DisplayName|**RegardingObjectTypeCode**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjecttypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_SLAKPIInstanceId"></a> SLAKPIInstanceId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SLA KPI Instance.**|
|DisplayName|**SLA KPI InstanceId**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slakpiinstanceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Status"></a> Status

|Property|Value|
|---|---|
|Description|**Reason for the status of the service level agreement (SLA) key performance indicator (KPI) instance. For example, the SLA KPI could be Noncompliant or Succeeded.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`status`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`slakpiinstance_status`|

#### Status Choices/Options

|Value|Label|
|---|---|
|0|**In Progress**|
|1|**Noncompliant**|
|2|**Nearing Noncompliance**|
|3|**Paused**|
|4|**Succeeded**|
|5|**Canceled**|

### <a name="BKMK_SucceededOn"></a> SucceededOn

|Property|Value|
|---|---|
|Description|**Shows the date and time when the service level agreement (SLA) key performance indicator (KPI) success criteria was met.**|
|DisplayName|**Succeeded On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`succeededon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_SuccessCheckedAt"></a> SuccessCheckedAt

|Property|Value|
|---|---|
|Description||
|DisplayName|**SuccessCheckedAt**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`successcheckedat`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_TerminalStateReached"></a> TerminalStateReached

|Property|Value|
|---|---|
|Description||
|DisplayName|**Terminal State Reached**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`terminalstatereached`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`servicelevelagreementinstance_terminalstatereached`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_TerminalStateTime"></a> TerminalStateTime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Terminal State Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`terminalstatetime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Choose the local currency for the record to make sure budgets are reported in the correct currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_WarningTime"></a> WarningTime

|Property|Value|
|---|---|
|Description|**Enter the date and time when the service level agreement (SLA) key performance indicator (KPI)will go to a warning state.**|
|DisplayName|**Warning Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`warningtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_WarningTimeReached"></a> WarningTimeReached

|Property|Value|
|---|---|
|Description|**Shows information about whether the case has reached its warning time.**|
|DisplayName|**Warning Time Reached**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`warningtimereached`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`slakpiinstance_warningtimereached`|

#### WarningTimeReached Choices/Options

|Value|Label|
|---|---|
|0|**No**|
|1|**Yes**|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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
|Description|**For internal use only.**|
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
|Description|**For internal use only.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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
|Description|**For internal use only.**|
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
|Description|**For internal use only.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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

- [business_unit_slakpiinstance](#BKMK_business_unit_slakpiinstance)
- [lk_slakpiinstancebase_createdby](#BKMK_lk_slakpiinstancebase_createdby)
- [lk_slakpiinstancebase_createdonbehalfby](#BKMK_lk_slakpiinstancebase_createdonbehalfby)
- [lk_slakpiinstancebase_modifiedby](#BKMK_lk_slakpiinstancebase_modifiedby)
- [lk_slakpiinstancebase_modifiedonbehalfby](#BKMK_lk_slakpiinstancebase_modifiedonbehalfby)
- [msdyn_slaitem_slakpiinstance](#BKMK_msdyn_slaitem_slakpiinstance)
- [slakpiinstance_account](#BKMK_slakpiinstance_account)
- [slakpiinstance_activitypointer](#BKMK_slakpiinstance_activitypointer)
- [slakpiinstance_appointment](#BKMK_slakpiinstance_appointment)
- [slakpiinstance_contact](#BKMK_slakpiinstance_contact)
- [slakpiinstance_email](#BKMK_slakpiinstance_email)
- [slakpiinstance_fax](#BKMK_slakpiinstance_fax)
- [slakpiinstance_letter](#BKMK_slakpiinstance_letter)
- [slakpiinstance_owner](#BKMK_slakpiinstance_owner)
- [slakpiinstance_phonecall](#BKMK_slakpiinstance_phonecall)
- [slakpiinstance_socialactivity](#BKMK_slakpiinstance_socialactivity)
- [slakpiinstance_task](#BKMK_slakpiinstance_task)
- [TransactionCurrency_slakpiinstance](#BKMK_TransactionCurrency_slakpiinstance)

### <a name="BKMK_business_unit_slakpiinstance"></a> business_unit_slakpiinstance

One-To-Many Relationship: [businessunit business_unit_slakpiinstance](businessunit.md#BKMK_business_unit_slakpiinstance)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slakpiinstancebase_createdby"></a> lk_slakpiinstancebase_createdby

One-To-Many Relationship: [systemuser lk_slakpiinstancebase_createdby](systemuser.md#BKMK_lk_slakpiinstancebase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slakpiinstancebase_createdonbehalfby"></a> lk_slakpiinstancebase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_slakpiinstancebase_createdonbehalfby](systemuser.md#BKMK_lk_slakpiinstancebase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slakpiinstancebase_modifiedby"></a> lk_slakpiinstancebase_modifiedby

One-To-Many Relationship: [systemuser lk_slakpiinstancebase_modifiedby](systemuser.md#BKMK_lk_slakpiinstancebase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slakpiinstancebase_modifiedonbehalfby"></a> lk_slakpiinstancebase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_slakpiinstancebase_modifiedonbehalfby](systemuser.md#BKMK_lk_slakpiinstancebase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_slaitem_slakpiinstance"></a> msdyn_slaitem_slakpiinstance

One-To-Many Relationship: [slaitem msdyn_slaitem_slakpiinstance](slaitem.md#BKMK_msdyn_slaitem_slakpiinstance)

|Property|Value|
|---|---|
|ReferencedEntity|`slaitem`|
|ReferencedAttribute|`slaitemid`|
|ReferencingAttribute|`msdyn_slaitemid`|
|ReferencingEntityNavigationPropertyName|`msdyn_slaitemid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_account"></a> slakpiinstance_account

One-To-Many Relationship: [account slakpiinstance_account](account.md#BKMK_slakpiinstance_account)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_activitypointer"></a> slakpiinstance_activitypointer

One-To-Many Relationship: [activitypointer slakpiinstance_activitypointer](activitypointer.md#BKMK_slakpiinstance_activitypointer)

|Property|Value|
|---|---|
|ReferencedEntity|`activitypointer`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_activitypointer`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_appointment"></a> slakpiinstance_appointment

One-To-Many Relationship: [appointment slakpiinstance_appointment](appointment.md#BKMK_slakpiinstance_appointment)

|Property|Value|
|---|---|
|ReferencedEntity|`appointment`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_appointment`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_contact"></a> slakpiinstance_contact

One-To-Many Relationship: [contact slakpiinstance_contact](contact.md#BKMK_slakpiinstance_contact)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_email"></a> slakpiinstance_email

One-To-Many Relationship: [email slakpiinstance_email](email.md#BKMK_slakpiinstance_email)

|Property|Value|
|---|---|
|ReferencedEntity|`email`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_email`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_fax"></a> slakpiinstance_fax

One-To-Many Relationship: [fax slakpiinstance_fax](fax.md#BKMK_slakpiinstance_fax)

|Property|Value|
|---|---|
|ReferencedEntity|`fax`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_fax`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_letter"></a> slakpiinstance_letter

One-To-Many Relationship: [letter slakpiinstance_letter](letter.md#BKMK_slakpiinstance_letter)

|Property|Value|
|---|---|
|ReferencedEntity|`letter`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_letter`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_owner"></a> slakpiinstance_owner

One-To-Many Relationship: [owner slakpiinstance_owner](owner.md#BKMK_slakpiinstance_owner)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_phonecall"></a> slakpiinstance_phonecall

One-To-Many Relationship: [phonecall slakpiinstance_phonecall](phonecall.md#BKMK_slakpiinstance_phonecall)

|Property|Value|
|---|---|
|ReferencedEntity|`phonecall`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_phonecall`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_socialactivity"></a> slakpiinstance_socialactivity

One-To-Many Relationship: [socialactivity slakpiinstance_socialactivity](socialactivity.md#BKMK_slakpiinstance_socialactivity)

|Property|Value|
|---|---|
|ReferencedEntity|`socialactivity`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_socialactivity`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slakpiinstance_task"></a> slakpiinstance_task

One-To-Many Relationship: [task slakpiinstance_task](task.md#BKMK_slakpiinstance_task)

|Property|Value|
|---|---|
|ReferencedEntity|`task`|
|ReferencedAttribute|`activityid`|
|ReferencingAttribute|`regarding`|
|ReferencingEntityNavigationPropertyName|`regarding_task`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_slakpiinstance"></a> TransactionCurrency_slakpiinstance

One-To-Many Relationship: [transactioncurrency TransactionCurrency_slakpiinstance](transactioncurrency.md#BKMK_TransactionCurrency_slakpiinstance)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_SLAKPIInstance_SyncErrors"></a> SLAKPIInstance_SyncErrors

Many-To-One Relationship: [syncerror SLAKPIInstance_SyncErrors](syncerror.md#BKMK_SLAKPIInstance_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SLAKPIInstance_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.slakpiinstance?displayProperty=fullName>
