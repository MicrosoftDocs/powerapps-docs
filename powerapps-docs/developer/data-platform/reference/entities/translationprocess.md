---
title: "Translation Process (TranslationProcess) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Translation Process (TranslationProcess) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Translation Process (TranslationProcess) table/entity reference (Microsoft Dataverse)

Translation Process Business Process Flow

## Messages

The following table lists the messages for the Translation Process (TranslationProcess) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /translationprocesses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /translationprocesses(*businessprocessflowinstanceid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /translationprocesses(*businessprocessflowinstanceid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /translationprocesses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /translationprocesses(*businessprocessflowinstanceid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /translationprocesses(*businessprocessflowinstanceid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /translationprocesses(*businessprocessflowinstanceid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Translation Process (TranslationProcess) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Translation Process** |
| **DisplayCollectionName** | **Translation Process** |
| **SchemaName** | `TranslationProcess` |
| **CollectionSchemaName** | `TranslationProcesses` |
| **EntitySetName** | `translationprocesses`|
| **LogicalName** | `translationprocess` |
| **LogicalCollectionName** | `translationprocesses` |
| **PrimaryIdAttribute** | `businessprocessflowinstanceid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ActiveStageId](#BKMK_ActiveStageId)
- [ActiveStageStartedOn](#BKMK_ActiveStageStartedOn)
- [BusinessProcessFlowInstanceId](#BKMK_BusinessProcessFlowInstanceId)
- [CompletedOn](#BKMK_CompletedOn)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [KnowledgeArticleId](#BKMK_KnowledgeArticleId)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ProcessId](#BKMK_ProcessId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)

### <a name="BKMK_ActiveStageId"></a> ActiveStageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the active stage for the Business Process Flow instance.**|
|DisplayName|**Active Stage**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activestageid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|processstage|

### <a name="BKMK_ActiveStageStartedOn"></a> ActiveStageStartedOn

|Property|Value|
|---|---|
|Description|**Date and time when current active stage is started.**|
|DisplayName|**Active Stage Started On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`activestagestartedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_BusinessProcessFlowInstanceId"></a> BusinessProcessFlowInstanceId

|Property|Value|
|---|---|
|Description|**Unique identifier for Translation Process bpf entity instances**|
|DisplayName|**Translation Process Instance Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessprocessflowinstanceid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CompletedOn"></a> CompletedOn

|Property|Value|
|---|---|
|Description|**Date and time when Business Process Flow instance is completed.**|
|DisplayName|**Completed On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`completedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|True|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_KnowledgeArticleId"></a> KnowledgeArticleId

|Property|Value|
|---|---|
|Description|**Unique identifier of the workflow associated to the Business Process Flow instance.**|
|DisplayName|**Knowledge Article**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`knowledgearticleid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|knowledgearticle|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Process Name.**|
|DisplayName|**Process Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Unique identifier of the workflow associated to the Business Process Flow instance.**|
|DisplayName|**Process**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|workflow|

### <a name="BKMK_StateCode"></a> StateCode

|Property|Value|
|---|---|
|Description|**Shows whether the Delve action record is pending, completed, or tracking.**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue|0|
|GlobalChoiceName|`translationprocess_statecode`|

#### StateCode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_StatusCode"></a> StatusCode

|Property|Value|
|---|---|
|Description|**Select the delve action record status.**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue|-1|
|GlobalChoiceName|`translationprocess_statuscode`|

#### StatusCode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Finished**<br />State:1<br />TransitionData: None|
|3|Label: **Aborted**<br />State:1<br />TransitionData: None|

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

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**Traversed Path**|
|DisplayName|**Comma delimited string of process stage ids that represent visited stages of the Business Process Flow instance.**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|1250|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [Duration](#BKMK_Duration)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [VersionNumber](#BKMK_VersionNumber)

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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.**|
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

### <a name="BKMK_Duration"></a> Duration

|Property|Value|
|---|---|
|Description|**Duration between completed on and started on, used by business process flow.**|
|DisplayName|**Duration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`duration`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics CRM options.**|
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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the SDK message request is associated.**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the business process instance.**|
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

- [lk_translationprocess_activestageid](#BKMK_lk_translationprocess_activestageid)
- [lk_translationprocess_createdby](#BKMK_lk_translationprocess_createdby)
- [lk_translationprocess_createdonbehalfby](#BKMK_lk_translationprocess_createdonbehalfby)
- [lk_translationprocess_knowledgearticleid](#BKMK_lk_translationprocess_knowledgearticleid)
- [lk_translationprocess_modifiedby](#BKMK_lk_translationprocess_modifiedby)
- [lk_translationprocess_modifiedonbehalfby](#BKMK_lk_translationprocess_modifiedonbehalfby)
- [lk_translationprocess_processid](#BKMK_lk_translationprocess_processid)
- [organization_translationprocess](#BKMK_organization_translationprocess)
- [transactioncurrency_translationprocess](#BKMK_transactioncurrency_translationprocess)

### <a name="BKMK_lk_translationprocess_activestageid"></a> lk_translationprocess_activestageid

One-To-Many Relationship: [processstage lk_translationprocess_activestageid](processstage.md#BKMK_lk_translationprocess_activestageid)

|Property|Value|
|---|---|
|ReferencedEntity|`processstage`|
|ReferencedAttribute|`processstageid`|
|ReferencingAttribute|`activestageid`|
|ReferencingEntityNavigationPropertyName|`activestageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_translationprocess_createdby"></a> lk_translationprocess_createdby

One-To-Many Relationship: [systemuser lk_translationprocess_createdby](systemuser.md#BKMK_lk_translationprocess_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_translationprocess_createdonbehalfby"></a> lk_translationprocess_createdonbehalfby

One-To-Many Relationship: [systemuser lk_translationprocess_createdonbehalfby](systemuser.md#BKMK_lk_translationprocess_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_translationprocess_knowledgearticleid"></a> lk_translationprocess_knowledgearticleid

One-To-Many Relationship: [knowledgearticle lk_translationprocess_knowledgearticleid](knowledgearticle.md#BKMK_lk_translationprocess_knowledgearticleid)

|Property|Value|
|---|---|
|ReferencedEntity|`knowledgearticle`|
|ReferencedAttribute|`knowledgearticleid`|
|ReferencingAttribute|`knowledgearticleid`|
|ReferencingEntityNavigationPropertyName|`knowledgearticleid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_translationprocess_modifiedby"></a> lk_translationprocess_modifiedby

One-To-Many Relationship: [systemuser lk_translationprocess_modifiedby](systemuser.md#BKMK_lk_translationprocess_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_translationprocess_modifiedonbehalfby"></a> lk_translationprocess_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_translationprocess_modifiedonbehalfby](systemuser.md#BKMK_lk_translationprocess_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfbyname`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_translationprocess_processid"></a> lk_translationprocess_processid

One-To-Many Relationship: [workflow lk_translationprocess_processid](workflow.md#BKMK_lk_translationprocess_processid)

|Property|Value|
|---|---|
|ReferencedEntity|`workflow`|
|ReferencedAttribute|`workflowid`|
|ReferencingAttribute|`processid`|
|ReferencingEntityNavigationPropertyName|`processid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_translationprocess"></a> organization_translationprocess

One-To-Many Relationship: [organization organization_translationprocess](organization.md#BKMK_organization_translationprocess)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_transactioncurrency_translationprocess"></a> transactioncurrency_translationprocess

One-To-Many Relationship: [transactioncurrency transactioncurrency_translationprocess](transactioncurrency.md#BKMK_transactioncurrency_translationprocess)

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

- [lk_translationprocess_workflowlogs](#BKMK_lk_translationprocess_workflowlogs)
- [TranslationProcess_ProcessSessions](#BKMK_TranslationProcess_ProcessSessions)
- [TranslationProcess_SyncErrors](#BKMK_TranslationProcess_SyncErrors)

### <a name="BKMK_lk_translationprocess_workflowlogs"></a> lk_translationprocess_workflowlogs

Many-To-One Relationship: [workflowlog lk_translationprocess_workflowlogs](workflowlog.md#BKMK_lk_translationprocess_workflowlogs)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`asyncoperationid`|
|ReferencedEntityNavigationPropertyName|`workflowlogs_translationprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TranslationProcess_ProcessSessions"></a> TranslationProcess_ProcessSessions

Many-To-One Relationship: [processsession TranslationProcess_ProcessSessions](processsession.md#BKMK_TranslationProcess_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`TranslationProcess_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_TranslationProcess_SyncErrors"></a> TranslationProcess_SyncErrors

Many-To-One Relationship: [syncerror TranslationProcess_SyncErrors](syncerror.md#BKMK_TranslationProcess_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`TranslationProcess_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.translationprocess?displayProperty=fullName>
