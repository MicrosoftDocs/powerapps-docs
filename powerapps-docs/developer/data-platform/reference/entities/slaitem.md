---
title: "SLA Item (SLAItem) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the SLA Item (SLAItem) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# SLA Item (SLAItem) table/entity reference (Microsoft Dataverse)

Contains information about a tracked support KPI for a specific customer.

## Messages

The following table lists the messages for the SLA Item (SLAItem) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /slaitems<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /slaitems(*slaitemid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /slaitems(*slaitemid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /slaitems<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /slaitems(*slaitemid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /slaitems(*slaitemid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the SLA Item (SLAItem) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **SLA Item** |
| **DisplayCollectionName** | **SLA Items** |
| **SchemaName** | `SLAItem` |
| **CollectionSchemaName** | `SLAItems` |
| **EntitySetName** | `slaitems`|
| **LogicalName** | `slaitem` |
| **LogicalCollectionName** | `slaitems` |
| **PrimaryIdAttribute** | `slaitemid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [actionflowuniquename](#BKMK_actionflowuniquename)
- [ActionURL](#BKMK_ActionURL)
- [AllowPauseResume](#BKMK_AllowPauseResume)
- [ApplicableEntity](#BKMK_ApplicableEntity)
- [ApplicableWhenXml](#BKMK_ApplicableWhenXml)
- [BusinessHoursId](#BKMK_BusinessHoursId)
- [ChangedAttributeList](#BKMK_ChangedAttributeList)
- [Description](#BKMK_Description)
- [FailureAfter](#BKMK_FailureAfter)
- [msdyn_AdvancedPauseConfiguration](#BKMK_msdyn_AdvancedPauseConfiguration)
- [msdyn_CustomTimeCalculation](#BKMK_msdyn_CustomTimeCalculation)
- [msdyn_CustomTimeCalculationWorkflowId](#BKMK_msdyn_CustomTimeCalculationWorkflowId)
- [msdyn_PauseConfigurationXml](#BKMK_msdyn_PauseConfigurationXml)
- [msdyn_slakpiid](#BKMK_msdyn_slakpiid)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningUser](#BKMK_OwningUser)
- [RelatedField](#BKMK_RelatedField)
- [SequenceNumber](#BKMK_SequenceNumber)
- [SLAId](#BKMK_SLAId)
- [SLAItemId](#BKMK_SLAItemId)
- [SuccessConditionsXml](#BKMK_SuccessConditionsXml)
- [WarnAfter](#BKMK_WarnAfter)
- [WorkflowId](#BKMK_WorkflowId)

### <a name="BKMK_actionflowuniquename"></a> actionflowuniquename

|Property|Value|
|---|---|
|Description||
|DisplayName|**Action Flow Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actionflowuniquename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ActionURL"></a> ActionURL

|Property|Value|
|---|---|
|Description|**Action URL**|
|DisplayName|**Action URL**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`actionurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_AllowPauseResume"></a> AllowPauseResume

|Property|Value|
|---|---|
|Description|**Select whether this SLA will allow pausing and resuming during the time calculation.**|
|DisplayName|**Allow Pause and Resume**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`allowpauseresume`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`slaitem_allowpauseresume`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ApplicableEntity"></a> ApplicableEntity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Applicable Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`applicableentity`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ApplicableWhenXml"></a> ApplicableWhenXml

|Property|Value|
|---|---|
|Description|**Condition for SLA item**|
|DisplayName|**ApplicableWhenXml**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`applicablewhenxml`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_BusinessHoursId"></a> BusinessHoursId

|Property|Value|
|---|---|
|Description|**Choose the business hours for calculating SLA item timelines.**|
|DisplayName|**Business Hours**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`businesshoursid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|calendar|

### <a name="BKMK_ChangedAttributeList"></a> ChangedAttributeList

|Property|Value|
|---|---|
|Description||
|DisplayName|**Changed Attribute List**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`changedattributelist`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Type additional information to describe the SLA Item**|
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

### <a name="BKMK_FailureAfter"></a> FailureAfter

|Property|Value|
|---|---|
|Description|**Select how soon the success criteria must be met until the SLA item is considered failed and failure actions are initiated. The actual duration is based on the business hours as specified in the associated SLA record.**|
|DisplayName|**Failure After**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`failureafter`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_AdvancedPauseConfiguration"></a> msdyn_AdvancedPauseConfiguration

|Property|Value|
|---|---|
|Description||
|DisplayName|**Advanced Pause Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_advancedpauseconfiguration`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`slaitem_msdyn_advancedpauseconfiguration`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_CustomTimeCalculation"></a> msdyn_CustomTimeCalculation

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom Time Calculation Flag**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_customtimecalculation`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`slaitem_msdyn_customtimecalculation`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_CustomTimeCalculationWorkflowId"></a> msdyn_CustomTimeCalculationWorkflowId

|Property|Value|
|---|---|
|Description|**Unique identifier for Custom Time Calculation Workflow associated with SLA Item.**|
|DisplayName|**Custom Time Calculation Workflow**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_customtimecalculationworkflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_msdyn_PauseConfigurationXml"></a> msdyn_PauseConfigurationXml

|Property|Value|
|---|---|
|Description||
|DisplayName|**PauseConfigurationXml**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_pauseconfigurationxml`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_slakpiid"></a> msdyn_slakpiid

|Property|Value|
|---|---|
|Description|**Unique identifier for SLAKPI associated with SLA Item.**|
|DisplayName|**SLA KPI**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_slakpiid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_slakpi|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a descriptive name of the service level agreement (SLA) item.**|
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
|Description|**Enter the user or team who owns the SLA. This field is updated every time the item is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
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
|Type|EntityName|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the SLA Item record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets||

### <a name="BKMK_RelatedField"></a> RelatedField

|Property|Value|
|---|---|
|Description|**Select the service level agreement (SLA) key performance indicator (KPI) that this SLA Item is created for.**|
|DisplayName|**Related Case Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relatedfield`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_SequenceNumber"></a> SequenceNumber

|Property|Value|
|---|---|
|Description|**Select the time zone, or UTC offset, for this address so that other people can reference it when they contact someone at this address.**|
|DisplayName|**Sequence**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|0|

### <a name="BKMK_SLAId"></a> SLAId

|Property|Value|
|---|---|
|Description|**Unique identifier for SLA associated with SLA Item.**|
|DisplayName|**SLA**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`slaid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|sla|

### <a name="BKMK_SLAItemId"></a> SLAItemId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SLA Item.**|
|DisplayName|**SLA Item**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slaitemid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SuccessConditionsXml"></a> SuccessConditionsXml

|Property|Value|
|---|---|
|Description|**Condition for SLA item**|
|DisplayName|**SuccessConditionsXml**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`successconditionsxml`|
|RequiredLevel|ApplicationRequired|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_WarnAfter"></a> WarnAfter

|Property|Value|
|---|---|
|Description|**Select how soon the success criteria must be met before warning actions are initiated. The actual duration is based on the business hours as specified in the associated SLA record.**|
|DisplayName|**Warn After**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`warnafter`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_WorkflowId"></a> WorkflowId

|Property|Value|
|---|---|
|Description|**Workflow associated with the SLA Item.**|
|DisplayName|**Workflow ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [SLAItemIdUnique](#BKMK_SLAItemIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
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
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
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
|Description|**Exchange rate between the currency associated with the SLA Item record and the base currency.**|
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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**For internal use only.**|
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
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
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

### <a name="BKMK_SLAItemIdUnique"></a> SLAItemIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`slaitemidunique`|
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

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the SLA Item record.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the SLA Item.**|
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

- [calendar_slaitem](#BKMK_calendar_slaitem)
- [lk_slaitembase_createdby](#BKMK_lk_slaitembase_createdby)
- [lk_slaitembase_createdonbehalfby](#BKMK_lk_slaitembase_createdonbehalfby)
- [lk_slaitembase_modifiedby](#BKMK_lk_slaitembase_modifiedby)
- [lk_slaitembase_modifiedonbehalfby](#BKMK_lk_slaitembase_modifiedonbehalfby)
- [msdyn_msdyn_slakpi_slaitem](#BKMK_msdyn_msdyn_slakpi_slaitem)
- [msdyn_workflow_slaitem_customtimecalculationworkflowid](#BKMK_msdyn_workflow_slaitem_customtimecalculationworkflowid)
- [sla_slaitem_slaId](#BKMK_sla_slaitem_slaId)
- [slaitembase_workflowid](#BKMK_slaitembase_workflowid)
- [TransactionCurrency_SLAItem](#BKMK_TransactionCurrency_SLAItem)

### <a name="BKMK_calendar_slaitem"></a> calendar_slaitem

One-To-Many Relationship: [calendar calendar_slaitem](calendar.md#BKMK_calendar_slaitem)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`businesshoursid`|
|ReferencingEntityNavigationPropertyName|`businesshoursid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slaitembase_createdby"></a> lk_slaitembase_createdby

One-To-Many Relationship: [systemuser lk_slaitembase_createdby](systemuser.md#BKMK_lk_slaitembase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slaitembase_createdonbehalfby"></a> lk_slaitembase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_slaitembase_createdonbehalfby](systemuser.md#BKMK_lk_slaitembase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slaitembase_modifiedby"></a> lk_slaitembase_modifiedby

One-To-Many Relationship: [systemuser lk_slaitembase_modifiedby](systemuser.md#BKMK_lk_slaitembase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_slaitembase_modifiedonbehalfby"></a> lk_slaitembase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_slaitembase_modifiedonbehalfby](systemuser.md#BKMK_lk_slaitembase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_msdyn_slakpi_slaitem"></a> msdyn_msdyn_slakpi_slaitem

One-To-Many Relationship: [msdyn_slakpi msdyn_msdyn_slakpi_slaitem](msdyn_slakpi.md#BKMK_msdyn_msdyn_slakpi_slaitem)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_slakpi`|
|ReferencedAttribute|`msdyn_slakpiid`|
|ReferencingAttribute|`msdyn_slakpiid`|
|ReferencingEntityNavigationPropertyName|`msdyn_SLAKPIID`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_workflow_slaitem_customtimecalculationworkflowid"></a> msdyn_workflow_slaitem_customtimecalculationworkflowid

One-To-Many Relationship: [workflow msdyn_workflow_slaitem_customtimecalculationworkflowid](workflow.md#BKMK_msdyn_workflow_slaitem_customtimecalculationworkflowid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`msdyn_customtimecalculationworkflowid`|
|ReferencingEntityNavigationPropertyName|`msdyn_customtimecalculationworkflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sla_slaitem_slaId"></a> sla_slaitem_slaId

One-To-Many Relationship: [sla sla_slaitem_slaId](sla.md#BKMK_sla_slaitem_slaId)

|Property|Value|
|---|---|
|ReferencedEntity|`sla`|
|ReferencedAttribute|`slaid`|
|ReferencingAttribute|`slaid`|
|ReferencingEntityNavigationPropertyName|`slaid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_slaitembase_workflowid"></a> slaitembase_workflowid

One-To-Many Relationship: [workflow slaitembase_workflowid](workflow.md#BKMK_slaitembase_workflowid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`workflowid`|
|ReferencingEntityNavigationPropertyName|`workflowid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_SLAItem"></a> TransactionCurrency_SLAItem

One-To-Many Relationship: [transactioncurrency TransactionCurrency_SLAItem](transactioncurrency.md#BKMK_TransactionCurrency_SLAItem)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_slaitem_slakpiinstance](#BKMK_msdyn_slaitem_slakpiinstance)
- [SLAItem_SyncErrors](#BKMK_SLAItem_SyncErrors)

### <a name="BKMK_msdyn_slaitem_slakpiinstance"></a> msdyn_slaitem_slakpiinstance

Many-To-One Relationship: [slakpiinstance msdyn_slaitem_slakpiinstance](slakpiinstance.md#BKMK_msdyn_slaitem_slakpiinstance)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`msdyn_slaitemid`|
|ReferencedEntityNavigationPropertyName|`msdyn_slaitem_slakpiinstance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_SLAItem_SyncErrors"></a> SLAItem_SyncErrors

Many-To-One Relationship: [syncerror SLAItem_SyncErrors](syncerror.md#BKMK_SLAItem_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`SLAItem_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.slaitem?displayProperty=fullName>
