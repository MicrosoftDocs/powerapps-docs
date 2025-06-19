---
title: "PM Inferred Task (msdyn_pminferredtask) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the PM Inferred Task (msdyn_pminferredtask) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# PM Inferred Task (msdyn_pminferredtask) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the PM Inferred Task (msdyn_pminferredtask) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Analyze`<br />Event: False |<xref:Microsoft.Dynamics.CRM.Analyze?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Assign`<br />Event: True |`PATCH` /msdyn_pminferredtasks(*msdyn_pminferredtaskid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `ownerid` property. |<xref:Microsoft.Crm.Sdk.Messages.AssignRequest>|
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_pminferredtasks<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_pminferredtasks(*msdyn_pminferredtaskid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `GrantAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.GrantAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest>|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `ModifyAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.ModifyAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest>|
| `Retrieve`<br />Event: False |`GET` /msdyn_pminferredtasks(*msdyn_pminferredtaskid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /msdyn_pminferredtasks<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrievePrincipalAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest>|
| `RetrieveSharedPrincipalsAndAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest>|
| `RevokeAccess`<br />Event: True |<xref:Microsoft.Dynamics.CRM.RevokeAccess?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest>|
| `SetState`<br />Event: True |`PATCH` /msdyn_pminferredtasks(*msdyn_pminferredtaskid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Share`<br />Event: False |<xref:Microsoft.Dynamics.CRM.Share?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Update`<br />Event: True |`PATCH` /msdyn_pminferredtasks(*msdyn_pminferredtaskid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /msdyn_pminferredtasks(*msdyn_pminferredtaskid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|


## Events

The following table lists the events for the PM Inferred Task (msdyn_pminferredtask) table.
Events are messages that exist so that you can subscribe to them. Unless you added the event, you shouldn't invoke the message, only subscribe to it.

|Name|Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `BulkRetain`|<xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `PurgeRetainedContent`|<xref:Microsoft.Dynamics.CRM.PurgeRetainedContent?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Retain`|<xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `RollbackRetain`|<xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `ValidateRetentionConfig`|<xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|

## Properties

The following table lists selected properties for the PM Inferred Task (msdyn_pminferredtask) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **PM Inferred Task** |
| **DisplayCollectionName** | **PM Inferred Tasks** |
| **SchemaName** | `msdyn_pminferredtask` |
| **CollectionSchemaName** | `msdyn_pminferredtasks` |
| **EntitySetName** | `msdyn_pminferredtasks`|
| **LogicalName** | `msdyn_pminferredtask` |
| **LogicalCollectionName** | `msdyn_pminferredtasks` |
| **PrimaryIdAttribute** | `msdyn_pminferredtaskid` |
| **PrimaryNameAttribute** |`msdyn_name` |
| **TableType** | `Standard` |
| **OwnershipType** | `UserOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [msdyn_analysisschedule](#BKMK_msdyn_analysisschedule)
- [msdyn_automationdata](#BKMK_msdyn_automationdata)
- [msdyn_automationstatus](#BKMK_msdyn_automationstatus)
- [msdyn_datavalidation](#BKMK_msdyn_datavalidation)
- [msdyn_description](#BKMK_msdyn_description)
- [msdyn_inputdatabinding](#BKMK_msdyn_inputdatabinding)
- [msdyn_isreportavailable](#BKMK_msdyn_isreportavailable)
- [msdyn_iterationid](#BKMK_msdyn_iterationid)
- [msdyn_lasterrors](#BKMK_msdyn_lasterrors)
- [msdyn_lastreportrefreshdate](#BKMK_msdyn_lastreportrefreshdate)
- [msdyn_name](#BKMK_msdyn_name)
- [msdyn_outputdata](#BKMK_msdyn_outputdata)
- [msdyn_pminferredtaskId](#BKMK_msdyn_pminferredtaskId)
- [msdyn_reportdata](#BKMK_msdyn_reportdata)
- [msdyn_reportprovisioningstatus](#BKMK_msdyn_reportprovisioningstatus)
- [msdyn_sharedrecordingmetadata](#BKMK_msdyn_sharedrecordingmetadata)
- [msdyn_source](#BKMK_msdyn_source)
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

### <a name="BKMK_IsCustomizable"></a> IsCustomizable

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Customizable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`iscustomizable`|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|

### <a name="BKMK_msdyn_analysisschedule"></a> msdyn_analysisschedule

|Property|Value|
|---|---|
|Description|**Information about the analysis schedule.**|
|DisplayName|**Analysis Schedule**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_analysisschedule`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_automationdata"></a> msdyn_automationdata

|Property|Value|
|---|---|
|Description|**Computed data to drive automation for this task.**|
|DisplayName|**AutomationData**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_automationdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_automationstatus"></a> msdyn_automationstatus

|Property|Value|
|---|---|
|Description|**The status of automation for this task.**|
|DisplayName|**AutomationStatus**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_automationstatus`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|200000000|
|GlobalChoiceName|`msdyn_pminferredtask_msdyn_automationstatus`|

#### msdyn_automationstatus Choices/Options

|Value|Label|
|---|---|
|200000000|**NotStarted**|
|200000001|**NotRecommended**|
|200000002|**InProgress**|
|200000003|**Complete**|

### <a name="BKMK_msdyn_datavalidation"></a> msdyn_datavalidation

|Property|Value|
|---|---|
|Description|**Information about the data validation for the data source.**|
|DisplayName|**Data Validation**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_datavalidation`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_description"></a> msdyn_description

|Property|Value|
|---|---|
|Description||
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_inputdatabinding"></a> msdyn_inputdatabinding

|Property|Value|
|---|---|
|Description|**Location of the data used as input for Task Analysis.**|
|DisplayName|**Input Data Location**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_inputdatabinding`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_isreportavailable"></a> msdyn_isreportavailable

|Property|Value|
|---|---|
|Description|**Surfaces whether the analysis report is currently available.**|
|DisplayName|**Is Report Available**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_isreportavailable`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`msdyn_pminferredtask_msdyn_isreportavailable`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_msdyn_iterationid"></a> msdyn_iterationid

|Property|Value|
|---|---|
|Description|**Identifies uniquely the last successful processing of the task.**|
|DisplayName|**Processing Iteration Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_iterationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_msdyn_lasterrors"></a> msdyn_lasterrors

|Property|Value|
|---|---|
|Description||
|DisplayName|**Last Errors**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lasterrors`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100000|

### <a name="BKMK_msdyn_lastreportrefreshdate"></a> msdyn_lastreportrefreshdate

|Property|Value|
|---|---|
|Description|**Date and time when the corresponding report was last refreshed.**|
|DisplayName|**Last Report Refresh Date**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lastreportrefreshdate`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|TimeZoneIndependent|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

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

### <a name="BKMK_msdyn_outputdata"></a> msdyn_outputdata

|Property|Value|
|---|---|
|Description||
|DisplayName|**Output Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_outputdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_pminferredtaskId"></a> msdyn_pminferredtaskId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**PM Inferred Task**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_pminferredtaskid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_reportdata"></a> msdyn_reportdata

|Property|Value|
|---|---|
|Description|**Data related to the report for this task.**|
|DisplayName|**Report Data**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_reportdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10000|

### <a name="BKMK_msdyn_reportprovisioningstatus"></a> msdyn_reportprovisioningstatus

|Property|Value|
|---|---|
|Description|**The current status of the provisioning operation for the report associated to this task.**|
|DisplayName|**Report Provisioning Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_reportprovisioningstatus`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|193350000|
|GlobalChoiceName|`msdyn_pminferredtask_msdyn_reportprovisioningstatus`|

#### msdyn_reportprovisioningstatus Choices/Options

|Value|Label|
|---|---|
|193350000|**NotStarted**|
|193350001|**Provisioning**|
|193350002|**Provisioned**|
|193350003|**Failed**|
|193350004|**Skipped**|

### <a name="BKMK_msdyn_sharedrecordingmetadata"></a> msdyn_sharedrecordingmetadata

|Property|Value|
|---|---|
|Description||
|DisplayName|**Shared Recording Metadata**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_sharedrecordingmetadata`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1048576|

### <a name="BKMK_msdyn_source"></a> msdyn_source

|Property|Value|
|---|---|
|Description|**The data source of this Pm Inferred Task.**|
|DisplayName|**Pm Inferred Task Source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_source`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`msdyn_pminferredtask_msdyn_source`|

#### msdyn_source Choices/Options

|Value|Label|
|---|---|
|0|**Recording**|
|1|**DataLake**|
|2|**ObjectCentric**|

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
|Description|**Status of the PM Inferred Task**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_pminferredtask_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />DefaultStatus: 0<br />InvariantName: `Draft`|
|1|Label: **InProgress**<br />DefaultStatus: 1<br />InvariantName: `InProgress`|
|2|Label: **Done**<br />DefaultStatus: 4<br />InvariantName: `Done`|
|3|Label: **Failed**<br />DefaultStatus: 5<br />InvariantName: `Failed`|
|4|Label: **Imported**<br />DefaultStatus: 7<br />InvariantName: `Imported`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the PM Inferred Task**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`msdyn_pminferredtask_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Draft**<br />State:0<br />TransitionData: None|
|1|Label: **Queued**<br />State:1<br />TransitionData: None|
|2|Label: **Analyzing**<br />State:1<br />TransitionData: None|
|3|Label: **Deleting**<br />State:1<br />TransitionData: None|
|4|Label: **Analyzed**<br />State:2<br />TransitionData: None|
|5|Label: **AnalyzeFailed**<br />State:3<br />TransitionData: None|
|6|Label: **DeleteFailed**<br />State:3<br />TransitionData: None|
|7|Label: **Imported**<br />State:4<br />TransitionData: None|

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

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [msdyn_lasterrorsreport](#BKMK_msdyn_lasterrorsreport)
- [msdyn_lasterrorsreport_Name](#BKMK_msdyn_lasterrorsreport_Name)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Row id unique**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`componentidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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
|DefaultFormValue||
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

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Indicates whether the solution component is part of a managed solution.**|
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

### <a name="BKMK_msdyn_lasterrorsreport"></a> msdyn_lasterrorsreport

|Property|Value|
|---|---|
|Description||
|DisplayName|**Last Errors Report**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lasterrorsreport`|
|RequiredLevel|None|
|Type|File|
|MaxSizeInKB|32768|

### <a name="BKMK_msdyn_lasterrorsreport_Name"></a> msdyn_lasterrorsreport_Name

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_lasterrorsreport_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

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

- [business_unit_msdyn_pminferredtask](#BKMK_business_unit_msdyn_pminferredtask)
- [FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport](#BKMK_FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport)
- [lk_msdyn_pminferredtask_createdby](#BKMK_lk_msdyn_pminferredtask_createdby)
- [lk_msdyn_pminferredtask_createdonbehalfby](#BKMK_lk_msdyn_pminferredtask_createdonbehalfby)
- [lk_msdyn_pminferredtask_modifiedby](#BKMK_lk_msdyn_pminferredtask_modifiedby)
- [lk_msdyn_pminferredtask_modifiedonbehalfby](#BKMK_lk_msdyn_pminferredtask_modifiedonbehalfby)
- [owner_msdyn_pminferredtask](#BKMK_owner_msdyn_pminferredtask)
- [team_msdyn_pminferredtask](#BKMK_team_msdyn_pminferredtask)
- [user_msdyn_pminferredtask](#BKMK_user_msdyn_pminferredtask)

### <a name="BKMK_business_unit_msdyn_pminferredtask"></a> business_unit_msdyn_pminferredtask

One-To-Many Relationship: [businessunit business_unit_msdyn_pminferredtask](businessunit.md#BKMK_business_unit_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencingEntityNavigationPropertyName|`owningbusinessunit`|
|IsHierarchical||
|CascadeConfiguration|Archive: `Restrict`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport"></a> FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport

One-To-Many Relationship: [fileattachment FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport](fileattachment.md#BKMK_FileAttachment_msdyn_pminferredtask_msdyn_lasterrorsreport)

|Property|Value|
|---|---|
|ReferencedEntity|`fileattachment`|
|ReferencedAttribute|`fileattachmentid`|
|ReferencingAttribute|`msdyn_lasterrorsreport`|
|ReferencingEntityNavigationPropertyName|`msdyn_lasterrorsreport`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_pminferredtask_createdby"></a> lk_msdyn_pminferredtask_createdby

One-To-Many Relationship: [systemuser lk_msdyn_pminferredtask_createdby](systemuser.md#BKMK_lk_msdyn_pminferredtask_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_pminferredtask_createdonbehalfby"></a> lk_msdyn_pminferredtask_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_pminferredtask_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_pminferredtask_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_pminferredtask_modifiedby"></a> lk_msdyn_pminferredtask_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_pminferredtask_modifiedby](systemuser.md#BKMK_lk_msdyn_pminferredtask_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_pminferredtask_modifiedonbehalfby"></a> lk_msdyn_pminferredtask_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_pminferredtask_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_pminferredtask_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_owner_msdyn_pminferredtask"></a> owner_msdyn_pminferredtask

One-To-Many Relationship: [owner owner_msdyn_pminferredtask](owner.md#BKMK_owner_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencedEntity|`owner`|
|ReferencedAttribute|`ownerid`|
|ReferencingAttribute|`ownerid`|
|ReferencingEntityNavigationPropertyName|`ownerid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_team_msdyn_pminferredtask"></a> team_msdyn_pminferredtask

One-To-Many Relationship: [team team_msdyn_pminferredtask](team.md#BKMK_team_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencedEntity|`team`|
|ReferencedAttribute|`teamid`|
|ReferencingAttribute|`owningteam`|
|ReferencingEntityNavigationPropertyName|`owningteam`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_user_msdyn_pminferredtask"></a> user_msdyn_pminferredtask

One-To-Many Relationship: [systemuser user_msdyn_pminferredtask](systemuser.md#BKMK_user_msdyn_pminferredtask)

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

- [flowcapacityassignment_msdyn_pminferredtask](#BKMK_flowcapacityassignment_msdyn_pminferredtask)
- [msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask](#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask)
- [msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId](#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId)
- [msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid](#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid)
- [msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask](#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask)
- [msdyn_pminferredtask_AsyncOperations](#BKMK_msdyn_pminferredtask_AsyncOperations)
- [msdyn_pminferredtask_BulkDeleteFailures](#BKMK_msdyn_pminferredtask_BulkDeleteFailures)
- [msdyn_pminferredtask_DuplicateBaseRecord](#BKMK_msdyn_pminferredtask_DuplicateBaseRecord)
- [msdyn_pminferredtask_DuplicateMatchingRecord](#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord)
- [msdyn_pminferredtask_FileAttachments](#BKMK_msdyn_pminferredtask_FileAttachments)
- [msdyn_pminferredtask_MailboxTrackingFolders](#BKMK_msdyn_pminferredtask_MailboxTrackingFolders)
- [msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask](#BKMK_msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask)
- [msdyn_pminferredtask_msdyn_pmprocessversion](#BKMK_msdyn_pminferredtask_msdyn_pmprocessversion)
- [msdyn_pminferredtask_PrincipalObjectAttributeAccesses](#BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses)
- [msdyn_pminferredtask_ProcessSession](#BKMK_msdyn_pminferredtask_ProcessSession)
- [msdyn_pminferredtask_SyncErrors](#BKMK_msdyn_pminferredtask_SyncErrors)
- [msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask](#BKMK_msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask)

### <a name="BKMK_flowcapacityassignment_msdyn_pminferredtask"></a> flowcapacityassignment_msdyn_pminferredtask

Many-To-One Relationship: [flowcapacityassignment flowcapacityassignment_msdyn_pminferredtask](flowcapacityassignment.md#BKMK_flowcapacityassignment_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`regarding`|
|ReferencedEntityNavigationPropertyName|`flowcapacityassignment_msdyn_pminferredtask`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask"></a> msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask

Many-To-One Relationship: [msdyn_pmanalysishistory msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask](msdyn_pmanalysishistory.md#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmanalysishistory`|
|ReferencingAttribute|`msdyn_parenttask`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_pminferredtask_msdyn_pmanalysishistory_parenttask`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId"></a> msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId

Many-To-One Relationship: [msdyn_pmbusinessruleautomationconfig msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId](msdyn_pmbusinessruleautomationconfig.md#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencingAttribute|`msdyn_pminferredtaskid`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_pminferredtask_msdyn_pmbusinessruleautomationconfig_PMInferredTaskId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid"></a> msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid

Many-To-One Relationship: [msdyn_pmprocesstemplate msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid](msdyn_pmprocesstemplate.md#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocesstemplate`|
|ReferencingAttribute|`msdyn_pminferredtaskid`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_pminferredtask_msdyn_pmprocesstemplate_pmnferredtaskid`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask"></a> msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask

Many-To-One Relationship: [msdyn_pmrecording msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask](msdyn_pmrecording.md#BKMK_msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmrecording`|
|ReferencingAttribute|`msdyn_parenttask`|
|ReferencedEntityNavigationPropertyName|`msdyn_msdyn_pminferredtask_msdyn_pmrecording_parenttask`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_AsyncOperations"></a> msdyn_pminferredtask_AsyncOperations

Many-To-One Relationship: [asyncoperation msdyn_pminferredtask_AsyncOperations](asyncoperation.md#BKMK_msdyn_pminferredtask_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_BulkDeleteFailures"></a> msdyn_pminferredtask_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure msdyn_pminferredtask_BulkDeleteFailures](bulkdeletefailure.md#BKMK_msdyn_pminferredtask_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_DuplicateBaseRecord"></a> msdyn_pminferredtask_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord msdyn_pminferredtask_DuplicateBaseRecord](duplicaterecord.md#BKMK_msdyn_pminferredtask_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_DuplicateMatchingRecord"></a> msdyn_pminferredtask_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord msdyn_pminferredtask_DuplicateMatchingRecord](duplicaterecord.md#BKMK_msdyn_pminferredtask_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_FileAttachments"></a> msdyn_pminferredtask_FileAttachments

Many-To-One Relationship: [fileattachment msdyn_pminferredtask_FileAttachments](fileattachment.md#BKMK_msdyn_pminferredtask_FileAttachments)

|Property|Value|
|---|---|
|ReferencingEntity|`fileattachment`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_FileAttachments`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_MailboxTrackingFolders"></a> msdyn_pminferredtask_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder msdyn_pminferredtask_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_msdyn_pminferredtask_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask"></a> msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask

Many-To-One Relationship: [msdyn_pmprocessusersettings msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask](msdyn_pmprocessusersettings.md#BKMK_msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessusersettings`|
|ReferencingAttribute|`msdyn_parenttask`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_msdyn_pmprocessusersettings_parenttask`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_msdyn_pmprocessversion"></a> msdyn_pminferredtask_msdyn_pmprocessversion

Many-To-One Relationship: [msdyn_pmprocessversion msdyn_pminferredtask_msdyn_pmprocessversion](msdyn_pmprocessversion.md#BKMK_msdyn_pminferredtask_msdyn_pmprocessversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessversion`|
|ReferencingAttribute|`msdyn_pminferredtaskid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_msdyn_pmprocessversion`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses"></a> msdyn_pminferredtask_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess msdyn_pminferredtask_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_msdyn_pminferredtask_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_ProcessSession"></a> msdyn_pminferredtask_ProcessSession

Many-To-One Relationship: [processsession msdyn_pminferredtask_ProcessSession](processsession.md#BKMK_msdyn_pminferredtask_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pminferredtask_SyncErrors"></a> msdyn_pminferredtask_SyncErrors

Many-To-One Relationship: [syncerror msdyn_pminferredtask_SyncErrors](syncerror.md#BKMK_msdyn_pminferredtask_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pminferredtask_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask"></a> msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask

Many-To-One Relationship: [msdyn_pmsimulation msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask](msdyn_pmsimulation.md#BKMK_msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmsimulation`|
|ReferencingAttribute|`msdyn_pminferredtaskid`|
|ReferencedEntityNavigationPropertyName|`msdyn_pmsimulation_pminferredtaskid_msdyn_pminferredtask`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.msdyn_pminferredtask?displayProperty=fullName>
