---
title: "Connection Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the Connection entity."
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
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Connection Entity Reference

Relationship between two entities.

## Entity Properties

**DisplayName**: Connection<br />
**DisplayCollectionName**: Connections<br />
**SchemaName**: Connection<br />
**CollectionSchemaName**: Connections<br />
**LogicalName**: connection<br />
**LogicalCollectionName**: connections<br />
**EntitySetName**: connections<br />
**PrimaryIdAttribute**: connectionid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: UserOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [ConnectionId](#BKMK_ConnectionId)
- [Description](#BKMK_Description)
- [EffectiveEnd](#BKMK_EffectiveEnd)
- [EffectiveStart](#BKMK_EffectiveStart)
- [EntityImage](#BKMK_EntityImage)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [Record1Id](#BKMK_Record1Id)
- [Record1IdObjectTypeCode](#BKMK_Record1IdObjectTypeCode)
- [Record1RoleId](#BKMK_Record1RoleId)
- [Record2Id](#BKMK_Record2Id)
- [Record2IdObjectTypeCode](#BKMK_Record2IdObjectTypeCode)
- [Record2RoleId](#BKMK_Record2RoleId)
- [StateCode](#BKMK_StateCode)
- [StatusCode](#BKMK_StatusCode)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)


### <a name="BKMK_ConnectionId"></a> ConnectionId

**Description**: Unique identifier of the connection.<br />
**DisplayName**: Connection<br />
**LogicalName**: connectionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Description"></a> Description

**Description**: Type additional information to describe the connection, such as the length or quality of the relationship.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_EffectiveEnd"></a> EffectiveEnd

**Description**: Enter the end date of the connection.<br />
**DisplayName**: Ending<br />
**LogicalName**: effectiveend<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_EffectiveStart"></a> EffectiveStart

**Description**: Enter the start date of the connection.<br />
**DisplayName**: Starting<br />
**LogicalName**: effectivestart<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


### <a name="BKMK_EntityImage"></a> EntityImage

**Description**: The default image for the entity.<br />
**DisplayName**: Entity Image<br />
**LogicalName**: entityimage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Image<br />
**IsPrimaryImage**: False<br />
**MaxHeight**: 144<br />
**MaxWidth**: 144


### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

**Description**: Unique identifier of the data import or data migration that created this record.<br />
**DisplayName**: Import Sequence Number<br />
**LogicalName**: importsequencenumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

**Description**: Date and time that the record was migrated.<br />
**DisplayName**: Record Created On<br />
**LogicalName**: overriddencreatedon<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateOnly


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

**Description**: Type of the owner of the connection, such as user, team, or business unit.<br />
**DisplayName**: <br />
**LogicalName**: owneridtype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: EntityName<br />


### <a name="BKMK_Record1Id"></a> Record1Id

**Description**: Choose the primary account, contact, or other record involved in the connection.<br />
**DisplayName**: Connected From<br />
**LogicalName**: record1id<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,activitypointer,appointment,channelaccessprofilerule,contact,email,fax,goal,knowledgearticle,knowledgebaserecord,letter,phonecall,position,processsession,recurringappointmentmaster,socialactivity,socialprofile,systemuser,task,team,territory


### <a name="BKMK_Record1IdObjectTypeCode"></a> Record1IdObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: record1idobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_Record1RoleId"></a> Record1RoleId

**Description**: Choose the primary party's role or relationship with the second party.<br />
**DisplayName**: Role (From)<br />
**LogicalName**: record1roleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: connectionrole


### <a name="BKMK_Record2Id"></a> Record2Id

**Description**: Select the secondary account, contact, or other record involved in the connection.<br />
**DisplayName**: Connected To<br />
**LogicalName**: record2id<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: account,activitypointer,appointment,channelaccessprofilerule,contact,email,fax,goal,knowledgearticle,knowledgebaserecord,letter,phonecall,position,processsession,recurringappointmentmaster,socialactivity,socialprofile,systemuser,task,team,territory


### <a name="BKMK_Record2IdObjectTypeCode"></a> Record2IdObjectTypeCode

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: record2idobjecttypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_Record2RoleId"></a> Record2RoleId

**Description**: Choose the secondary party's role or relationship with the primary party.<br />
**DisplayName**: Role (To)<br />
**LogicalName**: record2roleid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: connectionrole


### <a name="BKMK_StateCode"></a> StateCode

**Description**: Shows whether the connection is active or inactive. Inactive connections are read-only and can't be edited unless they are reactivated.<br />
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

**Description**: Reason for the status of the connection.<br />
**DisplayName**: Status Reason<br />
**LogicalName**: statuscode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Status<br />
**Options**:

- **Value**: 1 **Label**: Active **State**: 0
- **Value**: 2 **Label**: Inactive **State**: 1



### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Choose the local currency for the record to make sure budgets are reported in the correct currency.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [IsMaster](#BKMK_IsMaster)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [Name](#BKMK_Name)
- [OwnerIdName](#BKMK_OwnerIdName)
- [OwnerIdYomiName](#BKMK_OwnerIdYomiName)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningTeam](#BKMK_OwningTeam)
- [OwningUser](#BKMK_OwningUser)
- [Record1IdName](#BKMK_Record1IdName)
- [Record1ObjectTypeCode](#BKMK_Record1ObjectTypeCode)
- [Record1RoleIdName](#BKMK_Record1RoleIdName)
- [Record2IdName](#BKMK_Record2IdName)
- [Record2ObjectTypeCode](#BKMK_Record2ObjectTypeCode)
- [Record2RoleIdName](#BKMK_Record2RoleIdName)
- [RelatedConnectionId](#BKMK_RelatedConnectionId)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [VersionNumber](#BKMK_VersionNumber)


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

**Description**: Name of the user who created the connection.<br />
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

**Description**: YomiName of the user who created the connection.<br />
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


### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_timestamp<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: entityimage_url<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_EntityImageId"></a> EntityImageId

**Description**: For internal use only.<br />
**DisplayName**: Entity Image Id<br />
**LogicalName**: entityimageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_IsMaster"></a> IsMaster

**Description**: Indicates that this is the master record.<br />
**DisplayName**: Is Master<br />
**LogicalName**: ismaster<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

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

**Description**: Name of the user who last modified the connection.<br />
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

**Description**: YomiName of the user who last modified the connection.<br />
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

**Description**: Shows who last updated the record on behalf of another user.<br />
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


### <a name="BKMK_Name"></a> Name

**Description**: Name of the connection.<br />
**DisplayName**: Connection Name<br />
**LogicalName**: name<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_OwnerIdName"></a> OwnerIdName

**Description**: Name of the owner of the connection.<br />
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

**Description**: Shows the business unit that the record owner belongs to.<br />
**DisplayName**: Owning Business Unit<br />
**LogicalName**: owningbusinessunit<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_OwningTeam"></a> OwningTeam

**Description**: Unique identifier of the team who owns the connection.<br />
**DisplayName**: Owning Team<br />
**LogicalName**: owningteam<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: team


### <a name="BKMK_OwningUser"></a> OwningUser

**Description**: Unique identifier of the user who owns the connection.<br />
**DisplayName**: Owning User<br />
**LogicalName**: owninguser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_Record1IdName"></a> Record1IdName

**Description**: Display name for the source record.<br />
**DisplayName**: Name (From)<br />
**LogicalName**: record1idname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_Record1ObjectTypeCode"></a> Record1ObjectTypeCode

**Description**: Shows the record type of the source record.<br />
**DisplayName**: Type (From)<br />
**LogicalName**: record1objecttypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Account
- **Value**: 2 **Label**: Contact
- **Value**: 8 **Label**: User
- **Value**: 9 **Label**: Team
- **Value**: 50 **Label**: Position
- **Value**: 99 **Label**: Social Profile
- **Value**: 2013 **Label**: Territory
- **Value**: 4200 **Label**: Activity
- **Value**: 4201 **Label**: Appointment
- **Value**: 4202 **Label**: Email
- **Value**: 4204 **Label**: Fax
- **Value**: 4207 **Label**: Letter
- **Value**: 4210 **Label**: Phone Call
- **Value**: 4212 **Label**: Task
- **Value**: 4216 **Label**: Social Activity
- **Value**: 4251 **Label**: Recurring Appointment
- **Value**: 4710 **Label**: Process Session
- **Value**: 9400 **Label**: Channel Access Profile Rule
- **Value**: 9600 **Label**: Goal
- **Value**: 9930 **Label**: Knowledge Base Record
- **Value**: 9953 **Label**: Knowledge Article



### <a name="BKMK_Record1RoleIdName"></a> Record1RoleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: record1roleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Record2IdName"></a> Record2IdName

**Description**: Display name for the target record.<br />
**DisplayName**: Name (To)<br />
**LogicalName**: record2idname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_Record2ObjectTypeCode"></a> Record2ObjectTypeCode

**Description**: Shows the record type of the target record.<br />
**DisplayName**: Type (To)<br />
**LogicalName**: record2objecttypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Account
- **Value**: 2 **Label**: Contact
- **Value**: 8 **Label**: User
- **Value**: 9 **Label**: Team
- **Value**: 50 **Label**: Position
- **Value**: 99 **Label**: Social Profile
- **Value**: 2013 **Label**: Territory
- **Value**: 4200 **Label**: Activity
- **Value**: 4201 **Label**: Appointment
- **Value**: 4202 **Label**: Email
- **Value**: 4204 **Label**: Fax
- **Value**: 4207 **Label**: Letter
- **Value**: 4210 **Label**: Phone Call
- **Value**: 4212 **Label**: Task
- **Value**: 4216 **Label**: Social Activity
- **Value**: 4251 **Label**: Recurring Appointment
- **Value**: 4710 **Label**: Process Session
- **Value**: 9400 **Label**: Channel Access Profile Rule
- **Value**: 9600 **Label**: Goal
- **Value**: 9930 **Label**: Knowledge Base Record
- **Value**: 9953 **Label**: Knowledge Article



### <a name="BKMK_Record2RoleIdName"></a> Record2RoleIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: record2roleidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_RelatedConnectionId"></a> RelatedConnectionId

**Description**: Unique identifier for the reciprocal connection record.<br />
**DisplayName**: Reciprocal Connection<br />
**LogicalName**: relatedconnectionid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: connection


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

**Description**: Version number of the connection.<br />
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

- [Connection_AsyncOperations](#BKMK_Connection_AsyncOperations)
- [connection_related_connection](#BKMK_connection_related_connection)
- [userentityinstancedata_connection](#BKMK_userentityinstancedata_connection)
- [connection_principalobjectattributeaccess](#BKMK_connection_principalobjectattributeaccess)
- [Connection_SyncErrors](#BKMK_Connection_SyncErrors)
- [Connection_ProcessSessions](#BKMK_Connection_ProcessSessions)


### <a name="BKMK_Connection_AsyncOperations"></a> Connection_AsyncOperations

Same as asyncoperation entity [Connection_AsyncOperations](asyncoperation.md#BKMK_Connection_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Connection_AsyncOperations<br />
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


### <a name="BKMK_connection_related_connection"></a> connection_related_connection

Same as connection entity [connection_related_connection](connection.md#BKMK_connection_related_connection) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: relatedconnectionid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: connection_related_connection<br />
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


### <a name="BKMK_userentityinstancedata_connection"></a> userentityinstancedata_connection

Same as userentityinstancedata entity [userentityinstancedata_connection](userentityinstancedata.md#BKMK_userentityinstancedata_connection) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_connection<br />
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


### <a name="BKMK_connection_principalobjectattributeaccess"></a> connection_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [connection_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_connection_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: connection_principalobjectattributeaccess<br />
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


### <a name="BKMK_Connection_SyncErrors"></a> Connection_SyncErrors

Same as syncerror entity [Connection_SyncErrors](syncerror.md#BKMK_Connection_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: Connection_SyncErrors<br />
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


### <a name="BKMK_Connection_ProcessSessions"></a> Connection_ProcessSessions

Same as processsession entity [Connection_ProcessSessions](processsession.md#BKMK_Connection_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Connection_ProcessSessions<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [territory_connections1](#BKMK_territory_connections1)
- [territory_connections2](#BKMK_territory_connections2)
- [knowledgearticle_connections1](#BKMK_knowledgearticle_connections1)
- [knowledgearticle_connections2](#BKMK_knowledgearticle_connections2)
- [profilerule_connections1](#BKMK_profilerule_connections1)
- [profilerule_connections2](#BKMK_profilerule_connections2)
- [KnowledgeBaseRecord_connections1](#BKMK_KnowledgeBaseRecord_connections1)
- [KnowledgeBaseRecord_connections2](#BKMK_KnowledgeBaseRecord_connections2)
- [processsession_connections1](#BKMK_processsession_connections1)
- [contact_connections1](#BKMK_contact_connections1)
- [recurringappointmentmaster_connections1](#BKMK_recurringappointmentmaster_connections1)
- [processsession_connections2](#BKMK_processsession_connections2)
- [letter_connections1](#BKMK_letter_connections1)
- [connection_role_connections2](#BKMK_connection_role_connections2)
- [systemuser_connections2](#BKMK_systemuser_connections2)
- [letter_connections2](#BKMK_letter_connections2)
- [appointment_connections1](#BKMK_appointment_connections1)
- [email_connections1](#BKMK_email_connections1)
- [account_connections1](#BKMK_account_connections1)
- [fax_connections2](#BKMK_fax_connections2)
- [activitypointer_connections2](#BKMK_activitypointer_connections2)
- [socialprofile_connections2](#BKMK_socialprofile_connections2)
- [createdby_connection](#BKMK_createdby_connection)
- [account_connections2](#BKMK_account_connections2)
- [phonecall_connections1](#BKMK_phonecall_connections1)
- [task_connections1](#BKMK_task_connections1)
- [modifiedby_connection](#BKMK_modifiedby_connection)
- [appointment_connections2](#BKMK_appointment_connections2)
- [phonecall_connections2](#BKMK_phonecall_connections2)
- [TransactionCurrency_Connection](#BKMK_TransactionCurrency_Connection)
- [task_connections2](#BKMK_task_connections2)
- [fax_connections1](#BKMK_fax_connections1)
- [position_connection2](#BKMK_position_connection2)
- [goal_connections1](#BKMK_goal_connections1)
- [connection_role_connections1](#BKMK_connection_role_connections1)
- [position_connection1](#BKMK_position_connection1)
- [email_connections2](#BKMK_email_connections2)
- [team_connections1](#BKMK_team_connections1)
- [lk_connectionbase_modifiedonbehalfby](#BKMK_lk_connectionbase_modifiedonbehalfby)
- [socialactivity_connections1](#BKMK_socialactivity_connections1)
- [connection_related_connection](#BKMK_connection_related_connection)
- [contact_connections2](#BKMK_contact_connections2)
- [lk_connectionbase_createdonbehalfby](#BKMK_lk_connectionbase_createdonbehalfby)
- [activitypointer_connections1](#BKMK_activitypointer_connections1)
- [systemuser_connections1](#BKMK_systemuser_connections1)
- [team_connections2](#BKMK_team_connections2)
- [business_unit_connections](#BKMK_business_unit_connections)
- [goal_connections2](#BKMK_goal_connections2)
- [socialprofile_connections1](#BKMK_socialprofile_connections1)
- [socialactivity_connections2](#BKMK_socialactivity_connections2)
- [recurringappointmentmaster_connections2](#BKMK_recurringappointmentmaster_connections2)


### <a name="BKMK_territory_connections1"></a> territory_connections1

See territory Entity [territory_connections1](territory.md#BKMK_territory_connections1) One-To-Many relationship.

### <a name="BKMK_territory_connections2"></a> territory_connections2

See territory Entity [territory_connections2](territory.md#BKMK_territory_connections2) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_connections1"></a> knowledgearticle_connections1

See knowledgearticle Entity [knowledgearticle_connections1](knowledgearticle.md#BKMK_knowledgearticle_connections1) One-To-Many relationship.

### <a name="BKMK_knowledgearticle_connections2"></a> knowledgearticle_connections2

See knowledgearticle Entity [knowledgearticle_connections2](knowledgearticle.md#BKMK_knowledgearticle_connections2) One-To-Many relationship.

### <a name="BKMK_profilerule_connections1"></a> profilerule_connections1

See channelaccessprofilerule Entity [profilerule_connections1](channelaccessprofilerule.md#BKMK_profilerule_connections1) One-To-Many relationship.

### <a name="BKMK_profilerule_connections2"></a> profilerule_connections2

See channelaccessprofilerule Entity [profilerule_connections2](channelaccessprofilerule.md#BKMK_profilerule_connections2) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_connections1"></a> KnowledgeBaseRecord_connections1

See knowledgebaserecord Entity [KnowledgeBaseRecord_connections1](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_connections1) One-To-Many relationship.

### <a name="BKMK_KnowledgeBaseRecord_connections2"></a> KnowledgeBaseRecord_connections2

See knowledgebaserecord Entity [KnowledgeBaseRecord_connections2](knowledgebaserecord.md#BKMK_KnowledgeBaseRecord_connections2) One-To-Many relationship.

### <a name="BKMK_processsession_connections1"></a> processsession_connections1

See processsession Entity [processsession_connections1](processsession.md#BKMK_processsession_connections1) One-To-Many relationship.

### <a name="BKMK_contact_connections1"></a> contact_connections1

See contact Entity [contact_connections1](contact.md#BKMK_contact_connections1) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_connections1"></a> recurringappointmentmaster_connections1

See recurringappointmentmaster Entity [recurringappointmentmaster_connections1](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_connections1) One-To-Many relationship.

### <a name="BKMK_processsession_connections2"></a> processsession_connections2

See processsession Entity [processsession_connections2](processsession.md#BKMK_processsession_connections2) One-To-Many relationship.

### <a name="BKMK_letter_connections1"></a> letter_connections1

See letter Entity [letter_connections1](letter.md#BKMK_letter_connections1) One-To-Many relationship.

### <a name="BKMK_connection_role_connections2"></a> connection_role_connections2

See connectionrole Entity [connection_role_connections2](connectionrole.md#BKMK_connection_role_connections2) One-To-Many relationship.

### <a name="BKMK_systemuser_connections2"></a> systemuser_connections2

See systemuser Entity [systemuser_connections2](systemuser.md#BKMK_systemuser_connections2) One-To-Many relationship.

### <a name="BKMK_letter_connections2"></a> letter_connections2

See letter Entity [letter_connections2](letter.md#BKMK_letter_connections2) One-To-Many relationship.

### <a name="BKMK_appointment_connections1"></a> appointment_connections1

See appointment Entity [appointment_connections1](appointment.md#BKMK_appointment_connections1) One-To-Many relationship.

### <a name="BKMK_email_connections1"></a> email_connections1

See email Entity [email_connections1](email.md#BKMK_email_connections1) One-To-Many relationship.

### <a name="BKMK_account_connections1"></a> account_connections1

See account Entity [account_connections1](account.md#BKMK_account_connections1) One-To-Many relationship.

### <a name="BKMK_fax_connections2"></a> fax_connections2

See fax Entity [fax_connections2](fax.md#BKMK_fax_connections2) One-To-Many relationship.

### <a name="BKMK_activitypointer_connections2"></a> activitypointer_connections2

See activitypointer Entity [activitypointer_connections2](activitypointer.md#BKMK_activitypointer_connections2) One-To-Many relationship.

### <a name="BKMK_socialprofile_connections2"></a> socialprofile_connections2

See socialprofile Entity [socialprofile_connections2](socialprofile.md#BKMK_socialprofile_connections2) One-To-Many relationship.

### <a name="BKMK_createdby_connection"></a> createdby_connection

See systemuser Entity [createdby_connection](systemuser.md#BKMK_createdby_connection) One-To-Many relationship.

### <a name="BKMK_account_connections2"></a> account_connections2

See account Entity [account_connections2](account.md#BKMK_account_connections2) One-To-Many relationship.

### <a name="BKMK_phonecall_connections1"></a> phonecall_connections1

See phonecall Entity [phonecall_connections1](phonecall.md#BKMK_phonecall_connections1) One-To-Many relationship.

### <a name="BKMK_task_connections1"></a> task_connections1

See task Entity [task_connections1](task.md#BKMK_task_connections1) One-To-Many relationship.

### <a name="BKMK_modifiedby_connection"></a> modifiedby_connection

See systemuser Entity [modifiedby_connection](systemuser.md#BKMK_modifiedby_connection) One-To-Many relationship.

### <a name="BKMK_appointment_connections2"></a> appointment_connections2

See appointment Entity [appointment_connections2](appointment.md#BKMK_appointment_connections2) One-To-Many relationship.

### <a name="BKMK_phonecall_connections2"></a> phonecall_connections2

See phonecall Entity [phonecall_connections2](phonecall.md#BKMK_phonecall_connections2) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_Connection"></a> TransactionCurrency_Connection

See transactioncurrency Entity [TransactionCurrency_Connection](transactioncurrency.md#BKMK_TransactionCurrency_Connection) One-To-Many relationship.

### <a name="BKMK_task_connections2"></a> task_connections2

See task Entity [task_connections2](task.md#BKMK_task_connections2) One-To-Many relationship.

### <a name="BKMK_fax_connections1"></a> fax_connections1

See fax Entity [fax_connections1](fax.md#BKMK_fax_connections1) One-To-Many relationship.

### <a name="BKMK_position_connection2"></a> position_connection2

See position Entity [position_connection2](position.md#BKMK_position_connection2) One-To-Many relationship.

### <a name="BKMK_goal_connections1"></a> goal_connections1

See goal Entity [goal_connections1](goal.md#BKMK_goal_connections1) One-To-Many relationship.

### <a name="BKMK_connection_role_connections1"></a> connection_role_connections1

See connectionrole Entity [connection_role_connections1](connectionrole.md#BKMK_connection_role_connections1) One-To-Many relationship.

### <a name="BKMK_position_connection1"></a> position_connection1

See position Entity [position_connection1](position.md#BKMK_position_connection1) One-To-Many relationship.

### <a name="BKMK_email_connections2"></a> email_connections2

See email Entity [email_connections2](email.md#BKMK_email_connections2) One-To-Many relationship.

### <a name="BKMK_team_connections1"></a> team_connections1

See team Entity [team_connections1](team.md#BKMK_team_connections1) One-To-Many relationship.

### <a name="BKMK_lk_connectionbase_modifiedonbehalfby"></a> lk_connectionbase_modifiedonbehalfby

See systemuser Entity [lk_connectionbase_modifiedonbehalfby](systemuser.md#BKMK_lk_connectionbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_socialactivity_connections1"></a> socialactivity_connections1

See socialactivity Entity [socialactivity_connections1](socialactivity.md#BKMK_socialactivity_connections1) One-To-Many relationship.

### <a name="BKMK_connection_related_connection"></a> connection_related_connection

See connection Entity [connection_related_connection](connection.md#BKMK_connection_related_connection) One-To-Many relationship.

### <a name="BKMK_contact_connections2"></a> contact_connections2

See contact Entity [contact_connections2](contact.md#BKMK_contact_connections2) One-To-Many relationship.

### <a name="BKMK_lk_connectionbase_createdonbehalfby"></a> lk_connectionbase_createdonbehalfby

See systemuser Entity [lk_connectionbase_createdonbehalfby](systemuser.md#BKMK_lk_connectionbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_activitypointer_connections1"></a> activitypointer_connections1

See activitypointer Entity [activitypointer_connections1](activitypointer.md#BKMK_activitypointer_connections1) One-To-Many relationship.

### <a name="BKMK_systemuser_connections1"></a> systemuser_connections1

See systemuser Entity [systemuser_connections1](systemuser.md#BKMK_systemuser_connections1) One-To-Many relationship.

### <a name="BKMK_team_connections2"></a> team_connections2

See team Entity [team_connections2](team.md#BKMK_team_connections2) One-To-Many relationship.

### <a name="BKMK_business_unit_connections"></a> business_unit_connections

See businessunit Entity [business_unit_connections](businessunit.md#BKMK_business_unit_connections) One-To-Many relationship.

### <a name="BKMK_goal_connections2"></a> goal_connections2

See goal Entity [goal_connections2](goal.md#BKMK_goal_connections2) One-To-Many relationship.

### <a name="BKMK_socialprofile_connections1"></a> socialprofile_connections1

See socialprofile Entity [socialprofile_connections1](socialprofile.md#BKMK_socialprofile_connections1) One-To-Many relationship.

### <a name="BKMK_socialactivity_connections2"></a> socialactivity_connections2

See socialactivity Entity [socialactivity_connections2](socialactivity.md#BKMK_socialactivity_connections2) One-To-Many relationship.

### <a name="BKMK_recurringappointmentmaster_connections2"></a> recurringappointmentmaster_connections2

See recurringappointmentmaster Entity [recurringappointmentmaster_connections2](recurringappointmentmaster.md#BKMK_recurringappointmentmaster_connections2) One-To-Many relationship.
connection

