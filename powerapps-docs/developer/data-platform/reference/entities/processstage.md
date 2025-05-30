---
title: "Process Stage (ProcessStage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Process Stage (ProcessStage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Process Stage (ProcessStage) table/entity reference (Microsoft Dataverse)

Stage associated with a process.

## Messages

The following table lists the messages for the Process Stage (ProcessStage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /processstages<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /processstages(*processstageid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /processstages(*processstageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveActivePath`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveActivePath?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveActivePathRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /processstages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Process Stage (ProcessStage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Process Stage** |
| **DisplayCollectionName** | **Process Stages** |
| **SchemaName** | `ProcessStage` |
| **CollectionSchemaName** | `ProcessStages` |
| **EntitySetName** | `processstages`|
| **LogicalName** | `processstage` |
| **LogicalCollectionName** | `processstages` |
| **PrimaryIdAttribute** | `processstageid` |
| **PrimaryNameAttribute** |`stagename` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Connector](#BKMK_Connector)
- [IsTrigger](#BKMK_IsTrigger)
- [OperationId](#BKMK_OperationId)
- [OperationKind](#BKMK_OperationKind)
- [OperationType](#BKMK_OperationType)
- [ParameterName](#BKMK_ParameterName)
- [ParameterValue](#BKMK_ParameterValue)
- [ParentProcessStageId](#BKMK_ParentProcessStageId)
- [PrimaryEntityTypeCode](#BKMK_PrimaryEntityTypeCode)
- [ProcessId](#BKMK_ProcessId)
- [ProcessStageId](#BKMK_ProcessStageId)
- [StageCategory](#BKMK_StageCategory)
- [StageName](#BKMK_StageName)

### <a name="BKMK_Connector"></a> Connector

|Property|Value|
|---|---|
|Description|**The connector associated with the stage.**|
|DisplayName|**Connector**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`connector`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_IsTrigger"></a> IsTrigger

|Property|Value|
|---|---|
|Description|**Whether the stage is a trigger**|
|DisplayName|**Is Trigger**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`istrigger`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`processstage_istrigger`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_OperationId"></a> OperationId

|Property|Value|
|---|---|
|Description|**The operation id of the stage**|
|DisplayName|**Operation Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_OperationKind"></a> OperationKind

|Property|Value|
|---|---|
|Description|**The operation kind**|
|DisplayName|**Operation Kind**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationkind`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`processstage_operationkind`|

#### OperationKind Choices/Options

|Value|Label|
|---|---|
|473330000|**Http**|
|473330001|**PowerApp**|
|473330002|**PowerAppV2**|
|473330003|**Button**|
|473330004|**ApiConnection**|
|473330005|**Alert**|
|473330006|**EventGrid**|
|473330007|**CurrentTime**|
|473330008|**ConvertTimeZone**|
|473330009|**GetFutureTime**|
|473330010|**GetPastTime**|
|473330011|**AddToTime**|
|473330012|**SubtractFromTime**|
|473330013|**AzureMonitorAlert**|
|473330014|**SecurityCenterAlert**|
|473330015|**JsonToJson**|
|473330016|**JsonToText**|
|473330017|**XmlToJson**|
|473330018|**XmlToText**|
|473330019|**Geofence**|
|473330020|**ODataOpenApiConnection**|
|473330021|**IndexOf**|
|473330022|**Substring**|
|473330023|**VirtualAgent**|
|473330024|**FormatNumber**|
|473330025|**Skills**|
|473330026|**PowerPages**|
|473330027|**TeamsWebhook**|

### <a name="BKMK_OperationType"></a> OperationType

|Property|Value|
|---|---|
|Description|**The type of the operation**|
|DisplayName|**Operation Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operationtype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`processstage_operationtype`|

#### OperationType Choices/Options

|Value|Label|
|---|---|
|473330000|**Http**|
|473330001|**ApiApp**|
|473330002|**Recurrence**|
|473330003|**Workflow**|
|473330004|**Flow**|
|473330005|**Wait**|
|473330006|**ApiConnection**|
|473330007|**OpenApiConnection**|
|473330008|**Manual**|
|473330009|**ApiConnectionWebhook**|
|473330010|**OpenApiConnectionWebhook**|
|473330011|**Response**|
|473330012|**HttpWebhook**|
|473330013|**Compose**|
|473330014|**Query**|
|473330015|**Function**|
|473330016|**ApiManagement**|
|473330017|**XmlValidation**|
|473330018|**FlatFileEncoding**|
|473330019|**Scope**|
|473330020|**Request**|
|473330021|**If**|
|473330022|**Foreach**|
|473330023|**Until**|
|473330024|**Xslt**|
|473330025|**FlatFileDecoding**|
|473330026|**Terminate**|
|473330027|**IntegrationAccountArtifactLookup**|
|473330028|**Switch**|
|473330029|**ParseJson**|
|473330030|**Table**|
|473330031|**Join**|
|473330032|**Select**|
|473330033|**InitializeVariable**|
|473330034|**IncrementVariable**|
|473330035|**DecrementVariable**|
|473330036|**SetVariable**|
|473330037|**AppendToArrayVariable**|
|473330038|**AppendToStringVariable**|
|473330039|**Batch**|
|473330040|**SendToBatch**|
|473330041|**SlidingWindow**|
|473330042|**Expression**|
|473330043|**Liquid**|
|473330044|**JavascriptCode**|
|473330045|**As2Decode**|
|473330046|**As2Encode**|
|473330047|**RosettaNetEncode**|
|473330048|**RosettaNetDecode**|
|473330049|**RosettaNetWaitForResponse**|
|473330050|**ApiConnectionNotification**|
|473330051|**Changeset**|
|473330052|**SwiftEncode**|

### <a name="BKMK_ParameterName"></a> ParameterName

|Property|Value|
|---|---|
|Description|**The parameter name.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parametername`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_ParameterValue"></a> ParameterValue

|Property|Value|
|---|---|
|Description|**The parameter value.**|
|DisplayName|**Value**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parametervalue`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_ParentProcessStageId"></a> ParentProcessStageId

|Property|Value|
|---|---|
|Description|**The parent stage for the parameter.**|
|DisplayName|**Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentprocessstageid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|processstage|

### <a name="BKMK_PrimaryEntityTypeCode"></a> PrimaryEntityTypeCode

|Property|Value|
|---|---|
|Description|**Primary entity associated with the stage.**|
|DisplayName|**Primary Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryentitytypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_ProcessStageId"></a> ProcessStageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process stage record.**|
|DisplayName|**Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processstageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_StageCategory"></a> StageCategory

|Property|Value|
|---|---|
|Description|**Select the category of the sales process.**|
|DisplayName|**Stage Category**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagecategory`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`processstage_category`|

#### StageCategory Choices/Options

|Value|Label|
|---|---|
|0|**Qualify**|
|1|**Develop**|
|2|**Propose**|
|3|**Close**|
|4|**Identify**|
|5|**Research**|
|6|**Resolve**|
|7|**Approval**|

### <a name="BKMK_StageName"></a> StageName

|Property|Value|
|---|---|
|Description|**Type a name for the process stage.**|
|DisplayName|**Process Stage Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stagename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ClientData](#BKMK_ClientData)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_ClientData"></a> ClientData

|Property|Value|
|---|---|
|Description|**Step metadata for process stage**|
|DisplayName|**Client Data**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`clientdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
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

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Select the business unit that owns the record.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the process stage.**|
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

- [process_processstage](#BKMK_process_processstage)
- [processstage_parentprocessstage](#BKMK_processstage_parentprocessstage-many-to-one)

### <a name="BKMK_process_processstage"></a> process_processstage

One-To-Many Relationship: [workflow process_processstage](workflow.md#BKMK_process_processstage)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`processid`|
|ReferencingEntityNavigationPropertyName|`processid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_processstage_parentprocessstage-many-to-one"></a> processstage_parentprocessstage

One-To-Many Relationship: [processstage processstage_parentprocessstage](#BKMK_processstage_parentprocessstage-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`parentprocessstageid`|
|ReferencingEntityNavigationPropertyName|`ParentProcessStageId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [lk_expiredprocess_activestageid](#BKMK_lk_expiredprocess_activestageid)
- [lk_newprocess_activestageid](#BKMK_lk_newprocess_activestageid)
- [lk_translationprocess_activestageid](#BKMK_lk_translationprocess_activestageid)
- [processstage_account](#BKMK_processstage_account)
- [processstage_adx_portalcomment](#BKMK_processstage_adx_portalcomment)
- [processstage_appointments](#BKMK_processstage_appointments)
- [processstage_contact](#BKMK_processstage_contact)
- [processstage_emails](#BKMK_processstage_emails)
- [processstage_faxes](#BKMK_processstage_faxes)
- [processstage_knowledgearticle](#BKMK_processstage_knowledgearticle)
- [processstage_letters](#BKMK_processstage_letters)
- [processstage_parentprocessstage](#BKMK_processstage_parentprocessstage-one-to-many)
- [processstage_phonecalls](#BKMK_processstage_phonecalls)
- [processstage_processstageparameter](#BKMK_processstage_processstageparameter)
- [processstage_recurringappointmentmasters](#BKMK_processstage_recurringappointmentmasters)
- [ProcessStage_SyncErrors](#BKMK_ProcessStage_SyncErrors)
- [processstage_systemusers](#BKMK_processstage_systemusers)
- [processstage_tasks](#BKMK_processstage_tasks)
- [processstage_teams](#BKMK_processstage_teams)

### <a name="BKMK_lk_expiredprocess_activestageid"></a> lk_expiredprocess_activestageid

Many-To-One Relationship: [expiredprocess lk_expiredprocess_activestageid](expiredprocess.md#BKMK_lk_expiredprocess_activestageid)

|Property|Value|
|---|---|
|ReferencingEntity|`expiredprocess`|
|ReferencingAttribute|`activestageid`|
|ReferencedEntityNavigationPropertyName|`processstage_expiredprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_newprocess_activestageid"></a> lk_newprocess_activestageid

Many-To-One Relationship: [newprocess lk_newprocess_activestageid](newprocess.md#BKMK_lk_newprocess_activestageid)

|Property|Value|
|---|---|
|ReferencingEntity|`newprocess`|
|ReferencingAttribute|`activestageid`|
|ReferencedEntityNavigationPropertyName|`processstage_newprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_lk_translationprocess_activestageid"></a> lk_translationprocess_activestageid

Many-To-One Relationship: [translationprocess lk_translationprocess_activestageid](translationprocess.md#BKMK_lk_translationprocess_activestageid)

|Property|Value|
|---|---|
|ReferencingEntity|`translationprocess`|
|ReferencingAttribute|`activestageid`|
|ReferencedEntityNavigationPropertyName|`processstage_translationprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_account"></a> processstage_account

Many-To-One Relationship: [account processstage_account](account.md#BKMK_processstage_account)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_account`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_adx_portalcomment"></a> processstage_adx_portalcomment

Many-To-One Relationship: [adx_portalcomment processstage_adx_portalcomment](adx_portalcomment.md#BKMK_processstage_adx_portalcomment)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_adx_portalcomment`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_appointments"></a> processstage_appointments

Many-To-One Relationship: [appointment processstage_appointments](appointment.md#BKMK_processstage_appointments)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_appointments`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_contact"></a> processstage_contact

Many-To-One Relationship: [contact processstage_contact](contact.md#BKMK_processstage_contact)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_contact`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_emails"></a> processstage_emails

Many-To-One Relationship: [email processstage_emails](email.md#BKMK_processstage_emails)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_emails`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_faxes"></a> processstage_faxes

Many-To-One Relationship: [fax processstage_faxes](fax.md#BKMK_processstage_faxes)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_faxes`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_knowledgearticle"></a> processstage_knowledgearticle

Many-To-One Relationship: [knowledgearticle processstage_knowledgearticle](knowledgearticle.md#BKMK_processstage_knowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_knowledgearticle`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_letters"></a> processstage_letters

Many-To-One Relationship: [letter processstage_letters](letter.md#BKMK_processstage_letters)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_letters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_parentprocessstage-one-to-many"></a> processstage_parentprocessstage

Many-To-One Relationship: [processstage processstage_parentprocessstage](#BKMK_processstage_parentprocessstage-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`processstage`|
|ReferencingAttribute|`parentprocessstageid`|
|ReferencedEntityNavigationPropertyName|`processstage_parentprocessstage`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_phonecalls"></a> processstage_phonecalls

Many-To-One Relationship: [phonecall processstage_phonecalls](phonecall.md#BKMK_processstage_phonecalls)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_phonecalls`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_processstageparameter"></a> processstage_processstageparameter

Many-To-One Relationship: [processstageparameter processstage_processstageparameter](processstageparameter.md#BKMK_processstage_processstageparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`processstageparameter`|
|ReferencingAttribute|`processstageid`|
|ReferencedEntityNavigationPropertyName|`processstage_processstageparameter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_recurringappointmentmasters"></a> processstage_recurringappointmentmasters

Many-To-One Relationship: [recurringappointmentmaster processstage_recurringappointmentmasters](recurringappointmentmaster.md#BKMK_processstage_recurringappointmentmasters)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_recurringappointmentmasters`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_ProcessStage_SyncErrors"></a> ProcessStage_SyncErrors

Many-To-One Relationship: [syncerror ProcessStage_SyncErrors](syncerror.md#BKMK_ProcessStage_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`ProcessStage_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_systemusers"></a> processstage_systemusers

Many-To-One Relationship: [systemuser processstage_systemusers](systemuser.md#BKMK_processstage_systemusers)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_systemusers`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_tasks"></a> processstage_tasks

Many-To-One Relationship: [task processstage_tasks](task.md#BKMK_processstage_tasks)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_tasks`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_processstage_teams"></a> processstage_teams

Many-To-One Relationship: [team processstage_teams](team.md#BKMK_processstage_teams)

|Property|Value|
|---|---|
|ReferencingEntity|`team`|
|ReferencingAttribute|`stageid`|
|ReferencedEntityNavigationPropertyName|`processstage_teams`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.processstage?displayProperty=fullName>
