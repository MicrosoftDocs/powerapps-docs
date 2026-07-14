---
title: "Analysis Component (msdyn_analysiscomponent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Analysis Component (msdyn_analysiscomponent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Analysis Component (msdyn_analysiscomponent) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Analysis Component (msdyn_analysiscomponent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_analysiscomponents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: True |`GET` /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_analysiscomponents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_analysiscomponents(*msdyn_analysiscomponentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Analysis Component (msdyn_analysiscomponent) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Analysis Component (msdyn_analysiscomponent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Analysis Component** |
| **DisplayCollectionName** | **Analysis Components** |
| **SchemaName** | `msdyn_analysiscomponent` |
| **CollectionSchemaName** | `msdyn_analysiscomponents` |
| **EntitySetName** | `msdyn_analysiscomponents`|
| **LogicalName** | `msdyn_analysiscomponent` |
| **LogicalCollectionName** | `msdyn_analysiscomponents` |
| **PrimaryIdAttribute** | `msdyn_analysiscomponentid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_analysiscomponentId](#BKMK_msdyn_analysiscomponentId)
- [msdyn_AnalysisComponentType](#BKMK_msdyn_AnalysisComponentType)
- [msdyn_AnalysisJobId](#BKMK_msdyn_AnalysisJobId)
- [msdyn_ComponentId](#BKMK_msdyn_ComponentId)
- [msdyn_ComponentName](#BKMK_msdyn_ComponentName)
- [msdyn_ComponentType](#BKMK_msdyn_ComponentType)
- [msdyn_ComponentVersion](#BKMK_msdyn_ComponentVersion)
- [msdyn_ErrorCount](#BKMK_msdyn_ErrorCount)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_RetryCount](#BKMK_msdyn_RetryCount)
- [msdyn_RuleFailCount](#BKMK_msdyn_RuleFailCount)
- [msdyn_RulePassCount](#BKMK_msdyn_RulePassCount)
- [msdyn_RulePassRate](#BKMK_msdyn_RulePassRate)
- [msdyn_sevcriticalcount](#BKMK_msdyn_sevcriticalcount)
- [msdyn_sevhighcount](#BKMK_msdyn_sevhighcount)
- [msdyn_sevlowcount](#BKMK_msdyn_sevlowcount)
- [msdyn_sevmediumcount](#BKMK_msdyn_sevmediumcount)
- [msdyn_SolutionHealthRuleSetId](#BKMK_msdyn_SolutionHealthRuleSetId)
- [msdyn_SuggestionCount](#BKMK_msdyn_SuggestionCount)
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

### <a name="BKMK_msdyn_analysiscomponentId"></a> msdyn_analysiscomponentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Analysis Component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_analysiscomponentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_AnalysisComponentType"></a> msdyn_AnalysisComponentType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Analysis Component Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysiscomponenttype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|192350001|
|GlobalChoiceName|`msdyn_analysiscomponent_msdyn_analysiscomponenttype`|

#### msdyn_AnalysisComponentType Choices/Options

|Value|Label|
|---|---|
|192350000|**Organization Health**|
|192350001|**Component Health**|
|192350002|**Object Health**|

### <a name="BKMK_msdyn_AnalysisJobId"></a> msdyn_AnalysisJobId

|Property|Value|
|---|---|
|Description|**The parent Analysis Job that analyzed this particular Analysis Component.**|
|DisplayName|**Analysis Job**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisjobid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_analysisjob|

### <a name="BKMK_msdyn_ComponentId"></a> msdyn_ComponentId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentid`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_msdyn_ComponentName"></a> msdyn_ComponentName

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentname`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_ComponentType"></a> msdyn_ComponentType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componenttype`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_analysiscomponent_msdyn_componenttype`|

#### msdyn_ComponentType Choices/Options

|Value|Label|
|---|---|
|192350000|**Solution**|
|192350001|**Entity**|
|192350002|**View**|
|192350003|**Form**|
|192350004|**Plugin**|
|192350005|**Configuration**|

### <a name="BKMK_msdyn_ComponentVersion"></a> msdyn_ComponentVersion

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Version**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componentversion`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|50|

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
|MaxLength|200|

### <a name="BKMK_msdyn_RetryCount"></a> msdyn_RetryCount

|Property|Value|
|---|---|
|Description||
|DisplayName|**Retry Count**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_retrycount`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_msdyn_RulePassRate"></a> msdyn_RulePassRate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rule Pass Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_rulepassrate`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

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

### <a name="BKMK_msdyn_SolutionHealthRuleSetId"></a> msdyn_SolutionHealthRuleSetId

|Property|Value|
|---|---|
|Description|**The Solution Health Rule Set for which this is analysis component is for.**|
|DisplayName|**Solution Health Rule Set**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionhealthrulesetid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_solutionhealthruleset|

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
|Description|**Status of the Analysis Component**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_analysiscomponent_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 192350000<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Analysis Component**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_analysiscomponent_statuscode`|

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

- [business_unit_msdyn_analysiscomponent](#BKMK_business_unit_msdyn_analysiscomponent)
- [lk_msdyn_analysiscomponent_createdby](#BKMK_lk_msdyn_analysiscomponent_createdby)
- [lk_msdyn_analysiscomponent_createdonbehalfby](#BKMK_lk_msdyn_analysiscomponent_createdonbehalfby)
- [lk_msdyn_analysiscomponent_modifiedby](#BKMK_lk_msdyn_analysiscomponent_modifiedby)
- [lk_msdyn_analysiscomponent_modifiedonbehalfby](#BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby)
- [msdyn_analysisjob_msdyn_analysiscomponent](#BKMK_msdyn_analysisjob_msdyn_analysiscomponent)
- [msdyn_msdyn_solutionhealthruleset_msdyn_analysi](#BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_analysi)
- [owner_msdyn_analysiscomponent](#BKMK_owner_msdyn_analysiscomponent)
- [team_msdyn_analysiscomponent](#BKMK_team_msdyn_analysiscomponent)
- [user_msdyn_analysiscomponent](#BKMK_user_msdyn_analysiscomponent)

### <a name="BKMK_business_unit_msdyn_analysiscomponent"></a> business_unit_msdyn_analysiscomponent

One-To-Many Relationship: [businessunit business_unit_msdyn_analysiscomponent](businessunit.md#BKMK_business_unit_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysiscomponent_createdby"></a> lk_msdyn_analysiscomponent_createdby

One-To-Many Relationship: [systemuser lk_msdyn_analysiscomponent_createdby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysiscomponent_createdonbehalfby"></a> lk_msdyn_analysiscomponent_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_analysiscomponent_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysiscomponent_modifiedby"></a> lk_msdyn_analysiscomponent_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_analysiscomponent_modifiedby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby"></a> lk_msdyn_analysiscomponent_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_analysiscomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_analysiscomponent_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_msdyn_analysiscomponent"></a> msdyn_analysisjob_msdyn_analysiscomponent

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_msdyn_analysiscomponent](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`msdyn_analysisjobid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AnalysisJobId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_analysi"></a> msdyn_msdyn_solutionhealthruleset_msdyn_analysi

One-To-Many Relationship: [msdyn_solutionhealthruleset msdyn_msdyn_solutionhealthruleset_msdyn_analysi](msdyn_solutionhealthruleset.md#BKMK_msdyn_msdyn_solutionhealthruleset_msdyn_analysi)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_solutionhealthruleset`|
|ReferencedAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingAttribute|`msdyn_solutionhealthrulesetid`|
|ReferencingEntityNavigationPropertyName|`msdyn_SolutionHealthRuleSetId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_analysiscomponent"></a> owner_msdyn_analysiscomponent

One-To-Many Relationship: [owner owner_msdyn_analysiscomponent](owner.md#BKMK_owner_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_analysiscomponent"></a> team_msdyn_analysiscomponent

One-To-Many Relationship: [team team_msdyn_analysiscomponent](team.md#BKMK_team_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_analysiscomponent"></a> user_msdyn_analysiscomponent

One-To-Many Relationship: [systemuser user_msdyn_analysiscomponent](systemuser.md#BKMK_user_msdyn_analysiscomponent)

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

- [msdyn_analysiscomponent_AsyncOperations](#BKMK_msdyn_analysiscomponent_AsyncOperations)
- [msdyn_analysiscomponent_BulkDeleteFailures](#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)
- [msdyn_analysiscomponent_DuplicateBaseRecord](#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord)
- [msdyn_analysiscomponent_DuplicateMatchingRecord](#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord)
- [msdyn_analysiscomponent_MailboxTrackingFolders](#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)
- [msdyn_analysiscomponent_msdyn_analysisresult](#BKMK_msdyn_analysiscomponent_msdyn_analysisresult)
- [msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses)
- [msdyn_analysiscomponent_ProcessSession](#BKMK_msdyn_analysiscomponent_ProcessSession)
- [msdyn_analysiscomponent_SyncErrors](#BKMK_msdyn_analysiscomponent_SyncErrors)

### <a name="BKMK_msdyn_analysiscomponent_AsyncOperations"></a> msdyn_analysiscomponent_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_analysiscomponent_AsyncOperations](asyncoperation.md#BKMK_msdyn_analysiscomponent_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_BulkDeleteFailures"></a> msdyn_analysiscomponent_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_analysiscomponent_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_analysiscomponent_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_DuplicateBaseRecord"></a> msdyn_analysiscomponent_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_analysiscomponent_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_analysiscomponent_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord"></a> msdyn_analysiscomponent_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_analysiscomponent_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_analysiscomponent_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_MailboxTrackingFolders"></a> msdyn_analysiscomponent_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_analysiscomponent_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_analysiscomponent_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_msdyn_analysisresult"></a> msdyn_analysiscomponent_msdyn_analysisresult

Many-To-One Relationship: [msdyn_analysisresult msdyn_analysiscomponent_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_msdyn_analysiscomponent_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresult`|
|ReferencingAttribute|`msdyn_analysiscomponentid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_msdyn_analysisresult`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses"></a> msdyn_analysiscomponent_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_analysiscomponent_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_analysiscomponent_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_ProcessSession"></a> msdyn_analysiscomponent_ProcessSession

Many-To-One Relationship: [processsession msdyn_analysiscomponent_ProcessSession](processsession.md#BKMK_msdyn_analysiscomponent_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysiscomponent_SyncErrors"></a> msdyn_analysiscomponent_SyncErrors

Many-To-One Relationship: [syncerror msdyn_analysiscomponent_SyncErrors](syncerror.md#BKMK_msdyn_analysiscomponent_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysiscomponent_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_analysiscomponent?displayProperty=fullName>
