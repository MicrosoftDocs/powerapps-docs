---
title: "SLA Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SLA entity."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SLA Entity Reference

Contains information about the tracked service-level KPIs for cases that belong to different customers.

## Entity Properties

**DisplayName**: SLA<br />
**DisplayCollectionName**: SLAs<br />
**SchemaName**: SLA<br />
**CollectionSchemaName**: SLAs<br />
**LogicalName**: sla<br />
**LogicalCollectionName**: slas<br />
**EntitySetName**: slas<br />
**PrimaryIdAttribute**: slaid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AllowPauseResume](#BKMK_AllowPauseResume)
- [ApplicableFrom](#BKMK_ApplicableFrom)
- [ApplicableFromPickList](#BKMK_ApplicableFromPickList)
- [BusinessHoursId](#BKMK_BusinessHoursId)
- [ChangedAttributeList](#BKMK_ChangedAttributeList)
- [Description](#BKMK_Description)
- [IsDefault](#BKMK_IsDefault)
- [Name](#BKMK_Name)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [PrimaryEntityOTC](#BKMK_PrimaryEntityOTC)
- [SLAId](#BKMK_SLAId)
- [SLAType](#BKMK_SLAType)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [WorkflowId](#BKMK_WorkflowId)
- [WorkflowIdName](#BKMK_WorkflowIdName)


### <a name="BKMK_AllowPauseResume"></a> AllowPauseResume

**Description**: Select whether this SLA will allow pausing and resuming during the time calculation.<br />
**DisplayName**: Allow Pause and Resume<br />
**LogicalName**: allowpauseresume<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Allow
- **FalseOption Value**: 0 **Label**: Do Not Allow

**DefaultValue**: False


### <a name="BKMK_ApplicableFrom"></a> ApplicableFrom

**Description**: Select the field that specifies the date and time from which the SLA items will be calculated for the case record. For example, if you select the Case Created On field, SLA calculation will begin from the time the case is created. <br />
**DisplayName**: Applicable From<br />
**LogicalName**: applicablefrom<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ApplicableFromPickList"></a> ApplicableFromPickList

**Description**: Select the field that specifies the date and time from which the SLA items will be calculated. For example, if you select the Case Created On field, SLA calculation will begin from the time the case is created.<br />
**DisplayName**: Applicable From<br />
**LogicalName**: applicablefrompicklist<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: No
- **Value**: 2 **Label**: Yes



### <a name="BKMK_BusinessHoursId"></a> BusinessHoursId

**Description**: Choose the business hours for calculating SLA item timelines.<br />
**DisplayName**: Business Hours<br />
**LogicalName**: businesshoursid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: calendar


### <a name="BKMK_ChangedAttributeList"></a> ChangedAttributeList

**Description**: Type additional information to describe the SLA<br />
**DisplayName**: ChangedAttributeList<br />
**LogicalName**: changedattributelist<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_Description"></a> Description

**Description**: Type additional information to describe the SLA<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_IsDefault"></a> IsDefault

**Description**: Tells whether this SLA is the default one.<br />
**DisplayName**: Is Default<br />
**LogicalName**: isdefault<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Name"></a> Name

**Description**: Type a descriptive name of the service level agreement (SLA).<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_OwnerId"></a> OwnerId

**Description**: Enter the user or team who owns the SLA. This field is updated every time the item is assigned to a different user.<br />
**DisplayName**: Owner<br />
**LogicalName**: ownerid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Owner<br />
**Targets**: systemuser


### <a name="BKMK_OwnerIdType"></a> OwnerIdType

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

**Description**: Unique identifier for the business unit that owns the record<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier for the team that owns the record.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier for the user that owns the record.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_PrimaryEntityOTC"></a> PrimaryEntityOTC

**Description**: Shows the primary entity that the SLA has been created for.<br />
**DisplayName**: Primary Entity<br />
**LogicalName**: primaryentityotc<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_SLAId"></a> SLAId

**Description**: Unique identifier of the SLA.<br />
**DisplayName**: SLA<br />
**LogicalName**: slaid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SLAType"></a> SLAType

**Description**: Select the type of service level agreement (SLA).<br />
**DisplayName**: SLA Type<br />
**LogicalName**: slatype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Standard
- **Value**: 1 **Label**: Enhanced



### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the Service Level Agreement (SLA) is active or inactive.<br />
**DisplayName**: Status<br />
**LogicalName**: statecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: State<br />
**Options**:

- **Value**: 0 **Label**: Draft **DefaultStatus**: 1 **InvariantName**: Draft
- **Value**: 1 **Label**: Active **DefaultStatus**: 2 **InvariantName**: Active



### <a name="BKMK_StatusCode"></a> StatusCode

**Description**: Select the status of the service level agreement (SLA).<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Draft **State**: 0
- **Value**: 2 **Label**: Active **State**: 1



### <a name="BKMK_WorkflowId"></a> WorkflowId

**Description**: Workflow associated with the SLA.<br />
**DisplayName**: Workflow ID<br />
**LogicalName**: workflowid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: workflow


### <a name="BKMK_WorkflowIdName"></a> WorkflowIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: workflowidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [BusinessHoursIdName](#BKMK_BusinessHoursIdName)
- [ComponentState](#BKMK_ComponentState)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsManaged](#BKMK_IsManaged)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverwriteTime](#BKMK_OverwriteTime)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [SLAIdUnique](#BKMK_SLAIdUnique)
- [SolutionId](#BKMK_SolutionId)
- [SupportingSolutionId](#BKMK_SupportingSolutionId)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_BusinessHoursIdName"></a> BusinessHoursIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businesshoursidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate between the currency associated with the SLA record and the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


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
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Shows who created the record on behalf of another user.<br />
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
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

**Description**: Choose the entity type that the SLA is defined.<br />
**DisplayName**: Object Type Code<br />
**LogicalName**: objecttypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
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


### <a name="BKMK_SLAIdUnique"></a> SLAIdUnique

**Description**: For internal use only.<br />
**DisplayName**: Unique Id<br />
**LogicalName**: slaidunique<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the SLA record.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_TransactionCurrencyIdName"></a> TransactionCurrencyIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: transactioncurrencyidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the SLA.<br />
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

- [sla_socialactivity](#BKMK_sla_socialactivity)
- [manualsla_contact](#BKMK_manualsla_contact)
- [slabase_BulkDeleteFailures](#BKMK_slabase_BulkDeleteFailures)
- [manualsla_fax](#BKMK_manualsla_fax)
- [manualsla_activitypointer](#BKMK_manualsla_activitypointer)
- [slabase_AsyncOperations](#BKMK_slabase_AsyncOperations)
- [sla_Annotation](#BKMK_sla_Annotation)
- [sla_task](#BKMK_sla_task)
- [sla_activitypointer](#BKMK_sla_activitypointer)
- [manualsla_task](#BKMK_manualsla_task)
- [manualsla_account](#BKMK_manualsla_account)
- [sla_letter](#BKMK_sla_letter)
- [manualsla_phonecall](#BKMK_manualsla_phonecall)
- [sla_email](#BKMK_sla_email)
- [sla_appointment](#BKMK_sla_appointment)
- [sla_slaitem_slaId](#BKMK_sla_slaitem_slaId)
- [sla_account](#BKMK_sla_account)
- [SLA_SyncErrors](#BKMK_SLA_SyncErrors)
- [manualsla_letter](#BKMK_manualsla_letter)
- [manualsla_appointment](#BKMK_manualsla_appointment)
- [manualsla_socialactivity](#BKMK_manualsla_socialactivity)
- [slabase_userentityinstancedatas](#BKMK_slabase_userentityinstancedatas)
- [sla_fax](#BKMK_sla_fax)
- [sla_contact](#BKMK_sla_contact)
- [slabase_ProcessSessions](#BKMK_slabase_ProcessSessions)
- [sla_phonecall](#BKMK_sla_phonecall)
- [manualsla_email](#BKMK_manualsla_email)


### <a name="BKMK_sla_socialactivity"></a> sla_socialactivity

Same as socialactivity entity [sla_socialactivity](socialactivity.md#BKMK_sla_socialactivity) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_socialactivity<br />
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


### <a name="BKMK_manualsla_contact"></a> manualsla_contact

Same as contact entity [manualsla_contact](contact.md#BKMK_manualsla_contact) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_contact<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10000

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_slabase_BulkDeleteFailures"></a> slabase_BulkDeleteFailures

Same as bulkdeletefailure entity [slabase_BulkDeleteFailures](bulkdeletefailure.md#BKMK_slabase_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: slabase_BulkDeleteFailures<br />
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


### <a name="BKMK_manualsla_fax"></a> manualsla_fax

Same as fax entity [manualsla_fax](fax.md#BKMK_manualsla_fax) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_fax<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10001

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_manualsla_activitypointer"></a> manualsla_activitypointer

Same as activitypointer entity [manualsla_activitypointer](activitypointer.md#BKMK_manualsla_activitypointer) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_activitypointer<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10001

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_slabase_AsyncOperations"></a> slabase_AsyncOperations

Same as asyncoperation entity [slabase_AsyncOperations](asyncoperation.md#BKMK_slabase_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: slabase_AsyncOperations<br />
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


### <a name="BKMK_sla_Annotation"></a> sla_Annotation

Same as annotation entity [sla_Annotation](annotation.md#BKMK_sla_Annotation) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_Annotation<br />
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


### <a name="BKMK_sla_task"></a> sla_task

Same as task entity [sla_task](task.md#BKMK_sla_task) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_task<br />
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


### <a name="BKMK_sla_activitypointer"></a> sla_activitypointer

Same as activitypointer entity [sla_activitypointer](activitypointer.md#BKMK_sla_activitypointer) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_activitypointer<br />
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


### <a name="BKMK_manualsla_task"></a> manualsla_task

Same as task entity [manualsla_task](task.md#BKMK_manualsla_task) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_task<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10001

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_manualsla_account"></a> manualsla_account

Same as account entity [manualsla_account](account.md#BKMK_manualsla_account) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_account<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10000

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_sla_letter"></a> sla_letter

Same as letter entity [sla_letter](letter.md#BKMK_sla_letter) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_letter<br />
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


### <a name="BKMK_manualsla_phonecall"></a> manualsla_phonecall

Same as phonecall entity [manualsla_phonecall](phonecall.md#BKMK_manualsla_phonecall) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_phonecall<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10001

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_sla_email"></a> sla_email

Same as email entity [sla_email](email.md#BKMK_sla_email) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_email<br />
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


### <a name="BKMK_sla_appointment"></a> sla_appointment

Same as appointment entity [sla_appointment](appointment.md#BKMK_sla_appointment) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_appointment<br />
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


### <a name="BKMK_sla_slaitem_slaId"></a> sla_slaitem_slaId

Same as slaitem entity [sla_slaitem_slaId](slaitem.md#BKMK_sla_slaitem_slaId) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_slaitem_slaId<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10000

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Cascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_sla_account"></a> sla_account

Same as account entity [sla_account](account.md#BKMK_sla_account) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_account<br />
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


### <a name="BKMK_SLA_SyncErrors"></a> SLA_SyncErrors

Same as syncerror entity [SLA_SyncErrors](syncerror.md#BKMK_SLA_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: SLA_SyncErrors<br />
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


### <a name="BKMK_manualsla_letter"></a> manualsla_letter

Same as letter entity [manualsla_letter](letter.md#BKMK_manualsla_letter) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_letter<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10001

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_manualsla_appointment"></a> manualsla_appointment

Same as appointment entity [manualsla_appointment](appointment.md#BKMK_manualsla_appointment) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_appointment<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10000

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_manualsla_socialactivity"></a> manualsla_socialactivity

Same as socialactivity entity [manualsla_socialactivity](socialactivity.md#BKMK_manualsla_socialactivity) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_socialactivity<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10001

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_slabase_userentityinstancedatas"></a> slabase_userentityinstancedatas

Same as userentityinstancedata entity [slabase_userentityinstancedatas](userentityinstancedata.md#BKMK_slabase_userentityinstancedatas) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: slabase_userentityinstancedatas<br />
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


### <a name="BKMK_sla_fax"></a> sla_fax

Same as fax entity [sla_fax](fax.md#BKMK_sla_fax) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_fax<br />
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


### <a name="BKMK_sla_contact"></a> sla_contact

Same as contact entity [sla_contact](contact.md#BKMK_sla_contact) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_contact<br />
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


### <a name="BKMK_slabase_ProcessSessions"></a> slabase_ProcessSessions

Same as processsession entity [slabase_ProcessSessions](processsession.md#BKMK_slabase_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: slabase_ProcessSessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 110

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_sla_phonecall"></a> sla_phonecall

Same as phonecall entity [sla_phonecall](phonecall.md#BKMK_sla_phonecall) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: slainvokedid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: sla_phonecall<br />
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


### <a name="BKMK_manualsla_email"></a> manualsla_email

Same as email entity [manualsla_email](email.md#BKMK_manualsla_email) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: slaid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: manualsla_email<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 10000

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: RemoveLink
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [slabase_workflowid](#BKMK_slabase_workflowid)
- [lk_slabase_modifiedonbehalfby](#BKMK_lk_slabase_modifiedonbehalfby)
- [lk_slabase_createdonbehalfby](#BKMK_lk_slabase_createdonbehalfby)
- [lk_slabase_createdby](#BKMK_lk_slabase_createdby)
- [team_slaBase](#BKMK_team_slaBase)
- [TransactionCurrency_SLA](#BKMK_TransactionCurrency_SLA)
- [lk_slabase_modifiedby](#BKMK_lk_slabase_modifiedby)
- [user_slabase](#BKMK_user_slabase)
- [business_unit_slabase](#BKMK_business_unit_slabase)
- [slabase_businesshoursid](#BKMK_slabase_businesshoursid)


### <a name="BKMK_slabase_workflowid"></a> slabase_workflowid

See workflow Entity [slabase_workflowid](workflow.md#BKMK_slabase_workflowid) One-To-Many relationship.

### <a name="BKMK_lk_slabase_modifiedonbehalfby"></a> lk_slabase_modifiedonbehalfby

See systemuser Entity [lk_slabase_modifiedonbehalfby](systemuser.md#BKMK_lk_slabase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_slabase_createdonbehalfby"></a> lk_slabase_createdonbehalfby

See systemuser Entity [lk_slabase_createdonbehalfby](systemuser.md#BKMK_lk_slabase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_slabase_createdby"></a> lk_slabase_createdby

See systemuser Entity [lk_slabase_createdby](systemuser.md#BKMK_lk_slabase_createdby) One-To-Many relationship.

### <a name="BKMK_team_slaBase"></a> team_slaBase

See team Entity [team_slaBase](team.md#BKMK_team_slaBase) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SLA"></a> TransactionCurrency_SLA

See transactioncurrency Entity [TransactionCurrency_SLA](transactioncurrency.md#BKMK_TransactionCurrency_SLA) One-To-Many relationship.

### <a name="BKMK_lk_slabase_modifiedby"></a> lk_slabase_modifiedby

See systemuser Entity [lk_slabase_modifiedby](systemuser.md#BKMK_lk_slabase_modifiedby) One-To-Many relationship.

### <a name="BKMK_user_slabase"></a> user_slabase

See systemuser Entity [user_slabase](systemuser.md#BKMK_user_slabase) One-To-Many relationship.

### <a name="BKMK_business_unit_slabase"></a> business_unit_slabase

See businessunit Entity [business_unit_slabase](businessunit.md#BKMK_business_unit_slabase) One-To-Many relationship.

### <a name="BKMK_slabase_businesshoursid"></a> slabase_businesshoursid

See calendar Entity [slabase_businesshoursid](calendar.md#BKMK_slabase_businesshoursid) One-To-Many relationship.
sla

