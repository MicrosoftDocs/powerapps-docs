---
title: "Analysis Result (msdyn_analysisresult) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Analysis Result (msdyn_analysisresult) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Analysis Result (msdyn_analysisresult) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Analysis Result (msdyn_analysisresult) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Assign`<br />Event: True |`PATCH` /msdyn_analysisresults(*msdyn_analysisresultid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_analysisresults<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_analysisresults(*msdyn_analysisresultid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Restore`<br />Event: True |<xref:Microsoft.Dynamics.CRM.Restore?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retrieve`<br />Event: True |`GET` /msdyn_analysisresults(*msdyn_analysisresultid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_analysisresults<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_analysisresults(*msdyn_analysisresultid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /msdyn_analysisresults(*msdyn_analysisresultid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_analysisresults(*msdyn_analysisresultid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the Analysis Result (msdyn_analysisresult) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the Analysis Result (msdyn_analysisresult) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Analysis Result** |
| **DisplayCollectionName** | **Analysis Results** |
| **SchemaName** | `msdyn_analysisresult` |
| **CollectionSchemaName** | `msdyn_analysisresults` |
| **EntitySetName** | `msdyn_analysisresults`|
| **LogicalName** | `msdyn_analysisresult` |
| **LogicalCollectionName** | `msdyn_analysisresults` |
| **PrimaryIdAttribute** | `msdyn_analysisresultid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AnalysisComponentId](#BKMK_msdyn_AnalysisComponentId)
- [msdyn_AnalysisComponentType](#BKMK_msdyn_AnalysisComponentType)
- [msdyn_AnalysisJobId](#BKMK_msdyn_AnalysisJobId)
- [msdyn_analysisresultId](#BKMK_msdyn_analysisresultId)
- [msdyn_Category](#BKMK_msdyn_Category)
- [msdyn_ComponentType](#BKMK_msdyn_ComponentType)
- [msdyn_EntityName](#BKMK_msdyn_EntityName)
- [msdyn_FileUri](#BKMK_msdyn_FileUri)
- [msdyn_HasResolution](#BKMK_msdyn_HasResolution)
- [msdyn_helplink](#BKMK_msdyn_helplink)
- [msdyn_Level](#BKMK_msdyn_Level)
- [msdyn_Line](#BKMK_msdyn_Line)
- [msdyn_Member](#BKMK_msdyn_Member)
- [msdyn_Message](#BKMK_msdyn_Message)
- [msdyn_MessageArguments](#BKMK_msdyn_MessageArguments)
- [msdyn_MessageId](#BKMK_msdyn_MessageId)
- [msdyn_Module](#BKMK_msdyn_Module)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_RepairIssueType](#BKMK_msdyn_RepairIssueType)
- [msdyn_ReturnStatus](#BKMK_msdyn_ReturnStatus)
- [msdyn_RuleId](#BKMK_msdyn_RuleId)
- [msdyn_RuleReferenceUri](#BKMK_msdyn_RuleReferenceUri)
- [msdyn_Severity](#BKMK_msdyn_Severity)
- [msdyn_Snippet](#BKMK_msdyn_Snippet)
- [msdyn_SolutionHealthMessage](#BKMK_msdyn_SolutionHealthMessage)
- [msdyn_Type](#BKMK_msdyn_Type)
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

### <a name="BKMK_msdyn_AnalysisComponentId"></a> msdyn_AnalysisComponentId

|Property|Value|
|---|---|
|Description|**The associated Analysis Component that contains the issue described by the Analysis Result.**|
|DisplayName|**Analysis Component**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysiscomponentid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_analysiscomponent|

### <a name="BKMK_msdyn_AnalysisComponentType"></a> msdyn_AnalysisComponentType

|Property|Value|
|---|---|
|Description||
|DisplayName|**AnalysisComponentType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysiscomponenttype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|192350001|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_analysiscomponenttype`|

#### msdyn_AnalysisComponentType Choices/Options

|Value|Label|
|---|---|
|192350000|**Organization Health**|
|192350001|**Component Health**|

### <a name="BKMK_msdyn_AnalysisJobId"></a> msdyn_AnalysisJobId

|Property|Value|
|---|---|
|Description|**The parent Analysis Job that produced the Analysis Result**|
|DisplayName|**Analysis Job**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisjobid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|msdyn_analysisjob|

### <a name="BKMK_msdyn_analysisresultId"></a> msdyn_analysisresultId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Analysis Result**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisresultid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_Category"></a> msdyn_Category

|Property|Value|
|---|---|
|Description||
|DisplayName|**Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_category`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_category`|

#### msdyn_Category Choices/Options

|Value|Label|
|---|---|
|192350000|**Performance**|
|192350001|**Upgrade Readiness**|
|192350002|**Usage**|
|192350003|**Security**|
|192350004|**Design**|
|192350005|**Online Migration**|
|192350006|**Maintainability**|
|192350007|**Supportability**|
|192350008|**Accessibility**|
|192350009|**Licensing**|

### <a name="BKMK_msdyn_ComponentType"></a> msdyn_ComponentType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Component Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_componenttype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_componenttype`|

#### msdyn_ComponentType Choices/Options

|Value|Label|
|---|---|
|192350000|**Web Resources**|
|192350001|**Plug-In**|
|192350002|**Configuration**|

### <a name="BKMK_msdyn_EntityName"></a> msdyn_EntityName

|Property|Value|
|---|---|
|Description||
|DisplayName|**Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_entityname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_msdyn_FileUri"></a> msdyn_FileUri

|Property|Value|
|---|---|
|Description||
|DisplayName|**File Uri**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_fileuri`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_HasResolution"></a> msdyn_HasResolution

|Property|Value|
|---|---|
|Description||
|DisplayName|**HasResolution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_hasresolution`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_hasresolution`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_helplink"></a> msdyn_helplink

|Property|Value|
|---|---|
|Description||
|DisplayName|**Help Link**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_helplink`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_Level"></a> msdyn_Level

|Property|Value|
|---|---|
|Description||
|DisplayName|**Level**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_level`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_level`|

#### msdyn_Level Choices/Options

|Value|Label|
|---|---|
|192350000|**Error**|
|192350001|**Warning**|

### <a name="BKMK_msdyn_Line"></a> msdyn_Line

|Property|Value|
|---|---|
|Description||
|DisplayName|**Line**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_line`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_msdyn_Member"></a> msdyn_Member

|Property|Value|
|---|---|
|Description||
|DisplayName|**Member**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_member`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

### <a name="BKMK_msdyn_Message"></a> msdyn_Message

|Property|Value|
|---|---|
|Description||
|DisplayName|**Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_message`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_MessageArguments"></a> msdyn_MessageArguments

|Property|Value|
|---|---|
|Description||
|DisplayName|**Message Arguments**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_messagearguments`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_MessageId"></a> msdyn_MessageId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Message Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_messageid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_Module"></a> msdyn_Module

|Property|Value|
|---|---|
|Description||
|DisplayName|**Module**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_module`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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

### <a name="BKMK_msdyn_RepairIssueType"></a> msdyn_RepairIssueType

|Property|Value|
|---|---|
|Description|**Type of issue that needs to be repaired. Same as IssueType Input Parameter for Solution Health Rule.**|
|DisplayName|**Repair Issue Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_repairissuetype`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_msdyn_ReturnStatus"></a> msdyn_ReturnStatus

|Property|Value|
|---|---|
|Description|**The return status of a rule run: pass, fail, or configuration error**|
|DisplayName|**Return Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_returnstatus`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_returnstatus`|

#### msdyn_ReturnStatus Choices/Options

|Value|Label|
|---|---|
|192350000|**Pass**|
|192350001|**Fail**|
|192350002|**Config Error**|
|192350003|**Resolved**|
|192350004|**Warning**|
|192350005|**Error**|
|192350006|**Suggestion**|

### <a name="BKMK_msdyn_RuleId"></a> msdyn_RuleId

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rule Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_ruleid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_RuleReferenceUri"></a> msdyn_RuleReferenceUri

|Property|Value|
|---|---|
|Description||
|DisplayName|**Rule Reference Uri**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_rulereferenceuri`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_msdyn_Severity"></a> msdyn_Severity

|Property|Value|
|---|---|
|Description||
|DisplayName|**Severity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_severity`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`msdyn_analysisresult_msdyn_severity`|

#### msdyn_Severity Choices/Options

|Value|Label|
|---|---|
|192350000|**Low**|
|192350001|**Medium**|
|192350002|**High**|
|192350003|**Critical**|

### <a name="BKMK_msdyn_Snippet"></a> msdyn_Snippet

|Property|Value|
|---|---|
|Description||
|DisplayName|**Snippet**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_snippet`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_msdyn_SolutionHealthMessage"></a> msdyn_SolutionHealthMessage

|Property|Value|
|---|---|
|Description||
|DisplayName|**Message**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_solutionhealthmessage`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8000|

### <a name="BKMK_msdyn_Type"></a> msdyn_Type

|Property|Value|
|---|---|
|Description||
|DisplayName|**Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_type`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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
|Description|**Status of the Analysis Result**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_analysisresult_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Analysis Result**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_analysisresult_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

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

- [business_unit_msdyn_analysisresult](#BKMK_business_unit_msdyn_analysisresult)
- [lk_msdyn_analysisresult_createdby](#BKMK_lk_msdyn_analysisresult_createdby)
- [lk_msdyn_analysisresult_createdonbehalfby](#BKMK_lk_msdyn_analysisresult_createdonbehalfby)
- [lk_msdyn_analysisresult_modifiedby](#BKMK_lk_msdyn_analysisresult_modifiedby)
- [lk_msdyn_analysisresult_modifiedonbehalfby](#BKMK_lk_msdyn_analysisresult_modifiedonbehalfby)
- [msdyn_analysiscomponent_msdyn_analysisresult](#BKMK_msdyn_analysiscomponent_msdyn_analysisresult)
- [msdyn_analysisjob_msdyn_analysisresult](#BKMK_msdyn_analysisjob_msdyn_analysisresult)
- [owner_msdyn_analysisresult](#BKMK_owner_msdyn_analysisresult)
- [team_msdyn_analysisresult](#BKMK_team_msdyn_analysisresult)
- [user_msdyn_analysisresult](#BKMK_user_msdyn_analysisresult)

### <a name="BKMK_business_unit_msdyn_analysisresult"></a> business_unit_msdyn_analysisresult

One-To-Many Relationship: [businessunit business_unit_msdyn_analysisresult](businessunit.md#BKMK_business_unit_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisresult_createdby"></a> lk_msdyn_analysisresult_createdby

One-To-Many Relationship: [systemuser lk_msdyn_analysisresult_createdby](systemuser.md#BKMK_lk_msdyn_analysisresult_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisresult_createdonbehalfby"></a> lk_msdyn_analysisresult_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_analysisresult_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_analysisresult_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisresult_modifiedby"></a> lk_msdyn_analysisresult_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_analysisresult_modifiedby](systemuser.md#BKMK_lk_msdyn_analysisresult_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_analysisresult_modifiedonbehalfby"></a> lk_msdyn_analysisresult_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_analysisresult_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_analysisresult_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysiscomponent_msdyn_analysisresult"></a> msdyn_analysiscomponent_msdyn_analysisresult

One-To-Many Relationship: [msdyn_analysiscomponent msdyn_analysiscomponent_msdyn_analysisresult](msdyn_analysiscomponent.md#BKMK_msdyn_analysiscomponent_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysiscomponent`|
|ReferencedAttribute|`msdyn_analysiscomponentid`|
|ReferencingAttribute|`msdyn_analysiscomponentid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AnalysisComponentId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_msdyn_analysisjob_msdyn_analysisresult"></a> msdyn_analysisjob_msdyn_analysisresult

One-To-Many Relationship: [msdyn_analysisjob msdyn_analysisjob_msdyn_analysisresult](msdyn_analysisjob.md#BKMK_msdyn_analysisjob_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencedEntity|`msdyn_analysisjob`|
|ReferencedAttribute|`msdyn_analysisjobid`|
|ReferencingAttribute|`msdyn_analysisjobid`|
|ReferencingEntityNavigationPropertyName|`msdyn_AnalysisJobId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_owner_msdyn_analysisresult"></a> owner_msdyn_analysisresult

One-To-Many Relationship: [owner owner_msdyn_analysisresult](owner.md#BKMK_owner_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_analysisresult"></a> team_msdyn_analysisresult

One-To-Many Relationship: [team team_msdyn_analysisresult](team.md#BKMK_team_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_analysisresult"></a> user_msdyn_analysisresult

One-To-Many Relationship: [systemuser user_msdyn_analysisresult](systemuser.md#BKMK_user_msdyn_analysisresult)

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

- [msdyn_analysisresult_AsyncOperations](#BKMK_msdyn_analysisresult_AsyncOperations)
- [msdyn_analysisresult_BulkDeleteFailures](#BKMK_msdyn_analysisresult_BulkDeleteFailures)
- [msdyn_analysisresult_DuplicateBaseRecord](#BKMK_msdyn_analysisresult_DuplicateBaseRecord)
- [msdyn_analysisresult_DuplicateMatchingRecord](#BKMK_msdyn_analysisresult_DuplicateMatchingRecord)
- [msdyn_analysisresult_MailboxTrackingFolders](#BKMK_msdyn_analysisresult_MailboxTrackingFolders)
- [msdyn_analysisresult_PrincipalObjectAttributeAccesses](#BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses)
- [msdyn_analysisresult_ProcessSession](#BKMK_msdyn_analysisresult_ProcessSession)
- [msdyn_analysisresult_SyncErrors](#BKMK_msdyn_analysisresult_SyncErrors)
- [msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult](#BKMK_msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult)

### <a name="BKMK_msdyn_analysisresult_AsyncOperations"></a> msdyn_analysisresult_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_analysisresult_AsyncOperations](asyncoperation.md#BKMK_msdyn_analysisresult_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_BulkDeleteFailures"></a> msdyn_analysisresult_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_analysisresult_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_analysisresult_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_DuplicateBaseRecord"></a> msdyn_analysisresult_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_analysisresult_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_analysisresult_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_DuplicateMatchingRecord"></a> msdyn_analysisresult_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_analysisresult_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_analysisresult_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_MailboxTrackingFolders"></a> msdyn_analysisresult_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_analysisresult_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_analysisresult_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses"></a> msdyn_analysisresult_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_analysisresult_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_analysisresult_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_ProcessSession"></a> msdyn_analysisresult_ProcessSession

Many-To-One Relationship: [processsession msdyn_analysisresult_ProcessSession](processsession.md#BKMK_msdyn_analysisresult_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_analysisresult_SyncErrors"></a> msdyn_analysisresult_SyncErrors

Many-To-One Relationship: [syncerror msdyn_analysisresult_SyncErrors](syncerror.md#BKMK_msdyn_analysisresult_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_analysisresult_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult"></a> msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult

Many-To-One Relationship: [msdyn_analysisresultdetail msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult](msdyn_analysisresultdetail.md#BKMK_msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresultdetail`|
|ReferencingAttribute|`msdyn_analysisresult`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_analysisresult_msdyn_analysisresultdetail_AnalysisResult`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_analysisresult?displayProperty=fullName>
