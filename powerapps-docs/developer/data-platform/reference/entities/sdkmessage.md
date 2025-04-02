---
title: "Sdk Message (SdkMessage) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Sdk Message (SdkMessage) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Sdk Message (SdkMessage) table/entity reference (Microsoft Dataverse)

Message that is supported by the SDK.

## Messages

The following table lists the messages for the Sdk Message (SdkMessage) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /sdkmessages(*sdkmessageid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /sdkmessages<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Sdk Message (SdkMessage) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Sdk Message** |
| **DisplayCollectionName** | **Sdk Messages** |
| **SchemaName** | `SdkMessage` |
| **CollectionSchemaName** | `SdkMessages` |
| **EntitySetName** | `sdkmessages`|
| **LogicalName** | `sdkmessage` |
| **LogicalCollectionName** | `sdkmessages` |
| **PrimaryIdAttribute** | `sdkmessageid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AutoTransact](#BKMK_AutoTransact)
- [Availability](#BKMK_Availability)
- [CategoryName](#BKMK_CategoryName)
- [ExecutePrivilegeName](#BKMK_ExecutePrivilegeName)
- [Expand](#BKMK_Expand)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsActive](#BKMK_IsActive)
- [IsPrivate](#BKMK_IsPrivate)
- [IsReadOnly](#BKMK_IsReadOnly)
- [Name](#BKMK_Name)
- [SdkMessageId](#BKMK_SdkMessageId)
- [Template](#BKMK_Template)

### <a name="BKMK_AutoTransact"></a> AutoTransact

|Property|Value|
|---|---|
|Description|**Information about whether the SDK message is automatically transacted.**|
|DisplayName|**Auto Transact**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`autotransact`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_autotransact`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_CategoryName"></a> CategoryName

|Property|Value|
|---|---|
|Description|**If this is a categorized method, this is the name, otherwise None.**|
|DisplayName|**Category Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`categoryname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|25|

### <a name="BKMK_ExecutePrivilegeName"></a> ExecutePrivilegeName

|Property|Value|
|---|---|
|Description|**Name of the privilege that allows execution of the SDK message**|
|DisplayName|**Execute Privilege Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`executeprivilegename`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Expand"></a> Expand

|Property|Value|
|---|---|
|Description|**Indicates whether the SDK message should have its requests expanded per primary entity defined in its filters.**|
|DisplayName|**Expand**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`expand`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_expand`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

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

### <a name="BKMK_IsActive"></a> IsActive

|Property|Value|
|---|---|
|Description|**Information about whether the SDK message is active.**|
|DisplayName|**Is Active**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isactive`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_isactive`|
|DefaultValue|True|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsPrivate"></a> IsPrivate

|Property|Value|
|---|---|
|Description|**Indicates whether the SDK message is private.**|
|DisplayName|**Is Private**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isprivate`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_isprivate`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_IsReadOnly"></a> IsReadOnly

|Property|Value|
|---|---|
|Description|**Identifies whether an SDK message will be ReadOnly or Read Write. false - ReadWrite, true - ReadOnly .**|
|DisplayName|**Intent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isreadonly`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`isoperationintentreadonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the SDK message.**|
|DisplayName|**Name**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|

### <a name="BKMK_SdkMessageId"></a> SdkMessageId

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message entity.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Template"></a> Template

|Property|Value|
|---|---|
|Description|**Indicates whether the SDK message is a template.**|
|DisplayName|**Template**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`template`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_template`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CustomizationLevel](#BKMK_CustomizationLevel)
- [IsManaged](#BKMK_IsManaged)
- [IsValidForExecuteAsync](#BKMK_IsValidForExecuteAsync)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SdkMessageIdUnique](#BKMK_SdkMessageIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [ThrottleSettings](#BKMK_ThrottleSettings)
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
|Description|**Unique identifier of the user who created the SDK message.**|
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
|Description|**Date and time when the SDK message was created.**|
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
|Description|**Unique identifier of the delegate user who created the sdkmessage.**|
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
|Description|**Customization level of the SDK message.**|
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

### <a name="BKMK_IsValidForExecuteAsync"></a> IsValidForExecuteAsync

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Is Valid for Execute Async**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvalidforexecuteasync`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`sdkmessage_isvalidforexecuteasync`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the SDK message.**|
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
|Description|**Date and time when the SDK message was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the sdkmessage.**|
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
|Description|**Unique identifier of the organization with which the SDK message is associated.**|
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

### <a name="BKMK_SdkMessageIdUnique"></a> SdkMessageIdUnique

|Property|Value|
|---|---|
|Description|**Unique identifier of the SDK message.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`sdkmessageidunique`|
|RequiredLevel|SystemRequired|
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

### <a name="BKMK_ThrottleSettings"></a> ThrottleSettings

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Throttle Settings**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`throttlesettings`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|512|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Number that identifies a specific revision of the SDK message.**|
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
|GlobalChoiceName|`sdkmessage_workflowsdkstepenabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [createdby_sdkmessage](#BKMK_createdby_sdkmessage)
- [lk_sdkmessage_createdonbehalfby](#BKMK_lk_sdkmessage_createdonbehalfby)
- [lk_sdkmessage_modifiedonbehalfby](#BKMK_lk_sdkmessage_modifiedonbehalfby)
- [modifiedby_sdkmessage](#BKMK_modifiedby_sdkmessage)
- [organization_sdkmessage](#BKMK_organization_sdkmessage)

### <a name="BKMK_createdby_sdkmessage"></a> createdby_sdkmessage

One-To-Many Relationship: [systemuser createdby_sdkmessage](systemuser.md#BKMK_createdby_sdkmessage)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessage_createdonbehalfby"></a> lk_sdkmessage_createdonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessage_createdonbehalfby](systemuser.md#BKMK_lk_sdkmessage_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_sdkmessage_modifiedonbehalfby"></a> lk_sdkmessage_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_sdkmessage_modifiedonbehalfby](systemuser.md#BKMK_lk_sdkmessage_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_modifiedby_sdkmessage"></a> modifiedby_sdkmessage

One-To-Many Relationship: [systemuser modifiedby_sdkmessage](systemuser.md#BKMK_modifiedby_sdkmessage)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_sdkmessage"></a> organization_sdkmessage

One-To-Many Relationship: [organization organization_sdkmessage](organization.md#BKMK_organization_sdkmessage)

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

- [sdkmessage_customapi](#BKMK_sdkmessage_customapi)
- [sdkmessage_serviceplanmapping](#BKMK_sdkmessage_serviceplanmapping)
- [sdkmessageid_sdkmessagefilter](#BKMK_sdkmessageid_sdkmessagefilter)
- [sdkmessageid_sdkmessageprocessingstep](#BKMK_sdkmessageid_sdkmessageprocessingstep)

### <a name="BKMK_sdkmessage_customapi"></a> sdkmessage_customapi

Many-To-One Relationship: [customapi sdkmessage_customapi](customapi.md#BKMK_sdkmessage_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`customapi`|
|ReferencingAttribute|`sdkmessageid`|
|ReferencedEntityNavigationPropertyName|`CustomAPIId`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sdkmessage_serviceplanmapping"></a> sdkmessage_serviceplanmapping

Many-To-One Relationship: [serviceplanmapping sdkmessage_serviceplanmapping](serviceplanmapping.md#BKMK_sdkmessage_serviceplanmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`serviceplanmapping`|
|ReferencingAttribute|`sdkmessage`|
|ReferencedEntityNavigationPropertyName|`sdkmessage_serviceplanmapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 10000<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sdkmessageid_sdkmessagefilter"></a> sdkmessageid_sdkmessagefilter

Many-To-One Relationship: [sdkmessagefilter sdkmessageid_sdkmessagefilter](sdkmessagefilter.md#BKMK_sdkmessageid_sdkmessagefilter)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessagefilter`|
|ReferencingAttribute|`sdkmessageid`|
|ReferencedEntityNavigationPropertyName|`sdkmessageid_sdkmessagefilter`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_sdkmessageid_sdkmessageprocessingstep"></a> sdkmessageid_sdkmessageprocessingstep

Many-To-One Relationship: [sdkmessageprocessingstep sdkmessageid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_sdkmessageid_sdkmessageprocessingstep)

|Property|Value|
|---|---|
|ReferencingEntity|`sdkmessageprocessingstep`|
|ReferencingAttribute|`sdkmessageid`|
|ReferencedEntityNavigationPropertyName|`sdkmessageid_sdkmessageprocessingstep`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.sdkmessage?displayProperty=fullName>
