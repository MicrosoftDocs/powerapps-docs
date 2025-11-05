---
title: "AI Evaluation Metric (msdyn_AIEvaluationMetric) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the AI Evaluation Metric (msdyn_AIEvaluationMetric) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# AI Evaluation Metric (msdyn_AIEvaluationMetric) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the AI Evaluation Metric (msdyn_AIEvaluationMetric) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /msdyn_aievaluationmetrics<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /msdyn_aievaluationmetrics(*msdyn_aievaluationmetricid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /msdyn_aievaluationmetrics(*msdyn_aievaluationmetricid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: True | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: True |`GET` /msdyn_aievaluationmetrics<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /msdyn_aievaluationmetrics(*msdyn_aievaluationmetricid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: True |`PATCH` /msdyn_aievaluationmetrics(*msdyn_aievaluationmetricid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the AI Evaluation Metric (msdyn_AIEvaluationMetric) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **AI Evaluation Metric** |
| **DisplayCollectionName** | **AI Evaluation Metric** |
| **SchemaName** | `msdyn_AIEvaluationMetric` |
| **CollectionSchemaName** | `msdyn_AIEvaluationMetrics` |
| **EntitySetName** | `msdyn_aievaluationmetrics`|
| **LogicalName** | `msdyn_aievaluationmetric` |
| **LogicalCollectionName** | `msdyn_aievaluationmetrics` |
| **PrimaryIdAttribute** | `msdyn_aievaluationmetricid` |
| **PrimaryNameAttribute** |`msdyn_aiobjectid` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [msdyn_AIEvaluationMetricId](#BKMK_msdyn_AIEvaluationMetricId)
- [msdyn_AIEvaluatorName](#BKMK_msdyn_AIEvaluatorName)
- [msdyn_AIObjectId](#BKMK_msdyn_AIObjectId)
- [msdyn_AIObjectType](#BKMK_msdyn_AIObjectType)
- [msdyn_EvalAvgScore](#BKMK_msdyn_EvalAvgScore)
- [msdyn_EvalP50Score](#BKMK_msdyn_EvalP50Score)
- [msdyn_EvalP75Score](#BKMK_msdyn_EvalP75Score)
- [msdyn_EvalP95Score](#BKMK_msdyn_EvalP95Score)
- [msdyn_LastCalculatedAt](#BKMK_msdyn_LastCalculatedAt)
- [msdyn_LookBackWindowDurationInMinutes](#BKMK_msdyn_LookBackWindowDurationInMinutes)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [TTLInSeconds](#BKMK_TTLInSeconds)

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

### <a name="BKMK_msdyn_AIEvaluationMetricId"></a> msdyn_AIEvaluationMetricId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**AI Evaluation Metric**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`msdyn_aievaluationmetricid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_msdyn_AIEvaluatorName"></a> msdyn_AIEvaluatorName

|Property|Value|
|---|---|
|Description|**Evaluator Name**|
|DisplayName|**AIEvaluatorName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aievaluatorname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_msdyn_AIObjectId"></a> msdyn_AIObjectId

|Property|Value|
|---|---|
|Description|**Object Id**|
|DisplayName|**AIObjectId**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aiobjectid`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|850|

### <a name="BKMK_msdyn_AIObjectType"></a> msdyn_AIObjectType

|Property|Value|
|---|---|
|Description|**Object Type**|
|DisplayName|**AIObjectType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_aiobjecttype`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_msdyn_EvalAvgScore"></a> msdyn_EvalAvgScore

|Property|Value|
|---|---|
|Description|**Evaluation Average score**|
|DisplayName|**EvalAvgScore**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_evalavgscore`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_msdyn_EvalP50Score"></a> msdyn_EvalP50Score

|Property|Value|
|---|---|
|Description|**Evaluation P50 score**|
|DisplayName|**EvalP50Score**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_evalp50score`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_msdyn_EvalP75Score"></a> msdyn_EvalP75Score

|Property|Value|
|---|---|
|Description|**Evaluation P75 score**|
|DisplayName|**EvalP75Score**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_evalp75score`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_msdyn_EvalP95Score"></a> msdyn_EvalP95Score

|Property|Value|
|---|---|
|Description|**Evaluation P95 score**|
|DisplayName|**EvalP95Score**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_evalp95score`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Auto|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_msdyn_LastCalculatedAt"></a> msdyn_LastCalculatedAt

|Property|Value|
|---|---|
|Description|**Last calculated time**|
|DisplayName|**LastCalculatedAt**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lastcalculatedat`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Auto|
|SourceTypeMask|0|

### <a name="BKMK_msdyn_LookBackWindowDurationInMinutes"></a> msdyn_LookBackWindowDurationInMinutes

|Property|Value|
|---|---|
|Description|**Lookback duration in minutes**|
|DisplayName|**LookBackWindowDurationInMinutes**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`msdyn_lookbackwindowdurationinminutes`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

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

### <a name="BKMK_PartitionId"></a> PartitionId

|Property|Value|
|---|---|
|Description|**Logical partition id. A logical partition consists of a set of records with same partition id.**|
|DisplayName|**Partition Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionid`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_TTLInSeconds"></a> TTLInSeconds

|Property|Value|
|---|---|
|Description|**Time to live in seconds.**|
|DisplayName|**Time to live**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ttlinseconds`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
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

- [lk_msdyn_aievaluationmetric_createdby](#BKMK_lk_msdyn_aievaluationmetric_createdby)
- [lk_msdyn_aievaluationmetric_createdonbehalfby](#BKMK_lk_msdyn_aievaluationmetric_createdonbehalfby)
- [lk_msdyn_aievaluationmetric_modifiedby](#BKMK_lk_msdyn_aievaluationmetric_modifiedby)
- [lk_msdyn_aievaluationmetric_modifiedonbehalfby](#BKMK_lk_msdyn_aievaluationmetric_modifiedonbehalfby)

### <a name="BKMK_lk_msdyn_aievaluationmetric_createdby"></a> lk_msdyn_aievaluationmetric_createdby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationmetric_createdby](systemuser.md#BKMK_lk_msdyn_aievaluationmetric_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationmetric_createdonbehalfby"></a> lk_msdyn_aievaluationmetric_createdonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationmetric_createdonbehalfby](systemuser.md#BKMK_lk_msdyn_aievaluationmetric_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationmetric_modifiedby"></a> lk_msdyn_aievaluationmetric_modifiedby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationmetric_modifiedby](systemuser.md#BKMK_lk_msdyn_aievaluationmetric_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_msdyn_aievaluationmetric_modifiedonbehalfby"></a> lk_msdyn_aievaluationmetric_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_msdyn_aievaluationmetric_modifiedonbehalfby](systemuser.md#BKMK_lk_msdyn_aievaluationmetric_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

