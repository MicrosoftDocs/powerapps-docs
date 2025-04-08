---
title: "Sdk Message Filter (SdkMessageFilter) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sdk Message Filter (SdkMessageFilter) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sdk Message Filter (SdkMessageFilter) table/entity reference (Microsoft Dataverse)

Filter that defines which SDK messages are valid for each type of entity.

## Messages

The following table lists the messages for the Sdk Message Filter (SdkMessageFilter) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sdkmessagefilters(*sdkmessagefilterid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /sdkmessagefilters<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Sdk Message Filter (SdkMessageFilter) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sdk Message Filter** |
| **DisplayCollectionName** | **Sdk Message Filters** |
| **SchemaName** | `SdkMessageFilter` |
| **CollectionSchemaName** | `SdkMessageFilters` |
| **EntitySetName** | `sdkmessagefilters`|
| **LogicalName** | `sdkmessagefilter` |
| **LogicalCollectionName** | `sdkmessagefilters` |
| **PrimaryIdAttribute** | `sdkmessagefilterid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Availability](#BKMK_Availability)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsCustomProcessingStepAllowed](#BKMK_IsCustomProcessingStepAllowed)
- [Name](#BKMK_Name)
- [RestrictionLevel](#BKMK_RestrictionLevel)
- [SdkMessageFilterId](#BKMK_SdkMessageFilterId)
- [SdkMessageId](#BKMK_SdkMessageId)

### <a name="BKMK_Availability"></a> Availability

|Property|Value|
|---|---|
|Description|**Identifies where a method will be exposed. 0 - Server, 1 - Client, 2 - both.**|
|DisplayName|**Availability**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`availability`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the component is introduced.**|
|DisplayName|**Introduced Version**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`introducedversion`|
|RequiredLevel|None|
|Type|String|
|Format|VersionNumber|
|FormatName|VersionNumber|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|48|

### <a name="BKMK_IsCustomProcessingStepAllowed"></a> IsCustomProcessingStepAllowed

|Property|Value|
|---|---|
|Description|**Indicates whether a custom SDK message processing step is allowed.**|
|DisplayName|**Custom Processing Step Allowed**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`iscustomprocessingstepallowed`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`sdkmessagefilter_iscustomprocessingstepallowed`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the SDK message filter.**|
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
|MaxLength|256|

### <a name="BKMK_RestrictionLevel"></a> RestrictionLevel

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`restrictionlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|0|

### <a name="BKMK_SdkMessageFilterId"></a> SdkMessageFilterId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message filter entity.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessagefilterid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SdkMessageId"></a> SdkMessageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the related SDK message.**|
|DisplayName|**SDK Message ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|sdkmessage|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [IsVisible](#BKMK_IsVisible)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PrimaryObjectTypeCode](#BKMK_PrimaryObjectTypeCode)
- [SdkMessageFilterIdUnique](#BKMK_SdkMessageFilterIdUnique)
- [SecondaryObjectTypeCode](#BKMK_SecondaryObjectTypeCode)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)
- [WorkflowSdkStepEnabled](#BKMK_WorkflowSdkStepEnabled)

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
|DefaultFormValue|-1|
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
|Description|**Unique identifier of the user who created the SDK message filter.**|
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
|Description|**Date and time when the SDK message filter was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the sdkmessagefilter.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CustomizationLevel"></a> CustomizationLevel

|Property|Value|
|---|---|
|Description|**Customization level of the SDK message filter.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationlevel`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|255|
|MinValue|-255|

### <a name="BKMK_IsManaged"></a> IsManaged

|Property|Value|
|---|---|
|Description|**Information that specifies whether this component is managed.**|
|DisplayName|**State**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`ismanaged`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`ismanaged`|
|DefaultValue|False|
|True Label|Managed|
|False Label|Unmanaged|

### <a name="BKMK_IsVisible"></a> IsVisible

|Property|Value|
|---|---|
|Description|**Indicates whether the filter should be visible.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvisible`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`sdkmessagefilter_isvisible`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the SDK message filter.**|
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
|Description|**Date and time when the SDK message filter was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who last modified the sdkmessagefilter.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the organization with which the SDK message filter is associated.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
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
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_PrimaryObjectTypeCode"></a> PrimaryObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the SDK message filter is primarily associated.**|
|DisplayName|**Primary Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`primaryobjecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_SdkMessageFilterIdUnique"></a> SdkMessageFilterIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message filter.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessagefilteridunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SecondaryObjectTypeCode"></a> SecondaryObjectTypeCode

|Property|Value|
|---|---|
|Description|**Type of entity with which the SDK message filter is secondarily associated.**|
|DisplayName|**Secondary Object Type Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`secondaryobjecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

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
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_WorkflowSdkStepEnabled"></a> WorkflowSdkStepEnabled

|Property|Value|
|---|---|
|Description|**Whether or not the SDK message can be called from a workflow.**|
|DisplayName|**WorkflowSdkStepEnabled**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowsdkstepenabled`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessagefilter_workflowsdkstepenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_sdkmessagefilter](#BKMK_createdby_sdkmessagefilter)
- [lk_sdkmessagefilter_createdonbehalfby](#BKMK_lk_sdkmessagefilter_createdonbehalfby)
- [lk_sdkmessagefilter_modifiedonbehalfby](#BKMK_lk_sdkmessagefilter_modifiedonbehalfby)
- [modifiedby_sdkmessagefilter](#BKMK_modifiedby_sdkmessagefilter)
- [organization_sdkmessagefilter](#BKMK_organization_sdkmessagefilter)
- [sdkmessageid_sdkmessagefilter](#BKMK_sdkmessageid_sdkmessagefilter)

### <a name="BKMK_createdby_sdkmessagefilter"></a> createdby_sdkmessagefilter

One-To-Many Relationship: [systemuser createdby_sdkmessagefilter](systemuser.md#BKMK_createdby_sdkmessagefilter)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessagefilter_createdonbehalfby"></a> lk_sdkmessagefilter_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessagefilter_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessagefilter_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessagefilter_modifiedonbehalfby"></a> lk_sdkmessagefilter_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessagefilter_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessagefilter_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_sdkmessagefilter"></a> modifiedby_sdkmessagefilter

One-To-Many Relationship: [systemuser modifiedby_sdkmessagefilter](systemuser.md#BKMK_modifiedby_sdkmessagefilter)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sdkmessagefilter"></a> organization_sdkmessagefilter

One-To-Many Relationship: [organization organization_sdkmessagefilter](organization.md#BKMK_organization_sdkmessagefilter)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_sdkmessageid_sdkmessagefilter"></a> sdkmessageid_sdkmessagefilter

One-To-Many Relationship: [sdkmessage sdkmessageid_sdkmessagefilter](sdkmessage.md#BKMK_sdkmessageid_sdkmessagefilter)

|Property|Value|
|---|---|
|ReferencedEntity|`sdkmessage`|
|ReferencedAttribute|`sdkmessageid`|
|ReferencingAttribute|`sdkmessageid`|
|ReferencingEntityNavigationPropertyName|`sdkmessageid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

### <a name="BKMK_sdkmessagefilterid_sdkmessageprocessingstep"></a> sdkmessagefilterid_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep sdkmessagefilterid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_sdkmessagefilterid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`sdkmessagefilterid`|
|ReferencedEntityNavigationPropertyName|`sdkmessagefilterid_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sdkmessagefilter?displayProperty=fullName>
