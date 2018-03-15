---
title: "MobileOfflineProfileItem Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the MobileOfflineProfileItem entity."

services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/07/2018
ms.author: jdaly
---
# MobileOfflineProfileItem Entity Reference

Information on entity availability to mobile devices in offline mode for a mobile offline profile item.

## Entity Properties

**DisplayName**: Mobile Offline Profile Item<br />
**DisplayCollectionName**: Mobile Offline Profile Item<br />
**SchemaName**: MobileOfflineProfileItem<br />
**CollectionSchemaName**: MobileOfflineProfileItems<br />
**LogicalName**: mobileofflineprofileitem<br />
**LogicalCollectionName**: mobileofflineprofileitems<br />
**EntitySetName**: mobileofflineprofileitems<br />
**PrimaryIdAttribute**: mobileofflineprofileitemid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: OrganizationOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [CanBeFollowed](#BKMK_CanBeFollowed)
- [GetRelatedEntityRecords](#BKMK_GetRelatedEntityRecords)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsVisibleInGrid](#BKMK_IsVisibleInGrid)
- [MobileOfflineProfileItemId](#BKMK_MobileOfflineProfileItemId)
- [Name](#BKMK_Name)
- [ProcessId](#BKMK_ProcessId)
- [ProfileItemEntityFilter](#BKMK_ProfileItemEntityFilter)
- [ProfileItemRule](#BKMK_ProfileItemRule)
- [ProfileItemRuleName](#BKMK_ProfileItemRuleName)
- [RecordDistributionCriteria](#BKMK_RecordDistributionCriteria)
- [RecordsOwnedByMe](#BKMK_RecordsOwnedByMe)
- [RecordsOwnedByMyBusinessUnit](#BKMK_RecordsOwnedByMyBusinessUnit)
- [RecordsOwnedByMyTeam](#BKMK_RecordsOwnedByMyTeam)
- [RegardingObjectId](#BKMK_RegardingObjectId)
- [RegardingObjectIdName](#BKMK_RegardingObjectIdName)
- [RelationshipData](#BKMK_RelationshipData)
- [SelectedEntityTypeCode](#BKMK_SelectedEntityTypeCode)
- [StageId](#BKMK_StageId)
- [TraversedPath](#BKMK_TraversedPath)
- [ViewQuery](#BKMK_ViewQuery)


### <a name="BKMK_CanBeFollowed"></a> CanBeFollowed

**Description**: Specifies whether records of this entity can be followed.<br />
**DisplayName**: Allow Entity to Follow Relationship<br />
**LogicalName**: canbefollowed<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_GetRelatedEntityRecords"></a> GetRelatedEntityRecords

**Description**: Specify whether records related to this entity will be made available for offline access.<br />
**DisplayName**: Get Related Entities<br />
**LogicalName**: getrelatedentityrecords<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the Mobile offline Profile Item is introduced.<br />
**DisplayName**: Introduced Version<br />
**LogicalName**: introducedversion<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: VersionNumber<br />
**IsLocalizable**: False<br />
**MaxLength**: 48


### <a name="BKMK_IsVisibleInGrid"></a> IsVisibleInGrid

**Description**: Information about whether the mobile offline profile item is visible in the Profile Item subgrid.<br />
**DisplayName**: Is Visible In Grid<br />
**LogicalName**: isvisibleingrid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: True


### <a name="BKMK_MobileOfflineProfileItemId"></a> MobileOfflineProfileItemId

**Description**: Unique identifier of the mobile offline profile item.<br />
**DisplayName**: Mobile Offline Profile Item<br />
**LogicalName**: mobileofflineprofileitemid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Name"></a> Name

**Description**: Enter the name of the mobile offline profile item.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 255


### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Shows the ID of the process.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ProfileItemEntityFilter"></a> ProfileItemEntityFilter

**Description**: Profile item entity filter criteria<br />
**DisplayName**: Profile item entity filter<br />
**LogicalName**: profileitementityfilter<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ProfileItemRule"></a> ProfileItemRule

**Description**: Saved Query associated with the Mobile offline profile item rule.<br />
**DisplayName**: View to sync data to device<br />
**LogicalName**: profileitemrule<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: savedquery


### <a name="BKMK_ProfileItemRuleName"></a> ProfileItemRuleName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: profileitemrulename<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RecordDistributionCriteria"></a> RecordDistributionCriteria

**Description**: Specify data download filter for selected entity<br />
**DisplayName**: Data Download Filter<br />
**LogicalName**: recorddistributioncriteria<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Download related data only
- **Value**: 1 **Label**: All records
- **Value**: 2 **Label**: Other data filter
- **Value**: 3 **Label**: Custom data filter



### <a name="BKMK_RecordsOwnedByMe"></a> RecordsOwnedByMe

**Description**: Download my records<br />
**DisplayName**: Download my records<br />
**LogicalName**: recordsownedbyme<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: False


### <a name="BKMK_RecordsOwnedByMyBusinessUnit"></a> RecordsOwnedByMyBusinessUnit

**Description**: Download my business unit's records<br />
**DisplayName**: Download my business unit's records<br />
**LogicalName**: recordsownedbymybusinessunit<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: False


### <a name="BKMK_RecordsOwnedByMyTeam"></a> RecordsOwnedByMyTeam

**Description**: Download my team's records<br />
**DisplayName**: Download my team's records<br />
**LogicalName**: recordsownedbymyteam<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: False


### <a name="BKMK_RegardingObjectId"></a> RegardingObjectId

**Description**: Items contained with a particular Profile.<br />
**DisplayName**: Regarding<br />
**LogicalName**: regardingobjectid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Lookup<br />
**Targets**: mobileofflineprofile


### <a name="BKMK_RegardingObjectIdName"></a> RegardingObjectIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: regardingobjectidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RelationshipData"></a> RelationshipData

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
**LogicalName**: relationshipdata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_SelectedEntityTypeCode"></a> SelectedEntityTypeCode

**Description**: Mobile offline enabled entity<br />
**DisplayName**: Entity<br />
**LogicalName**: selectedentitytypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_StageId"></a> StageId

**Description**: Shows the ID of the stage.<br />
**DisplayName**: Process Stage<br />
**LogicalName**: stageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TraversedPath"></a> TraversedPath

**Description**: For internal use only.<br />
**DisplayName**: Traversed Path<br />
**LogicalName**: traversedpath<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1250


### <a name="BKMK_ViewQuery"></a> ViewQuery

**Description**: Contains converted sql of the referenced view.<br />
**DisplayName**: View Query<br />
**LogicalName**: viewquery<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EntityObjectTypeCode](#BKMK_EntityObjectTypeCode)
- [IsManaged](#BKMK_IsManaged)
- [IsValidated](#BKMK_IsValidated)
- [MobileOfflineProfileItemIdUnique](#BKMK_MobileOfflineProfileItemIdUnique)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [PublishedOn](#BKMK_PublishedOn)
- [SelectedEntityMetadata](#BKMK_SelectedEntityMetadata)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_ComponentState"></a> ComponentState

**Description**: For internal use only.<br />
**DisplayName**: Component State<br />
**LogicalName**: componentstate<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Published
- **Value**: 1 **Label**: Unpublished
- **Value**: 2 **Label**: Deleted
- **Value**: 3 **Label**: Deleted Unpublished



### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Shows who created the record.<br />
**DisplayName**: Created By<br />
**LogicalName**: createdby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedByName"></a> CreatedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedByYomiName"></a> CreatedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOn"></a> CreatedOn

**Description**: Shows the date and time when the record was created. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_CreatedOnBehalfByName"></a> CreatedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedOnBehalfByYomiName"></a> CreatedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: createdonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EntityObjectTypeCode"></a> EntityObjectTypeCode

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
**LogicalName**: entityobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: For internal use only.<br />
**DisplayName**: Is Managed<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_IsValidated"></a> IsValidated

**Description**: Information about whether profile item is validated or not<br />
**DisplayName**: Is Valid For Mobile Offline<br />
**LogicalName**: isvalidated<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_MobileOfflineProfileItemIdUnique"></a> MobileOfflineProfileItemIdUnique

**Description**: For Internal Use Only<br />
**DisplayName**: Unique Id<br />
**LogicalName**: mobileofflineprofileitemidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedByName"></a> ModifiedByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedByYomiName"></a> ModifiedByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOn"></a> ModifiedOn

**Description**: Shows the date and time when the record was last updated. The date and time are displayed in the time zone selected in Microsoft Dynamics 365 options.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who updated the record on behalf of another user.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_ModifiedOnBehalfByName"></a> ModifiedOnBehalfByName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ModifiedOnBehalfByYomiName"></a> ModifiedOnBehalfByYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: modifiedonbehalfbyyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the Mobile Offline Profile Item.<br />
**DisplayName**: Organization<br />
**LogicalName**: organizationid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: organization


### <a name="BKMK_OrganizationIdName"></a> OrganizationIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: organizationidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OverwriteTime"></a> OverwriteTime

**Description**: For internal use only.<br />
**DisplayName**: Record Overwrite Time<br />
**LogicalName**: overwritetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_PublishedOn"></a> PublishedOn

**Description**: Displays the last published date time.<br />
**DisplayName**: Published On<br />
**LogicalName**: publishedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_SelectedEntityMetadata"></a> SelectedEntityMetadata

**Description**: Internal Use Only<br />
**DisplayName**: Internal Use Only<br />
**LogicalName**: selectedentitymetadata<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_SolutionId"></a> SolutionId

**Description**: Unique identifier of the associated solution.<br />
**DisplayName**: Solution<br />
**LogicalName**: solutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SupportingSolutionId"></a> SupportingSolutionId

**Description**: For internal use only.<br />
**DisplayName**: Solution<br />
**LogicalName**: supportingsolutionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the Mobile Offline Profile Item.<br />
**DisplayName**: Version Number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.


### <a name="BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation"></a> MobileOfflineProfileItem_MobileOfflineProfileItemAssociation

Same as mobileofflineprofileitemassociation entity [MobileOfflineProfileItem_MobileOfflineProfileItemAssociation](mobileofflineprofileitemassociation.md#BKMK_MobileOfflineProfileItem_MobileOfflineProfileItemAssociation) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitemassociation<br />
**ReferencingAttribute**: mobileofflineprofileitemid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: MobileOfflineProfileItem_MobileOfflineProfileItemAssociation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [lk_mobileofflineprofileitem_createdonbehalfby](#BKMK_lk_mobileofflineprofileitem_createdonbehalfby)
- [lk_mobileofflineprofileitem_savedquery](#BKMK_lk_mobileofflineprofileitem_savedquery)
- [lk_mobileofflineprofileitem_modifiedby](#BKMK_lk_mobileofflineprofileitem_modifiedby)
- [MobileOfflineProfile_MobileOfflineProfileItem](#BKMK_MobileOfflineProfile_MobileOfflineProfileItem)
- [lk_mobileofflineprofileitem_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby)
- [MobileOfflineProfileItem_organization](#BKMK_MobileOfflineProfileItem_organization)
- [lk_MobileOfflineProfileItem_createdby](#BKMK_lk_MobileOfflineProfileItem_createdby)


### <a name="BKMK_lk_mobileofflineprofileitem_createdonbehalfby"></a> lk_mobileofflineprofileitem_createdonbehalfby

See systemuser Entity [lk_mobileofflineprofileitem_createdonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitem_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_mobileofflineprofileitem_savedquery"></a> lk_mobileofflineprofileitem_savedquery

See savedquery Entity [lk_mobileofflineprofileitem_savedquery](savedquery.md#BKMK_lk_mobileofflineprofileitem_savedquery) One-To-Many relationship.

### <a name="BKMK_lk_mobileofflineprofileitem_modifiedby"></a> lk_mobileofflineprofileitem_modifiedby

See systemuser Entity [lk_mobileofflineprofileitem_modifiedby](systemuser.md#BKMK_lk_mobileofflineprofileitem_modifiedby) One-To-Many relationship.

### <a name="BKMK_MobileOfflineProfile_MobileOfflineProfileItem"></a> MobileOfflineProfile_MobileOfflineProfileItem

See mobileofflineprofile Entity [MobileOfflineProfile_MobileOfflineProfileItem](mobileofflineprofile.md#BKMK_MobileOfflineProfile_MobileOfflineProfileItem) One-To-Many relationship.

### <a name="BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby"></a> lk_mobileofflineprofileitem_modifiedonbehalfby

See systemuser Entity [lk_mobileofflineprofileitem_modifiedonbehalfby](systemuser.md#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_MobileOfflineProfileItem_organization"></a> MobileOfflineProfileItem_organization

See organization Entity [MobileOfflineProfileItem_organization](organization.md#BKMK_MobileOfflineProfileItem_organization) One-To-Many relationship.

### <a name="BKMK_lk_MobileOfflineProfileItem_createdby"></a> lk_MobileOfflineProfileItem_createdby

See systemuser Entity [lk_MobileOfflineProfileItem_createdby](systemuser.md#BKMK_lk_MobileOfflineProfileItem_createdby) One-To-Many relationship.
mobileofflineprofileitem

