---
title: "BusinessUnit Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the BusinessUnit entity."
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
# BusinessUnit Entity Reference

Business, division, or department in the Microsoft Dynamics 365 database.

## Entity Properties

**DisplayName**: Business Unit<br />
**DisplayCollectionName**: Business Units<br />
**SchemaName**: BusinessUnit<br />
**CollectionSchemaName**: BusinessUnits<br />
**LogicalName**: businessunit<br />
**LogicalCollectionName**: businessunits<br />
**EntitySetName**: businessunits<br />
**PrimaryIdAttribute**: businessunitid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: BusinessOwned<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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
- [BusinessUnitId](#BKMK_BusinessUnitId)
- [CalendarId](#BKMK_CalendarId)
- [CostCenter](#BKMK_CostCenter)
- [CreditLimit](#BKMK_CreditLimit)
- [Description](#BKMK_Description)
- [DivisionName](#BKMK_DivisionName)
- [EMailAddress](#BKMK_EMailAddress)
- [FileAsName](#BKMK_FileAsName)
- [FtpSiteUrl](#BKMK_FtpSiteUrl)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [InheritanceMask](#BKMK_InheritanceMask)
- [IsDisabled](#BKMK_IsDisabled)
- [Name](#BKMK_Name)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentBusinessUnitId](#BKMK_ParentBusinessUnitId)
- [Picture](#BKMK_Picture)
- [StockExchange](#BKMK_StockExchange)
- [TickerSymbol](#BKMK_TickerSymbol)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UTCOffset](#BKMK_UTCOffset)
- [WebSiteUrl](#BKMK_WebSiteUrl)
- [WorkflowSuspended](#BKMK_WorkflowSuspended)


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
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address1_City"></a> Address1_City

**Description**: City name for address 1.<br />
**DisplayName**: Bill To City<br />
**LogicalName**: address1_city<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


### <a name="BKMK_Address1_Country"></a> Address1_Country

**Description**: Country/region name for address 1.<br />
**DisplayName**: Bill To Country/Region<br />
**LogicalName**: address1_country<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


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
**MaxLength**: 50


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
**MaxLength**: 50


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
**DisplayName**: Bill To Street 1<br />
**LogicalName**: address1_line1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_Address1_Line2"></a> Address1_Line2

**Description**: Second line for entering address 1 information.<br />
**DisplayName**: Bill To Street 2<br />
**LogicalName**: address1_line2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_Address1_Line3"></a> Address1_Line3

**Description**: Third line for entering address 1 information.<br />
**DisplayName**: Bill To Street 3<br />
**LogicalName**: address1_line3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


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
**DisplayName**: Bill To ZIP/Postal Code<br />
**LogicalName**: address1_postalcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


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
**MaxLength**: 20


### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

**Description**: Method of shipment for address 1.<br />
**DisplayName**: Address 1: Shipping Method<br />
**LogicalName**: address1_shippingmethodcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

**Description**: State or province for address 1.<br />
**DisplayName**: Bill To State/Province<br />
**LogicalName**: address1_stateorprovince<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address1_Telephone1"></a> Address1_Telephone1

**Description**: First telephone number associated with address 1.<br />
**DisplayName**: Main Phone<br />
**LogicalName**: address1_telephone1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address1_Telephone2"></a> Address1_Telephone2

**Description**: Second telephone number associated with address 1.<br />
**DisplayName**: Other Phone<br />
**LogicalName**: address1_telephone2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address1_Telephone3"></a> Address1_Telephone3

**Description**: Third telephone number associated with address 1.<br />
**DisplayName**: Address 1: Telephone 3<br />
**LogicalName**: address1_telephone3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address1_UPSZone"></a> Address1_UPSZone

**Description**: United Parcel Service (UPS) zone for address 1.<br />
**DisplayName**: Address 1: UPS Zone<br />
**LogicalName**: address1_upszone<br />
**IsValidForForm**: True<br />
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
**IsValidForForm**: True<br />
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
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address2_City"></a> Address2_City

**Description**: City name for address 2.<br />
**DisplayName**: Ship To City<br />
**LogicalName**: address2_city<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


### <a name="BKMK_Address2_Country"></a> Address2_Country

**Description**: Country/region name for address 2.<br />
**DisplayName**: Ship To Country/Region<br />
**LogicalName**: address2_country<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


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
**MaxLength**: 50


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
**DisplayName**: Ship To Street 1<br />
**LogicalName**: address2_line1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_Address2_Line2"></a> Address2_Line2

**Description**: Second line for entering address 2 information.<br />
**DisplayName**: Ship To Street 2<br />
**LogicalName**: address2_line2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


### <a name="BKMK_Address2_Line3"></a> Address2_Line3

**Description**: Third line for entering address 2 information.<br />
**DisplayName**: Ship To Street 3<br />
**LogicalName**: address2_line3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 250


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
**DisplayName**: Ship To ZIP/Postal Code<br />
**LogicalName**: address2_postalcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


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
**MaxLength**: 20


### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

**Description**: Method of shipment for address 2.<br />
**DisplayName**: Address 2: Shipping Method<br />
**LogicalName**: address2_shippingmethodcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default Value



### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

**Description**: State or province for address 2.<br />
**DisplayName**: Ship To State/Province<br />
**LogicalName**: address2_stateorprovince<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address2_Telephone1"></a> Address2_Telephone1

**Description**: First telephone number associated with address 2.<br />
**DisplayName**: Address 2: Telephone 1<br />
**LogicalName**: address2_telephone1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
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
**FormatName**: Text<br />
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
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Address2_UPSZone"></a> Address2_UPSZone

**Description**: United Parcel Service (UPS) zone for address 2.<br />
**DisplayName**: Address 2: UPS Zone<br />
**LogicalName**: address2_upszone<br />
**IsValidForForm**: True<br />
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
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: TimeZone<br />
**MaxValue**: 1500<br />
**MinValue**: -1500


### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

**Description**: Unique identifier of the business unit.<br />
**DisplayName**: Business Unit<br />
**LogicalName**: businessunitid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_CalendarId"></a> CalendarId

**Description**: Fiscal calendar associated with the business unit.<br />
**DisplayName**: Calendar<br />
**LogicalName**: calendarid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: calendar


### <a name="BKMK_CostCenter"></a> CostCenter

**Description**: Name of the business unit cost center.<br />
**DisplayName**: Cost Center<br />
**LogicalName**: costcenter<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_CreditLimit"></a> CreditLimit

**Description**: Credit limit for the business unit.<br />
**DisplayName**: Credit Limit<br />
**LogicalName**: creditlimit<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0<br />
**Precision**: 2


### <a name="BKMK_Description"></a> Description

**Description**: Description of the business unit.<br />
**DisplayName**: Description<br />
**LogicalName**: description<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 2000


### <a name="BKMK_DivisionName"></a> DivisionName

**Description**: Name of the division to which the business unit belongs.<br />
**DisplayName**: Division<br />
**LogicalName**: divisionname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_EMailAddress"></a> EMailAddress

**Description**: Email address for the business unit.<br />
**DisplayName**: Email<br />
**LogicalName**: emailaddress<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Email<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FileAsName"></a> FileAsName

**Description**: Alternative name under which the business unit can be filed.<br />
**DisplayName**: File as Name<br />
**LogicalName**: fileasname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 100


### <a name="BKMK_FtpSiteUrl"></a> FtpSiteUrl

**Description**: FTP site URL for the business unit.<br />
**DisplayName**: FTP Site<br />
**LogicalName**: ftpsiteurl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


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


### <a name="BKMK_InheritanceMask"></a> InheritanceMask

**Description**: Inheritance mask for the business unit.<br />
**DisplayName**: Inheritance Mask<br />
**LogicalName**: inheritancemask<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForUpdate**: False<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_IsDisabled"></a> IsDisabled

**Description**: Information about whether the business unit is enabled or disabled.<br />
**DisplayName**: Is Disabled<br />
**LogicalName**: isdisabled<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**IsValidForCreate**: False<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False


### <a name="BKMK_Name"></a> Name

**Description**: Name of the business unit.<br />
**DisplayName**: Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 160


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


### <a name="BKMK_ParentBusinessUnitId"></a> ParentBusinessUnitId

**Description**: Unique identifier for the parent business unit.<br />
**DisplayName**: Parent Business<br />
**LogicalName**: parentbusinessunitid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: Lookup<br />
**Targets**: businessunit


### <a name="BKMK_Picture"></a> Picture

**Description**: Picture or diagram of the business unit.<br />
**DisplayName**: Picture<br />
**LogicalName**: picture<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Memo<br />
**Format**: TextArea<br />
**IsLocalizable**: False<br />
**MaxLength**: 1073741823


### <a name="BKMK_StockExchange"></a> StockExchange

**Description**: Stock exchange on which the business is listed.<br />
**DisplayName**: Stock Exchange<br />
**LogicalName**: stockexchange<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_TickerSymbol"></a> TickerSymbol

**Description**: Stock exchange ticker symbol for the business unit.<br />
**DisplayName**: Ticker Symbol<br />
**LogicalName**: tickersymbol<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 10


### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

**Description**: Unique identifier of the currency associated with the businessunit.<br />
**DisplayName**: Currency<br />
**LogicalName**: transactioncurrencyid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Lookup<br />
**Targets**: transactioncurrency


### <a name="BKMK_UTCOffset"></a> UTCOffset

**Description**: UTC offset for the business unit. This is the difference between local time and standard Coordinated Universal Time.<br />
**DisplayName**: UTC Offset<br />
**LogicalName**: utcoffset<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: TimeZone<br />
**MaxValue**: 1500<br />
**MinValue**: -1500


### <a name="BKMK_WebSiteUrl"></a> WebSiteUrl

**Description**: Website URL for the business unit.<br />
**DisplayName**: Website<br />
**LogicalName**: websiteurl<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Url<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_WorkflowSuspended"></a> WorkflowSuspended

**Description**: Information about whether workflow or sales process rules have been suspended.<br />
**DisplayName**: Workflow Suspended<br />
**LogicalName**: workflowsuspended<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Boolean<br />
**Options**:

- **TrueOption Value**: 1 **Label**: Yes
- **FalseOption Value**: 0 **Label**: No

**DefaultValue**: False

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
- [DisabledReason](#BKMK_DisabledReason)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [OrganizationId](#BKMK_OrganizationId)
- [OrganizationIdName](#BKMK_OrganizationIdName)
- [ParentBusinessUnitIdName](#BKMK_ParentBusinessUnitIdName)
- [TransactionCurrencyIdName](#BKMK_TransactionCurrencyIdName)
- [UserGroupId](#BKMK_UserGroupId)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the business unit.<br />
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

**Description**: Date and time when the business unit was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the businessunit.<br />
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


### <a name="BKMK_DisabledReason"></a> DisabledReason

**Description**: Reason for disabling the business unit.<br />
**DisplayName**: Disable Reason<br />
**LogicalName**: disabledreason<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 500


### <a name="BKMK_ExchangeRate"></a> ExchangeRate

**Description**: Exchange rate for the currency associated with the businessunit with respect to the base currency.<br />
**DisplayName**: Exchange Rate<br />
**LogicalName**: exchangerate<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Decimal<br />
**MaxValue**: 100000000000<br />
**MinValue**: 0.0000000001<br />
**Precision**: 10


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the business unit.<br />
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

**Description**: Date and time when the business unit was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who last modified the businessunit.<br />
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

**Description**: Unique identifier of the organization associated with the business unit.<br />
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


### <a name="BKMK_ParentBusinessUnitIdName"></a> ParentBusinessUnitIdName

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: parentbusinessunitidname<br />
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


### <a name="BKMK_UserGroupId"></a> UserGroupId

**Description**: <br />
**DisplayName**: <br />
**LogicalName**: usergroupid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: False<br />
**RequiredLevel**: None<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_VersionNumber"></a> VersionNumber

**Description**: Version number of the business unit.<br />
**DisplayName**: Version number<br />
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

- [business_unit_exchangesyncidmapping](#BKMK_business_unit_exchangesyncidmapping)
- [business_unit_interactionforemail](#BKMK_business_unit_interactionforemail)
- [business_unit_knowledgearticle](#BKMK_business_unit_knowledgearticle)
- [business_unit_sharepointdocumentlocation](#BKMK_business_unit_sharepointdocumentlocation)
- [business_unit_goal](#BKMK_business_unit_goal)
- [business_unit_mailbox](#BKMK_business_unit_mailbox)
- [business_unit_channelaccessprofile](#BKMK_business_unit_channelaccessprofile)
- [business_unit_externalparty](#BKMK_business_unit_externalparty)
- [business_unit_recurrencerule](#BKMK_business_unit_recurrencerule)
- [business_unit_profilerule](#BKMK_business_unit_profilerule)
- [BusinessUnit_AsyncOperations](#BKMK_BusinessUnit_AsyncOperations)
- [BusinessUnit_ImportLogs](#BKMK_BusinessUnit_ImportLogs)
- [business_unit_user_settings](#BKMK_business_unit_user_settings)
- [userentityuisettings_businessunit](#BKMK_userentityuisettings_businessunit)
- [BusinessUnit_SyncError](#BKMK_BusinessUnit_SyncError)
- [business_unit_sharepointsites](#BKMK_business_unit_sharepointsites)
- [business_unit_feedback](#BKMK_business_unit_feedback)
- [business_unit_roles](#BKMK_business_unit_roles)
- [business_unit_postfollows](#BKMK_business_unit_postfollows)
- [business_unit_teams](#BKMK_business_unit_teams)
- [business_unit_queues2](#BKMK_business_unit_queues2)
- [business_unit_goalrollupquery](#BKMK_business_unit_goalrollupquery)
- [business_unit_userquery](#BKMK_business_unit_userquery)
- [BusinessUnit_Imports](#BKMK_BusinessUnit_Imports)
- [BusinessUnit_ImportFiles](#BKMK_BusinessUnit_ImportFiles)
- [business_unit_letter_activities](#BKMK_business_unit_letter_activities)
- [businessunit_mailboxtrackingfolder](#BKMK_businessunit_mailboxtrackingfolder)
- [business_unit_queues](#BKMK_business_unit_queues)
- [business_unit_annotations](#BKMK_business_unit_annotations)
- [business_unit_workflow](#BKMK_business_unit_workflow)
- [business_unit_personaldocumenttemplates](#BKMK_business_unit_personaldocumenttemplates)
- [businessunit_principalobjectattributeaccess](#BKMK_businessunit_principalobjectattributeaccess)
- [business_unit_emailserverprofile](#BKMK_business_unit_emailserverprofile)
- [business_unit_templates](#BKMK_business_unit_templates)
- [business_unit_contacts](#BKMK_business_unit_contacts)
- [BulkDeleteOperation_BusinessUnit](#BKMK_BulkDeleteOperation_BusinessUnit)
- [business_unit_task_activities](#BKMK_business_unit_task_activities)
- [business_unit_actioncards](#BKMK_business_unit_actioncards)
- [business_unit_asyncoperation](#BKMK_business_unit_asyncoperation)
- [business_unit_mailmergetemplates](#BKMK_business_unit_mailmergetemplates)
- [business_unit_userform](#BKMK_business_unit_userform)
- [business_unit_category](#BKMK_business_unit_category)
- [business_unit_connections](#BKMK_business_unit_connections)
- [BusinessUnit_SyncErrors](#BKMK_BusinessUnit_SyncErrors)
- [business_unit_workflowlogs](#BKMK_business_unit_workflowlogs)
- [business_unit_phone_call_activities](#BKMK_business_unit_phone_call_activities)
- [business_unit_fax_activities](#BKMK_business_unit_fax_activities)
- [business_unit_appointment_activities](#BKMK_business_unit_appointment_activities)
- [business_unit_routingrule](#BKMK_business_unit_routingrule)
- [BusinessUnit_DuplicateRules](#BKMK_BusinessUnit_DuplicateRules)
- [business_unit_sharepointdocument](#BKMK_business_unit_sharepointdocument)
- [business_unit_email_activities](#BKMK_business_unit_email_activities)
- [business_unit_sharepointdocument2](#BKMK_business_unit_sharepointdocument2)
- [business_unit_socialactivity](#BKMK_business_unit_socialactivity)
- [business_unit_reports](#BKMK_business_unit_reports)
- [business_unit_calendars](#BKMK_business_unit_calendars)
- [BusinessUnit_ImportMaps](#BKMK_BusinessUnit_ImportMaps)
- [business_unit_convertrule](#BKMK_business_unit_convertrule)
- [userentityinstancedata_businessunit](#BKMK_userentityinstancedata_businessunit)
- [business_unit_customer_relationship](#BKMK_business_unit_customer_relationship)
- [business_unit_slakpiinstance](#BKMK_business_unit_slakpiinstance)
- [business_unit_emailsignatures](#BKMK_business_unit_emailsignatures)
- [business_unit_recurringappointmentmaster_activities](#BKMK_business_unit_recurringappointmentmaster_activities)
- [business_unit_slabase](#BKMK_business_unit_slabase)
- [business_unit_userqueryvisualizations](#BKMK_business_unit_userqueryvisualizations)
- [actioncardusersettings_businessunit](#BKMK_actioncardusersettings_businessunit)
- [business_unit_system_users](#BKMK_business_unit_system_users)
- [business_unit_socialprofiles](#BKMK_business_unit_socialprofiles)
- [BusinessUnit_BulkDeleteFailures](#BKMK_BusinessUnit_BulkDeleteFailures)
- [BusinessUnit_ProcessSessions](#BKMK_BusinessUnit_ProcessSessions)
- [business_unit_accounts](#BKMK_business_unit_accounts)
- [business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit)
- [Owning_businessunit_processsessions](#BKMK_Owning_businessunit_processsessions)
- [business_unit_activitypointer](#BKMK_business_unit_activitypointer)


### <a name="BKMK_business_unit_exchangesyncidmapping"></a> business_unit_exchangesyncidmapping

Same as exchangesyncidmapping entity [business_unit_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_business_unit_exchangesyncidmapping) Many-To-One relationship.

**ReferencingEntity**: exchangesyncidmapping<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_exchangesyncidmapping<br />
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


### <a name="BKMK_business_unit_interactionforemail"></a> business_unit_interactionforemail

Same as interactionforemail entity [business_unit_interactionforemail](interactionforemail.md#BKMK_business_unit_interactionforemail) Many-To-One relationship.

**ReferencingEntity**: interactionforemail<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_new_interactionforemail<br />
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


### <a name="BKMK_business_unit_knowledgearticle"></a> business_unit_knowledgearticle

Same as knowledgearticle entity [business_unit_knowledgearticle](knowledgearticle.md#BKMK_business_unit_knowledgearticle) Many-To-One relationship.

**ReferencingEntity**: knowledgearticle<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_knowledgearticle<br />
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


### <a name="BKMK_business_unit_sharepointdocumentlocation"></a> business_unit_sharepointdocumentlocation

Same as sharepointdocumentlocation entity [business_unit_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_business_unit_sharepointdocumentlocation) Many-To-One relationship.

**ReferencingEntity**: sharepointdocumentlocation<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_sharepointdocumentlocation<br />
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


### <a name="BKMK_business_unit_goal"></a> business_unit_goal

Same as goal entity [business_unit_goal](goal.md#BKMK_business_unit_goal) Many-To-One relationship.

**ReferencingEntity**: goal<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_goal<br />
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


### <a name="BKMK_business_unit_mailbox"></a> business_unit_mailbox

Same as mailbox entity [business_unit_mailbox](mailbox.md#BKMK_business_unit_mailbox) Many-To-One relationship.

**ReferencingEntity**: mailbox<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_mailbox<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_channelaccessprofile"></a> business_unit_channelaccessprofile

Same as channelaccessprofile entity [business_unit_channelaccessprofile](channelaccessprofile.md#BKMK_business_unit_channelaccessprofile) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofile<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_channelaccessprofile<br />
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


### <a name="BKMK_business_unit_externalparty"></a> business_unit_externalparty

Same as externalparty entity [business_unit_externalparty](externalparty.md#BKMK_business_unit_externalparty) Many-To-One relationship.

**ReferencingEntity**: externalparty<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_externalparty<br />
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


### <a name="BKMK_business_unit_recurrencerule"></a> business_unit_recurrencerule

Same as recurrencerule entity [business_unit_recurrencerule](recurrencerule.md#BKMK_business_unit_recurrencerule) Many-To-One relationship.

**ReferencingEntity**: recurrencerule<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_recurrencerule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_profilerule"></a> business_unit_profilerule

Same as channelaccessprofilerule entity [business_unit_profilerule](channelaccessprofilerule.md#BKMK_business_unit_profilerule) Many-To-One relationship.

**ReferencingEntity**: channelaccessprofilerule<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_profilerule<br />
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


### <a name="BKMK_BusinessUnit_AsyncOperations"></a> BusinessUnit_AsyncOperations

Same as asyncoperation entity [BusinessUnit_AsyncOperations](asyncoperation.md#BKMK_BusinessUnit_AsyncOperations) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_AsyncOperations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_ImportLogs"></a> BusinessUnit_ImportLogs

Same as importlog entity [BusinessUnit_ImportLogs](importlog.md#BKMK_BusinessUnit_ImportLogs) Many-To-One relationship.

**ReferencingEntity**: importlog<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_ImportLogs<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_user_settings"></a> business_unit_user_settings

Same as usersettings entity [business_unit_user_settings](usersettings.md#BKMK_business_unit_user_settings) Many-To-One relationship.

**ReferencingEntity**: usersettings<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_user_settings<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityuisettings_businessunit"></a> userentityuisettings_businessunit

Same as userentityuisettings entity [userentityuisettings_businessunit](userentityuisettings.md#BKMK_userentityuisettings_businessunit) Many-To-One relationship.

**ReferencingEntity**: userentityuisettings<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityuisettings_businessunit<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

Same as syncerror entity [BusinessUnit_SyncError](syncerror.md#BKMK_BusinessUnit_SyncError) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_SyncError<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_sharepointsites"></a> business_unit_sharepointsites

Same as sharepointsite entity [business_unit_sharepointsites](sharepointsite.md#BKMK_business_unit_sharepointsites) Many-To-One relationship.

**ReferencingEntity**: sharepointsite<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_sharepointsites<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_feedback"></a> business_unit_feedback

Same as feedback entity [business_unit_feedback](feedback.md#BKMK_business_unit_feedback) Many-To-One relationship.

**ReferencingEntity**: feedback<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_feedback<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_roles"></a> business_unit_roles

Same as role entity [business_unit_roles](role.md#BKMK_business_unit_roles) Many-To-One relationship.

**ReferencingEntity**: role<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_roles<br />
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


### <a name="BKMK_business_unit_postfollows"></a> business_unit_postfollows

Same as postfollow entity [business_unit_postfollows](postfollow.md#BKMK_business_unit_postfollows) Many-To-One relationship.

**ReferencingEntity**: postfollow<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_postfollows<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_teams"></a> business_unit_teams

Same as team entity [business_unit_teams](team.md#BKMK_business_unit_teams) Many-To-One relationship.

**ReferencingEntity**: team<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_teams<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_queues2"></a> business_unit_queues2

Same as queue entity [business_unit_queues2](queue.md#BKMK_business_unit_queues2) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_queues2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_goalrollupquery"></a> business_unit_goalrollupquery

Same as goalrollupquery entity [business_unit_goalrollupquery](goalrollupquery.md#BKMK_business_unit_goalrollupquery) Many-To-One relationship.

**ReferencingEntity**: goalrollupquery<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_goalrollupquery<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_userquery"></a> business_unit_userquery

Same as userquery entity [business_unit_userquery](userquery.md#BKMK_business_unit_userquery) Many-To-One relationship.

**ReferencingEntity**: userquery<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_userquery<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_Imports"></a> BusinessUnit_Imports

Same as import entity [BusinessUnit_Imports](import.md#BKMK_BusinessUnit_Imports) Many-To-One relationship.

**ReferencingEntity**: import<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_Imports<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_ImportFiles"></a> BusinessUnit_ImportFiles

Same as importfile entity [BusinessUnit_ImportFiles](importfile.md#BKMK_BusinessUnit_ImportFiles) Many-To-One relationship.

**ReferencingEntity**: importfile<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_ImportFiles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_letter_activities"></a> business_unit_letter_activities

Same as letter entity [business_unit_letter_activities](letter.md#BKMK_business_unit_letter_activities) Many-To-One relationship.

**ReferencingEntity**: letter<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_letter_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_businessunit_mailboxtrackingfolder"></a> businessunit_mailboxtrackingfolder

Same as mailboxtrackingfolder entity [businessunit_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_businessunit_mailboxtrackingfolder) Many-To-One relationship.

**ReferencingEntity**: mailboxtrackingfolder<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: businessunit_mailboxtrackingfolder<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_queues"></a> business_unit_queues

Same as queue entity [business_unit_queues](queue.md#BKMK_business_unit_queues) Many-To-One relationship.

**ReferencingEntity**: queue<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_queues<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_annotations"></a> business_unit_annotations

Same as annotation entity [business_unit_annotations](annotation.md#BKMK_business_unit_annotations) Many-To-One relationship.

**ReferencingEntity**: annotation<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_annotations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_workflow"></a> business_unit_workflow

Same as workflow entity [business_unit_workflow](workflow.md#BKMK_business_unit_workflow) Many-To-One relationship.

**ReferencingEntity**: workflow<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_workflow<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_personaldocumenttemplates"></a> business_unit_personaldocumenttemplates

Same as personaldocumenttemplate entity [business_unit_personaldocumenttemplates](personaldocumenttemplate.md#BKMK_business_unit_personaldocumenttemplates) Many-To-One relationship.

**ReferencingEntity**: personaldocumenttemplate<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_personaldocumenttemplates<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_businessunit_principalobjectattributeaccess"></a> businessunit_principalobjectattributeaccess

Same as principalobjectattributeaccess entity [businessunit_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_businessunit_principalobjectattributeaccess) Many-To-One relationship.

**ReferencingEntity**: principalobjectattributeaccess<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: businessunit_principalobjectattributeaccess<br />
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


### <a name="BKMK_business_unit_emailserverprofile"></a> business_unit_emailserverprofile

Same as emailserverprofile entity [business_unit_emailserverprofile](emailserverprofile.md#BKMK_business_unit_emailserverprofile) Many-To-One relationship.

**ReferencingEntity**: emailserverprofile<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_emailserverprofile<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_templates"></a> business_unit_templates

Same as template entity [business_unit_templates](template.md#BKMK_business_unit_templates) Many-To-One relationship.

**ReferencingEntity**: template<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_templates<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_contacts"></a> business_unit_contacts

Same as contact entity [business_unit_contacts](contact.md#BKMK_business_unit_contacts) Many-To-One relationship.

**ReferencingEntity**: contact<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_contacts<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BulkDeleteOperation_BusinessUnit"></a> BulkDeleteOperation_BusinessUnit

Same as bulkdeleteoperation entity [BulkDeleteOperation_BusinessUnit](bulkdeleteoperation.md#BKMK_BulkDeleteOperation_BusinessUnit) Many-To-One relationship.

**ReferencingEntity**: bulkdeleteoperation<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BulkDeleteOperation_BusinessUnit<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_task_activities"></a> business_unit_task_activities

Same as task entity [business_unit_task_activities](task.md#BKMK_business_unit_task_activities) Many-To-One relationship.

**ReferencingEntity**: task<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_task_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_actioncards"></a> business_unit_actioncards

Same as actioncard entity [business_unit_actioncards](actioncard.md#BKMK_business_unit_actioncards) Many-To-One relationship.

**ReferencingEntity**: actioncard<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_actioncards<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_asyncoperation"></a> business_unit_asyncoperation

Same as asyncoperation entity [business_unit_asyncoperation](asyncoperation.md#BKMK_business_unit_asyncoperation) Many-To-One relationship.

**ReferencingEntity**: asyncoperation<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_asyncoperation<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_mailmergetemplates"></a> business_unit_mailmergetemplates

Same as mailmergetemplate entity [business_unit_mailmergetemplates](mailmergetemplate.md#BKMK_business_unit_mailmergetemplates) Many-To-One relationship.

**ReferencingEntity**: mailmergetemplate<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_mailmergetemplates<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_userform"></a> business_unit_userform

Same as userform entity [business_unit_userform](userform.md#BKMK_business_unit_userform) Many-To-One relationship.

**ReferencingEntity**: userform<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_userform<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_category"></a> business_unit_category

Same as category entity [business_unit_category](category.md#BKMK_business_unit_category) Many-To-One relationship.

**ReferencingEntity**: category<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_category<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_connections"></a> business_unit_connections

Same as connection entity [business_unit_connections](connection.md#BKMK_business_unit_connections) Many-To-One relationship.

**ReferencingEntity**: connection<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_connections<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

Same as syncerror entity [BusinessUnit_SyncErrors](syncerror.md#BKMK_BusinessUnit_SyncErrors) Many-To-One relationship.

**ReferencingEntity**: syncerror<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_SyncErrors<br />
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
- **Share**: Cascade
- **Unshare**: Cascade


### <a name="BKMK_business_unit_workflowlogs"></a> business_unit_workflowlogs

Same as workflowlog entity [business_unit_workflowlogs](workflowlog.md#BKMK_business_unit_workflowlogs) Many-To-One relationship.

**ReferencingEntity**: workflowlog<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_workflowlogs<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_phone_call_activities"></a> business_unit_phone_call_activities

Same as phonecall entity [business_unit_phone_call_activities](phonecall.md#BKMK_business_unit_phone_call_activities) Many-To-One relationship.

**ReferencingEntity**: phonecall<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_phone_call_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_fax_activities"></a> business_unit_fax_activities

Same as fax entity [business_unit_fax_activities](fax.md#BKMK_business_unit_fax_activities) Many-To-One relationship.

**ReferencingEntity**: fax<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_fax_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_appointment_activities"></a> business_unit_appointment_activities

Same as appointment entity [business_unit_appointment_activities](appointment.md#BKMK_business_unit_appointment_activities) Many-To-One relationship.

**ReferencingEntity**: appointment<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_appointment_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_routingrule"></a> business_unit_routingrule

Same as routingrule entity [business_unit_routingrule](routingrule.md#BKMK_business_unit_routingrule) Many-To-One relationship.

**ReferencingEntity**: routingrule<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_routingrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_DuplicateRules"></a> BusinessUnit_DuplicateRules

Same as duplicaterule entity [BusinessUnit_DuplicateRules](duplicaterule.md#BKMK_BusinessUnit_DuplicateRules) Many-To-One relationship.

**ReferencingEntity**: duplicaterule<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_DuplicateRules<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_sharepointdocument"></a> business_unit_sharepointdocument

Same as sharepointdocument entity [business_unit_sharepointdocument](sharepointdocument.md#BKMK_business_unit_sharepointdocument) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_sharepointdocument<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_email_activities"></a> business_unit_email_activities

Same as email entity [business_unit_email_activities](email.md#BKMK_business_unit_email_activities) Many-To-One relationship.

**ReferencingEntity**: email<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_email_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_sharepointdocument2"></a> business_unit_sharepointdocument2

Same as sharepointdocument entity [business_unit_sharepointdocument2](sharepointdocument.md#BKMK_business_unit_sharepointdocument2) Many-To-One relationship.

**ReferencingEntity**: sharepointdocument<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_sharepointdocument2<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_socialactivity"></a> business_unit_socialactivity

Same as socialactivity entity [business_unit_socialactivity](socialactivity.md#BKMK_business_unit_socialactivity) Many-To-One relationship.

**ReferencingEntity**: socialactivity<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_socialactivity<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_reports"></a> business_unit_reports

Same as report entity [business_unit_reports](report.md#BKMK_business_unit_reports) Many-To-One relationship.

**ReferencingEntity**: report<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_reports<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_calendars"></a> business_unit_calendars

Same as calendar entity [business_unit_calendars](calendar.md#BKMK_business_unit_calendars) Many-To-One relationship.

**ReferencingEntity**: calendar<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_calendars<br />
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


### <a name="BKMK_BusinessUnit_ImportMaps"></a> BusinessUnit_ImportMaps

Same as importmap entity [BusinessUnit_ImportMaps](importmap.md#BKMK_BusinessUnit_ImportMaps) Many-To-One relationship.

**ReferencingEntity**: importmap<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_ImportMaps<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_convertrule"></a> business_unit_convertrule

Same as convertrule entity [business_unit_convertrule](convertrule.md#BKMK_business_unit_convertrule) Many-To-One relationship.

**ReferencingEntity**: convertrule<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_convertrule<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_userentityinstancedata_businessunit"></a> userentityinstancedata_businessunit

Same as userentityinstancedata entity [userentityinstancedata_businessunit](userentityinstancedata.md#BKMK_userentityinstancedata_businessunit) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_businessunit<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_customer_relationship"></a> business_unit_customer_relationship

Same as customerrelationship entity [business_unit_customer_relationship](customerrelationship.md#BKMK_business_unit_customer_relationship) Many-To-One relationship.

**ReferencingEntity**: customerrelationship<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_customer_relationship<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_slakpiinstance"></a> business_unit_slakpiinstance

Same as slakpiinstance entity [business_unit_slakpiinstance](slakpiinstance.md#BKMK_business_unit_slakpiinstance) Many-To-One relationship.

**ReferencingEntity**: slakpiinstance<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_slakpiinstance<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_emailsignatures"></a> business_unit_emailsignatures

Same as emailsignature entity [business_unit_emailsignatures](emailsignature.md#BKMK_business_unit_emailsignatures) Many-To-One relationship.

**ReferencingEntity**: emailsignature<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_emailsignatures<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_recurringappointmentmaster_activities"></a> business_unit_recurringappointmentmaster_activities

Same as recurringappointmentmaster entity [business_unit_recurringappointmentmaster_activities](recurringappointmentmaster.md#BKMK_business_unit_recurringappointmentmaster_activities) Many-To-One relationship.

**ReferencingEntity**: recurringappointmentmaster<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_recurringappointmentmaster_activities<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_slabase"></a> business_unit_slabase

Same as sla entity [business_unit_slabase](sla.md#BKMK_business_unit_slabase) Many-To-One relationship.

**ReferencingEntity**: sla<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_slabase<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_userqueryvisualizations"></a> business_unit_userqueryvisualizations

Same as userqueryvisualization entity [business_unit_userqueryvisualizations](userqueryvisualization.md#BKMK_business_unit_userqueryvisualizations) Many-To-One relationship.

**ReferencingEntity**: userqueryvisualization<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_userqueryvisualizations<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_actioncardusersettings_businessunit"></a> actioncardusersettings_businessunit

Same as actioncardusersettings entity [actioncardusersettings_businessunit](actioncardusersettings.md#BKMK_actioncardusersettings_businessunit) Many-To-One relationship.

**ReferencingEntity**: actioncardusersettings<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: actioncardusersettings_businessunit<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_system_users"></a> business_unit_system_users

Same as systemuser entity [business_unit_system_users](systemuser.md#BKMK_business_unit_system_users) Many-To-One relationship.

**ReferencingEntity**: systemuser<br />
**ReferencingAttribute**: businessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_system_users<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_socialprofiles"></a> business_unit_socialprofiles

Same as socialprofile entity [business_unit_socialprofiles](socialprofile.md#BKMK_business_unit_socialprofiles) Many-To-One relationship.

**ReferencingEntity**: socialprofile<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_socialprofiles<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_BusinessUnit_BulkDeleteFailures"></a> BusinessUnit_BulkDeleteFailures

Same as bulkdeletefailure entity [BusinessUnit_BulkDeleteFailures](bulkdeletefailure.md#BKMK_BusinessUnit_BulkDeleteFailures) Many-To-One relationship.

**ReferencingEntity**: bulkdeletefailure<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_BulkDeleteFailures<br />
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


### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

Same as processsession entity [BusinessUnit_ProcessSessions](processsession.md#BKMK_BusinessUnit_ProcessSessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: regardingobjectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: BusinessUnit_ProcessSessions<br />
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


### <a name="BKMK_business_unit_accounts"></a> business_unit_accounts

Same as account entity [business_unit_accounts](account.md#BKMK_business_unit_accounts) Many-To-One relationship.

**ReferencingEntity**: account<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_accounts<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_parent_business_unit"></a> business_unit_parent_business_unit

Same as businessunit entity [business_unit_parent_business_unit](businessunit.md#BKMK_business_unit_parent_business_unit) Many-To-One relationship.

**ReferencingEntity**: businessunit<br />
**ReferencingAttribute**: parentbusinessunitid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: True<br />
**ReferencedEntityNavigationPropertyName**: business_unit_parent_business_unit<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: Restrict
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

Same as processsession entity [Owning_businessunit_processsessions](processsession.md#BKMK_Owning_businessunit_processsessions) Many-To-One relationship.

**ReferencingEntity**: processsession<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: Owning_businessunit_processsessions<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
- **Label**: 
- **Order**: 

**CascadeConfiguration**:

- **Assign**: NoCascade
- **Delete**: NoCascade
- **Merge**: NoCascade
- **Reparent**: NoCascade
- **Share**: NoCascade
- **Unshare**: NoCascade


### <a name="BKMK_business_unit_activitypointer"></a> business_unit_activitypointer

Same as activitypointer entity [business_unit_activitypointer](activitypointer.md#BKMK_business_unit_activitypointer) Many-To-One relationship.

**ReferencingEntity**: activitypointer<br />
**ReferencingAttribute**: owningbusinessunit<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: business_unit_activitypointer<br />
**AssociatedMenuConfiguration**:

- **Behavior**: DoNotDisplay
- **Group**: Details
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

- [TransactionCurrency_BusinessUnit](#BKMK_TransactionCurrency_BusinessUnit)
- [lk_businessunitbase_createdby](#BKMK_lk_businessunitbase_createdby)
- [lk_businessunit_modifiedonbehalfby](#BKMK_lk_businessunit_modifiedonbehalfby)
- [business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit)
- [organization_business_units](#BKMK_organization_business_units)
- [lk_businessunit_createdonbehalfby](#BKMK_lk_businessunit_createdonbehalfby)
- [lk_businessunitbase_modifiedby](#BKMK_lk_businessunitbase_modifiedby)
- [BusinessUnit_Calendar](#BKMK_BusinessUnit_Calendar)


### <a name="BKMK_TransactionCurrency_BusinessUnit"></a> TransactionCurrency_BusinessUnit

See transactioncurrency Entity [TransactionCurrency_BusinessUnit](transactioncurrency.md#BKMK_TransactionCurrency_BusinessUnit) One-To-Many relationship.

### <a name="BKMK_lk_businessunitbase_createdby"></a> lk_businessunitbase_createdby

See systemuser Entity [lk_businessunitbase_createdby](systemuser.md#BKMK_lk_businessunitbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_businessunit_modifiedonbehalfby"></a> lk_businessunit_modifiedonbehalfby

See systemuser Entity [lk_businessunit_modifiedonbehalfby](systemuser.md#BKMK_lk_businessunit_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_business_unit_parent_business_unit"></a> business_unit_parent_business_unit

See businessunit Entity [business_unit_parent_business_unit](businessunit.md#BKMK_business_unit_parent_business_unit) One-To-Many relationship.

### <a name="BKMK_organization_business_units"></a> organization_business_units

See organization Entity [organization_business_units](organization.md#BKMK_organization_business_units) One-To-Many relationship.

### <a name="BKMK_lk_businessunit_createdonbehalfby"></a> lk_businessunit_createdonbehalfby

See systemuser Entity [lk_businessunit_createdonbehalfby](systemuser.md#BKMK_lk_businessunit_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_businessunitbase_modifiedby"></a> lk_businessunitbase_modifiedby

See systemuser Entity [lk_businessunitbase_modifiedby](systemuser.md#BKMK_lk_businessunitbase_modifiedby) One-To-Many relationship.

### <a name="BKMK_BusinessUnit_Calendar"></a> BusinessUnit_Calendar

See calendar Entity [BusinessUnit_Calendar](calendar.md#BKMK_BusinessUnit_Calendar) One-To-Many relationship.
businessunit

