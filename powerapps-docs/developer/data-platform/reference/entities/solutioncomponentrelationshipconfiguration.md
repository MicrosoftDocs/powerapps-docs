---
title: "Solution Component Relationship Configuration (solutioncomponentrelationshipconfiguration) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component Relationship Configuration (solutioncomponentrelationshipconfiguration) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component Relationship Configuration (solutioncomponentrelationshipconfiguration) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Solution Component Relationship Configuration (solutioncomponentrelationshipconfiguration) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /solutioncomponentrelationshipconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: False |`GET` /solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /solutioncomponentrelationshipconfigurations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: False |`PATCH` /solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /solutioncomponentrelationshipconfigurations(*solutioncomponentrelationshipconfigurationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Solution Component Relationship Configuration (solutioncomponentrelationshipconfiguration) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component Relationship Configuration** |
| **DisplayCollectionName** | **Solution Component Relationship Configurations** |
| **SchemaName** | `solutioncomponentrelationshipconfiguration` |
| **CollectionSchemaName** | `solutioncomponentrelationshipconfigurations` |
| **EntitySetName** | `solutioncomponentrelationshipconfigurations`|
| **LogicalName** | `solutioncomponentrelationshipconfiguration` |
| **LogicalCollectionName** | `solutioncomponentrelationshipconfigurations` |
| **PrimaryIdAttribute** | `solutioncomponentrelationshipconfigurationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddRelatedComponents](#BKMK_AddRelatedComponents)
- [CascadeRemoveComponents](#BKMK_CascadeRemoveComponents)
- [EntityRelationshipId](#BKMK_EntityRelationshipId)
- [ForceAddingManagedRelatedComponents](#BKMK_ForceAddingManagedRelatedComponents)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [name](#BKMK_name)
- [NoMissingDependencyForApiManagedSolution](#BKMK_NoMissingDependencyForApiManagedSolution)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [PrimaryEntityDependencyType](#BKMK_PrimaryEntityDependencyType)
- [RespectParentRootComponentBehavior](#BKMK_RespectParentRootComponentBehavior)
- [SecondaryEntityDependencyType](#BKMK_SecondaryEntityDependencyType)
- [solutioncomponentrelationshipconfigurationId](#BKMK_solutioncomponentrelationshipconfigurationId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AddRelatedComponents"></a> AddRelatedComponents

|Property|Value|
|---|---|
|Description||
|DisplayName|**Add Related Components**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`addrelatedcomponents`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_addrelatedcomponents`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_CascadeRemoveComponents"></a> CascadeRemoveComponents

|Property|Value|
|---|---|
|Description||
|DisplayName|**Cascade Remove Components**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`cascaderemovecomponents`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_cascaderemovecomponents`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_EntityRelationshipId"></a> EntityRelationshipId

|Property|Value|
|---|---|
|Description|**Unique identifier for Entity Relationship associated with Solution Component Relationship Configuration.**|
|DisplayName|**Entity Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityrelationshipid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|entityrelationship|

### <a name="BKMK_ForceAddingManagedRelatedComponents"></a> ForceAddingManagedRelatedComponents

|Property|Value|
|---|---|
|Description||
|DisplayName|**Force Adding Managed Related Components**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`forceaddingmanagedrelatedcomponents`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_forceaddingmanagedrelatedcomponents`|
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

### <a name="BKMK_NoMissingDependencyForApiManagedSolution"></a> NoMissingDependencyForApiManagedSolution

|Property|Value|
|---|---|
|Description|**Boolean that indicates if this relationship can be excluded from the export as a missing dependency if the target is part of an api managed solution.**|
|DisplayName|**Do Not Export As Missing Dependency For Api Managed Solution**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`nomissingdependencyforapimanagedsolution`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_nomissingdependencyforapimanagedsolution`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_PrimaryEntityDependencyType"></a> PrimaryEntityDependencyType

|Property|Value|
|---|---|
|Description||
|DisplayName|**PrimaryEntityDependencyType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primaryentitydependencytype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_primaryentitydependencytype`|

#### PrimaryEntityDependencyType Choices/Options

|Value|Label|
|---|---|
|0|**Hard Dependency**|
|1|**Soft Dependency**|

### <a name="BKMK_RespectParentRootComponentBehavior"></a> RespectParentRootComponentBehavior

|Property|Value|
|---|---|
|Description||
|DisplayName|**Respect Parent Root Component Behavior**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`respectparentrootcomponentbehavior`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_respectparentrootcomponentbehavior`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_SecondaryEntityDependencyType"></a> SecondaryEntityDependencyType

|Property|Value|
|---|---|
|Description||
|DisplayName|**SecondaryEntityDependencyType**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`secondaryentitydependencytype`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_secondaryentitydependencytype`|

#### SecondaryEntityDependencyType Choices/Options

|Value|Label|
|---|---|
|0|**Hard Dependency**|
|1|**Soft Dependency**|

### <a name="BKMK_solutioncomponentrelationshipconfigurationId"></a> solutioncomponentrelationshipconfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Solution Component Relationship Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutioncomponentrelationshipconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Solution Component Relationship Configuration**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Solution Component Relationship Configuration**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentrelationshipconfiguration_statuscode`|

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

- [entityrelationship_config](#BKMK_entityrelationship_config)
- [lk_solutioncomponentrelationshipconfiguration_createdby](#BKMK_lk_solutioncomponentrelationshipconfiguration_createdby)
- [lk_solutioncomponentrelationshipconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby)
- [lk_solutioncomponentrelationshipconfiguration_modifiedby](#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby)
- [lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby)
- [organization_solutioncomponentrelationshipconfiguration](#BKMK_organization_solutioncomponentrelationshipconfiguration)

### <a name="BKMK_entityrelationship_config"></a> entityrelationship_config

One-To-Many Relationship: [entityrelationship entityrelationship_config](entityrelationship.md#BKMK_entityrelationship_config)

|Property|Value|
|---|---|
|ReferencedEntity|`entityrelationship`|
|ReferencedAttribute|`entityrelationshipid`|
|ReferencingAttribute|`entityrelationshipid`|
|ReferencingEntityNavigationPropertyName|`EntityRelationshipId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_createdby"></a> lk_solutioncomponentrelationshipconfiguration_createdby

One-To-Many Relationship: [systemuser lk_solutioncomponentrelationshipconfiguration_createdby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby"></a> lk_solutioncomponentrelationshipconfiguration_createdonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentrelationshipconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby"></a> lk_solutioncomponentrelationshipconfiguration_modifiedby

One-To-Many Relationship: [systemuser lk_solutioncomponentrelationshipconfiguration_modifiedby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentrelationshipconfiguration_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_solutioncomponentrelationshipconfiguration"></a> organization_solutioncomponentrelationshipconfiguration

One-To-Many Relationship: [organization organization_solutioncomponentrelationshipconfiguration](organization.md#BKMK_organization_solutioncomponentrelationshipconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [solutioncomponentrelationshipconfiguration_AsyncOperations](#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations)
- [solutioncomponentrelationshipconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)
- [solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord)
- [solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord)
- [solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders)
- [solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentrelationshipconfiguration_ProcessSession](#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession)
- [solutioncomponentrelationshipconfiguration_SyncErrors](#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)

### <a name="BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations"></a> solutioncomponentrelationshipconfiguration_AsyncOperations

Many-To-One Relationship: [asyncoperation solutioncomponentrelationshipconfiguration_AsyncOperations](asyncoperation.md#BKMK_solutioncomponentrelationshipconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures"></a> solutioncomponentrelationshipconfiguration_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure solutioncomponentrelationshipconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_solutioncomponentrelationshipconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord solutioncomponentrelationshipconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord"></a> solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders"></a> solutioncomponentrelationshipconfiguration_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder solutioncomponentrelationshipconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_solutioncomponentrelationshipconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_ProcessSession"></a> solutioncomponentrelationshipconfiguration_ProcessSession

Many-To-One Relationship: [processsession solutioncomponentrelationshipconfiguration_ProcessSession](processsession.md#BKMK_solutioncomponentrelationshipconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentrelationshipconfiguration_SyncErrors"></a> solutioncomponentrelationshipconfiguration_SyncErrors

Many-To-One Relationship: [syncerror solutioncomponentrelationshipconfiguration_SyncErrors](syncerror.md#BKMK_solutioncomponentrelationshipconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentrelationshipconfiguration_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.solutioncomponentrelationshipconfiguration?displayProperty=fullName>
