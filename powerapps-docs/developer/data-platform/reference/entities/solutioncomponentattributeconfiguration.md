---
title: "Solution Component Attribute Configuration (solutioncomponentattributeconfiguration) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Solution Component Attribute Configuration (solutioncomponentattributeconfiguration) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Solution Component Attribute Configuration (solutioncomponentattributeconfiguration) table/entity reference (Microsoft Dataverse)



## Messages

The following table lists the messages for the Solution Component Attribute Configuration (solutioncomponentattributeconfiguration) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /solutioncomponentattributeconfigurations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `CreateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.CreateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest>|
| `Delete`<br />Event: False |`DELETE` /solutioncomponentattributeconfigurations(*solutioncomponentattributeconfigurationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `IsValidStateTransition`<br />Event: False |<xref:Microsoft.Dynamics.CRM.IsValidStateTransition?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.IsValidStateTransitionRequest>|
| `Retrieve`<br />Event: False |`GET` /solutioncomponentattributeconfigurations(*solutioncomponentattributeconfigurationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /solutioncomponentattributeconfigurations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `SetState`<br />Event: False |`PATCH` /solutioncomponentattributeconfigurations(*solutioncomponentattributeconfigurationid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: False |`PATCH` /solutioncomponentattributeconfigurations(*solutioncomponentattributeconfigurationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `UpdateMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpdateMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest>|
| `Upsert`<br />Event: False |`PATCH` /solutioncomponentattributeconfigurations(*solutioncomponentattributeconfigurationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|
| `UpsertMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.UpsertMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Xrm.Sdk.Messages.UpsertMultipleRequest>|

## Properties

The following table lists selected properties for the Solution Component Attribute Configuration (solutioncomponentattributeconfiguration) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Solution Component Attribute Configuration** |
| **DisplayCollectionName** | **Solution Component Attribute Configurations** |
| **SchemaName** | `solutioncomponentattributeconfiguration` |
| **CollectionSchemaName** | `solutioncomponentattributeconfigurations` |
| **EntitySetName** | `solutioncomponentattributeconfigurations`|
| **LogicalName** | `solutioncomponentattributeconfiguration` |
| **LogicalCollectionName** | `solutioncomponentattributeconfigurations` |
| **PrimaryIdAttribute** | `solutioncomponentattributeconfigurationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AttributeId](#BKMK_AttributeId)
- [CustomManagedBehaviorType](#BKMK_CustomManagedBehaviorType)
- [DependencyRemovalCapability](#BKMK_DependencyRemovalCapability)
- [EncodingFormat](#BKMK_EncodingFormat)
- [FileExtension](#BKMK_FileExtension)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InvokeSubstitutionForAttribute](#BKMK_InvokeSubstitutionForAttribute)
- [IsCustomizable](#BKMK_IsCustomizable)
- [IsEnabledForDependencyExtraction](#BKMK_IsEnabledForDependencyExtraction)
- [IsExportDisabled](#BKMK_IsExportDisabled)
- [IsExportedAsFile](#BKMK_IsExportedAsFile)
- [IsPrefixedByTemplate](#BKMK_IsPrefixedByTemplate)
- [name](#BKMK_name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [solutioncomponentattributeconfigurationId](#BKMK_solutioncomponentattributeconfigurationId)
- [SolutionComponentConfigurationId](#BKMK_SolutionComponentConfigurationId)
- [statecode](#BKMK_statecode)
- [statuscode](#BKMK_statuscode)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)

### <a name="BKMK_AttributeId"></a> AttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier for Attribute associated with Solution Component Attribute Configuration.**|
|DisplayName|**Attribute**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`attributeid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|attribute|

### <a name="BKMK_CustomManagedBehaviorType"></a> CustomManagedBehaviorType

|Property|Value|
|---|---|
|Description||
|DisplayName|**Custom Managed Behavior Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`custommanagedbehaviortype`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue|0|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_custommanagedbehaviortype`|

#### CustomManagedBehaviorType Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**State Transition**|

### <a name="BKMK_DependencyRemovalCapability"></a> DependencyRemovalCapability

|Property|Value|
|---|---|
|Description|**Indicates whether 1 click dependency removal is enabled or disabled**|
|DisplayName|**dependency removal capability**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`dependencyremovalcapability`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentattributeconfiguration_dependencyremovalcapability`|

#### DependencyRemovalCapability Choices/Options

|Value|Label|
|---|---|
|0|**Disabled**|
|1|**Enabled**|

### <a name="BKMK_EncodingFormat"></a> EncodingFormat

|Property|Value|
|---|---|
|Description||
|DisplayName|**Encoding Format**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`encodingformat`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentattributeconfiguration_encodingformat`|

#### EncodingFormat Choices/Options

|Value|Label|
|---|---|
|0|**None**|
|1|**Base64**|
|2|**UTF8**|

### <a name="BKMK_FileExtension"></a> FileExtension

|Property|Value|
|---|---|
|Description||
|DisplayName|**File Extension**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fileextension`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|30|

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

### <a name="BKMK_InvokeSubstitutionForAttribute"></a> InvokeSubstitutionForAttribute

|Property|Value|
|---|---|
|Description|**Boolean that indicates if invoke substitution API will be used on attribute on template mode import**|
|DisplayName|**Invoke substitution API on attribute**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`invokesubstitutionforattribute`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`_solutioncomponentattributeconfiguration_invokesubstitutionforattribute`|
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

### <a name="BKMK_IsEnabledForDependencyExtraction"></a> IsEnabledForDependencyExtraction

|Property|Value|
|---|---|
|Description||
|DisplayName|**Enabled for Dependency Extraction**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isenabledfordependencyextraction`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_isenabledfordependencyextraction`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsExportDisabled"></a> IsExportDisabled

|Property|Value|
|---|---|
|Description||
|DisplayName|**Export Disabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isexportdisabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_isexportdisabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsExportedAsFile"></a> IsExportedAsFile

|Property|Value|
|---|---|
|Description||
|DisplayName|**IsExportedAsFile**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isexportedasfile`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_isexportedasfile`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPrefixedByTemplate"></a> IsPrefixedByTemplate

|Property|Value|
|---|---|
|Description||
|DisplayName|**Prefixed by Template**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isprefixedbytemplate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`solutioncomponentattributeconfiguration_isprefixedbyttemplate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_solutioncomponentattributeconfigurationId"></a> solutioncomponentattributeconfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for entity instances**|
|DisplayName|**Solution Component Attribute Configuration**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`solutioncomponentattributeconfigurationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SolutionComponentConfigurationId"></a> SolutionComponentConfigurationId

|Property|Value|
|---|---|
|Description|**Unique identifier for the Solution Component Configuration associated with Solution Component Attribute Configuration.**|
|DisplayName|**Solution Component Attribute Configuration**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`solutioncomponentconfigurationid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|solutioncomponentconfiguration|

### <a name="BKMK_statecode"></a> statecode

|Property|Value|
|---|---|
|Description|**Status of the Solution Component Attribute Configuration**|
|DisplayName|**Status**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statecode`|
|RequiredLevel|SystemRequired|
|Type|State|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentattributeconfiguration_statecode`|

#### statecode Choices/Options

|Value|Details|
|---|---|
|0|Label: **Active**<br />DefaultStatus: 1<br />InvariantName: `Active`|
|1|Label: **Inactive**<br />DefaultStatus: 2<br />InvariantName: `Inactive`|

### <a name="BKMK_statuscode"></a> statuscode

|Property|Value|
|---|---|
|Description|**Reason for the status of the Solution Component Attribute Configuration**|
|DisplayName|**Status Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`statuscode`|
|RequiredLevel|None|
|Type|Status|
|DefaultFormValue||
|GlobalChoiceName|`solutioncomponentattributeconfiguration_statuscode`|

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

- [attribute_solutioncomponentattrconfig](#BKMK_attribute_solutioncomponentattrconfig)
- [lk_solutioncomponentattributeconfiguration_createdby](#BKMK_lk_solutioncomponentattributeconfiguration_createdby)
- [lk_solutioncomponentattributeconfiguration_createdonbehalfby](#BKMK_lk_solutioncomponentattributeconfiguration_createdonbehalfby)
- [lk_solutioncomponentattributeconfiguration_modifiedby](#BKMK_lk_solutioncomponentattributeconfiguration_modifiedby)
- [lk_solutioncomponentattributeconfiguration_modifiedonbehalfby](#BKMK_lk_solutioncomponentattributeconfiguration_modifiedonbehalfby)
- [organization_solutioncomponentattributeconfiguration](#BKMK_organization_solutioncomponentattributeconfiguration)
- [solutioncomponentconfig_solutioncomponentattrconfig](#BKMK_solutioncomponentconfig_solutioncomponentattrconfig)

### <a name="BKMK_attribute_solutioncomponentattrconfig"></a> attribute_solutioncomponentattrconfig

One-To-Many Relationship: [attribute attribute_solutioncomponentattrconfig](attribute.md#BKMK_attribute_solutioncomponentattrconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`attribute`|
|ReferencedAttribute|`attributeid`|
|ReferencingAttribute|`attributeid`|
|ReferencingEntityNavigationPropertyName|`AttributeId`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|

### <a name="BKMK_lk_solutioncomponentattributeconfiguration_createdby"></a> lk_solutioncomponentattributeconfiguration_createdby

One-To-Many Relationship: [systemuser lk_solutioncomponentattributeconfiguration_createdby](systemuser.md#BKMK_lk_solutioncomponentattributeconfiguration_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentattributeconfiguration_createdonbehalfby"></a> lk_solutioncomponentattributeconfiguration_createdonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentattributeconfiguration_createdonbehalfby](systemuser.md#BKMK_lk_solutioncomponentattributeconfiguration_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentattributeconfiguration_modifiedby"></a> lk_solutioncomponentattributeconfiguration_modifiedby

One-To-Many Relationship: [systemuser lk_solutioncomponentattributeconfiguration_modifiedby](systemuser.md#BKMK_lk_solutioncomponentattributeconfiguration_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_solutioncomponentattributeconfiguration_modifiedonbehalfby"></a> lk_solutioncomponentattributeconfiguration_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_solutioncomponentattributeconfiguration_modifiedonbehalfby](systemuser.md#BKMK_lk_solutioncomponentattributeconfiguration_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_solutioncomponentattributeconfiguration"></a> organization_solutioncomponentattributeconfiguration

One-To-Many Relationship: [organization organization_solutioncomponentattributeconfiguration](organization.md#BKMK_organization_solutioncomponentattributeconfiguration)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_solutioncomponentconfig_solutioncomponentattrconfig"></a> solutioncomponentconfig_solutioncomponentattrconfig

One-To-Many Relationship: [solutioncomponentconfiguration solutioncomponentconfig_solutioncomponentattrconfig](solutioncomponentconfiguration.md#BKMK_solutioncomponentconfig_solutioncomponentattrconfig)

|Property|Value|
|---|---|
|ReferencedEntity|`solutioncomponentconfiguration`|
|ReferencedAttribute|`solutioncomponentconfigurationid`|
|ReferencingAttribute|`solutioncomponentconfigurationid`|
|ReferencingEntityNavigationPropertyName|`solutioncomponentconfigurationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [solutioncomponentattributeconfiguration_AsyncOperations](#BKMK_solutioncomponentattributeconfiguration_AsyncOperations)
- [solutioncomponentattributeconfiguration_BulkDeleteFailures](#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures)
- [solutioncomponentattributeconfiguration_DuplicateBaseRecord](#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord)
- [solutioncomponentattributeconfiguration_DuplicateMatchingRecord](#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord)
- [solutioncomponentattributeconfiguration_MailboxTrackingFolders](#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders)
- [solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses](#BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses)
- [solutioncomponentattributeconfiguration_ProcessSession](#BKMK_solutioncomponentattributeconfiguration_ProcessSession)
- [solutioncomponentattributeconfiguration_SyncErrors](#BKMK_solutioncomponentattributeconfiguration_SyncErrors)

### <a name="BKMK_solutioncomponentattributeconfiguration_AsyncOperations"></a> solutioncomponentattributeconfiguration_AsyncOperations

Many-To-One Relationship: [asyncoperation solutioncomponentattributeconfiguration_AsyncOperations](asyncoperation.md#BKMK_solutioncomponentattributeconfiguration_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures"></a> solutioncomponentattributeconfiguration_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure solutioncomponentattributeconfiguration_BulkDeleteFailures](bulkdeletefailure.md#BKMK_solutioncomponentattributeconfiguration_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord"></a> solutioncomponentattributeconfiguration_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord solutioncomponentattributeconfiguration_DuplicateBaseRecord](duplicaterecord.md#BKMK_solutioncomponentattributeconfiguration_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_DuplicateBaseRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord"></a> solutioncomponentattributeconfiguration_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord solutioncomponentattributeconfiguration_DuplicateMatchingRecord](duplicaterecord.md#BKMK_solutioncomponentattributeconfiguration_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_DuplicateMatchingRecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders"></a> solutioncomponentattributeconfiguration_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder solutioncomponentattributeconfiguration_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_solutioncomponentattributeconfiguration_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses"></a> solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_ProcessSession"></a> solutioncomponentattributeconfiguration_ProcessSession

Many-To-One Relationship: [processsession solutioncomponentattributeconfiguration_ProcessSession](processsession.md#BKMK_solutioncomponentattributeconfiguration_ProcessSession)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_ProcessSession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_solutioncomponentattributeconfiguration_SyncErrors"></a> solutioncomponentattributeconfiguration_SyncErrors

Many-To-One Relationship: [syncerror solutioncomponentattributeconfiguration_SyncErrors](syncerror.md#BKMK_solutioncomponentattributeconfiguration_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`solutioncomponentattributeconfiguration_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.solutioncomponentattributeconfiguration?displayProperty=fullName>
