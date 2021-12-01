---
title: "RelationshipAttribute table/entity reference (Microsoft Dataverse)| MicrosoftDocs"
description: "Includes schema information and supported messages for the RelationshipAttribute table/entity."
ms.date: 10/05/2021
ms.service: "powerapps"
ms.topic: "reference"
ms.assetid: 3948cc48-07c8-7f60-0608-71c37158ad7c
author: "KumarVivek"
ms.author: "kvivek"
manager: "margoc"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# RelationshipAttribute table/entity reference

> [!NOTE]
> Unsure about table vs. entity? See [Developers: Understand terminology in Microsoft Dataverse](/powerapps/developer/data-platform/understand-terminology).

Stores relationship attributes mapping for Multi-predicate relationship

**Added by**: Metadata Extension Solution


## Messages

|Message|Web API Operation|SDK Assembly|
|-|-|-|
|Retrieve|GET [*org URI*]/api/data/v9.0/relationshipattributes(*relationshipattributeid*)<br />See [Retrieve](/powerapps/developer/common-data-service/webapi/retrieve-entity-using-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*>|
|RetrieveMultiple|GET [*org URI*]/api/data/v9.0/relationshipattributes<br />See [Query Data](/powerapps/developer/common-data-service/webapi/query-data-web-api)|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> or <br /><xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple*>|

## Properties

|Property|Value|
|--------|-----|
|CollectionSchemaName|RelationshipAttributes|
|DisplayCollectionName|Relationship Attributes|
|DisplayName|Relationship Attribute|
|EntitySetName|relationshipattributes|
|IsBPFEntity|False|
|LogicalCollectionName|relationshipattributes|
|LogicalName|relationshipattribute|
|OwnershipType|OrganizationOwned|
|PrimaryIdAttribute|relationshipattributeid|
|PrimaryNameAttribute|name|
|SchemaName|RelationshipAttribute|

<a name="writable-attributes"></a>

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IsCustomizable](#BKMK_IsCustomizable)
- [Name](#BKMK_Name)
- [ReferencedAttributeId](#BKMK_ReferencedAttributeId)
- [ReferencingAttributeId](#BKMK_ReferencingAttributeId)
- [RelationshipAttributeId](#BKMK_RelationshipAttributeId)
- [RelationshipId](#BKMK_RelationshipId)


### <a name="BKMK_IsCustomizable"></a> IsCustomizable

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Is Customizable|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|iscustomizable|
|RequiredLevel|SystemRequired|
|Type|ManagedProperty|


### <a name="BKMK_Name"></a> Name

|Property|Value|
|--------|-----|
|Description|Display Name|
|DisplayName|Display Name|
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|name|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ReferencedAttributeId"></a> ReferencedAttributeId

|Property|Value|
|--------|-----|
|Description|Referenced Attribute Id|
|DisplayName|Referenced Attribute Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|referencedattributeid|
|RequiredLevel|SystemRequired|
|Targets|attribute|
|Type|Lookup|


### <a name="BKMK_ReferencingAttributeId"></a> ReferencingAttributeId

|Property|Value|
|--------|-----|
|Description|Referencing Attribute Id|
|DisplayName|Referencing Attribute Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|referencingattributeid|
|RequiredLevel|SystemRequired|
|Targets|attribute|
|Type|Lookup|


### <a name="BKMK_RelationshipAttributeId"></a> RelationshipAttributeId

|Property|Value|
|--------|-----|
|Description|Unique identifier of the relationship attribute|
|DisplayName|Relationship Attribute Id|
|IsValidForForm|False|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|relationshipattributeid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|--------|-----|
|Description|Relationship Id|
|DisplayName|Relationship Id|
|IsValidForForm|True|
|IsValidForRead|True|
|IsValidForUpdate|False|
|LogicalName|relationshipid|
|RequiredLevel|SystemRequired|
|Targets|relationship|
|Type|Lookup|

<a name="read-only-attributes"></a>

## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentIdUnique](#BKMK_ComponentIdUnique)
- [ComponentState](#BKMK_ComponentState)
- [IsManaged](#BKMK_IsManaged)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [ReferencedAttributeIdName](#BKMK_ReferencedAttributeIdName)
- [ReferencingAttributeIdName](#BKMK_ReferencingAttributeIdName)
- [RelationshipIdName](#BKMK_RelationshipIdName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)


### <a name="BKMK_ComponentIdUnique"></a> ComponentIdUnique

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Row id unique|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentidunique|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_ComponentState"></a> ComponentState

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Component State|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|componentstate|
|RequiredLevel|SystemRequired|
|Type|Picklist|

#### ComponentState Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|0|Published||
|1|Unpublished||
|2|Deleted||
|3|Deleted Unpublished||



### <a name="BKMK_IsManaged"></a> IsManaged

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Indicates whether the solution component is part of a managed solution.|
|DisplayName|Is Managed|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|ismanaged|
|RequiredLevel|SystemRequired|
|Type|Boolean|

#### IsManaged Choices/Options

|Value|Label|Description|
|-----|-----|--------|
|1|Managed|
|0|Unmanaged|

**DefaultValue**: False



### <a name="BKMK_OrganizationId"></a> OrganizationId

|Property|Value|
|--------|-----|
|Description|Unique identifier for the organization|
|DisplayName|Organization Id|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationid|
|RequiredLevel|None|
|Targets|organization|
|Type|Lookup|


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|organizationidname|
|MaxLength|160|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|DateTimeBehavior|UserLocal|
|Description|For internal use only.|
|DisplayName|Record Overwrite Time|
|Format|DateAndTime|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|overwritetime|
|RequiredLevel|SystemRequired|
|Type|DateTime|


### <a name="BKMK_ReferencedAttributeIdName"></a> ReferencedAttributeIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|referencedattributeidname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_ReferencingAttributeIdName"></a> ReferencingAttributeIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|referencingattributeidname|
|MaxLength|128|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_RelationshipIdName"></a> RelationshipIdName

|Property|Value|
|--------|-----|
|Description||
|DisplayName||
|FormatName|Text|
|IsLocalizable|False|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|relationshipidname|
|MaxLength|255|
|RequiredLevel|None|
|Type|String|


### <a name="BKMK_SolutionId"></a> SolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|Unique identifier of the associated solution.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|solutionid|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Added by**: Basic Solution Solution

|Property|Value|
|--------|-----|
|Description|For internal use only.|
|DisplayName|Solution|
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|supportingsolutionid|
|RequiredLevel|None|
|Type|Uniqueidentifier|

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [relationshipattribute_SyncErrors](#BKMK_relationshipattribute_SyncErrors)
- [relationshipattribute_AsyncOperations](#BKMK_relationshipattribute_AsyncOperations)
- [relationshipattribute_MailboxTrackingFolders](#BKMK_relationshipattribute_MailboxTrackingFolders)
- [relationshipattribute_BulkDeleteFailures](#BKMK_relationshipattribute_BulkDeleteFailures)
- [relationshipattribute_PrincipalObjectAttributeAccesses](#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses)


### <a name="BKMK_relationshipattribute_SyncErrors"></a> relationshipattribute_SyncErrors

**Added by**: System Solution Solution

Same as syncerror table [relationshipattribute_SyncErrors](syncerror.md#BKMK_relationshipattribute_SyncErrors) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|syncerror|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|relationshipattribute_SyncErrors|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_relationshipattribute_AsyncOperations"></a> relationshipattribute_AsyncOperations

**Added by**: System Solution Solution

Same as asyncoperation table [relationshipattribute_AsyncOperations](asyncoperation.md#BKMK_relationshipattribute_AsyncOperations) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|asyncoperation|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|relationshipattribute_AsyncOperations|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: NoCascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_relationshipattribute_MailboxTrackingFolders"></a> relationshipattribute_MailboxTrackingFolders

**Added by**: System Solution Solution

Same as mailboxtrackingfolder table [relationshipattribute_MailboxTrackingFolders](mailboxtrackingfolder.md#BKMK_relationshipattribute_MailboxTrackingFolders) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|mailboxtrackingfolder|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|relationshipattribute_MailboxTrackingFolders|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_relationshipattribute_BulkDeleteFailures"></a> relationshipattribute_BulkDeleteFailures

**Added by**: System Solution Solution

Same as bulkdeletefailure table [relationshipattribute_BulkDeleteFailures](bulkdeletefailure.md#BKMK_relationshipattribute_BulkDeleteFailures) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|bulkdeletefailure|
|ReferencingAttribute|regardingobjectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|relationshipattribute_BulkDeleteFailures|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|


### <a name="BKMK_relationshipattribute_PrincipalObjectAttributeAccesses"></a> relationshipattribute_PrincipalObjectAttributeAccesses

**Added by**: System Solution Solution

Same as principalobjectattributeaccess table [relationshipattribute_PrincipalObjectAttributeAccesses](principalobjectattributeaccess.md#BKMK_relationshipattribute_PrincipalObjectAttributeAccesses) Many-To-One relationship.

|Property|Value|
|--------|-----|
|ReferencingEntity|principalobjectattributeaccess|
|ReferencingAttribute|objectid|
|IsHierarchical|False|
|IsCustomizable|True|
|ReferencedEntityNavigationPropertyName|relationshipattribute_PrincipalObjectAttributeAccesses|
|AssociatedMenuConfiguration|Behavior: DoNotDisplay<br />Group: Details<br />Label: <br />Order: |
|CascadeConfiguration|Assign: NoCascade<br />Delete: Cascade<br />Merge: NoCascade<br />Reparent: NoCascade<br />Share: NoCascade<br />Unshare: NoCascade|

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related table. Listed by **SchemaName**.

- [referencingattribute_relationshipattribute](#BKMK_referencingattribute_relationshipattribute)
- [referencedattribute_relationshipattribute](#BKMK_referencedattribute_relationshipattribute)
- [relationship_relationshipattribute](#BKMK_relationship_relationshipattribute)
- [organization_relationshipattribute](#BKMK_organization_relationshipattribute)


### <a name="BKMK_referencingattribute_relationshipattribute"></a> referencingattribute_relationshipattribute

**Added by**: System Solution Solution

See attribute Table [referencingattribute_relationshipattribute](attribute.md#BKMK_referencingattribute_relationshipattribute) One-To-Many relationship.

### <a name="BKMK_referencedattribute_relationshipattribute"></a> referencedattribute_relationshipattribute

**Added by**: System Solution Solution

See attribute Table [referencedattribute_relationshipattribute](attribute.md#BKMK_referencedattribute_relationshipattribute) One-To-Many relationship.

### <a name="BKMK_relationship_relationshipattribute"></a> relationship_relationshipattribute

**Added by**: System Solution Solution

See relationship Table [relationship_relationshipattribute](relationship.md#BKMK_relationship_relationshipattribute) One-To-Many relationship.

### <a name="BKMK_organization_relationshipattribute"></a> organization_relationshipattribute

**Added by**: System Solution Solution

See organization Table [organization_relationshipattribute](organization.md#BKMK_organization_relationshipattribute) One-To-Many relationship.

### See also

[About the table reference](../about-entity-reference.md)<br />
[Web API Reference](/dynamics365/customer-engagement/web-api/about)<br />
<xref href="Microsoft.Dynamics.CRM.relationshipattribute?text=relationshipattribute EntityType" />