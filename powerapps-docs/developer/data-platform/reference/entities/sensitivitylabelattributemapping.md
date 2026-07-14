---
title: "Sensitivity Label Attribute Mapping (sensitivitylabelattributemapping) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sensitivity Label Attribute Mapping (sensitivitylabelattributemapping) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sensitivity Label Attribute Mapping (sensitivitylabelattributemapping) table/entity reference (Microsoft Dataverse)

Sensitivity Label Attribute Mapping

## Messages

The following table lists the messages for the Sensitivity Label Attribute Mapping (sensitivitylabelattributemapping) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /sensitivitylabelattributemappings<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: True |`DELETE` /sensitivitylabelattributemappings(*sensitivitylabelattributemappingid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: True |`GET` /sensitivitylabelattributemappings(*sensitivitylabelattributemappingid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /sensitivitylabelattributemappings<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: True |`PATCH` /sensitivitylabelattributemappings(*sensitivitylabelattributemappingid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /sensitivitylabelattributemappings(*sensitivitylabelattributemappingid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: True |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /sensitivitylabelattributemappings(*sensitivitylabelattributemappingid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Sensitivity Label Attribute Mapping (sensitivitylabelattributemapping) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sensitivity Label Attribute Mapping** |
| **DisplayCollectionName** | **Sensitivity Label Attribute Mappings** |
| **SchemaName** | `sensitivitylabelattributemapping` |
| **CollectionSchemaName** | `sensitivitylabelattributemappings` |
| **EntitySetName** | `sensitivitylabelattributemappings`|
| **LogicalName** | `sensitivitylabelattributemapping` |
| **LogicalCollectionName** | `sensitivitylabelattributemappings` |
| **PrimaryIdAttribute** | `sensitivitylabelattributemappingid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [EntityId](#BKMK_EntityId)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IsCustomizable](#BKMK_IsCustomizable)
- [LabelId](#BKMK_LabelId)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [sensitivitylabelattributemappingId](#BKMK_sensitivitylabelattributemappingId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier for Attribute associated with SensitivityLabelAttributeMapping.**|
|DisplayName|**Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributeid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|attribute|

### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|---|---|
|Description|**Unique identifier for Entity associated with SensitivityLabelAttributeMapping.**|
|DisplayName|**Entity Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|entity|

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

### <a name="BKMK_LabelId"></a> LabelId

|Property|Value|
|---|---|
|Description|**The sensitivity label assigned to the Attribute.**|
|DisplayName|**Sensitivity Label**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`labelid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|sensitivitylabel|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**The name of the settings.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
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

### <a name="BKMK_sensitivitylabelattributemappingId"></a> sensitivitylabelattributemappingId

|Property|Value|
|---|---|
|Description|**Unique identifier for Sensitivity Label Attribute Mapping**|
|DisplayName|**Sensitivity Label Attribute Mapping Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sensitivitylabelattributemappingid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Sensitivity Label Attribute Mapping**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`sensitivitylabelattributemapping_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Sensitivity Label Attribute Mapping**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`sensitivitylabelattributemapping_statuscode`|

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

- [attribute_sensitivitylabelattributemapping_AttributeId](#BKMK_attribute_sensitivitylabelattributemapping_AttributeId)
- [entity_sensitivitylabelattributemapping_EntityId](#BKMK_entity_sensitivitylabelattributemapping_EntityId)
- [lk_sensitivitylabelattributemapping_createdby](#BKMK_lk_sensitivitylabelattributemapping_createdby)
- [lk_sensitivitylabelattributemapping_createdonbehalfby](#BKMK_lk_sensitivitylabelattributemapping_createdonbehalfby)
- [lk_sensitivitylabelattributemapping_modifiedby](#BKMK_lk_sensitivitylabelattributemapping_modifiedby)
- [lk_sensitivitylabelattributemapping_modifiedonbehalfby](#BKMK_lk_sensitivitylabelattributemapping_modifiedonbehalfby)
- [organization_sensitivitylabelattributemapping](#BKMK_organization_sensitivitylabelattributemapping)
- [sensitivitylabelattributemapping_sensitivitylabel](#BKMK_sensitivitylabelattributemapping_sensitivitylabel)

### <a name="BKMK_attribute_sensitivitylabelattributemapping_AttributeId"></a> attribute_sensitivitylabelattributemapping_AttributeId

One-To-Many Relationship: [attribute attribute_sensitivitylabelattributemapping_AttributeId](attribute.md#BKMK_attribute_sensitivitylabelattributemapping_AttributeId)

|Property|Value|
|---|---|
|ReferencedEntity|`attribute`|
|ReferencedAttribute|`attributeid`|
|ReferencingAttribute|`attributeid`|
|ReferencingEntityNavigationPropertyName|`AttributeId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_entity_sensitivitylabelattributemapping_EntityId"></a> entity_sensitivitylabelattributemapping_EntityId

One-To-Many Relationship: [entity entity_sensitivitylabelattributemapping_EntityId](entity.md#BKMK_entity_sensitivitylabelattributemapping_EntityId)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`entityid`|
|ReferencingEntityNavigationPropertyName|`EntityId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sensitivitylabelattributemapping_createdby"></a> lk_sensitivitylabelattributemapping_createdby

One-To-Many Relationship: [systemuser lk_sensitivitylabelattributemapping_createdby](systemuser.md#BKMK_lk_sensitivitylabelattributemapping_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sensitivitylabelattributemapping_createdonbehalfby"></a> lk_sensitivitylabelattributemapping_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sensitivitylabelattributemapping_createdonbehalfby](systemuser.md#BKMK_lk_sensitivitylabelattributemapping_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sensitivitylabelattributemapping_modifiedby"></a> lk_sensitivitylabelattributemapping_modifiedby

One-To-Many Relationship: [systemuser lk_sensitivitylabelattributemapping_modifiedby](systemuser.md#BKMK_lk_sensitivitylabelattributemapping_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sensitivitylabelattributemapping_modifiedonbehalfby"></a> lk_sensitivitylabelattributemapping_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sensitivitylabelattributemapping_modifiedonbehalfby](systemuser.md#BKMK_lk_sensitivitylabelattributemapping_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sensitivitylabelattributemapping"></a> organization_sensitivitylabelattributemapping

One-To-Many Relationship: [organization organization_sensitivitylabelattributemapping](organization.md#BKMK_organization_sensitivitylabelattributemapping)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sensitivitylabelattributemapping_sensitivitylabel"></a> sensitivitylabelattributemapping_sensitivitylabel

One-To-Many Relationship: [sensitivitylabel sensitivitylabelattributemapping_sensitivitylabel](sensitivitylabel.md#BKMK_sensitivitylabelattributemapping_sensitivitylabel)

|Property|Value|
|---|---|
|ReferencedEntity|`sensitivitylabel`|
|ReferencedAttribute|`sensitivitylabelid`|
|ReferencingAttribute|`labelid`|
|ReferencingEntityNavigationPropertyName|`LabelId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `RemoveLink`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [sensitivitylabelattributemapping_AsyncOperations](#BKMK_sensitivitylabelattributemapping_AsyncOperations)
- [sensitivitylabelattributemapping_BulkDeleteFailures](#BKMK_sensitivitylabelattributemapping_BulkDeleteFailures)
- [sensitivitylabelattributemapping_DuplicateBaseRecord](#BKMK_sensitivitylabelattributemapping_DuplicateBaseRecord)
- [sensitivitylabelattributemapping_DuplicateMatchingRecord](#BKMK_sensitivitylabelattributemapping_DuplicateMatchingRecord)
- [sensitivitylabelattributemapping_MailboxTrackingFolders](#BKMK_sensitivitylabelattributemapping_MailboxTrackingFolders)
- [sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses](#BKMK_sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses)
- [sensitivitylabelattributemapping_ProcessSession](#BKMK_sensitivitylabelattributemapping_ProcessSession)
- [sensitivitylabelattributemapping_SyncErrors](#BKMK_sensitivitylabelattributemapping_SyncErrors)

### <a name="BKMK_sensitivitylabelattributemapping_AsyncOperations"></a> sensitivitylabelattributemapping_AsyncOperations

Many-To-One Relationship: [asyncoperation sensitivitylabelattributemapping_AsyncOperations](asyncoperation.md#BKMK_sensitivitylabelattributemapping_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_BulkDeleteFailures"></a> sensitivitylabelattributemapping_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure sensitivitylabelattributemapping_BulkDeleteFailures](bulkdeletefailure.md#BKMK_sensitivitylabelattributemapping_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_DuplicateBaseRecord"></a> sensitivitylabelattributemapping_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord sensitivitylabelattributemapping_DuplicateBaseRecord](duplicaterecord.md#BKMK_sensitivitylabelattributemapping_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_DuplicateMatchingRecord"></a> sensitivitylabelattributemapping_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord sensitivitylabelattributemapping_DuplicateMatchingRecord](duplicaterecord.md#BKMK_sensitivitylabelattributemapping_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_MailboxTrackingFolders"></a> sensitivitylabelattributemapping_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder sensitivitylabelattributemapping_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_sensitivitylabelattributemapping_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses"></a> sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_ProcessSession"></a> sensitivitylabelattributemapping_ProcessSession

Many-To-One Relationship: [processsession sensitivitylabelattributemapping_ProcessSession](processsession.md#BKMK_sensitivitylabelattributemapping_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sensitivitylabelattributemapping_SyncErrors"></a> sensitivitylabelattributemapping_SyncErrors

Many-To-One Relationship: [syncerror sensitivitylabelattributemapping_SyncErrors](syncerror.md#BKMK_sensitivitylabelattributemapping_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`sensitivitylabelattributemapping_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   

