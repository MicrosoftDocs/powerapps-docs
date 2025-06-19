---
title: "Analysis Job (msdyn_analysisjob) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Analysis Job (msdyn_analysisjob) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Analysis Job (msdyn_analysisjob) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Analysis Job (msdyn_analysisjob) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_analysisjobs(*msdyn_analysisjobid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_analysisjobs<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_analysisjobs<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_analysisjobs(*msdyn_analysisjobid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_analysisjobs(*msdyn_analysisjobid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Analysis Job (msdyn_analysisjob) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Analysis Job (msdyn_analysisjob) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Analysis Job** |
| **DisplayCollectionName** | **Analysis Jobs** |
| **SchemaName** | `msdyn_analysisjob` |
| **CollectionSchemaName** | `msdyn_analysisjobs` |
| **EntitySetName** | `msdyn_analysisjobs`|
| **LogicalName** | `msdyn_analysisjob` |
| **LogicalCollectionName** | `msdyn_analysisjobs` |
| **PrimaryIdAttribute** | `msdyn_analysisjobid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_analysisjobId](#BKMK_msdyn_analysisjobId)
- [msdyn_CustomDetails](#BKMK_msdyn_CustomDetails)
- [msdyn_DisplayStatus](#BKMK_msdyn_DisplayStatus)
- [msdyn_EndTime](#BKMK_msdyn_EndTime)
- [msdyn_ErrorCount](#BKMK_msdyn_ErrorCount)
- [msdyn_Exception](#BKMK_msdyn_Exception)
- [msdyn_InAppNotificationEnabled](#BKMK_msdyn_InAppNotificationEnabled)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_RuleFailCount](#BKMK_msdyn_RuleFailCount)
- [msdyn_RulePassCount](#BKMK_msdyn_RulePassCount)
- [msdyn_RuleRunCount](#BKMK_msdyn_RuleRunCount)
- [msdyn_RunCorrelationId](#BKMK_msdyn_RunCorrelationId)
- [msdyn_sevcriticalcount](#BKMK_msdyn_sevcriticalcount)
- [msdyn_sevhighcount](#BKMK_msdyn_sevhighcount)
- [msdyn_sevlowcount](#BKMK_msdyn_sevlowcount)
- [msdyn_sevmediumcount](#BKMK_msdyn_sevmediumcount)
- [msdyn_StartTime](#BKMK_msdyn_StartTime)
- [msdyn_SuggestionCount](#BKMK_msdyn_SuggestionCount)
- [msdyn_TenantId](#BKMK_msdyn_TenantId)
- [msdyn_TriggerType](#BKMK_msdyn_TriggerType)
- [msdyn_WarningCount](#BKMK_msdyn_WarningCount)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Sequence number of the import that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_msdyn_analysisjobId"></a> msdyn_analysisjobId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Analysis Job**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisjobid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_CustomDetails"></a> msdyn_CustomDetails

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom Details**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_customdetails`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_DisplayStatus"></a> msdyn_DisplayStatus

|Property|Value|
|---|---|
|Description||
|DisplayName|**Display Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_displaystatus`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_EndTime"></a> msdyn_EndTime

|Property|Value|
|---|---|
|Description||
|DisplayName|**End Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_endtime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_ErrorCount"></a> msdyn_ErrorCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Error Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_errorcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_Exception"></a> msdyn_Exception

|Property|Value|
|---|---|
|Description||
|DisplayName|**Exception**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_exception`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_InAppNotificationEnabled"></a> msdyn_InAppNotificationEnabled

|Property|Value|
|---|---|
|Description|**Health rule set Failure In App Notification Enabled.**|
|DisplayName|**Health rule set Failure In App Notification Enabled.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_inappnotificationenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_analysisjob_msdyn_inappnotificationenabled`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_msdyn_name"></a> msdyn_name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_RuleFailCount"></a> msdyn_RuleFailCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rule Fail Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_rulefailcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_RulePassCount"></a> msdyn_RulePassCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rule Pass Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_rulepasscount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_RuleRunCount"></a> msdyn_RuleRunCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rule Run Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ruleruncount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_RunCorrelationId"></a> msdyn_RunCorrelationId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Run Correlation Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_runcorrelationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_msdyn_sevcriticalcount"></a> msdyn_sevcriticalcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Critical Severity Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sevcriticalcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_sevhighcount"></a> msdyn_sevhighcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**High Severity Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sevhighcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_sevlowcount"></a> msdyn_sevlowcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Low Severity Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sevlowcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_sevmediumcount"></a> msdyn_sevmediumcount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Medium Severity Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sevmediumcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_StartTime"></a> msdyn_StartTime

|Property|Value|
|---|---|
|Description||
|DisplayName|**Start Time**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_starttime`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_SuggestionCount"></a> msdyn_SuggestionCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Suggestion Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_suggestioncount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_TenantId"></a> msdyn_TenantId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Tenant Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_tenantid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_TriggerType"></a> msdyn_TriggerType

|Property|Value|
|---|---|
|Description|**Health rule set Trigger Type.**|
|DisplayName|**Health rule set Trigger Type.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_triggertype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_WarningCount"></a> msdyn_WarningCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Warning Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_warningcount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Owner Id**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|SystemRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description|**Owner Id Type**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Analysis Job**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_analysisjob_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 192350000<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Analysis Job**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_analysisjob_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Pending**<br />State:0<br />TransitionData: None|
|2|Label: **Canceled**<br />State:1<br />TransitionData: None|
|192350000|Label: **Running**<br />State:0<br />TransitionData: None|
|192350001|Label: **Complete**<br />State:0<br />TransitionData: None|
|192350002|Label: **Exception**<br />State:0<br />TransitionData: None|
|192350003|Label: **Completed With Exceptions**<br />State:0<br />TransitionData: None|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [msdyn_AnalysisJobsReport](#BKMK_msdyn_AnalysisJobsReport)
- [msdyn_AnalysisJobsReport_Name](#BKMK_msdyn_AnalysisJobsReport_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the record.**|
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
|Description|**Date and time when the record was created.**|
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
|Description|**Unique identifier of the delegate user who created the record.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who modified the record.**|
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
|Description|**Date and time when the record was modified.**|
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
|Description|**Unique identifier of the delegate user who modified the record.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_msdyn_AnalysisJobsReport"></a> msdyn_AnalysisJobsReport

|Property|Value|
|---|---|
|Description|**Analysis job report stored in excel format.**|
|DisplayName|**Analysis Job Report File**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisjobsreport`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_AnalysisJobsReport_Name"></a> msdyn_AnalysisJobsReport_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisjobsreport_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_OwnerIdName"></a> OwnerIdName

|Property|Value|
|---|---|
|Description|**Name of the owner**|
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
|Description|**Yomi name of the owner**|
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
|Description|**Unique identifier for the business unit that owns the record**|
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
|Description|**Unique identifier for the team that owns the record.**|
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
|Description|**Unique identifier for the user that owns the record.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version Number**|
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

- [business_unit_msdyn_analysisjob](#BKMK_business_unit_msdyn_analysisjob)
- [FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport](#BKMK_FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport)
- [lk_msdyn_analysisjob_createdby](#BKMK_lk_msdyn_analysisjob_createdby)
- [lk_msdyn_analysisjob_createdonbehalfby](#BKMK_lk_msdyn_analysisjob_createdonbehalfby)
- [lk_msdyn_analysisjob_modifiedby](#BKMK_lk_msdyn_analysisjob_modifiedby)
- [lk_msdyn_analysisjob_modifiedonbehalfby](#BKMK_lk_msdyn_analysisjob_modifiedonbehalfby)
- [owner_msdyn_analysisjob](#BKMK_owner_msdyn_analysisjob)
- [team_msdyn_analysisjob](#BKMK_team_msdyn_analysisjob)
- [user_msdyn_analysisjob](#BKMK_user_msdyn_analysisjob)

### <a name="BKMK_business_unit_msdyn_analysisjob"></a> business_unit_msdyn_analysisjob

One-To-Many Relationship: [businessunit business_unit_msdyn_analysisjob](businessunit.md#BKMK_business_unit_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport"></a> FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport](fileattachment.md#BKMK_FileAttachment_msdyn_analysisjob_msdyn_AnalysisJobsReport)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_analysisjobsreport`|
|ReferencingEntityNavigationPropertyName|`msdyn_analysisjobsreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisjob_createdby"></a> lk_msdyn_analysisjob_createdby

One-To-Many Relationship: [systemuser lk_msdyn_analysisjob_createdby](systemuser.md#BKMK_lk_msdyn_analysisjob_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisjob_createdonbehalfby"></a> lk_msdyn_analysisjob_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_analysisjob_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_analysisjob_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisjob_modifiedby"></a> lk_msdyn_analysisjob_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_analysisjob_modifiedby](systemuser.md#BKMK_lk_msdyn_analysisjob_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisjob_modifiedonbehalfby"></a> lk_msdyn_analysisjob_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_analysisjob_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_analysisjob_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_analysisjob"></a> owner_msdyn_analysisjob

One-To-Many Relationship: [owner owner_msdyn_analysisjob](owner.md#BKMK_owner_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_analysisjob"></a> team_msdyn_analysisjob

One-To-Many Relationship: [team team_msdyn_analysisjob](team.md#BKMK_team_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_analysisjob"></a> user_msdyn_analysisjob

One-To-Many Relationship: [systemuser user_msdyn_analysisjob](systemuser.md#BKMK_user_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`owninguser`|
|ReferencingEntityNavigationPropertyName|`owninguser`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [msdyn_analysisjob_AsyncOperations](#BKMK_msdyn_analysisjob_AsyncOperations)
- [msdyn_analysisjob_BulkDeleteFailures](#BKMK_msdyn_analysisjob_BulkDeleteFailures)
- [msdyn_analysisjob_DuplicateBaseRecord](#BKMK_msdyn_analysisjob_DuplicateBaseRecord)
- [msdyn_analysisjob_DuplicateMatchingRecord](#BKMK_msdyn_analysisjob_DuplicateMatchingRecord)
- [msdyn_analysisjob_FileAttachments](#BKMK_msdyn_analysisjob_FileAttachments)
- [msdyn_analysisjob_MailboxTrackingFolders](#BKMK_msdyn_analysisjob_MailboxTrackingFolders)
- [msdyn_analysisjob_msdyn_analysiscomponent](#BKMK_msdyn_analysisjob_msdyn_analysiscomponent)
- [msdyn_analysisjob_msdyn_analysisresult](#BKMK_msdyn_analysisjob_msdyn_analysisresult)
- [msdyn_analysisjob_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses)
- [msdyn_analysisjob_ProcessSession](#BKMK_msdyn_analysisjob_ProcessSession)
- [msdyn_analysisjob_SyncErrors](#BKMK_msdyn_analysisjob_SyncErrors)

### <a name="BKMK_msdyn_analysisjob_AsyncOperations"></a> msdyn_analysisjob_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_analysisjob_AsyncOperations](asyncoperation.md#BKMK_msdyn_analysisjob_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_BulkDeleteFailures"></a> msdyn_analysisjob_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_analysisjob_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_analysisjob_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_DuplicateBaseRecord"></a> msdyn_analysisjob_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_analysisjob_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_analysisjob_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_DuplicateMatchingRecord"></a> msdyn_analysisjob_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_analysisjob_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_analysisjob_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_FileAttachments"></a> msdyn_analysisjob_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_analysisjob_FileAttachments](fileattachment.md#BKMK_msdyn_analysisjob_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_MailboxTrackingFolders"></a> msdyn_analysisjob_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_analysisjob_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_analysisjob_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_msdyn_analysiscomponent"></a> msdyn_analysisjob_msdyn_analysiscomponent

Many-To-One Relationship: [msdyn_analysiscomponent msdyn_analysisjob_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_msdyn_analysisjob_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysiscomponent`|
|ReferencingAttribute|`msdyn_analysisjobid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_msdyn_analysiscomponent`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_msdyn_analysisresult"></a> msdyn_analysisjob_msdyn_analysisresult

Many-To-One Relationship: [msdyn_analysisresult msdyn_analysisjob_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_msdyn_analysisjob_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresult`|
|ReferencingAttribute|`msdyn_analysisjobid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_msdyn_analysisresult`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses"></a> msdyn_analysisjob_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_analysisjob_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_analysisjob_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_ProcessSession"></a> msdyn_analysisjob_ProcessSession

Many-To-One Relationship: [processsession msdyn_analysisjob_ProcessSession](processsession.md#BKMK_msdyn_analysisjob_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisjob_SyncErrors"></a> msdyn_analysisjob_SyncErrors

Many-To-One Relationship: [syncerror msdyn_analysisjob_SyncErrors](syncerror.md#BKMK_msdyn_analysisjob_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisjob_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_analysisjob?displayProperty=fullName>
