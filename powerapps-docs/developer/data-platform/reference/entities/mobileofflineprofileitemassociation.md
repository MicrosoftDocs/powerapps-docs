---
title: "Mobile Offline Profile Item Association (MobileOfflineProfileItemAssociation) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Mobile Offline Profile Item Association (MobileOfflineProfileItemAssociation) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Mobile Offline Profile Item Association (MobileOfflineProfileItemAssociation) table/entity reference (Microsoft Dataverse)

Information on relationships to be used to follow related entity's records for mobile offline profile item.

## Messages

The following table lists the messages for the Mobile Offline Profile Item Association (MobileOfflineProfileItemAssociation) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /mobileofflineprofileitemassociations<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /mobileofflineprofileitemassociations<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveUnpublished`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublished?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedRequest>|
| `RetrieveUnpublishedMultiple`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveUnpublishedMultipleRequest>|
| `Update`<br />Event: False |`PATCH` /mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /mobileofflineprofileitemassociations(*mobileofflineprofileitemassociationid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Mobile Offline Profile Item Association (MobileOfflineProfileItemAssociation) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Mobile Offline Profile Item Association** |
| **DisplayCollectionName** | **Mobile Offline Profile Item Associations** |
| **SchemaName** | `MobileOfflineProfileItemAssociation` |
| **CollectionSchemaName** | `MobileOfflineProfileItemAssociations` |
| **EntitySetName** | `mobileofflineprofileitemassociations`|
| **LogicalName** | `mobileofflineprofileitemassociation` |
| **LogicalCollectionName** | `mobileofflineprofileitemassociations` |
| **PrimaryIdAttribute** | `mobileofflineprofileitemassociationid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [IntroducedVersion](#BKMK_IntroducedVersion)
- [MobileOfflineProfileItemAssociationId](#BKMK_MobileOfflineProfileItemAssociationId)
- [MobileOfflineProfileItemId](#BKMK_MobileOfflineProfileItemId)
- [Name](#BKMK_Name)
- [ProcessId](#BKMK_ProcessId)
- [ProfileItemAssociationEntityFilter](#BKMK_ProfileItemAssociationEntityFilter)
- [RelationshipData](#BKMK_RelationshipData)
- [RelationshipDisplayName](#BKMK_RelationshipDisplayName)
- [RelationshipId](#BKMK_RelationshipId)
- [SelectedRelationShipsSchema](#BKMK_SelectedRelationShipsSchema)
- [StageId](#BKMK_StageId)
- [TraversedPath](#BKMK_TraversedPath)

### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

|Property|Value|
|---|---|
|Description|**Version in which the Mobile offline Profile Item Association is introduced.**|
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

### <a name="BKMK_MobileOfflineProfileItemAssociationId"></a> MobileOfflineProfileItemAssociationId

|Property|Value|
|---|---|
|Description|**Unique identifier of the mobile offline profile item associaition.**|
|DisplayName|**Mobile Offline profileitemassociation**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemassociationid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_MobileOfflineProfileItemId"></a> MobileOfflineProfileItemId

|Property|Value|
|---|---|
|Description|**Id of the parent profile item.**|
|DisplayName|**Regarding**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|mobileofflineprofileitem|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Enter the name of the mobile offline profile item association.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ProcessId"></a> ProcessId

|Property|Value|
|---|---|
|Description|**Shows the ID of the process.**|
|DisplayName|**Process**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`processid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_ProfileItemAssociationEntityFilter"></a> ProfileItemAssociationEntityFilter

|Property|Value|
|---|---|
|Description|**Profile item association entity filter criteria.**|
|DisplayName|**Profile item association entity filter**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`profileitemassociationentityfilter`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_RelationshipData"></a> RelationshipData

|Property|Value|
|---|---|
|Description|**Internal Use Only**|
|DisplayName|**Internal Use Only**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`relationshipdata`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_RelationshipDisplayName"></a> RelationshipDisplayName

|Property|Value|
|---|---|
|Description|**Entity relationship schema name**|
|DisplayName|**Entity Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshipdisplayname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_RelationshipId"></a> RelationshipId

|Property|Value|
|---|---|
|Description|**Shows the relationship**|
|DisplayName|**Shows the relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshipid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SelectedRelationShipsSchema"></a> SelectedRelationShipsSchema

|Property|Value|
|---|---|
|Description|**List of relationships of entity selected in parent profile item**|
|DisplayName|**Entity Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`selectedrelationshipsschema`|
|RequiredLevel|SystemRequired|
|Type|Picklist|
|DefaultFormValue||
|GlobalChoiceName|`selectedmobileofflineenabledentityrelationships`|

#### SelectedRelationShipsSchema Choices/Options

|Value|Label|
|---|---|

### <a name="BKMK_StageId"></a> StageId

|Property|Value|
|---|---|
|Description|**Shows the ID of the stage.**|
|DisplayName|**(Deprecated) Process Stage**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`stageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_TraversedPath"></a> TraversedPath

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**(Deprecated) Traversed Path**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`traversedpath`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1250|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [IsManaged](#BKMK_IsManaged)
- [IsValidated](#BKMK_IsValidated)
- [MobileOfflineProfileItemAssociationIdUnique](#BKMK_MobileOfflineProfileItemAssociationIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [RelationshipName](#BKMK_RelationshipName)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)

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
|Description|**Shows who created the record.**|
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
|Description|**Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who created the record on behalf of another user.**|
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
|Description|**For internal use only.**|
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

### <a name="BKMK_IsValidated"></a> IsValidated

|Property|Value|
|---|---|
|Description|**Information about whether profile item association is validated or not**|
|DisplayName|**Is Valid For Mobile Offline**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isvalidated`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`mobileofflineprofile_isvalidated`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_MobileOfflineProfileItemAssociationIdUnique"></a> MobileOfflineProfileItemAssociationIdUnique

|Property|Value|
|---|---|
|Description|**For Internal Use Only**|
|DisplayName|**Unique Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`mobileofflineprofileitemassociationidunique`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Shows who last updated the record.**|
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
|Description|**Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.**|
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
|Description|**Shows who updated the record on behalf of another user.**|
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
|Description|**Unique identifier of the organization associated with the Mobile Offline Profile Item Association.**|
|DisplayName|**Organization**|
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

### <a name="BKMK_PublishedOn"></a> PublishedOn

|Property|Value|
|---|---|
|Description|**Displays the last published date time.**|
|DisplayName|**Published On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publishedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateAndTime|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_RelationshipName"></a> RelationshipName

|Property|Value|
|---|---|
|Description|**Display name of entity relationship**|
|DisplayName|**Entity Relationship**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`relationshipname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

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
|Description|**Version number of the Mobile Offline profileitemassociation.**|
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

- [lk_MobileOfflineProfileItemAssociation_createdby](#BKMK_lk_MobileOfflineProfileItemAssociation_createdby)
- [lk_mobileofflineprofileitemassociation_createdonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby)
- [lk_mobileofflineprofileitemassociation_modifiedby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedby)
- [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby)
- [MobileOfflineProfileItem_MobileOfflineProfileItemAssociation](#BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation)
- [MobileOfflineProfileItemAssociation_organization](#BKMK_MobileOfflineProfileItemAssociation_organization)

### <a name="BKMK_lk_MobileOfflineProfileItemAssociation_createdby"></a> lk_MobileOfflineProfileItemAssociation_createdby

One-To-Many Relationship: [systemuser lk_MobileOfflineProfileItemAssociation_createdby](systemuser.md#BKMK_lk_MobileOfflineProfileItemAssociation_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby"></a> lk_mobileofflineprofileitemassociation_createdonbehalfby

One-To-Many Relationship: [systemuser lk_mobileofflineprofileitemassociation_createdonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedby"></a> lk_mobileofflineprofileitemassociation_modifiedby

One-To-Many Relationship: [systemuser lk_mobileofflineprofileitemassociation_modifiedby](systemuser.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby"></a> lk_mobileofflineprofileitemassociation_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_mobileofflineprofileitemassociation_modifiedonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation"></a> MobileOfflineProfileItem_MobileOfflineProfileItemAssociation

One-To-Many Relationship: [mobileofflineprofileitem MobileOfflineProfileItem_MobileOfflineProfileItemAssociation](mobileofflineprofileitem.md#BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation)

|Property|Value|
|---|---|
|ReferencedEntity|`mobileofflineprofileitem`|
|ReferencedAttribute|`mobileofflineprofileitemid`|
|ReferencingAttribute|`mobileofflineprofileitemid`|
|ReferencingEntityNavigationPropertyName|`regardingobjectid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `Cascade`<br />Delete: `Cascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_MobileOfflineProfileItemAssociation_organization"></a> MobileOfflineProfileItemAssociation_organization

One-To-Many Relationship: [organization MobileOfflineProfileItemAssociation_organization](organization.md#BKMK_MobileOfflineProfileItemAssociation_organization)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.mobileofflineprofileitemassociation?displayProperty=fullName>
