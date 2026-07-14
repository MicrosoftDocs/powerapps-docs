---
title: "Relationship Attribute (RelationshipAttribute) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Relationship Attribute (RelationshipAttribute) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Relationship Attribute (RelationshipAttribute) table/entity reference (Microsoft Dataverse)

Stores relationship attributes mapping for Multi-predicate relationship

## Messages

The following table lists the messages for the Relationship Attribute (RelationshipAttribute) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /relationshipattributes(*relationshipattributeid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /relationshipattributes<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|

## Properties

The following table lists selected properties for the Relationship Attribute (RelationshipAttribute) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Relationship Attribute** |
| **DisplayCollectionName** | **Relationship Attributes** |
| **SchemaName** | `RelationshipAttribute` |
| **CollectionSchemaName** | `RelationshipAttributes` |
| **EntitySetName** | `relationshipattributes`|
| **LogicalName** | `relationshipattribute` |
| **LogicalCollectionName** | `relationshipattributes` |
| **PrimaryIdAttribute** | `relationshipattributeid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IsCustomizable](#BKMK_IsCustomizable)
- [Name](#BKMK_Name)
- [ReferencedAttributeId](#BKMK_ReferencedAttributeId)
- [ReferencingAttributeId](#BKMK_ReferencingAttributeId)
- [RelationshipAttributeId](#BKMK_RelationshipAttributeId)
- [RelationshipId](#BKMK_RelationshipId)

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

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Display Name**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|128|

### <a name="BKMK_ReferencedAttributeId"></a> ReferencedAttributeId

|Property|Value|
|---|---|
|Description|**Referenced Attribute Id**|
|DisplayName|**Referenced Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencedattributeid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|attribute|

### <a name="BKMK_ReferencingAttributeId"></a> ReferencingAttributeId

|Property|Value|
|---|---|
|Description|**Referencing Attribute Id**|
|DisplayName|**Referencing Attribute Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`referencingattributeid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|attribute|

### <a name="BKMK_RelationshipAttributeId"></a> RelationshipAttributeId

|Property|Value|
|---|---|
|Description|**Unique identifier of the relationship attribute**|
|DisplayName|**Relationship Attribute Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relationshipattributeid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|---|---|
|Description|**Relationship Id**|
|DisplayName|**Relationship Id**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshipid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|relationship|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [versionnumber](#BKMK_versionnumber)

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

### <a name="BKMK_versionnumber"></a> versionnumber

|Property|Value|
|---|---|
|Description|**Version number of Image descriptor.**|
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

- [organization_relationshipattribute](#BKMK_organization_relationshipattribute)
- [referencedattribute_relationshipattribute](#BKMK_referencedattribute_relationshipattribute)
- [referencingattribute_relationshipattribute](#BKMK_referencingattribute_relationshipattribute)
- [relationship_relationshipattribute](#BKMK_relationship_relationshipattribute)

### <a name="BKMK_organization_relationshipattribute"></a> organization_relationshipattribute

One-To-Many Relationship: [organization organization_relationshipattribute](organization.md#BKMK_organization_relationshipattribute)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_referencedattribute_relationshipattribute"></a> referencedattribute_relationshipattribute

One-To-Many Relationship: [attribute referencedattribute_relationshipattribute](attribute.md#BKMK_referencedattribute_relationshipattribute)

|Property|Value|
|---|---|
|ReferencedEntity|`attribute`|
|ReferencedAttribute|`attributeid`|
|ReferencingAttribute|`referencedattributeid`|
|ReferencingEntityNavigationPropertyName|`referencedattributeid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_referencingattribute_relationshipattribute"></a> referencingattribute_relationshipattribute

One-To-Many Relationship: [attribute referencingattribute_relationshipattribute](attribute.md#BKMK_referencingattribute_relationshipattribute)

|Property|Value|
|---|---|
|ReferencedEntity|`attribute`|
|ReferencedAttribute|`attributeid`|
|ReferencingAttribute|`referencingattributeid`|
|ReferencingEntityNavigationPropertyName|`referencingattributeid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_relationship_relationshipattribute"></a> relationship_relationshipattribute

One-To-Many Relationship: [relationship relationship_relationshipattribute](relationship.md#BKMK_relationship_relationshipattribute)

|Property|Value|
|---|---|
|ReferencedEntity|`relationship`|
|ReferencedAttribute|`relationshipid`|
|ReferencingAttribute|`relationshipid`|
|ReferencingEntityNavigationPropertyName|`relationshipid_relationshipattribute`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `Cascade`<br />RollupView: `NoCascade`<br />Share: `Cascade`<br />Unshare: `Cascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [relationshipattribute_AsyncOperations](#BKMK_relationshipattribute_AsyncOperations)
- [relationshipattribute_BulkDeleteFailures](#BKMK_relationshipattribute_BulkDeleteFailures)
- [relationshipattribute_MailboxTrackingFolders](#BKMK_relationshipattribute_MailboxTrackingFolders)
- [relationshipattribute_PrincipalObjectAttributeAccesses](#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses)
- [relationshipattribute_SyncErrors](#BKMK_relationshipattribute_SyncErrors)

### <a name="BKMK_relationshipattribute_AsyncOperations"></a> relationshipattribute_AsyncOperations

Many-To-One Relationship: [asyncoperation relationshipattribute_AsyncOperations](asyncoperation.md#BKMK_relationshipattribute_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`relationshipattribute_AsyncOperations`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_relationshipattribute_BulkDeleteFailures"></a> relationshipattribute_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure relationshipattribute_BulkDeleteFailures](bulkdeletefailure.md#BKMK_relationshipattribute_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`relationshipattribute_BulkDeleteFailures`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_relationshipattribute_MailboxTrackingFolders"></a> relationshipattribute_MailboxTrackingFolders

Many-To-One Relationship: [mailboxtrackingfolder relationshipattribute_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_relationshipattribute_MailboxTrackingFolders)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`relationshipattribute_MailboxTrackingFolders`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_relationshipattribute_PrincipalObjectAttributeAccesses"></a> relationshipattribute_PrincipalObjectAttributeAccesses

Many-To-One Relationship: [principalobjectattributeaccess relationshipattribute_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`relationshipattribute_PrincipalObjectAttributeAccesses`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_relationshipattribute_SyncErrors"></a> relationshipattribute_SyncErrors

Many-To-One Relationship: [syncerror relationshipattribute_SyncErrors](syncerror.md#BKMK_relationshipattribute_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`relationshipattribute_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.relationshipattribute?displayProperty=fullName>
