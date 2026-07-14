---
title: "Solution Component Configuration (solutioncomponentconfiguration) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component Configuration (solutioncomponentconfiguration) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component Configuration (solutioncomponentconfiguration) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Solution Component Configuration (solutioncomponentconfiguration) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /solutioncomponentconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: False |`GET` /solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /solutioncomponentconfigurations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: False |`PATCH` /solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /solutioncomponentconfigurations(*solutioncomponentconfigurationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Solution Component Configuration (solutioncomponentconfiguration) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component Configuration** |
| **DisplayCollectionName** | **Solution Component Configurations** |
| **SchemaName** | `solutioncomponentconfiguration` |
| **CollectionSchemaName** | `solutioncomponentconfigurations` |
| **EntitySetName** | `solutioncomponentconfigurations`|
| **LogicalName** | `solutioncomponentconfiguration` |
| **LogicalCollectionName** | `solutioncomponentconfigurations` |
| **PrimaryIdAttribute** | `solutioncomponentconfigurationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllowExportKeyWithoutPrefix](#BKMK_AllowExportKeyWithoutPrefix)
- [DependencyRemovalDisabledForComponents](#BKMK_DependencyRemovalDisabledForComponents)
- [EntityId](#BKMK_EntityId)
- [FileFormat](#BKMK_FileFormat)
- [FileScope](#BKMK_FileScope)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InvokeSubstitution](#BKMK_InvokeSubstitution)
- [IsCustomizable](#BKMK_IsCustomizable)
- [isdisplayable](#BKMK_isdisplayable)
- [IsOneToOneChildComponent](#BKMK_IsOneToOneChildComponent)
- [IsSoftDeleteEnabled](#BKMK_IsSoftDeleteEnabled)
- [IsVersioningEnabled](#BKMK_IsVersioningEnabled)
- [KeepActiveCustomizationAfterConversion](#BKMK_KeepActiveCustomizationAfterConversion)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [solutioncomponentconfigurationId](#BKMK_solutioncomponentconfigurationId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AllowExportKeyWithoutPrefix"></a> AllowExportKeyWithoutPrefix

|Property|Value|
|---|---|
|Description|**Boolean that indicates if an export key without a prefix is allowed.**|
|DisplayName|**Allow Export Key Without Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`allowexportkeywithoutprefix`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_solutioncomponentconfiguration_allowexportkeywithoutprefix`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_DependencyRemovalDisabledForComponents"></a> DependencyRemovalDisabledForComponents

|Property|Value|
|---|---|
|Description|**Comma separated list of required components not supported for automatic dependency removal**|
|DisplayName|**Automatic Dependency Removal Disabled For Components**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dependencyremovaldisabledforcomponents`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1024|

### <a name="BKMK_EntityId"></a> EntityId

|Property|Value|
|---|---|
|Description|**Unique identifier for Entity associated with Solution Component Configuration.**|
|DisplayName|**Entity**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`entityid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|entity|

### <a name="BKMK_FileFormat"></a> FileFormat

|Property|Value|
|---|---|
|Description||
|DisplayName|**File Format**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fileformat`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`solutioncomponentconfiguration_fileformat`|

#### FileFormat Choices/Options

|Value|Label|
|---|---|
|0|**xml**|
|1|**json**|

### <a name="BKMK_FileScope"></a> FileScope

|Property|Value|
|---|---|
|Description||
|DisplayName|**File Scope**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`filescope`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`solutioncomponentconfiguration_filescope`|

#### FileScope Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Individual**|
|2|**Global**|

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

### <a name="BKMK_InvokeSubstitution"></a> InvokeSubstitution

|Property|Value|
|---|---|
|Description|**Boolean that indicates if invoke substitution API will be used on component on template mode import**|
|DisplayName|**Invoke substitution API on component**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`invokesubstitution`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_solutioncomponentconfiguration_invokesubstitution`|
|DefaultValue|False|
|True Label||
|False Label||

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

### <a name="BKMK_isdisplayable"></a> isdisplayable

|Property|Value|
|---|---|
|Description|**Boolean that indicates if the component has user interface enabled.**|
|DisplayName|**Displayable**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isdisplayable`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_solutioncomponentconfiguration_isdisplayable`|
|DefaultValue|False|
|True Label||
|False Label||

### <a name="BKMK_IsOneToOneChildComponent"></a> IsOneToOneChildComponent

|Property|Value|
|---|---|
|Description|**Boolean that indicates if the component is 1-1 child component.**|
|DisplayName|**Is 1-1 Child Component**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isonetoonechildcomponent`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_isonetoonechildcomponent`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsSoftDeleteEnabled"></a> IsSoftDeleteEnabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsSoftDeleteEnabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`issoftdeleteenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_issoftdeleteenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsVersioningEnabled"></a> IsVersioningEnabled

|Property|Value|
|---|---|
|Description|**Boolean that indicates if the component should be versioned.**|
|DisplayName|**Is Versioning Enabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isversioningenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_isversioningenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_KeepActiveCustomizationAfterConversion"></a> KeepActiveCustomizationAfterConversion

|Property|Value|
|---|---|
|Description|**Boolean that indicates if the component should retain its unmanaged customization after conversion.**|
|DisplayName|**Keep Active Customization After Conversion**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`keepactivecustomizationafterconversion`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_solutioncomponentconfiguration_keepactivecustomizationafterconversion`|
|DefaultValue|False|
|True Label||
|False Label||

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

### <a name="BKMK_solutioncomponentconfigurationId"></a> solutioncomponentconfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Solution Component Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutioncomponentconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Solution Component Configuration**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentconfiguration_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Solution Component Configuration**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentconfiguration_statuscode`|

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

- [entity_solutioncomponentconfiguration](#BKMK_entity_solutioncomponentconfiguration)
- [lk_solutioncomponentconfiguration_createdby](#BKMK_lk_solutioncomponentconfiguration_createdby)
- [lk_solutioncomponentconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentconfiguration_createdonbehalfby)
- [lk_solutioncomponentconfiguration_modifiedby](#BKMK_lk_solutioncomponentconfiguration_modifiedby)
- [lk_solutioncomponentconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby)
- [organization_solutioncomponentconfiguration](#BKMK_organization_solutioncomponentconfiguration)

### <a name="BKMK_entity_solutioncomponentconfiguration"></a> entity_solutioncomponentconfiguration

One-To-Many Relationship: [entity entity_solutioncomponentconfiguration](entity.md#BKMK_entity_solutioncomponentconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`entity`|
|ReferencedAttribute|`entityid`|
|ReferencingAttribute|`entityid`|
|ReferencingEntityNavigationPropertyName|`EntityId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_solutioncomponentconfiguration_createdby"></a> lk_solutioncomponentconfiguration_createdby

One-To-Many Relationship: [systemuser lk_solutioncomponentconfiguration_createdby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentconfiguration_createdonbehalfby"></a> lk_solutioncomponentconfiguration_createdonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentconfiguration_modifiedby"></a> lk_solutioncomponentconfiguration_modifiedby

One-To-Many Relationship: [systemuser lk_solutioncomponentconfiguration_modifiedby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentconfiguration_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentconfiguration_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_solutioncomponentconfiguration"></a> organization_solutioncomponentconfiguration

One-To-Many Relationship: [organization organization_solutioncomponentconfiguration](organization.md#BKMK_organization_solutioncomponentconfiguration)

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

- [solutioncomponentconfig_solutioncomponentattrconfig](#BKMK_solutioncomponentconfig_solutioncomponentattrconfig)
- [solutioncomponentconfiguration_AsyncOperations](#BKMK_solutioncomponentconfiguration_AsyncOperations)
- [solutioncomponentconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)
- [solutioncomponentconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord)
- [solutioncomponentconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord)
- [solutioncomponentconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders)
- [solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentconfiguration_ProcessSession](#BKMK_solutioncomponentconfiguration_ProcessSession)
- [solutioncomponentconfiguration_SyncErrors](#BKMK_solutioncomponentconfiguration_SyncErrors)

### <a name="BKMK_solutioncomponentconfig_solutioncomponentattrconfig"></a> solutioncomponentconfig_solutioncomponentattrconfig

Many-To-One Relationship: [solutioncomponentattributeconfiguration solutioncomponentconfig_solutioncomponentattrconfig](solutioncomponentattributeconfiguration.md#BKMK_solutioncomponentconfig_solutioncomponentattrconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentattributeconfiguration`|
|ReferencingAttribute|`solutioncomponentconfigurationid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfig_solutioncomponentattrconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_AsyncOperations"></a> solutioncomponentconfiguration_AsyncOperations

Many-To-One Relationship: [asyncoperation solutioncomponentconfiguration_AsyncOperations](asyncoperation.md#BKMK_solutioncomponentconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_BulkDeleteFailures"></a> solutioncomponentconfiguration_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure solutioncomponentconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_solutioncomponentconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_DuplicateBaseRecord"></a> solutioncomponentconfiguration_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord solutioncomponentconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_solutioncomponentconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord"></a> solutioncomponentconfiguration_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord solutioncomponentconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_solutioncomponentconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_MailboxTrackingFolders"></a> solutioncomponentconfiguration_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder solutioncomponentconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_solutioncomponentconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentconfiguration_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess solutioncomponentconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_solutioncomponentconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_ProcessSession"></a> solutioncomponentconfiguration_ProcessSession

Many-To-One Relationship: [processsession solutioncomponentconfiguration_ProcessSession](processsession.md#BKMK_solutioncomponentconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentconfiguration_SyncErrors"></a> solutioncomponentconfiguration_SyncErrors

Many-To-One Relationship: [syncerror solutioncomponentconfiguration_SyncErrors](syncerror.md#BKMK_solutioncomponentconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentconfiguration_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.solutioncomponentconfiguration?displayProperty=fullName>
