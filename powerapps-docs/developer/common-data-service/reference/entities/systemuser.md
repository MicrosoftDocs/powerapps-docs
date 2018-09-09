---
title: "SystemUser Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the SystemUser entity."
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
ms.date: 03/07/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# SystemUser Entity Reference

Person with access to the Microsoft CRM system and who owns objects in the Microsoft CRM database.

## Entity Properties

**DisplayName**: User<br />
**DisplayCollectionName**: Users<br />
**SchemaName**: SystemUser<br />
**CollectionSchemaName**: SystemUsers<br />
**LogicalName**: systemuser<br />
**LogicalCollectionName**: systemusers<br />
**EntitySetName**: systemusers<br />
**PrimaryIdAttribute**: systemuserid<br />
**PrimaryNameAttribute**: fullname<br />
**OwnershipType**: BusinessOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AccessMode](#BKMK_AccessMode)
- [Address1_AddressId](#BKMK_Address1_AddressId)
- [Address1_AddressTypeCode](#BKMK_Address1_AddressTypeCode)
- [Address1_City](#BKMK_Address1_City)
- [Address1_Country](#BKMK_Address1_Country)
- [Address1_County](#BKMK_Address1_County)
- [Address1_Fax](#BKMK_Address1_Fax)
- [Address1_Latitude](#BKMK_Address1_Latitude)
- [Address1_Line1](#BKMK_Address1_Line1)
- [Address1_Line2](#BKMK_Address1_Line2)
- [Address1_Line3](#BKMK_Address1_Line3)
- [Address1_Longitude](#BKMK_Address1_Longitude)
- [Address1_Name](#BKMK_Address1_Name)
- [Address1_PostalCode](#BKMK_Address1_PostalCode)
- [Address1_PostOfficeBox](#BKMK_Address1_PostOfficeBox)
- [Address1_ShippingMethodCode](#BKMK_Address1_ShippingMethodCode)
- [Address1_StateOrProvince](#BKMK_Address1_StateOrProvince)
- [Address1_Telephone1](#BKMK_Address1_Telephone1)
- [Address1_Telephone2](#BKMK_Address1_Telephone2)
- [Address1_Telephone3](#BKMK_Address1_Telephone3)
- [Address1_UPSZone](#BKMK_Address1_UPSZone)
- [Address1_UTCOffset](#BKMK_Address1_UTCOffset)
- [Address2_AddressId](#BKMK_Address2_AddressId)
- [Address2_AddressTypeCode](#BKMK_Address2_AddressTypeCode)
- [Address2_City](#BKMK_Address2_City)
- [Address2_Country](#BKMK_Address2_Country)
- [Address2_County](#BKMK_Address2_County)
- [Address2_Fax](#BKMK_Address2_Fax)
- [Address2_Latitude](#BKMK_Address2_Latitude)
- [Address2_Line1](#BKMK_Address2_Line1)
- [Address2_Line2](#BKMK_Address2_Line2)
- [Address2_Line3](#BKMK_Address2_Line3)
- [Address2_Longitude](#BKMK_Address2_Longitude)
- [Address2_Name](#BKMK_Address2_Name)
- [Address2_PostalCode](#BKMK_Address2_PostalCode)
- [Address2_PostOfficeBox](#BKMK_Address2_PostOfficeBox)
- [Address2_ShippingMethodCode](#BKMK_Address2_ShippingMethodCode)
- [Address2_StateOrProvince](#BKMK_Address2_StateOrProvince)
- [Address2_Telephone1](#BKMK_Address2_Telephone1)
- [Address2_Telephone2](#BKMK_Address2_Telephone2)
- [Address2_Telephone3](#BKMK_Address2_Telephone3)
- [Address2_UPSZone](#BKMK_Address2_UPSZone)
- [Address2_UTCOffset](#BKMK_Address2_UTCOffset)
- [ApplicationId](#BKMK_ApplicationId)
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CalendarId](#BKMK_CalendarId)
- [CALType](#BKMK_CALType)
- [DisplayInServiceViews](#BKMK_DisplayInServiceViews)
- [DomainName](#BKMK_DomainName)
- [EmailRouterAccessApproval](#BKMK_EmailRouterAccessApproval)
- [EmployeeId](#BKMK_EmployeeId)
- [EntityImage](#BKMK_EntityImage)
- [FirstName](#BKMK_FirstName)
- [GovernmentId](#BKMK_GovernmentId)
- [HomePhone](#BKMK_HomePhone)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [IncomingEmailDeliveryMethod](#BKMK_IncomingEmailDeliveryMethod)
- [InternalEMailAddress](#BKMK_InternalEMailAddress)
- [InviteStatusCode](#BKMK_InviteStatusCode)
- [IsDisabled](#BKMK_IsDisabled)
- [IsIntegrationUser](#BKMK_IsIntegrationUser)
- [IsLicensed](#BKMK_IsLicensed)
- [IsSyncWithDirectory](#BKMK_IsSyncWithDirectory)
- [JobTitle](#BKMK_JobTitle)
- [LastName](#BKMK_LastName)
- [MiddleName](#BKMK_MiddleName)
- [MobileAlertEMail](#BKMK_MobileAlertEMail)
- [MobileOfflineProfileId](#BKMK_MobileOfflineProfileId)
- [MobileOfflineProfileIdName](#BKMK_MobileOfflineProfileIdName)
- [MobilePhone](#BKMK_MobilePhone)
- [NickName](#BKMK_NickName)
- [OutgoingEmailDeliveryMethod](#BKMK_OutgoingEmailDeliveryMethod)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentSystemUserId](#BKMK_ParentSystemUserId)
- [PassportHi](#BKMK_PassportHi)
- [PassportLo](#BKMK_PassportLo)
- [PersonalEMailAddress](#BKMK_PersonalEMailAddress)
- [PhotoUrl](#BKMK_PhotoUrl)
- [PositionId](#BKMK_PositionId)
- [PreferredAddressCode](#BKMK_PreferredAddressCode)
- [PreferredEmailCode](#BKMK_PreferredEmailCode)
- [PreferredPhoneCode](#BKMK_PreferredPhoneCode)
- [ProcessId](#BKMK_ProcessId)
- [QueueId](#BKMK_QueueId)
- [Salutation](#BKMK_Salutation)
- [SetupUser](#BKMK_SetupUser)
- [SharePointEmailAddress](#BKMK_SharePointEmailAddress)
- [Skills](#BKMK_Skills)
- [StageId](#BKMK_StageId)
- [SystemUserId](#BKMK_SystemUserId)
- [TerritoryId](#BKMK_TerritoryId)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [Title](#BKMK_Title)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [TraversedPath](#BKMK_TraversedPath)
- [UserLicenseType](#BKMK_UserLicenseType)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [WindowsLiveID](#BKMK_WindowsLiveID)
- [YammerEmailAddress](#BKMK_YammerEmailAddress)
- [YammerUserId](#BKMK_YammerUserId)
- [YomiFirstName](#BKMK_YomiFirstName)
- [YomiLastName](#BKMK_YomiLastName)
- [YomiMiddleName](#BKMK_YomiMiddleName)


### <a name="BKMK_AccessMode"></a> AccessMode

**Description**: Type of user.<br />
**DisplayName**: Access Mode<br />
**LogicalName**: accessmode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Read-Write
- **Value**: 1 **Label**: Administrative
- **Value**: 2 **Label**: Read
- **Value**: 3 **Label**: Support User
- **Value**: 4 **Label**: Non-interactive
- **Value**: 5 **Label**: Delegated Admin



### <a name="BKMK_Address1_AddressId"></a> Address1_AddressId

**Description**: Unique identifier for address 1.<br />
**DisplayName**: Address 1: ID<br />
**LogicalName**: address1_addressid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Address1_AddressTypeCode"></a> Address1_AddressTypeCode

**Description**: Type of address for address 1, such as billing, shipping, or primary address.<br />
**DisplayName**: Address 1: Address Type<br />
**LogicalName**: address1_addresstypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address1_City"></a> Address1_City

**Description**: City name for address 1.<br />
**DisplayName**: City<br />
**LogicalName**: address1_city<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address1_Country"></a> Address1_Country

**Description**: Country/region name in address 1.<br />
**DisplayName**: Country/Region<br />
**LogicalName**: address1_country<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address1_County"></a> Address1_County

**Description**: County name for address 1.<br />
**DisplayName**: Address 1: County<br />
**LogicalName**: address1_county<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address1_Fax"></a> Address1_Fax

**Description**: Fax number for address 1.<br />
**DisplayName**: Address 1: Fax<br />
**LogicalName**: address1_fax<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_Address1_Latitude"></a> Address1_Latitude

**Description**: Latitude for address 1.<br />
**DisplayName**: Address 1: Latitude<br />
**LogicalName**: address1_latitude<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 90<br />
**MinValue**: -90<br />
**Precision**: 5


### <a name="BKMK_Address1_Line1"></a> Address1_Line1

**Description**: First line for entering address 1 information.<br />
**DisplayName**: Street 1<br />
**LogicalName**: address1_line1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Address1_Line2"></a> Address1_Line2

**Description**: Second line for entering address 1 information.<br />
**DisplayName**: Street 2<br />
**LogicalName**: address1_line2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Address1_Line3"></a> Address1_Line3

**Description**: Third line for entering address 1 information.<br />
**DisplayName**: Street 3<br />
**LogicalName**: address1_line3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Address1_Longitude"></a> Address1_Longitude

**Description**: Longitude for address 1.<br />
**DisplayName**: Address 1: Longitude<br />
**LogicalName**: address1_longitude<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 180<br />
**MinValue**: -180<br />
**Precision**: 5


### <a name="BKMK_Address1_Name"></a> Address1_Name

**Description**: Name to enter for address 1.<br />
**DisplayName**: Address 1: Name<br />
**LogicalName**: address1_name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Address1_PostalCode"></a> Address1_PostalCode

**Description**: ZIP Code or postal code for address 1.<br />
**DisplayName**: ZIP/Postal Code<br />
**LogicalName**: address1_postalcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 40


### <a name="BKMK_Address1_PostOfficeBox"></a> Address1_PostOfficeBox

**Description**: Post office box number for address 1.<br />
**DisplayName**: Address 1: Post Office Box<br />
**LogicalName**: address1_postofficebox<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 40


### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

**Description**: Method of shipment for address 1.<br />
**DisplayName**: Address 1: Shipping Method<br />
**LogicalName**: address1_shippingmethodcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

**Description**: State or province for address 1.<br />
**DisplayName**: State/Province<br />
**LogicalName**: address1_stateorprovince<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address1_Telephone1"></a> Address1_Telephone1

**Description**: First telephone number associated with address 1.<br />
**DisplayName**: Main Phone<br />
**LogicalName**: address1_telephone1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_Address1_Telephone2"></a> Address1_Telephone2

**Description**: Second telephone number associated with address 1.<br />
**DisplayName**: Other Phone<br />
**LogicalName**: address1_telephone2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address1_Telephone3"></a> Address1_Telephone3

**Description**: Third telephone number associated with address 1.<br />
**DisplayName**: Pager<br />
**LogicalName**: address1_telephone3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address1_UPSZone"></a> Address1_UPSZone

**Description**: United Parcel Service (UPS) zone for address 1.<br />
**DisplayName**: Address 1: UPS Zone<br />
**LogicalName**: address1_upszone<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4


### <a name="BKMK_Address1_UTCOffset"></a> Address1_UTCOffset

**Description**: UTC offset for address 1. This is the difference between local time and standard Coordinated Universal Time.<br />
**DisplayName**: Address 1: UTC Offset<br />
**LogicalName**: address1_utcoffset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: TimeZone<br />
**MaxValue**: 1500<br />
**MinValue**: -1500


### <a name="BKMK_Address2_AddressId"></a> Address2_AddressId

**Description**: Unique identifier for address 2.<br />
**DisplayName**: Address 2: ID<br />
**LogicalName**: address2_addressid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Address2_AddressTypeCode"></a> Address2_AddressTypeCode

**Description**: Type of address for address 2, such as billing, shipping, or primary address.<br />
**DisplayName**: Address 2: Address Type<br />
**LogicalName**: address2_addresstypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address2_City"></a> Address2_City

**Description**: City name for address 2.<br />
**DisplayName**: Other City<br />
**LogicalName**: address2_city<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address2_Country"></a> Address2_Country

**Description**: Country/region name in address 2.<br />
**DisplayName**: Other Country/Region<br />
**LogicalName**: address2_country<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address2_County"></a> Address2_County

**Description**: County name for address 2.<br />
**DisplayName**: Address 2: County<br />
**LogicalName**: address2_county<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address2_Fax"></a> Address2_Fax

**Description**: Fax number for address 2.<br />
**DisplayName**: Address 2: Fax<br />
**LogicalName**: address2_fax<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address2_Latitude"></a> Address2_Latitude

**Description**: Latitude for address 2.<br />
**DisplayName**: Address 2: Latitude<br />
**LogicalName**: address2_latitude<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 90<br />
**MinValue**: -90<br />
**Precision**: 5


### <a name="BKMK_Address2_Line1"></a> Address2_Line1

**Description**: First line for entering address 2 information.<br />
**DisplayName**: Other Street 1<br />
**LogicalName**: address2_line1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Address2_Line2"></a> Address2_Line2

**Description**: Second line for entering address 2 information.<br />
**DisplayName**: Other Street 2<br />
**LogicalName**: address2_line2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Address2_Line3"></a> Address2_Line3

**Description**: Third line for entering address 2 information.<br />
**DisplayName**: Other Street 3<br />
**LogicalName**: address2_line3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Address2_Longitude"></a> Address2_Longitude

**Description**: Longitude for address 2.<br />
**DisplayName**: Address 2: Longitude<br />
**LogicalName**: address2_longitude<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 180<br />
**MinValue**: -180<br />
**Precision**: 5


### <a name="BKMK_Address2_Name"></a> Address2_Name

**Description**: Name to enter for address 2.<br />
**DisplayName**: Address 2: Name<br />
**LogicalName**: address2_name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_Address2_PostalCode"></a> Address2_PostalCode

**Description**: ZIP Code or postal code for address 2.<br />
**DisplayName**: Other ZIP/Postal Code<br />
**LogicalName**: address2_postalcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 40


### <a name="BKMK_Address2_PostOfficeBox"></a> Address2_PostOfficeBox

**Description**: Post office box number for address 2.<br />
**DisplayName**: Address 2: Post Office Box<br />
**LogicalName**: address2_postofficebox<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 40


### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

**Description**: Method of shipment for address 2.<br />
**DisplayName**: Address 2: Shipping Method<br />
**LogicalName**: address2_shippingmethodcode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

**Description**: State or province for address 2.<br />
**DisplayName**: Other State/Province<br />
**LogicalName**: address2_stateorprovince<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_Address2_Telephone1"></a> Address2_Telephone1

**Description**: First telephone number associated with address 2.<br />
**DisplayName**: Address 2: Telephone 1<br />
**LogicalName**: address2_telephone1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address2_Telephone2"></a> Address2_Telephone2

**Description**: Second telephone number associated with address 2.<br />
**DisplayName**: Address 2: Telephone 2<br />
**LogicalName**: address2_telephone2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address2_Telephone3"></a> Address2_Telephone3

**Description**: Third telephone number associated with address 2.<br />
**DisplayName**: Address 2: Telephone 3<br />
**LogicalName**: address2_telephone3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address2_UPSZone"></a> Address2_UPSZone

**Description**: United Parcel Service (UPS) zone for address 2.<br />
**DisplayName**: Address 2: UPS Zone<br />
**LogicalName**: address2_upszone<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4


### <a name="BKMK_Address2_UTCOffset"></a> Address2_UTCOffset

**Description**: UTC offset for address 2. This is the difference between local time and standard Coordinated Universal Time.<br />
**DisplayName**: Address 2: UTC Offset<br />
**LogicalName**: address2_utcoffset<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: TimeZone<br />
**MaxValue**: 1500<br />
**MinValue**: -1500


### <a name="BKMK_ApplicationId"></a> ApplicationId

**Description**: The identifier for the application. This is used to access data in another application.<br />
**DisplayName**: Application ID<br />
**LogicalName**: applicationid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

**Description**: Unique identifier of the business unit with which the user is associated.<br />
**DisplayName**: Business Unit<br />
**LogicalName**: businessunitid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_CalendarId"></a> CalendarId

**Description**: Fiscal calendar associated with the user.<br />
**DisplayName**: Calendar<br />
**LogicalName**: calendarid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: calendar


### <a name="BKMK_CALType"></a> CALType

**Description**: License type of user.<br />
**DisplayName**: License Type<br />
**LogicalName**: caltype<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Professional
- **Value**: 1 **Label**: Administrative
- **Value**: 2 **Label**: Basic
- **Value**: 3 **Label**: Device Professional
- **Value**: 4 **Label**: Device Basic
- **Value**: 5 **Label**: Essential
- **Value**: 6 **Label**: Device Essential
- **Value**: 7 **Label**: Enterprise
- **Value**: 8 **Label**: Device Enterprise
- **Value**: 9 **Label**: Sales
- **Value**: 10 **Label**: Service
- **Value**: 11 **Label**: Field Service
- **Value**: 12 **Label**: Project Service



### <a name="BKMK_DisplayInServiceViews"></a> DisplayInServiceViews

**Description**: Whether to display the user in service views.<br />
**DisplayName**: Display in Service Views<br />
**LogicalName**: displayinserviceviews<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_DomainName"></a> DomainName

**Description**: Active Directory domain of which the user is a member.<br />
**DisplayName**: User Name<br />
**LogicalName**: domainname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_EmailRouterAccessApproval"></a> EmailRouterAccessApproval

**Description**: Shows the status of the primary email address.<br />
**DisplayName**: Primary Email Status<br />
**LogicalName**: emailrouteraccessapproval<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForCreate**: False<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Empty
- **Value**: 1 **Label**: Approved
- **Value**: 2 **Label**: Pending Approval
- **Value**: 3 **Label**: Rejected



### <a name="BKMK_EmployeeId"></a> EmployeeId

**Description**: Employee identifier for the user.<br />
**DisplayName**: Employee<br />
**LogicalName**: employeeid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EntityImage"></a> EntityImage

**Description**: Shows the default image for the record.<br />
**DisplayName**: Entity Image<br />
**LogicalName**: entityimage<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Image<br />
**IsPrimaryImage**: True<br />
**MaxHeight**: 144<br />
**MaxWidth**: 144


### <a name="BKMK_FirstName"></a> FirstName

**Description**: First name of the user.<br />
**DisplayName**: First Name<br />
**LogicalName**: firstname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_GovernmentId"></a> GovernmentId

**Description**: Government identifier for the user.<br />
**DisplayName**: Government<br />
**LogicalName**: governmentid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_HomePhone"></a> HomePhone

**Description**: Home phone number for the user.<br />
**DisplayName**: Home Phone<br />
**LogicalName**: homephone<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


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


### <a name="BKMK_IncomingEmailDeliveryMethod"></a> IncomingEmailDeliveryMethod

**Description**: Incoming email delivery method for the user.<br />
**DisplayName**: Incoming Email Delivery Method<br />
**LogicalName**: incomingemaildeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Microsoft Dynamics 365 for Outlook
- **Value**: 2 **Label**: Server-Side Synchronization or Email Router
- **Value**: 3 **Label**: Forward Mailbox



### <a name="BKMK_InternalEMailAddress"></a> InternalEMailAddress

**Description**: Internal email address for the user.<br />
**DisplayName**: Primary Email<br />
**LogicalName**: internalemailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_InviteStatusCode"></a> InviteStatusCode

**Description**: User invitation status.<br />
**DisplayName**: Invitation Status<br />
**LogicalName**: invitestatuscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: Invitation Not Sent
- **Value**: 1 **Label**: Invited
- **Value**: 2 **Label**: Invitation Near Expired
- **Value**: 3 **Label**: Invitation Expired
- **Value**: 4 **Label**: Invitation Accepted
- **Value**: 5 **Label**: Invitation Rejected
- **Value**: 6 **Label**: Invitation Revoked



### <a name="BKMK_IsDisabled"></a> IsDisabled

**Description**: Information about whether the user is enabled.<br />
**DisplayName**: Status<br />
**LogicalName**: isdisabled<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Disabled
- **FalseOption Value**: 0 **Label**: Enabled

**DefaultValue**: False


### <a name="BKMK_IsIntegrationUser"></a> IsIntegrationUser

**Description**: Check if user is an integration user.<br />
**DisplayName**: Integration user mode<br />
**LogicalName**: isintegrationuser<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsLicensed"></a> IsLicensed

**Description**: Information about whether the user is licensed.<br />
**DisplayName**: User Licensed<br />
**LogicalName**: islicensed<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_IsSyncWithDirectory"></a> IsSyncWithDirectory

**Description**: Information about whether the user is synced with the directory.<br />
**DisplayName**: User Synced<br />
**LogicalName**: issyncwithdirectory<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_JobTitle"></a> JobTitle

**Description**: Job title of the user.<br />
**DisplayName**: Job Title<br />
**LogicalName**: jobtitle<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_LastName"></a> LastName

**Description**: Last name of the user.<br />
**DisplayName**: Last Name<br />
**LogicalName**: lastname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_MiddleName"></a> MiddleName

**Description**: Middle name of the user.<br />
**DisplayName**: Middle Name<br />
**LogicalName**: middlename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_MobileAlertEMail"></a> MobileAlertEMail

**Description**: Mobile alert email address for the user.<br />
**DisplayName**: Mobile Alert Email<br />
**LogicalName**: mobilealertemail<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_MobileOfflineProfileId"></a> MobileOfflineProfileId

**Description**: Items contained with a particular SystemUser.<br />
**DisplayName**: Mobile Offline Profile<br />
**LogicalName**: mobileofflineprofileid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: mobileofflineprofile


### <a name="BKMK_MobileOfflineProfileIdName"></a> MobileOfflineProfileIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: mobileofflineprofileidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_MobilePhone"></a> MobilePhone

**Description**: Mobile phone number for the user.<br />
**DisplayName**: Mobile Phone<br />
**LogicalName**: mobilephone<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Phone<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_NickName"></a> NickName

**Description**: Nickname of the user.<br />
**DisplayName**: Nickname<br />
**LogicalName**: nickname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_OutgoingEmailDeliveryMethod"></a> OutgoingEmailDeliveryMethod

**Description**: Outgoing email delivery method for the user.<br />
**DisplayName**: Outgoing Email Delivery Method<br />
**LogicalName**: outgoingemaildeliverymethod<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 0 **Label**: None
- **Value**: 1 **Label**: Microsoft Dynamics 365 for Outlook
- **Value**: 2 **Label**: Server-Side Synchronization or Email Router



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


### <a name="BKMK_ParentSystemUserId"></a> ParentSystemUserId

**Description**: Unique identifier of the manager of the user.<br />
**DisplayName**: Manager<br />
**LogicalName**: parentsystemuserid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: systemuser


### <a name="BKMK_PassportHi"></a> PassportHi

**Description**: For internal use only.<br />
**DisplayName**: Passport Hi<br />
**LogicalName**: passporthi<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_PassportLo"></a> PassportLo

**Description**: For internal use only.<br />
**DisplayName**: Passport Lo<br />
**LogicalName**: passportlo<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_PersonalEMailAddress"></a> PersonalEMailAddress

**Description**: Personal email address of the user.<br />
**DisplayName**: Email 2<br />
**LogicalName**: personalemailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PhotoUrl"></a> PhotoUrl

**Description**: URL for the Website on which a photo of the user is located.<br />
**DisplayName**: Photo URL<br />
**LogicalName**: photourl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_PositionId"></a> PositionId

**Description**: User's position in hierarchical security model.<br />
**DisplayName**: Position<br />
**LogicalName**: positionid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: position


### <a name="BKMK_PreferredAddressCode"></a> PreferredAddressCode

**Description**: Preferred address for the user.<br />
**DisplayName**: Preferred Address<br />
**LogicalName**: preferredaddresscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Mailing Address
- **Value**: 2 **Label**: Other Address



### <a name="BKMK_PreferredEmailCode"></a> PreferredEmailCode

**Description**: Preferred email address for the user.<br />
**DisplayName**: Preferred Email<br />
**LogicalName**: preferredemailcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_PreferredPhoneCode"></a> PreferredPhoneCode

**Description**: Preferred phone number for the user.<br />
**DisplayName**: Preferred Phone<br />
**LogicalName**: preferredphonecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Main Phone
- **Value**: 2 **Label**: Other Phone
- **Value**: 3 **Label**: Home Phone
- **Value**: 4 **Label**: Mobile Phone



### <a name="BKMK_ProcessId"></a> ProcessId

**Description**: Shows the ID of the process.<br />
**DisplayName**: Process<br />
**LogicalName**: processid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_QueueId"></a> QueueId

**Description**: Unique identifier of the default queue for the user.<br />
**DisplayName**: Default Queue<br />
**LogicalName**: queueid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: queue


### <a name="BKMK_Salutation"></a> Salutation

**Description**: Salutation for correspondence with the user.<br />
**DisplayName**: Salutation<br />
**LogicalName**: salutation<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_SetupUser"></a> SetupUser

**Description**: Check if user is a setup user.<br />
**DisplayName**: Restricted Access Mode<br />
**LogicalName**: setupuser<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_SharePointEmailAddress"></a> SharePointEmailAddress

**Description**: SharePoint Work Email Address<br />
**DisplayName**: SharePoint Email Address<br />
**LogicalName**: sharepointemailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_Skills"></a> Skills

**Description**: Skill set of the user.<br />
**DisplayName**: Skills<br />
**LogicalName**: skills<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_StageId"></a> StageId

**Description**: Shows the ID of the stage.<br />
**DisplayName**: Process Stage<br />
**LogicalName**: stageid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_SystemUserId"></a> SystemUserId

**Description**: Unique identifier for the user.<br />
**DisplayName**: User<br />
**LogicalName**: systemuserid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_TerritoryId"></a> TerritoryId

**Added by**: Application Common Solution<br />
**Description**: Unique identifier of the territory to which the user is assigned.<br />
**DisplayName**: Territory<br />
**LogicalName**: territoryid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: territory


### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

**Description**: For internal use only.<br />
**DisplayName**: Time Zone Rule Version Number<br />
**LogicalName**: timezoneruleversionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_Title"></a> Title

**Description**: Title of the user.<br />
**DisplayName**: Title<br />
**LogicalName**: title<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the systemuser.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


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


### <a name="BKMK_UserLicenseType"></a> UserLicenseType

**Description**: Shows the type of user license.<br />
**DisplayName**: User License Type<br />
**LogicalName**: userlicensetype<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

**Description**: Time zone code that was in use when the record was created.<br />
**DisplayName**: UTC Conversion Time Zone Code<br />
**LogicalName**: utcconversiontimezonecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -1


### <a name="BKMK_WindowsLiveID"></a> WindowsLiveID

**Description**: Windows Live ID<br />
**DisplayName**: Windows Live ID<br />
**LogicalName**: windowsliveid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_YammerEmailAddress"></a> YammerEmailAddress

**Description**: User's Yammer login email address<br />
**DisplayName**: Yammer Email<br />
**LogicalName**: yammeremailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_YammerUserId"></a> YammerUserId

**Description**: User's Yammer ID<br />
**DisplayName**: Yammer User ID<br />
**LogicalName**: yammeruserid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 128


### <a name="BKMK_YomiFirstName"></a> YomiFirstName

**Description**: Pronunciation of the first name of the user, written in phonetic hiragana or katakana characters.<br />
**DisplayName**: Yomi First Name<br />
**LogicalName**: yomifirstname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: PhoneticGuide<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_YomiLastName"></a> YomiLastName

**Description**: Pronunciation of the last name of the user, written in phonetic hiragana or katakana characters.<br />
**DisplayName**: Yomi Last Name<br />
**LogicalName**: yomilastname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: PhoneticGuide<br />
**IsLocalizable**: False<br />
**MaxLength**: 64


### <a name="BKMK_YomiMiddleName"></a> YomiMiddleName

**Description**: Pronunciation of the middle name of the user, written in phonetic hiragana or katakana characters.<br />
**DisplayName**: Yomi Middle Name<br />
**LogicalName**: yomimiddlename<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: PhoneticGuide<br />
**IsLocalizable**: False<br />
**MaxLength**: 50

<a name="read-only-attributes"></a>
## Read-only attributes
These attributes return false for both **IsValidForCreate** or **IsValidForUpdate**. Listed by **SchemaName**.

- [ActiveDirectoryGuid](#BKMK_ActiveDirectoryGuid)
- [Address1_Composite](#BKMK_Address1_Composite)
- [Address2_Composite](#BKMK_Address2_Composite)
- [ApplicationIdUri](#BKMK_ApplicationIdUri)
- [AzureActiveDirectoryObjectId](#BKMK_AzureActiveDirectoryObjectId)
- [BusinessUnitIdName](#BKMK_BusinessUnitIdName)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedByName](#BKMK_CreatedByName)
- [CreatedByYomiName](#BKMK_CreatedByYomiName)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [CreatedOnBehalfByName](#BKMK_CreatedOnBehalfByName)
- [CreatedOnBehalfByYomiName](#BKMK_CreatedOnBehalfByYomiName)
- [DefaultFiltersPopulated](#BKMK_DefaultFiltersPopulated)
- [DefaultMailbox](#BKMK_DefaultMailbox)
- [DefaultMailboxName](#BKMK_DefaultMailboxName)
- [DefaultOdbFolderName](#BKMK_DefaultOdbFolderName)
- [DisabledReason](#BKMK_DisabledReason)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [ExchangeRate](#BKMK_ExchangeRate)
- [FullName](#BKMK_FullName)
- [IdentityId](#BKMK_IdentityId)
- [IsActiveDirectoryUser](#BKMK_IsActiveDirectoryUser)
- [IsEmailAddressApprovedByO365Admin](#BKMK_IsEmailAddressApprovedByO365Admin)
- [LatestUpdateTime](#BKMK_LatestUpdateTime)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [ParentSystemUserIdName](#BKMK_ParentSystemUserIdName)
- [ParentSystemUserIdYomiName](#BKMK_ParentSystemUserIdYomiName)
- [PositionIdName](#BKMK_PositionIdName)
- [QueueIdName](#BKMK_QueueIdName)
- [TerritoryIdName](#BKMK_TerritoryIdName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [UserPuid](#BKMK_UserPuid)
- [VersionNumber](#BKMK_VersionNumber)
- [YomiFullName](#BKMK_YomiFullName)


### <a name="BKMK_ActiveDirectoryGuid"></a> ActiveDirectoryGuid

**Description**: Active Directory object GUID for the system user.<br />
**DisplayName**: Active Directory Guid<br />
**LogicalName**: activedirectoryguid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_Address1_Composite"></a> Address1_Composite

**Description**: Shows the complete primary address.<br />
**DisplayName**: Address<br />
**LogicalName**: address1_composite<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_Address2_Composite"></a> Address2_Composite

**Description**: Shows the complete secondary address.<br />
**DisplayName**: Other Address<br />
**LogicalName**: address2_composite<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1000


### <a name="BKMK_ApplicationIdUri"></a> ApplicationIdUri

**Description**: The URI used as a unique logical identifier for the external app. This can be used to validate the application.<br />
**DisplayName**: Application ID URI<br />
**LogicalName**: applicationiduri<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 1024


### <a name="BKMK_AzureActiveDirectoryObjectId"></a> AzureActiveDirectoryObjectId

**Description**: This is the application directory object Id.<br />
**DisplayName**: Azure AD Object ID<br />
**LogicalName**: azureactivedirectoryobjectid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_BusinessUnitIdName"></a> BusinessUnitIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: businessunitidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the user.<br />
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

**Description**: Date and time when the user was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the systemuser.<br />
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


### <a name="BKMK_DefaultFiltersPopulated"></a> DefaultFiltersPopulated

**Description**: Indicates if default outlook filters have been populated.<br />
**DisplayName**: Default Filters Populated<br />
**LogicalName**: defaultfilterspopulated<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_DefaultMailbox"></a> DefaultMailbox

**Description**: Select the mailbox associated with this user.<br />
**DisplayName**: Mailbox<br />
**LogicalName**: defaultmailbox<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: mailbox


### <a name="BKMK_DefaultMailboxName"></a> DefaultMailboxName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: defaultmailboxname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_DefaultOdbFolderName"></a> DefaultOdbFolderName

**Description**: Type a default folder name for the user's OneDrive For Business location.<br />
**DisplayName**: Default OneDrive for Business Folder Name<br />
**LogicalName**: defaultodbfoldername<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_DisabledReason"></a> DisabledReason

**Description**: Reason for disabling the user.<br />
**DisplayName**: Disabled Reason<br />
**LogicalName**: disabledreason<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


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

**Description**: Exchange rate for the currency associated with the systemuser with respect to the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_FullName"></a> FullName

**Description**: Full name of the user.<br />
**DisplayName**: Full Name<br />
**LogicalName**: fullname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_IdentityId"></a> IdentityId

**Description**: For internal use only.<br />
**DisplayName**: Unique user identity id<br />
**LogicalName**: identityid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 2147483647<br />
**MinValue**: -2147483648


### <a name="BKMK_IsActiveDirectoryUser"></a> IsActiveDirectoryUser

**Description**: Information about whether the user is an AD user.<br />
**DisplayName**: Is Active Directory User<br />
**LogicalName**: isactivedirectoryuser<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: True


### <a name="BKMK_IsEmailAddressApprovedByO365Admin"></a> IsEmailAddressApprovedByO365Admin

**Description**: Shows the status of approval of the email address by O365 Admin.<br />
**DisplayName**: Email Address O365 Admin Approval Status<br />
**LogicalName**: isemailaddressapprovedbyo365admin<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_LatestUpdateTime"></a> LatestUpdateTime

**Description**: Time stamp of the latest update for the user<br />
**DisplayName**: Latest User Update Time<br />
**LogicalName**: latestupdatetime<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the user.<br />
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

**Description**: Date and time when the user was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the systemuser.<br />
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


### <a name="BKMK_OrganizationId"></a> OrganizationId

**Description**: Unique identifier of the organization associated with the user.<br />
**DisplayName**: Organization <br />
**LogicalName**: organizationid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Uniqueidentifier<br />


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


### <a name="BKMK_ParentSystemUserIdName"></a> ParentSystemUserIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentsystemuseridname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_ParentSystemUserIdYomiName"></a> ParentSystemUserIdYomiName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentsystemuseridyominame<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_PositionIdName"></a> PositionIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: positionidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_QueueIdName"></a> QueueIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: queueidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 400


### <a name="BKMK_TerritoryIdName"></a> TerritoryIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: territoryidname<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


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


### <a name="BKMK_UserPuid"></a> UserPuid

**Description**:  User PUID User Identifiable Information<br />
**DisplayName**: User PUID<br />
**LogicalName**: userpuid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the user.<br />
**DisplayName**: Version number<br />
**LogicalName**: versionnumber<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: BigInt<br />
**MaxValue**: 9223372036854775807<br />
**MinValue**: -9223372036854775808<br />


### <a name="BKMK_YomiFullName"></a> YomiFullName

**Description**: Pronunciation of the full name of the user, written in phonetic hiragana or katakana characters.<br />
**DisplayName**: Yomi Full Name<br />
**LogicalName**: yomifullname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: PhoneticGuide<br />
**IsLocalizable**: False<br />
**MaxLength**: 200

<a name="onetomany"></a>

## One-To-Many Relationships

Listed by **SchemaName**.

- [lk_appmodule_modifiedby](#BKMK_lk_appmodule_modifiedby)
- [lk_territorybase_createdby](#BKMK_lk_territorybase_createdby)
- [lk_territory_createdonbehalfby](#BKMK_lk_territory_createdonbehalfby)
- [lk_territorybase_modifiedby](#BKMK_lk_territorybase_modifiedby)
- [lk_territory_modifiedonbehalfby](#BKMK_lk_territory_modifiedonbehalfby)
- [system_user_territories](#BKMK_system_user_territories)
- [systemuser_principalobjectattributeaccess_principalid](#BKMK_systemuser_principalobjectattributeaccess_principalid)
- [user_exchangesyncidmapping](#BKMK_user_exchangesyncidmapping)
- [lk_theme_createdby](#BKMK_lk_theme_createdby)
- [lk_theme_createdonbehalfby](#BKMK_lk_theme_createdonbehalfby)
- [lk_theme_modifiedby](#BKMK_lk_theme_modifiedby)
- [lk_theme_modifiedonbehalfby](#BKMK_lk_theme_modifiedonbehalfby)
- [lk_usermapping_createdby](#BKMK_lk_usermapping_createdby)
- [lk_usermapping_createdonbehalfby](#BKMK_lk_usermapping_createdonbehalfby)
- [lk_usermapping_modifiedby](#BKMK_lk_usermapping_modifiedby)
- [lk_usermapping_modifiedonbehalfby](#BKMK_lk_usermapping_modifiedonbehalfby)
- [lk_interactionforemail_createdby](#BKMK_lk_interactionforemail_createdby)
- [lk_interactionforemail_createdonbehalfby](#BKMK_lk_interactionforemail_createdonbehalfby)
- [lk_interactionforemail_modifiedby](#BKMK_lk_interactionforemail_modifiedby)
- [lk_interactionforemail_modifiedonbehalfby](#BKMK_lk_interactionforemail_modifiedonbehalfby)
- [user_interactionforemail](#BKMK_user_interactionforemail)
- [lk_knowledgearticle_createdby](#BKMK_lk_knowledgearticle_createdby)
- [lk_knowledgearticle_createdonbehalfby](#BKMK_lk_knowledgearticle_createdonbehalfby)
- [lk_knowledgearticle_modifiedby](#BKMK_lk_knowledgearticle_modifiedby)
- [lk_knowledgearticle_modifiedonbehalfby](#BKMK_lk_knowledgearticle_modifiedonbehalfby)
- [user_knowledgearticle](#BKMK_user_knowledgearticle)
- [user_sharepointsite](#BKMK_user_sharepointsite)
- [user_sharepointdocumentlocation](#BKMK_user_sharepointdocumentlocation)
- [lk_suggestioncardtemplate_createdby](#BKMK_lk_suggestioncardtemplate_createdby)
- [lk_suggestioncardtemplate_createdonbehalfby](#BKMK_lk_suggestioncardtemplate_createdonbehalfby)
- [lk_suggestioncardtemplate_modifiedby](#BKMK_lk_suggestioncardtemplate_modifiedby)
- [lk_suggestioncardtemplate_modifiedonbehalfby](#BKMK_lk_suggestioncardtemplate_modifiedonbehalfby)
- [lk_goal_createdby](#BKMK_lk_goal_createdby)
- [lk_goal_createdonbehalfby](#BKMK_lk_goal_createdonbehalfby)
- [lk_goal_modifiedby](#BKMK_lk_goal_modifiedby)
- [lk_goal_modifiedonbehalfby](#BKMK_lk_goal_modifiedonbehalfby)
- [user_goal](#BKMK_user_goal)
- [user_goal_goalowner](#BKMK_user_goal_goalowner)
- [lk_metric_createdby](#BKMK_lk_metric_createdby)
- [lk_metric_createdonbehalfby](#BKMK_lk_metric_createdonbehalfby)
- [lk_metric_modifiedby](#BKMK_lk_metric_modifiedby)
- [lk_metric_modifiedonbehalfby](#BKMK_lk_metric_modifiedonbehalfby)
- [lk_rollupfield_createdby](#BKMK_lk_rollupfield_createdby)
- [lk_rollupfield_createdonbehalfby](#BKMK_lk_rollupfield_createdonbehalfby)
- [lk_rollupfield_modifiedby](#BKMK_lk_rollupfield_modifiedby)
- [lk_rollupfield_modifiedonbehalfby](#BKMK_lk_rollupfield_modifiedonbehalfby)
- [lk_goalrollupquery_createdby](#BKMK_lk_goalrollupquery_createdby)
- [lk_goalrollupquery_createdonbehalfby](#BKMK_lk_goalrollupquery_createdonbehalfby)
- [lk_goalrollupquery_modifiedby](#BKMK_lk_goalrollupquery_modifiedby)
- [lk_goalrollupquery_modifiedonbehalfby](#BKMK_lk_goalrollupquery_modifiedonbehalfby)
- [lk_emailserverprofile_createdonbehalfby](#BKMK_lk_emailserverprofile_createdonbehalfby)
- [lk_emailserverprofile_modifiedonbehalfby](#BKMK_lk_emailserverprofile_modifiedonbehalfby)
- [lk_mailbox_createdby](#BKMK_lk_mailbox_createdby)
- [lk_mailbox_createdonbehalfby](#BKMK_lk_mailbox_createdonbehalfby)
- [lk_mailbox_modifiedby](#BKMK_lk_mailbox_modifiedby)
- [lk_mailbox_modifiedonbehalfby](#BKMK_lk_mailbox_modifiedonbehalfby)
- [user_mailbox](#BKMK_user_mailbox)
- [mailbox_regarding_systemuser](#BKMK_mailbox_regarding_systemuser)
- [lk_post_modifiedonbehalfby](#BKMK_lk_post_modifiedonbehalfby)
- [lk_position_createdby](#BKMK_lk_position_createdby)
- [lk_position_createdonbehalfby](#BKMK_lk_position_createdonbehalfby)
- [lk_position_modifiedby](#BKMK_lk_position_modifiedby)
- [lk_position_modifiedonbehalfby](#BKMK_lk_position_modifiedonbehalfby)
- [lk_cardtype_createdby](#BKMK_lk_cardtype_createdby)
- [lk_cardtype_createdonbehalfby](#BKMK_lk_cardtype_createdonbehalfby)
- [lk_cardtype_modifiedby](#BKMK_lk_cardtype_modifiedby)
- [lk_cardtype_modifiedonbehalfby](#BKMK_lk_cardtype_modifiedonbehalfby)
- [lk_channelaccessprofile_createdby](#BKMK_lk_channelaccessprofile_createdby)
- [lk_channelaccessprofile_createdonbehalfby](#BKMK_lk_channelaccessprofile_createdonbehalfby)
- [lk_channelaccessprofile_modifiedby](#BKMK_lk_channelaccessprofile_modifiedby)
- [lk_channelaccessprofile_modifiedonbehalfby](#BKMK_lk_channelaccessprofile_modifiedonbehalfby)
- [user_channelaccessprofile](#BKMK_user_channelaccessprofile)
- [lk_externalparty_createdby](#BKMK_lk_externalparty_createdby)
- [lk_externalparty_createdonbehalfby](#BKMK_lk_externalparty_createdonbehalfby)
- [lk_externalparty_modifiedby](#BKMK_lk_externalparty_modifiedby)
- [lk_externalparty_modifiedonbehalfby](#BKMK_lk_externalparty_modifiedonbehalfby)
- [user_externalparty](#BKMK_user_externalparty)
- [lk_solution_createdby](#BKMK_lk_solution_createdby)
- [lk_solution_modifiedby](#BKMK_lk_solution_modifiedby)
- [lk_publisher_createdby](#BKMK_lk_publisher_createdby)
- [lk_publisher_modifiedby](#BKMK_lk_publisher_modifiedby)
- [lk_officegraphdocument_createdonbehalfby](#BKMK_lk_officegraphdocument_createdonbehalfby)
- [lk_officegraphdocument_modifiedonbehalfby](#BKMK_lk_officegraphdocument_modifiedonbehalfby)
- [lk_profilerule_createdby](#BKMK_lk_profilerule_createdby)
- [lk_profilerule_createdonbehalfby](#BKMK_lk_profilerule_createdonbehalfby)
- [lk_profilerule_modifiedby](#BKMK_lk_profilerule_modifiedby)
- [lk_profilerule_modifiedonbehalfby](#BKMK_lk_profilerule_modifiedonbehalfby)
- [user_profilerule](#BKMK_user_profilerule)
- [lk_profileruleitem_createdby](#BKMK_lk_profileruleitem_createdby)
- [lk_profileruleitem_createdonbehalfby](#BKMK_lk_profileruleitem_createdonbehalfby)
- [lk_profileruleitem_modifiedby](#BKMK_lk_profileruleitem_modifiedby)
- [lk_profileruleitem_modifiedonbehalfby](#BKMK_lk_profileruleitem_modifiedonbehalfby)
- [lk_delveactionhub_createdby](#BKMK_lk_delveactionhub_createdby)
- [lk_delveactionhub_createdonbehalfby](#BKMK_lk_delveactionhub_createdonbehalfby)
- [lk_delveactionhub_modifiedby](#BKMK_lk_delveactionhub_modifiedby)
- [lk_delveactionhub_modifiedonbehalfby](#BKMK_lk_delveactionhub_modifiedonbehalfby)
- [lk_recommendeddocument_createdby](#BKMK_lk_recommendeddocument_createdby)
- [lk_recommendeddocument_createdonbehalfby](#BKMK_lk_recommendeddocument_createdonbehalfby)
- [lk_recommendeddocument_modifiedby](#BKMK_lk_recommendeddocument_modifiedby)
- [lk_recommendeddocument_modifiedonbehalfby](#BKMK_lk_recommendeddocument_modifiedonbehalfby)
- [lk_KnowledgeBaseRecord_createdby](#BKMK_lk_KnowledgeBaseRecord_createdby)
- [lk_KnowledgeBaseRecord_createdonbehalfby](#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby)
- [lk_KnowledgeBaseRecord_modifiedby](#BKMK_lk_KnowledgeBaseRecord_modifiedby)
- [lk_KnowledgeBaseRecord_modifiedonbehalfby](#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby)
- [lk_externalpartyitem_createdonbehalfby](#BKMK_lk_externalpartyitem_createdonbehalfby)
- [lk_lookupmapping_modifiedby](#BKMK_lk_lookupmapping_modifiedby)
- [lk_relationshiprole_createdonbehalfby](#BKMK_lk_relationshiprole_createdonbehalfby)
- [lk_usersettings_createdonbehalfby](#BKMK_lk_usersettings_createdonbehalfby)
- [lk_kbarticletemplatebase_modifiedby](#BKMK_lk_kbarticletemplatebase_modifiedby)
- [lk_fax_modifiedby](#BKMK_lk_fax_modifiedby)
- [lk_processsession_completedby](#BKMK_lk_processsession_completedby)
- [modifiedby_sdkmessageprocessingstepsecureconfig](#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig)
- [lk_businessunit_createdonbehalfby](#BKMK_lk_businessunit_createdonbehalfby)
- [lk_duplicaterule_createdonbehalfby](#BKMK_lk_duplicaterule_createdonbehalfby)
- [lk_sdkmessagepair_createdonbehalfby](#BKMK_lk_sdkmessagepair_createdonbehalfby)
- [lk_sdkmessage_modifiedonbehalfby](#BKMK_lk_sdkmessage_modifiedonbehalfby)
- [lk_translationprocess_modifiedonbehalfby](#BKMK_lk_translationprocess_modifiedonbehalfby)
- [lk_actioncardbase_createdonbehalfby](#BKMK_lk_actioncardbase_createdonbehalfby)
- [lk_sdkmessagefilter_createdonbehalfby](#BKMK_lk_sdkmessagefilter_createdonbehalfby)
- [lk_slabase_modifiedonbehalfby](#BKMK_lk_slabase_modifiedonbehalfby)
- [lk_feedback_modifiedby](#BKMK_lk_feedback_modifiedby)
- [lk_templatebase_modifiedby](#BKMK_lk_templatebase_modifiedby)
- [createdby_relationship_role_map](#BKMK_createdby_relationship_role_map)
- [lk_azureserviceconnection_modifiedonbehalfby](#BKMK_lk_azureserviceconnection_modifiedonbehalfby)
- [lk_kbarticletemplate_modifiedonbehalfby](#BKMK_lk_kbarticletemplate_modifiedonbehalfby)
- [lk_slakpiinstancebase_createdby](#BKMK_lk_slakpiinstancebase_createdby)
- [lk_convertruleitembase_createdby](#BKMK_lk_convertruleitembase_createdby)
- [lk_ChannelProperty_modifiedby](#BKMK_lk_ChannelProperty_modifiedby)
- [lk_ACIViewMapper_createdby](#BKMK_lk_ACIViewMapper_createdby)
- [lk_azureserviceconnection_createdonbehalfby](#BKMK_lk_azureserviceconnection_createdonbehalfby)
- [lk_ChannelPropertyGroup_modifiedonbehalfby](#BKMK_lk_ChannelPropertyGroup_modifiedonbehalfby)
- [lk_userqueryvisualization_modifiedby](#BKMK_lk_userqueryvisualization_modifiedby)
- [lk_recurringappointmentmaster_createdonbehalfby](#BKMK_lk_recurringappointmentmaster_createdonbehalfby)
- [lk_businessprocessflowinstancebase_createdonbehalfby](#BKMK_lk_businessprocessflowinstancebase_createdonbehalfby)
- [lk_lookupmapping_createdonbehalfby](#BKMK_lk_lookupmapping_createdonbehalfby)
- [lk_MobileOfflineProfileItem_createdby](#BKMK_lk_MobileOfflineProfileItem_createdby)
- [lk_sdkmessageresponsefield_createdonbehalfby](#BKMK_lk_sdkmessageresponsefield_createdonbehalfby)
- [lk_recurringappointmentmaster_modifiedby](#BKMK_lk_recurringappointmentmaster_modifiedby)
- [lk_fax_createdby](#BKMK_lk_fax_createdby)
- [lk_ConvertRule_createdonbehalfby](#BKMK_lk_ConvertRule_createdonbehalfby)
- [lk_letter_modifiedonbehalfby](#BKMK_lk_letter_modifiedonbehalfby)
- [lk_transformationmapping_createdby](#BKMK_lk_transformationmapping_createdby)
- [lk_entitymap_modifiedonbehalfby](#BKMK_lk_entitymap_modifiedonbehalfby)
- [lk_reportcategorybase_createdby](#BKMK_lk_reportcategorybase_createdby)
- [lk_letter_createdby](#BKMK_lk_letter_createdby)
- [lk_customcontrolresource_modifiedby](#BKMK_lk_customcontrolresource_modifiedby)
- [lk_expiredprocess_createdonbehalfby](#BKMK_lk_expiredprocess_createdonbehalfby)
- [actioncardusersettings_owning_user](#BKMK_actioncardusersettings_owning_user)
- [createdby_customer_relationship](#BKMK_createdby_customer_relationship)
- [lk_reportentity_createdonbehalfby](#BKMK_lk_reportentity_createdonbehalfby)
- [lk_routingrule_createdby](#BKMK_lk_routingrule_createdby)
- [workflow_dependency_createdby](#BKMK_workflow_dependency_createdby)
- [lk_appmodulecomponent_modifiedby](#BKMK_lk_appmodulecomponent_modifiedby)
- [lk_calendar_modifiedby](#BKMK_lk_calendar_modifiedby)
- [lk_RoutingRuleItem_createdby](#BKMK_lk_RoutingRuleItem_createdby)
- [SystemUser_DuplicateRules](#BKMK_SystemUser_DuplicateRules)
- [lk_plugintype_createdonbehalfby](#BKMK_lk_plugintype_createdonbehalfby)
- [lk_routingrule_modifiedby](#BKMK_lk_routingrule_modifiedby)
- [lk_mobileofflineprofileitem_createdonbehalfby](#BKMK_lk_mobileofflineprofileitem_createdonbehalfby)
- [lk_fax_createdonbehalfby](#BKMK_lk_fax_createdonbehalfby)
- [lk_timezonedefinition_modifiedby](#BKMK_lk_timezonedefinition_modifiedby)
- [lk_reportvisibilitybase_modifiedby](#BKMK_lk_reportvisibilitybase_modifiedby)
- [lk_columnmapping_createdby](#BKMK_lk_columnmapping_createdby)
- [lk_reportcategorybase_modifiedby](#BKMK_lk_reportcategorybase_modifiedby)
- [lk_sharepointsitebase_createdonbehalfby](#BKMK_lk_sharepointsitebase_createdonbehalfby)
- [lk_workflowlog_modifiedby](#BKMK_lk_workflowlog_modifiedby)
- [lk_syncerrorbase_createdonbehalfby](#BKMK_lk_syncerrorbase_createdonbehalfby)
- [lk_bulkdeleteoperation_modifiedonbehalfby](#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby)
- [lk_serviceendpointbase_createdonbehalfby](#BKMK_lk_serviceendpointbase_createdonbehalfby)
- [lk_solutioncomponentbase_createdonbehalfby](#BKMK_lk_solutioncomponentbase_createdonbehalfby)
- [lk_plugintype_modifiedonbehalfby](#BKMK_lk_plugintype_modifiedonbehalfby)
- [lk_lookupmapping_modifiedonbehalfby](#BKMK_lk_lookupmapping_modifiedonbehalfby)
- [lk_phonecall_modifiedby](#BKMK_lk_phonecall_modifiedby)
- [lk_slabase_modifiedby](#BKMK_lk_slabase_modifiedby)
- [lk_workflowlog_modifiedonbehalfby](#BKMK_lk_workflowlog_modifiedonbehalfby)
- [lk_importfilebase_createdonbehalfby](#BKMK_lk_importfilebase_createdonbehalfby)
- [lk_fieldsecurityprofile_createdonbehalfby](#BKMK_lk_fieldsecurityprofile_createdonbehalfby)
- [lk_importmapbase_createdby](#BKMK_lk_importmapbase_createdby)
- [createdby_relationship_role](#BKMK_createdby_relationship_role)
- [lk_PostFollow_createdby](#BKMK_lk_PostFollow_createdby)
- [systemuser_PostFollows](#BKMK_systemuser_PostFollows)
- [lk_post_createdby](#BKMK_lk_post_createdby)
- [lk_post_createdonbehalfby](#BKMK_lk_post_createdonbehalfby)
- [lk_post_modifiedby](#BKMK_lk_post_modifiedby)
- [lk_postcomment_createdby](#BKMK_lk_postcomment_createdby)
- [user_owner_postfollows](#BKMK_user_owner_postfollows)
- [lk_postfollow_createdonbehalfby](#BKMK_lk_postfollow_createdonbehalfby)
- [lk_postcomment_createdonbehalfby](#BKMK_lk_postcomment_createdonbehalfby)
- [lk_postlike_createdonbehalfby](#BKMK_lk_postlike_createdonbehalfby)
- [lk_postlike_createdby](#BKMK_lk_postlike_createdby)
- [lk_queueitem_modifiedonbehalfby](#BKMK_lk_queueitem_modifiedonbehalfby)
- [user_socialactivity](#BKMK_user_socialactivity)
- [lk_translationprocess_createdonbehalfby](#BKMK_lk_translationprocess_createdonbehalfby)
- [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby)
- [lk_feedback_modifiedonbehalfby](#BKMK_lk_feedback_modifiedonbehalfby)
- [lk_workflowlog_createdonbehalfby](#BKMK_lk_workflowlog_createdonbehalfby)
- [lk_role_createdonbehalfby](#BKMK_lk_role_createdonbehalfby)
- [lk_transactioncurrency_modifiedonbehalfby](#BKMK_lk_transactioncurrency_modifiedonbehalfby)
- [lk_rolebase_modifiedby](#BKMK_lk_rolebase_modifiedby)
- [lk_navigationsetting_createdby](#BKMK_lk_navigationsetting_createdby)
- [lk_subject_modifiedonbehalfby](#BKMK_lk_subject_modifiedonbehalfby)
- [lk_duplicaterule_modifiedonbehalfby](#BKMK_lk_duplicaterule_modifiedonbehalfby)
- [lk_task_modifiedonbehalfby](#BKMK_lk_task_modifiedonbehalfby)
- [lk_subjectbase_modifiedby](#BKMK_lk_subjectbase_modifiedby)
- [lk_relationshiprole_modifiedonbehalfby](#BKMK_lk_relationshiprole_modifiedonbehalfby)
- [lk_mailboxtrackingfolder_modifiedby](#BKMK_lk_mailboxtrackingfolder_modifiedby)
- [lk_sdkmessageresponsefield_modifiedonbehalfby](#BKMK_lk_sdkmessageresponsefield_modifiedonbehalfby)
- [modifiedby_sdkmessageresponse](#BKMK_modifiedby_sdkmessageresponse)
- [impersonatinguserid_sdkmessageprocessingstep](#BKMK_impersonatinguserid_sdkmessageprocessingstep)
- [lk_kbarticle_createdonbehalfby](#BKMK_lk_kbarticle_createdonbehalfby)
- [lk_calendar_createdonbehalfby](#BKMK_lk_calendar_createdonbehalfby)
- [lk_businessunitnewsarticlebase_modifiedby](#BKMK_lk_businessunitnewsarticlebase_modifiedby)
- [createdby_expanderevent](#BKMK_createdby_expanderevent)
- [userentityinstancedata_systemuser](#BKMK_userentityinstancedata_systemuser)
- [user_userqueryvisualizations](#BKMK_user_userqueryvisualizations)
- [lk_tracelog_createdonbehalfby](#BKMK_lk_tracelog_createdonbehalfby)
- [lk_queueitembase_workerid](#BKMK_lk_queueitembase_workerid)
- [modifiedonbehalfby_attributemap](#BKMK_modifiedonbehalfby_attributemap)
- [lk_mobileofflineprofileitem_modifiedby](#BKMK_lk_mobileofflineprofileitem_modifiedby)
- [lk_customeraddressbase_modifiedby](#BKMK_lk_customeraddressbase_modifiedby)
- [lk_activitypointer_modifiedby](#BKMK_lk_activitypointer_modifiedby)
- [lk_customeraddressbase_createdby](#BKMK_lk_customeraddressbase_createdby)
- [createdby_sdkmessageresponse](#BKMK_createdby_sdkmessageresponse)
- [lk_syncerrorbase_modifiedonbehalfby](#BKMK_lk_syncerrorbase_modifiedonbehalfby)
- [SystemUser_BulkDeleteFailures](#BKMK_SystemUser_BulkDeleteFailures)
- [lk_teambase_modifiedby](#BKMK_lk_teambase_modifiedby)
- [workflow_createdby](#BKMK_workflow_createdby)
- [lk_queue_modifiedonbehalfby](#BKMK_lk_queue_modifiedonbehalfby)
- [lk_customeraddress_modifiedonbehalfby](#BKMK_lk_customeraddress_modifiedonbehalfby)
- [workflow_dependency_createdonbehalfby](#BKMK_workflow_dependency_createdonbehalfby)
- [modifiedby_sdkmessagepair](#BKMK_modifiedby_sdkmessagepair)
- [lk_emailsignaturebase_modifiedby](#BKMK_lk_emailsignaturebase_modifiedby)
- [lk_rolebase_createdby](#BKMK_lk_rolebase_createdby)
- [lk_reportcategory_modifiedonbehalfby](#BKMK_lk_reportcategory_modifiedonbehalfby)
- [lk_transformationmapping_modifiedby](#BKMK_lk_transformationmapping_modifiedby)
- [lk_duplicaterulecondition_modifiedonbehalfby](#BKMK_lk_duplicaterulecondition_modifiedonbehalfby)
- [lk_picklistmapping_createdby](#BKMK_lk_picklistmapping_createdby)
- [lk_savedqueryvisualizationbase_modifiedby](#BKMK_lk_savedqueryvisualizationbase_modifiedby)
- [lk_kbarticlecommentbase_modifiedby](#BKMK_lk_kbarticlecommentbase_modifiedby)
- [lk_email_modifiedonbehalfby](#BKMK_lk_email_modifiedonbehalfby)
- [createdby_entitymap](#BKMK_createdby_entitymap)
- [lk_asyncoperation_createdonbehalfby](#BKMK_lk_asyncoperation_createdonbehalfby)
- [lk_pluginassembly_modifiedonbehalfby](#BKMK_lk_pluginassembly_modifiedonbehalfby)
- [lk_team_createdonbehalfby](#BKMK_lk_team_createdonbehalfby)
- [createdby_connection](#BKMK_createdby_connection)
- [workflow_modifiedby](#BKMK_workflow_modifiedby)
- [lk_businessunitnewsarticle_createdonbehalfby](#BKMK_lk_businessunitnewsarticle_createdonbehalfby)
- [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby)
- [lk_processsessionbase_createdonbehalfby](#BKMK_lk_processsessionbase_createdonbehalfby)
- [lk_appmodule_modifiedonbehalfby](#BKMK_lk_appmodule_modifiedonbehalfby)
- [lk_customcontroldefaultconfig_modifiedonbehalfby](#BKMK_lk_customcontroldefaultconfig_modifiedonbehalfby)
- [lk_tracelog_modifiedby](#BKMK_lk_tracelog_modifiedby)
- [user_appointment](#BKMK_user_appointment)
- [lk_externalpartyitem_modifiedby](#BKMK_lk_externalpartyitem_modifiedby)
- [lk_appconfig_createdonbehalfby](#BKMK_lk_appconfig_createdonbehalfby)
- [lk_appconfiginstance_createdonbehalfby](#BKMK_lk_appconfiginstance_createdonbehalfby)
- [lk_DisplayStringbase_modifiedby](#BKMK_lk_DisplayStringbase_modifiedby)
- [lk_importlog_modifiedonbehalfby](#BKMK_lk_importlog_modifiedonbehalfby)
- [lk_navigationsetting_modifiedby](#BKMK_lk_navigationsetting_modifiedby)
- [SystemUser_Email_EmailSender](#BKMK_SystemUser_Email_EmailSender)
- [modifiedby_sdkmessagerequest](#BKMK_modifiedby_sdkmessagerequest)
- [user_activity](#BKMK_user_activity)
- [modifiedby_customer_relationship](#BKMK_modifiedby_customer_relationship)
- [lk_ConvertRule_modifiedby](#BKMK_lk_ConvertRule_modifiedby)
- [lk_monthlyfiscalcalendar_salespersonid](#BKMK_lk_monthlyfiscalcalendar_salespersonid)
- [SystemUser_ExternalPartyItems](#BKMK_SystemUser_ExternalPartyItems)
- [lk_businessunit_modifiedonbehalfby](#BKMK_lk_businessunit_modifiedonbehalfby)
- [lk_asyncoperation_modifiedonbehalfby](#BKMK_lk_asyncoperation_modifiedonbehalfby)
- [lk_teambase_createdby](#BKMK_lk_teambase_createdby)
- [lk_emailserverprofile_modifiedby](#BKMK_lk_emailserverprofile_modifiedby)
- [lk_processtriggerbase_modifiedonbehalfby](#BKMK_lk_processtriggerbase_modifiedonbehalfby)
- [lk_mailmergetemplate_modifiedonbehalfby](#BKMK_lk_mailmergetemplate_modifiedonbehalfby)
- [lk_connectionbase_modifiedonbehalfby](#BKMK_lk_connectionbase_modifiedonbehalfby)
- [lk_queueitem_createdonbehalfby](#BKMK_lk_queueitem_createdonbehalfby)
- [lk_teamtemplate_modifiedonbehalfby](#BKMK_lk_teamtemplate_modifiedonbehalfby)
- [lk_documenttemplatebase_modifiedby](#BKMK_lk_documenttemplatebase_modifiedby)
- [lk_transformationparametermapping_createdonbehalfby](#BKMK_lk_transformationparametermapping_createdonbehalfby)
- [lk_sharepointdocumentbase_modifiedonbehalfby](#BKMK_lk_sharepointdocumentbase_modifiedonbehalfby)
- [lk_relationshiprolemap_createdonbehalfby](#BKMK_lk_relationshiprolemap_createdonbehalfby)
- [user_userquery](#BKMK_user_userquery)
- [lk_appmodule_createdby](#BKMK_lk_appmodule_createdby)
- [lk_businessprocessflowinstancebase_createdby](#BKMK_lk_businessprocessflowinstancebase_createdby)
- [lk_kbarticlecommentbase_createdby](#BKMK_lk_kbarticlecommentbase_createdby)
- [lk_convertruleitembase_modifiedby](#BKMK_lk_convertruleitembase_modifiedby)
- [workflow_createdonbehalfby](#BKMK_workflow_createdonbehalfby)
- [lk_recurrencerule_modifiedby](#BKMK_lk_recurrencerule_modifiedby)
- [lk_category_modifiedonbehalfby](#BKMK_lk_category_modifiedonbehalfby)
- [lk_appconfig_modifiedby](#BKMK_lk_appconfig_modifiedby)
- [lk_bulkdeleteoperationbase_createdby](#BKMK_lk_bulkdeleteoperationbase_createdby)
- [lk_asyncoperation_createdby](#BKMK_lk_asyncoperation_createdby)
- [lk_sdkmessagefilter_modifiedonbehalfby](#BKMK_lk_sdkmessagefilter_modifiedonbehalfby)
- [user_recurringappointmentmaster](#BKMK_user_recurringappointmentmaster)
- [user_customer_relationship](#BKMK_user_customer_relationship)
- [lk_slaitembase_modifiedby](#BKMK_lk_slaitembase_modifiedby)
- [lk_publisheraddressbase_modifiedonbehalfby](#BKMK_lk_publisheraddressbase_modifiedonbehalfby)
- [lk_documenttemplatebase_createdby](#BKMK_lk_documenttemplatebase_createdby)
- [lk_transformationparametermapping_modifiedby](#BKMK_lk_transformationparametermapping_modifiedby)
- [lk_slabase_createdby](#BKMK_lk_slabase_createdby)
- [lk_organizationbase_createdby](#BKMK_lk_organizationbase_createdby)
- [lk_report_modifiedonbehalfby](#BKMK_lk_report_modifiedonbehalfby)
- [lk_quarterlyfiscalcalendar_modifiedby](#BKMK_lk_quarterlyfiscalcalendar_modifiedby)
- [createdby_serviceendpoint](#BKMK_createdby_serviceendpoint)
- [lk_knowledgesearchmodel_modifiedonbehalfby](#BKMK_lk_knowledgesearchmodel_modifiedonbehalfby)
- [lk_duplicaterulecondition_createdonbehalfby](#BKMK_lk_duplicaterulecondition_createdonbehalfby)
- [lk_routingruleitem_createdonbehalfby](#BKMK_lk_routingruleitem_createdonbehalfby)
- [lk_transactioncurrencybase_modifiedby](#BKMK_lk_transactioncurrencybase_modifiedby)
- [lk_DisplayStringbase_createdby](#BKMK_lk_DisplayStringbase_createdby)
- [lk_slaitembase_modifiedonbehalfby](#BKMK_lk_slaitembase_modifiedonbehalfby)
- [annotation_owning_user](#BKMK_annotation_owning_user)
- [system_user_contacts](#BKMK_system_user_contacts)
- [lk_transformationparametermapping_createdby](#BKMK_lk_transformationparametermapping_createdby)
- [lk_phonecall_createdonbehalfby](#BKMK_lk_phonecall_createdonbehalfby)
- [lk_email_modifiedby](#BKMK_lk_email_modifiedby)
- [lk_sharepointdocumentbase_createdonbehalfby](#BKMK_lk_sharepointdocumentbase_createdonbehalfby)
- [lk_usersettingsbase_createdby](#BKMK_lk_usersettingsbase_createdby)
- [lk_teamtemplate_createdonbehalfby](#BKMK_lk_teamtemplate_createdonbehalfby)
- [lk_appmodule_createdonbehalfby](#BKMK_lk_appmodule_createdonbehalfby)
- [lk_importlogbase_createdby](#BKMK_lk_importlogbase_createdby)
- [lk_sharepointdocumentlocationbase_createdby](#BKMK_lk_sharepointdocumentlocationbase_createdby)
- [lk_socialinsightsconfiguration_modifiedby](#BKMK_lk_socialinsightsconfiguration_modifiedby)
- [user_accounts](#BKMK_user_accounts)
- [lk_externalpartyitem_modifiedonbehalfby](#BKMK_lk_externalpartyitem_modifiedonbehalfby)
- [lk_reportentitybase_modifiedby](#BKMK_lk_reportentitybase_modifiedby)
- [lk_sdkmessagepair_modifiedonbehalfby](#BKMK_lk_sdkmessagepair_modifiedonbehalfby)
- [user_settings](#BKMK_user_settings)
- [modifiedby_plugintype](#BKMK_modifiedby_plugintype)
- [lk_importentitymapping_modifiedonbehalfby](#BKMK_lk_importentitymapping_modifiedonbehalfby)
- [lk_savedquerybase_createdby](#BKMK_lk_savedquerybase_createdby)
- [lk_offlinecommanddefinition_createdby](#BKMK_lk_offlinecommanddefinition_createdby)
- [lk_activitypointer_createdby](#BKMK_lk_activitypointer_createdby)
- [lk_columnmapping_createdonbehalfby](#BKMK_lk_columnmapping_createdonbehalfby)
- [modifiedby_relationship_role](#BKMK_modifiedby_relationship_role)
- [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby)
- [lk_subject_createdonbehalfby](#BKMK_lk_subject_createdonbehalfby)
- [lk_appconfigmaster_createdonbehalfby](#BKMK_lk_appconfigmaster_createdonbehalfby)
- [lk_ChannelProperty_createdby](#BKMK_lk_ChannelProperty_createdby)
- [lk_kbarticle_modifiedonbehalfby](#BKMK_lk_kbarticle_modifiedonbehalfby)
- [modifiedby_entitymap](#BKMK_modifiedby_entitymap)
- [createdby_sdkmessageprocessingstepsecureconfig](#BKMK_createdby_sdkmessageprocessingstepsecureconfig)
- [createdby_sdkmessageprocessingstep](#BKMK_createdby_sdkmessageprocessingstep)
- [lk_appconfig_modifiedonbehalfby](#BKMK_lk_appconfig_modifiedonbehalfby)
- [lk_quarterlyfiscalcalendar_salespersonid](#BKMK_lk_quarterlyfiscalcalendar_salespersonid)
- [lk_transformationparametermapping_modifiedonbehalfby](#BKMK_lk_transformationparametermapping_modifiedonbehalfby)
- [lk_importentitymapping_createdonbehalfby](#BKMK_lk_importentitymapping_createdonbehalfby)
- [SystemUser_ProcessSessions](#BKMK_SystemUser_ProcessSessions)
- [lk_templatebase_createdonbehalfby](#BKMK_lk_templatebase_createdonbehalfby)
- [lk_lookupmapping_createdby](#BKMK_lk_lookupmapping_createdby)
- [lk_mobileofflineprofileitem_modifiedonbehalfby](#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby)
- [lk_processsessionbase_modifiedonbehalfby](#BKMK_lk_processsessionbase_modifiedonbehalfby)
- [lk_processsession_createdby](#BKMK_lk_processsession_createdby)
- [lk_personaldocumenttemplatebase_createdby](#BKMK_lk_personaldocumenttemplatebase_createdby)
- [lk_publisherbase_modifiedonbehalfby](#BKMK_lk_publisherbase_modifiedonbehalfby)
- [lk_MobileOfflineProfile_createdonbehalfby](#BKMK_lk_MobileOfflineProfile_createdonbehalfby)
- [lk_timezonerule_createdby](#BKMK_lk_timezonerule_createdby)
- [lk_contactbase_createdby](#BKMK_lk_contactbase_createdby)
- [lk_slakpiinstancebase_createdonbehalfby](#BKMK_lk_slakpiinstancebase_createdonbehalfby)
- [system_user_workflow](#BKMK_system_user_workflow)
- [lk_duplicaterulebase_createdby](#BKMK_lk_duplicaterulebase_createdby)
- [lk_appointment_createdonbehalfby](#BKMK_lk_appointment_createdonbehalfby)
- [createdby_connection_role](#BKMK_createdby_connection_role)
- [lk_appconfigmaster_modifiedby](#BKMK_lk_appconfigmaster_modifiedby)
- [lk_newprocess_modifiedby](#BKMK_lk_newprocess_modifiedby)
- [lk_columnmapping_modifiedonbehalfby](#BKMK_lk_columnmapping_modifiedonbehalfby)
- [lk_translationprocess_createdby](#BKMK_lk_translationprocess_createdby)
- [lk_monthlyfiscalcalendar_modifiedby](#BKMK_lk_monthlyfiscalcalendar_modifiedby)
- [lk_systemuserbase_modifiedby](#BKMK_lk_systemuserbase_modifiedby)
- [lk_expiredprocess_modifiedby](#BKMK_lk_expiredprocess_modifiedby)
- [lk_SocialProfile_createdonbehalfby](#BKMK_lk_SocialProfile_createdonbehalfby)
- [lk_importmap_createdonbehalfby](#BKMK_lk_importmap_createdonbehalfby)
- [modifiedby_connection](#BKMK_modifiedby_connection)
- [lk_import_createdonbehalfby](#BKMK_lk_import_createdonbehalfby)
- [lk_advancedsimilarityrule_createdby](#BKMK_lk_advancedsimilarityrule_createdby)
- [lk_slaitembase_createdonbehalfby](#BKMK_lk_slaitembase_createdonbehalfby)
- [lk_offlinecommanddefinition_createdonbehalfby](#BKMK_lk_offlinecommanddefinition_createdonbehalfby)
- [lk_navigationsetting_createdonbehalfby](#BKMK_lk_navigationsetting_createdonbehalfby)
- [lk_sdkmessagerequestfield_createdonbehalfby](#BKMK_lk_sdkmessagerequestfield_createdonbehalfby)
- [lk_savedquery_modifiedonbehalfby](#BKMK_lk_savedquery_modifiedonbehalfby)
- [lk_solutioncomponentbase_modifiedonbehalfby](#BKMK_lk_solutioncomponentbase_modifiedonbehalfby)
- [lk_connectionrolebase_createdonbehalfby](#BKMK_lk_connectionrolebase_createdonbehalfby)
- [lk_actioncardbase_createdby](#BKMK_lk_actioncardbase_createdby)
- [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby)
- [lk_webresourcebase_modifiedonbehalfby](#BKMK_lk_webresourcebase_modifiedonbehalfby)
- [user_letter](#BKMK_user_letter)
- [lk_tracelog_modifiedonbehalfby](#BKMK_lk_tracelog_modifiedonbehalfby)
- [lk_timezonedefinition_createdby](#BKMK_lk_timezonedefinition_createdby)
- [lk_reportcategory_createdonbehalfby](#BKMK_lk_reportcategory_createdonbehalfby)
- [createdby_plugintype](#BKMK_createdby_plugintype)
- [lk_organization_createdonbehalfby](#BKMK_lk_organization_createdonbehalfby)
- [lk_calendar_modifiedonbehalfby](#BKMK_lk_calendar_modifiedonbehalfby)
- [lk_slakpiinstancebase_modifiedby](#BKMK_lk_slakpiinstancebase_modifiedby)
- [createdby_plugintracelog](#BKMK_createdby_plugintracelog)
- [user_convertrule](#BKMK_user_convertrule)
- [lk_appconfiginstance_modifiedby](#BKMK_lk_appconfiginstance_modifiedby)
- [lk_picklistmapping_createdonbehalfby](#BKMK_lk_picklistmapping_createdonbehalfby)
- [lk_knowledgearticleviews_createdby](#BKMK_lk_knowledgearticleviews_createdby)
- [SystemUser_Imports](#BKMK_SystemUser_Imports)
- [modifiedby_sdkmessage](#BKMK_modifiedby_sdkmessage)
- [lk_ownermapping_createdonbehalfby](#BKMK_lk_ownermapping_createdonbehalfby)
- [modifiedby_attributemap](#BKMK_modifiedby_attributemap)
- [lk_kbarticlecomment_createdonbehalfby](#BKMK_lk_kbarticlecomment_createdonbehalfby)
- [lk_navigationsetting_modifiedonbehalfby](#BKMK_lk_navigationsetting_modifiedonbehalfby)
- [lk_timezonerule_createdonbehalfby](#BKMK_lk_timezonerule_createdonbehalfby)
- [lk_templatebase_createdby](#BKMK_lk_templatebase_createdby)
- [lk_routingruleitem_modifiedby](#BKMK_lk_routingruleitem_modifiedby)
- [lk_userformbase_modifiedonbehalfby](#BKMK_lk_userformbase_modifiedonbehalfby)
- [workflow_dependency_modifiedby](#BKMK_workflow_dependency_modifiedby)
- [lk_mobileofflineprofileitemassociation_createdonbehalfby](#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby)
- [lk_customeraddress_createdonbehalfby](#BKMK_lk_customeraddress_createdonbehalfby)
- [lk_importfilebase_modifiedby](#BKMK_lk_importfilebase_modifiedby)
- [lk_accountbase_modifiedby](#BKMK_lk_accountbase_modifiedby)
- [lk_personaldocumenttemplatebase_modifiedonbehalfby](#BKMK_lk_personaldocumenttemplatebase_modifiedonbehalfby)
- [lk_category_createdby](#BKMK_lk_category_createdby)
- [lk_customcontroldefaultconfig_modifiedby](#BKMK_lk_customcontroldefaultconfig_modifiedby)
- [user_routingrule](#BKMK_user_routingrule)
- [lk_SharePointData_modifiedonbehalfby](#BKMK_lk_SharePointData_modifiedonbehalfby)
- [lk_SocialProfile_modifiedonbehalfby](#BKMK_lk_SocialProfile_modifiedonbehalfby)
- [user_fax](#BKMK_user_fax)
- [lk_activitypointer_modifiedonbehalfby](#BKMK_lk_activitypointer_modifiedonbehalfby)
- [lk_feedback_createdonbehalfby](#BKMK_lk_feedback_createdonbehalfby)
- [lk_appmodulecomponent_createdby](#BKMK_lk_appmodulecomponent_createdby)
- [lk_sharepointsitebase_modifiedby](#BKMK_lk_sharepointsitebase_modifiedby)
- [lk_sdkmessageprocessingstepimage_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby)
- [lk_importlog_createdonbehalfby](#BKMK_lk_importlog_createdonbehalfby)
- [lk_reportlink_modifiedonbehalfby](#BKMK_lk_reportlink_modifiedonbehalfby)
- [lk_ChannelProperty_modifiedonbehalfby](#BKMK_lk_ChannelProperty_modifiedonbehalfby)
- [lk_processsession_executedby](#BKMK_lk_processsession_executedby)
- [lk_customcontrol_modifiedby](#BKMK_lk_customcontrol_modifiedby)
- [workflow_dependency_modifiedonbehalfby](#BKMK_workflow_dependency_modifiedonbehalfby)
- [lk_customcontrolresource_createdonbehalfby](#BKMK_lk_customcontrolresource_createdonbehalfby)
- [SystemUser_DuplicateMatchingRecord](#BKMK_SystemUser_DuplicateMatchingRecord)
- [createdby_sdkmessageprocessingstepimage](#BKMK_createdby_sdkmessageprocessingstepimage)
- [lk_connectionbase_createdonbehalfby](#BKMK_lk_connectionbase_createdonbehalfby)
- [lk_customcontrol_createdby](#BKMK_lk_customcontrol_createdby)
- [lk_customcontrolresource_modifiedonbehalfby](#BKMK_lk_customcontrolresource_modifiedonbehalfby)
- [lk_ChannelProperty_createdonbehalfby](#BKMK_lk_ChannelProperty_createdonbehalfby)
- [lk_timezonerule_modifiedby](#BKMK_lk_timezonerule_modifiedby)
- [lk_ACIViewMapper_createdonbehalfby](#BKMK_lk_ACIViewMapper_createdonbehalfby)
- [lk_routingrule_modifiedonbehalfby](#BKMK_lk_routingrule_modifiedonbehalfby)
- [lk_audit_userid](#BKMK_lk_audit_userid)
- [lk_solutionbase_createdonbehalfby](#BKMK_lk_solutionbase_createdonbehalfby)
- [lk_convertruleitembase_createdonbehalfby](#BKMK_lk_convertruleitembase_createdonbehalfby)
- [lk_convertruleitembase_modifiedonbehalfby](#BKMK_lk_convertruleitembase_modifiedonbehalfby)
- [lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby)
- [OwnerMapping_SystemUser](#BKMK_OwnerMapping_SystemUser)
- [lk_columnmapping_modifiedby](#BKMK_lk_columnmapping_modifiedby)
- [lk_publisheraddressbase_modifiedby](#BKMK_lk_publisheraddressbase_modifiedby)
- [lk_accountbase_createdby](#BKMK_lk_accountbase_createdby)
- [lk_savedquerybase_modifiedby](#BKMK_lk_savedquerybase_modifiedby)
- [lk_MobileOfflineProfile_modifiedby](#BKMK_lk_MobileOfflineProfile_modifiedby)
- [lk_quarterlyfiscalcalendar_createdby](#BKMK_lk_quarterlyfiscalcalendar_createdby)
- [lk_timezonedefinition_modifiedonbehalfby](#BKMK_lk_timezonedefinition_modifiedonbehalfby)
- [lk_organization_modifiedonbehalfby](#BKMK_lk_organization_modifiedonbehalfby)
- [systemuser_connections1](#BKMK_systemuser_connections1)
- [lk_expanderevent_createdonbehalfby](#BKMK_lk_expanderevent_createdonbehalfby)
- [lk_SiteMap_modifiedby](#BKMK_lk_SiteMap_modifiedby)
- [lk_documenttemplatebase_createdonbehalfby](#BKMK_lk_documenttemplatebase_createdonbehalfby)
- [lk_kbarticlebase_createdby](#BKMK_lk_kbarticlebase_createdby)
- [lk_emailserverprofile_createdby](#BKMK_lk_emailserverprofile_createdby)
- [lk_azureserviceconnection_modifiedby](#BKMK_lk_azureserviceconnection_modifiedby)
- [lk_quarterlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby)
- [lk_userquery_modifiedby](#BKMK_lk_userquery_modifiedby)
- [lk_mobileofflineprofileitemassociation_modifiedby](#BKMK_lk_mobileofflineprofileitemassociation_modifiedby)
- [lk_savedorginsightsconfiguration_modifiedby](#BKMK_lk_savedorginsightsconfiguration_modifiedby)
- [lk_knowledgearticleviews_createdonbehalfby](#BKMK_lk_knowledgearticleviews_createdonbehalfby)
- [lk_convertrule_createdby](#BKMK_lk_convertrule_createdby)
- [lk_savedorginsightsconfiguration_modifiedonbehalfby](#BKMK_lk_savedorginsightsconfiguration_modifiedonbehalfby)
- [lk_processtriggerbase_createdonbehalfby](#BKMK_lk_processtriggerbase_createdonbehalfby)
- [modifiedby_sdkmessageprocessingstepimage](#BKMK_modifiedby_sdkmessageprocessingstepimage)
- [lk_phonecall_modifiedonbehalfby](#BKMK_lk_phonecall_modifiedonbehalfby)
- [lk_workflowlog_createdby](#BKMK_lk_workflowlog_createdby)
- [lk_fixedmonthlyfiscalcalendar_salespersonid](#BKMK_lk_fixedmonthlyfiscalcalendar_salespersonid)
- [lk_quarterlyfiscalcalendar_createdonbehalfby](#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby)
- [createdby_attributemap](#BKMK_createdby_attributemap)
- [lk_teamtemplate_modifiedby](#BKMK_lk_teamtemplate_modifiedby)
- [user_userform](#BKMK_user_userform)
- [lk_processsession_startedby](#BKMK_lk_processsession_startedby)
- [lk_knowledgearticleviews_modifiedonbehalfby](#BKMK_lk_knowledgearticleviews_modifiedonbehalfby)
- [lk_role_modifiedonbehalfby](#BKMK_lk_role_modifiedonbehalfby)
- [lk_SharePointData_modifiedby](#BKMK_lk_SharePointData_modifiedby)
- [lk_reportbase_modifiedby](#BKMK_lk_reportbase_modifiedby)
- [lk_fixedmonthlyfiscalcalendar_createdby](#BKMK_lk_fixedmonthlyfiscalcalendar_createdby)
- [lk_appconfigmaster_createdby](#BKMK_lk_appconfigmaster_createdby)
- [lk_sharepointdata_user](#BKMK_lk_sharepointdata_user)
- [lk_businessunitbase_modifiedby](#BKMK_lk_businessunitbase_modifiedby)
- [socialProfile_owning_user](#BKMK_socialProfile_owning_user)
- [lk_businessprocessflowinstancebase_modifiedonbehalfby](#BKMK_lk_businessprocessflowinstancebase_modifiedonbehalfby)
- [lk_task_modifiedby](#BKMK_lk_task_modifiedby)
- [lk_slaitembase_createdby](#BKMK_lk_slaitembase_createdby)
- [lk_mailboxtrackingfolder_createdonbehalfby](#BKMK_lk_mailboxtrackingfolder_createdonbehalfby)
- [lk_isvconfigbase_createdby](#BKMK_lk_isvconfigbase_createdby)
- [modifiedby_sdkmessageprocessingstep](#BKMK_modifiedby_sdkmessageprocessingstep)
- [lk_reportvisibilitybase_createdby](#BKMK_lk_reportvisibilitybase_createdby)
- [lk_duplicaterulebase_modifiedby](#BKMK_lk_duplicaterulebase_modifiedby)
- [lk_recurrencerulebase_createdonbehalfby](#BKMK_lk_recurrencerulebase_createdonbehalfby)
- [modifiedby_relationship_role_map](#BKMK_modifiedby_relationship_role_map)
- [lk_organizationbase_modifiedby](#BKMK_lk_organizationbase_modifiedby)
- [lk_mailboxtrackingfolder_modifiedonbehalfby](#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby)
- [lk_task_createdby](#BKMK_lk_task_createdby)
- [lk_mailboxtrackingfolder_createdby](#BKMK_lk_mailboxtrackingfolder_createdby)
- [lk_personaldocumenttemplatebase_modifiedby](#BKMK_lk_personaldocumenttemplatebase_modifiedby)
- [lk_processtriggerbase_modifiedby](#BKMK_lk_processtriggerbase_modifiedby)
- [userentityuisettings_owning_user](#BKMK_userentityuisettings_owning_user)
- [lk_userquery_createdby](#BKMK_lk_userquery_createdby)
- [contact_owning_user](#BKMK_contact_owning_user)
- [lk_mailmergetemplate_createdonbehalfby](#BKMK_lk_mailmergetemplate_createdonbehalfby)
- [lk_importjobbase_modifiedonbehalfby](#BKMK_lk_importjobbase_modifiedonbehalfby)
- [lk_customcontroldefaultconfig_createdby](#BKMK_lk_customcontroldefaultconfig_createdby)
- [lk_savedquery_createdonbehalfby](#BKMK_lk_savedquery_createdonbehalfby)
- [system_user_accounts](#BKMK_system_user_accounts)
- [lk_systemuser_createdonbehalfby](#BKMK_lk_systemuser_createdonbehalfby)
- [lk_customcontrol_modifiedonbehalfby](#BKMK_lk_customcontrol_modifiedonbehalfby)
- [lk_appointment_modifiedonbehalfby](#BKMK_lk_appointment_modifiedonbehalfby)
- [lk_externalpartyitem_createdby](#BKMK_lk_externalpartyitem_createdby)
- [lk_knowledgearticleviews_modifiedby](#BKMK_lk_knowledgearticleviews_modifiedby)
- [lk_appconfigmaster_modifiedonbehalfby](#BKMK_lk_appconfigmaster_modifiedonbehalfby)
- [lk_importbase_createdby](#BKMK_lk_importbase_createdby)
- [lk_ACIViewMapper_modifiedonbehalfby](#BKMK_lk_ACIViewMapper_modifiedonbehalfby)
- [lk_solutionbase_modifiedonbehalfby](#BKMK_lk_solutionbase_modifiedonbehalfby)
- [lk_DisplayStringbase_modifiedonbehalfby](#BKMK_lk_DisplayStringbase_modifiedonbehalfby)
- [lk_annotationbase_modifiedby](#BKMK_lk_annotationbase_modifiedby)
- [lk_timezonerule_modifiedonbehalfby](#BKMK_lk_timezonerule_modifiedonbehalfby)
- [lk_importjobbase_createdby](#BKMK_lk_importjobbase_createdby)
- [lk_socialinsightsconfiguration_createdonbehalfby](#BKMK_lk_socialinsightsconfiguration_createdonbehalfby)
- [lk_feedback_createdby](#BKMK_lk_feedback_createdby)
- [lk_timezonelocalizedname_modifiedby](#BKMK_lk_timezonelocalizedname_modifiedby)
- [createdby_sdkmessagepair](#BKMK_createdby_sdkmessagepair)
- [lk_mailmergetemplatebase_createdby](#BKMK_lk_mailmergetemplatebase_createdby)
- [createdby_pluginassembly](#BKMK_createdby_pluginassembly)
- [lk_appconfiginstance_modifiedonbehalfby](#BKMK_lk_appconfiginstance_modifiedonbehalfby)
- [lk_userform_modifiedby](#BKMK_lk_userform_modifiedby)
- [lk_ChannelPropertyGroup_createdby](#BKMK_lk_ChannelPropertyGroup_createdby)
- [lk_publisherbase_createdonbehalfby](#BKMK_lk_publisherbase_createdonbehalfby)
- [lk_sdkmessageresponse_createdonbehalfby](#BKMK_lk_sdkmessageresponse_createdonbehalfby)
- [lk_recurrencerule_createdby](#BKMK_lk_recurrencerule_createdby)
- [lk_slakpiinstancebase_modifiedonbehalfby](#BKMK_lk_slakpiinstancebase_modifiedonbehalfby)
- [SystemUser_ImportFiles](#BKMK_SystemUser_ImportFiles)
- [lk_sdkmessageresponse_modifiedonbehalfby](#BKMK_lk_sdkmessageresponse_modifiedonbehalfby)
- [lk_processsession_modifiedby](#BKMK_lk_processsession_modifiedby)
- [lk_translationprocess_modifiedby](#BKMK_lk_translationprocess_modifiedby)
- [lk_offlinecommanddefinition_modifiedby](#BKMK_lk_offlinecommanddefinition_modifiedby)
- [lk_annualfiscalcalendar_modifiedby](#BKMK_lk_annualfiscalcalendar_modifiedby)
- [user_task](#BKMK_user_task)
- [lk_recurrencerulebase_modifiedonbehalfby](#BKMK_lk_recurrencerulebase_modifiedonbehalfby)
- [lk_phonecall_createdby](#BKMK_lk_phonecall_createdby)
- [lk_templatebase_modifiedonbehalfby](#BKMK_lk_templatebase_modifiedonbehalfby)
- [lk_advancedsimilarityrule_modifiedby](#BKMK_lk_advancedsimilarityrule_modifiedby)
- [lk_fax_modifiedonbehalfby](#BKMK_lk_fax_modifiedonbehalfby)
- [lk_isvconfigbase_modifiedby](#BKMK_lk_isvconfigbase_modifiedby)
- [lk_relationshiprolemap_modifiedonbehalfby](#BKMK_lk_relationshiprolemap_modifiedonbehalfby)
- [lk_contact_createdonbehalfby](#BKMK_lk_contact_createdonbehalfby)
- [lk_customcontroldefaultconfig_createdonbehalfby](#BKMK_lk_customcontroldefaultconfig_createdonbehalfby)
- [lk_publisheraddressbase_createdonbehalfby](#BKMK_lk_publisheraddressbase_createdonbehalfby)
- [lk_annualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_modifiedby](#BKMK_lk_semiannualfiscalcalendar_modifiedby)
- [lk_socialactivity_createdby](#BKMK_lk_socialactivity_createdby)
- [lk_SiteMap_createdby](#BKMK_lk_SiteMap_createdby)
- [lk_syncerrorbase_modifiedby](#BKMK_lk_syncerrorbase_modifiedby)
- [lk_emailsignaturebase_createdonbehalfby](#BKMK_lk_emailsignaturebase_createdonbehalfby)
- [lk_calendar_createdby](#BKMK_lk_calendar_createdby)
- [lk_semiannualfiscalcalendar_modifiedonbehalfby](#BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby)
- [lk_fixedmonthlyfiscalcalendar_modifiedby](#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedby)
- [SystemUser_DuplicateBaseRecord](#BKMK_SystemUser_DuplicateBaseRecord)
- [lk_importentitymapping_createdby](#BKMK_lk_importentitymapping_createdby)
- [lk_queueitembase_createdby](#BKMK_lk_queueitembase_createdby)
- [lk_sdkmessage_createdonbehalfby](#BKMK_lk_sdkmessage_createdonbehalfby)
- [createdby_plugintypestatistic](#BKMK_createdby_plugintypestatistic)
- [createdby_sdkmessagerequest](#BKMK_createdby_sdkmessagerequest)
- [lk_picklistmapping_modifiedby](#BKMK_lk_picklistmapping_modifiedby)
- [lk_sdkmessagerequest_modifiedonbehalfby](#BKMK_lk_sdkmessagerequest_modifiedonbehalfby)
- [lk_team_modifiedonbehalfby](#BKMK_lk_team_modifiedonbehalfby)
- [lk_advancedsimilarityrule_modifiedonbehalfby](#BKMK_lk_advancedsimilarityrule_modifiedonbehalfby)
- [lk_businessunitnewsarticle_modifiedonbehalfby](#BKMK_lk_businessunitnewsarticle_modifiedonbehalfby)
- [SystemUser_ImportLogs](#BKMK_SystemUser_ImportLogs)
- [lk_plugintypestatisticbase_modifiedonbehalfby](#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby)
- [lk_tracelog_createdby](#BKMK_lk_tracelog_createdby)
- [lk_teambase_administratorid](#BKMK_lk_teambase_administratorid)
- [lk_SharePointData_createdby](#BKMK_lk_SharePointData_createdby)
- [lk_reportentity_modifiedonbehalfby](#BKMK_lk_reportentity_modifiedonbehalfby)
- [lk_isvconfig_modifiedonbehalfby](#BKMK_lk_isvconfig_modifiedonbehalfby)
- [lk_savedqueryvisualizationbase_createdby](#BKMK_lk_savedqueryvisualizationbase_createdby)
- [knowledgearticle_primaryauthorid](#BKMK_knowledgearticle_primaryauthorid)
- [lk_fixedmonthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_fixedmonthlyfiscalcalendar_createdonbehalfby)
- [lk_offlinecommanddefinition_modifiedonbehalfby](#BKMK_lk_offlinecommanddefinition_modifiedonbehalfby)
- [lk_email_createdby](#BKMK_lk_email_createdby)
- [lk_monthlyfiscalcalendar_createdby](#BKMK_lk_monthlyfiscalcalendar_createdby)
- [lk_routingruleitem_modifiedonbehalfby](#BKMK_lk_routingruleitem_modifiedonbehalfby)
- [lk_queuebase_createdby](#BKMK_lk_queuebase_createdby)
- [lk_appmodulecomponent_createdonbehalfby](#BKMK_lk_appmodulecomponent_createdonbehalfby)
- [lk_personaldocumenttemplatebase_createdonbehalfby](#BKMK_lk_personaldocumenttemplatebase_createdonbehalfby)
- [lk_savedqueryvisualizationbase_createdonbehalfby](#BKMK_lk_savedqueryvisualizationbase_createdonbehalfby)
- [lk_newprocess_createdby](#BKMK_lk_newprocess_createdby)
- [lk_category_createdonbehalfby](#BKMK_lk_category_createdonbehalfby)
- [lk_sharepointdocumentbase_modifiedby](#BKMK_lk_sharepointdocumentbase_modifiedby)
- [lk_newprocess_modifiedonbehalfby](#BKMK_lk_newprocess_modifiedonbehalfby)
- [lk_feedback_closedby](#BKMK_lk_feedback_closedby)
- [lk_expanderevent_modifiedonbehalfby](#BKMK_lk_expanderevent_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_createdby](#BKMK_lk_semiannualfiscalcalendar_createdby)
- [lk_duplicateruleconditionbase_modifiedby](#BKMK_lk_duplicateruleconditionbase_modifiedby)
- [queue_primary_user](#BKMK_queue_primary_user)
- [lk_emailsignaturebase_createdby](#BKMK_lk_emailsignaturebase_createdby)
- [user_email](#BKMK_user_email)
- [lk_reportbase_createdby](#BKMK_lk_reportbase_createdby)
- [lk_appointment_createdby](#BKMK_lk_appointment_createdby)
- [lk_letter_modifiedby](#BKMK_lk_letter_modifiedby)
- [lk_customcontrol_createdonbehalfby](#BKMK_lk_customcontrol_createdonbehalfby)
- [lk_usersettingsbase_modifiedby](#BKMK_lk_usersettingsbase_modifiedby)
- [lk_reportvisibility_modifiedonbehalfby](#BKMK_lk_reportvisibility_modifiedonbehalfby)
- [lk_queueitembase_modifiedby](#BKMK_lk_queueitembase_modifiedby)
- [userentityinstancedata_owning_user](#BKMK_userentityinstancedata_owning_user)
- [lk_sdkmessageprocessingstep_modifiedonbehalfby](#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby)
- [modifiedby_pluginassembly](#BKMK_modifiedby_pluginassembly)
- [lk_businessprocessflowinstancebase_modifiedby](#BKMK_lk_businessprocessflowinstancebase_modifiedby)
- [lk_sharepointdocumentlocationbase_modifiedby](#BKMK_lk_sharepointdocumentlocationbase_modifiedby)
- [system_user_activity_parties](#BKMK_system_user_activity_parties)
- [lk_annualfiscalcalendar_salespersonid](#BKMK_lk_annualfiscalcalendar_salespersonid)
- [SystemUser_AsyncOperations](#BKMK_SystemUser_AsyncOperations)
- [lk_publisheraddressbase_createdby](#BKMK_lk_publisheraddressbase_createdby)
- [lk_import_modifiedonbehalfby](#BKMK_lk_import_modifiedonbehalfby)
- [lk_queuebase_modifiedby](#BKMK_lk_queuebase_modifiedby)
- [lk_savedorginsightsconfiguration_createdby](#BKMK_lk_savedorginsightsconfiguration_createdby)
- [SystemUser_ImportMaps](#BKMK_SystemUser_ImportMaps)
- [workflow_modifiedonbehalfby](#BKMK_workflow_modifiedonbehalfby)
- [lk_category_modifiedby](#BKMK_lk_category_modifiedby)
- [lk_SiteMap_createdonbehalfby](#BKMK_lk_SiteMap_createdonbehalfby)
- [webresource_modifiedby](#BKMK_webresource_modifiedby)
- [createdby_sdkmessage](#BKMK_createdby_sdkmessage)
- [lk_importlogbase_modifiedby](#BKMK_lk_importlogbase_modifiedby)
- [lk_routingrule_createdonbehalfby](#BKMK_lk_routingrule_createdonbehalfby)
- [lk_importjobbase_createdonbehalfby](#BKMK_lk_importjobbase_createdonbehalfby)
- [lk_monthlyfiscalcalendar_modifiedonbehalfby](#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby)
- [lk_transactioncurrency_createdonbehalfby](#BKMK_lk_transactioncurrency_createdonbehalfby)
- [lk_bulkdeleteoperation_createdonbehalfby](#BKMK_lk_bulkdeleteoperation_createdonbehalfby)
- [modifiedby_plugintypestatistic](#BKMK_modifiedby_plugintypestatistic)
- [lk_actioncardbase_modifiedonbehalfby](#BKMK_lk_actioncardbase_modifiedonbehalfby)
- [lk_recurringappointmentmaster_createdby](#BKMK_lk_recurringappointmentmaster_createdby)
- [modifiedonbehalfby_customer_relationship](#BKMK_modifiedonbehalfby_customer_relationship)
- [lk_DisplayStringbase_createdonbehalfby](#BKMK_lk_DisplayStringbase_createdonbehalfby)
- [lk_audit_callinguserid](#BKMK_lk_audit_callinguserid)
- [lk_sdkmessagerequest_createdonbehalfby](#BKMK_lk_sdkmessagerequest_createdonbehalfby)
- [lk_importfilebase_createdby](#BKMK_lk_importfilebase_createdby)
- [lk_importmap_modifiedonbehalfby](#BKMK_lk_importmap_modifiedonbehalfby)
- [lk_expiredprocess_modifiedonbehalfby](#BKMK_lk_expiredprocess_modifiedonbehalfby)
- [lk_userqueryvisualizationbase_modifiedonbehalfby](#BKMK_lk_userqueryvisualizationbase_modifiedonbehalfby)
- [lk_semiannualfiscalcalendar_salespersonid](#BKMK_lk_semiannualfiscalcalendar_salespersonid)
- [lk_report_createdonbehalfby](#BKMK_lk_report_createdonbehalfby)
- [lk_processsession_canceledby](#BKMK_lk_processsession_canceledby)
- [lk_SiteMap_modifiedonbehalfby](#BKMK_lk_SiteMap_modifiedonbehalfby)
- [SystemUser_SyncError](#BKMK_SystemUser_SyncError)
- [lk_socialactivity_modifiedby](#BKMK_lk_socialactivity_modifiedby)
- [lk_accountbase_modifiedonbehalfby](#BKMK_lk_accountbase_modifiedonbehalfby)
- [lk_subjectbase_createdby](#BKMK_lk_subjectbase_createdby)
- [lk_MobileOfflineProfile_modifiedonbehalfby](#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby)
- [lk_annotationbase_modifiedonbehalfby](#BKMK_lk_annotationbase_modifiedonbehalfby)
- [lk_kbarticletemplatebase_createdby](#BKMK_lk_kbarticletemplatebase_createdby)
- [lk_importbase_modifiedby](#BKMK_lk_importbase_modifiedby)
- [modifiedby_connection_role](#BKMK_modifiedby_connection_role)
- [lk_sharepointdocumentlocationbase_createdonbehalfby](#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby)
- [lk_mailmergetemplatebase_modifiedby](#BKMK_lk_mailmergetemplatebase_modifiedby)
- [lk_userquery_createdonbehalfby](#BKMK_lk_userquery_createdonbehalfby)
- [lk_transactioncurrencybase_createdby](#BKMK_lk_transactioncurrencybase_createdby)
- [lk_entitymap_createdonbehalfby](#BKMK_lk_entitymap_createdonbehalfby)
- [lk_knowledgesearchmodel_createdonbehalfby](#BKMK_lk_knowledgesearchmodel_createdonbehalfby)
- [createdonbehalfby_customer_relationship](#BKMK_createdonbehalfby_customer_relationship)
- [lk_sharepointdocumentbase_createdby](#BKMK_lk_sharepointdocumentbase_createdby)
- [lk_queue_createdonbehalfby](#BKMK_lk_queue_createdonbehalfby)
- [lk_MobileOfflineProfile_createdby](#BKMK_lk_MobileOfflineProfile_createdby)
- [modifiedby_expanderevent](#BKMK_modifiedby_expanderevent)
- [lk_savedorginsightsconfiguration_createdonbehalfby](#BKMK_lk_savedorginsightsconfiguration_createdonbehalfby)
- [modifiedby_serviceendpoint](#BKMK_modifiedby_serviceendpoint)
- [lk_appointment_modifiedby](#BKMK_lk_appointment_modifiedby)
- [lk_emailsignaturebase_modifiedonbehalfby](#BKMK_lk_emailsignaturebase_modifiedonbehalfby)
- [lk_picklistmapping_modifiedonbehalfby](#BKMK_lk_picklistmapping_modifiedonbehalfby)
- [user_routingruleitem](#BKMK_user_routingruleitem)
- [lk_transformationmapping_createdonbehalfby](#BKMK_lk_transformationmapping_createdonbehalfby)
- [lk_plugintypestatisticbase_createdonbehalfby](#BKMK_lk_plugintypestatisticbase_createdonbehalfby)
- [lk_kbarticletemplate_createdonbehalfby](#BKMK_lk_kbarticletemplate_createdonbehalfby)
- [createdby_sdkmessagerequestfield](#BKMK_createdby_sdkmessagerequestfield)
- [ImportFile_SystemUser](#BKMK_ImportFile_SystemUser)
- [lk_importmapbase_modifiedby](#BKMK_lk_importmapbase_modifiedby)
- [lk_userform_createdby](#BKMK_lk_userform_createdby)
- [lk_isvconfig_createdonbehalfby](#BKMK_lk_isvconfig_createdonbehalfby)
- [lk_expiredprocess_createdby](#BKMK_lk_expiredprocess_createdby)
- [lk_socialinsightsconfiguration_modifiedonbehalfby](#BKMK_lk_socialinsightsconfiguration_modifiedonbehalfby)
- [lk_reportvisibility_createdonbehalfby](#BKMK_lk_reportvisibility_createdonbehalfby)
- [lk_userqueryvisualization_createdby](#BKMK_lk_userqueryvisualization_createdby)
- [lk_ACIViewMapper_modifiedby](#BKMK_lk_ACIViewMapper_modifiedby)
- [user_slabase](#BKMK_user_slabase)
- [lk_reportlinkbase_createdby](#BKMK_lk_reportlinkbase_createdby)
- [lk_annotationbase_createdby](#BKMK_lk_annotationbase_createdby)
- [webresource_createdby](#BKMK_webresource_createdby)
- [lk_userqueryvisualizationbase_createdonbehalfby](#BKMK_lk_userqueryvisualizationbase_createdonbehalfby)
- [lk_usersettings_modifiedonbehalfby](#BKMK_lk_usersettings_modifiedonbehalfby)
- [user_parent_user](#BKMK_user_parent_user)
- [lk_appconfiginstance_createdby](#BKMK_lk_appconfiginstance_createdby)
- [createdonbehalfby_attributemap](#BKMK_createdonbehalfby_attributemap)
- [lk_annualfiscalcalendar_createdonbehalfby](#BKMK_lk_annualfiscalcalendar_createdonbehalfby)
- [lk_userformbase_createdonbehalfby](#BKMK_lk_userformbase_createdonbehalfby)
- [lk_knowledgesearchmodel_modifiedby](#BKMK_lk_knowledgesearchmodel_modifiedby)
- [modifiedby_sdkmessageresponsefield](#BKMK_modifiedby_sdkmessageresponsefield)
- [lk_SharePointData_createdonbehalfby](#BKMK_lk_SharePointData_createdonbehalfby)
- [lk_fieldsecurityprofile_createdby](#BKMK_lk_fieldsecurityprofile_createdby)
- [lk_asyncoperation_modifiedby](#BKMK_lk_asyncoperation_modifiedby)
- [lk_pluginassembly_createdonbehalfby](#BKMK_lk_pluginassembly_createdonbehalfby)
- [lk_importentitymapping_modifiedby](#BKMK_lk_importentitymapping_modifiedby)
- [lk_ChannelPropertyGroup_createdonbehalfby](#BKMK_lk_ChannelPropertyGroup_createdonbehalfby)
- [lk_sdkmessageprocessingstep_createdonbehalfby](#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby)
- [lk_ConvertRule_modifiedonbehalfby](#BKMK_lk_ConvertRule_modifiedonbehalfby)
- [lk_activitypointer_createdonbehalfby](#BKMK_lk_activitypointer_createdonbehalfby)
- [lk_contact_modifiedonbehalfby](#BKMK_lk_contact_modifiedonbehalfby)
- [lk_savedqueryvisualizationbase_modifiedonbehalfby](#BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby)
- [lk_socialinsightsconfiguration_createdby](#BKMK_lk_socialinsightsconfiguration_createdby)
- [lk_accountbase_createdonbehalfby](#BKMK_lk_accountbase_createdonbehalfby)
- [modifiedby_sdkmessagefilter](#BKMK_modifiedby_sdkmessagefilter)
- [system_user_email_templates](#BKMK_system_user_email_templates)
- [lk_ownermapping_modifiedonbehalfby](#BKMK_lk_ownermapping_modifiedonbehalfby)
- [lk_ChannelPropertyGroup_modifiedby](#BKMK_lk_ChannelPropertyGroup_modifiedby)
- [lk_systemuser_modifiedonbehalfby](#BKMK_lk_systemuser_modifiedonbehalfby)
- [lk_annualfiscalcalendar_createdby](#BKMK_lk_annualfiscalcalendar_createdby)
- [lk_email_createdonbehalfby](#BKMK_lk_email_createdonbehalfby)
- [lk_recurringappointmentmaster_modifiedonbehalfby](#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby)
- [lk_timezonelocalizedname_createdby](#BKMK_lk_timezonelocalizedname_createdby)
- [lk_bulkdeleteoperationbase_modifiedby](#BKMK_lk_bulkdeleteoperationbase_modifiedby)
- [lk_sharepointsitebase_modifiedonbehalfby](#BKMK_lk_sharepointsitebase_modifiedonbehalfby)
- [lk_ownermapping_modifiedby](#BKMK_lk_ownermapping_modifiedby)
- [lk_sharepointsitebase_createdby](#BKMK_lk_sharepointsitebase_createdby)
- [createdby_sdkmessageresponsefield](#BKMK_createdby_sdkmessageresponsefield)
- [lk_actioncardbase_modifiedby](#BKMK_lk_actioncardbase_modifiedby)
- [lk_webresourcebase_createdonbehalfby](#BKMK_lk_webresourcebase_createdonbehalfby)
- [lk_connectionrolebase_modifiedonbehalfby](#BKMK_lk_connectionrolebase_modifiedonbehalfby)
- [lk_timezonelocalizedname_modifiedonbehalfby](#BKMK_lk_timezonelocalizedname_modifiedonbehalfby)
- [lk_transformationmapping_modifiedonbehalfby](#BKMK_lk_transformationmapping_modifiedonbehalfby)
- [lk_azureserviceconnection_createdby](#BKMK_lk_azureserviceconnection_createdby)
- [lk_documenttemplatebase_modifiedonbehalfby](#BKMK_lk_documenttemplatebase_modifiedonbehalfby)
- [user_phonecall](#BKMK_user_phonecall)
- [lk_serviceendpointbase_modifiedonbehalfby](#BKMK_lk_serviceendpointbase_modifiedonbehalfby)
- [lk_reportlinkbase_modifiedby](#BKMK_lk_reportlinkbase_modifiedby)
- [lk_slabase_createdonbehalfby](#BKMK_lk_slabase_createdonbehalfby)
- [lk_importjobbase_modifiedby](#BKMK_lk_importjobbase_modifiedby)
- [lk_MobileOfflineProfileItemAssociation_createdby](#BKMK_lk_MobileOfflineProfileItemAssociation_createdby)
- [lk_processtriggerbase_createdby](#BKMK_lk_processtriggerbase_createdby)
- [lk_timezonedefinition_createdonbehalfby](#BKMK_lk_timezonedefinition_createdonbehalfby)
- [lk_kbarticlecomment_modifiedonbehalfby](#BKMK_lk_kbarticlecomment_modifiedonbehalfby)
- [lk_timezonelocalizedname_createdonbehalfby](#BKMK_lk_timezonelocalizedname_createdonbehalfby)
- [lk_systemuserbase_createdby](#BKMK_lk_systemuserbase_createdby)
- [systemuser_principalobjectattributeaccess](#BKMK_systemuser_principalobjectattributeaccess)
- [system_user_asyncoperation](#BKMK_system_user_asyncoperation)
- [lk_reportlink_createdonbehalfby](#BKMK_lk_reportlink_createdonbehalfby)
- [lk_plugintracelogbase_createdonbehalfby](#BKMK_lk_plugintracelogbase_createdonbehalfby)
- [lk_teamtemplate_createdby](#BKMK_lk_teamtemplate_createdby)
- [lk_annotationbase_createdonbehalfby](#BKMK_lk_annotationbase_createdonbehalfby)
- [lk_fieldsecurityprofile_modifiedonbehalfby](#BKMK_lk_fieldsecurityprofile_modifiedonbehalfby)
- [lk_appmodulecomponent_modifiedonbehalfby](#BKMK_lk_appmodulecomponent_modifiedonbehalfby)
- [lk_reportentitybase_createdby](#BKMK_lk_reportentitybase_createdby)
- [lk_semiannualfiscalcalendar_createdonbehalfby](#BKMK_lk_semiannualfiscalcalendar_createdonbehalfby)
- [lk_userquery_modifiedonbehalfby](#BKMK_lk_userquery_modifiedonbehalfby)
- [lk_businessunitnewsarticlebase_createdby](#BKMK_lk_businessunitnewsarticlebase_createdby)
- [systemuser_connections2](#BKMK_systemuser_connections2)
- [lk_task_createdonbehalfby](#BKMK_lk_task_createdonbehalfby)
- [lk_contactbase_modifiedby](#BKMK_lk_contactbase_modifiedby)
- [lk_letter_createdonbehalfby](#BKMK_lk_letter_createdonbehalfby)
- [lk_customcontrolresource_createdby](#BKMK_lk_customcontrolresource_createdby)
- [lk_socialactivitybase_modifiedonbehalfby](#BKMK_lk_socialactivitybase_modifiedonbehalfby)
- [lk_socialactivitybase_createdonbehalfby](#BKMK_lk_socialactivitybase_createdonbehalfby)
- [lk_importfilebase_modifiedonbehalfby](#BKMK_lk_importfilebase_modifiedonbehalfby)
- [lk_sdkmessagerequestfield_modifiedonbehalfby](#BKMK_lk_sdkmessagerequestfield_modifiedonbehalfby)
- [lk_fieldsecurityprofile_modifiedby](#BKMK_lk_fieldsecurityprofile_modifiedby)
- [lk_newprocess_createdonbehalfby](#BKMK_lk_newprocess_createdonbehalfby)
- [lk_appconfig_createdby](#BKMK_lk_appconfig_createdby)
- [lk_businessunitbase_createdby](#BKMK_lk_businessunitbase_createdby)
- [lk_monthlyfiscalcalendar_createdonbehalfby](#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby)
- [lk_sharepointdocumentlocationbase_modifiedonbehalfby](#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby)
- [lk_advancedsimilarityrule_createdonbehalfby](#BKMK_lk_advancedsimilarityrule_createdonbehalfby)
- [lk_syncerrorbase_createdby](#BKMK_lk_syncerrorbase_createdby)
- [modifiedby_sdkmessagerequestfield](#BKMK_modifiedby_sdkmessagerequestfield)
- [createdby_sdkmessagefilter](#BKMK_createdby_sdkmessagefilter)
- [lk_knowledgesearchmodel_createdby](#BKMK_lk_knowledgesearchmodel_createdby)
- [lk_kbarticlebase_modifiedby](#BKMK_lk_kbarticlebase_modifiedby)
- [lk_ownermapping_createdby](#BKMK_lk_ownermapping_createdby)
- [SystemUser_SyncErrors](#BKMK_SystemUser_SyncErrors)
- [lk_duplicateruleconditionbase_createdby](#BKMK_lk_duplicateruleconditionbase_createdby)


### <a name="BKMK_lk_appmodule_modifiedby"></a> lk_appmodule_modifiedby

Same as appmodule entity [lk_appmodule_modifiedby](appmodule.md#BKMK_lk_appmodule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: appmodule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appmodule_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_territorybase_createdby"></a> lk_territorybase_createdby

Same as territory entity [lk_territorybase_createdby](territory.md#BKMK_lk_territorybase_createdby) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_territorybase_createdby<br />
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


### <a name="BKMK_lk_territory_createdonbehalfby"></a> lk_territory_createdonbehalfby

Same as territory entity [lk_territory_createdonbehalfby](territory.md#BKMK_lk_territory_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_territorybase_createdonbehalfby<br />
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


### <a name="BKMK_lk_territorybase_modifiedby"></a> lk_territorybase_modifiedby

Same as territory entity [lk_territorybase_modifiedby](territory.md#BKMK_lk_territorybase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_territorybase_modifiedby<br />
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


### <a name="BKMK_lk_territory_modifiedonbehalfby"></a> lk_territory_modifiedonbehalfby

Same as territory entity [lk_territory_modifiedonbehalfby](territory.md#BKMK_lk_territory_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_territorybase_modifiedonbehalfby<br />
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


### <a name="BKMK_system_user_territories"></a> system_user_territories

Same as territory entity [system_user_territories](territory.md#BKMK_system_user_territories) Many-To-One relationship.

**ReferencingEntity**: territory<br />
**ReferencingAttribute**: managerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: system_user_territories<br />
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


### <a name="BKMK_systemuser_principalobjectattributeaccess_principalid"></a> systemuser_principalobjectattributeaccess_principalid

Same as principalobjectattributeaccess entity [systemuser_principalobjectattributeaccess_principalid](principalobjectattributeaccess.md#BKMK_systemuser_principalobjectattributeaccess_principalid) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: principalid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: systemuser_principalobjectattributeaccess_principalid<br />
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


### <a name="BKMK_user_exchangesyncidmapping"></a> user_exchangesyncidmapping

Same as exchangesyncidmapping entity [user_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_user_exchangesyncidmapping) Many-To-One relationship.

**ReferencingEntity**: exchangesyncidmapping<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_exchangesyncidmapping<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_theme_createdby"></a> lk_theme_createdby

Same as theme entity [lk_theme_createdby](theme.md#BKMK_lk_theme_createdby) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_theme_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_theme_createdonbehalfby"></a> lk_theme_createdonbehalfby

Same as theme entity [lk_theme_createdonbehalfby](theme.md#BKMK_lk_theme_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_theme_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_theme_modifiedby"></a> lk_theme_modifiedby

Same as theme entity [lk_theme_modifiedby](theme.md#BKMK_lk_theme_modifiedby) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_theme_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_theme_modifiedonbehalfby"></a> lk_theme_modifiedonbehalfby

Same as theme entity [lk_theme_modifiedonbehalfby](theme.md#BKMK_lk_theme_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: theme<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_theme_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_usermapping_createdby"></a> lk_usermapping_createdby

Same as usermapping entity [lk_usermapping_createdby](usermapping.md#BKMK_lk_usermapping_createdby) Many-To-One relationship.

**ReferencingEntity**: usermapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_usermapping_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_usermapping_createdonbehalfby"></a> lk_usermapping_createdonbehalfby

Same as usermapping entity [lk_usermapping_createdonbehalfby](usermapping.md#BKMK_lk_usermapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: usermapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_usermapping_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_usermapping_modifiedby"></a> lk_usermapping_modifiedby

Same as usermapping entity [lk_usermapping_modifiedby](usermapping.md#BKMK_lk_usermapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: usermapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_usermapping_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_usermapping_modifiedonbehalfby"></a> lk_usermapping_modifiedonbehalfby

Same as usermapping entity [lk_usermapping_modifiedonbehalfby](usermapping.md#BKMK_lk_usermapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: usermapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_usermapping_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_interactionforemail_createdby"></a> lk_interactionforemail_createdby

Same as interactionforemail entity [lk_interactionforemail_createdby](interactionforemail.md#BKMK_lk_interactionforemail_createdby) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_new_interactionforemail_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_interactionforemail_createdonbehalfby"></a> lk_interactionforemail_createdonbehalfby

Same as interactionforemail entity [lk_interactionforemail_createdonbehalfby](interactionforemail.md#BKMK_lk_interactionforemail_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_new_interactionforemail_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_interactionforemail_modifiedby"></a> lk_interactionforemail_modifiedby

Same as interactionforemail entity [lk_interactionforemail_modifiedby](interactionforemail.md#BKMK_lk_interactionforemail_modifiedby) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_new_interactionforemail_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_interactionforemail_modifiedonbehalfby"></a> lk_interactionforemail_modifiedonbehalfby

Same as interactionforemail entity [lk_interactionforemail_modifiedonbehalfby](interactionforemail.md#BKMK_lk_interactionforemail_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_new_interactionforemail_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_interactionforemail"></a> user_interactionforemail

Same as interactionforemail entity [user_interactionforemail](interactionforemail.md#BKMK_user_interactionforemail) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_new_interactionforemail<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_knowledgearticle_createdby"></a> lk_knowledgearticle_createdby

Same as knowledgearticle entity [lk_knowledgearticle_createdby](knowledgearticle.md#BKMK_lk_knowledgearticle_createdby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticle_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_knowledgearticle_createdonbehalfby"></a> lk_knowledgearticle_createdonbehalfby

Same as knowledgearticle entity [lk_knowledgearticle_createdonbehalfby](knowledgearticle.md#BKMK_lk_knowledgearticle_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticle_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_knowledgearticle_modifiedby"></a> lk_knowledgearticle_modifiedby

Same as knowledgearticle entity [lk_knowledgearticle_modifiedby](knowledgearticle.md#BKMK_lk_knowledgearticle_modifiedby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticle_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_knowledgearticle_modifiedonbehalfby"></a> lk_knowledgearticle_modifiedonbehalfby

Same as knowledgearticle entity [lk_knowledgearticle_modifiedonbehalfby](knowledgearticle.md#BKMK_lk_knowledgearticle_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticle_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_knowledgearticle"></a> user_knowledgearticle

Same as knowledgearticle entity [user_knowledgearticle](knowledgearticle.md#BKMK_user_knowledgearticle) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_knowledgearticle<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_sharepointsite"></a> user_sharepointsite

Same as sharepointsite entity [user_sharepointsite](sharepointsite.md#BKMK_user_sharepointsite) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_sharepointsite<br />
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


### <a name="BKMK_user_sharepointdocumentlocation"></a> user_sharepointdocumentlocation

Same as sharepointdocumentlocation entity [user_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_user_sharepointdocumentlocation) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_sharepointdocumentlocation<br />
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


### <a name="BKMK_lk_suggestioncardtemplate_createdby"></a> lk_suggestioncardtemplate_createdby

Same as suggestioncardtemplate entity [lk_suggestioncardtemplate_createdby](suggestioncardtemplate.md#BKMK_lk_suggestioncardtemplate_createdby) Many-To-One relationship.

**ReferencingEntity**: suggestioncardtemplate<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_suggestioncardtemplate_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_suggestioncardtemplate_createdonbehalfby"></a> lk_suggestioncardtemplate_createdonbehalfby

Same as suggestioncardtemplate entity [lk_suggestioncardtemplate_createdonbehalfby](suggestioncardtemplate.md#BKMK_lk_suggestioncardtemplate_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: suggestioncardtemplate<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_suggestioncardtemplate_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_suggestioncardtemplate_modifiedby"></a> lk_suggestioncardtemplate_modifiedby

Same as suggestioncardtemplate entity [lk_suggestioncardtemplate_modifiedby](suggestioncardtemplate.md#BKMK_lk_suggestioncardtemplate_modifiedby) Many-To-One relationship.

**ReferencingEntity**: suggestioncardtemplate<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_suggestioncardtemplate_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_suggestioncardtemplate_modifiedonbehalfby"></a> lk_suggestioncardtemplate_modifiedonbehalfby

Same as suggestioncardtemplate entity [lk_suggestioncardtemplate_modifiedonbehalfby](suggestioncardtemplate.md#BKMK_lk_suggestioncardtemplate_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: suggestioncardtemplate<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_suggestioncardtemplate_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goal_createdby"></a> lk_goal_createdby

Same as goal entity [lk_goal_createdby](goal.md#BKMK_lk_goal_createdby) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_goal_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goal_createdonbehalfby"></a> lk_goal_createdonbehalfby

Same as goal entity [lk_goal_createdonbehalfby](goal.md#BKMK_lk_goal_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_goal_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goal_modifiedby"></a> lk_goal_modifiedby

Same as goal entity [lk_goal_modifiedby](goal.md#BKMK_lk_goal_modifiedby) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_goal_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goal_modifiedonbehalfby"></a> lk_goal_modifiedonbehalfby

Same as goal entity [lk_goal_modifiedonbehalfby](goal.md#BKMK_lk_goal_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_goal_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_goal"></a> user_goal

Same as goal entity [user_goal](goal.md#BKMK_user_goal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_goal<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_goal_goalowner"></a> user_goal_goalowner

Same as goal entity [user_goal_goalowner](goal.md#BKMK_user_goal_goalowner) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: goalownerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_goal_goalowner<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_metric_createdby"></a> lk_metric_createdby

Same as metric entity [lk_metric_createdby](metric.md#BKMK_lk_metric_createdby) Many-To-One relationship.

**ReferencingEntity**: metric<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_metric_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_metric_createdonbehalfby"></a> lk_metric_createdonbehalfby

Same as metric entity [lk_metric_createdonbehalfby](metric.md#BKMK_lk_metric_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: metric<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_metric_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_metric_modifiedby"></a> lk_metric_modifiedby

Same as metric entity [lk_metric_modifiedby](metric.md#BKMK_lk_metric_modifiedby) Many-To-One relationship.

**ReferencingEntity**: metric<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_metric_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_metric_modifiedonbehalfby"></a> lk_metric_modifiedonbehalfby

Same as metric entity [lk_metric_modifiedonbehalfby](metric.md#BKMK_lk_metric_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: metric<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_metric_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_rollupfield_createdby"></a> lk_rollupfield_createdby

Same as rollupfield entity [lk_rollupfield_createdby](rollupfield.md#BKMK_lk_rollupfield_createdby) Many-To-One relationship.

**ReferencingEntity**: rollupfield<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_rollupfield_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_rollupfield_createdonbehalfby"></a> lk_rollupfield_createdonbehalfby

Same as rollupfield entity [lk_rollupfield_createdonbehalfby](rollupfield.md#BKMK_lk_rollupfield_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: rollupfield<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_rollupfield_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_rollupfield_modifiedby"></a> lk_rollupfield_modifiedby

Same as rollupfield entity [lk_rollupfield_modifiedby](rollupfield.md#BKMK_lk_rollupfield_modifiedby) Many-To-One relationship.

**ReferencingEntity**: rollupfield<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_rollupfield_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_rollupfield_modifiedonbehalfby"></a> lk_rollupfield_modifiedonbehalfby

Same as rollupfield entity [lk_rollupfield_modifiedonbehalfby](rollupfield.md#BKMK_lk_rollupfield_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: rollupfield<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_rollupfield_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goalrollupquery_createdby"></a> lk_goalrollupquery_createdby

Same as goalrollupquery entity [lk_goalrollupquery_createdby](goalrollupquery.md#BKMK_lk_goalrollupquery_createdby) Many-To-One relationship.

**ReferencingEntity**: goalrollupquery<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_goalrollupquery_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goalrollupquery_createdonbehalfby"></a> lk_goalrollupquery_createdonbehalfby

Same as goalrollupquery entity [lk_goalrollupquery_createdonbehalfby](goalrollupquery.md#BKMK_lk_goalrollupquery_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: goalrollupquery<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_goalrollupquery_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goalrollupquery_modifiedby"></a> lk_goalrollupquery_modifiedby

Same as goalrollupquery entity [lk_goalrollupquery_modifiedby](goalrollupquery.md#BKMK_lk_goalrollupquery_modifiedby) Many-To-One relationship.

**ReferencingEntity**: goalrollupquery<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_goalrollupquery_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_goalrollupquery_modifiedonbehalfby"></a> lk_goalrollupquery_modifiedonbehalfby

Same as goalrollupquery entity [lk_goalrollupquery_modifiedonbehalfby](goalrollupquery.md#BKMK_lk_goalrollupquery_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: goalrollupquery<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_goalrollupquery_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_emailserverprofile_createdonbehalfby"></a> lk_emailserverprofile_createdonbehalfby

Same as emailserverprofile entity [lk_emailserverprofile_createdonbehalfby](emailserverprofile.md#BKMK_lk_emailserverprofile_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_emailserverprofile_createdonbehalfby<br />
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


### <a name="BKMK_lk_emailserverprofile_modifiedonbehalfby"></a> lk_emailserverprofile_modifiedonbehalfby

Same as emailserverprofile entity [lk_emailserverprofile_modifiedonbehalfby](emailserverprofile.md#BKMK_lk_emailserverprofile_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_emailserverprofile_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_mailbox_createdby"></a> lk_mailbox_createdby

Same as mailbox entity [lk_mailbox_createdby](mailbox.md#BKMK_lk_mailbox_createdby) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailbox_createdby<br />
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


### <a name="BKMK_lk_mailbox_createdonbehalfby"></a> lk_mailbox_createdonbehalfby

Same as mailbox entity [lk_mailbox_createdonbehalfby](mailbox.md#BKMK_lk_mailbox_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailbox_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_mailbox_modifiedby"></a> lk_mailbox_modifiedby

Same as mailbox entity [lk_mailbox_modifiedby](mailbox.md#BKMK_lk_mailbox_modifiedby) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailbox_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_mailbox_modifiedonbehalfby"></a> lk_mailbox_modifiedonbehalfby

Same as mailbox entity [lk_mailbox_modifiedonbehalfby](mailbox.md#BKMK_lk_mailbox_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailbox_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_mailbox"></a> user_mailbox

Same as mailbox entity [user_mailbox](mailbox.md#BKMK_user_mailbox) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_mailbox<br />
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


### <a name="BKMK_mailbox_regarding_systemuser"></a> mailbox_regarding_systemuser

Same as mailbox entity [mailbox_regarding_systemuser](mailbox.md#BKMK_mailbox_regarding_systemuser) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: mailbox_regarding_systemuser<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: Cascade
- **Delete**: NoCascade
- **Merge**: Cascade
- **Reparent**: Cascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_post_modifiedonbehalfby"></a> lk_post_modifiedonbehalfby

Same as post entity [lk_post_modifiedonbehalfby](post.md#BKMK_lk_post_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: post<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_post_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_position_createdby"></a> lk_position_createdby

Same as position entity [lk_position_createdby](position.md#BKMK_lk_position_createdby) Many-To-One relationship.

**ReferencingEntity**: position<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_position_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_position_createdonbehalfby"></a> lk_position_createdonbehalfby

Same as position entity [lk_position_createdonbehalfby](position.md#BKMK_lk_position_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: position<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_position_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_position_modifiedby"></a> lk_position_modifiedby

Same as position entity [lk_position_modifiedby](position.md#BKMK_lk_position_modifiedby) Many-To-One relationship.

**ReferencingEntity**: position<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_position_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_position_modifiedonbehalfby"></a> lk_position_modifiedonbehalfby

Same as position entity [lk_position_modifiedonbehalfby](position.md#BKMK_lk_position_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: position<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_position_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_cardtype_createdby"></a> lk_cardtype_createdby

Same as cardtype entity [lk_cardtype_createdby](cardtype.md#BKMK_lk_cardtype_createdby) Many-To-One relationship.

**ReferencingEntity**: cardtype<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_cardtype_createdby<br />
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


### <a name="BKMK_lk_cardtype_createdonbehalfby"></a> lk_cardtype_createdonbehalfby

Same as cardtype entity [lk_cardtype_createdonbehalfby](cardtype.md#BKMK_lk_cardtype_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: cardtype<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_cardtype_createdonbehalfby<br />
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


### <a name="BKMK_lk_cardtype_modifiedby"></a> lk_cardtype_modifiedby

Same as cardtype entity [lk_cardtype_modifiedby](cardtype.md#BKMK_lk_cardtype_modifiedby) Many-To-One relationship.

**ReferencingEntity**: cardtype<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_cardtype_modifiedby<br />
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


### <a name="BKMK_lk_cardtype_modifiedonbehalfby"></a> lk_cardtype_modifiedonbehalfby

Same as cardtype entity [lk_cardtype_modifiedonbehalfby](cardtype.md#BKMK_lk_cardtype_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: cardtype<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_cardtype_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_channelaccessprofile_createdby"></a> lk_channelaccessprofile_createdby

Same as channelaccessprofile entity [lk_channelaccessprofile_createdby](channelaccessprofile.md#BKMK_lk_channelaccessprofile_createdby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: channelaccessprofile_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_channelaccessprofile_createdonbehalfby"></a> lk_channelaccessprofile_createdonbehalfby

Same as channelaccessprofile entity [lk_channelaccessprofile_createdonbehalfby](channelaccessprofile.md#BKMK_lk_channelaccessprofile_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: channelaccessprofile_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_channelaccessprofile_modifiedby"></a> lk_channelaccessprofile_modifiedby

Same as channelaccessprofile entity [lk_channelaccessprofile_modifiedby](channelaccessprofile.md#BKMK_lk_channelaccessprofile_modifiedby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: channelaccessprofile_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_channelaccessprofile_modifiedonbehalfby"></a> lk_channelaccessprofile_modifiedonbehalfby

Same as channelaccessprofile entity [lk_channelaccessprofile_modifiedonbehalfby](channelaccessprofile.md#BKMK_lk_channelaccessprofile_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: channelaccessprofile_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_channelaccessprofile"></a> user_channelaccessprofile

Same as channelaccessprofile entity [user_channelaccessprofile](channelaccessprofile.md#BKMK_user_channelaccessprofile) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_channelaccessprofile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_externalparty_createdby"></a> lk_externalparty_createdby

Same as externalparty entity [lk_externalparty_createdby](externalparty.md#BKMK_lk_externalparty_createdby) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_externalparty_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_externalparty_createdonbehalfby"></a> lk_externalparty_createdonbehalfby

Same as externalparty entity [lk_externalparty_createdonbehalfby](externalparty.md#BKMK_lk_externalparty_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_externalparty_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_externalparty_modifiedby"></a> lk_externalparty_modifiedby

Same as externalparty entity [lk_externalparty_modifiedby](externalparty.md#BKMK_lk_externalparty_modifiedby) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_externalparty_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_externalparty_modifiedonbehalfby"></a> lk_externalparty_modifiedonbehalfby

Same as externalparty entity [lk_externalparty_modifiedonbehalfby](externalparty.md#BKMK_lk_externalparty_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_externalparty_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_externalparty"></a> user_externalparty

Same as externalparty entity [user_externalparty](externalparty.md#BKMK_user_externalparty) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_user_externalparty<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_solution_createdby"></a> lk_solution_createdby

Same as solution entity [lk_solution_createdby](solution.md#BKMK_lk_solution_createdby) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_solution_createdby<br />
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


### <a name="BKMK_lk_solution_modifiedby"></a> lk_solution_modifiedby

Same as solution entity [lk_solution_modifiedby](solution.md#BKMK_lk_solution_modifiedby) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_solution_modifiedby<br />
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


### <a name="BKMK_lk_publisher_createdby"></a> lk_publisher_createdby

Same as publisher entity [lk_publisher_createdby](publisher.md#BKMK_lk_publisher_createdby) Many-To-One relationship.

**ReferencingEntity**: publisher<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisher_createdby<br />
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


### <a name="BKMK_lk_publisher_modifiedby"></a> lk_publisher_modifiedby

Same as publisher entity [lk_publisher_modifiedby](publisher.md#BKMK_lk_publisher_modifiedby) Many-To-One relationship.

**ReferencingEntity**: publisher<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisher_modifiedby<br />
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


### <a name="BKMK_lk_officegraphdocument_createdonbehalfby"></a> lk_officegraphdocument_createdonbehalfby

Same as officegraphdocument entity [lk_officegraphdocument_createdonbehalfby](officegraphdocument.md#BKMK_lk_officegraphdocument_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: officegraphdocument<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_officegraphdocument_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_officegraphdocument_modifiedonbehalfby"></a> lk_officegraphdocument_modifiedonbehalfby

Same as officegraphdocument entity [lk_officegraphdocument_modifiedonbehalfby](officegraphdocument.md#BKMK_lk_officegraphdocument_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: officegraphdocument<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_officegraphdocument_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profilerule_createdby"></a> lk_profilerule_createdby

Same as channelaccessprofilerule entity [lk_profilerule_createdby](channelaccessprofilerule.md#BKMK_lk_profilerule_createdby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profilerule_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profilerule_createdonbehalfby"></a> lk_profilerule_createdonbehalfby

Same as channelaccessprofilerule entity [lk_profilerule_createdonbehalfby](channelaccessprofilerule.md#BKMK_lk_profilerule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profilerule_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profilerule_modifiedby"></a> lk_profilerule_modifiedby

Same as channelaccessprofilerule entity [lk_profilerule_modifiedby](channelaccessprofilerule.md#BKMK_lk_profilerule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profilerule_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profilerule_modifiedonbehalfby"></a> lk_profilerule_modifiedonbehalfby

Same as channelaccessprofilerule entity [lk_profilerule_modifiedonbehalfby](channelaccessprofilerule.md#BKMK_lk_profilerule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profilerule_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_profilerule"></a> user_profilerule

Same as channelaccessprofilerule entity [user_profilerule](channelaccessprofilerule.md#BKMK_user_profilerule) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_profilerule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profileruleitem_createdby"></a> lk_profileruleitem_createdby

Same as channelaccessprofileruleitem entity [lk_profileruleitem_createdby](channelaccessprofileruleitem.md#BKMK_lk_profileruleitem_createdby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofileruleitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profileruleitem_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profileruleitem_createdonbehalfby"></a> lk_profileruleitem_createdonbehalfby

Same as channelaccessprofileruleitem entity [lk_profileruleitem_createdonbehalfby](channelaccessprofileruleitem.md#BKMK_lk_profileruleitem_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofileruleitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profileruleitem_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profileruleitem_modifiedby"></a> lk_profileruleitem_modifiedby

Same as channelaccessprofileruleitem entity [lk_profileruleitem_modifiedby](channelaccessprofileruleitem.md#BKMK_lk_profileruleitem_modifiedby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofileruleitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profileruleitem_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_profileruleitem_modifiedonbehalfby"></a> lk_profileruleitem_modifiedonbehalfby

Same as channelaccessprofileruleitem entity [lk_profileruleitem_modifiedonbehalfby](channelaccessprofileruleitem.md#BKMK_lk_profileruleitem_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofileruleitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_profileruleitem_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_delveactionhub_createdby"></a> lk_delveactionhub_createdby

Same as delveactionhub entity [lk_delveactionhub_createdby](delveactionhub.md#BKMK_lk_delveactionhub_createdby) Many-To-One relationship.

**ReferencingEntity**: delveactionhub<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_delveactionhub_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_delveactionhub_createdonbehalfby"></a> lk_delveactionhub_createdonbehalfby

Same as delveactionhub entity [lk_delveactionhub_createdonbehalfby](delveactionhub.md#BKMK_lk_delveactionhub_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: delveactionhub<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_delveactionhub_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_delveactionhub_modifiedby"></a> lk_delveactionhub_modifiedby

Same as delveactionhub entity [lk_delveactionhub_modifiedby](delveactionhub.md#BKMK_lk_delveactionhub_modifiedby) Many-To-One relationship.

**ReferencingEntity**: delveactionhub<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_delveactionhub_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_delveactionhub_modifiedonbehalfby"></a> lk_delveactionhub_modifiedonbehalfby

Same as delveactionhub entity [lk_delveactionhub_modifiedonbehalfby](delveactionhub.md#BKMK_lk_delveactionhub_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: delveactionhub<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_delveactionhub_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_recommendeddocument_createdby"></a> lk_recommendeddocument_createdby

Same as recommendeddocument entity [lk_recommendeddocument_createdby](recommendeddocument.md#BKMK_lk_recommendeddocument_createdby) Many-To-One relationship.

**ReferencingEntity**: recommendeddocument<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recommendeddocument_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_recommendeddocument_createdonbehalfby"></a> lk_recommendeddocument_createdonbehalfby

Same as recommendeddocument entity [lk_recommendeddocument_createdonbehalfby](recommendeddocument.md#BKMK_lk_recommendeddocument_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: recommendeddocument<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recommendeddocument_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_recommendeddocument_modifiedby"></a> lk_recommendeddocument_modifiedby

Same as recommendeddocument entity [lk_recommendeddocument_modifiedby](recommendeddocument.md#BKMK_lk_recommendeddocument_modifiedby) Many-To-One relationship.

**ReferencingEntity**: recommendeddocument<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recommendeddocument_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_recommendeddocument_modifiedonbehalfby"></a> lk_recommendeddocument_modifiedonbehalfby

Same as recommendeddocument entity [lk_recommendeddocument_modifiedonbehalfby](recommendeddocument.md#BKMK_lk_recommendeddocument_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: recommendeddocument<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recommendeddocument_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_KnowledgeBaseRecord_createdby"></a> lk_KnowledgeBaseRecord_createdby

Same as knowledgebaserecord entity [lk_KnowledgeBaseRecord_createdby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_createdby) Many-To-One relationship.

**ReferencingEntity**: knowledgebaserecord<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_KnowledgeBaseRecord_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_KnowledgeBaseRecord_createdonbehalfby"></a> lk_KnowledgeBaseRecord_createdonbehalfby

Same as knowledgebaserecord entity [lk_KnowledgeBaseRecord_createdonbehalfby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgebaserecord<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_KnowledgeBaseRecord_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedby"></a> lk_KnowledgeBaseRecord_modifiedby

Same as knowledgebaserecord entity [lk_KnowledgeBaseRecord_modifiedby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_modifiedby) Many-To-One relationship.

**ReferencingEntity**: knowledgebaserecord<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_KnowledgeBaseRecord_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby"></a> lk_KnowledgeBaseRecord_modifiedonbehalfby

Same as knowledgebaserecord entity [lk_KnowledgeBaseRecord_modifiedonbehalfby](knowledgebaserecord.md#BKMK_lk_KnowledgeBaseRecord_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgebaserecord<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_KnowledgeBaseRecord_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_externalpartyitem_createdonbehalfby"></a> lk_externalpartyitem_createdonbehalfby

Same as externalpartyitem entity [lk_externalpartyitem_createdonbehalfby](externalpartyitem.md#BKMK_lk_externalpartyitem_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: externalpartyitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_externalpartyitem_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_lookupmapping_modifiedby"></a> lk_lookupmapping_modifiedby

Same as lookupmapping entity [lk_lookupmapping_modifiedby](lookupmapping.md#BKMK_lk_lookupmapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: lookupmapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_lookupmapping_modifiedby<br />
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


### <a name="BKMK_lk_relationshiprole_createdonbehalfby"></a> lk_relationshiprole_createdonbehalfby

Same as relationshiprole entity [lk_relationshiprole_createdonbehalfby](relationshiprole.md#BKMK_lk_relationshiprole_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: relationshiprole<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_relationshiprole_createdonbehalfby<br />
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


### <a name="BKMK_lk_usersettings_createdonbehalfby"></a> lk_usersettings_createdonbehalfby

Same as usersettings entity [lk_usersettings_createdonbehalfby](usersettings.md#BKMK_lk_usersettings_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_usersettings_createdonbehalfby<br />
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


### <a name="BKMK_lk_kbarticletemplatebase_modifiedby"></a> lk_kbarticletemplatebase_modifiedby

Same as kbarticletemplate entity [lk_kbarticletemplatebase_modifiedby](kbarticletemplate.md#BKMK_lk_kbarticletemplatebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: kbarticletemplate<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticletemplatebase_modifiedby<br />
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


### <a name="BKMK_lk_fax_modifiedby"></a> lk_fax_modifiedby

Same as fax entity [lk_fax_modifiedby](fax.md#BKMK_lk_fax_modifiedby) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_fax_modifiedby<br />
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


### <a name="BKMK_lk_processsession_completedby"></a> lk_processsession_completedby

Same as processsession entity [lk_processsession_completedby](processsession.md#BKMK_lk_processsession_completedby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: completedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_completedby<br />
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


### <a name="BKMK_modifiedby_sdkmessageprocessingstepsecureconfig"></a> modifiedby_sdkmessageprocessingstepsecureconfig

Same as sdkmessageprocessingstepsecureconfig entity [modifiedby_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_modifiedby_sdkmessageprocessingstepsecureconfig) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepsecureconfig<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessageprocessingstepsecureconfig<br />
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


### <a name="BKMK_lk_businessunit_createdonbehalfby"></a> lk_businessunit_createdonbehalfby

Same as businessunit entity [lk_businessunit_createdonbehalfby](businessunit.md#BKMK_lk_businessunit_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunit_createdonbehalfby<br />
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


### <a name="BKMK_lk_duplicaterule_createdonbehalfby"></a> lk_duplicaterule_createdonbehalfby

Same as duplicaterule entity [lk_duplicaterule_createdonbehalfby](duplicaterule.md#BKMK_lk_duplicaterule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicaterule_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessagepair_createdonbehalfby"></a> lk_sdkmessagepair_createdonbehalfby

Same as sdkmessagepair entity [lk_sdkmessagepair_createdonbehalfby](sdkmessagepair.md#BKMK_lk_sdkmessagepair_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagepair<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagepair_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessage_modifiedonbehalfby"></a> lk_sdkmessage_modifiedonbehalfby

Same as sdkmessage entity [lk_sdkmessage_modifiedonbehalfby](sdkmessage.md#BKMK_lk_sdkmessage_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessage<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessage_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_translationprocess_modifiedonbehalfby"></a> lk_translationprocess_modifiedonbehalfby

Same as translationprocess entity [lk_translationprocess_modifiedonbehalfby](translationprocess.md#BKMK_lk_translationprocess_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_translationprocess_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_actioncardbase_createdonbehalfby"></a> lk_actioncardbase_createdonbehalfby

Same as actioncard entity [lk_actioncardbase_createdonbehalfby](actioncard.md#BKMK_lk_actioncardbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_actioncardbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessagefilter_createdonbehalfby"></a> lk_sdkmessagefilter_createdonbehalfby

Same as sdkmessagefilter entity [lk_sdkmessagefilter_createdonbehalfby](sdkmessagefilter.md#BKMK_lk_sdkmessagefilter_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagefilter<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagefilter_createdonbehalfby<br />
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


### <a name="BKMK_lk_slabase_modifiedonbehalfby"></a> lk_slabase_modifiedonbehalfby

Same as sla entity [lk_slabase_modifiedonbehalfby](sla.md#BKMK_lk_slabase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slabase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_feedback_modifiedby"></a> lk_feedback_modifiedby

Same as feedback entity [lk_feedback_modifiedby](feedback.md#BKMK_lk_feedback_modifiedby) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_feedback_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_templatebase_modifiedby"></a> lk_templatebase_modifiedby

Same as template entity [lk_templatebase_modifiedby](template.md#BKMK_lk_templatebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_templatebase_modifiedby<br />
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


### <a name="BKMK_createdby_relationship_role_map"></a> createdby_relationship_role_map

Same as relationshiprolemap entity [createdby_relationship_role_map](relationshiprolemap.md#BKMK_createdby_relationship_role_map) Many-To-One relationship.

**ReferencingEntity**: relationshiprolemap<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_relationship_role_map<br />
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


### <a name="BKMK_lk_azureserviceconnection_modifiedonbehalfby"></a> lk_azureserviceconnection_modifiedonbehalfby

Same as azureserviceconnection entity [lk_azureserviceconnection_modifiedonbehalfby](azureserviceconnection.md#BKMK_lk_azureserviceconnection_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: azureserviceconnection<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_azureserviceconnection_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_kbarticletemplate_modifiedonbehalfby"></a> lk_kbarticletemplate_modifiedonbehalfby

Same as kbarticletemplate entity [lk_kbarticletemplate_modifiedonbehalfby](kbarticletemplate.md#BKMK_lk_kbarticletemplate_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: kbarticletemplate<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticletemplate_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_slakpiinstancebase_createdby"></a> lk_slakpiinstancebase_createdby

Same as slakpiinstance entity [lk_slakpiinstancebase_createdby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_createdby) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slakpiinstancebase_createdby<br />
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


### <a name="BKMK_lk_convertruleitembase_createdby"></a> lk_convertruleitembase_createdby

Same as convertruleitem entity [lk_convertruleitembase_createdby](convertruleitem.md#BKMK_lk_convertruleitembase_createdby) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_convertruleitembase_createdby<br />
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


### <a name="BKMK_lk_ChannelProperty_modifiedby"></a> lk_ChannelProperty_modifiedby

Same as channelproperty entity [lk_ChannelProperty_modifiedby](channelproperty.md#BKMK_lk_ChannelProperty_modifiedby) Many-To-One relationship.

**ReferencingEntity**: channelproperty<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelProperty_modifiedby<br />
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


### <a name="BKMK_lk_ACIViewMapper_createdby"></a> lk_ACIViewMapper_createdby

Same as aciviewmapper entity [lk_ACIViewMapper_createdby](aciviewmapper.md#BKMK_lk_ACIViewMapper_createdby) Many-To-One relationship.

**ReferencingEntity**: aciviewmapper<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ACIViewMapper_createdby<br />
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


### <a name="BKMK_lk_azureserviceconnection_createdonbehalfby"></a> lk_azureserviceconnection_createdonbehalfby

Same as azureserviceconnection entity [lk_azureserviceconnection_createdonbehalfby](azureserviceconnection.md#BKMK_lk_azureserviceconnection_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: azureserviceconnection<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_azureserviceconnection_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_ChannelPropertyGroup_modifiedonbehalfby"></a> lk_ChannelPropertyGroup_modifiedonbehalfby

Same as channelpropertygroup entity [lk_ChannelPropertyGroup_modifiedonbehalfby](channelpropertygroup.md#BKMK_lk_ChannelPropertyGroup_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelpropertygroup<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelPropertyGroup_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_userqueryvisualization_modifiedby"></a> lk_userqueryvisualization_modifiedby

Same as userqueryvisualization entity [lk_userqueryvisualization_modifiedby](userqueryvisualization.md#BKMK_lk_userqueryvisualization_modifiedby) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userqueryvisualization_modifiedby<br />
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


### <a name="BKMK_lk_recurringappointmentmaster_createdonbehalfby"></a> lk_recurringappointmentmaster_createdonbehalfby

Same as recurringappointmentmaster entity [lk_recurringappointmentmaster_createdonbehalfby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recurringappointmentmaster_createdonbehalfby<br />
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


### <a name="BKMK_lk_businessprocessflowinstancebase_createdonbehalfby"></a> lk_businessprocessflowinstancebase_createdonbehalfby

Same as businessprocessflowinstance entity [lk_businessprocessflowinstancebase_createdonbehalfby](businessprocessflowinstance.md#BKMK_lk_businessprocessflowinstancebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: businessprocessflowinstance<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessprocessflowinstancebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_lookupmapping_createdonbehalfby"></a> lk_lookupmapping_createdonbehalfby

Same as lookupmapping entity [lk_lookupmapping_createdonbehalfby](lookupmapping.md#BKMK_lk_lookupmapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: lookupmapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_lookupmapping_createdonbehalfby<br />
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


### <a name="BKMK_lk_MobileOfflineProfileItem_createdby"></a> lk_MobileOfflineProfileItem_createdby

Same as mobileofflineprofileitem entity [lk_MobileOfflineProfileItem_createdby](mobileofflineprofileitem.md#BKMK_lk_MobileOfflineProfileItem_createdby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_MobileOfflineProfileItem_createdby<br />
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


### <a name="BKMK_lk_sdkmessageresponsefield_createdonbehalfby"></a> lk_sdkmessageresponsefield_createdonbehalfby

Same as sdkmessageresponsefield entity [lk_sdkmessageresponsefield_createdonbehalfby](sdkmessageresponsefield.md#BKMK_lk_sdkmessageresponsefield_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponsefield<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageresponsefield_createdonbehalfby<br />
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


### <a name="BKMK_lk_recurringappointmentmaster_modifiedby"></a> lk_recurringappointmentmaster_modifiedby

Same as recurringappointmentmaster entity [lk_recurringappointmentmaster_modifiedby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_modifiedby) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recurringappointmentmaster_modifiedby<br />
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


### <a name="BKMK_lk_fax_createdby"></a> lk_fax_createdby

Same as fax entity [lk_fax_createdby](fax.md#BKMK_lk_fax_createdby) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_fax_createdby<br />
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


### <a name="BKMK_lk_ConvertRule_createdonbehalfby"></a> lk_ConvertRule_createdonbehalfby

Same as convertrule entity [lk_ConvertRule_createdonbehalfby](convertrule.md#BKMK_lk_ConvertRule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ConvertRule_createdonbehalfby<br />
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


### <a name="BKMK_lk_letter_modifiedonbehalfby"></a> lk_letter_modifiedonbehalfby

Same as letter entity [lk_letter_modifiedonbehalfby](letter.md#BKMK_lk_letter_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_letter_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_transformationmapping_createdby"></a> lk_transformationmapping_createdby

Same as transformationmapping entity [lk_transformationmapping_createdby](transformationmapping.md#BKMK_lk_transformationmapping_createdby) Many-To-One relationship.

**ReferencingEntity**: transformationmapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationmapping_createdby<br />
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


### <a name="BKMK_lk_entitymap_modifiedonbehalfby"></a> lk_entitymap_modifiedonbehalfby

Same as entitymap entity [lk_entitymap_modifiedonbehalfby](entitymap.md#BKMK_lk_entitymap_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: entitymap<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_entitymap_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_reportcategorybase_createdby"></a> lk_reportcategorybase_createdby

Same as reportcategory entity [lk_reportcategorybase_createdby](reportcategory.md#BKMK_lk_reportcategorybase_createdby) Many-To-One relationship.

**ReferencingEntity**: reportcategory<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_reportcategorybase_createdby<br />
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


### <a name="BKMK_lk_letter_createdby"></a> lk_letter_createdby

Same as letter entity [lk_letter_createdby](letter.md#BKMK_lk_letter_createdby) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_letter_createdby<br />
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


### <a name="BKMK_lk_customcontrolresource_modifiedby"></a> lk_customcontrolresource_modifiedby

Same as customcontrolresource entity [lk_customcontrolresource_modifiedby](customcontrolresource.md#BKMK_lk_customcontrolresource_modifiedby) Many-To-One relationship.

**ReferencingEntity**: customcontrolresource<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrolresource_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_expiredprocess_createdonbehalfby"></a> lk_expiredprocess_createdonbehalfby

Same as expiredprocess entity [lk_expiredprocess_createdonbehalfby](expiredprocess.md#BKMK_lk_expiredprocess_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_expiredprocess_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_actioncardusersettings_owning_user"></a> actioncardusersettings_owning_user

Same as actioncardusersettings entity [actioncardusersettings_owning_user](actioncardusersettings.md#BKMK_actioncardusersettings_owning_user) Many-To-One relationship.

**ReferencingEntity**: actioncardusersettings<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: actioncardusersettings_owning_user<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_createdby_customer_relationship"></a> createdby_customer_relationship

Same as customerrelationship entity [createdby_customer_relationship](customerrelationship.md#BKMK_createdby_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_customer_relationship<br />
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


### <a name="BKMK_lk_reportentity_createdonbehalfby"></a> lk_reportentity_createdonbehalfby

Same as reportentity entity [lk_reportentity_createdonbehalfby](reportentity.md#BKMK_lk_reportentity_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportentity<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportentity_createdonbehalfby<br />
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


### <a name="BKMK_lk_routingrule_createdby"></a> lk_routingrule_createdby

Same as routingrule entity [lk_routingrule_createdby](routingrule.md#BKMK_lk_routingrule_createdby) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingrule_createdby<br />
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


### <a name="BKMK_workflow_dependency_createdby"></a> workflow_dependency_createdby

Same as workflowdependency entity [workflow_dependency_createdby](workflowdependency.md#BKMK_workflow_dependency_createdby) Many-To-One relationship.

**ReferencingEntity**: workflowdependency<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_dependency_createdby<br />
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


### <a name="BKMK_lk_appmodulecomponent_modifiedby"></a> lk_appmodulecomponent_modifiedby

Same as appmodulecomponent entity [lk_appmodulecomponent_modifiedby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_modifiedby) Many-To-One relationship.

**ReferencingEntity**: appmodulecomponent<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: appmodulecomponent_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_calendar_modifiedby"></a> lk_calendar_modifiedby

Same as calendar entity [lk_calendar_modifiedby](calendar.md#BKMK_lk_calendar_modifiedby) Many-To-One relationship.

**ReferencingEntity**: calendar<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_calendar_modifiedby<br />
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


### <a name="BKMK_lk_RoutingRuleItem_createdby"></a> lk_RoutingRuleItem_createdby

Same as routingruleitem entity [lk_RoutingRuleItem_createdby](routingruleitem.md#BKMK_lk_RoutingRuleItem_createdby) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_RoutingRuleItem_createdby<br />
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


### <a name="BKMK_SystemUser_DuplicateRules"></a> SystemUser_DuplicateRules

Same as duplicaterule entity [SystemUser_DuplicateRules](duplicaterule.md#BKMK_SystemUser_DuplicateRules) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_DuplicateRules<br />
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


### <a name="BKMK_lk_plugintype_createdonbehalfby"></a> lk_plugintype_createdonbehalfby

Same as plugintype entity [lk_plugintype_createdonbehalfby](plugintype.md#BKMK_lk_plugintype_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: plugintype<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_plugintype_createdonbehalfby<br />
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


### <a name="BKMK_lk_routingrule_modifiedby"></a> lk_routingrule_modifiedby

Same as routingrule entity [lk_routingrule_modifiedby](routingrule.md#BKMK_lk_routingrule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingrule_modifiedby<br />
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


### <a name="BKMK_lk_mobileofflineprofileitem_createdonbehalfby"></a> lk_mobileofflineprofileitem_createdonbehalfby

Same as mobileofflineprofileitem entity [lk_mobileofflineprofileitem_createdonbehalfby](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mobileofflineprofileitem_createdonbehalfby<br />
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


### <a name="BKMK_lk_fax_createdonbehalfby"></a> lk_fax_createdonbehalfby

Same as fax entity [lk_fax_createdonbehalfby](fax.md#BKMK_lk_fax_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_fax_createdonbehalfby<br />
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


### <a name="BKMK_lk_timezonedefinition_modifiedby"></a> lk_timezonedefinition_modifiedby

Same as timezonedefinition entity [lk_timezonedefinition_modifiedby](timezonedefinition.md#BKMK_lk_timezonedefinition_modifiedby) Many-To-One relationship.

**ReferencingEntity**: timezonedefinition<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonedefinition_modifiedby<br />
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


### <a name="BKMK_lk_reportvisibilitybase_modifiedby"></a> lk_reportvisibilitybase_modifiedby

Same as reportvisibility entity [lk_reportvisibilitybase_modifiedby](reportvisibility.md#BKMK_lk_reportvisibilitybase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: reportvisibility<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportvisibilitybase_modifiedby<br />
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


### <a name="BKMK_lk_columnmapping_createdby"></a> lk_columnmapping_createdby

Same as columnmapping entity [lk_columnmapping_createdby](columnmapping.md#BKMK_lk_columnmapping_createdby) Many-To-One relationship.

**ReferencingEntity**: columnmapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_columnmapping_createdby<br />
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


### <a name="BKMK_lk_reportcategorybase_modifiedby"></a> lk_reportcategorybase_modifiedby

Same as reportcategory entity [lk_reportcategorybase_modifiedby](reportcategory.md#BKMK_lk_reportcategorybase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: reportcategory<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_reportcategorybase_modifiedby<br />
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


### <a name="BKMK_lk_sharepointsitebase_createdonbehalfby"></a> lk_sharepointsitebase_createdonbehalfby

Same as sharepointsite entity [lk_sharepointsitebase_createdonbehalfby](sharepointsite.md#BKMK_lk_sharepointsitebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointsitebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_workflowlog_modifiedby"></a> lk_workflowlog_modifiedby

Same as workflowlog entity [lk_workflowlog_modifiedby](workflowlog.md#BKMK_lk_workflowlog_modifiedby) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_modifiedby<br />
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


### <a name="BKMK_lk_syncerrorbase_createdonbehalfby"></a> lk_syncerrorbase_createdonbehalfby

Same as syncerror entity [lk_syncerrorbase_createdonbehalfby](syncerror.md#BKMK_lk_syncerrorbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_syncerrorbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_bulkdeleteoperation_modifiedonbehalfby"></a> lk_bulkdeleteoperation_modifiedonbehalfby

Same as bulkdeleteoperation entity [lk_bulkdeleteoperation_modifiedonbehalfby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperation_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: bulkdeleteoperation<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_bulkdeleteoperation_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_serviceendpointbase_createdonbehalfby"></a> lk_serviceendpointbase_createdonbehalfby

Same as serviceendpoint entity [lk_serviceendpointbase_createdonbehalfby](serviceendpoint.md#BKMK_lk_serviceendpointbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: serviceendpoint<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_serviceendpointbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_solutioncomponentbase_createdonbehalfby"></a> lk_solutioncomponentbase_createdonbehalfby

Same as solutioncomponent entity [lk_solutioncomponentbase_createdonbehalfby](solutioncomponent.md#BKMK_lk_solutioncomponentbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: solutioncomponent<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_solutioncomponentbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_plugintype_modifiedonbehalfby"></a> lk_plugintype_modifiedonbehalfby

Same as plugintype entity [lk_plugintype_modifiedonbehalfby](plugintype.md#BKMK_lk_plugintype_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: plugintype<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_plugintype_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_lookupmapping_modifiedonbehalfby"></a> lk_lookupmapping_modifiedonbehalfby

Same as lookupmapping entity [lk_lookupmapping_modifiedonbehalfby](lookupmapping.md#BKMK_lk_lookupmapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: lookupmapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_lookupmapping_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_phonecall_modifiedby"></a> lk_phonecall_modifiedby

Same as phonecall entity [lk_phonecall_modifiedby](phonecall.md#BKMK_lk_phonecall_modifiedby) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_phonecall_modifiedby<br />
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


### <a name="BKMK_lk_slabase_modifiedby"></a> lk_slabase_modifiedby

Same as sla entity [lk_slabase_modifiedby](sla.md#BKMK_lk_slabase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slabase_modifiedby<br />
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


### <a name="BKMK_lk_workflowlog_modifiedonbehalfby"></a> lk_workflowlog_modifiedonbehalfby

Same as workflowlog entity [lk_workflowlog_modifiedonbehalfby](workflowlog.md#BKMK_lk_workflowlog_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_importfilebase_createdonbehalfby"></a> lk_importfilebase_createdonbehalfby

Same as importfile entity [lk_importfilebase_createdonbehalfby](importfile.md#BKMK_lk_importfilebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importfilebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_fieldsecurityprofile_createdonbehalfby"></a> lk_fieldsecurityprofile_createdonbehalfby

Same as fieldsecurityprofile entity [lk_fieldsecurityprofile_createdonbehalfby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: fieldsecurityprofile<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fieldsecurityprofile_createdonbehalfby<br />
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


### <a name="BKMK_lk_importmapbase_createdby"></a> lk_importmapbase_createdby

Same as importmap entity [lk_importmapbase_createdby](importmap.md#BKMK_lk_importmapbase_createdby) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importmapbase_createdby<br />
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


### <a name="BKMK_createdby_relationship_role"></a> createdby_relationship_role

Same as relationshiprole entity [createdby_relationship_role](relationshiprole.md#BKMK_createdby_relationship_role) Many-To-One relationship.

**ReferencingEntity**: relationshiprole<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_relationship_role<br />
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


### <a name="BKMK_lk_PostFollow_createdby"></a> lk_PostFollow_createdby

Same as postfollow entity [lk_PostFollow_createdby](postfollow.md#BKMK_lk_PostFollow_createdby) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_PostFollow_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_systemuser_PostFollows"></a> systemuser_PostFollows

Same as postfollow entity [systemuser_PostFollows](postfollow.md#BKMK_systemuser_PostFollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: systemuser_PostFollows<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_post_createdby"></a> lk_post_createdby

Same as post entity [lk_post_createdby](post.md#BKMK_lk_post_createdby) Many-To-One relationship.

**ReferencingEntity**: post<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_post_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_post_createdonbehalfby"></a> lk_post_createdonbehalfby

Same as post entity [lk_post_createdonbehalfby](post.md#BKMK_lk_post_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: post<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_post_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_post_modifiedby"></a> lk_post_modifiedby

Same as post entity [lk_post_modifiedby](post.md#BKMK_lk_post_modifiedby) Many-To-One relationship.

**ReferencingEntity**: post<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_post_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_postcomment_createdby"></a> lk_postcomment_createdby

Same as postcomment entity [lk_postcomment_createdby](postcomment.md#BKMK_lk_postcomment_createdby) Many-To-One relationship.

**ReferencingEntity**: postcomment<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_postcomment_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_owner_postfollows"></a> user_owner_postfollows

Same as postfollow entity [user_owner_postfollows](postfollow.md#BKMK_user_owner_postfollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_owner_postfollows<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_postfollow_createdonbehalfby"></a> lk_postfollow_createdonbehalfby

Same as postfollow entity [lk_postfollow_createdonbehalfby](postfollow.md#BKMK_lk_postfollow_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_postfollow_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_postcomment_createdonbehalfby"></a> lk_postcomment_createdonbehalfby

Same as postcomment entity [lk_postcomment_createdonbehalfby](postcomment.md#BKMK_lk_postcomment_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: postcomment<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_postcomment_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_postlike_createdonbehalfby"></a> lk_postlike_createdonbehalfby

Same as postlike entity [lk_postlike_createdonbehalfby](postlike.md#BKMK_lk_postlike_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: postlike<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_postlike_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_postlike_createdby"></a> lk_postlike_createdby

Same as postlike entity [lk_postlike_createdby](postlike.md#BKMK_lk_postlike_createdby) Many-To-One relationship.

**ReferencingEntity**: postlike<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_postlike_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_queueitem_modifiedonbehalfby"></a> lk_queueitem_modifiedonbehalfby

Same as queueitem entity [lk_queueitem_modifiedonbehalfby](queueitem.md#BKMK_lk_queueitem_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queueitem_modifiedonbehalfby<br />
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


### <a name="BKMK_user_socialactivity"></a> user_socialactivity

Same as socialactivity entity [user_socialactivity](socialactivity.md#BKMK_user_socialactivity) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_socialactivity<br />
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


### <a name="BKMK_lk_translationprocess_createdonbehalfby"></a> lk_translationprocess_createdonbehalfby

Same as translationprocess entity [lk_translationprocess_createdonbehalfby](translationprocess.md#BKMK_lk_translationprocess_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_translationprocess_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby

Same as sdkmessageprocessingstepsecureconfig entity [lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby](sdkmessageprocessingstepsecureconfig.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepsecureconfig<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageprocessingstepsecureconfig_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_feedback_modifiedonbehalfby"></a> lk_feedback_modifiedonbehalfby

Same as feedback entity [lk_feedback_modifiedonbehalfby](feedback.md#BKMK_lk_feedback_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_feedback_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_workflowlog_createdonbehalfby"></a> lk_workflowlog_createdonbehalfby

Same as workflowlog entity [lk_workflowlog_createdonbehalfby](workflowlog.md#BKMK_lk_workflowlog_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_createdonbehalfby<br />
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


### <a name="BKMK_lk_role_createdonbehalfby"></a> lk_role_createdonbehalfby

Same as role entity [lk_role_createdonbehalfby](role.md#BKMK_lk_role_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: role<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_role_createdonbehalfby<br />
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


### <a name="BKMK_lk_transactioncurrency_modifiedonbehalfby"></a> lk_transactioncurrency_modifiedonbehalfby

Same as transactioncurrency entity [lk_transactioncurrency_modifiedonbehalfby](transactioncurrency.md#BKMK_lk_transactioncurrency_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: transactioncurrency<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transactioncurrency_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_rolebase_modifiedby"></a> lk_rolebase_modifiedby

Same as role entity [lk_rolebase_modifiedby](role.md#BKMK_lk_rolebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: role<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_rolebase_modifiedby<br />
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


### <a name="BKMK_lk_navigationsetting_createdby"></a> lk_navigationsetting_createdby

Same as navigationsetting entity [lk_navigationsetting_createdby](navigationsetting.md#BKMK_lk_navigationsetting_createdby) Many-To-One relationship.

**ReferencingEntity**: navigationsetting<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_navigationsetting_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_subject_modifiedonbehalfby"></a> lk_subject_modifiedonbehalfby

Same as subject entity [lk_subject_modifiedonbehalfby](subject.md#BKMK_lk_subject_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: subject<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_subject_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_duplicaterule_modifiedonbehalfby"></a> lk_duplicaterule_modifiedonbehalfby

Same as duplicaterule entity [lk_duplicaterule_modifiedonbehalfby](duplicaterule.md#BKMK_lk_duplicaterule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicaterule_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_task_modifiedonbehalfby"></a> lk_task_modifiedonbehalfby

Same as task entity [lk_task_modifiedonbehalfby](task.md#BKMK_lk_task_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_task_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_subjectbase_modifiedby"></a> lk_subjectbase_modifiedby

Same as subject entity [lk_subjectbase_modifiedby](subject.md#BKMK_lk_subjectbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: subject<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_subjectbase_modifiedby<br />
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


### <a name="BKMK_lk_relationshiprole_modifiedonbehalfby"></a> lk_relationshiprole_modifiedonbehalfby

Same as relationshiprole entity [lk_relationshiprole_modifiedonbehalfby](relationshiprole.md#BKMK_lk_relationshiprole_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: relationshiprole<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_relationshiprole_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_mailboxtrackingfolder_modifiedby"></a> lk_mailboxtrackingfolder_modifiedby

Same as mailboxtrackingfolder entity [lk_mailboxtrackingfolder_modifiedby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_modifiedby) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailboxtrackingfolder_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_sdkmessageresponsefield_modifiedonbehalfby"></a> lk_sdkmessageresponsefield_modifiedonbehalfby

Same as sdkmessageresponsefield entity [lk_sdkmessageresponsefield_modifiedonbehalfby](sdkmessageresponsefield.md#BKMK_lk_sdkmessageresponsefield_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponsefield<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageresponsefield_modifiedonbehalfby<br />
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


### <a name="BKMK_modifiedby_sdkmessageresponse"></a> modifiedby_sdkmessageresponse

Same as sdkmessageresponse entity [modifiedby_sdkmessageresponse](sdkmessageresponse.md#BKMK_modifiedby_sdkmessageresponse) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponse<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessageresponse<br />
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


### <a name="BKMK_impersonatinguserid_sdkmessageprocessingstep"></a> impersonatinguserid_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [impersonatinguserid_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_impersonatinguserid_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: impersonatinguserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: impersonatinguserid_sdkmessageprocessingstep<br />
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


### <a name="BKMK_lk_kbarticle_createdonbehalfby"></a> lk_kbarticle_createdonbehalfby

Same as kbarticle entity [lk_kbarticle_createdonbehalfby](kbarticle.md#BKMK_lk_kbarticle_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: kbarticle<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticle_createdonbehalfby<br />
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


### <a name="BKMK_lk_calendar_createdonbehalfby"></a> lk_calendar_createdonbehalfby

Same as calendar entity [lk_calendar_createdonbehalfby](calendar.md#BKMK_lk_calendar_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: calendar<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_calendar_createdonbehalfby<br />
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


### <a name="BKMK_lk_businessunitnewsarticlebase_modifiedby"></a> lk_businessunitnewsarticlebase_modifiedby

Same as businessunitnewsarticle entity [lk_businessunitnewsarticlebase_modifiedby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticlebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: businessunitnewsarticle<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunitnewsarticlebase_modifiedby<br />
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


### <a name="BKMK_createdby_expanderevent"></a> createdby_expanderevent

Same as expanderevent entity [createdby_expanderevent](expanderevent.md#BKMK_createdby_expanderevent) Many-To-One relationship.

**ReferencingEntity**: expanderevent<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_expanderevent<br />
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


### <a name="BKMK_userentityinstancedata_systemuser"></a> userentityinstancedata_systemuser

Same as userentityinstancedata entity [userentityinstancedata_systemuser](userentityinstancedata.md#BKMK_userentityinstancedata_systemuser) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_systemuser<br />
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


### <a name="BKMK_user_userqueryvisualizations"></a> user_userqueryvisualizations

Same as userqueryvisualization entity [user_userqueryvisualizations](userqueryvisualization.md#BKMK_user_userqueryvisualizations) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_userqueryvisualizations<br />
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


### <a name="BKMK_lk_tracelog_createdonbehalfby"></a> lk_tracelog_createdonbehalfby

Same as tracelog entity [lk_tracelog_createdonbehalfby](tracelog.md#BKMK_lk_tracelog_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_tracelog_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_queueitembase_workerid"></a> lk_queueitembase_workerid

Same as queueitem entity [lk_queueitembase_workerid](queueitem.md#BKMK_lk_queueitembase_workerid) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: workerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queueitembase_workerid<br />
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


### <a name="BKMK_modifiedonbehalfby_attributemap"></a> modifiedonbehalfby_attributemap

Same as attributemap entity [modifiedonbehalfby_attributemap](attributemap.md#BKMK_modifiedonbehalfby_attributemap) Many-To-One relationship.

**ReferencingEntity**: attributemap<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedonbehalfby_attributemap<br />
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


### <a name="BKMK_lk_mobileofflineprofileitem_modifiedby"></a> lk_mobileofflineprofileitem_modifiedby

Same as mobileofflineprofileitem entity [lk_mobileofflineprofileitem_modifiedby](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_modifiedby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mobileofflineprofileitem_modifiedby<br />
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


### <a name="BKMK_lk_customeraddressbase_modifiedby"></a> lk_customeraddressbase_modifiedby

Same as customeraddress entity [lk_customeraddressbase_modifiedby](customeraddress.md#BKMK_lk_customeraddressbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: customeraddress<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_customeraddressbase_modifiedby<br />
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


### <a name="BKMK_lk_activitypointer_modifiedby"></a> lk_activitypointer_modifiedby

Same as activitypointer entity [lk_activitypointer_modifiedby](activitypointer.md#BKMK_lk_activitypointer_modifiedby) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_activitypointer_modifiedby<br />
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


### <a name="BKMK_lk_customeraddressbase_createdby"></a> lk_customeraddressbase_createdby

Same as customeraddress entity [lk_customeraddressbase_createdby](customeraddress.md#BKMK_lk_customeraddressbase_createdby) Many-To-One relationship.

**ReferencingEntity**: customeraddress<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_customeraddressbase_createdby<br />
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


### <a name="BKMK_createdby_sdkmessageresponse"></a> createdby_sdkmessageresponse

Same as sdkmessageresponse entity [createdby_sdkmessageresponse](sdkmessageresponse.md#BKMK_createdby_sdkmessageresponse) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponse<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessageresponse<br />
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


### <a name="BKMK_lk_syncerrorbase_modifiedonbehalfby"></a> lk_syncerrorbase_modifiedonbehalfby

Same as syncerror entity [lk_syncerrorbase_modifiedonbehalfby](syncerror.md#BKMK_lk_syncerrorbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_syncerrorbase_modifiedonbehalfby<br />
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


### <a name="BKMK_SystemUser_BulkDeleteFailures"></a> SystemUser_BulkDeleteFailures

Same as bulkdeletefailure entity [SystemUser_BulkDeleteFailures](bulkdeletefailure.md#BKMK_SystemUser_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_BulkDeleteFailures<br />
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


### <a name="BKMK_lk_teambase_modifiedby"></a> lk_teambase_modifiedby

Same as team entity [lk_teambase_modifiedby](team.md#BKMK_lk_teambase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_teambase_modifiedby<br />
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


### <a name="BKMK_workflow_createdby"></a> workflow_createdby

Same as workflow entity [workflow_createdby](workflow.md#BKMK_workflow_createdby) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_createdby<br />
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


### <a name="BKMK_lk_queue_modifiedonbehalfby"></a> lk_queue_modifiedonbehalfby

Same as queue entity [lk_queue_modifiedonbehalfby](queue.md#BKMK_lk_queue_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queue_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_customeraddress_modifiedonbehalfby"></a> lk_customeraddress_modifiedonbehalfby

Same as customeraddress entity [lk_customeraddress_modifiedonbehalfby](customeraddress.md#BKMK_lk_customeraddress_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customeraddress<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_customeraddress_modifiedonbehalfby<br />
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


### <a name="BKMK_workflow_dependency_createdonbehalfby"></a> workflow_dependency_createdonbehalfby

Same as workflowdependency entity [workflow_dependency_createdonbehalfby](workflowdependency.md#BKMK_workflow_dependency_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: workflowdependency<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_dependency_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_sdkmessagepair"></a> modifiedby_sdkmessagepair

Same as sdkmessagepair entity [modifiedby_sdkmessagepair](sdkmessagepair.md#BKMK_modifiedby_sdkmessagepair) Many-To-One relationship.

**ReferencingEntity**: sdkmessagepair<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessagepair<br />
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


### <a name="BKMK_lk_emailsignaturebase_modifiedby"></a> lk_emailsignaturebase_modifiedby

Same as emailsignature entity [lk_emailsignaturebase_modifiedby](emailsignature.md#BKMK_lk_emailsignaturebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: emailsignature<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_emailsignaturebase_modifiedby<br />
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


### <a name="BKMK_lk_rolebase_createdby"></a> lk_rolebase_createdby

Same as role entity [lk_rolebase_createdby](role.md#BKMK_lk_rolebase_createdby) Many-To-One relationship.

**ReferencingEntity**: role<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_rolebase_createdby<br />
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


### <a name="BKMK_lk_reportcategory_modifiedonbehalfby"></a> lk_reportcategory_modifiedonbehalfby

Same as reportcategory entity [lk_reportcategory_modifiedonbehalfby](reportcategory.md#BKMK_lk_reportcategory_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportcategory<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_reportcategory_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_transformationmapping_modifiedby"></a> lk_transformationmapping_modifiedby

Same as transformationmapping entity [lk_transformationmapping_modifiedby](transformationmapping.md#BKMK_lk_transformationmapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: transformationmapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationmapping_modifiedby<br />
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


### <a name="BKMK_lk_duplicaterulecondition_modifiedonbehalfby"></a> lk_duplicaterulecondition_modifiedonbehalfby

Same as duplicaterulecondition entity [lk_duplicaterulecondition_modifiedonbehalfby](duplicaterulecondition.md#BKMK_lk_duplicaterulecondition_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: duplicaterulecondition<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicaterulecondition_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_picklistmapping_createdby"></a> lk_picklistmapping_createdby

Same as picklistmapping entity [lk_picklistmapping_createdby](picklistmapping.md#BKMK_lk_picklistmapping_createdby) Many-To-One relationship.

**ReferencingEntity**: picklistmapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_picklistmapping_createdby<br />
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


### <a name="BKMK_lk_savedqueryvisualizationbase_modifiedby"></a> lk_savedqueryvisualizationbase_modifiedby

Same as savedqueryvisualization entity [lk_savedqueryvisualizationbase_modifiedby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: savedqueryvisualization<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedqueryvisualizationbase_modifiedby<br />
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


### <a name="BKMK_lk_kbarticlecommentbase_modifiedby"></a> lk_kbarticlecommentbase_modifiedby

Same as kbarticlecomment entity [lk_kbarticlecommentbase_modifiedby](kbarticlecomment.md#BKMK_lk_kbarticlecommentbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: kbarticlecomment<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticlecommentbase_modifiedby<br />
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


### <a name="BKMK_lk_email_modifiedonbehalfby"></a> lk_email_modifiedonbehalfby

Same as email entity [lk_email_modifiedonbehalfby](email.md#BKMK_lk_email_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_email_modifiedonbehalfby<br />
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


### <a name="BKMK_createdby_entitymap"></a> createdby_entitymap

Same as entitymap entity [createdby_entitymap](entitymap.md#BKMK_createdby_entitymap) Many-To-One relationship.

**ReferencingEntity**: entitymap<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_entitymap<br />
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


### <a name="BKMK_lk_asyncoperation_createdonbehalfby"></a> lk_asyncoperation_createdonbehalfby

Same as asyncoperation entity [lk_asyncoperation_createdonbehalfby](asyncoperation.md#BKMK_lk_asyncoperation_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_asyncoperation_createdonbehalfby<br />
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


### <a name="BKMK_lk_pluginassembly_modifiedonbehalfby"></a> lk_pluginassembly_modifiedonbehalfby

Same as pluginassembly entity [lk_pluginassembly_modifiedonbehalfby](pluginassembly.md#BKMK_lk_pluginassembly_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: pluginassembly<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_pluginassembly_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_team_createdonbehalfby"></a> lk_team_createdonbehalfby

Same as team entity [lk_team_createdonbehalfby](team.md#BKMK_lk_team_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_team_createdonbehalfby<br />
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


### <a name="BKMK_createdby_connection"></a> createdby_connection

Same as connection entity [createdby_connection](connection.md#BKMK_createdby_connection) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: createdby_connection<br />
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


### <a name="BKMK_workflow_modifiedby"></a> workflow_modifiedby

Same as workflow entity [workflow_modifiedby](workflow.md#BKMK_workflow_modifiedby) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_modifiedby<br />
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


### <a name="BKMK_lk_businessunitnewsarticle_createdonbehalfby"></a> lk_businessunitnewsarticle_createdonbehalfby

Same as businessunitnewsarticle entity [lk_businessunitnewsarticle_createdonbehalfby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticle_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: businessunitnewsarticle<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunitnewsarticle_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby"></a> lk_sdkmessageprocessingstepimage_modifiedonbehalfby

Same as sdkmessageprocessingstepimage entity [lk_sdkmessageprocessingstepimage_modifiedonbehalfby](sdkmessageprocessingstepimage.md#BKMK_lk_sdkmessageprocessingstepimage_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepimage<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageprocessingstepimage_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_processsessionbase_createdonbehalfby"></a> lk_processsessionbase_createdonbehalfby

Same as processsession entity [lk_processsessionbase_createdonbehalfby](processsession.md#BKMK_lk_processsessionbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsessionbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_appmodule_modifiedonbehalfby"></a> lk_appmodule_modifiedonbehalfby

Same as appmodule entity [lk_appmodule_modifiedonbehalfby](appmodule.md#BKMK_lk_appmodule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appmodule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appmodule_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_customcontroldefaultconfig_modifiedonbehalfby"></a> lk_customcontroldefaultconfig_modifiedonbehalfby

Same as customcontroldefaultconfig entity [lk_customcontroldefaultconfig_modifiedonbehalfby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customcontroldefaultconfig<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontroldefaultconfig_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_tracelog_modifiedby"></a> lk_tracelog_modifiedby

Same as tracelog entity [lk_tracelog_modifiedby](tracelog.md#BKMK_lk_tracelog_modifiedby) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_tracelog_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_appointment"></a> user_appointment

Same as appointment entity [user_appointment](appointment.md#BKMK_user_appointment) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_appointment<br />
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


### <a name="BKMK_lk_externalpartyitem_modifiedby"></a> lk_externalpartyitem_modifiedby

Same as externalpartyitem entity [lk_externalpartyitem_modifiedby](externalpartyitem.md#BKMK_lk_externalpartyitem_modifiedby) Many-To-One relationship.

**ReferencingEntity**: externalpartyitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_externalpartyitem_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_appconfig_createdonbehalfby"></a> lk_appconfig_createdonbehalfby

Same as appconfig entity [lk_appconfig_createdonbehalfby](appconfig.md#BKMK_lk_appconfig_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appconfig<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfig_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_appconfiginstance_createdonbehalfby"></a> lk_appconfiginstance_createdonbehalfby

Same as appconfiginstance entity [lk_appconfiginstance_createdonbehalfby](appconfiginstance.md#BKMK_lk_appconfiginstance_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appconfiginstance<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfiginstance_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_DisplayStringbase_modifiedby"></a> lk_DisplayStringbase_modifiedby

Same as displaystring entity [lk_DisplayStringbase_modifiedby](displaystring.md#BKMK_lk_DisplayStringbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: displaystring<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_DisplayStringbase_modifiedby<br />
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


### <a name="BKMK_lk_importlog_modifiedonbehalfby"></a> lk_importlog_modifiedonbehalfby

Same as importlog entity [lk_importlog_modifiedonbehalfby](importlog.md#BKMK_lk_importlog_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importlog_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_navigationsetting_modifiedby"></a> lk_navigationsetting_modifiedby

Same as navigationsetting entity [lk_navigationsetting_modifiedby](navigationsetting.md#BKMK_lk_navigationsetting_modifiedby) Many-To-One relationship.

**ReferencingEntity**: navigationsetting<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_navigationsetting_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_SystemUser_Email_EmailSender"></a> SystemUser_Email_EmailSender

Same as email entity [SystemUser_Email_EmailSender](email.md#BKMK_SystemUser_Email_EmailSender) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: emailsender<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_Email_EmailSender<br />
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


### <a name="BKMK_modifiedby_sdkmessagerequest"></a> modifiedby_sdkmessagerequest

Same as sdkmessagerequest entity [modifiedby_sdkmessagerequest](sdkmessagerequest.md#BKMK_modifiedby_sdkmessagerequest) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequest<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessagerequest<br />
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


### <a name="BKMK_user_activity"></a> user_activity

Same as activitypointer entity [user_activity](activitypointer.md#BKMK_user_activity) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_activity<br />
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


### <a name="BKMK_modifiedby_customer_relationship"></a> modifiedby_customer_relationship

Same as customerrelationship entity [modifiedby_customer_relationship](customerrelationship.md#BKMK_modifiedby_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_customer_relationship<br />
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


### <a name="BKMK_lk_ConvertRule_modifiedby"></a> lk_ConvertRule_modifiedby

Same as convertrule entity [lk_ConvertRule_modifiedby](convertrule.md#BKMK_lk_ConvertRule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ConvertRule_modifiedby<br />
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


### <a name="BKMK_lk_monthlyfiscalcalendar_salespersonid"></a> lk_monthlyfiscalcalendar_salespersonid

Same as monthlyfiscalcalendar entity [lk_monthlyfiscalcalendar_salespersonid](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_salespersonid) Many-To-One relationship.

**ReferencingEntity**: monthlyfiscalcalendar<br />
**ReferencingAttribute**: salespersonid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_monthlyfiscalcalendar_salespersonid<br />
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


### <a name="BKMK_SystemUser_ExternalPartyItems"></a> SystemUser_ExternalPartyItems

Same as externalpartyitem entity [SystemUser_ExternalPartyItems](externalpartyitem.md#BKMK_SystemUser_ExternalPartyItems) Many-To-One relationship.

**ReferencingEntity**: externalpartyitem<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_ExternalPartyItems<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_businessunit_modifiedonbehalfby"></a> lk_businessunit_modifiedonbehalfby

Same as businessunit entity [lk_businessunit_modifiedonbehalfby](businessunit.md#BKMK_lk_businessunit_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunit_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_asyncoperation_modifiedonbehalfby"></a> lk_asyncoperation_modifiedonbehalfby

Same as asyncoperation entity [lk_asyncoperation_modifiedonbehalfby](asyncoperation.md#BKMK_lk_asyncoperation_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_asyncoperation_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_teambase_createdby"></a> lk_teambase_createdby

Same as team entity [lk_teambase_createdby](team.md#BKMK_lk_teambase_createdby) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_teambase_createdby<br />
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


### <a name="BKMK_lk_emailserverprofile_modifiedby"></a> lk_emailserverprofile_modifiedby

Same as emailserverprofile entity [lk_emailserverprofile_modifiedby](emailserverprofile.md#BKMK_lk_emailserverprofile_modifiedby) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_emailserverprofile_modifiedby<br />
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


### <a name="BKMK_lk_processtriggerbase_modifiedonbehalfby"></a> lk_processtriggerbase_modifiedonbehalfby

Same as processtrigger entity [lk_processtriggerbase_modifiedonbehalfby](processtrigger.md#BKMK_lk_processtriggerbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: processtrigger<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processtriggerbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_mailmergetemplate_modifiedonbehalfby"></a> lk_mailmergetemplate_modifiedonbehalfby

Same as mailmergetemplate entity [lk_mailmergetemplate_modifiedonbehalfby](mailmergetemplate.md#BKMK_lk_mailmergetemplate_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mailmergetemplate<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailmergetemplate_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_connectionbase_modifiedonbehalfby"></a> lk_connectionbase_modifiedonbehalfby

Same as connection entity [lk_connectionbase_modifiedonbehalfby](connection.md#BKMK_lk_connectionbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_connectionbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_queueitem_createdonbehalfby"></a> lk_queueitem_createdonbehalfby

Same as queueitem entity [lk_queueitem_createdonbehalfby](queueitem.md#BKMK_lk_queueitem_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queueitem_createdonbehalfby<br />
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


### <a name="BKMK_lk_teamtemplate_modifiedonbehalfby"></a> lk_teamtemplate_modifiedonbehalfby

Same as teamtemplate entity [lk_teamtemplate_modifiedonbehalfby](teamtemplate.md#BKMK_lk_teamtemplate_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: teamtemplate<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_teamtemplate_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_documenttemplatebase_modifiedby"></a> lk_documenttemplatebase_modifiedby

Same as documenttemplate entity [lk_documenttemplatebase_modifiedby](documenttemplate.md#BKMK_lk_documenttemplatebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: documenttemplate<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_documenttemplatebase_modifiedby<br />
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


### <a name="BKMK_lk_transformationparametermapping_createdonbehalfby"></a> lk_transformationparametermapping_createdonbehalfby

Same as transformationparametermapping entity [lk_transformationparametermapping_createdonbehalfby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: transformationparametermapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationparametermapping_createdonbehalfby<br />
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


### <a name="BKMK_lk_sharepointdocumentbase_modifiedonbehalfby"></a> lk_sharepointdocumentbase_modifiedonbehalfby

Same as sharepointdocument entity [lk_sharepointdocumentbase_modifiedonbehalfby](sharepointdocument.md#BKMK_lk_sharepointdocumentbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_relationshiprolemap_createdonbehalfby"></a> lk_relationshiprolemap_createdonbehalfby

Same as relationshiprolemap entity [lk_relationshiprolemap_createdonbehalfby](relationshiprolemap.md#BKMK_lk_relationshiprolemap_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: relationshiprolemap<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_relationshiprolemap_createdonbehalfby<br />
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


### <a name="BKMK_user_userquery"></a> user_userquery

Same as userquery entity [user_userquery](userquery.md#BKMK_user_userquery) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_userquery<br />
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


### <a name="BKMK_lk_appmodule_createdby"></a> lk_appmodule_createdby

Same as appmodule entity [lk_appmodule_createdby](appmodule.md#BKMK_lk_appmodule_createdby) Many-To-One relationship.

**ReferencingEntity**: appmodule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appmodule_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_businessprocessflowinstancebase_createdby"></a> lk_businessprocessflowinstancebase_createdby

Same as businessprocessflowinstance entity [lk_businessprocessflowinstancebase_createdby](businessprocessflowinstance.md#BKMK_lk_businessprocessflowinstancebase_createdby) Many-To-One relationship.

**ReferencingEntity**: businessprocessflowinstance<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessprocessflowinstancebase_createdby<br />
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


### <a name="BKMK_lk_kbarticlecommentbase_createdby"></a> lk_kbarticlecommentbase_createdby

Same as kbarticlecomment entity [lk_kbarticlecommentbase_createdby](kbarticlecomment.md#BKMK_lk_kbarticlecommentbase_createdby) Many-To-One relationship.

**ReferencingEntity**: kbarticlecomment<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticlecommentbase_createdby<br />
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


### <a name="BKMK_lk_convertruleitembase_modifiedby"></a> lk_convertruleitembase_modifiedby

Same as convertruleitem entity [lk_convertruleitembase_modifiedby](convertruleitem.md#BKMK_lk_convertruleitembase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_convertruleitembase_modifiedby<br />
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


### <a name="BKMK_workflow_createdonbehalfby"></a> workflow_createdonbehalfby

Same as workflow entity [workflow_createdonbehalfby](workflow.md#BKMK_workflow_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_createdonbehalfby<br />
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


### <a name="BKMK_lk_recurrencerule_modifiedby"></a> lk_recurrencerule_modifiedby

Same as recurrencerule entity [lk_recurrencerule_modifiedby](recurrencerule.md#BKMK_lk_recurrencerule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: recurrencerule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_recurrencerule_modifiedby<br />
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


### <a name="BKMK_lk_category_modifiedonbehalfby"></a> lk_category_modifiedonbehalfby

Same as category entity [lk_category_modifiedonbehalfby](category.md#BKMK_lk_category_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: category<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_category_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_appconfig_modifiedby"></a> lk_appconfig_modifiedby

Same as appconfig entity [lk_appconfig_modifiedby](appconfig.md#BKMK_lk_appconfig_modifiedby) Many-To-One relationship.

**ReferencingEntity**: appconfig<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfig_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_bulkdeleteoperationbase_createdby"></a> lk_bulkdeleteoperationbase_createdby

Same as bulkdeleteoperation entity [lk_bulkdeleteoperationbase_createdby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperationbase_createdby) Many-To-One relationship.

**ReferencingEntity**: bulkdeleteoperation<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_bulkdeleteoperationbase_createdby<br />
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


### <a name="BKMK_lk_asyncoperation_createdby"></a> lk_asyncoperation_createdby

Same as asyncoperation entity [lk_asyncoperation_createdby](asyncoperation.md#BKMK_lk_asyncoperation_createdby) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_asyncoperation_createdby<br />
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


### <a name="BKMK_lk_sdkmessagefilter_modifiedonbehalfby"></a> lk_sdkmessagefilter_modifiedonbehalfby

Same as sdkmessagefilter entity [lk_sdkmessagefilter_modifiedonbehalfby](sdkmessagefilter.md#BKMK_lk_sdkmessagefilter_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagefilter<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagefilter_modifiedonbehalfby<br />
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


### <a name="BKMK_user_recurringappointmentmaster"></a> user_recurringappointmentmaster

Same as recurringappointmentmaster entity [user_recurringappointmentmaster](recurringappointmentmaster.md#BKMK_user_recurringappointmentmaster) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_recurringappointmentmaster<br />
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


### <a name="BKMK_user_customer_relationship"></a> user_customer_relationship

Same as customerrelationship entity [user_customer_relationship](customerrelationship.md#BKMK_user_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_customer_relationship<br />
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


### <a name="BKMK_lk_slaitembase_modifiedby"></a> lk_slaitembase_modifiedby

Same as slaitem entity [lk_slaitembase_modifiedby](slaitem.md#BKMK_lk_slaitembase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slaitembase_modifiedby<br />
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


### <a name="BKMK_lk_publisheraddressbase_modifiedonbehalfby"></a> lk_publisheraddressbase_modifiedonbehalfby

Same as publisheraddress entity [lk_publisheraddressbase_modifiedonbehalfby](publisheraddress.md#BKMK_lk_publisheraddressbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: publisheraddress<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisheraddressbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_documenttemplatebase_createdby"></a> lk_documenttemplatebase_createdby

Same as documenttemplate entity [lk_documenttemplatebase_createdby](documenttemplate.md#BKMK_lk_documenttemplatebase_createdby) Many-To-One relationship.

**ReferencingEntity**: documenttemplate<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_documenttemplatebase_createdby<br />
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


### <a name="BKMK_lk_transformationparametermapping_modifiedby"></a> lk_transformationparametermapping_modifiedby

Same as transformationparametermapping entity [lk_transformationparametermapping_modifiedby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: transformationparametermapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationparametermapping_modifiedby<br />
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


### <a name="BKMK_lk_slabase_createdby"></a> lk_slabase_createdby

Same as sla entity [lk_slabase_createdby](sla.md#BKMK_lk_slabase_createdby) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slabase_createdby<br />
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


### <a name="BKMK_lk_organizationbase_createdby"></a> lk_organizationbase_createdby

Same as organization entity [lk_organizationbase_createdby](organization.md#BKMK_lk_organizationbase_createdby) Many-To-One relationship.

**ReferencingEntity**: organization<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_organizationbase_createdby<br />
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


### <a name="BKMK_lk_report_modifiedonbehalfby"></a> lk_report_modifiedonbehalfby

Same as report entity [lk_report_modifiedonbehalfby](report.md#BKMK_lk_report_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: report<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_report_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedby"></a> lk_quarterlyfiscalcalendar_modifiedby

Same as quarterlyfiscalcalendar entity [lk_quarterlyfiscalcalendar_modifiedby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_modifiedby) Many-To-One relationship.

**ReferencingEntity**: quarterlyfiscalcalendar<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_quarterlyfiscalcalendar_modifiedby<br />
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


### <a name="BKMK_createdby_serviceendpoint"></a> createdby_serviceendpoint

Same as serviceendpoint entity [createdby_serviceendpoint](serviceendpoint.md#BKMK_createdby_serviceendpoint) Many-To-One relationship.

**ReferencingEntity**: serviceendpoint<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_serviceendpoint<br />
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


### <a name="BKMK_lk_knowledgesearchmodel_modifiedonbehalfby"></a> lk_knowledgesearchmodel_modifiedonbehalfby

Same as knowledgesearchmodel entity [lk_knowledgesearchmodel_modifiedonbehalfby](knowledgesearchmodel.md#BKMK_lk_knowledgesearchmodel_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgesearchmodel<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgesearchmodel_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_duplicaterulecondition_createdonbehalfby"></a> lk_duplicaterulecondition_createdonbehalfby

Same as duplicaterulecondition entity [lk_duplicaterulecondition_createdonbehalfby](duplicaterulecondition.md#BKMK_lk_duplicaterulecondition_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: duplicaterulecondition<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicaterulecondition_createdonbehalfby<br />
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


### <a name="BKMK_lk_routingruleitem_createdonbehalfby"></a> lk_routingruleitem_createdonbehalfby

Same as routingruleitem entity [lk_routingruleitem_createdonbehalfby](routingruleitem.md#BKMK_lk_routingruleitem_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingruleitem_createdonbehalfby<br />
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


### <a name="BKMK_lk_transactioncurrencybase_modifiedby"></a> lk_transactioncurrencybase_modifiedby

Same as transactioncurrency entity [lk_transactioncurrencybase_modifiedby](transactioncurrency.md#BKMK_lk_transactioncurrencybase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: transactioncurrency<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transactioncurrencybase_modifiedby<br />
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


### <a name="BKMK_lk_DisplayStringbase_createdby"></a> lk_DisplayStringbase_createdby

Same as displaystring entity [lk_DisplayStringbase_createdby](displaystring.md#BKMK_lk_DisplayStringbase_createdby) Many-To-One relationship.

**ReferencingEntity**: displaystring<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_DisplayStringbase_createdby<br />
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


### <a name="BKMK_lk_slaitembase_modifiedonbehalfby"></a> lk_slaitembase_modifiedonbehalfby

Same as slaitem entity [lk_slaitembase_modifiedonbehalfby](slaitem.md#BKMK_lk_slaitembase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slaitembase_modifiedonbehalfby<br />
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


### <a name="BKMK_annotation_owning_user"></a> annotation_owning_user

Same as annotation entity [annotation_owning_user](annotation.md#BKMK_annotation_owning_user) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: annotation_owning_user<br />
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


### <a name="BKMK_system_user_contacts"></a> system_user_contacts

Same as contact entity [system_user_contacts](contact.md#BKMK_system_user_contacts) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: preferredsystemuserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: system_user_contacts<br />
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


### <a name="BKMK_lk_transformationparametermapping_createdby"></a> lk_transformationparametermapping_createdby

Same as transformationparametermapping entity [lk_transformationparametermapping_createdby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_createdby) Many-To-One relationship.

**ReferencingEntity**: transformationparametermapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationparametermapping_createdby<br />
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


### <a name="BKMK_lk_phonecall_createdonbehalfby"></a> lk_phonecall_createdonbehalfby

Same as phonecall entity [lk_phonecall_createdonbehalfby](phonecall.md#BKMK_lk_phonecall_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_phonecall_createdonbehalfby<br />
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


### <a name="BKMK_lk_email_modifiedby"></a> lk_email_modifiedby

Same as email entity [lk_email_modifiedby](email.md#BKMK_lk_email_modifiedby) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_email_modifiedby<br />
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


### <a name="BKMK_lk_sharepointdocumentbase_createdonbehalfby"></a> lk_sharepointdocumentbase_createdonbehalfby

Same as sharepointdocument entity [lk_sharepointdocumentbase_createdonbehalfby](sharepointdocument.md#BKMK_lk_sharepointdocumentbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_usersettingsbase_createdby"></a> lk_usersettingsbase_createdby

Same as usersettings entity [lk_usersettingsbase_createdby](usersettings.md#BKMK_lk_usersettingsbase_createdby) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_usersettingsbase_createdby<br />
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


### <a name="BKMK_lk_teamtemplate_createdonbehalfby"></a> lk_teamtemplate_createdonbehalfby

Same as teamtemplate entity [lk_teamtemplate_createdonbehalfby](teamtemplate.md#BKMK_lk_teamtemplate_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: teamtemplate<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_teamtemplate_createdonbehalfby<br />
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


### <a name="BKMK_lk_appmodule_createdonbehalfby"></a> lk_appmodule_createdonbehalfby

Same as appmodule entity [lk_appmodule_createdonbehalfby](appmodule.md#BKMK_lk_appmodule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appmodule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appmodule_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_importlogbase_createdby"></a> lk_importlogbase_createdby

Same as importlog entity [lk_importlogbase_createdby](importlog.md#BKMK_lk_importlogbase_createdby) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importlogbase_createdby<br />
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


### <a name="BKMK_lk_sharepointdocumentlocationbase_createdby"></a> lk_sharepointdocumentlocationbase_createdby

Same as sharepointdocumentlocation entity [lk_sharepointdocumentlocationbase_createdby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_createdby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentlocationbase_createdby<br />
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


### <a name="BKMK_lk_socialinsightsconfiguration_modifiedby"></a> lk_socialinsightsconfiguration_modifiedby

Same as socialinsightsconfiguration entity [lk_socialinsightsconfiguration_modifiedby](socialinsightsconfiguration.md#BKMK_lk_socialinsightsconfiguration_modifiedby) Many-To-One relationship.

**ReferencingEntity**: socialinsightsconfiguration<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_socialinsightsconfiguration_modifiedby<br />
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


### <a name="BKMK_user_accounts"></a> user_accounts

Same as account entity [user_accounts](account.md#BKMK_user_accounts) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_accounts<br />
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


### <a name="BKMK_lk_externalpartyitem_modifiedonbehalfby"></a> lk_externalpartyitem_modifiedonbehalfby

Same as externalpartyitem entity [lk_externalpartyitem_modifiedonbehalfby](externalpartyitem.md#BKMK_lk_externalpartyitem_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: externalpartyitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_externalpartyitem_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_reportentitybase_modifiedby"></a> lk_reportentitybase_modifiedby

Same as reportentity entity [lk_reportentitybase_modifiedby](reportentity.md#BKMK_lk_reportentitybase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: reportentity<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportentitybase_modifiedby<br />
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


### <a name="BKMK_lk_sdkmessagepair_modifiedonbehalfby"></a> lk_sdkmessagepair_modifiedonbehalfby

Same as sdkmessagepair entity [lk_sdkmessagepair_modifiedonbehalfby](sdkmessagepair.md#BKMK_lk_sdkmessagepair_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagepair<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagepair_modifiedonbehalfby<br />
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


### <a name="BKMK_user_settings"></a> user_settings

Same as usersettings entity [user_settings](usersettings.md#BKMK_user_settings) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: systemuserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_settings<br />
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


### <a name="BKMK_modifiedby_plugintype"></a> modifiedby_plugintype

Same as plugintype entity [modifiedby_plugintype](plugintype.md#BKMK_modifiedby_plugintype) Many-To-One relationship.

**ReferencingEntity**: plugintype<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_plugintype<br />
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


### <a name="BKMK_lk_importentitymapping_modifiedonbehalfby"></a> lk_importentitymapping_modifiedonbehalfby

Same as importentitymapping entity [lk_importentitymapping_modifiedonbehalfby](importentitymapping.md#BKMK_lk_importentitymapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importentitymapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importentitymapping_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_savedquerybase_createdby"></a> lk_savedquerybase_createdby

Same as savedquery entity [lk_savedquerybase_createdby](savedquery.md#BKMK_lk_savedquerybase_createdby) Many-To-One relationship.

**ReferencingEntity**: savedquery<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedquerybase_createdby<br />
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


### <a name="BKMK_lk_offlinecommanddefinition_createdby"></a> lk_offlinecommanddefinition_createdby

Same as offlinecommanddefinition entity [lk_offlinecommanddefinition_createdby](offlinecommanddefinition.md#BKMK_lk_offlinecommanddefinition_createdby) Many-To-One relationship.

**ReferencingEntity**: offlinecommanddefinition<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_offlinecommanddefinition_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_activitypointer_createdby"></a> lk_activitypointer_createdby

Same as activitypointer entity [lk_activitypointer_createdby](activitypointer.md#BKMK_lk_activitypointer_createdby) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_activitypointer_createdby<br />
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


### <a name="BKMK_lk_columnmapping_createdonbehalfby"></a> lk_columnmapping_createdonbehalfby

Same as columnmapping entity [lk_columnmapping_createdonbehalfby](columnmapping.md#BKMK_lk_columnmapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: columnmapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_columnmapping_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_relationship_role"></a> modifiedby_relationship_role

Same as relationshiprole entity [modifiedby_relationship_role](relationshiprole.md#BKMK_modifiedby_relationship_role) Many-To-One relationship.

**ReferencingEntity**: relationshiprole<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_relationship_role<br />
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


### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby"></a> lk_mobileofflineprofileitemassociation_modifiedonbehalfby

Same as mobileofflineprofileitemassociation entity [lk_mobileofflineprofileitemassociation_modifiedonbehalfby](mobileofflineprofileitemassociation.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitemassociation<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mobileofflineprofileitemassocaition_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_subject_createdonbehalfby"></a> lk_subject_createdonbehalfby

Same as subject entity [lk_subject_createdonbehalfby](subject.md#BKMK_lk_subject_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: subject<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_subject_createdonbehalfby<br />
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


### <a name="BKMK_lk_appconfigmaster_createdonbehalfby"></a> lk_appconfigmaster_createdonbehalfby

Same as appconfigmaster entity [lk_appconfigmaster_createdonbehalfby](appconfigmaster.md#BKMK_lk_appconfigmaster_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appconfigmaster<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfigmaster_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_ChannelProperty_createdby"></a> lk_ChannelProperty_createdby

Same as channelproperty entity [lk_ChannelProperty_createdby](channelproperty.md#BKMK_lk_ChannelProperty_createdby) Many-To-One relationship.

**ReferencingEntity**: channelproperty<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelProperty_createdby<br />
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


### <a name="BKMK_lk_kbarticle_modifiedonbehalfby"></a> lk_kbarticle_modifiedonbehalfby

Same as kbarticle entity [lk_kbarticle_modifiedonbehalfby](kbarticle.md#BKMK_lk_kbarticle_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: kbarticle<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticle_modifiedonbehalfby<br />
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


### <a name="BKMK_modifiedby_entitymap"></a> modifiedby_entitymap

Same as entitymap entity [modifiedby_entitymap](entitymap.md#BKMK_modifiedby_entitymap) Many-To-One relationship.

**ReferencingEntity**: entitymap<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_entitymap<br />
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


### <a name="BKMK_createdby_sdkmessageprocessingstepsecureconfig"></a> createdby_sdkmessageprocessingstepsecureconfig

Same as sdkmessageprocessingstepsecureconfig entity [createdby_sdkmessageprocessingstepsecureconfig](sdkmessageprocessingstepsecureconfig.md#BKMK_createdby_sdkmessageprocessingstepsecureconfig) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepsecureconfig<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessageprocessingstepsecureconfig<br />
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


### <a name="BKMK_createdby_sdkmessageprocessingstep"></a> createdby_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [createdby_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_createdby_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessageprocessingstep<br />
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


### <a name="BKMK_lk_appconfig_modifiedonbehalfby"></a> lk_appconfig_modifiedonbehalfby

Same as appconfig entity [lk_appconfig_modifiedonbehalfby](appconfig.md#BKMK_lk_appconfig_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appconfig<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfig_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_quarterlyfiscalcalendar_salespersonid"></a> lk_quarterlyfiscalcalendar_salespersonid

Same as quarterlyfiscalcalendar entity [lk_quarterlyfiscalcalendar_salespersonid](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_salespersonid) Many-To-One relationship.

**ReferencingEntity**: quarterlyfiscalcalendar<br />
**ReferencingAttribute**: salespersonid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_quarterlyfiscalcalendar_salespersonid<br />
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


### <a name="BKMK_lk_transformationparametermapping_modifiedonbehalfby"></a> lk_transformationparametermapping_modifiedonbehalfby

Same as transformationparametermapping entity [lk_transformationparametermapping_modifiedonbehalfby](transformationparametermapping.md#BKMK_lk_transformationparametermapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: transformationparametermapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationparametermapping_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_importentitymapping_createdonbehalfby"></a> lk_importentitymapping_createdonbehalfby

Same as importentitymapping entity [lk_importentitymapping_createdonbehalfby](importentitymapping.md#BKMK_lk_importentitymapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importentitymapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importentitymapping_createdonbehalfby<br />
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


### <a name="BKMK_SystemUser_ProcessSessions"></a> SystemUser_ProcessSessions

Same as processsession entity [SystemUser_ProcessSessions](processsession.md#BKMK_SystemUser_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_ProcessSessions<br />
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


### <a name="BKMK_lk_templatebase_createdonbehalfby"></a> lk_templatebase_createdonbehalfby

Same as template entity [lk_templatebase_createdonbehalfby](template.md#BKMK_lk_templatebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_templatebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_lookupmapping_createdby"></a> lk_lookupmapping_createdby

Same as lookupmapping entity [lk_lookupmapping_createdby](lookupmapping.md#BKMK_lk_lookupmapping_createdby) Many-To-One relationship.

**ReferencingEntity**: lookupmapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_lookupmapping_createdby<br />
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


### <a name="BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby"></a> lk_mobileofflineprofileitem_modifiedonbehalfby

Same as mobileofflineprofileitem entity [lk_mobileofflineprofileitem_modifiedonbehalfby](mobileofflineprofileitem.md#BKMK_lk_mobileofflineprofileitem_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mobileofflineprofileitem_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_processsessionbase_modifiedonbehalfby"></a> lk_processsessionbase_modifiedonbehalfby

Same as processsession entity [lk_processsessionbase_modifiedonbehalfby](processsession.md#BKMK_lk_processsessionbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsessionbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_processsession_createdby"></a> lk_processsession_createdby

Same as processsession entity [lk_processsession_createdby](processsession.md#BKMK_lk_processsession_createdby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_createdby<br />
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


### <a name="BKMK_lk_personaldocumenttemplatebase_createdby"></a> lk_personaldocumenttemplatebase_createdby

Same as personaldocumenttemplate entity [lk_personaldocumenttemplatebase_createdby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_createdby) Many-To-One relationship.

**ReferencingEntity**: personaldocumenttemplate<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_personaldocumenttemplatebase_createdby<br />
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


### <a name="BKMK_lk_publisherbase_modifiedonbehalfby"></a> lk_publisherbase_modifiedonbehalfby

Same as publisher entity [lk_publisherbase_modifiedonbehalfby](publisher.md#BKMK_lk_publisherbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: publisher<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisherbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_MobileOfflineProfile_createdonbehalfby"></a> lk_MobileOfflineProfile_createdonbehalfby

Same as mobileofflineprofile entity [lk_MobileOfflineProfile_createdonbehalfby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofile<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_MobileOfflineProfile_createdonbehalfby<br />
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


### <a name="BKMK_lk_timezonerule_createdby"></a> lk_timezonerule_createdby

Same as timezonerule entity [lk_timezonerule_createdby](timezonerule.md#BKMK_lk_timezonerule_createdby) Many-To-One relationship.

**ReferencingEntity**: timezonerule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonerule_createdby<br />
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


### <a name="BKMK_lk_contactbase_createdby"></a> lk_contactbase_createdby

Same as contact entity [lk_contactbase_createdby](contact.md#BKMK_lk_contactbase_createdby) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_contactbase_createdby<br />
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


### <a name="BKMK_lk_slakpiinstancebase_createdonbehalfby"></a> lk_slakpiinstancebase_createdonbehalfby

Same as slakpiinstance entity [lk_slakpiinstancebase_createdonbehalfby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slakpiinstancebase_createdonbehalfby<br />
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


### <a name="BKMK_system_user_workflow"></a> system_user_workflow

Same as workflow entity [system_user_workflow](workflow.md#BKMK_system_user_workflow) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: system_user_workflow<br />
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


### <a name="BKMK_lk_duplicaterulebase_createdby"></a> lk_duplicaterulebase_createdby

Same as duplicaterule entity [lk_duplicaterulebase_createdby](duplicaterule.md#BKMK_lk_duplicaterulebase_createdby) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicaterulebase_createdby<br />
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


### <a name="BKMK_lk_appointment_createdonbehalfby"></a> lk_appointment_createdonbehalfby

Same as appointment entity [lk_appointment_createdonbehalfby](appointment.md#BKMK_lk_appointment_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_appointment_createdonbehalfby<br />
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


### <a name="BKMK_createdby_connection_role"></a> createdby_connection_role

Same as connectionrole entity [createdby_connection_role](connectionrole.md#BKMK_createdby_connection_role) Many-To-One relationship.

**ReferencingEntity**: connectionrole<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_connection_role<br />
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


### <a name="BKMK_lk_appconfigmaster_modifiedby"></a> lk_appconfigmaster_modifiedby

Same as appconfigmaster entity [lk_appconfigmaster_modifiedby](appconfigmaster.md#BKMK_lk_appconfigmaster_modifiedby) Many-To-One relationship.

**ReferencingEntity**: appconfigmaster<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfigmaster_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_newprocess_modifiedby"></a> lk_newprocess_modifiedby

Same as newprocess entity [lk_newprocess_modifiedby](newprocess.md#BKMK_lk_newprocess_modifiedby) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_newprocess_modifiedby<br />
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


### <a name="BKMK_lk_columnmapping_modifiedonbehalfby"></a> lk_columnmapping_modifiedonbehalfby

Same as columnmapping entity [lk_columnmapping_modifiedonbehalfby](columnmapping.md#BKMK_lk_columnmapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: columnmapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_columnmapping_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_translationprocess_createdby"></a> lk_translationprocess_createdby

Same as translationprocess entity [lk_translationprocess_createdby](translationprocess.md#BKMK_lk_translationprocess_createdby) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_translationprocess_createdby<br />
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


### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedby"></a> lk_monthlyfiscalcalendar_modifiedby

Same as monthlyfiscalcalendar entity [lk_monthlyfiscalcalendar_modifiedby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_modifiedby) Many-To-One relationship.

**ReferencingEntity**: monthlyfiscalcalendar<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_monthlyfiscalcalendar_modifiedby<br />
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


### <a name="BKMK_lk_systemuserbase_modifiedby"></a> lk_systemuserbase_modifiedby

Same as systemuser entity [lk_systemuserbase_modifiedby](systemuser.md#BKMK_lk_systemuserbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_systemuserbase_modifiedby<br />
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


### <a name="BKMK_lk_expiredprocess_modifiedby"></a> lk_expiredprocess_modifiedby

Same as expiredprocess entity [lk_expiredprocess_modifiedby](expiredprocess.md#BKMK_lk_expiredprocess_modifiedby) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_expiredprocess_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_SocialProfile_createdonbehalfby"></a> lk_SocialProfile_createdonbehalfby

Same as socialprofile entity [lk_SocialProfile_createdonbehalfby](socialprofile.md#BKMK_lk_SocialProfile_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: socialprofile<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_SocialProfile_createdonbehalfby<br />
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


### <a name="BKMK_lk_importmap_createdonbehalfby"></a> lk_importmap_createdonbehalfby

Same as importmap entity [lk_importmap_createdonbehalfby](importmap.md#BKMK_lk_importmap_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importmap_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_connection"></a> modifiedby_connection

Same as connection entity [modifiedby_connection](connection.md#BKMK_modifiedby_connection) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_connection<br />
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


### <a name="BKMK_lk_import_createdonbehalfby"></a> lk_import_createdonbehalfby

Same as import entity [lk_import_createdonbehalfby](import.md#BKMK_lk_import_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_import_createdonbehalfby<br />
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


### <a name="BKMK_lk_advancedsimilarityrule_createdby"></a> lk_advancedsimilarityrule_createdby

Same as advancedsimilarityrule entity [lk_advancedsimilarityrule_createdby](advancedsimilarityrule.md#BKMK_lk_advancedsimilarityrule_createdby) Many-To-One relationship.

**ReferencingEntity**: advancedsimilarityrule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_advancedsimilarityrule_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_slaitembase_createdonbehalfby"></a> lk_slaitembase_createdonbehalfby

Same as slaitem entity [lk_slaitembase_createdonbehalfby](slaitem.md#BKMK_lk_slaitembase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slaitembase_createdonbehalfby<br />
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


### <a name="BKMK_lk_offlinecommanddefinition_createdonbehalfby"></a> lk_offlinecommanddefinition_createdonbehalfby

Same as offlinecommanddefinition entity [lk_offlinecommanddefinition_createdonbehalfby](offlinecommanddefinition.md#BKMK_lk_offlinecommanddefinition_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: offlinecommanddefinition<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_offlinecommanddefinition_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_navigationsetting_createdonbehalfby"></a> lk_navigationsetting_createdonbehalfby

Same as navigationsetting entity [lk_navigationsetting_createdonbehalfby](navigationsetting.md#BKMK_lk_navigationsetting_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: navigationsetting<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_navigationsetting_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_sdkmessagerequestfield_createdonbehalfby"></a> lk_sdkmessagerequestfield_createdonbehalfby

Same as sdkmessagerequestfield entity [lk_sdkmessagerequestfield_createdonbehalfby](sdkmessagerequestfield.md#BKMK_lk_sdkmessagerequestfield_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequestfield<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagerequestfield_createdonbehalfby<br />
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


### <a name="BKMK_lk_savedquery_modifiedonbehalfby"></a> lk_savedquery_modifiedonbehalfby

Same as savedquery entity [lk_savedquery_modifiedonbehalfby](savedquery.md#BKMK_lk_savedquery_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: savedquery<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedquery_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_solutioncomponentbase_modifiedonbehalfby"></a> lk_solutioncomponentbase_modifiedonbehalfby

Same as solutioncomponent entity [lk_solutioncomponentbase_modifiedonbehalfby](solutioncomponent.md#BKMK_lk_solutioncomponentbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: solutioncomponent<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_solutioncomponentbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_connectionrolebase_createdonbehalfby"></a> lk_connectionrolebase_createdonbehalfby

Same as connectionrole entity [lk_connectionrolebase_createdonbehalfby](connectionrole.md#BKMK_lk_connectionrolebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: connectionrole<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_connectionrolebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_actioncardbase_createdby"></a> lk_actioncardbase_createdby

Same as actioncard entity [lk_actioncardbase_createdby](actioncard.md#BKMK_lk_actioncardbase_createdby) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_actioncardbase_createdby<br />
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


### <a name="BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby"></a> lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby

Same as sdkmessageprocessingstepsecureconfig entity [lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby](sdkmessageprocessingstepsecureconfig.md#BKMK_lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepsecureconfig<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageprocessingstepsecureconfig_createdonbehalfby<br />
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


### <a name="BKMK_lk_webresourcebase_modifiedonbehalfby"></a> lk_webresourcebase_modifiedonbehalfby

Same as webresource entity [lk_webresourcebase_modifiedonbehalfby](webresource.md#BKMK_lk_webresourcebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: webresource<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_webresourcebase_modifiedonbehalfby<br />
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


### <a name="BKMK_user_letter"></a> user_letter

Same as letter entity [user_letter](letter.md#BKMK_user_letter) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_letter<br />
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


### <a name="BKMK_lk_tracelog_modifiedonbehalfby"></a> lk_tracelog_modifiedonbehalfby

Same as tracelog entity [lk_tracelog_modifiedonbehalfby](tracelog.md#BKMK_lk_tracelog_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_tracelog_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_timezonedefinition_createdby"></a> lk_timezonedefinition_createdby

Same as timezonedefinition entity [lk_timezonedefinition_createdby](timezonedefinition.md#BKMK_lk_timezonedefinition_createdby) Many-To-One relationship.

**ReferencingEntity**: timezonedefinition<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonedefinition_createdby<br />
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


### <a name="BKMK_lk_reportcategory_createdonbehalfby"></a> lk_reportcategory_createdonbehalfby

Same as reportcategory entity [lk_reportcategory_createdonbehalfby](reportcategory.md#BKMK_lk_reportcategory_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportcategory<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_reportcategory_createdonbehalfby<br />
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


### <a name="BKMK_createdby_plugintype"></a> createdby_plugintype

Same as plugintype entity [createdby_plugintype](plugintype.md#BKMK_createdby_plugintype) Many-To-One relationship.

**ReferencingEntity**: plugintype<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_plugintype<br />
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


### <a name="BKMK_lk_organization_createdonbehalfby"></a> lk_organization_createdonbehalfby

Same as organization entity [lk_organization_createdonbehalfby](organization.md#BKMK_lk_organization_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: organization<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_organization_createdonbehalfby<br />
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


### <a name="BKMK_lk_calendar_modifiedonbehalfby"></a> lk_calendar_modifiedonbehalfby

Same as calendar entity [lk_calendar_modifiedonbehalfby](calendar.md#BKMK_lk_calendar_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: calendar<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_calendar_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_slakpiinstancebase_modifiedby"></a> lk_slakpiinstancebase_modifiedby

Same as slakpiinstance entity [lk_slakpiinstancebase_modifiedby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slakpiinstancebase_modifiedby<br />
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


### <a name="BKMK_createdby_plugintracelog"></a> createdby_plugintracelog

Same as plugintracelog entity [createdby_plugintracelog](plugintracelog.md#BKMK_createdby_plugintracelog) Many-To-One relationship.

**ReferencingEntity**: plugintracelog<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_plugintracelog<br />
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


### <a name="BKMK_user_convertrule"></a> user_convertrule

Same as convertrule entity [user_convertrule](convertrule.md#BKMK_user_convertrule) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_convertrule<br />
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


### <a name="BKMK_lk_appconfiginstance_modifiedby"></a> lk_appconfiginstance_modifiedby

Same as appconfiginstance entity [lk_appconfiginstance_modifiedby](appconfiginstance.md#BKMK_lk_appconfiginstance_modifiedby) Many-To-One relationship.

**ReferencingEntity**: appconfiginstance<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfiginstance_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_picklistmapping_createdonbehalfby"></a> lk_picklistmapping_createdonbehalfby

Same as picklistmapping entity [lk_picklistmapping_createdonbehalfby](picklistmapping.md#BKMK_lk_picklistmapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: picklistmapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_picklistmapping_createdonbehalfby<br />
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


### <a name="BKMK_lk_knowledgearticleviews_createdby"></a> lk_knowledgearticleviews_createdby

Same as knowledgearticleviews entity [lk_knowledgearticleviews_createdby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_createdby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticleviews<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticleviews_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_SystemUser_Imports"></a> SystemUser_Imports

Same as import entity [SystemUser_Imports](import.md#BKMK_SystemUser_Imports) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_Imports<br />
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


### <a name="BKMK_modifiedby_sdkmessage"></a> modifiedby_sdkmessage

Same as sdkmessage entity [modifiedby_sdkmessage](sdkmessage.md#BKMK_modifiedby_sdkmessage) Many-To-One relationship.

**ReferencingEntity**: sdkmessage<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessage<br />
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


### <a name="BKMK_lk_ownermapping_createdonbehalfby"></a> lk_ownermapping_createdonbehalfby

Same as ownermapping entity [lk_ownermapping_createdonbehalfby](ownermapping.md#BKMK_lk_ownermapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: ownermapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ownermapping_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_attributemap"></a> modifiedby_attributemap

Same as attributemap entity [modifiedby_attributemap](attributemap.md#BKMK_modifiedby_attributemap) Many-To-One relationship.

**ReferencingEntity**: attributemap<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_attributemap<br />
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


### <a name="BKMK_lk_kbarticlecomment_createdonbehalfby"></a> lk_kbarticlecomment_createdonbehalfby

Same as kbarticlecomment entity [lk_kbarticlecomment_createdonbehalfby](kbarticlecomment.md#BKMK_lk_kbarticlecomment_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: kbarticlecomment<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticlecomment_createdonbehalfby<br />
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


### <a name="BKMK_lk_navigationsetting_modifiedonbehalfby"></a> lk_navigationsetting_modifiedonbehalfby

Same as navigationsetting entity [lk_navigationsetting_modifiedonbehalfby](navigationsetting.md#BKMK_lk_navigationsetting_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: navigationsetting<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_navigationsetting_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_timezonerule_createdonbehalfby"></a> lk_timezonerule_createdonbehalfby

Same as timezonerule entity [lk_timezonerule_createdonbehalfby](timezonerule.md#BKMK_lk_timezonerule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: timezonerule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonerule_createdonbehalfby<br />
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


### <a name="BKMK_lk_templatebase_createdby"></a> lk_templatebase_createdby

Same as template entity [lk_templatebase_createdby](template.md#BKMK_lk_templatebase_createdby) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_templatebase_createdby<br />
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


### <a name="BKMK_lk_routingruleitem_modifiedby"></a> lk_routingruleitem_modifiedby

Same as routingruleitem entity [lk_routingruleitem_modifiedby](routingruleitem.md#BKMK_lk_routingruleitem_modifiedby) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingruleitem_modifiedby<br />
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


### <a name="BKMK_lk_userformbase_modifiedonbehalfby"></a> lk_userformbase_modifiedonbehalfby

Same as userform entity [lk_userformbase_modifiedonbehalfby](userform.md#BKMK_lk_userformbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userformbase_modifiedonbehalfby<br />
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


### <a name="BKMK_workflow_dependency_modifiedby"></a> workflow_dependency_modifiedby

Same as workflowdependency entity [workflow_dependency_modifiedby](workflowdependency.md#BKMK_workflow_dependency_modifiedby) Many-To-One relationship.

**ReferencingEntity**: workflowdependency<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_dependency_modifiedby<br />
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


### <a name="BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby"></a> lk_mobileofflineprofileitemassociation_createdonbehalfby

Same as mobileofflineprofileitemassociation entity [lk_mobileofflineprofileitemassociation_createdonbehalfby](mobileofflineprofileitemassociation.md#BKMK_lk_mobileofflineprofileitemassociation_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitemassociation<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mobileofflineprofileitemassociation_createdonbehalfby<br />
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


### <a name="BKMK_lk_customeraddress_createdonbehalfby"></a> lk_customeraddress_createdonbehalfby

Same as customeraddress entity [lk_customeraddress_createdonbehalfby](customeraddress.md#BKMK_lk_customeraddress_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customeraddress<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_customeraddress_createdonbehalfby<br />
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


### <a name="BKMK_lk_importfilebase_modifiedby"></a> lk_importfilebase_modifiedby

Same as importfile entity [lk_importfilebase_modifiedby](importfile.md#BKMK_lk_importfilebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importfilebase_modifiedby<br />
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


### <a name="BKMK_lk_accountbase_modifiedby"></a> lk_accountbase_modifiedby

Same as account entity [lk_accountbase_modifiedby](account.md#BKMK_lk_accountbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_accountbase_modifiedby<br />
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


### <a name="BKMK_lk_personaldocumenttemplatebase_modifiedonbehalfby"></a> lk_personaldocumenttemplatebase_modifiedonbehalfby

Same as personaldocumenttemplate entity [lk_personaldocumenttemplatebase_modifiedonbehalfby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: personaldocumenttemplate<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_personaldocumenttemplatebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_category_createdby"></a> lk_category_createdby

Same as category entity [lk_category_createdby](category.md#BKMK_lk_category_createdby) Many-To-One relationship.

**ReferencingEntity**: category<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_category_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_customcontroldefaultconfig_modifiedby"></a> lk_customcontroldefaultconfig_modifiedby

Same as customcontroldefaultconfig entity [lk_customcontroldefaultconfig_modifiedby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_modifiedby) Many-To-One relationship.

**ReferencingEntity**: customcontroldefaultconfig<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontroldefaultconfig_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_user_routingrule"></a> user_routingrule

Same as routingrule entity [user_routingrule](routingrule.md#BKMK_user_routingrule) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_routingrule<br />
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


### <a name="BKMK_lk_SharePointData_modifiedonbehalfby"></a> lk_SharePointData_modifiedonbehalfby

Same as sharepointdata entity [lk_SharePointData_modifiedonbehalfby](sharepointdata.md#BKMK_lk_SharePointData_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_SharePointData_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_SocialProfile_modifiedonbehalfby"></a> lk_SocialProfile_modifiedonbehalfby

Same as socialprofile entity [lk_SocialProfile_modifiedonbehalfby](socialprofile.md#BKMK_lk_SocialProfile_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: socialprofile<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_SocialProfile_modifiedonbehalfby<br />
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


### <a name="BKMK_user_fax"></a> user_fax

Same as fax entity [user_fax](fax.md#BKMK_user_fax) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_fax<br />
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


### <a name="BKMK_lk_activitypointer_modifiedonbehalfby"></a> lk_activitypointer_modifiedonbehalfby

Same as activitypointer entity [lk_activitypointer_modifiedonbehalfby](activitypointer.md#BKMK_lk_activitypointer_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_activitypointer_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_feedback_createdonbehalfby"></a> lk_feedback_createdonbehalfby

Same as feedback entity [lk_feedback_createdonbehalfby](feedback.md#BKMK_lk_feedback_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_feedback_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_appmodulecomponent_createdby"></a> lk_appmodulecomponent_createdby

Same as appmodulecomponent entity [lk_appmodulecomponent_createdby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_createdby) Many-To-One relationship.

**ReferencingEntity**: appmodulecomponent<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: appmodulecomponent_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_sharepointsitebase_modifiedby"></a> lk_sharepointsitebase_modifiedby

Same as sharepointsite entity [lk_sharepointsitebase_modifiedby](sharepointsite.md#BKMK_lk_sharepointsitebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointsitebase_modifiedby<br />
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


### <a name="BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby"></a> lk_sdkmessageprocessingstepimage_createdonbehalfby

Same as sdkmessageprocessingstepimage entity [lk_sdkmessageprocessingstepimage_createdonbehalfby](sdkmessageprocessingstepimage.md#BKMK_lk_sdkmessageprocessingstepimage_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepimage<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageprocessingstepimage_createdonbehalfby<br />
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


### <a name="BKMK_lk_importlog_createdonbehalfby"></a> lk_importlog_createdonbehalfby

Same as importlog entity [lk_importlog_createdonbehalfby](importlog.md#BKMK_lk_importlog_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importlog_createdonbehalfby<br />
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


### <a name="BKMK_lk_reportlink_modifiedonbehalfby"></a> lk_reportlink_modifiedonbehalfby

Same as reportlink entity [lk_reportlink_modifiedonbehalfby](reportlink.md#BKMK_lk_reportlink_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportlink<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportlink_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_ChannelProperty_modifiedonbehalfby"></a> lk_ChannelProperty_modifiedonbehalfby

Same as channelproperty entity [lk_ChannelProperty_modifiedonbehalfby](channelproperty.md#BKMK_lk_ChannelProperty_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelproperty<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelProperty_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_processsession_executedby"></a> lk_processsession_executedby

Same as processsession entity [lk_processsession_executedby](processsession.md#BKMK_lk_processsession_executedby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: executedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_executedby<br />
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


### <a name="BKMK_lk_customcontrol_modifiedby"></a> lk_customcontrol_modifiedby

Same as customcontrol entity [lk_customcontrol_modifiedby](customcontrol.md#BKMK_lk_customcontrol_modifiedby) Many-To-One relationship.

**ReferencingEntity**: customcontrol<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrol_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_workflow_dependency_modifiedonbehalfby"></a> workflow_dependency_modifiedonbehalfby

Same as workflowdependency entity [workflow_dependency_modifiedonbehalfby](workflowdependency.md#BKMK_workflow_dependency_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: workflowdependency<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_dependency_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_customcontrolresource_createdonbehalfby"></a> lk_customcontrolresource_createdonbehalfby

Same as customcontrolresource entity [lk_customcontrolresource_createdonbehalfby](customcontrolresource.md#BKMK_lk_customcontrolresource_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customcontrolresource<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrolresource_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_SystemUser_DuplicateMatchingRecord"></a> SystemUser_DuplicateMatchingRecord

Same as duplicaterecord entity [SystemUser_DuplicateMatchingRecord](duplicaterecord.md#BKMK_SystemUser_DuplicateMatchingRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: duplicaterecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_DuplicateMatchingRecord<br />
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


### <a name="BKMK_createdby_sdkmessageprocessingstepimage"></a> createdby_sdkmessageprocessingstepimage

Same as sdkmessageprocessingstepimage entity [createdby_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_createdby_sdkmessageprocessingstepimage) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepimage<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessageprocessingstepimage<br />
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


### <a name="BKMK_lk_connectionbase_createdonbehalfby"></a> lk_connectionbase_createdonbehalfby

Same as connection entity [lk_connectionbase_createdonbehalfby](connection.md#BKMK_lk_connectionbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_connectionbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_customcontrol_createdby"></a> lk_customcontrol_createdby

Same as customcontrol entity [lk_customcontrol_createdby](customcontrol.md#BKMK_lk_customcontrol_createdby) Many-To-One relationship.

**ReferencingEntity**: customcontrol<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrol_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_customcontrolresource_modifiedonbehalfby"></a> lk_customcontrolresource_modifiedonbehalfby

Same as customcontrolresource entity [lk_customcontrolresource_modifiedonbehalfby](customcontrolresource.md#BKMK_lk_customcontrolresource_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customcontrolresource<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrolresource_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_ChannelProperty_createdonbehalfby"></a> lk_ChannelProperty_createdonbehalfby

Same as channelproperty entity [lk_ChannelProperty_createdonbehalfby](channelproperty.md#BKMK_lk_ChannelProperty_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelproperty<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelProperty_createdonbehalfby<br />
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


### <a name="BKMK_lk_timezonerule_modifiedby"></a> lk_timezonerule_modifiedby

Same as timezonerule entity [lk_timezonerule_modifiedby](timezonerule.md#BKMK_lk_timezonerule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: timezonerule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonerule_modifiedby<br />
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


### <a name="BKMK_lk_ACIViewMapper_createdonbehalfby"></a> lk_ACIViewMapper_createdonbehalfby

Same as aciviewmapper entity [lk_ACIViewMapper_createdonbehalfby](aciviewmapper.md#BKMK_lk_ACIViewMapper_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: aciviewmapper<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ACIViewMapper_createdonbehalfby<br />
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


### <a name="BKMK_lk_routingrule_modifiedonbehalfby"></a> lk_routingrule_modifiedonbehalfby

Same as routingrule entity [lk_routingrule_modifiedonbehalfby](routingrule.md#BKMK_lk_routingrule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingrule_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_audit_userid"></a> lk_audit_userid

Same as audit entity [lk_audit_userid](audit.md#BKMK_lk_audit_userid) Many-To-One relationship.

**ReferencingEntity**: audit<br />
**ReferencingAttribute**: userid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_audit_userid<br />
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


### <a name="BKMK_lk_solutionbase_createdonbehalfby"></a> lk_solutionbase_createdonbehalfby

Same as solution entity [lk_solutionbase_createdonbehalfby](solution.md#BKMK_lk_solutionbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_solutionbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_convertruleitembase_createdonbehalfby"></a> lk_convertruleitembase_createdonbehalfby

Same as convertruleitem entity [lk_convertruleitembase_createdonbehalfby](convertruleitem.md#BKMK_lk_convertruleitembase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_convertruleitembase_createdonbehalfby<br />
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


### <a name="BKMK_lk_convertruleitembase_modifiedonbehalfby"></a> lk_convertruleitembase_modifiedonbehalfby

Same as convertruleitem entity [lk_convertruleitembase_modifiedonbehalfby](convertruleitem.md#BKMK_lk_convertruleitembase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: convertruleitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_convertruleitembase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby"></a> lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby

Same as fixedmonthlyfiscalcalendar entity [lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: fixedmonthlyfiscalcalendar<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fixedmonthlyfiscalcalendar_modifiedonbehalfby<br />
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


### <a name="BKMK_OwnerMapping_SystemUser"></a> OwnerMapping_SystemUser

Same as ownermapping entity [OwnerMapping_SystemUser](ownermapping.md#BKMK_OwnerMapping_SystemUser) Many-To-One relationship.

**ReferencingEntity**: ownermapping<br />
**ReferencingAttribute**: targetsystemuserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: OwnerMapping_SystemUser<br />
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


### <a name="BKMK_lk_columnmapping_modifiedby"></a> lk_columnmapping_modifiedby

Same as columnmapping entity [lk_columnmapping_modifiedby](columnmapping.md#BKMK_lk_columnmapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: columnmapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_columnmapping_modifiedby<br />
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


### <a name="BKMK_lk_publisheraddressbase_modifiedby"></a> lk_publisheraddressbase_modifiedby

Same as publisheraddress entity [lk_publisheraddressbase_modifiedby](publisheraddress.md#BKMK_lk_publisheraddressbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: publisheraddress<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisheraddressbase_modifiedby<br />
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


### <a name="BKMK_lk_accountbase_createdby"></a> lk_accountbase_createdby

Same as account entity [lk_accountbase_createdby](account.md#BKMK_lk_accountbase_createdby) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_accountbase_createdby<br />
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


### <a name="BKMK_lk_savedquerybase_modifiedby"></a> lk_savedquerybase_modifiedby

Same as savedquery entity [lk_savedquerybase_modifiedby](savedquery.md#BKMK_lk_savedquerybase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: savedquery<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedquerybase_modifiedby<br />
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


### <a name="BKMK_lk_MobileOfflineProfile_modifiedby"></a> lk_MobileOfflineProfile_modifiedby

Same as mobileofflineprofile entity [lk_MobileOfflineProfile_modifiedby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_modifiedby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofile<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_MobileOfflineProfile_modifiedby<br />
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


### <a name="BKMK_lk_quarterlyfiscalcalendar_createdby"></a> lk_quarterlyfiscalcalendar_createdby

Same as quarterlyfiscalcalendar entity [lk_quarterlyfiscalcalendar_createdby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_createdby) Many-To-One relationship.

**ReferencingEntity**: quarterlyfiscalcalendar<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_quarterlyfiscalcalendar_createdby<br />
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


### <a name="BKMK_lk_timezonedefinition_modifiedonbehalfby"></a> lk_timezonedefinition_modifiedonbehalfby

Same as timezonedefinition entity [lk_timezonedefinition_modifiedonbehalfby](timezonedefinition.md#BKMK_lk_timezonedefinition_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: timezonedefinition<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonedefinition_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_organization_modifiedonbehalfby"></a> lk_organization_modifiedonbehalfby

Same as organization entity [lk_organization_modifiedonbehalfby](organization.md#BKMK_lk_organization_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: organization<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_organization_modifiedonbehalfby<br />
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


### <a name="BKMK_systemuser_connections1"></a> systemuser_connections1

Same as connection entity [systemuser_connections1](connection.md#BKMK_systemuser_connections1) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record1id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_connections1<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_expanderevent_createdonbehalfby"></a> lk_expanderevent_createdonbehalfby

Same as expanderevent entity [lk_expanderevent_createdonbehalfby](expanderevent.md#BKMK_lk_expanderevent_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: expanderevent<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_expanderevent_createdonbehalfby<br />
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


### <a name="BKMK_lk_SiteMap_modifiedby"></a> lk_SiteMap_modifiedby

Same as sitemap entity [lk_SiteMap_modifiedby](sitemap.md#BKMK_lk_SiteMap_modifiedby) Many-To-One relationship.

**ReferencingEntity**: sitemap<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_SiteMap_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_documenttemplatebase_createdonbehalfby"></a> lk_documenttemplatebase_createdonbehalfby

Same as documenttemplate entity [lk_documenttemplatebase_createdonbehalfby](documenttemplate.md#BKMK_lk_documenttemplatebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: documenttemplate<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_documenttemplatebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_kbarticlebase_createdby"></a> lk_kbarticlebase_createdby

Same as kbarticle entity [lk_kbarticlebase_createdby](kbarticle.md#BKMK_lk_kbarticlebase_createdby) Many-To-One relationship.

**ReferencingEntity**: kbarticle<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticlebase_createdby<br />
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


### <a name="BKMK_lk_emailserverprofile_createdby"></a> lk_emailserverprofile_createdby

Same as emailserverprofile entity [lk_emailserverprofile_createdby](emailserverprofile.md#BKMK_lk_emailserverprofile_createdby) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_emailserverprofile_createdby<br />
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


### <a name="BKMK_lk_azureserviceconnection_modifiedby"></a> lk_azureserviceconnection_modifiedby

Same as azureserviceconnection entity [lk_azureserviceconnection_modifiedby](azureserviceconnection.md#BKMK_lk_azureserviceconnection_modifiedby) Many-To-One relationship.

**ReferencingEntity**: azureserviceconnection<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_azureserviceconnection_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby"></a> lk_quarterlyfiscalcalendar_modifiedonbehalfby

Same as quarterlyfiscalcalendar entity [lk_quarterlyfiscalcalendar_modifiedonbehalfby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: quarterlyfiscalcalendar<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_quarterlyfiscalcalendar_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_userquery_modifiedby"></a> lk_userquery_modifiedby

Same as userquery entity [lk_userquery_modifiedby](userquery.md#BKMK_lk_userquery_modifiedby) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userquery_modifiedby<br />
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


### <a name="BKMK_lk_mobileofflineprofileitemassociation_modifiedby"></a> lk_mobileofflineprofileitemassociation_modifiedby

Same as mobileofflineprofileitemassociation entity [lk_mobileofflineprofileitemassociation_modifiedby](mobileofflineprofileitemassociation.md#BKMK_lk_mobileofflineprofileitemassociation_modifiedby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitemassociation<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mobileofflineprofileitemassocaition_modifiedby<br />
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


### <a name="BKMK_lk_savedorginsightsconfiguration_modifiedby"></a> lk_savedorginsightsconfiguration_modifiedby

Same as savedorginsightsconfiguration entity [lk_savedorginsightsconfiguration_modifiedby](savedorginsightsconfiguration.md#BKMK_lk_savedorginsightsconfiguration_modifiedby) Many-To-One relationship.

**ReferencingEntity**: savedorginsightsconfiguration<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_savedorginsightsconfiguration_modifiedby<br />
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


### <a name="BKMK_lk_knowledgearticleviews_createdonbehalfby"></a> lk_knowledgearticleviews_createdonbehalfby

Same as knowledgearticleviews entity [lk_knowledgearticleviews_createdonbehalfby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticleviews<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticleviews_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_convertrule_createdby"></a> lk_convertrule_createdby

Same as convertrule entity [lk_convertrule_createdby](convertrule.md#BKMK_lk_convertrule_createdby) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_convertrule_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_savedorginsightsconfiguration_modifiedonbehalfby"></a> lk_savedorginsightsconfiguration_modifiedonbehalfby

Same as savedorginsightsconfiguration entity [lk_savedorginsightsconfiguration_modifiedonbehalfby](savedorginsightsconfiguration.md#BKMK_lk_savedorginsightsconfiguration_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: savedorginsightsconfiguration<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedorginsightsconfiguration_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_processtriggerbase_createdonbehalfby"></a> lk_processtriggerbase_createdonbehalfby

Same as processtrigger entity [lk_processtriggerbase_createdonbehalfby](processtrigger.md#BKMK_lk_processtriggerbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: processtrigger<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processtriggerbase_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_sdkmessageprocessingstepimage"></a> modifiedby_sdkmessageprocessingstepimage

Same as sdkmessageprocessingstepimage entity [modifiedby_sdkmessageprocessingstepimage](sdkmessageprocessingstepimage.md#BKMK_modifiedby_sdkmessageprocessingstepimage) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstepimage<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessageprocessingstepimage<br />
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


### <a name="BKMK_lk_phonecall_modifiedonbehalfby"></a> lk_phonecall_modifiedonbehalfby

Same as phonecall entity [lk_phonecall_modifiedonbehalfby](phonecall.md#BKMK_lk_phonecall_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_phonecall_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_workflowlog_createdby"></a> lk_workflowlog_createdby

Same as workflowlog entity [lk_workflowlog_createdby](workflowlog.md#BKMK_lk_workflowlog_createdby) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_workflowlog_createdby<br />
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


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_salespersonid"></a> lk_fixedmonthlyfiscalcalendar_salespersonid

Same as fixedmonthlyfiscalcalendar entity [lk_fixedmonthlyfiscalcalendar_salespersonid](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_salespersonid) Many-To-One relationship.

**ReferencingEntity**: fixedmonthlyfiscalcalendar<br />
**ReferencingAttribute**: salespersonid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fixedmonthlyfiscalcalendar_salespersonid<br />
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


### <a name="BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby"></a> lk_quarterlyfiscalcalendar_createdonbehalfby

Same as quarterlyfiscalcalendar entity [lk_quarterlyfiscalcalendar_createdonbehalfby](quarterlyfiscalcalendar.md#BKMK_lk_quarterlyfiscalcalendar_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: quarterlyfiscalcalendar<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_quarterlyfiscalcalendar_createdonbehalfby<br />
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


### <a name="BKMK_createdby_attributemap"></a> createdby_attributemap

Same as attributemap entity [createdby_attributemap](attributemap.md#BKMK_createdby_attributemap) Many-To-One relationship.

**ReferencingEntity**: attributemap<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_attributemap<br />
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


### <a name="BKMK_lk_teamtemplate_modifiedby"></a> lk_teamtemplate_modifiedby

Same as teamtemplate entity [lk_teamtemplate_modifiedby](teamtemplate.md#BKMK_lk_teamtemplate_modifiedby) Many-To-One relationship.

**ReferencingEntity**: teamtemplate<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_teamtemplate_modifiedby<br />
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


### <a name="BKMK_user_userform"></a> user_userform

Same as userform entity [user_userform](userform.md#BKMK_user_userform) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_userform<br />
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


### <a name="BKMK_lk_processsession_startedby"></a> lk_processsession_startedby

Same as processsession entity [lk_processsession_startedby](processsession.md#BKMK_lk_processsession_startedby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: startedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_startedby<br />
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


### <a name="BKMK_lk_knowledgearticleviews_modifiedonbehalfby"></a> lk_knowledgearticleviews_modifiedonbehalfby

Same as knowledgearticleviews entity [lk_knowledgearticleviews_modifiedonbehalfby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticleviews<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticleviews_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_role_modifiedonbehalfby"></a> lk_role_modifiedonbehalfby

Same as role entity [lk_role_modifiedonbehalfby](role.md#BKMK_lk_role_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: role<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_role_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_SharePointData_modifiedby"></a> lk_SharePointData_modifiedby

Same as sharepointdata entity [lk_SharePointData_modifiedby](sharepointdata.md#BKMK_lk_SharePointData_modifiedby) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_SharePointData_modifiedby<br />
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


### <a name="BKMK_lk_reportbase_modifiedby"></a> lk_reportbase_modifiedby

Same as report entity [lk_reportbase_modifiedby](report.md#BKMK_lk_reportbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: report<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportbase_modifiedby<br />
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


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_createdby"></a> lk_fixedmonthlyfiscalcalendar_createdby

Same as fixedmonthlyfiscalcalendar entity [lk_fixedmonthlyfiscalcalendar_createdby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_createdby) Many-To-One relationship.

**ReferencingEntity**: fixedmonthlyfiscalcalendar<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fixedmonthlyfiscalcalendar_createdby<br />
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


### <a name="BKMK_lk_appconfigmaster_createdby"></a> lk_appconfigmaster_createdby

Same as appconfigmaster entity [lk_appconfigmaster_createdby](appconfigmaster.md#BKMK_lk_appconfigmaster_createdby) Many-To-One relationship.

**ReferencingEntity**: appconfigmaster<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfigmaster_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_sharepointdata_user"></a> lk_sharepointdata_user

Same as sharepointdata entity [lk_sharepointdata_user](sharepointdata.md#BKMK_lk_sharepointdata_user) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: userid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdata_user<br />
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


### <a name="BKMK_lk_businessunitbase_modifiedby"></a> lk_businessunitbase_modifiedby

Same as businessunit entity [lk_businessunitbase_modifiedby](businessunit.md#BKMK_lk_businessunitbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunitbase_modifiedby<br />
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


### <a name="BKMK_socialProfile_owning_user"></a> socialProfile_owning_user

Same as socialprofile entity [socialProfile_owning_user](socialprofile.md#BKMK_socialProfile_owning_user) Many-To-One relationship.

**ReferencingEntity**: socialprofile<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: socialProfile_owning_user<br />
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


### <a name="BKMK_lk_businessprocessflowinstancebase_modifiedonbehalfby"></a> lk_businessprocessflowinstancebase_modifiedonbehalfby

Same as businessprocessflowinstance entity [lk_businessprocessflowinstancebase_modifiedonbehalfby](businessprocessflowinstance.md#BKMK_lk_businessprocessflowinstancebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: businessprocessflowinstance<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessprocessflowinstancebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_task_modifiedby"></a> lk_task_modifiedby

Same as task entity [lk_task_modifiedby](task.md#BKMK_lk_task_modifiedby) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_task_modifiedby<br />
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


### <a name="BKMK_lk_slaitembase_createdby"></a> lk_slaitembase_createdby

Same as slaitem entity [lk_slaitembase_createdby](slaitem.md#BKMK_lk_slaitembase_createdby) Many-To-One relationship.

**ReferencingEntity**: slaitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slaitembase_createdby<br />
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


### <a name="BKMK_lk_mailboxtrackingfolder_createdonbehalfby"></a> lk_mailboxtrackingfolder_createdonbehalfby

Same as mailboxtrackingfolder entity [lk_mailboxtrackingfolder_createdonbehalfby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailboxtrackingfolder_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_isvconfigbase_createdby"></a> lk_isvconfigbase_createdby

Same as isvconfig entity [lk_isvconfigbase_createdby](isvconfig.md#BKMK_lk_isvconfigbase_createdby) Many-To-One relationship.

**ReferencingEntity**: isvconfig<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_isvconfigbase_createdby<br />
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


### <a name="BKMK_modifiedby_sdkmessageprocessingstep"></a> modifiedby_sdkmessageprocessingstep

Same as sdkmessageprocessingstep entity [modifiedby_sdkmessageprocessingstep](sdkmessageprocessingstep.md#BKMK_modifiedby_sdkmessageprocessingstep) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessageprocessingstep<br />
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


### <a name="BKMK_lk_reportvisibilitybase_createdby"></a> lk_reportvisibilitybase_createdby

Same as reportvisibility entity [lk_reportvisibilitybase_createdby](reportvisibility.md#BKMK_lk_reportvisibilitybase_createdby) Many-To-One relationship.

**ReferencingEntity**: reportvisibility<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportvisibilitybase_createdby<br />
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


### <a name="BKMK_lk_duplicaterulebase_modifiedby"></a> lk_duplicaterulebase_modifiedby

Same as duplicaterule entity [lk_duplicaterulebase_modifiedby](duplicaterule.md#BKMK_lk_duplicaterulebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicaterulebase_modifiedby<br />
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


### <a name="BKMK_lk_recurrencerulebase_createdonbehalfby"></a> lk_recurrencerulebase_createdonbehalfby

Same as recurrencerule entity [lk_recurrencerulebase_createdonbehalfby](recurrencerule.md#BKMK_lk_recurrencerulebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: recurrencerule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_recurrencerulebase_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_relationship_role_map"></a> modifiedby_relationship_role_map

Same as relationshiprolemap entity [modifiedby_relationship_role_map](relationshiprolemap.md#BKMK_modifiedby_relationship_role_map) Many-To-One relationship.

**ReferencingEntity**: relationshiprolemap<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_relationship_role_map<br />
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


### <a name="BKMK_lk_organizationbase_modifiedby"></a> lk_organizationbase_modifiedby

Same as organization entity [lk_organizationbase_modifiedby](organization.md#BKMK_lk_organizationbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: organization<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_organizationbase_modifiedby<br />
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


### <a name="BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby"></a> lk_mailboxtrackingfolder_modifiedonbehalfby

Same as mailboxtrackingfolder entity [lk_mailboxtrackingfolder_modifiedonbehalfby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailboxtrackingfolder_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_task_createdby"></a> lk_task_createdby

Same as task entity [lk_task_createdby](task.md#BKMK_lk_task_createdby) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_task_createdby<br />
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


### <a name="BKMK_lk_mailboxtrackingfolder_createdby"></a> lk_mailboxtrackingfolder_createdby

Same as mailboxtrackingfolder entity [lk_mailboxtrackingfolder_createdby](mailboxtrackingfolder.md#BKMK_lk_mailboxtrackingfolder_createdby) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailboxtrackingfolder_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_personaldocumenttemplatebase_modifiedby"></a> lk_personaldocumenttemplatebase_modifiedby

Same as personaldocumenttemplate entity [lk_personaldocumenttemplatebase_modifiedby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: personaldocumenttemplate<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_personaldocumenttemplatebase_modifiedby<br />
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


### <a name="BKMK_lk_processtriggerbase_modifiedby"></a> lk_processtriggerbase_modifiedby

Same as processtrigger entity [lk_processtriggerbase_modifiedby](processtrigger.md#BKMK_lk_processtriggerbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: processtrigger<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_processtriggerbase_modifiedby<br />
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


### <a name="BKMK_userentityuisettings_owning_user"></a> userentityuisettings_owning_user

Same as userentityuisettings entity [userentityuisettings_owning_user](userentityuisettings.md#BKMK_userentityuisettings_owning_user) Many-To-One relationship.

**ReferencingEntity**: userentityuisettings<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityuisettings_owning_user<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_userquery_createdby"></a> lk_userquery_createdby

Same as userquery entity [lk_userquery_createdby](userquery.md#BKMK_lk_userquery_createdby) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userquery_createdby<br />
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


### <a name="BKMK_contact_owning_user"></a> contact_owning_user

Same as contact entity [contact_owning_user](contact.md#BKMK_contact_owning_user) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: contact_owning_user<br />
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


### <a name="BKMK_lk_mailmergetemplate_createdonbehalfby"></a> lk_mailmergetemplate_createdonbehalfby

Same as mailmergetemplate entity [lk_mailmergetemplate_createdonbehalfby](mailmergetemplate.md#BKMK_lk_mailmergetemplate_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mailmergetemplate<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailmergetemplate_createdonbehalfby<br />
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


### <a name="BKMK_lk_importjobbase_modifiedonbehalfby"></a> lk_importjobbase_modifiedonbehalfby

Same as importjob entity [lk_importjobbase_modifiedonbehalfby](importjob.md#BKMK_lk_importjobbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importjob<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importjobbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_customcontroldefaultconfig_createdby"></a> lk_customcontroldefaultconfig_createdby

Same as customcontroldefaultconfig entity [lk_customcontroldefaultconfig_createdby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_createdby) Many-To-One relationship.

**ReferencingEntity**: customcontroldefaultconfig<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontroldefaultconfig_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_savedquery_createdonbehalfby"></a> lk_savedquery_createdonbehalfby

Same as savedquery entity [lk_savedquery_createdonbehalfby](savedquery.md#BKMK_lk_savedquery_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: savedquery<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedquery_createdonbehalfby<br />
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


### <a name="BKMK_system_user_accounts"></a> system_user_accounts

Same as account entity [system_user_accounts](account.md#BKMK_system_user_accounts) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: preferredsystemuserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: system_user_accounts<br />
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


### <a name="BKMK_lk_systemuser_createdonbehalfby"></a> lk_systemuser_createdonbehalfby

Same as systemuser entity [lk_systemuser_createdonbehalfby](systemuser.md#BKMK_lk_systemuser_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_systemuser_createdonbehalfby<br />
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


### <a name="BKMK_lk_customcontrol_modifiedonbehalfby"></a> lk_customcontrol_modifiedonbehalfby

Same as customcontrol entity [lk_customcontrol_modifiedonbehalfby](customcontrol.md#BKMK_lk_customcontrol_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customcontrol<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrol_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_appointment_modifiedonbehalfby"></a> lk_appointment_modifiedonbehalfby

Same as appointment entity [lk_appointment_modifiedonbehalfby](appointment.md#BKMK_lk_appointment_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_appointment_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_externalpartyitem_createdby"></a> lk_externalpartyitem_createdby

Same as externalpartyitem entity [lk_externalpartyitem_createdby](externalpartyitem.md#BKMK_lk_externalpartyitem_createdby) Many-To-One relationship.

**ReferencingEntity**: externalpartyitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_externalpartyitem_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_knowledgearticleviews_modifiedby"></a> lk_knowledgearticleviews_modifiedby

Same as knowledgearticleviews entity [lk_knowledgearticleviews_modifiedby](knowledgearticleviews.md#BKMK_lk_knowledgearticleviews_modifiedby) Many-To-One relationship.

**ReferencingEntity**: knowledgearticleviews<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgearticleviews_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_appconfigmaster_modifiedonbehalfby"></a> lk_appconfigmaster_modifiedonbehalfby

Same as appconfigmaster entity [lk_appconfigmaster_modifiedonbehalfby](appconfigmaster.md#BKMK_lk_appconfigmaster_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appconfigmaster<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfigmaster_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_importbase_createdby"></a> lk_importbase_createdby

Same as import entity [lk_importbase_createdby](import.md#BKMK_lk_importbase_createdby) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importbase_createdby<br />
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


### <a name="BKMK_lk_ACIViewMapper_modifiedonbehalfby"></a> lk_ACIViewMapper_modifiedonbehalfby

Same as aciviewmapper entity [lk_ACIViewMapper_modifiedonbehalfby](aciviewmapper.md#BKMK_lk_ACIViewMapper_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: aciviewmapper<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ACIViewMapper_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_solutionbase_modifiedonbehalfby"></a> lk_solutionbase_modifiedonbehalfby

Same as solution entity [lk_solutionbase_modifiedonbehalfby](solution.md#BKMK_lk_solutionbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: solution<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_solutionbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_DisplayStringbase_modifiedonbehalfby"></a> lk_DisplayStringbase_modifiedonbehalfby

Same as displaystring entity [lk_DisplayStringbase_modifiedonbehalfby](displaystring.md#BKMK_lk_DisplayStringbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: displaystring<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_DisplayStringbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_annotationbase_modifiedby"></a> lk_annotationbase_modifiedby

Same as annotation entity [lk_annotationbase_modifiedby](annotation.md#BKMK_lk_annotationbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annotationbase_modifiedby<br />
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


### <a name="BKMK_lk_timezonerule_modifiedonbehalfby"></a> lk_timezonerule_modifiedonbehalfby

Same as timezonerule entity [lk_timezonerule_modifiedonbehalfby](timezonerule.md#BKMK_lk_timezonerule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: timezonerule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonerule_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_importjobbase_createdby"></a> lk_importjobbase_createdby

Same as importjob entity [lk_importjobbase_createdby](importjob.md#BKMK_lk_importjobbase_createdby) Many-To-One relationship.

**ReferencingEntity**: importjob<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importjobbase_createdby<br />
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


### <a name="BKMK_lk_socialinsightsconfiguration_createdonbehalfby"></a> lk_socialinsightsconfiguration_createdonbehalfby

Same as socialinsightsconfiguration entity [lk_socialinsightsconfiguration_createdonbehalfby](socialinsightsconfiguration.md#BKMK_lk_socialinsightsconfiguration_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: socialinsightsconfiguration<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_socialinsightsconfiguration_createdonbehalfby<br />
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


### <a name="BKMK_lk_feedback_createdby"></a> lk_feedback_createdby

Same as feedback entity [lk_feedback_createdby](feedback.md#BKMK_lk_feedback_createdby) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_feedback_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_timezonelocalizedname_modifiedby"></a> lk_timezonelocalizedname_modifiedby

Same as timezonelocalizedname entity [lk_timezonelocalizedname_modifiedby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_modifiedby) Many-To-One relationship.

**ReferencingEntity**: timezonelocalizedname<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonelocalizedname_modifiedby<br />
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


### <a name="BKMK_createdby_sdkmessagepair"></a> createdby_sdkmessagepair

Same as sdkmessagepair entity [createdby_sdkmessagepair](sdkmessagepair.md#BKMK_createdby_sdkmessagepair) Many-To-One relationship.

**ReferencingEntity**: sdkmessagepair<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessagepair<br />
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


### <a name="BKMK_lk_mailmergetemplatebase_createdby"></a> lk_mailmergetemplatebase_createdby

Same as mailmergetemplate entity [lk_mailmergetemplatebase_createdby](mailmergetemplate.md#BKMK_lk_mailmergetemplatebase_createdby) Many-To-One relationship.

**ReferencingEntity**: mailmergetemplate<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailmergetemplatebase_createdby<br />
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


### <a name="BKMK_createdby_pluginassembly"></a> createdby_pluginassembly

Same as pluginassembly entity [createdby_pluginassembly](pluginassembly.md#BKMK_createdby_pluginassembly) Many-To-One relationship.

**ReferencingEntity**: pluginassembly<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_pluginassembly<br />
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


### <a name="BKMK_lk_appconfiginstance_modifiedonbehalfby"></a> lk_appconfiginstance_modifiedonbehalfby

Same as appconfiginstance entity [lk_appconfiginstance_modifiedonbehalfby](appconfiginstance.md#BKMK_lk_appconfiginstance_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appconfiginstance<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfiginstance_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_userform_modifiedby"></a> lk_userform_modifiedby

Same as userform entity [lk_userform_modifiedby](userform.md#BKMK_lk_userform_modifiedby) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userform_modifiedby<br />
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


### <a name="BKMK_lk_ChannelPropertyGroup_createdby"></a> lk_ChannelPropertyGroup_createdby

Same as channelpropertygroup entity [lk_ChannelPropertyGroup_createdby](channelpropertygroup.md#BKMK_lk_ChannelPropertyGroup_createdby) Many-To-One relationship.

**ReferencingEntity**: channelpropertygroup<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelPropertyGroup_createdby<br />
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


### <a name="BKMK_lk_publisherbase_createdonbehalfby"></a> lk_publisherbase_createdonbehalfby

Same as publisher entity [lk_publisherbase_createdonbehalfby](publisher.md#BKMK_lk_publisherbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: publisher<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisherbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessageresponse_createdonbehalfby"></a> lk_sdkmessageresponse_createdonbehalfby

Same as sdkmessageresponse entity [lk_sdkmessageresponse_createdonbehalfby](sdkmessageresponse.md#BKMK_lk_sdkmessageresponse_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponse<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageresponse_createdonbehalfby<br />
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


### <a name="BKMK_lk_recurrencerule_createdby"></a> lk_recurrencerule_createdby

Same as recurrencerule entity [lk_recurrencerule_createdby](recurrencerule.md#BKMK_lk_recurrencerule_createdby) Many-To-One relationship.

**ReferencingEntity**: recurrencerule<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_recurrencerule_createdby<br />
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


### <a name="BKMK_lk_slakpiinstancebase_modifiedonbehalfby"></a> lk_slakpiinstancebase_modifiedonbehalfby

Same as slakpiinstance entity [lk_slakpiinstancebase_modifiedonbehalfby](slakpiinstance.md#BKMK_lk_slakpiinstancebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slakpiinstancebase_modifiedonbehalfby<br />
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


### <a name="BKMK_SystemUser_ImportFiles"></a> SystemUser_ImportFiles

Same as importfile entity [SystemUser_ImportFiles](importfile.md#BKMK_SystemUser_ImportFiles) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_ImportFiles<br />
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


### <a name="BKMK_lk_sdkmessageresponse_modifiedonbehalfby"></a> lk_sdkmessageresponse_modifiedonbehalfby

Same as sdkmessageresponse entity [lk_sdkmessageresponse_modifiedonbehalfby](sdkmessageresponse.md#BKMK_lk_sdkmessageresponse_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponse<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageresponse_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_processsession_modifiedby"></a> lk_processsession_modifiedby

Same as processsession entity [lk_processsession_modifiedby](processsession.md#BKMK_lk_processsession_modifiedby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_modifiedby<br />
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


### <a name="BKMK_lk_translationprocess_modifiedby"></a> lk_translationprocess_modifiedby

Same as translationprocess entity [lk_translationprocess_modifiedby](translationprocess.md#BKMK_lk_translationprocess_modifiedby) Many-To-One relationship.

**ReferencingEntity**: translationprocess<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_translationprocess_modifiedby<br />
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


### <a name="BKMK_lk_offlinecommanddefinition_modifiedby"></a> lk_offlinecommanddefinition_modifiedby

Same as offlinecommanddefinition entity [lk_offlinecommanddefinition_modifiedby](offlinecommanddefinition.md#BKMK_lk_offlinecommanddefinition_modifiedby) Many-To-One relationship.

**ReferencingEntity**: offlinecommanddefinition<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_offlinecommanddefinition_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_annualfiscalcalendar_modifiedby"></a> lk_annualfiscalcalendar_modifiedby

Same as annualfiscalcalendar entity [lk_annualfiscalcalendar_modifiedby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_modifiedby) Many-To-One relationship.

**ReferencingEntity**: annualfiscalcalendar<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annualfiscalcalendar_modifiedby<br />
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


### <a name="BKMK_user_task"></a> user_task

Same as task entity [user_task](task.md#BKMK_user_task) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_task<br />
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


### <a name="BKMK_lk_recurrencerulebase_modifiedonbehalfby"></a> lk_recurrencerulebase_modifiedonbehalfby

Same as recurrencerule entity [lk_recurrencerulebase_modifiedonbehalfby](recurrencerule.md#BKMK_lk_recurrencerulebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: recurrencerule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_recurrencerulebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_phonecall_createdby"></a> lk_phonecall_createdby

Same as phonecall entity [lk_phonecall_createdby](phonecall.md#BKMK_lk_phonecall_createdby) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_phonecall_createdby<br />
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


### <a name="BKMK_lk_templatebase_modifiedonbehalfby"></a> lk_templatebase_modifiedonbehalfby

Same as template entity [lk_templatebase_modifiedonbehalfby](template.md#BKMK_lk_templatebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_templatebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_advancedsimilarityrule_modifiedby"></a> lk_advancedsimilarityrule_modifiedby

Same as advancedsimilarityrule entity [lk_advancedsimilarityrule_modifiedby](advancedsimilarityrule.md#BKMK_lk_advancedsimilarityrule_modifiedby) Many-To-One relationship.

**ReferencingEntity**: advancedsimilarityrule<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_advancedsimilarityrule_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_fax_modifiedonbehalfby"></a> lk_fax_modifiedonbehalfby

Same as fax entity [lk_fax_modifiedonbehalfby](fax.md#BKMK_lk_fax_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_fax_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_isvconfigbase_modifiedby"></a> lk_isvconfigbase_modifiedby

Same as isvconfig entity [lk_isvconfigbase_modifiedby](isvconfig.md#BKMK_lk_isvconfigbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: isvconfig<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_isvconfigbase_modifiedby<br />
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


### <a name="BKMK_lk_relationshiprolemap_modifiedonbehalfby"></a> lk_relationshiprolemap_modifiedonbehalfby

Same as relationshiprolemap entity [lk_relationshiprolemap_modifiedonbehalfby](relationshiprolemap.md#BKMK_lk_relationshiprolemap_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: relationshiprolemap<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_relationshiprolemap_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_contact_createdonbehalfby"></a> lk_contact_createdonbehalfby

Same as contact entity [lk_contact_createdonbehalfby](contact.md#BKMK_lk_contact_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_contact_createdonbehalfby<br />
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


### <a name="BKMK_lk_customcontroldefaultconfig_createdonbehalfby"></a> lk_customcontroldefaultconfig_createdonbehalfby

Same as customcontroldefaultconfig entity [lk_customcontroldefaultconfig_createdonbehalfby](customcontroldefaultconfig.md#BKMK_lk_customcontroldefaultconfig_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customcontroldefaultconfig<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontroldefaultconfig_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_publisheraddressbase_createdonbehalfby"></a> lk_publisheraddressbase_createdonbehalfby

Same as publisheraddress entity [lk_publisheraddressbase_createdonbehalfby](publisheraddress.md#BKMK_lk_publisheraddressbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: publisheraddress<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisheraddressbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_annualfiscalcalendar_modifiedonbehalfby"></a> lk_annualfiscalcalendar_modifiedonbehalfby

Same as annualfiscalcalendar entity [lk_annualfiscalcalendar_modifiedonbehalfby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: annualfiscalcalendar<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annualfiscalcalendar_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_semiannualfiscalcalendar_modifiedby"></a> lk_semiannualfiscalcalendar_modifiedby

Same as semiannualfiscalcalendar entity [lk_semiannualfiscalcalendar_modifiedby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_modifiedby) Many-To-One relationship.

**ReferencingEntity**: semiannualfiscalcalendar<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_semiannualfiscalcalendar_modifiedby<br />
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


### <a name="BKMK_lk_socialactivity_createdby"></a> lk_socialactivity_createdby

Same as socialactivity entity [lk_socialactivity_createdby](socialactivity.md#BKMK_lk_socialactivity_createdby) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_socialactivity_createdby<br />
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


### <a name="BKMK_lk_SiteMap_createdby"></a> lk_SiteMap_createdby

Same as sitemap entity [lk_SiteMap_createdby](sitemap.md#BKMK_lk_SiteMap_createdby) Many-To-One relationship.

**ReferencingEntity**: sitemap<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_SiteMap_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_syncerrorbase_modifiedby"></a> lk_syncerrorbase_modifiedby

Same as syncerror entity [lk_syncerrorbase_modifiedby](syncerror.md#BKMK_lk_syncerrorbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_syncerrorbase_modifiedby<br />
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


### <a name="BKMK_lk_emailsignaturebase_createdonbehalfby"></a> lk_emailsignaturebase_createdonbehalfby

Same as emailsignature entity [lk_emailsignaturebase_createdonbehalfby](emailsignature.md#BKMK_lk_emailsignaturebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: emailsignature<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_emailsignaturebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_calendar_createdby"></a> lk_calendar_createdby

Same as calendar entity [lk_calendar_createdby](calendar.md#BKMK_lk_calendar_createdby) Many-To-One relationship.

**ReferencingEntity**: calendar<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_calendar_createdby<br />
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


### <a name="BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby"></a> lk_semiannualfiscalcalendar_modifiedonbehalfby

Same as semiannualfiscalcalendar entity [lk_semiannualfiscalcalendar_modifiedonbehalfby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: semiannualfiscalcalendar<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_semiannualfiscalcalendar_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_modifiedby"></a> lk_fixedmonthlyfiscalcalendar_modifiedby

Same as fixedmonthlyfiscalcalendar entity [lk_fixedmonthlyfiscalcalendar_modifiedby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_modifiedby) Many-To-One relationship.

**ReferencingEntity**: fixedmonthlyfiscalcalendar<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fixedmonthlyfiscalcalendar_modifiedby<br />
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


### <a name="BKMK_SystemUser_DuplicateBaseRecord"></a> SystemUser_DuplicateBaseRecord

Same as duplicaterecord entity [SystemUser_DuplicateBaseRecord](duplicaterecord.md#BKMK_SystemUser_DuplicateBaseRecord) Many-To-One relationship.

**ReferencingEntity**: duplicaterecord<br />
**ReferencingAttribute**: baserecordid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_DuplicateBaseRecord<br />
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


### <a name="BKMK_lk_importentitymapping_createdby"></a> lk_importentitymapping_createdby

Same as importentitymapping entity [lk_importentitymapping_createdby](importentitymapping.md#BKMK_lk_importentitymapping_createdby) Many-To-One relationship.

**ReferencingEntity**: importentitymapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importentitymapping_createdby<br />
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


### <a name="BKMK_lk_queueitembase_createdby"></a> lk_queueitembase_createdby

Same as queueitem entity [lk_queueitembase_createdby](queueitem.md#BKMK_lk_queueitembase_createdby) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queueitembase_createdby<br />
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


### <a name="BKMK_lk_sdkmessage_createdonbehalfby"></a> lk_sdkmessage_createdonbehalfby

Same as sdkmessage entity [lk_sdkmessage_createdonbehalfby](sdkmessage.md#BKMK_lk_sdkmessage_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessage<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessage_createdonbehalfby<br />
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


### <a name="BKMK_createdby_plugintypestatistic"></a> createdby_plugintypestatistic

Same as plugintypestatistic entity [createdby_plugintypestatistic](plugintypestatistic.md#BKMK_createdby_plugintypestatistic) Many-To-One relationship.

**ReferencingEntity**: plugintypestatistic<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_plugintypestatistic<br />
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


### <a name="BKMK_createdby_sdkmessagerequest"></a> createdby_sdkmessagerequest

Same as sdkmessagerequest entity [createdby_sdkmessagerequest](sdkmessagerequest.md#BKMK_createdby_sdkmessagerequest) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequest<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessagerequest<br />
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


### <a name="BKMK_lk_picklistmapping_modifiedby"></a> lk_picklistmapping_modifiedby

Same as picklistmapping entity [lk_picklistmapping_modifiedby](picklistmapping.md#BKMK_lk_picklistmapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: picklistmapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_picklistmapping_modifiedby<br />
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


### <a name="BKMK_lk_sdkmessagerequest_modifiedonbehalfby"></a> lk_sdkmessagerequest_modifiedonbehalfby

Same as sdkmessagerequest entity [lk_sdkmessagerequest_modifiedonbehalfby](sdkmessagerequest.md#BKMK_lk_sdkmessagerequest_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequest<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagerequest_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_team_modifiedonbehalfby"></a> lk_team_modifiedonbehalfby

Same as team entity [lk_team_modifiedonbehalfby](team.md#BKMK_lk_team_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_team_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_advancedsimilarityrule_modifiedonbehalfby"></a> lk_advancedsimilarityrule_modifiedonbehalfby

Same as advancedsimilarityrule entity [lk_advancedsimilarityrule_modifiedonbehalfby](advancedsimilarityrule.md#BKMK_lk_advancedsimilarityrule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: advancedsimilarityrule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_advancedsimilarityrule_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_businessunitnewsarticle_modifiedonbehalfby"></a> lk_businessunitnewsarticle_modifiedonbehalfby

Same as businessunitnewsarticle entity [lk_businessunitnewsarticle_modifiedonbehalfby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticle_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: businessunitnewsarticle<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunitnewsarticle_modifiedonbehalfby<br />
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


### <a name="BKMK_SystemUser_ImportLogs"></a> SystemUser_ImportLogs

Same as importlog entity [SystemUser_ImportLogs](importlog.md#BKMK_SystemUser_ImportLogs) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_ImportLogs<br />
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


### <a name="BKMK_lk_plugintypestatisticbase_modifiedonbehalfby"></a> lk_plugintypestatisticbase_modifiedonbehalfby

Same as plugintypestatistic entity [lk_plugintypestatisticbase_modifiedonbehalfby](plugintypestatistic.md#BKMK_lk_plugintypestatisticbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: plugintypestatistic<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_plugintypestatisticbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_tracelog_createdby"></a> lk_tracelog_createdby

Same as tracelog entity [lk_tracelog_createdby](tracelog.md#BKMK_lk_tracelog_createdby) Many-To-One relationship.

**ReferencingEntity**: tracelog<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_tracelog_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_teambase_administratorid"></a> lk_teambase_administratorid

Same as team entity [lk_teambase_administratorid](team.md#BKMK_lk_teambase_administratorid) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: administratorid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_teambase_administratorid<br />
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


### <a name="BKMK_lk_SharePointData_createdby"></a> lk_SharePointData_createdby

Same as sharepointdata entity [lk_SharePointData_createdby](sharepointdata.md#BKMK_lk_SharePointData_createdby) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_SharePointData_createdby<br />
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


### <a name="BKMK_lk_reportentity_modifiedonbehalfby"></a> lk_reportentity_modifiedonbehalfby

Same as reportentity entity [lk_reportentity_modifiedonbehalfby](reportentity.md#BKMK_lk_reportentity_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportentity<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportentity_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_isvconfig_modifiedonbehalfby"></a> lk_isvconfig_modifiedonbehalfby

Same as isvconfig entity [lk_isvconfig_modifiedonbehalfby](isvconfig.md#BKMK_lk_isvconfig_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: isvconfig<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_isvconfig_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_savedqueryvisualizationbase_createdby"></a> lk_savedqueryvisualizationbase_createdby

Same as savedqueryvisualization entity [lk_savedqueryvisualizationbase_createdby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_createdby) Many-To-One relationship.

**ReferencingEntity**: savedqueryvisualization<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedqueryvisualizationbase_createdby<br />
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


### <a name="BKMK_knowledgearticle_primaryauthorid"></a> knowledgearticle_primaryauthorid

Same as knowledgearticle entity [knowledgearticle_primaryauthorid](knowledgearticle.md#BKMK_knowledgearticle_primaryauthorid) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: primaryauthorid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: knowledgearticle_primaryauthorid<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_fixedmonthlyfiscalcalendar_createdonbehalfby"></a> lk_fixedmonthlyfiscalcalendar_createdonbehalfby

Same as fixedmonthlyfiscalcalendar entity [lk_fixedmonthlyfiscalcalendar_createdonbehalfby](fixedmonthlyfiscalcalendar.md#BKMK_lk_fixedmonthlyfiscalcalendar_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: fixedmonthlyfiscalcalendar<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fixedmonthlyfiscalcalendar_createdonbehalfby<br />
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


### <a name="BKMK_lk_offlinecommanddefinition_modifiedonbehalfby"></a> lk_offlinecommanddefinition_modifiedonbehalfby

Same as offlinecommanddefinition entity [lk_offlinecommanddefinition_modifiedonbehalfby](offlinecommanddefinition.md#BKMK_lk_offlinecommanddefinition_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: offlinecommanddefinition<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_offlinecommanddefinition_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_email_createdby"></a> lk_email_createdby

Same as email entity [lk_email_createdby](email.md#BKMK_lk_email_createdby) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_email_createdby<br />
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


### <a name="BKMK_lk_monthlyfiscalcalendar_createdby"></a> lk_monthlyfiscalcalendar_createdby

Same as monthlyfiscalcalendar entity [lk_monthlyfiscalcalendar_createdby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_createdby) Many-To-One relationship.

**ReferencingEntity**: monthlyfiscalcalendar<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_monthlyfiscalcalendar_createdby<br />
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


### <a name="BKMK_lk_routingruleitem_modifiedonbehalfby"></a> lk_routingruleitem_modifiedonbehalfby

Same as routingruleitem entity [lk_routingruleitem_modifiedonbehalfby](routingruleitem.md#BKMK_lk_routingruleitem_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingruleitem_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_queuebase_createdby"></a> lk_queuebase_createdby

Same as queue entity [lk_queuebase_createdby](queue.md#BKMK_lk_queuebase_createdby) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queuebase_createdby<br />
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


### <a name="BKMK_lk_appmodulecomponent_createdonbehalfby"></a> lk_appmodulecomponent_createdonbehalfby

Same as appmodulecomponent entity [lk_appmodulecomponent_createdonbehalfby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appmodulecomponent<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_appmodulecomponent_createdonbehalfby<br />
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


### <a name="BKMK_lk_personaldocumenttemplatebase_createdonbehalfby"></a> lk_personaldocumenttemplatebase_createdonbehalfby

Same as personaldocumenttemplate entity [lk_personaldocumenttemplatebase_createdonbehalfby](personaldocumenttemplate.md#BKMK_lk_personaldocumenttemplatebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: personaldocumenttemplate<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_personaldocumenttemplatebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_savedqueryvisualizationbase_createdonbehalfby"></a> lk_savedqueryvisualizationbase_createdonbehalfby

Same as savedqueryvisualization entity [lk_savedqueryvisualizationbase_createdonbehalfby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: savedqueryvisualization<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedqueryvisualizationbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_newprocess_createdby"></a> lk_newprocess_createdby

Same as newprocess entity [lk_newprocess_createdby](newprocess.md#BKMK_lk_newprocess_createdby) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_newprocess_createdby<br />
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


### <a name="BKMK_lk_category_createdonbehalfby"></a> lk_category_createdonbehalfby

Same as category entity [lk_category_createdonbehalfby](category.md#BKMK_lk_category_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: category<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_category_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_sharepointdocumentbase_modifiedby"></a> lk_sharepointdocumentbase_modifiedby

Same as sharepointdocument entity [lk_sharepointdocumentbase_modifiedby](sharepointdocument.md#BKMK_lk_sharepointdocumentbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentbase_modifiedby<br />
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


### <a name="BKMK_lk_newprocess_modifiedonbehalfby"></a> lk_newprocess_modifiedonbehalfby

Same as newprocess entity [lk_newprocess_modifiedonbehalfby](newprocess.md#BKMK_lk_newprocess_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_newprocess_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_feedback_closedby"></a> lk_feedback_closedby

Same as feedback entity [lk_feedback_closedby](feedback.md#BKMK_lk_feedback_closedby) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: closedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_feedback_closedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_expanderevent_modifiedonbehalfby"></a> lk_expanderevent_modifiedonbehalfby

Same as expanderevent entity [lk_expanderevent_modifiedonbehalfby](expanderevent.md#BKMK_lk_expanderevent_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: expanderevent<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_expanderevent_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_semiannualfiscalcalendar_createdby"></a> lk_semiannualfiscalcalendar_createdby

Same as semiannualfiscalcalendar entity [lk_semiannualfiscalcalendar_createdby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_createdby) Many-To-One relationship.

**ReferencingEntity**: semiannualfiscalcalendar<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_semiannualfiscalcalendar_createdby<br />
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


### <a name="BKMK_lk_duplicateruleconditionbase_modifiedby"></a> lk_duplicateruleconditionbase_modifiedby

Same as duplicaterulecondition entity [lk_duplicateruleconditionbase_modifiedby](duplicaterulecondition.md#BKMK_lk_duplicateruleconditionbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: duplicaterulecondition<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicateruleconditionbase_modifiedby<br />
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


### <a name="BKMK_queue_primary_user"></a> queue_primary_user

Same as queue entity [queue_primary_user](queue.md#BKMK_queue_primary_user) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: primaryuserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: queue_primary_user<br />
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


### <a name="BKMK_lk_emailsignaturebase_createdby"></a> lk_emailsignaturebase_createdby

Same as emailsignature entity [lk_emailsignaturebase_createdby](emailsignature.md#BKMK_lk_emailsignaturebase_createdby) Many-To-One relationship.

**ReferencingEntity**: emailsignature<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_emailsignaturebase_createdby<br />
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


### <a name="BKMK_user_email"></a> user_email

Same as email entity [user_email](email.md#BKMK_user_email) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_email<br />
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


### <a name="BKMK_lk_reportbase_createdby"></a> lk_reportbase_createdby

Same as report entity [lk_reportbase_createdby](report.md#BKMK_lk_reportbase_createdby) Many-To-One relationship.

**ReferencingEntity**: report<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportbase_createdby<br />
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


### <a name="BKMK_lk_appointment_createdby"></a> lk_appointment_createdby

Same as appointment entity [lk_appointment_createdby](appointment.md#BKMK_lk_appointment_createdby) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_appointment_createdby<br />
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


### <a name="BKMK_lk_letter_modifiedby"></a> lk_letter_modifiedby

Same as letter entity [lk_letter_modifiedby](letter.md#BKMK_lk_letter_modifiedby) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_letter_modifiedby<br />
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


### <a name="BKMK_lk_customcontrol_createdonbehalfby"></a> lk_customcontrol_createdonbehalfby

Same as customcontrol entity [lk_customcontrol_createdonbehalfby](customcontrol.md#BKMK_lk_customcontrol_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: customcontrol<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrol_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_usersettingsbase_modifiedby"></a> lk_usersettingsbase_modifiedby

Same as usersettings entity [lk_usersettingsbase_modifiedby](usersettings.md#BKMK_lk_usersettingsbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_usersettingsbase_modifiedby<br />
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


### <a name="BKMK_lk_reportvisibility_modifiedonbehalfby"></a> lk_reportvisibility_modifiedonbehalfby

Same as reportvisibility entity [lk_reportvisibility_modifiedonbehalfby](reportvisibility.md#BKMK_lk_reportvisibility_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportvisibility<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportvisibility_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_queueitembase_modifiedby"></a> lk_queueitembase_modifiedby

Same as queueitem entity [lk_queueitembase_modifiedby](queueitem.md#BKMK_lk_queueitembase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: queueitem<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queueitembase_modifiedby<br />
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


### <a name="BKMK_userentityinstancedata_owning_user"></a> userentityinstancedata_owning_user

Same as userentityinstancedata entity [userentityinstancedata_owning_user](userentityinstancedata.md#BKMK_userentityinstancedata_owning_user) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_owning_user<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby"></a> lk_sdkmessageprocessingstep_modifiedonbehalfby

Same as sdkmessageprocessingstep entity [lk_sdkmessageprocessingstep_modifiedonbehalfby](sdkmessageprocessingstep.md#BKMK_lk_sdkmessageprocessingstep_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageprocessingstep_modifiedonbehalfby<br />
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


### <a name="BKMK_modifiedby_pluginassembly"></a> modifiedby_pluginassembly

Same as pluginassembly entity [modifiedby_pluginassembly](pluginassembly.md#BKMK_modifiedby_pluginassembly) Many-To-One relationship.

**ReferencingEntity**: pluginassembly<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_pluginassembly<br />
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


### <a name="BKMK_lk_businessprocessflowinstancebase_modifiedby"></a> lk_businessprocessflowinstancebase_modifiedby

Same as businessprocessflowinstance entity [lk_businessprocessflowinstancebase_modifiedby](businessprocessflowinstance.md#BKMK_lk_businessprocessflowinstancebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: businessprocessflowinstance<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessprocessflowinstancebase_modifiedby<br />
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


### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedby"></a> lk_sharepointdocumentlocationbase_modifiedby

Same as sharepointdocumentlocation entity [lk_sharepointdocumentlocationbase_modifiedby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentlocationbase_modifiedby<br />
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


### <a name="BKMK_system_user_activity_parties"></a> system_user_activity_parties

Same as activityparty entity [system_user_activity_parties](activityparty.md#BKMK_system_user_activity_parties) Many-To-One relationship.

**ReferencingEntity**: activityparty<br />
**ReferencingAttribute**: partyid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: system_user_activity_parties<br />
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


### <a name="BKMK_lk_annualfiscalcalendar_salespersonid"></a> lk_annualfiscalcalendar_salespersonid

Same as annualfiscalcalendar entity [lk_annualfiscalcalendar_salespersonid](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_salespersonid) Many-To-One relationship.

**ReferencingEntity**: annualfiscalcalendar<br />
**ReferencingAttribute**: salespersonid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annualfiscalcalendar_salespersonid<br />
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


### <a name="BKMK_SystemUser_AsyncOperations"></a> SystemUser_AsyncOperations

Same as asyncoperation entity [SystemUser_AsyncOperations](asyncoperation.md#BKMK_SystemUser_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_AsyncOperations<br />
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


### <a name="BKMK_lk_publisheraddressbase_createdby"></a> lk_publisheraddressbase_createdby

Same as publisheraddress entity [lk_publisheraddressbase_createdby](publisheraddress.md#BKMK_lk_publisheraddressbase_createdby) Many-To-One relationship.

**ReferencingEntity**: publisheraddress<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_publisheraddressbase_createdby<br />
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


### <a name="BKMK_lk_import_modifiedonbehalfby"></a> lk_import_modifiedonbehalfby

Same as import entity [lk_import_modifiedonbehalfby](import.md#BKMK_lk_import_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_import_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_queuebase_modifiedby"></a> lk_queuebase_modifiedby

Same as queue entity [lk_queuebase_modifiedby](queue.md#BKMK_lk_queuebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queuebase_modifiedby<br />
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


### <a name="BKMK_lk_savedorginsightsconfiguration_createdby"></a> lk_savedorginsightsconfiguration_createdby

Same as savedorginsightsconfiguration entity [lk_savedorginsightsconfiguration_createdby](savedorginsightsconfiguration.md#BKMK_lk_savedorginsightsconfiguration_createdby) Many-To-One relationship.

**ReferencingEntity**: savedorginsightsconfiguration<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedorginsightsconfiguration_createdby<br />
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


### <a name="BKMK_SystemUser_ImportMaps"></a> SystemUser_ImportMaps

Same as importmap entity [SystemUser_ImportMaps](importmap.md#BKMK_SystemUser_ImportMaps) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_ImportMaps<br />
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


### <a name="BKMK_workflow_modifiedonbehalfby"></a> workflow_modifiedonbehalfby

Same as workflow entity [workflow_modifiedonbehalfby](workflow.md#BKMK_workflow_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: workflow_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_category_modifiedby"></a> lk_category_modifiedby

Same as category entity [lk_category_modifiedby](category.md#BKMK_lk_category_modifiedby) Many-To-One relationship.

**ReferencingEntity**: category<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_category_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_SiteMap_createdonbehalfby"></a> lk_SiteMap_createdonbehalfby

Same as sitemap entity [lk_SiteMap_createdonbehalfby](sitemap.md#BKMK_lk_SiteMap_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sitemap<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_SiteMap_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_webresource_modifiedby"></a> webresource_modifiedby

Same as webresource entity [webresource_modifiedby](webresource.md#BKMK_webresource_modifiedby) Many-To-One relationship.

**ReferencingEntity**: webresource<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: webresource_modifiedby<br />
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


### <a name="BKMK_createdby_sdkmessage"></a> createdby_sdkmessage

Same as sdkmessage entity [createdby_sdkmessage](sdkmessage.md#BKMK_createdby_sdkmessage) Many-To-One relationship.

**ReferencingEntity**: sdkmessage<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessage<br />
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


### <a name="BKMK_lk_importlogbase_modifiedby"></a> lk_importlogbase_modifiedby

Same as importlog entity [lk_importlogbase_modifiedby](importlog.md#BKMK_lk_importlogbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importlogbase_modifiedby<br />
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


### <a name="BKMK_lk_routingrule_createdonbehalfby"></a> lk_routingrule_createdonbehalfby

Same as routingrule entity [lk_routingrule_createdonbehalfby](routingrule.md#BKMK_lk_routingrule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_routingrule_createdonbehalfby<br />
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


### <a name="BKMK_lk_importjobbase_createdonbehalfby"></a> lk_importjobbase_createdonbehalfby

Same as importjob entity [lk_importjobbase_createdonbehalfby](importjob.md#BKMK_lk_importjobbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importjob<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importjobbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby"></a> lk_monthlyfiscalcalendar_modifiedonbehalfby

Same as monthlyfiscalcalendar entity [lk_monthlyfiscalcalendar_modifiedonbehalfby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: monthlyfiscalcalendar<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_monthlyfiscalcalendar_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_transactioncurrency_createdonbehalfby"></a> lk_transactioncurrency_createdonbehalfby

Same as transactioncurrency entity [lk_transactioncurrency_createdonbehalfby](transactioncurrency.md#BKMK_lk_transactioncurrency_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: transactioncurrency<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transactioncurrency_createdonbehalfby<br />
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


### <a name="BKMK_lk_bulkdeleteoperation_createdonbehalfby"></a> lk_bulkdeleteoperation_createdonbehalfby

Same as bulkdeleteoperation entity [lk_bulkdeleteoperation_createdonbehalfby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperation_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: bulkdeleteoperation<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_bulkdeleteoperation_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_plugintypestatistic"></a> modifiedby_plugintypestatistic

Same as plugintypestatistic entity [modifiedby_plugintypestatistic](plugintypestatistic.md#BKMK_modifiedby_plugintypestatistic) Many-To-One relationship.

**ReferencingEntity**: plugintypestatistic<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_plugintypestatistic<br />
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


### <a name="BKMK_lk_actioncardbase_modifiedonbehalfby"></a> lk_actioncardbase_modifiedonbehalfby

Same as actioncard entity [lk_actioncardbase_modifiedonbehalfby](actioncard.md#BKMK_lk_actioncardbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_actioncardbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_recurringappointmentmaster_createdby"></a> lk_recurringappointmentmaster_createdby

Same as recurringappointmentmaster entity [lk_recurringappointmentmaster_createdby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_createdby) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recurringappointmentmaster_createdby<br />
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


### <a name="BKMK_modifiedonbehalfby_customer_relationship"></a> modifiedonbehalfby_customer_relationship

Same as customerrelationship entity [modifiedonbehalfby_customer_relationship](customerrelationship.md#BKMK_modifiedonbehalfby_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedonbehalfby_customer_relationship<br />
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


### <a name="BKMK_lk_DisplayStringbase_createdonbehalfby"></a> lk_DisplayStringbase_createdonbehalfby

Same as displaystring entity [lk_DisplayStringbase_createdonbehalfby](displaystring.md#BKMK_lk_DisplayStringbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: displaystring<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_DisplayStringbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_audit_callinguserid"></a> lk_audit_callinguserid

Same as audit entity [lk_audit_callinguserid](audit.md#BKMK_lk_audit_callinguserid) Many-To-One relationship.

**ReferencingEntity**: audit<br />
**ReferencingAttribute**: callinguserid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_audit_callinguserid<br />
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


### <a name="BKMK_lk_sdkmessagerequest_createdonbehalfby"></a> lk_sdkmessagerequest_createdonbehalfby

Same as sdkmessagerequest entity [lk_sdkmessagerequest_createdonbehalfby](sdkmessagerequest.md#BKMK_lk_sdkmessagerequest_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequest<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagerequest_createdonbehalfby<br />
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


### <a name="BKMK_lk_importfilebase_createdby"></a> lk_importfilebase_createdby

Same as importfile entity [lk_importfilebase_createdby](importfile.md#BKMK_lk_importfilebase_createdby) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importfilebase_createdby<br />
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


### <a name="BKMK_lk_importmap_modifiedonbehalfby"></a> lk_importmap_modifiedonbehalfby

Same as importmap entity [lk_importmap_modifiedonbehalfby](importmap.md#BKMK_lk_importmap_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importmap_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_expiredprocess_modifiedonbehalfby"></a> lk_expiredprocess_modifiedonbehalfby

Same as expiredprocess entity [lk_expiredprocess_modifiedonbehalfby](expiredprocess.md#BKMK_lk_expiredprocess_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_expiredprocess_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_userqueryvisualizationbase_modifiedonbehalfby"></a> lk_userqueryvisualizationbase_modifiedonbehalfby

Same as userqueryvisualization entity [lk_userqueryvisualizationbase_modifiedonbehalfby](userqueryvisualization.md#BKMK_lk_userqueryvisualizationbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userqueryvisualizationbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_semiannualfiscalcalendar_salespersonid"></a> lk_semiannualfiscalcalendar_salespersonid

Same as semiannualfiscalcalendar entity [lk_semiannualfiscalcalendar_salespersonid](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_salespersonid) Many-To-One relationship.

**ReferencingEntity**: semiannualfiscalcalendar<br />
**ReferencingAttribute**: salespersonid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_semiannualfiscalcalendar_salespersonid<br />
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


### <a name="BKMK_lk_report_createdonbehalfby"></a> lk_report_createdonbehalfby

Same as report entity [lk_report_createdonbehalfby](report.md#BKMK_lk_report_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: report<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_report_createdonbehalfby<br />
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


### <a name="BKMK_lk_processsession_canceledby"></a> lk_processsession_canceledby

Same as processsession entity [lk_processsession_canceledby](processsession.md#BKMK_lk_processsession_canceledby) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: canceledby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processsession_canceledby<br />
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


### <a name="BKMK_lk_SiteMap_modifiedonbehalfby"></a> lk_SiteMap_modifiedonbehalfby

Same as sitemap entity [lk_SiteMap_modifiedonbehalfby](sitemap.md#BKMK_lk_SiteMap_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sitemap<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_SiteMap_modifiedonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_SystemUser_SyncError"></a> SystemUser_SyncError

Same as syncerror entity [SystemUser_SyncError](syncerror.md#BKMK_SystemUser_SyncError) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_SyncError<br />
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


### <a name="BKMK_lk_socialactivity_modifiedby"></a> lk_socialactivity_modifiedby

Same as socialactivity entity [lk_socialactivity_modifiedby](socialactivity.md#BKMK_lk_socialactivity_modifiedby) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_socialactivity_modifiedby<br />
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


### <a name="BKMK_lk_accountbase_modifiedonbehalfby"></a> lk_accountbase_modifiedonbehalfby

Same as account entity [lk_accountbase_modifiedonbehalfby](account.md#BKMK_lk_accountbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_accountbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_subjectbase_createdby"></a> lk_subjectbase_createdby

Same as subject entity [lk_subjectbase_createdby](subject.md#BKMK_lk_subjectbase_createdby) Many-To-One relationship.

**ReferencingEntity**: subject<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_subjectbase_createdby<br />
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


### <a name="BKMK_lk_MobileOfflineProfile_modifiedonbehalfby"></a> lk_MobileOfflineProfile_modifiedonbehalfby

Same as mobileofflineprofile entity [lk_MobileOfflineProfile_modifiedonbehalfby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofile<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_MobileOfflineProfile_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_annotationbase_modifiedonbehalfby"></a> lk_annotationbase_modifiedonbehalfby

Same as annotation entity [lk_annotationbase_modifiedonbehalfby](annotation.md#BKMK_lk_annotationbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annotationbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_kbarticletemplatebase_createdby"></a> lk_kbarticletemplatebase_createdby

Same as kbarticletemplate entity [lk_kbarticletemplatebase_createdby](kbarticletemplate.md#BKMK_lk_kbarticletemplatebase_createdby) Many-To-One relationship.

**ReferencingEntity**: kbarticletemplate<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticletemplatebase_createdby<br />
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


### <a name="BKMK_lk_importbase_modifiedby"></a> lk_importbase_modifiedby

Same as import entity [lk_importbase_modifiedby](import.md#BKMK_lk_importbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importbase_modifiedby<br />
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


### <a name="BKMK_modifiedby_connection_role"></a> modifiedby_connection_role

Same as connectionrole entity [modifiedby_connection_role](connectionrole.md#BKMK_modifiedby_connection_role) Many-To-One relationship.

**ReferencingEntity**: connectionrole<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_connection_role<br />
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


### <a name="BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby"></a> lk_sharepointdocumentlocationbase_createdonbehalfby

Same as sharepointdocumentlocation entity [lk_sharepointdocumentlocationbase_createdonbehalfby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentlocationbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_mailmergetemplatebase_modifiedby"></a> lk_mailmergetemplatebase_modifiedby

Same as mailmergetemplate entity [lk_mailmergetemplatebase_modifiedby](mailmergetemplate.md#BKMK_lk_mailmergetemplatebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: mailmergetemplate<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_mailmergetemplatebase_modifiedby<br />
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


### <a name="BKMK_lk_userquery_createdonbehalfby"></a> lk_userquery_createdonbehalfby

Same as userquery entity [lk_userquery_createdonbehalfby](userquery.md#BKMK_lk_userquery_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userquery_createdonbehalfby<br />
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


### <a name="BKMK_lk_transactioncurrencybase_createdby"></a> lk_transactioncurrencybase_createdby

Same as transactioncurrency entity [lk_transactioncurrencybase_createdby](transactioncurrency.md#BKMK_lk_transactioncurrencybase_createdby) Many-To-One relationship.

**ReferencingEntity**: transactioncurrency<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transactioncurrencybase_createdby<br />
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


### <a name="BKMK_lk_entitymap_createdonbehalfby"></a> lk_entitymap_createdonbehalfby

Same as entitymap entity [lk_entitymap_createdonbehalfby](entitymap.md#BKMK_lk_entitymap_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: entitymap<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_entitymap_createdonbehalfby<br />
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


### <a name="BKMK_lk_knowledgesearchmodel_createdonbehalfby"></a> lk_knowledgesearchmodel_createdonbehalfby

Same as knowledgesearchmodel entity [lk_knowledgesearchmodel_createdonbehalfby](knowledgesearchmodel.md#BKMK_lk_knowledgesearchmodel_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: knowledgesearchmodel<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgesearchmodel_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_createdonbehalfby_customer_relationship"></a> createdonbehalfby_customer_relationship

Same as customerrelationship entity [createdonbehalfby_customer_relationship](customerrelationship.md#BKMK_createdonbehalfby_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdonbehalfby_customer_relationship<br />
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


### <a name="BKMK_lk_sharepointdocumentbase_createdby"></a> lk_sharepointdocumentbase_createdby

Same as sharepointdocument entity [lk_sharepointdocumentbase_createdby](sharepointdocument.md#BKMK_lk_sharepointdocumentbase_createdby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentbase_createdby<br />
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


### <a name="BKMK_lk_queue_createdonbehalfby"></a> lk_queue_createdonbehalfby

Same as queue entity [lk_queue_createdonbehalfby](queue.md#BKMK_lk_queue_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_queue_createdonbehalfby<br />
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


### <a name="BKMK_lk_MobileOfflineProfile_createdby"></a> lk_MobileOfflineProfile_createdby

Same as mobileofflineprofile entity [lk_MobileOfflineProfile_createdby](mobileofflineprofile.md#BKMK_lk_MobileOfflineProfile_createdby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofile<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_MobileOfflineProfile_createdby<br />
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


### <a name="BKMK_modifiedby_expanderevent"></a> modifiedby_expanderevent

Same as expanderevent entity [modifiedby_expanderevent](expanderevent.md#BKMK_modifiedby_expanderevent) Many-To-One relationship.

**ReferencingEntity**: expanderevent<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_expanderevent<br />
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


### <a name="BKMK_lk_savedorginsightsconfiguration_createdonbehalfby"></a> lk_savedorginsightsconfiguration_createdonbehalfby

Same as savedorginsightsconfiguration entity [lk_savedorginsightsconfiguration_createdonbehalfby](savedorginsightsconfiguration.md#BKMK_lk_savedorginsightsconfiguration_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: savedorginsightsconfiguration<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedorginsightsconfiguration_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_serviceendpoint"></a> modifiedby_serviceendpoint

Same as serviceendpoint entity [modifiedby_serviceendpoint](serviceendpoint.md#BKMK_modifiedby_serviceendpoint) Many-To-One relationship.

**ReferencingEntity**: serviceendpoint<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_serviceendpoint<br />
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


### <a name="BKMK_lk_appointment_modifiedby"></a> lk_appointment_modifiedby

Same as appointment entity [lk_appointment_modifiedby](appointment.md#BKMK_lk_appointment_modifiedby) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_appointment_modifiedby<br />
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


### <a name="BKMK_lk_emailsignaturebase_modifiedonbehalfby"></a> lk_emailsignaturebase_modifiedonbehalfby

Same as emailsignature entity [lk_emailsignaturebase_modifiedonbehalfby](emailsignature.md#BKMK_lk_emailsignaturebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: emailsignature<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_emailsignaturebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_picklistmapping_modifiedonbehalfby"></a> lk_picklistmapping_modifiedonbehalfby

Same as picklistmapping entity [lk_picklistmapping_modifiedonbehalfby](picklistmapping.md#BKMK_lk_picklistmapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: picklistmapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_picklistmapping_modifiedonbehalfby<br />
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


### <a name="BKMK_user_routingruleitem"></a> user_routingruleitem

Same as routingruleitem entity [user_routingruleitem](routingruleitem.md#BKMK_user_routingruleitem) Many-To-One relationship.

**ReferencingEntity**: routingruleitem<br />
**ReferencingAttribute**: assignobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: user_routingruleitem<br />
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


### <a name="BKMK_lk_transformationmapping_createdonbehalfby"></a> lk_transformationmapping_createdonbehalfby

Same as transformationmapping entity [lk_transformationmapping_createdonbehalfby](transformationmapping.md#BKMK_lk_transformationmapping_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: transformationmapping<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationmapping_createdonbehalfby<br />
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


### <a name="BKMK_lk_plugintypestatisticbase_createdonbehalfby"></a> lk_plugintypestatisticbase_createdonbehalfby

Same as plugintypestatistic entity [lk_plugintypestatisticbase_createdonbehalfby](plugintypestatistic.md#BKMK_lk_plugintypestatisticbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: plugintypestatistic<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_plugintypestatisticbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_kbarticletemplate_createdonbehalfby"></a> lk_kbarticletemplate_createdonbehalfby

Same as kbarticletemplate entity [lk_kbarticletemplate_createdonbehalfby](kbarticletemplate.md#BKMK_lk_kbarticletemplate_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: kbarticletemplate<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticletemplate_createdonbehalfby<br />
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


### <a name="BKMK_createdby_sdkmessagerequestfield"></a> createdby_sdkmessagerequestfield

Same as sdkmessagerequestfield entity [createdby_sdkmessagerequestfield](sdkmessagerequestfield.md#BKMK_createdby_sdkmessagerequestfield) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequestfield<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessagerequestfield<br />
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


### <a name="BKMK_ImportFile_SystemUser"></a> ImportFile_SystemUser

Same as importfile entity [ImportFile_SystemUser](importfile.md#BKMK_ImportFile_SystemUser) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: recordsownerid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: ImportFile_SystemUser<br />
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


### <a name="BKMK_lk_importmapbase_modifiedby"></a> lk_importmapbase_modifiedby

Same as importmap entity [lk_importmapbase_modifiedby](importmap.md#BKMK_lk_importmapbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importmapbase_modifiedby<br />
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


### <a name="BKMK_lk_userform_createdby"></a> lk_userform_createdby

Same as userform entity [lk_userform_createdby](userform.md#BKMK_lk_userform_createdby) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userform_createdby<br />
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


### <a name="BKMK_lk_isvconfig_createdonbehalfby"></a> lk_isvconfig_createdonbehalfby

Same as isvconfig entity [lk_isvconfig_createdonbehalfby](isvconfig.md#BKMK_lk_isvconfig_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: isvconfig<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_isvconfig_createdonbehalfby<br />
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


### <a name="BKMK_lk_expiredprocess_createdby"></a> lk_expiredprocess_createdby

Same as expiredprocess entity [lk_expiredprocess_createdby](expiredprocess.md#BKMK_lk_expiredprocess_createdby) Many-To-One relationship.

**ReferencingEntity**: expiredprocess<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_expiredprocess_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_socialinsightsconfiguration_modifiedonbehalfby"></a> lk_socialinsightsconfiguration_modifiedonbehalfby

Same as socialinsightsconfiguration entity [lk_socialinsightsconfiguration_modifiedonbehalfby](socialinsightsconfiguration.md#BKMK_lk_socialinsightsconfiguration_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: socialinsightsconfiguration<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_socialinsightsconfiguration_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_reportvisibility_createdonbehalfby"></a> lk_reportvisibility_createdonbehalfby

Same as reportvisibility entity [lk_reportvisibility_createdonbehalfby](reportvisibility.md#BKMK_lk_reportvisibility_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportvisibility<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportvisibility_createdonbehalfby<br />
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


### <a name="BKMK_lk_userqueryvisualization_createdby"></a> lk_userqueryvisualization_createdby

Same as userqueryvisualization entity [lk_userqueryvisualization_createdby](userqueryvisualization.md#BKMK_lk_userqueryvisualization_createdby) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userqueryvisualization_createdby<br />
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


### <a name="BKMK_lk_ACIViewMapper_modifiedby"></a> lk_ACIViewMapper_modifiedby

Same as aciviewmapper entity [lk_ACIViewMapper_modifiedby](aciviewmapper.md#BKMK_lk_ACIViewMapper_modifiedby) Many-To-One relationship.

**ReferencingEntity**: aciviewmapper<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ACIViewMapper_modifiedby<br />
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


### <a name="BKMK_user_slabase"></a> user_slabase

Same as sla entity [user_slabase](sla.md#BKMK_user_slabase) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_slabase<br />
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


### <a name="BKMK_lk_reportlinkbase_createdby"></a> lk_reportlinkbase_createdby

Same as reportlink entity [lk_reportlinkbase_createdby](reportlink.md#BKMK_lk_reportlinkbase_createdby) Many-To-One relationship.

**ReferencingEntity**: reportlink<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportlinkbase_createdby<br />
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


### <a name="BKMK_lk_annotationbase_createdby"></a> lk_annotationbase_createdby

Same as annotation entity [lk_annotationbase_createdby](annotation.md#BKMK_lk_annotationbase_createdby) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annotationbase_createdby<br />
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


### <a name="BKMK_webresource_createdby"></a> webresource_createdby

Same as webresource entity [webresource_createdby](webresource.md#BKMK_webresource_createdby) Many-To-One relationship.

**ReferencingEntity**: webresource<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: webresource_createdby<br />
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


### <a name="BKMK_lk_userqueryvisualizationbase_createdonbehalfby"></a> lk_userqueryvisualizationbase_createdonbehalfby

Same as userqueryvisualization entity [lk_userqueryvisualizationbase_createdonbehalfby](userqueryvisualization.md#BKMK_lk_userqueryvisualizationbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userqueryvisualizationbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_usersettings_modifiedonbehalfby"></a> lk_usersettings_modifiedonbehalfby

Same as usersettings entity [lk_usersettings_modifiedonbehalfby](usersettings.md#BKMK_lk_usersettings_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_usersettings_modifiedonbehalfby<br />
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


### <a name="BKMK_user_parent_user"></a> user_parent_user

Same as systemuser entity [user_parent_user](systemuser.md#BKMK_user_parent_user) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: parentsystemuserid<br />
**IsHierarchical**: True<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_parent_user<br />
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


### <a name="BKMK_lk_appconfiginstance_createdby"></a> lk_appconfiginstance_createdby

Same as appconfiginstance entity [lk_appconfiginstance_createdby](appconfiginstance.md#BKMK_lk_appconfiginstance_createdby) Many-To-One relationship.

**ReferencingEntity**: appconfiginstance<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfiginstance_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_createdonbehalfby_attributemap"></a> createdonbehalfby_attributemap

Same as attributemap entity [createdonbehalfby_attributemap](attributemap.md#BKMK_createdonbehalfby_attributemap) Many-To-One relationship.

**ReferencingEntity**: attributemap<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdonbehalfby_attributemap<br />
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


### <a name="BKMK_lk_annualfiscalcalendar_createdonbehalfby"></a> lk_annualfiscalcalendar_createdonbehalfby

Same as annualfiscalcalendar entity [lk_annualfiscalcalendar_createdonbehalfby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: annualfiscalcalendar<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annualfiscalcalendar_createdonbehalfby<br />
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


### <a name="BKMK_lk_userformbase_createdonbehalfby"></a> lk_userformbase_createdonbehalfby

Same as userform entity [lk_userformbase_createdonbehalfby](userform.md#BKMK_lk_userformbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userformbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_knowledgesearchmodel_modifiedby"></a> lk_knowledgesearchmodel_modifiedby

Same as knowledgesearchmodel entity [lk_knowledgesearchmodel_modifiedby](knowledgesearchmodel.md#BKMK_lk_knowledgesearchmodel_modifiedby) Many-To-One relationship.

**ReferencingEntity**: knowledgesearchmodel<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgesearchmodel_modifiedby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_modifiedby_sdkmessageresponsefield"></a> modifiedby_sdkmessageresponsefield

Same as sdkmessageresponsefield entity [modifiedby_sdkmessageresponsefield](sdkmessageresponsefield.md#BKMK_modifiedby_sdkmessageresponsefield) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponsefield<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessageresponsefield<br />
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


### <a name="BKMK_lk_SharePointData_createdonbehalfby"></a> lk_SharePointData_createdonbehalfby

Same as sharepointdata entity [lk_SharePointData_createdonbehalfby](sharepointdata.md#BKMK_lk_SharePointData_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointdata<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_SharePointData_createdonbehalfby<br />
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


### <a name="BKMK_lk_fieldsecurityprofile_createdby"></a> lk_fieldsecurityprofile_createdby

Same as fieldsecurityprofile entity [lk_fieldsecurityprofile_createdby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_createdby) Many-To-One relationship.

**ReferencingEntity**: fieldsecurityprofile<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fieldsecurityprofile_createdby<br />
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


### <a name="BKMK_lk_asyncoperation_modifiedby"></a> lk_asyncoperation_modifiedby

Same as asyncoperation entity [lk_asyncoperation_modifiedby](asyncoperation.md#BKMK_lk_asyncoperation_modifiedby) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_asyncoperation_modifiedby<br />
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


### <a name="BKMK_lk_pluginassembly_createdonbehalfby"></a> lk_pluginassembly_createdonbehalfby

Same as pluginassembly entity [lk_pluginassembly_createdonbehalfby](pluginassembly.md#BKMK_lk_pluginassembly_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: pluginassembly<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_pluginassembly_createdonbehalfby<br />
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


### <a name="BKMK_lk_importentitymapping_modifiedby"></a> lk_importentitymapping_modifiedby

Same as importentitymapping entity [lk_importentitymapping_modifiedby](importentitymapping.md#BKMK_lk_importentitymapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: importentitymapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importentitymapping_modifiedby<br />
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


### <a name="BKMK_lk_ChannelPropertyGroup_createdonbehalfby"></a> lk_ChannelPropertyGroup_createdonbehalfby

Same as channelpropertygroup entity [lk_ChannelPropertyGroup_createdonbehalfby](channelpropertygroup.md#BKMK_lk_ChannelPropertyGroup_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: channelpropertygroup<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelPropertyGroup_createdonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessageprocessingstep_createdonbehalfby"></a> lk_sdkmessageprocessingstep_createdonbehalfby

Same as sdkmessageprocessingstep entity [lk_sdkmessageprocessingstep_createdonbehalfby](sdkmessageprocessingstep.md#BKMK_lk_sdkmessageprocessingstep_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessageprocessingstep<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessageprocessingstep_createdonbehalfby<br />
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


### <a name="BKMK_lk_ConvertRule_modifiedonbehalfby"></a> lk_ConvertRule_modifiedonbehalfby

Same as convertrule entity [lk_ConvertRule_modifiedonbehalfby](convertrule.md#BKMK_lk_ConvertRule_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ConvertRule_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_activitypointer_createdonbehalfby"></a> lk_activitypointer_createdonbehalfby

Same as activitypointer entity [lk_activitypointer_createdonbehalfby](activitypointer.md#BKMK_lk_activitypointer_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_activitypointer_createdonbehalfby<br />
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


### <a name="BKMK_lk_contact_modifiedonbehalfby"></a> lk_contact_modifiedonbehalfby

Same as contact entity [lk_contact_modifiedonbehalfby](contact.md#BKMK_lk_contact_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_contact_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby"></a> lk_savedqueryvisualizationbase_modifiedonbehalfby

Same as savedqueryvisualization entity [lk_savedqueryvisualizationbase_modifiedonbehalfby](savedqueryvisualization.md#BKMK_lk_savedqueryvisualizationbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: savedqueryvisualization<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_savedqueryvisualizationbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_socialinsightsconfiguration_createdby"></a> lk_socialinsightsconfiguration_createdby

Same as socialinsightsconfiguration entity [lk_socialinsightsconfiguration_createdby](socialinsightsconfiguration.md#BKMK_lk_socialinsightsconfiguration_createdby) Many-To-One relationship.

**ReferencingEntity**: socialinsightsconfiguration<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_socialinsightsconfiguration_createdby<br />
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


### <a name="BKMK_lk_accountbase_createdonbehalfby"></a> lk_accountbase_createdonbehalfby

Same as account entity [lk_accountbase_createdonbehalfby](account.md#BKMK_lk_accountbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_accountbase_createdonbehalfby<br />
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


### <a name="BKMK_modifiedby_sdkmessagefilter"></a> modifiedby_sdkmessagefilter

Same as sdkmessagefilter entity [modifiedby_sdkmessagefilter](sdkmessagefilter.md#BKMK_modifiedby_sdkmessagefilter) Many-To-One relationship.

**ReferencingEntity**: sdkmessagefilter<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessagefilter<br />
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


### <a name="BKMK_system_user_email_templates"></a> system_user_email_templates

Same as template entity [system_user_email_templates](template.md#BKMK_system_user_email_templates) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: system_user_email_templates<br />
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


### <a name="BKMK_lk_ownermapping_modifiedonbehalfby"></a> lk_ownermapping_modifiedonbehalfby

Same as ownermapping entity [lk_ownermapping_modifiedonbehalfby](ownermapping.md#BKMK_lk_ownermapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: ownermapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ownermapping_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_ChannelPropertyGroup_modifiedby"></a> lk_ChannelPropertyGroup_modifiedby

Same as channelpropertygroup entity [lk_ChannelPropertyGroup_modifiedby](channelpropertygroup.md#BKMK_lk_ChannelPropertyGroup_modifiedby) Many-To-One relationship.

**ReferencingEntity**: channelpropertygroup<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_ChannelPropertyGroup_modifiedby<br />
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


### <a name="BKMK_lk_systemuser_modifiedonbehalfby"></a> lk_systemuser_modifiedonbehalfby

Same as systemuser entity [lk_systemuser_modifiedonbehalfby](systemuser.md#BKMK_lk_systemuser_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_systemuser_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_annualfiscalcalendar_createdby"></a> lk_annualfiscalcalendar_createdby

Same as annualfiscalcalendar entity [lk_annualfiscalcalendar_createdby](annualfiscalcalendar.md#BKMK_lk_annualfiscalcalendar_createdby) Many-To-One relationship.

**ReferencingEntity**: annualfiscalcalendar<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annualfiscalcalendar_createdby<br />
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


### <a name="BKMK_lk_email_createdonbehalfby"></a> lk_email_createdonbehalfby

Same as email entity [lk_email_createdonbehalfby](email.md#BKMK_lk_email_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_email_createdonbehalfby<br />
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


### <a name="BKMK_lk_recurringappointmentmaster_modifiedonbehalfby"></a> lk_recurringappointmentmaster_modifiedonbehalfby

Same as recurringappointmentmaster entity [lk_recurringappointmentmaster_modifiedonbehalfby](recurringappointmentmaster.md#BKMK_lk_recurringappointmentmaster_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_recurringappointmentmaster_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_timezonelocalizedname_createdby"></a> lk_timezonelocalizedname_createdby

Same as timezonelocalizedname entity [lk_timezonelocalizedname_createdby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_createdby) Many-To-One relationship.

**ReferencingEntity**: timezonelocalizedname<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonelocalizedname_createdby<br />
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


### <a name="BKMK_lk_bulkdeleteoperationbase_modifiedby"></a> lk_bulkdeleteoperationbase_modifiedby

Same as bulkdeleteoperation entity [lk_bulkdeleteoperationbase_modifiedby](bulkdeleteoperation.md#BKMK_lk_bulkdeleteoperationbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: bulkdeleteoperation<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_bulkdeleteoperationbase_modifiedby<br />
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


### <a name="BKMK_lk_sharepointsitebase_modifiedonbehalfby"></a> lk_sharepointsitebase_modifiedonbehalfby

Same as sharepointsite entity [lk_sharepointsitebase_modifiedonbehalfby](sharepointsite.md#BKMK_lk_sharepointsitebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointsitebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_ownermapping_modifiedby"></a> lk_ownermapping_modifiedby

Same as ownermapping entity [lk_ownermapping_modifiedby](ownermapping.md#BKMK_lk_ownermapping_modifiedby) Many-To-One relationship.

**ReferencingEntity**: ownermapping<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ownermapping_modifiedby<br />
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


### <a name="BKMK_lk_sharepointsitebase_createdby"></a> lk_sharepointsitebase_createdby

Same as sharepointsite entity [lk_sharepointsitebase_createdby](sharepointsite.md#BKMK_lk_sharepointsitebase_createdby) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointsitebase_createdby<br />
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


### <a name="BKMK_createdby_sdkmessageresponsefield"></a> createdby_sdkmessageresponsefield

Same as sdkmessageresponsefield entity [createdby_sdkmessageresponsefield](sdkmessageresponsefield.md#BKMK_createdby_sdkmessageresponsefield) Many-To-One relationship.

**ReferencingEntity**: sdkmessageresponsefield<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessageresponsefield<br />
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


### <a name="BKMK_lk_actioncardbase_modifiedby"></a> lk_actioncardbase_modifiedby

Same as actioncard entity [lk_actioncardbase_modifiedby](actioncard.md#BKMK_lk_actioncardbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_actioncardbase_modifiedby<br />
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


### <a name="BKMK_lk_webresourcebase_createdonbehalfby"></a> lk_webresourcebase_createdonbehalfby

Same as webresource entity [lk_webresourcebase_createdonbehalfby](webresource.md#BKMK_lk_webresourcebase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: webresource<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_webresourcebase_createdonbehalfby<br />
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


### <a name="BKMK_lk_connectionrolebase_modifiedonbehalfby"></a> lk_connectionrolebase_modifiedonbehalfby

Same as connectionrole entity [lk_connectionrolebase_modifiedonbehalfby](connectionrole.md#BKMK_lk_connectionrolebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: connectionrole<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_connectionrolebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_timezonelocalizedname_modifiedonbehalfby"></a> lk_timezonelocalizedname_modifiedonbehalfby

Same as timezonelocalizedname entity [lk_timezonelocalizedname_modifiedonbehalfby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: timezonelocalizedname<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonelocalizedname_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_transformationmapping_modifiedonbehalfby"></a> lk_transformationmapping_modifiedonbehalfby

Same as transformationmapping entity [lk_transformationmapping_modifiedonbehalfby](transformationmapping.md#BKMK_lk_transformationmapping_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: transformationmapping<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_transformationmapping_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_azureserviceconnection_createdby"></a> lk_azureserviceconnection_createdby

Same as azureserviceconnection entity [lk_azureserviceconnection_createdby](azureserviceconnection.md#BKMK_lk_azureserviceconnection_createdby) Many-To-One relationship.

**ReferencingEntity**: azureserviceconnection<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_azureserviceconnection_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_documenttemplatebase_modifiedonbehalfby"></a> lk_documenttemplatebase_modifiedonbehalfby

Same as documenttemplate entity [lk_documenttemplatebase_modifiedonbehalfby](documenttemplate.md#BKMK_lk_documenttemplatebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: documenttemplate<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_documenttemplatebase_modifiedonbehalfby<br />
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


### <a name="BKMK_user_phonecall"></a> user_phonecall

Same as phonecall entity [user_phonecall](phonecall.md#BKMK_user_phonecall) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: user_phonecall<br />
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


### <a name="BKMK_lk_serviceendpointbase_modifiedonbehalfby"></a> lk_serviceendpointbase_modifiedonbehalfby

Same as serviceendpoint entity [lk_serviceendpointbase_modifiedonbehalfby](serviceendpoint.md#BKMK_lk_serviceendpointbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: serviceendpoint<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_serviceendpointbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_reportlinkbase_modifiedby"></a> lk_reportlinkbase_modifiedby

Same as reportlink entity [lk_reportlinkbase_modifiedby](reportlink.md#BKMK_lk_reportlinkbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: reportlink<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportlinkbase_modifiedby<br />
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


### <a name="BKMK_lk_slabase_createdonbehalfby"></a> lk_slabase_createdonbehalfby

Same as sla entity [lk_slabase_createdonbehalfby](sla.md#BKMK_lk_slabase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_slabase_createdonbehalfby<br />
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


### <a name="BKMK_lk_importjobbase_modifiedby"></a> lk_importjobbase_modifiedby

Same as importjob entity [lk_importjobbase_modifiedby](importjob.md#BKMK_lk_importjobbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: importjob<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importjobbase_modifiedby<br />
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


### <a name="BKMK_lk_MobileOfflineProfileItemAssociation_createdby"></a> lk_MobileOfflineProfileItemAssociation_createdby

Same as mobileofflineprofileitemassociation entity [lk_MobileOfflineProfileItemAssociation_createdby](mobileofflineprofileitemassociation.md#BKMK_lk_MobileOfflineProfileItemAssociation_createdby) Many-To-One relationship.

**ReferencingEntity**: mobileofflineprofileitemassociation<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_MobileOfflineProfileItemAssociation_createdby<br />
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


### <a name="BKMK_lk_processtriggerbase_createdby"></a> lk_processtriggerbase_createdby

Same as processtrigger entity [lk_processtriggerbase_createdby](processtrigger.md#BKMK_lk_processtriggerbase_createdby) Many-To-One relationship.

**ReferencingEntity**: processtrigger<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_processtriggerbase_createdby<br />
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


### <a name="BKMK_lk_timezonedefinition_createdonbehalfby"></a> lk_timezonedefinition_createdonbehalfby

Same as timezonedefinition entity [lk_timezonedefinition_createdonbehalfby](timezonedefinition.md#BKMK_lk_timezonedefinition_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: timezonedefinition<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonedefinition_createdonbehalfby<br />
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


### <a name="BKMK_lk_kbarticlecomment_modifiedonbehalfby"></a> lk_kbarticlecomment_modifiedonbehalfby

Same as kbarticlecomment entity [lk_kbarticlecomment_modifiedonbehalfby](kbarticlecomment.md#BKMK_lk_kbarticlecomment_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: kbarticlecomment<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticlecomment_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_timezonelocalizedname_createdonbehalfby"></a> lk_timezonelocalizedname_createdonbehalfby

Same as timezonelocalizedname entity [lk_timezonelocalizedname_createdonbehalfby](timezonelocalizedname.md#BKMK_lk_timezonelocalizedname_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: timezonelocalizedname<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_timezonelocalizedname_createdonbehalfby<br />
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


### <a name="BKMK_lk_systemuserbase_createdby"></a> lk_systemuserbase_createdby

Same as systemuser entity [lk_systemuserbase_createdby](systemuser.md#BKMK_lk_systemuserbase_createdby) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_systemuserbase_createdby<br />
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


### <a name="BKMK_systemuser_principalobjectattributeaccess"></a> systemuser_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [systemuser_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_systemuser_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: systemuser_principalobjectattributeaccess<br />
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


### <a name="BKMK_system_user_asyncoperation"></a> system_user_asyncoperation

Same as asyncoperation entity [system_user_asyncoperation](asyncoperation.md#BKMK_system_user_asyncoperation) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: owninguser<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: system_user_asyncoperation<br />
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


### <a name="BKMK_lk_reportlink_createdonbehalfby"></a> lk_reportlink_createdonbehalfby

Same as reportlink entity [lk_reportlink_createdonbehalfby](reportlink.md#BKMK_lk_reportlink_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: reportlink<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportlink_createdonbehalfby<br />
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


### <a name="BKMK_lk_plugintracelogbase_createdonbehalfby"></a> lk_plugintracelogbase_createdonbehalfby

Same as plugintracelog entity [lk_plugintracelogbase_createdonbehalfby](plugintracelog.md#BKMK_lk_plugintracelogbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: plugintracelog<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_plugintracelogbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_teamtemplate_createdby"></a> lk_teamtemplate_createdby

Same as teamtemplate entity [lk_teamtemplate_createdby](teamtemplate.md#BKMK_lk_teamtemplate_createdby) Many-To-One relationship.

**ReferencingEntity**: teamtemplate<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_teamtemplate_createdby<br />
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


### <a name="BKMK_lk_annotationbase_createdonbehalfby"></a> lk_annotationbase_createdonbehalfby

Same as annotation entity [lk_annotationbase_createdonbehalfby](annotation.md#BKMK_lk_annotationbase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_annotationbase_createdonbehalfby<br />
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


### <a name="BKMK_lk_fieldsecurityprofile_modifiedonbehalfby"></a> lk_fieldsecurityprofile_modifiedonbehalfby

Same as fieldsecurityprofile entity [lk_fieldsecurityprofile_modifiedonbehalfby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: fieldsecurityprofile<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fieldsecurityprofile_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_appmodulecomponent_modifiedonbehalfby"></a> lk_appmodulecomponent_modifiedonbehalfby

Same as appmodulecomponent entity [lk_appmodulecomponent_modifiedonbehalfby](appmodulecomponent.md#BKMK_lk_appmodulecomponent_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: appmodulecomponent<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_appmodulecomponent_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_reportentitybase_createdby"></a> lk_reportentitybase_createdby

Same as reportentity entity [lk_reportentitybase_createdby](reportentity.md#BKMK_lk_reportentitybase_createdby) Many-To-One relationship.

**ReferencingEntity**: reportentity<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_reportentitybase_createdby<br />
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


### <a name="BKMK_lk_semiannualfiscalcalendar_createdonbehalfby"></a> lk_semiannualfiscalcalendar_createdonbehalfby

Same as semiannualfiscalcalendar entity [lk_semiannualfiscalcalendar_createdonbehalfby](semiannualfiscalcalendar.md#BKMK_lk_semiannualfiscalcalendar_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: semiannualfiscalcalendar<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_semiannualfiscalcalendar_createdonbehalfby<br />
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


### <a name="BKMK_lk_userquery_modifiedonbehalfby"></a> lk_userquery_modifiedonbehalfby

Same as userquery entity [lk_userquery_modifiedonbehalfby](userquery.md#BKMK_lk_userquery_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_userquery_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_businessunitnewsarticlebase_createdby"></a> lk_businessunitnewsarticlebase_createdby

Same as businessunitnewsarticle entity [lk_businessunitnewsarticlebase_createdby](businessunitnewsarticle.md#BKMK_lk_businessunitnewsarticlebase_createdby) Many-To-One relationship.

**ReferencingEntity**: businessunitnewsarticle<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunitnewsarticlebase_createdby<br />
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


### <a name="BKMK_systemuser_connections2"></a> systemuser_connections2

Same as connection entity [systemuser_connections2](connection.md#BKMK_systemuser_connections2) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: record2id<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_connections2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 100

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_lk_task_createdonbehalfby"></a> lk_task_createdonbehalfby

Same as task entity [lk_task_createdonbehalfby](task.md#BKMK_lk_task_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_task_createdonbehalfby<br />
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


### <a name="BKMK_lk_contactbase_modifiedby"></a> lk_contactbase_modifiedby

Same as contact entity [lk_contactbase_modifiedby](contact.md#BKMK_lk_contactbase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_contactbase_modifiedby<br />
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


### <a name="BKMK_lk_letter_createdonbehalfby"></a> lk_letter_createdonbehalfby

Same as letter entity [lk_letter_createdonbehalfby](letter.md#BKMK_lk_letter_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_letter_createdonbehalfby<br />
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


### <a name="BKMK_lk_customcontrolresource_createdby"></a> lk_customcontrolresource_createdby

Same as customcontrolresource entity [lk_customcontrolresource_createdby](customcontrolresource.md#BKMK_lk_customcontrolresource_createdby) Many-To-One relationship.

**ReferencingEntity**: customcontrolresource<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_customcontrolresource_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_socialactivitybase_modifiedonbehalfby"></a> lk_socialactivitybase_modifiedonbehalfby

Same as socialactivity entity [lk_socialactivitybase_modifiedonbehalfby](socialactivity.md#BKMK_lk_socialactivitybase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_socialactivitybase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_socialactivitybase_createdonbehalfby"></a> lk_socialactivitybase_createdonbehalfby

Same as socialactivity entity [lk_socialactivitybase_createdonbehalfby](socialactivity.md#BKMK_lk_socialactivitybase_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_socialactivitybase_createdonbehalfby<br />
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


### <a name="BKMK_lk_importfilebase_modifiedonbehalfby"></a> lk_importfilebase_modifiedonbehalfby

Same as importfile entity [lk_importfilebase_modifiedonbehalfby](importfile.md#BKMK_lk_importfilebase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_importfilebase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_sdkmessagerequestfield_modifiedonbehalfby"></a> lk_sdkmessagerequestfield_modifiedonbehalfby

Same as sdkmessagerequestfield entity [lk_sdkmessagerequestfield_modifiedonbehalfby](sdkmessagerequestfield.md#BKMK_lk_sdkmessagerequestfield_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequestfield<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_sdkmessagerequestfield_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_fieldsecurityprofile_modifiedby"></a> lk_fieldsecurityprofile_modifiedby

Same as fieldsecurityprofile entity [lk_fieldsecurityprofile_modifiedby](fieldsecurityprofile.md#BKMK_lk_fieldsecurityprofile_modifiedby) Many-To-One relationship.

**ReferencingEntity**: fieldsecurityprofile<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_fieldsecurityprofile_modifiedby<br />
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


### <a name="BKMK_lk_newprocess_createdonbehalfby"></a> lk_newprocess_createdonbehalfby

Same as newprocess entity [lk_newprocess_createdonbehalfby](newprocess.md#BKMK_lk_newprocess_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: newprocess<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_newprocess_createdonbehalfby<br />
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


### <a name="BKMK_lk_appconfig_createdby"></a> lk_appconfig_createdby

Same as appconfig entity [lk_appconfig_createdby](appconfig.md#BKMK_lk_appconfig_createdby) Many-To-One relationship.

**ReferencingEntity**: appconfig<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: systemuser_appconfig_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_businessunitbase_createdby"></a> lk_businessunitbase_createdby

Same as businessunit entity [lk_businessunitbase_createdby](businessunit.md#BKMK_lk_businessunitbase_createdby) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_businessunitbase_createdby<br />
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


### <a name="BKMK_lk_monthlyfiscalcalendar_createdonbehalfby"></a> lk_monthlyfiscalcalendar_createdonbehalfby

Same as monthlyfiscalcalendar entity [lk_monthlyfiscalcalendar_createdonbehalfby](monthlyfiscalcalendar.md#BKMK_lk_monthlyfiscalcalendar_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: monthlyfiscalcalendar<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_monthlyfiscalcalendar_createdonbehalfby<br />
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


### <a name="BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby"></a> lk_sharepointdocumentlocationbase_modifiedonbehalfby

Same as sharepointdocumentlocation entity [lk_sharepointdocumentlocationbase_modifiedonbehalfby](sharepointdocumentlocation.md#BKMK_lk_sharepointdocumentlocationbase_modifiedonbehalfby) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: modifiedonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_sharepointdocumentlocationbase_modifiedonbehalfby<br />
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


### <a name="BKMK_lk_advancedsimilarityrule_createdonbehalfby"></a> lk_advancedsimilarityrule_createdonbehalfby

Same as advancedsimilarityrule entity [lk_advancedsimilarityrule_createdonbehalfby](advancedsimilarityrule.md#BKMK_lk_advancedsimilarityrule_createdonbehalfby) Many-To-One relationship.

**ReferencingEntity**: advancedsimilarityrule<br />
**ReferencingAttribute**: createdonbehalfby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_advancedsimilarityrule_createdonbehalfby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_syncerrorbase_createdby"></a> lk_syncerrorbase_createdby

Same as syncerror entity [lk_syncerrorbase_createdby](syncerror.md#BKMK_lk_syncerrorbase_createdby) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_syncerrorbase_createdby<br />
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


### <a name="BKMK_modifiedby_sdkmessagerequestfield"></a> modifiedby_sdkmessagerequestfield

Same as sdkmessagerequestfield entity [modifiedby_sdkmessagerequestfield](sdkmessagerequestfield.md#BKMK_modifiedby_sdkmessagerequestfield) Many-To-One relationship.

**ReferencingEntity**: sdkmessagerequestfield<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: modifiedby_sdkmessagerequestfield<br />
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


### <a name="BKMK_createdby_sdkmessagefilter"></a> createdby_sdkmessagefilter

Same as sdkmessagefilter entity [createdby_sdkmessagefilter](sdkmessagefilter.md#BKMK_createdby_sdkmessagefilter) Many-To-One relationship.

**ReferencingEntity**: sdkmessagefilter<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: createdby_sdkmessagefilter<br />
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


### <a name="BKMK_lk_knowledgesearchmodel_createdby"></a> lk_knowledgesearchmodel_createdby

Same as knowledgesearchmodel entity [lk_knowledgesearchmodel_createdby](knowledgesearchmodel.md#BKMK_lk_knowledgesearchmodel_createdby) Many-To-One relationship.

**ReferencingEntity**: knowledgesearchmodel<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_knowledgesearchmodel_createdby<br />
**AssociatedMenuConfiguration**:

- **Behavior**: UseCollectionName
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


### <a name="BKMK_lk_kbarticlebase_modifiedby"></a> lk_kbarticlebase_modifiedby

Same as kbarticle entity [lk_kbarticlebase_modifiedby](kbarticle.md#BKMK_lk_kbarticlebase_modifiedby) Many-To-One relationship.

**ReferencingEntity**: kbarticle<br />
**ReferencingAttribute**: modifiedby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: lk_kbarticlebase_modifiedby<br />
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


### <a name="BKMK_lk_ownermapping_createdby"></a> lk_ownermapping_createdby

Same as ownermapping entity [lk_ownermapping_createdby](ownermapping.md#BKMK_lk_ownermapping_createdby) Many-To-One relationship.

**ReferencingEntity**: ownermapping<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_ownermapping_createdby<br />
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


### <a name="BKMK_SystemUser_SyncErrors"></a> SystemUser_SyncErrors

Same as syncerror entity [SystemUser_SyncErrors](syncerror.md#BKMK_SystemUser_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: SystemUser_SyncErrors<br />
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


### <a name="BKMK_lk_duplicateruleconditionbase_createdby"></a> lk_duplicateruleconditionbase_createdby

Same as duplicaterulecondition entity [lk_duplicateruleconditionbase_createdby](duplicaterulecondition.md#BKMK_lk_duplicateruleconditionbase_createdby) Many-To-One relationship.

**ReferencingEntity**: duplicaterulecondition<br />
**ReferencingAttribute**: createdby<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: lk_duplicateruleconditionbase_createdby<br />
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

<a name="manytoone"></a>

## Many-To-One Relationships

Each Many-To-One relationship is defined by a corresponding One-To-Many relationship with the related entity. Listed by **SchemaName**.

- [territory_system_users](#BKMK_territory_system_users)
- [systemuser_defaultmailbox_mailbox](#BKMK_systemuser_defaultmailbox_mailbox)
- [position_users](#BKMK_position_users)
- [calendar_system_users](#BKMK_calendar_system_users)
- [business_unit_system_users](#BKMK_business_unit_system_users)
- [MobileOfflineProfile_SystemUser](#BKMK_MobileOfflineProfile_SystemUser)
- [TransactionCurrency_SystemUser](#BKMK_TransactionCurrency_SystemUser)
- [user_parent_user](#BKMK_user_parent_user)
- [organization_system_users](#BKMK_organization_system_users)
- [lk_systemuserbase_modifiedby](#BKMK_lk_systemuserbase_modifiedby)
- [queue_system_user](#BKMK_queue_system_user)
- [lk_systemuser_modifiedonbehalfby](#BKMK_lk_systemuser_modifiedonbehalfby)
- [processstage_systemusers](#BKMK_processstage_systemusers)
- [lk_systemuserbase_createdby](#BKMK_lk_systemuserbase_createdby)
- [lk_systemuser_createdonbehalfby](#BKMK_lk_systemuser_createdonbehalfby)


### <a name="BKMK_territory_system_users"></a> territory_system_users

See territory Entity [territory_system_users](territory.md#BKMK_territory_system_users) One-To-Many relationship.

### <a name="BKMK_systemuser_defaultmailbox_mailbox"></a> systemuser_defaultmailbox_mailbox

See mailbox Entity [systemuser_defaultmailbox_mailbox](mailbox.md#BKMK_systemuser_defaultmailbox_mailbox) One-To-Many relationship.

### <a name="BKMK_position_users"></a> position_users

See position Entity [position_users](position.md#BKMK_position_users) One-To-Many relationship.

### <a name="BKMK_calendar_system_users"></a> calendar_system_users

See calendar Entity [calendar_system_users](calendar.md#BKMK_calendar_system_users) One-To-Many relationship.

### <a name="BKMK_business_unit_system_users"></a> business_unit_system_users

See businessunit Entity [business_unit_system_users](businessunit.md#BKMK_business_unit_system_users) One-To-Many relationship.

### <a name="BKMK_MobileOfflineProfile_SystemUser"></a> MobileOfflineProfile_SystemUser

See mobileofflineprofile Entity [MobileOfflineProfile_SystemUser](mobileofflineprofile.md#BKMK_MobileOfflineProfile_SystemUser) One-To-Many relationship.

### <a name="BKMK_TransactionCurrency_SystemUser"></a> TransactionCurrency_SystemUser

See transactioncurrency Entity [TransactionCurrency_SystemUser](transactioncurrency.md#BKMK_TransactionCurrency_SystemUser) One-To-Many relationship.

### <a name="BKMK_user_parent_user"></a> user_parent_user

See systemuser Entity [user_parent_user](systemuser.md#BKMK_user_parent_user) One-To-Many relationship.

### <a name="BKMK_organization_system_users"></a> organization_system_users

See organization Entity [organization_system_users](organization.md#BKMK_organization_system_users) One-To-Many relationship.

### <a name="BKMK_lk_systemuserbase_modifiedby"></a> lk_systemuserbase_modifiedby

See systemuser Entity [lk_systemuserbase_modifiedby](systemuser.md#BKMK_lk_systemuserbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_queue_system_user"></a> queue_system_user

See queue Entity [queue_system_user](queue.md#BKMK_queue_system_user) One-To-Many relationship.

### <a name="BKMK_lk_systemuser_modifiedonbehalfby"></a> lk_systemuser_modifiedonbehalfby

See systemuser Entity [lk_systemuser_modifiedonbehalfby](systemuser.md#BKMK_lk_systemuser_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_processstage_systemusers"></a> processstage_systemusers

See processstage Entity [processstage_systemusers](processstage.md#BKMK_processstage_systemusers) One-To-Many relationship.

### <a name="BKMK_lk_systemuserbase_createdby"></a> lk_systemuserbase_createdby

See systemuser Entity [lk_systemuserbase_createdby](systemuser.md#BKMK_lk_systemuserbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_systemuser_createdonbehalfby"></a> lk_systemuser_createdonbehalfby

See systemuser Entity [lk_systemuser_createdonbehalfby](systemuser.md#BKMK_lk_systemuser_createdonbehalfby) One-To-Many relationship.
<a name="manytomany"></a>

## Many-To-Many Relationships

Relationship details provided where the SystemUser entity is the first entity in the relationship. Listed by **SchemaName**.

- [systemuserprofiles_association](#BKMK_systemuserprofiles_association)
- [systemuserroles_association](#BKMK_systemuserroles_association)
- [teammembership_association](#BKMK_teammembership_association)
- [queuemembership_association](#BKMK_queuemembership_association)


### <a name="BKMK_systemuserprofiles_association"></a> systemuserprofiles_association

**IntersectEntityName**: systemuserprofiles<br />
**Entity1LogicalName**: systemuser<br />

- **Entity1IntersectAttribute**: systemuserid
- **Entity1NavigationPropertyName**: systemuserprofiles_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: UseCollectionName
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [fieldsecurityprofile](fieldsecurityprofile.md)<br />

- **Entity2IntersectAttribute**: fieldsecurityprofileid
- **Entity2NavigationPropertyName**: systemuserprofiles_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: UseCollectionName
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />

### <a name="BKMK_systemuserroles_association"></a> systemuserroles_association

**IntersectEntityName**: systemuserroles<br />
**Entity1LogicalName**: systemuser<br />

- **Entity1IntersectAttribute**: systemuserid
- **Entity1NavigationPropertyName**: systemuserroles_association
- **Entity1AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**Entity2LogicalName**: [role](role.md)<br />

- **Entity2IntersectAttribute**: roleid
- **Entity2NavigationPropertyName**: systemuserroles_association
- **Entity2AssociatedMenuConfiguration**:

  - **Behavior**: DoNotDisplay
  - **Group**: Details
  - **Label**: 
  - **Order**: 

**IsCustomizable**: False<br />

### <a name="BKMK_teammembership_association"></a> teammembership_association

See team Entity [teammembership_association](team.md#BKMK_teammembership_association) Many-To-Many Relationship.

### <a name="BKMK_queuemembership_association"></a> queuemembership_association

See queue Entity [queuemembership_association](queue.md#BKMK_queuemembership_association) Many-To-Many Relationship.
systemuser

