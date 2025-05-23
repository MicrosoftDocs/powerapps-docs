---
title: "Source Control Component (SourceControlComponent) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Source Control Component (SourceControlComponent) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Source Control Component (SourceControlComponent) table/entity reference (Microsoft Dataverse)

Stores the Source Control Components associated with the organization or solution

## Messages

The following table lists the messages for the Source Control Component (SourceControlComponent) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /sourcecontrolcomponents<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /sourcecontrolcomponents(*sourcecontrolcomponentid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `DeleteMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.DeleteMultiple?displayProperty=nameWithType /> |[Learn to use messages with the SDK for .NET](/power-apps/developer/data-platform/org-service/use-messages)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sourcecontrolcomponents(*sourcecontrolcomponentid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveEntityChanges`<br />Event: False | |<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityChangesRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /sourcecontrolcomponents<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /sourcecontrolcomponents(*sourcecontrolcomponentid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sourcecontrolcomponents(*sourcecontrolcomponentid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Source Control Component (SourceControlComponent) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Source Control Component** |
| **DisplayCollectionName** | **Source Control Components** |
| **SchemaName** | `SourceControlComponent` |
| **CollectionSchemaName** | `SourceControlComponents` |
| **EntitySetName** | `sourcecontrolcomponents`|
| **LogicalName** | `sourcecontrolcomponent` |
| **LogicalCollectionName** | `sourcecontrolcomponents` |
| **PrimaryIdAttribute** | `sourcecontrolcomponentid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Elastic` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Action](#BKMK_Action)
- [ComponentDisplayName](#BKMK_ComponentDisplayName)
- [ComponentId](#BKMK_ComponentId)
- [ComponentPath](#BKMK_ComponentPath)
- [ComponentType](#BKMK_ComponentType)
- [ComponentTypeName](#BKMK_ComponentTypeName)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCommitted](#BKMK_IsCommitted)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionId](#BKMK_PartitionId)
- [SolutionComponentState](#BKMK_SolutionComponentState)
- [SourceControlComponentId](#BKMK_SourceControlComponentId)
- [SourceControlComponentPayloadId](#BKMK_SourceControlComponentPayloadId)
- [SourceControlComponentPayloadIdPId](#BKMK_SourceControlComponentPayloadIdPId)
- [TTLInSeconds](#BKMK_TTLInSeconds)
- [UserAction](#BKMK_UserAction)

### <a name="BKMK_Action"></a> Action

|Property|Value|
|---|---|
|Description|**Describes an action after syncing from git.**|
|DisplayName|**Action**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`action`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontrolcomponent_action`|

#### Action Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Push**|
|2|**Pull**|
|3|**Conflict**|

### <a name="BKMK_ComponentDisplayName"></a> ComponentDisplayName

|Property|Value|
|---|---|
|Description|**Component Display Name**|
|DisplayName|**Component Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentdisplayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ComponentId"></a> ComponentId

|Property|Value|
|---|---|
|Description|**Component id of the component**|
|DisplayName|**Component Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentid`|
|RequiredLevel|Recommended|
|Type|Uniqueidentifier|

### <a name="BKMK_ComponentPath"></a> ComponentPath

|Property|Value|
|---|---|
|Description|**The path to the component**|
|DisplayName|**Component Path**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componentpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_ComponentType"></a> ComponentType

|Property|Value|
|---|---|
|Description|**Component type of the solution aware components**|
|DisplayName|**Component Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componenttype`|
|RequiredLevel|Recommended|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_ComponentTypeName"></a> ComponentTypeName

|Property|Value|
|---|---|
|Description|**Component type Name of the solution aware components**|
|DisplayName|**Component Type Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`componenttypename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|100|

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

### <a name="BKMK_IsCommitted"></a> IsCommitted

|Property|Value|
|---|---|
|Description|**Is component committed to the Git**|
|DisplayName|**Is Committed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscommitted`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`sourcecontrolcomponent_iscommitted`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description||
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

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

### <a name="BKMK_SolutionComponentState"></a> SolutionComponentState

|Property|Value|
|---|---|
|Description|**Solution Component State**|
|DisplayName|**Solution Component State**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutioncomponentstate`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontrolcomponent_solutioncomponentstate`|

#### SolutionComponentState Choices/Options

|Value|Label|
|---|---|
|0|**Create**|
|1|**Update**|
|2|**Delete**|

### <a name="BKMK_SourceControlComponentId"></a> SourceControlComponentId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Source Control Component Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontrolcomponentid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SourceControlComponentPayloadId"></a> SourceControlComponentPayloadId

|Property|Value|
|---|---|
|Description|**Unique identifier of Source Control Component Payload**|
|DisplayName|**Source Control Component Payload Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`sourcecontrolcomponentpayloadid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|sourcecontrolcomponentpayload|

### <a name="BKMK_SourceControlComponentPayloadIdPId"></a> SourceControlComponentPayloadIdPId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sourcecontrolcomponentpayloadidpid`|
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

### <a name="BKMK_UserAction"></a> UserAction

|Property|Value|
|---|---|
|Description|**Describes a user action to resolve a conflict.**|
|DisplayName|**UserAction**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`useraction`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`sourcecontrolcomponent_useraction`|

#### UserAction Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Push**|
|2|**Pull**|


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

- [lk_sourcecontrolcomponent_createdby](#BKMK_lk_sourcecontrolcomponent_createdby)
- [lk_sourcecontrolcomponent_createdonbehalfby](#BKMK_lk_sourcecontrolcomponent_createdonbehalfby)
- [lk_sourcecontrolcomponent_modifiedby](#BKMK_lk_sourcecontrolcomponent_modifiedby)
- [lk_sourcecontrolcomponent_modifiedonbehalfby](#BKMK_lk_sourcecontrolcomponent_modifiedonbehalfby)
- [sourcecontrolcomponentpayload_sourcecontrolcomponent](#BKMK_sourcecontrolcomponentpayload_sourcecontrolcomponent)

### <a name="BKMK_lk_sourcecontrolcomponent_createdby"></a> lk_sourcecontrolcomponent_createdby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponent_createdby](systemuser.md#BKMK_lk_sourcecontrolcomponent_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponent_createdonbehalfby"></a> lk_sourcecontrolcomponent_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponent_createdonbehalfby](systemuser.md#BKMK_lk_sourcecontrolcomponent_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponent_modifiedby"></a> lk_sourcecontrolcomponent_modifiedby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponent_modifiedby](systemuser.md#BKMK_lk_sourcecontrolcomponent_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sourcecontrolcomponent_modifiedonbehalfby"></a> lk_sourcecontrolcomponent_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sourcecontrolcomponent_modifiedonbehalfby](systemuser.md#BKMK_lk_sourcecontrolcomponent_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sourcecontrolcomponentpayload_sourcecontrolcomponent"></a> sourcecontrolcomponentpayload_sourcecontrolcomponent

One-To-Many Relationship: [sourcecontrolcomponentpayload sourcecontrolcomponentpayload_sourcecontrolcomponent](sourcecontrolcomponentpayload.md#BKMK_sourcecontrolcomponentpayload_sourcecontrolcomponent)

|Property|Value|
|---|---|
|ReferencedEntity|`sourcecontrolcomponentpayload`|
|ReferencedAttribute|`sourcecontrolcomponentpayloadid`|
|ReferencingAttribute|`sourcecontrolcomponentpayloadid`|
|ReferencingEntityNavigationPropertyName|`sourcecontrolcomponentpayloadid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sourcecontrolcomponent?displayProperty=fullName>
