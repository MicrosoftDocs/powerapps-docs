---
title: "Synapse Link Profile Entity (synapselinkprofileentity) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Synapse Link Profile Entity (synapselinkprofileentity) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Synapse Link Profile Entity (synapselinkprofileentity) table/entity reference (Microsoft Dataverse)

Entities associated with the Synapse Link profile

## Messages

The following table lists the messages for the Synapse Link Profile Entity (synapselinkprofileentity) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /synapselinkprofileentities<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /synapselinkprofileentities(*synapselinkprofileentityid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /synapselinkprofileentities(*synapselinkprofileentityid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /synapselinkprofileentities<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /synapselinkprofileentities(*synapselinkprofileentityid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /synapselinkprofileentities(*synapselinkprofileentityid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /synapselinkprofileentities(*synapselinkprofileentityid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Synapse Link Profile Entity (synapselinkprofileentity) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Synapse Link Profile Entity** |
| **DisplayCollectionName** | **Synapse Link Profile Entities** |
| **SchemaName** | `synapselinkprofileentity` |
| **CollectionSchemaName** | `synapselinkprofileentities` |
| **EntitySetName** | `synapselinkprofileentities`|
| **LogicalName** | `synapselinkprofileentity` |
| **LogicalCollectionName** | `synapselinkprofileentities` |
| **PrimaryIdAttribute** | `synapselinkprofileentityid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AppendOnlyMode](#BKMK_AppendOnlyMode)
- [Enabled](#BKMK_Enabled)
- [EntityName](#BKMK_EntityName)
- [EntitySource](#BKMK_EntitySource)
- [EntityType](#BKMK_EntityType)
- [ExtendedProperties](#BKMK_ExtendedProperties)
- [GenerateParquet](#BKMK_GenerateParquet)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PartitionStrategy](#BKMK_PartitionStrategy)
- [profile](#BKMK_profile)
- [RecordCountPerBlock](#BKMK_RecordCountPerBlock)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [synapselinkprofileentityId](#BKMK_synapselinkprofileentityId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UniqueName](#BKMK_UniqueName)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AppendOnlyMode"></a> AppendOnlyMode

|Property|Value|
|---|---|
|Description|**Is append only mode**|
|DisplayName|**Append Only Mode**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`appendonlymode`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`synapselinkprofileentity_appendonlymode`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Enabled"></a> Enabled

|Property|Value|
|---|---|
|Description|**Is entity enabled**|
|DisplayName|**Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`enabled`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`synapselinkprofileentity_enabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EntityName"></a> EntityName

|Property|Value|
|---|---|
|Description|**Name of the entity**|
|DisplayName|**Entity Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_EntitySource"></a> EntitySource

|Property|Value|
|---|---|
|Description|**Source of the entity**|
|DisplayName|**Entity source**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitysource`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`synapselinkentitysource`|

#### EntitySource Choices/Options

|Value|Label|
|---|---|
|0|**Dataverse**|
|1|**FnOTables**|

### <a name="BKMK_EntityType"></a> EntityType

|Property|Value|
|---|---|
|Description|**Type of the entity**|
|DisplayName|**Entity Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entitytype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`synapselinkprofileentitytype`|

#### EntityType Choices/Options

|Value|Label|
|---|---|
|0|**Requested**|

### <a name="BKMK_ExtendedProperties"></a> ExtendedProperties

|Property|Value|
|---|---|
|Description|**Extended properties**|
|DisplayName|**Extended Properties**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`extendedproperties`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4000|

### <a name="BKMK_GenerateParquet"></a> GenerateParquet

|Property|Value|
|---|---|
|Description|**Generate parquet**|
|DisplayName|**Generate Parquet**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`generateparquet`|
|RequiredLevel|ApplicationRequired|
|Type|Boolean|
|GlobalChoiceName|`synapselinkprofileentity_generateparquet`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_name"></a> name

|Property|Value|
|---|---|
|Description|**The name of the custom entity.**|
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
|MaxLength|100|

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

### <a name="BKMK_PartitionStrategy"></a> PartitionStrategy

|Property|Value|
|---|---|
|Description|**Partition strategy**|
|DisplayName|**Partition Strategy**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`partitionstrategy`|
|RequiredLevel|ApplicationRequired|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`synapselinkentitypartitionstrategy`|

#### PartitionStrategy Choices/Options

|Value|Label|
|---|---|
|0|**Year**|
|1|**Month**|
|2|**HalfMonth**|
|3|**FiveDay**|

### <a name="BKMK_profile"></a> profile

|Property|Value|
|---|---|
|Description|**Unique identifier for Synapse Link Profile associated with Synapse Link Profile Entity.**|
|DisplayName|**Profile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`profile`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|synapselinkprofile|

### <a name="BKMK_RecordCountPerBlock"></a> RecordCountPerBlock

|Property|Value|
|---|---|
|Description|**Record count per block**|
|DisplayName|**Record Count Per Block**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`recordcountperblock`|
|RequiredLevel|ApplicationRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|0|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Synapse Link Profile Entity**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkprofileentity_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Synapse Link Profile Entity**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`synapselinkprofileentity_statuscode`|

#### statuscode Choices/Options

|Value|Details|
|---|---|
|1|Label: **Active**<br />State:0<br />TransitionData: None|
|2|Label: **Inactive**<br />State:1<br />TransitionData: None|

### <a name="BKMK_synapselinkprofileentityId"></a> synapselinkprofileentityId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Synapse Link Profile Entity**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`synapselinkprofileentityid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

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

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**Unique name**|
|DisplayName|**Unique Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

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
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
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

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the organization**|
|DisplayName|**Organization Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|organization|

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

- [lk_synapselinkprofileentity_createdby](#BKMK_lk_synapselinkprofileentity_createdby)
- [lk_synapselinkprofileentity_createdonbehalfby](#BKMK_lk_synapselinkprofileentity_createdonbehalfby)
- [lk_synapselinkprofileentity_modifiedby](#BKMK_lk_synapselinkprofileentity_modifiedby)
- [lk_synapselinkprofileentity_modifiedonbehalfby](#BKMK_lk_synapselinkprofileentity_modifiedonbehalfby)
- [organization_synapselinkprofileentity](#BKMK_organization_synapselinkprofileentity)
- [profileentities](#BKMK_profileentities)

### <a name="BKMK_lk_synapselinkprofileentity_createdby"></a> lk_synapselinkprofileentity_createdby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentity_createdby](systemuser.md#BKMK_lk_synapselinkprofileentity_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofileentity_createdonbehalfby"></a> lk_synapselinkprofileentity_createdonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentity_createdonbehalfby](systemuser.md#BKMK_lk_synapselinkprofileentity_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofileentity_modifiedby"></a> lk_synapselinkprofileentity_modifiedby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentity_modifiedby](systemuser.md#BKMK_lk_synapselinkprofileentity_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_synapselinkprofileentity_modifiedonbehalfby"></a> lk_synapselinkprofileentity_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_synapselinkprofileentity_modifiedonbehalfby](systemuser.md#BKMK_lk_synapselinkprofileentity_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_synapselinkprofileentity"></a> organization_synapselinkprofileentity

One-To-Many Relationship: [organization organization_synapselinkprofileentity](organization.md#BKMK_organization_synapselinkprofileentity)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_profileentities"></a> profileentities

One-To-Many Relationship: [synapselinkprofile profileentities](synapselinkprofile.md#BKMK_profileentities)

|Property|Value|
|---|---|
|ReferencedEntity|`synapselinkprofile`|
|ReferencedAttribute|`synapselinkprofileid`|
|ReferencingAttribute|`profile`|
|ReferencingEntityNavigationPropertyName|`profile`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [entitystate](#BKMK_entitystate)
- [synapselinkprofileentity_AsyncOperations](#BKMK_synapselinkprofileentity_AsyncOperations)
- [synapselinkprofileentity_BulkDeleteFailures](#BKMK_synapselinkprofileentity_BulkDeleteFailures)
- [synapselinkprofileentity_DuplicateBaseRecord](#BKMK_synapselinkprofileentity_DuplicateBaseRecord)
- [synapselinkprofileentity_DuplicateMatchingRecord](#BKMK_synapselinkprofileentity_DuplicateMatchingRecord)
- [synapselinkprofileentity_MailboxTrackingFolders](#BKMK_synapselinkprofileentity_MailboxTrackingFolders)
- [synapselinkprofileentity_PrincipalObjectAttributeAccesses](#BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses)
- [synapselinkprofileentity_ProcessSession](#BKMK_synapselinkprofileentity_ProcessSession)
- [synapselinkprofileentity_SyncErrors](#BKMK_synapselinkprofileentity_SyncErrors)

### <a name="BKMK_entitystate"></a> entitystate

Many-To-One Relationship: [synapselinkprofileentitystate entitystate](synapselinkprofileentitystate.md#BKMK_entitystate)

|Property|Value|
|---|---|
|ReferencingEntity|`synapselinkprofileentitystate`|
|ReferencingAttribute|`profileentity`|
|ReferencedEntityNavigationPropertyName|`entitystate`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_AsyncOperations"></a> synapselinkprofileentity_AsyncOperations

Many-To-One Relationship: [asyncoperation synapselinkprofileentity_AsyncOperations](asyncoperation.md#BKMK_synapselinkprofileentity_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_BulkDeleteFailures"></a> synapselinkprofileentity_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure synapselinkprofileentity_BulkDeleteFailures](bulkdeletefailure.md#BKMK_synapselinkprofileentity_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_DuplicateBaseRecord"></a> synapselinkprofileentity_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord synapselinkprofileentity_DuplicateBaseRecord](duplicaterecord.md#BKMK_synapselinkprofileentity_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_DuplicateMatchingRecord"></a> synapselinkprofileentity_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord synapselinkprofileentity_DuplicateMatchingRecord](duplicaterecord.md#BKMK_synapselinkprofileentity_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_MailboxTrackingFolders"></a> synapselinkprofileentity_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder synapselinkprofileentity_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_synapselinkprofileentity_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses"></a> synapselinkprofileentity_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess synapselinkprofileentity_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_synapselinkprofileentity_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_ProcessSession"></a> synapselinkprofileentity_ProcessSession

Many-To-One Relationship: [processsession synapselinkprofileentity_ProcessSession](processsession.md#BKMK_synapselinkprofileentity_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_synapselinkprofileentity_SyncErrors"></a> synapselinkprofileentity_SyncErrors

Many-To-One Relationship: [syncerror synapselinkprofileentity_SyncErrors](syncerror.md#BKMK_synapselinkprofileentity_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`synapselinkprofileentity_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.synapselinkprofileentity?displayProperty=fullName>
