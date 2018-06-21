---
title: "PublisherAddress Entity Reference (Common Data Service for Apps)| Microsoft Docs"
description: "Includes schema information and supported messages for the PublisherAddress entity."

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
---
# PublisherAddress Entity Reference

Address and shipping information. Used to store additional addresses for a publisher.

## Entity Properties

**DisplayName**: Publisher Address<br />
**DisplayCollectionName**: Publisher Addresses<br />
**SchemaName**: PublisherAddress<br />
**CollectionSchemaName**: PublisherAddresses<br />
**LogicalName**: publisheraddress<br />
**LogicalCollectionName**: publisheraddresses<br />
**EntitySetName**: publisheraddresses<br />
**PrimaryIdAttribute**: publisheraddressid<br />
**PrimaryNameAttribute**: name<br />
**OwnershipType**: None<br />
**IsBPFEntity**: False<br />
<a name="writable-attributes"></a>

## Writable attributes

These attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddressNumber](#BKMK_AddressNumber)
- [AddressTypeCode](#BKMK_AddressTypeCode)
- [City](#BKMK_City)
- [Country](#BKMK_Country)
- [County](#BKMK_County)
- [Fax](#BKMK_Fax)
- [FreightTermsCode](#BKMK_FreightTermsCode)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Latitude](#BKMK_Latitude)
- [Line1](#BKMK_Line1)
- [Line2](#BKMK_Line2)
- [Line3](#BKMK_Line3)
- [Longitude](#BKMK_Longitude)
- [Name](#BKMK_Name)
- [ParentId](#BKMK_ParentId)
- [ParentIdTypeCode](#BKMK_ParentIdTypeCode)
- [PostalCode](#BKMK_PostalCode)
- [PostOfficeBox](#BKMK_PostOfficeBox)
- [PrimaryContactName](#BKMK_PrimaryContactName)
- [PublisherAddressId](#BKMK_PublisherAddressId)
- [ShippingMethodCode](#BKMK_ShippingMethodCode)
- [StateOrProvince](#BKMK_StateOrProvince)
- [Telephone1](#BKMK_Telephone1)
- [Telephone2](#BKMK_Telephone2)
- [Telephone3](#BKMK_Telephone3)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [UPSZone](#BKMK_UPSZone)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [UTCOffset](#BKMK_UTCOffset)


### <a name="BKMK_AddressNumber"></a> AddressNumber

**Description**: Specifies which publisher address is applicable.<br />
**DisplayName**: Address Number<br />
**LogicalName**: addressnumber<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: None<br />
**MaxValue**: 1000000000<br />
**MinValue**: 0


### <a name="BKMK_AddressTypeCode"></a> AddressTypeCode

**Description**: Type of address for the publisher, such as billing, shipping, or primary address.<br />
**DisplayName**: Address Type<br />
**LogicalName**: addresstypecode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Bill To
- **Value**: 2 **Label**: Ship To
- **Value**: 3 **Label**: Primary
- **Value**: 4 **Label**: Other



### <a name="BKMK_City"></a> City

**Description**: City name in the publisher address.<br />
**DisplayName**: City<br />
**LogicalName**: city<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


### <a name="BKMK_Country"></a> Country

**Description**: Country/region name in the publisher address.<br />
**DisplayName**: Country<br />
**LogicalName**: country<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 80


### <a name="BKMK_County"></a> County

**Description**: County name in the publisher address.<br />
**DisplayName**: County<br />
**LogicalName**: county<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Fax"></a> Fax

**Description**: Fax number for the publisher address.<br />
**DisplayName**: Fax<br />
**LogicalName**: fax<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_FreightTermsCode"></a> FreightTermsCode

**Description**: Freight terms for the publisher address.<br />
**DisplayName**: Freight Terms<br />
**LogicalName**: freighttermscode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: FOB
- **Value**: 2 **Label**: No Charge



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


### <a name="BKMK_Latitude"></a> Latitude

**Description**: Latitude for the publisher address.<br />
**DisplayName**: Latitude<br />
**LogicalName**: latitude<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 90<br />
**MinValue**: -90<br />
**Precision**: 5


### <a name="BKMK_Line1"></a> Line1

**Description**: First line for entering address information.<br />
**DisplayName**: Street 1<br />
**LogicalName**: line1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Line2"></a> Line2

**Description**: Second line for entering address information.<br />
**DisplayName**: Street 2<br />
**LogicalName**: line2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Line3"></a> Line3

**Description**: Third line for entering address information.<br />
**DisplayName**: Street 3<br />
**LogicalName**: line3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Longitude"></a> Longitude

**Description**: Longitude for the publisher address.<br />
**DisplayName**: Longitude<br />
**LogicalName**: longitude<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Double<br />
**MaxValue**: 180<br />
**MinValue**: -180<br />
**Precision**: 5


### <a name="BKMK_Name"></a> Name

**Description**: Name used to identify the publisher address.<br />
**DisplayName**: Address Name<br />
**LogicalName**: name<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: ApplicationRequired<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 200


### <a name="BKMK_ParentId"></a> ParentId

**Description**: Unique identifier of the parent object with which the publisher address is associated.<br />
**DisplayName**: Parent<br />
**LogicalName**: parentid<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**Type**: Lookup<br />
**Targets**: publisher


### <a name="BKMK_ParentIdTypeCode"></a> ParentIdTypeCode

**Description**: <br />
**DisplayName**: Parent Object Type<br />
**LogicalName**: parentidtypecode<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: EntityName<br />


### <a name="BKMK_PostalCode"></a> PostalCode

**Description**: ZIP Code or postal code in the publisher address.<br />
**DisplayName**: ZIP/Postal Code<br />
**LogicalName**: postalcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_PostOfficeBox"></a> PostOfficeBox

**Description**: Post office box number in the publisher address.<br />
**DisplayName**: Post Office Box<br />
**LogicalName**: postofficebox<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 20


### <a name="BKMK_PrimaryContactName"></a> PrimaryContactName

**Description**: Name of the primary contact at the publisher address.<br />
**DisplayName**: Address Contact<br />
**LogicalName**: primarycontactname<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 150


### <a name="BKMK_PublisherAddressId"></a> PublisherAddressId

**Description**: Unique identifier of the publisher address.<br />
**DisplayName**: Address<br />
**LogicalName**: publisheraddressid<br />
**IsValidForForm**: False<br />
**IsValidForRead**: True<br />
**RequiredLevel**: SystemRequired<br />
**IsValidForUpdate**: False<br />
**Type**: Uniqueidentifier<br />


### <a name="BKMK_ShippingMethodCode"></a> ShippingMethodCode

**Description**: Method of shipment for the publisher address.<br />
**DisplayName**: Shipping Method<br />
**LogicalName**: shippingmethodcode<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Picklist<br />
**Options**:

- **Value**: 1 **Label**: Default



### <a name="BKMK_StateOrProvince"></a> StateOrProvince

**Description**: State or province in the publisher address.<br />
**DisplayName**: State/Province<br />
**LogicalName**: stateorprovince<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Telephone1"></a> Telephone1

**Description**: First telephone number for the publisher address.<br />
**DisplayName**: Main Phone<br />
**LogicalName**: telephone1<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Telephone2"></a> Telephone2

**Description**: Second telephone number for the publisher address.<br />
**DisplayName**: Phone 2<br />
**LogicalName**: telephone2<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


### <a name="BKMK_Telephone3"></a> Telephone3

**Description**: Third telephone number for the publisher address.<br />
**DisplayName**: Telephone 3<br />
**LogicalName**: telephone3<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 50


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


### <a name="BKMK_UPSZone"></a> UPSZone

**Description**: United Parcel Service (UPS) zone for the address of the publisher.<br />
**DisplayName**: UPS Zone<br />
**LogicalName**: upszone<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: String<br />
**FormatName**: Text<br />
**IsLocalizable**: False<br />
**MaxLength**: 4


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


### <a name="BKMK_UTCOffset"></a> UTCOffset

**Description**: UTC offset for the address. This is the difference between local time and standard Coordinated Universal Time.<br />
**DisplayName**: UTC Offset<br />
**LogicalName**: utcoffset<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: Integer<br />
**Format**: TimeZone<br />
**MaxValue**: 1500<br />
**MinValue**: -1500

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
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedByName](#BKMK_ModifiedByName)
- [ModifiedByYomiName](#BKMK_ModifiedByYomiName)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [ModifiedOnBehalfByName](#BKMK_ModifiedOnBehalfByName)
- [ModifiedOnBehalfByYomiName](#BKMK_ModifiedOnBehalfByYomiName)
- [VersionNumber](#BKMK_VersionNumber)


### <a name="BKMK_CreatedBy"></a> CreatedBy

**Description**: Unique identifier of the user who created the publisher address.<br />
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

**Description**: Date and time when the publisher address was created.<br />
**DisplayName**: Created On<br />
**LogicalName**: createdon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_CreatedOnBehalfBy"></a> CreatedOnBehalfBy

**Description**: Unique identifier of the delegate user who created the publisher address.<br />
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


### <a name="BKMK_ModifiedBy"></a> ModifiedBy

**Description**: Unique identifier of the user who last modified the publisher address.<br />
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

**Description**: Date and time when the publisher address was last modified.<br />
**DisplayName**: Modified On<br />
**LogicalName**: modifiedon<br />
**IsValidForForm**: True<br />
**IsValidForRead**: True<br />
**RequiredLevel**: None<br />
**Type**: DateTime<br />
**DateTimeBehavior**: UserLocal<br />
**Format**: DateAndTime


### <a name="BKMK_ModifiedOnBehalfBy"></a> ModifiedOnBehalfBy

**Description**: Unique identifier of the delegate user who modified the publisher address.<br />
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


### <a name="BKMK_userentityinstancedata_publisheraddress"></a> userentityinstancedata_publisheraddress

Same as userentityinstancedata entity [userentityinstancedata_publisheraddress](userentityinstancedata.md#BKMK_userentityinstancedata_publisheraddress) Many-To-One relationship.

**ReferencingEntity**: userentityinstancedata<br />
**ReferencingAttribute**: objectid<br />
**IsHierarchical**: False<br />
**IsCustomizable**: False<br />
**ReferencedEntityNavigationPropertyName**: userentityinstancedata_publisheraddress<br />
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

- [lk_publisheraddressbase_modifiedonbehalfby](#BKMK_lk_publisheraddressbase_modifiedonbehalfby)
- [lk_publisheraddressbase_createdonbehalfby](#BKMK_lk_publisheraddressbase_createdonbehalfby)
- [Publisher_PublisherAddress](#BKMK_Publisher_PublisherAddress)
- [lk_publisheraddressbase_createdby](#BKMK_lk_publisheraddressbase_createdby)
- [lk_publisheraddressbase_modifiedby](#BKMK_lk_publisheraddressbase_modifiedby)


### <a name="BKMK_lk_publisheraddressbase_modifiedonbehalfby"></a> lk_publisheraddressbase_modifiedonbehalfby

See systemuser Entity [lk_publisheraddressbase_modifiedonbehalfby](systemuser.md#BKMK_lk_publisheraddressbase_modifiedonbehalfby) One-To-Many relationship.

### <a name="BKMK_lk_publisheraddressbase_createdonbehalfby"></a> lk_publisheraddressbase_createdonbehalfby

See systemuser Entity [lk_publisheraddressbase_createdonbehalfby](systemuser.md#BKMK_lk_publisheraddressbase_createdonbehalfby) One-To-Many relationship.

### <a name="BKMK_Publisher_PublisherAddress"></a> Publisher_PublisherAddress

See publisher Entity [Publisher_PublisherAddress](publisher.md#BKMK_Publisher_PublisherAddress) One-To-Many relationship.

### <a name="BKMK_lk_publisheraddressbase_createdby"></a> lk_publisheraddressbase_createdby

See systemuser Entity [lk_publisheraddressbase_createdby](systemuser.md#BKMK_lk_publisheraddressbase_createdby) One-To-Many relationship.

### <a name="BKMK_lk_publisheraddressbase_modifiedby"></a> lk_publisheraddressbase_modifiedby

See systemuser Entity [lk_publisheraddressbase_modifiedby](systemuser.md#BKMK_lk_publisheraddressbase_modifiedby) One-To-Many relationship.
publisheraddress

