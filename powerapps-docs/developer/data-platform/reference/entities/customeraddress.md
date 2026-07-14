---
title: "Address (CustomerAddress) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Address (CustomerAddress) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Address (CustomerAddress) table/entity reference (Microsoft Dataverse)

Address and shipping information. Used to store additional addresses for an account or contact.

## Messages

The following table lists the messages for the Address (CustomerAddress) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /customeraddresses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /customeraddresses(*customeraddressid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /customeraddresses(*customeraddressid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /customeraddresses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: True |`PATCH` /customeraddresses(*customeraddressid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /customeraddresses(*customeraddressid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Address (CustomerAddress) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Address** |
| **DisplayCollectionName** | **Addresses** |
| **SchemaName** | `CustomerAddress` |
| **CollectionSchemaName** | `CustomerAddresses` |
| **EntitySetName** | `customeraddresses`|
| **LogicalName** | `customeraddress` |
| **LogicalCollectionName** | `customeraddresses` |
| **PrimaryIdAttribute** | `customeraddressid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `None` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

- [AddressNumber](#BKMK_AddressNumber)
- [AddressTypeCode](#BKMK_AddressTypeCode)
- [City](#BKMK_City)
- [Country](#BKMK_Country)
- [County](#BKMK_County)
- [CustomerAddressId](#BKMK_CustomerAddressId)
- [Fax](#BKMK_Fax)
- [FreightTermsCode](#BKMK_FreightTermsCode)
- [ImportSequenceNumber](#BKMK_ImportSequenceNumber)
- [Latitude](#BKMK_Latitude)
- [Line1](#BKMK_Line1)
- [Line2](#BKMK_Line2)
- [Line3](#BKMK_Line3)
- [Longitude](#BKMK_Longitude)
- [Name](#BKMK_Name)
- [ObjectTypeCode](#BKMK_ObjectTypeCode)
- [OverriddenCreatedOn](#BKMK_OverriddenCreatedOn)
- [ParentId](#BKMK_ParentId)
- [ParentIdTypeCode](#BKMK_ParentIdTypeCode)
- [PostalCode](#BKMK_PostalCode)
- [PostOfficeBox](#BKMK_PostOfficeBox)
- [PrimaryContactName](#BKMK_PrimaryContactName)
- [ShippingMethodCode](#BKMK_ShippingMethodCode)
- [StateOrProvince](#BKMK_StateOrProvince)
- [Telephone1](#BKMK_Telephone1)
- [Telephone2](#BKMK_Telephone2)
- [Telephone3](#BKMK_Telephone3)
- [TimeZoneRuleVersionNumber](#BKMK_TimeZoneRuleVersionNumber)
- [TransactionCurrencyId](#BKMK_TransactionCurrencyId)
- [UPSZone](#BKMK_UPSZone)
- [UTCConversionTimeZoneCode](#BKMK_UTCConversionTimeZoneCode)
- [UTCOffset](#BKMK_UTCOffset)

### <a name="BKMK_AddressNumber"></a> AddressNumber

|Property|Value|
|---|---|
|Description|**Shows the number of the address, to indicate whether the address is the primary, secondary, or other address for the customer.**|
|DisplayName|**Address Number**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`addressnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_AddressTypeCode"></a> AddressTypeCode

|Property|Value|
|---|---|
|Description|**Select the address type, such as primary or billing.**|
|DisplayName|**Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`customeraddress_addresstypecode`|

#### AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Bill To**|
|2|**Ship To**|
|3|**Primary**|
|4|**Other**|

### <a name="BKMK_City"></a> City

|Property|Value|
|---|---|
|Description|**Type the city for the customer's address to help identify the location.**|
|DisplayName|**City**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`city`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Country"></a> Country

|Property|Value|
|---|---|
|Description|**Type the country or region for the customer's address.**|
|DisplayName|**Country/Region**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`country`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_County"></a> County

|Property|Value|
|---|---|
|Description|**Type the county for the customer's address.**|
|DisplayName|**County**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`county`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_CustomerAddressId"></a> CustomerAddressId

|Property|Value|
|---|---|
|Description|**Unique identifier of the customer address.**|
|DisplayName|**Address**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customeraddressid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_Fax"></a> Fax

|Property|Value|
|---|---|
|Description|**Type the fax number associated with the customer's address.**|
|DisplayName|**Fax**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fax`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_FreightTermsCode"></a> FreightTermsCode

|Property|Value|
|---|---|
|Description|**Select the freight terms to make sure shipping charges are processed correctly.**|
|DisplayName|**Freight Terms**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`freighttermscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`customeraddress_freighttermscode`|

#### FreightTermsCode Choices/Options

|Value|Label|
|---|---|
|1|**FOB**|
|2|**No Charge**|

### <a name="BKMK_ImportSequenceNumber"></a> ImportSequenceNumber

|Property|Value|
|---|---|
|Description|**Unique identifier of the data import or data migration that created this record.**|
|DisplayName|**Import Sequence Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`importsequencenumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-2147483648|

### <a name="BKMK_Latitude"></a> Latitude

|Property|Value|
|---|---|
|Description|**Type the latitude value for the customer's address, for use in mapping and other applications.**|
|DisplayName|**Latitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`latitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|90|
|MinValue|-90|
|Precision|5|

### <a name="BKMK_Line1"></a> Line1

|Property|Value|
|---|---|
|Description|**Type the first line of the customer's address to help identify the location.**|
|DisplayName|**Street 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`line1`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Line2"></a> Line2

|Property|Value|
|---|---|
|Description|**Type the second line of the customer's address.**|
|DisplayName|**Street 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`line2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Line3"></a> Line3

|Property|Value|
|---|---|
|Description|**Type the third line of the customer's address.**|
|DisplayName|**Street 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`line3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Longitude"></a> Longitude

|Property|Value|
|---|---|
|Description|**Type the longitude value for the customer's address, for use in mapping and other applications.**|
|DisplayName|**Longitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`longitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|180|
|MinValue|-180|
|Precision|5|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Type a descriptive name for the customer's address, such as Corporate Headquarters.**|
|DisplayName|**Address Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|ApplicationRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_ObjectTypeCode"></a> ObjectTypeCode

|Property|Value|
|---|---|
|Description|**Shows the type code of the customer record to indicate whether the address belongs to a customer account or contact.**|
|DisplayName|**Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`objecttypecode`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OverriddenCreatedOn"></a> OverriddenCreatedOn

|Property|Value|
|---|---|
|Description|**Date and time that the record was migrated.**|
|DisplayName|**Record Created On**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`overriddencreatedon`|
|RequiredLevel|None|
|Type|DateTime|
|CanChangeDateTimeBehavior|False|
|DateTimeBehavior|UserLocal|
|Format|DateOnly|
|ImeMode|Inactive|
|SourceTypeMask|0|

### <a name="BKMK_ParentId"></a> ParentId

|Property|Value|
|---|---|
|Description|**Choose the customer's address.**|
|DisplayName|**Parent**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|account, contact|

### <a name="BKMK_ParentIdTypeCode"></a> ParentIdTypeCode

|Property|Value|
|---|---|
|Description||
|DisplayName|**Parent Object Type**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`parentidtypecode`|
|RequiredLevel|None|
|Type|EntityName|

### <a name="BKMK_PostalCode"></a> PostalCode

|Property|Value|
|---|---|
|Description|**Type the ZIP Code or postal code for the address.**|
|DisplayName|**ZIP/Postal Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postalcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_PostOfficeBox"></a> PostOfficeBox

|Property|Value|
|---|---|
|Description|**Type the post office box number of the customer's address.**|
|DisplayName|**Post Office Box**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`postofficebox`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_PrimaryContactName"></a> PrimaryContactName

|Property|Value|
|---|---|
|Description|**Type the name of the primary contact person for the customer's address.**|
|DisplayName|**Address Contact**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`primarycontactname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|150|

### <a name="BKMK_ShippingMethodCode"></a> ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Select a shipping method for deliveries sent to this address.**|
|DisplayName|**Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`customeraddress_shippingmethodcode`|

#### ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Airborne**|
|2|**DHL**|
|3|**FedEx**|
|4|**UPS**|
|5|**Postal Mail**|
|6|**Full Load**|
|7|**Will Call**|

### <a name="BKMK_StateOrProvince"></a> StateOrProvince

|Property|Value|
|---|---|
|Description|**Type the state or province of the customer's address.**|
|DisplayName|**State/Province**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stateorprovince`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Telephone1"></a> Telephone1

|Property|Value|
|---|---|
|Description|**Type the primary phone number for the customer's address.**|
|DisplayName|**Main Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Telephone2"></a> Telephone2

|Property|Value|
|---|---|
|Description|**Type a second phone number for the customer's address.**|
|DisplayName|**Phone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Telephone3"></a> Telephone3

|Property|Value|
|---|---|
|Description|**Type a third phone number for the customer's address.**|
|DisplayName|**Telephone 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_TimeZoneRuleVersionNumber"></a> TimeZoneRuleVersionNumber

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Time Zone Rule Version Number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`timezoneruleversionnumber`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Choose the local currency for the record to make sure budgets are reported in the correct currency.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_UPSZone"></a> UPSZone

|Property|Value|
|---|---|
|Description|**Type the UPS zone of the customer's address to make sure shipping charges are calculated correctly and deliveries are made promptly, if shipped by UPS.**|
|DisplayName|**UPS Zone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`upszone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4|

### <a name="BKMK_UTCConversionTimeZoneCode"></a> UTCConversionTimeZoneCode

|Property|Value|
|---|---|
|Description|**Time zone code that was in use when the record was created.**|
|DisplayName|**UTC Conversion Time Zone Code**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`utcconversiontimezonecode`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|2147483647|
|MinValue|-1|

### <a name="BKMK_UTCOffset"></a> UTCOffset

|Property|Value|
|---|---|
|Description|**Select the time zone for the address.**|
|DisplayName|**UTC Offset**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`utcoffset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [Composite](#BKMK_Composite)
- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OwnerId](#BKMK_OwnerId)
- [OwnerIdType](#BKMK_OwnerIdType)
- [OwningBusinessUnit](#BKMK_OwningBusinessUnit)
- [OwningUser](#BKMK_OwningUser)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_Composite"></a> Composite

|Property|Value|
|---|---|
|Description|**Shows the complete address.**|
|DisplayName|**Address**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`composite`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1000|

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

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Shows the conversion rate of the record's currency. The exchange rate is used to convert all money fields in the record from the local currency to the system's default currency.**|
|DisplayName|**Exchange Rate**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`exchangerate`|
|RequiredLevel|None|
|Type|Decimal|
|ImeMode|Disabled|
|MaxValue|100000000000|
|MinValue|1E-12|
|Precision|12|
|SourceTypeMask|0|

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
|Description|**Shows who last updated the record on behalf of another user.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_OwnerId"></a> OwnerId

|Property|Value|
|---|---|
|Description|**Enter the user or team who is assigned to manage the record. This field is updated every time the record is assigned to a different user.**|
|DisplayName|**Owner**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ownerid`|
|RequiredLevel|ApplicationRequired|
|Type|Owner|
|Targets|systemuser, team|

### <a name="BKMK_OwnerIdType"></a> OwnerIdType

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owneridtype`|
|RequiredLevel|SystemRequired|
|Type|EntityName|

### <a name="BKMK_OwningBusinessUnit"></a> OwningBusinessUnit

|Property|Value|
|---|---|
|Description|**Shows the business unit that the record owner belongs to.**|
|DisplayName|**Owning Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owningbusinessunit`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_OwningUser"></a> OwningUser

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who owns the customer address.**|
|DisplayName|**Owner**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`owninguser`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the customer address.**|
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

- [Account_CustomerAddress](#BKMK_Account_CustomerAddress)
- [Contact_CustomerAddress](#BKMK_Contact_CustomerAddress)
- [lk_customeraddress_createdonbehalfby](#BKMK_lk_customeraddress_createdonbehalfby)
- [lk_customeraddress_modifiedonbehalfby](#BKMK_lk_customeraddress_modifiedonbehalfby)
- [lk_customeraddressbase_createdby](#BKMK_lk_customeraddressbase_createdby)
- [lk_customeraddressbase_modifiedby](#BKMK_lk_customeraddressbase_modifiedby)
- [TransactionCurrency_CustomerAddress](#BKMK_TransactionCurrency_CustomerAddress)

### <a name="BKMK_Account_CustomerAddress"></a> Account_CustomerAddress

One-To-Many Relationship: [account Account_CustomerAddress](account.md#BKMK_Account_CustomerAddress)

|Property|Value|
|---|---|
|ReferencedEntity|`account`|
|ReferencedAttribute|`accountid`|
|ReferencingAttribute|`parentid`|
|ReferencingEntityNavigationPropertyName|`parentid_account`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Contact_CustomerAddress"></a> Contact_CustomerAddress

One-To-Many Relationship: [contact Contact_CustomerAddress](contact.md#BKMK_Contact_CustomerAddress)

|Property|Value|
|---|---|
|ReferencedEntity|`contact`|
|ReferencedAttribute|`contactid`|
|ReferencingAttribute|`parentid`|
|ReferencingEntityNavigationPropertyName|`parentid_contact`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customeraddress_createdonbehalfby"></a> lk_customeraddress_createdonbehalfby

One-To-Many Relationship: [systemuser lk_customeraddress_createdonbehalfby](systemuser.md#BKMK_lk_customeraddress_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customeraddress_modifiedonbehalfby"></a> lk_customeraddress_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_customeraddress_modifiedonbehalfby](systemuser.md#BKMK_lk_customeraddress_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customeraddressbase_createdby"></a> lk_customeraddressbase_createdby

One-To-Many Relationship: [systemuser lk_customeraddressbase_createdby](systemuser.md#BKMK_lk_customeraddressbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_customeraddressbase_modifiedby"></a> lk_customeraddressbase_modifiedby

One-To-Many Relationship: [systemuser lk_customeraddressbase_modifiedby](systemuser.md#BKMK_lk_customeraddressbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_CustomerAddress"></a> TransactionCurrency_CustomerAddress

One-To-Many Relationship: [transactioncurrency TransactionCurrency_CustomerAddress](transactioncurrency.md#BKMK_TransactionCurrency_CustomerAddress)

|Property|Value|
|---|---|
|ReferencedEntity|`transactioncurrency`|
|ReferencedAttribute|`transactioncurrencyid`|
|ReferencingAttribute|`transactioncurrencyid`|
|ReferencingEntityNavigationPropertyName|`transactioncurrencyid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [CustomerAddress_AsyncOperations](#BKMK_CustomerAddress_AsyncOperations)
- [CustomerAddress_BulkDeleteFailures](#BKMK_CustomerAddress_BulkDeleteFailures)
- [customeraddress_principalobjectattributeaccess](#BKMK_customeraddress_principalobjectattributeaccess)
- [CustomerAddress_ProcessSessions](#BKMK_CustomerAddress_ProcessSessions)
- [CustomerAddress_SyncErrors](#BKMK_CustomerAddress_SyncErrors)

### <a name="BKMK_CustomerAddress_AsyncOperations"></a> CustomerAddress_AsyncOperations

Many-To-One Relationship: [asyncoperation CustomerAddress_AsyncOperations](asyncoperation.md#BKMK_CustomerAddress_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`CustomerAddress_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_CustomerAddress_BulkDeleteFailures"></a> CustomerAddress_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure CustomerAddress_BulkDeleteFailures](bulkdeletefailure.md#BKMK_CustomerAddress_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`CustomerAddress_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_customeraddress_principalobjectattributeaccess"></a> customeraddress_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess customeraddress_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_customeraddress_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`customeraddress_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_CustomerAddress_ProcessSessions"></a> CustomerAddress_ProcessSessions

Many-To-One Relationship: [processsession CustomerAddress_ProcessSessions](processsession.md#BKMK_CustomerAddress_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`CustomerAddress_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_CustomerAddress_SyncErrors"></a> CustomerAddress_SyncErrors

Many-To-One Relationship: [syncerror CustomerAddress_SyncErrors](syncerror.md#BKMK_CustomerAddress_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`CustomerAddress_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.customeraddress?displayProperty=fullName>
