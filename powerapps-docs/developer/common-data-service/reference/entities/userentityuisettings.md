---
title: "UserEntityUISettings Entity Reference (Common Data Service for Apps)| MicrosoftDocs"
description: "Includes schema information and supported messages for the UserEntityUISettings entity."

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
# UserEntityUISettings Entity Reference

Stores user settings for entity views.

## Entity Properties

**DisplayName**: User Entity UI Settings<br />
**DisplayCollectionName**: User Entity UI Settings<br />
**SchemaName**: UserEntityUISettings<br />
**CollectionSchemaName**: UserEntityUISettingses<br />
**LogicalName**: userentityuisettings<br />
**LogicalCollectionName**: userentityuisettingses<br />
**EntitySetName**: userentityuisettingsset<br />
**PrimaryIdAttribute**: userentityuisettingsid<br />
**PrimaryNameAttribute**: <br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [InsertIntoEmailMRUXml](#BKMK_InsertIntoEmailMRUXml)
- [LastViewedFormXml](#BKMK_LastViewedFormXml)
- [LookupMRUXml](#BKMK_LookupMRUXml)
- [MRUXml](#BKMK_MRUXml)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [ReadingPaneXml](#BKMK_ReadingPaneXml)
- [RecentlyViewedXml](#BKMK_RecentlyViewedXml)
- [ShowInAddressBook](#BKMK_ShowInAddressBook)
- [TabOrderXml](#BKMK_TabOrderXml)
- [UserEntityUISettingsId](#BKMK_UserEntityUISettingsId)


### <a name="BKMK_InsertIntoEmailMRUXml"></a> InsertIntoEmailMRUXml

**Description**: Describes which entities are most recently inserted into email for this entity<br />
**DisplayName**: Most Recently Inserted Into Email Xml<br />
**LogicalName**: insertintoemailmruxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_LastViewedFormXml"></a> LastViewedFormXml

**Description**: Describes which forms are most recently viewed for this entity.<br />
**DisplayName**: Last Viewed Form Xml<br />
**LogicalName**: lastviewedformxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_LookupMRUXml"></a> LookupMRUXml

**Description**: List of most recently used lookup references for this entity<br />
**DisplayName**: Most Recently Used Xml<br />
**LogicalName**: lookupmruxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_MRUXml"></a> MRUXml

**Description**: Describes which tabs are most recently used for this entity<br />
**DisplayName**: Most Recently Used Xml<br />
**LogicalName**: mruxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Object Type Code<br />
**DisplayName**: <br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: 0


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Unique identifier of the user or team who owns the settings.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: Type of the owner of the saved view, such as user, team, or business unit.<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: EntityName<br />


### <a name="BKMK_ReadingPaneXml"></a> ReadingPaneXml

**Description**: Describes the reading pane formatting of this entity<br />
**DisplayName**: Conditional formatting<br />
**LogicalName**: readingpanexml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_RecentlyViewedXml"></a> RecentlyViewedXml

**Description**: Describes which objects are most recently viewed for this entity<br />
**DisplayName**: Most Recently Viewed Objects<br />
**LogicalName**: recentlyviewedxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_ShowInAddressBook"></a> ShowInAddressBook

**Description**: Determines whether a record type is exposed in the Outlook Address Book<br />
**DisplayName**: Show In Address Book<br />
**LogicalName**: showinaddressbook<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_TabOrderXml"></a> TabOrderXml

**Description**: Describes the tab ordering for this entity<br />
**DisplayName**: Tab Order Xml<br />
**LogicalName**: taborderxml<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_UserEntityUISettingsId"></a> UserEntityUISettingsId

**Description**: Unique identifier user entity<br />
**DisplayName**: <br />
**LogicalName**: userentityuisettingsid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner of the saved view.<br />
**DisplayName**: <br />
**LogicalName**: owneridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerIdYomiName"></a> OwnerIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier of the business unit that owns this.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns this saved view.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns this saved view.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: <br />
**DisplayName**: <br />
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


### <a name="BKMK_userentityinstancedata_userentityuisettings"></a> userentityinstancedata_userentityuisettings

Same as userentityinstancedata entity [userentityinstancedata_userentityuisettings](userentityinstancedata.md#BKMK_userentityinstancedata_userentityuisettings) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_userentityuisettings<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [team_userentityuisettings](#BKMK_team_userentityuisettings)
- [userentityuisettings_businessunit](#BKMK_userentityuisettings_businessunit)
- [userentityuisettings_owning_user](#BKMK_userentityuisettings_owning_user)


### <a name="BKMK_team_userentityuisettings"></a> team_userentityuisettings

See team Entity [team_userentityuisettings](team.md#BKMK_team_userentityuisettings) One-To-Many relationship.

### <a name="BKMK_userentityuisettings_businessunit"></a> userentityuisettings_businessunit

See businessunit Entity [userentityuisettings_businessunit](businessunit.md#BKMK_userentityuisettings_businessunit) One-To-Many relationship.

### <a name="BKMK_userentityuisettings_owning_user"></a> userentityuisettings_owning_user

See systemuser Entity [userentityuisettings_owning_user](systemuser.md#BKMK_userentityuisettings_owning_user) One-To-Many relationship.
userentityuisettings

