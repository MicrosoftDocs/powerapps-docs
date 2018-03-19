---
title: "ImportMap Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the ImportMap entity."

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
# ImportMap Entity Reference

Data map used in import.

## Entity Properties

**DisplayName**: Data Map<br />
**DisplayCollectionName**: Data Maps<br />
**SchemaName**: ImportMap<br />
**CollectionSchemaName**: ImportMaps<br />
**LogicalName**: importmap<br />
**LogicalCollectionName**: importmaps<br />
**EntitySetName**: importmaps<br />
**PrimaryIdAttribute**: importmapid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [Description](#BKMK_Description)
- [EntitiesPerFile](#BKMK_EntitiesPerFile)
- [ImportMapId](#BKMK_ImportMapId)
- [ImportMapType](#BKMK_ImportMapType)
- [IntroducedVersion](#BKMK_IntroducedVersion)
- [IsWizardCreated](#BKMK_IsWizardCreated)
- [MapCustomizations](#BKMK_MapCustomizations)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Source](#BKMK_Source)
- [SourceType](#BKMK_SourceType)
- [SourceUserIdentifierForSourceCRMUserLink](#BKMK_SourceUserIdentifierForSourceCRMUserLink)
- [SourceUserIdentifierForSourceDataSourceUserLink](#BKMK_SourceUserIdentifierForSourceDataSourceUserLink)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TargetUserIdentifierForSourceCRMUserLink](#BKMK_TargetUserIdentifierForSourceCRMUserLink)


### <a name="BKMK_Description"></a> Description

**Description**: Type additional information to describe the data map, such as the intended use or data source.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_EntitiesPerFile"></a> EntitiesPerFile

**Description**: Choose whether a data file can contain data for one or more record types.<br />
**DisplayName**: Entities Per File<br />
**LogicalName**: entitiesperfile<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Single Entity Per File
- **Value**: 2 **Label**: Multiple Entities Per File



### <a name="BKMK_ImportMapId"></a> ImportMapId

**Description**: Unique identifier of the data map.<br />
**DisplayName**: Data Map<br />
**LogicalName**: importmapid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ImportMapType"></a> ImportMapType

**Description**: Select the type of data map to distinguish out-of-the-box data maps from custom maps.<br />
**DisplayName**: Map Type<br />
**LogicalName**: importmaptype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Standard
- **Value**: 2 **Label**: Out of Box
- **Value**: 3 **Label**: In Process



### <a name="BKMK_IntroducedVersion"></a> IntroducedVersion

**Description**: Version in which the component is introduced.<br />
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


### <a name="BKMK_IsWizardCreated"></a> IsWizardCreated

**Description**: Information about whether this data map was created by the Data Migration Manager.<br />
**DisplayName**: Is Wizard-Created<br />
**LogicalName**: iswizardcreated<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: True
- **FalseOption Value**: 0 **Label**: False

**DefaultValue**: False


### <a name="BKMK_MapCustomizations"></a> MapCustomizations

**Description**: Customizations XML<br />
**DisplayName**: Map Customizations<br />
**LogicalName**: mapcustomizations<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_Name"></a> Name

**Description**: Type a descriptive name for the data map.<br />
**DisplayName**: Map Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 320


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser,team


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_Source"></a> Source

**Description**: Type the name of the migration source that this data map is used for.<br />
**DisplayName**: Source<br />
**LogicalName**: source<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_SourceType"></a> SourceType

**Description**: Select the migration source type that this data map is used for.<br />
**DisplayName**: Source System Type<br />
**LogicalName**: sourcetype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Map For SalesForce.com Full Data Export
- **Value**: 2 **Label**: Map For SalesForce.com Report Export
- **Value**: 3 **Label**: Map For SalesForce.com Contact and Account Report Export
- **Value**: 4 **Label**: Microsoft Office Outlook 2010 with Business Contact Manager
- **Value**: 5 **Label**: Generic Map for Contact and Account



### <a name="BKMK_SourceUserIdentifierForSourceCRMUserLink"></a> SourceUserIdentifierForSourceCRMUserLink

**Description**: Source user value for source Microsoft Dynamics 365 user link.<br />
**DisplayName**: Source User Value<br />
**LogicalName**: sourceuseridentifierforsourcecrmuserlink<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_SourceUserIdentifierForSourceDataSourceUserLink"></a> SourceUserIdentifierForSourceDataSourceUserLink

**Description**: Column in the source file that uniquely identifies a user.<br />
**DisplayName**: Source User Identifier<br />
**LogicalName**: sourceuseridentifierforsourcedatasourceuserlink<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the data map is active or inactive. Inactive data maps are read-only and can't be edited.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Active **DefaultStatus**: 1 **InvariantName**: Active
- **Value**: 1 **Label**: Inactive **DefaultStatus**: 2 **InvariantName**: Inactive



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the data map's status.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



### <a name="BKMK_TargetUserIdentifierForSourceCRMUserLink"></a> TargetUserIdentifierForSourceCRMUserLink

**Description**: Microsoft Dynamics 365 user.<br />
**DisplayName**: Target User Value<br />
**LogicalName**: targetuseridentifierforsourcecrmuserlink<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160

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
- [ImportMapIdUnique](#BKMK_ImportMapIdUnique)
- [IsManaged](#BKMK_IsManaged)
- [IsValidForImport](#BKMK_IsValidForImport)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TargetEntity](#BKMK_TargetEntity)


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
**IsValidForForm**: False<br />
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
**RequiredLevel**: None<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
**DisplayName**: Created By (Delegate)<br />
**LogicalName**: createdonbehalfby<br />
**IsValidForForm**: False<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ImportMapIdUnique"></a> ImportMapIdUnique

**Description**: Unique identifier of the ImortMap.<br />
**DisplayName**: <br />
**LogicalName**: importmapidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_IsManaged"></a> IsManaged

**Description**: Information that specifies whether this component is managed.<br />
**DisplayName**: State<br />
**LogicalName**: ismanaged<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Managed
- **FalseOption Value**: 0 **Label**: Unmanaged

**DefaultValue**: False


### <a name="BKMK_IsValidForImport"></a> IsValidForImport

**Description**: Information about whether the data map is valid for use with data import.<br />
**DisplayName**: Is Valid For Import<br />
**LogicalName**: isvalidforimport<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Shows who last updated the record.<br />
**DisplayName**: Modified By<br />
**LogicalName**: modifiedby<br />
**IsValidForForm**: False<br />
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
**RequiredLevel**: None<br />
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
**RequiredLevel**: SystemRequired<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who last updated the record on behalf of another user.<br />
**DisplayName**: Modified By (Delegate)<br />
**LogicalName**: modifiedonbehalfby<br />
**IsValidForForm**: False<br />
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
**RequiredLevel**: None<br />
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


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: <br />
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

**Description**: Business unit that owns the data map.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the data map.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the data map.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


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


### <a name="BKMK_TargetEntity"></a> TargetEntity

**Description**: Select the name of the Microsoft Dynamics 365 record type that this data map is defined for.<br />
**DisplayName**: Record Type<br />
**LogicalName**: targetentity<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Account
- **Value**: 2 **Label**: Contact
- **Value**: 5 **Label**: Note
- **Value**: 6 **Label**: Business Unit Map
- **Value**: 7 **Label**: Owner
- **Value**: 8 **Label**: User
- **Value**: 9 **Label**: Team
- **Value**: 10 **Label**: Business Unit
- **Value**: 14 **Label**: System User Principal
- **Value**: 29 **Label**: Subscription
- **Value**: 30 **Label**: Filter Template
- **Value**: 31 **Label**: Privilege Object Type Code
- **Value**: 33 **Label**: Subscription Synchronization Information
- **Value**: 35 **Label**: Tracking information for deleted entities
- **Value**: 36 **Label**: Client update
- **Value**: 37 **Label**: Subscription Manually Tracked Object
- **Value**: 42 **Label**: SystemUser BusinessUnit Entity Map
- **Value**: 44 **Label**: Field Sharing
- **Value**: 45 **Label**: Subscription Statistic Offline
- **Value**: 46 **Label**: Subscription Statistic Outlook
- **Value**: 47 **Label**: Subscription Sync Entry Offline
- **Value**: 48 **Label**: Subscription Sync Entry Outlook
- **Value**: 50 **Label**: Position
- **Value**: 51 **Label**: System User Manager Map
- **Value**: 52 **Label**: User Search Facet
- **Value**: 54 **Label**: Global Search Configuration
- **Value**: 78 **Label**: Virtual Entity Data Provider
- **Value**: 85 **Label**: Virtual Entity Data Source
- **Value**: 92 **Label**: Team template
- **Value**: 99 **Label**: Social Profile
- **Value**: 126 **Label**: Indexed Article
- **Value**: 127 **Label**: Article
- **Value**: 129 **Label**: Subject
- **Value**: 132 **Label**: Announcement
- **Value**: 135 **Label**: Activity Party
- **Value**: 150 **Label**: User Settings
- **Value**: 950 **Label**: New Process
- **Value**: 951 **Label**: Translation Process
- **Value**: 955 **Label**: Expired Process
- **Value**: 1001 **Label**: Attachment
- **Value**: 1002 **Label**: Attachment
- **Value**: 1003 **Label**: Internal Address
- **Value**: 1007 **Label**: Image Descriptor
- **Value**: 1016 **Label**: Article Template
- **Value**: 1019 **Label**: Organization
- **Value**: 1021 **Label**: Organization UI
- **Value**: 1023 **Label**: Privilege
- **Value**: 1030 **Label**: System Form
- **Value**: 1031 **Label**: User Dashboard
- **Value**: 1036 **Label**: Security Role
- **Value**: 1037 **Label**: Role Template
- **Value**: 1039 **Label**: View
- **Value**: 1043 **Label**: String Map
- **Value**: 1071 **Label**: Address
- **Value**: 1072 **Label**: Subscription Clients
- **Value**: 1075 **Label**: Status Map
- **Value**: 1082 **Label**: Article Comment
- **Value**: 1086 **Label**: User Fiscal Calendar
- **Value**: 1094 **Label**: Authorization Server
- **Value**: 1095 **Label**: Partner Application
- **Value**: 1111 **Label**: System Chart
- **Value**: 1112 **Label**: User Chart
- **Value**: 1113 **Label**: Ribbon Tab To Command Mapping
- **Value**: 1115 **Label**: Ribbon Context Group
- **Value**: 1116 **Label**: Ribbon Command
- **Value**: 1117 **Label**: Ribbon Rule
- **Value**: 1120 **Label**: Application Ribbons
- **Value**: 1130 **Label**: Ribbon Difference
- **Value**: 1140 **Label**: Replication Backlog
- **Value**: 1189 **Label**: Document Suggestions
- **Value**: 1190 **Label**: SuggestionCardTemplate
- **Value**: 1200 **Label**: Field Security Profile
- **Value**: 1201 **Label**: Field Permission
- **Value**: 1203 **Label**: Team Profiles
- **Value**: 1234 **Label**: Channel Property Group
- **Value**: 1236 **Label**: Channel Property
- **Value**: 1300 **Label**: SocialInsightsConfiguration
- **Value**: 1309 **Label**: Saved Organization Insights Configuration
- **Value**: 1400 **Label**: Sync Attribute Mapping Profile
- **Value**: 1401 **Label**: Sync Attribute Mapping
- **Value**: 1403 **Label**: Team Sync-Attribute Mapping Profiles
- **Value**: 1404 **Label**: Principal Sync Attribute Map
- **Value**: 2000 **Label**: Annual Fiscal Calendar
- **Value**: 2001 **Label**: Semiannual Fiscal Calendar
- **Value**: 2002 **Label**: Quarterly Fiscal Calendar
- **Value**: 2003 **Label**: Monthly Fiscal Calendar
- **Value**: 2004 **Label**: Fixed Monthly Fiscal Calendar
- **Value**: 2010 **Label**: Email Template
- **Value**: 2012 **Label**: Unresolved Address
- **Value**: 2013 **Label**: Territory
- **Value**: 2015 **Label**: Theme
- **Value**: 2016 **Label**: User Mapping
- **Value**: 2020 **Label**: Queue
- **Value**: 2023 **Label**: QueueItemCount
- **Value**: 2024 **Label**: QueueMemberCount
- **Value**: 2027 **Label**: License
- **Value**: 2029 **Label**: Queue Item
- **Value**: 2500 **Label**: User Entity UI Settings
- **Value**: 2501 **Label**: User Entity Instance Data
- **Value**: 3000 **Label**: Integration Status
- **Value**: 3005 **Label**: Channel Access Profile
- **Value**: 3008 **Label**: External Party
- **Value**: 3231 **Label**: Connection Role
- **Value**: 3233 **Label**: Connection Role Object Type Code
- **Value**: 3234 **Label**: Connection
- **Value**: 4003 **Label**: Calendar
- **Value**: 4004 **Label**: Calendar Rule
- **Value**: 4011 **Label**: Inter Process Lock
- **Value**: 4023 **Label**: Email Hash
- **Value**: 4101 **Label**: Display String Map
- **Value**: 4102 **Label**: Display String
- **Value**: 4110 **Label**: Notification
- **Value**: 4120 **Label**: Exchange Sync Id Mapping
- **Value**: 4200 **Label**: Activity
- **Value**: 4201 **Label**: Appointment
- **Value**: 4202 **Label**: Email
- **Value**: 4204 **Label**: Fax
- **Value**: 4207 **Label**: Letter
- **Value**: 4210 **Label**: Phone Call
- **Value**: 4212 **Label**: Task
- **Value**: 4216 **Label**: Social Activity
- **Value**: 4220 **Label**: UntrackedEmail
- **Value**: 4230 **Label**: Saved View
- **Value**: 4231 **Label**: Metadata Difference
- **Value**: 4232 **Label**: Business Data Localized Label
- **Value**: 4250 **Label**: Recurrence Rule
- **Value**: 4251 **Label**: Recurring Appointment
- **Value**: 4299 **Label**: Email Search
- **Value**: 4410 **Label**: Data Import
- **Value**: 4411 **Label**: Data Map
- **Value**: 4412 **Label**: Import Source File
- **Value**: 4413 **Label**: Import Data
- **Value**: 4414 **Label**: Duplicate Detection Rule
- **Value**: 4415 **Label**: Duplicate Record
- **Value**: 4416 **Label**: Duplicate Rule Condition
- **Value**: 4417 **Label**: Column Mapping
- **Value**: 4418 **Label**: List Value Mapping
- **Value**: 4419 **Label**: Lookup Mapping
- **Value**: 4420 **Label**: Owner Mapping
- **Value**: 4423 **Label**: Import Log
- **Value**: 4424 **Label**: Bulk Delete Operation
- **Value**: 4425 **Label**: Bulk Delete Failure
- **Value**: 4426 **Label**: Transformation Mapping
- **Value**: 4427 **Label**: Transformation Parameter Mapping
- **Value**: 4428 **Label**: Import Entity Mapping
- **Value**: 4450 **Label**: Data Performance Dashboard
- **Value**: 4490 **Label**: Office Document
- **Value**: 4500 **Label**: Relationship Role
- **Value**: 4501 **Label**: Relationship Role Map
- **Value**: 4502 **Label**: Customer Relationship
- **Value**: 4567 **Label**: Auditing
- **Value**: 4579 **Label**: Ribbon Client Metadata.
- **Value**: 4600 **Label**: Entity Map
- **Value**: 4601 **Label**: Attribute Map
- **Value**: 4602 **Label**: Plug-in Type
- **Value**: 4603 **Label**: Plug-in Type Statistic
- **Value**: 4605 **Label**: Plug-in Assembly
- **Value**: 4606 **Label**: Sdk Message
- **Value**: 4607 **Label**: Sdk Message Filter
- **Value**: 4608 **Label**: Sdk Message Processing Step
- **Value**: 4609 **Label**: Sdk Message Request
- **Value**: 4610 **Label**: Sdk Message Response
- **Value**: 4611 **Label**: Sdk Message Response Field
- **Value**: 4613 **Label**: Sdk Message Pair
- **Value**: 4614 **Label**: Sdk Message Request Field
- **Value**: 4615 **Label**: Sdk Message Processing Step Image
- **Value**: 4616 **Label**: Sdk Message Processing Step Secure Configuration
- **Value**: 4618 **Label**: Service Endpoint
- **Value**: 4619 **Label**: Plug-in Trace Log
- **Value**: 4700 **Label**: System Job
- **Value**: 4702 **Label**: Workflow Wait Subscription
- **Value**: 4703 **Label**: Process
- **Value**: 4704 **Label**: Process Dependency
- **Value**: 4705 **Label**: ISV Config
- **Value**: 4706 **Label**: Process Log
- **Value**: 4707 **Label**: Application File
- **Value**: 4708 **Label**: Organization Statistic
- **Value**: 4709 **Label**: Site Map
- **Value**: 4710 **Label**: Process Session
- **Value**: 4711 **Label**: Expander Event
- **Value**: 4712 **Label**: Process Trigger
- **Value**: 4724 **Label**: Process Stage
- **Value**: 4725 **Label**: Business Process Flow Instance
- **Value**: 4800 **Label**: Web Wizard
- **Value**: 4802 **Label**: Wizard Page
- **Value**: 4803 **Label**: Web Wizard Access Privilege
- **Value**: 4810 **Label**: Time Zone Definition
- **Value**: 4811 **Label**: Time Zone Rule
- **Value**: 4812 **Label**: Time Zone Localized Name
- **Value**: 7000 **Label**: System Application Metadata
- **Value**: 7001 **Label**: User Application Metadata
- **Value**: 7100 **Label**: Solution
- **Value**: 7101 **Label**: Publisher
- **Value**: 7102 **Label**: Publisher Address
- **Value**: 7103 **Label**: Solution Component
- **Value**: 7105 **Label**: Dependency
- **Value**: 7106 **Label**: Dependency Node
- **Value**: 7107 **Label**: Invalid Dependency
- **Value**: 7108 **Label**: Dependency Feature
- **Value**: 7200 **Label**: RuntimeDependency
- **Value**: 8000 **Label**: Post
- **Value**: 8001 **Label**: Post Role
- **Value**: 8002 **Label**: Post Regarding
- **Value**: 8003 **Label**: Follow
- **Value**: 8005 **Label**: Comment
- **Value**: 8006 **Label**: Like
- **Value**: 8040 **Label**: ACIViewMapper
- **Value**: 8050 **Label**: Trace
- **Value**: 8051 **Label**: Trace Association
- **Value**: 8052 **Label**: Trace Regarding
- **Value**: 8181 **Label**: Routing Rule Set
- **Value**: 8199 **Label**: Rule Item
- **Value**: 8700 **Label**: AppModule Metadata
- **Value**: 8701 **Label**: AppModule Metadata Dependency
- **Value**: 8702 **Label**: AppModule Metadata Async Operation
- **Value**: 8840 **Label**: Hierarchy Rule
- **Value**: 9006 **Label**: App
- **Value**: 9007 **Label**: App Module Component
- **Value**: 9009 **Label**: App Module Roles
- **Value**: 9011 **Label**: App Config Master
- **Value**: 9012 **Label**: App Configuration
- **Value**: 9013 **Label**: App Configuration Instance
- **Value**: 9100 **Label**: Report
- **Value**: 9101 **Label**: Report Related Entity
- **Value**: 9102 **Label**: Report Related Category
- **Value**: 9103 **Label**: Report Visibility
- **Value**: 9104 **Label**: Report Link
- **Value**: 9105 **Label**: Currency
- **Value**: 9106 **Label**: Mail Merge Template
- **Value**: 9107 **Label**: Import Job
- **Value**: 9201 **Label**: LocalConfigStore
- **Value**: 9300 **Label**: Record Creation and Update Rule
- **Value**: 9301 **Label**: Record Creation and Update Rule Item
- **Value**: 9333 **Label**: Web Resource
- **Value**: 9400 **Label**: Channel Access Profile Rule
- **Value**: 9401 **Label**: Channel Access Profile Rule Item
- **Value**: 9502 **Label**: SharePoint Site
- **Value**: 9507 **Label**: Sharepoint Document
- **Value**: 9508 **Label**: Document Location
- **Value**: 9509 **Label**: SharePoint Data
- **Value**: 9510 **Label**: Rollup Properties
- **Value**: 9511 **Label**: Rollup Job
- **Value**: 9600 **Label**: Goal
- **Value**: 9602 **Label**: Rollup Query
- **Value**: 9603 **Label**: Goal Metric
- **Value**: 9604 **Label**: Rollup Field
- **Value**: 9605 **Label**: Email Server Profile
- **Value**: 9606 **Label**: Mailbox
- **Value**: 9607 **Label**: Mailbox Statistics
- **Value**: 9608 **Label**: Mailbox Auto Tracking Folder
- **Value**: 9650 **Label**: Process Configuration
- **Value**: 9690 **Label**: Organization Insights Notification
- **Value**: 9699 **Label**: Organization Insights Metric
- **Value**: 9750 **Label**: SLA
- **Value**: 9751 **Label**: SLA Item
- **Value**: 9752 **Label**: SLA KPI Instance
- **Value**: 9753 **Label**: Custom Control
- **Value**: 9754 **Label**: Custom Control Resource
- **Value**: 9755 **Label**: Custom Control Default Config
- **Value**: 9866 **Label**: Mobile Offline Profile
- **Value**: 9867 **Label**: Mobile Offline Profile Item
- **Value**: 9868 **Label**: Mobile Offline Profile Item Association
- **Value**: 9869 **Label**: Sync Error
- **Value**: 9870 **Label**: Offline Command Definition
- **Value**: 9900 **Label**: Navigation Setting
- **Value**: 9910 **Label**: MultiEntitySearch
- **Value**: 9912 **Label**: Multi Select Option Value
- **Value**: 9919 **Label**: Hierarchy Security Configuration
- **Value**: 9930 **Label**: Knowledge Base Record
- **Value**: 9932 **Label**: Time Stamp Date Mapping
- **Value**: 9936 **Label**: Azure Service Connection
- **Value**: 9940 **Label**: Document Template
- **Value**: 9941 **Label**: Personal Document Template
- **Value**: 9945 **Label**: Text Analytics Entity Mapping
- **Value**: 9947 **Label**: Knowledge Search Model
- **Value**: 9949 **Label**: Advanced Similarity Rule
- **Value**: 9950 **Label**: Office Graph Document
- **Value**: 9951 **Label**: Similarity Rule
- **Value**: 9953 **Label**: Knowledge Article
- **Value**: 9955 **Label**: Knowledge Article Views
- **Value**: 9957 **Label**: Language
- **Value**: 9958 **Label**: Feedback
- **Value**: 9959 **Label**: Category
- **Value**: 9960 **Label**: Knowledge Article Category
- **Value**: 9961 **Label**: DelveActionHub
- **Value**: 9962 **Label**: Action Card
- **Value**: 9968 **Label**: ActionCardUserState
- **Value**: 9973 **Label**: Action Card User Settings
- **Value**: 9983 **Label**: Action Card Type
- **Value**: 9986 **Label**: Interaction for Email
- **Value**: 9987 **Label**: External Party Item
- **Value**: 9997 **Label**: Email Signature
- **Value**: 10000 **Label**: OData v4 Data Source


<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [userentityinstancedata_importmap](#BKMK_userentityinstancedata_importmap)
- [TransformationMapping_ImportMap](#BKMK_TransformationMapping_ImportMap)
- [OwnerMapping_ImportMap](#BKMK_OwnerMapping_ImportMap)
- [ImportMap_AsyncOperations](#BKMK_ImportMap_AsyncOperations)
- [ImportMap_ImportFile](#BKMK_ImportMap_ImportFile)
- [ImportMap_BulkDeleteFailures](#BKMK_ImportMap_BulkDeleteFailures)
- [ImportEntityMapping_ImportMap](#BKMK_ImportEntityMapping_ImportMap)
- [ImportMap_SyncErrors](#BKMK_ImportMap_SyncErrors)
- [ColumnMapping_ImportMap](#BKMK_ColumnMapping_ImportMap)


### <a name="BKMK_userentityinstancedata_importmap"></a> userentityinstancedata_importmap

Same as userentityinstancedata entity [userentityinstancedata_importmap](userentityinstancedata.md#BKMK_userentityinstancedata_importmap) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_importmap<br />
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


### <a name="BKMK_TransformationMapping_ImportMap"></a> TransformationMapping_ImportMap

Same as transformationmapping entity [TransformationMapping_ImportMap](transformationmapping.md#BKMK_TransformationMapping_ImportMap) Many-To-One relationship.

**ReferencingEntity**: transformationmapping<br />
**ReferencingAttribute**: importmapid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: TransformationMapping_ImportMap<br />
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


### <a name="BKMK_OwnerMapping_ImportMap"></a> OwnerMapping_ImportMap

Same as ownermapping entity [OwnerMapping_ImportMap](ownermapping.md#BKMK_OwnerMapping_ImportMap) Many-To-One relationship.

**ReferencingEntity**: ownermapping<br />
**ReferencingAttribute**: importmapid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: OwnerMapping_ImportMap<br />
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


### <a name="BKMK_ImportMap_AsyncOperations"></a> ImportMap_AsyncOperations

Same as asyncoperation entity [ImportMap_AsyncOperations](asyncoperation.md#BKMK_ImportMap_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportMap_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportMap_ImportFile"></a> ImportMap_ImportFile

Same as importfile entity [ImportMap_ImportFile](importfile.md#BKMK_ImportMap_ImportFile) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: importmapid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportMap_ImportFile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_ImportMap_BulkDeleteFailures"></a> ImportMap_BulkDeleteFailures

Same as bulkdeletefailure entity [ImportMap_BulkDeleteFailures](bulkdeletefailure.md#BKMK_ImportMap_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportMap_BulkDeleteFailures<br />
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


### <a name="BKMK_ImportEntityMapping_ImportMap"></a> ImportEntityMapping_ImportMap

Same as importentitymapping entity [ImportEntityMapping_ImportMap](importentitymapping.md#BKMK_ImportEntityMapping_ImportMap) Many-To-One relationship.

**ReferencingEntity**: importentitymapping<br />
**ReferencingAttribute**: importmapid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportEntityMapping_ImportMap<br />
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


### <a name="BKMK_ImportMap_SyncErrors"></a> ImportMap_SyncErrors

Same as syncerror entity [ImportMap_SyncErrors](syncerror.md#BKMK_ImportMap_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: ImportMap_SyncErrors<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: Cascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_ColumnMapping_ImportMap"></a> ColumnMapping_ImportMap

Same as columnmapping entity [ColumnMapping_ImportMap](columnmapping.md#BKMK_ColumnMapping_ImportMap) Many-To-One relationship.

**ReferencingEntity**: columnmapping<br />
**ReferencingAttribute**: importmapid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ColumnMapping_ImportMap<br />
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

- [lk_importmapbase_createdby](#BKMK_lk_importmapbase_createdby)
- [lk_importmap_createdonbehalfby](#BKMK_lk_importmap_createdonbehalfby)
- [BusinessUnit_ImportMaps](#BKMK_BusinessUnit_ImportMaps)
- [team_ImportMaps](#BKMK_team_ImportMaps)
- [lk_importmap_modifiedonbehalfby](#BKMK_lk_importmap_modifiedonbehalfby)
- [SystemUser_ImportMaps](#BKMK_SystemUser_ImportMaps)
- [lk_importmapbase_modifiedby](#BKMK_lk_importmapbase_modifiedby)


### <a name="BKMK_lk_importmapbase_createdby"></a> lk_importmapbase_createdby

See systemuser Entity [lk_importmapbase_createdby](systemuser.md#BKMK_lk_importmapbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_importmap_createdonbehalfby"></a> lk_importmap_createdonbehalfby

See systemuser Entity [lk_importmap_createdonbehalfby](systemuser.md#BKMK_lk_importmap_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_ImportMaps"></a> BusinessUnit_ImportMaps

See businessunit Entity [BusinessUnit_ImportMaps](businessunit.md#BKMK_BusinessUnit_ImportMaps) One-To-Many relationship.

### <a name="BKMK_team_ImportMaps"></a> team_ImportMaps

See team Entity [team_ImportMaps](team.md#BKMK_team_ImportMaps) One-To-Many relationship.

### <a name="BKMK_lk_importmap_modifiedonbehalfby"></a> lk_importmap_modifiedonbehalfby

See systemuser Entity [lk_importmap_modifiedonbehalfby](systemuser.md#BKMK_lk_importmap_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_SystemUser_ImportMaps"></a> SystemUser_ImportMaps

See systemuser Entity [SystemUser_ImportMaps](systemuser.md#BKMK_SystemUser_ImportMaps) One-To-Many relationship.

### <a name="BKMK_lk_importmapbase_modifiedby"></a> lk_importmapbase_modifiedby

See systemuser Entity [lk_importmapbase_modifiedby](systemuser.md#BKMK_lk_importmapbase_modifiedby) One-To-Many relationship.
importmap

