---
title: "Duplicate Rule Condition (DuplicateRuleCondition) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Duplicate Rule Condition (DuplicateRuleCondition) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Duplicate Rule Condition (DuplicateRuleCondition) table/entity reference (Microsoft Dataverse)

Condition of a duplicate detection rule.

## Messages

The following table lists the messages for the Duplicate Rule Condition (DuplicateRuleCondition) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /duplicateruleconditions<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /duplicateruleconditions(*duplicateruleconditionid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /duplicateruleconditions(*duplicateruleconditionid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /duplicateruleconditions<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /duplicateruleconditions(*duplicateruleconditionid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /duplicateruleconditions(*duplicateruleconditionid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Duplicate Rule Condition (DuplicateRuleCondition) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Duplicate Rule Condition** |
| **DisplayCollectionName** | **Duplicate Rule Conditions** |
| **SchemaName** | `DuplicateRuleCondition` |
| **CollectionSchemaName** | `DuplicateRuleConditions` |
| **EntitySetName** | `duplicateruleconditions`|
| **LogicalName** | `duplicaterulecondition` |
| **LogicalCollectionName** | `duplicateruleconditions` |
| **PrimaryIdAttribute** | `duplicateruleconditionid` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [BaseAttributeName](#BKMK_BaseAttributeName)
- [DuplicateRuleConditionId](#BKMK_DuplicateRuleConditionId)
- [IgnoreBlankValues](#BKMK_IgnoreBlankValues)
- [IsCustomizable](#BKMK_IsCustomizable)
- [MatchingAttributeName](#BKMK_MatchingAttributeName)
- [OperatorCode](#BKMK_OperatorCode)
- [OperatorParam](#BKMK_OperatorParam)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [UniqueRuleName](#BKMK_UniqueRuleName)

### <a name="BKMK_BaseAttributeName"></a> BaseAttributeName

|Property|Value|
|---|---|
|Description|**Field that is being compared.**|
|DisplayName|**Base Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`baseattributename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_DuplicateRuleConditionId"></a> DuplicateRuleConditionId

|Property|Value|
|---|---|
|Description|**Unique identifier of the condition.**|
|DisplayName|**Duplicate Rule Condition**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`duplicateruleconditionid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_IgnoreBlankValues"></a> IgnoreBlankValues

|Property|Value|
|---|---|
|Description|**Determines whether to consider blank values as non-duplicate values**|
|DisplayName|**Ignore Blank Values**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ignoreblankvalues`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`duplicaterulecondition_ignoreblankvalues`|
|DefaultValue|False|
|True Label|True|
|False Label|False|

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

### <a name="BKMK_MatchingAttributeName"></a> MatchingAttributeName

|Property|Value|
|---|---|
|Description|**Field that is being compared with the base field.**|
|DisplayName|**Matching Field**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`matchingattributename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_OperatorCode"></a> OperatorCode

|Property|Value|
|---|---|
|Description|**Operator for this rule condition.**|
|DisplayName|**Operator Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operatorcode`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`duplicaterulecondition_operatorcode`|

#### OperatorCode Choices/Options

|Value|Label|
|---|---|
|0|**Exact Match**|
|1|**Same First Characters**|
|2|**Same Last Characters**|
|3|**Same Date**|
|4|**Same Date and Time**|
|5|**Exact Match (Pick List Label)**|
|6|**Exact Match (Pick List Value)**|

### <a name="BKMK_OperatorParam"></a> OperatorParam

|Property|Value|
|---|---|
|Description|**Parameter value of N if the operator is Same First Characters or Same Last Characters.**|
|DisplayName|**Operator Parameter**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`operatorparam`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|1|

### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

|Property|Value|
|---|---|
|Description|**Unique identifier of the object with which the condition is associated.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`regardingobjectid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|duplicaterule|

### <a name="BKMK_UniqueRuleName"></a> UniqueRuleName

|Property|Value|
|---|---|
|Description||
|DisplayName|**UniqueRuleName**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquerulename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|


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
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)

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
|Description|**Unique identifier of the user who created the condition.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the condition was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who created the duplicate rule condition.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the user who last modified the condition.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the condition was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedon`|
|RequiredLevel|SystemRequired|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the delegate user who last modified the duplicate rule condition.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
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
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Unique identifier of the user or team who owns the duplicate rule condition.**|
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
|Description|**Unique identifier of the business unit that owns the condition.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|ApplicationRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the condition.**|
|DisplayName|**Owning User**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|ApplicationRequired|
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

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [DuplicateRule_DuplicateRuleConditions](#BKMK_DuplicateRule_DuplicateRuleConditions)
- [lk_duplicaterulecondition_createdonbehalfby](#BKMK_lk_duplicaterulecondition_createdonbehalfby)
- [lk_duplicaterulecondition_modifiedonbehalfby](#BKMK_lk_duplicaterulecondition_modifiedonbehalfby)
- [lk_duplicateruleconditionbase_createdby](#BKMK_lk_duplicateruleconditionbase_createdby)
- [lk_duplicateruleconditionbase_modifiedby](#BKMK_lk_duplicateruleconditionbase_modifiedby)

### <a name="BKMK_DuplicateRule_DuplicateRuleConditions"></a> DuplicateRule_DuplicateRuleConditions

One-To-Many Relationship: [duplicaterule DuplicateRule_DuplicateRuleConditions](duplicaterule.md#BKMK_DuplicateRule_DuplicateRuleConditions)

|Property|Value|
|---|---|
|ReferencedEntity|`duplicaterule`|
|ReferencedAttribute|`duplicateruleid`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_duplicaterulecondition_createdonbehalfby"></a> lk_duplicaterulecondition_createdonbehalfby

One-To-Many Relationship: [systemuser lk_duplicaterulecondition_createdonbehalfby](systemuser.md#BKMK_lk_duplicaterulecondition_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_duplicaterulecondition_modifiedonbehalfby"></a> lk_duplicaterulecondition_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_duplicaterulecondition_modifiedonbehalfby](systemuser.md#BKMK_lk_duplicaterulecondition_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_duplicateruleconditionbase_createdby"></a> lk_duplicateruleconditionbase_createdby

One-To-Many Relationship: [systemuser lk_duplicateruleconditionbase_createdby](systemuser.md#BKMK_lk_duplicateruleconditionbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_duplicateruleconditionbase_modifiedby"></a> lk_duplicateruleconditionbase_modifiedby

One-To-Many Relationship: [systemuser lk_duplicateruleconditionbase_modifiedby](systemuser.md#BKMK_lk_duplicateruleconditionbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_DuplicateRuleCondition_SyncErrors"></a> DuplicateRuleCondition_SyncErrors

Many-To-One Relationship: [syncerror DuplicateRuleCondition_SyncErrors](syncerror.md#BKMK_DuplicateRuleCondition_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`DuplicateRuleCondition_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.duplicaterulecondition?displayProperty=fullName>
