---
title: "Publisher table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Publisher table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Publisher table/entity reference (Microsoft Dataverse)

A publisher of a CRM solution.

## Messages

The following table lists the messages for the Publisher table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /publishers<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: False |`DELETE` /publishers(*publisherid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /publishers(*publisherid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: False |`GET` /publishers<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /publishers(*publisherid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /publishers(*publisherid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Publisher table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Publisher** |
| **DisplayCollectionName** | **Publishers** |
| **SchemaName** | `Publisher` |
| **CollectionSchemaName** | `Publishers` |
| **EntitySetName** | `publishers`|
| **LogicalName** | `publisher` |
| **LogicalCollectionName** | `publishers` |
| **PrimaryIdAttribute** | `publisherid` |
| **PrimaryNameAttribute** |`friendlyname` |
| **TableType** | `Standard` |
| **OwnershipType** | `OrganizationOwned` |

## Writable columns/attributes

These columns/attributes return true for either **IsValidForCreate** or **IsValidForUpdate** (usually both). Listed by **SchemaName**.

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
- [CustomizationOptionValuePrefix](#BKMK_CustomizationOptionValuePrefix)
- [CustomizationPrefix](#BKMK_CustomizationPrefix)
- [Description](#BKMK_Description)
- [EMailAddress](#BKMK_EMailAddress)
- [EntityImage](#BKMK_EntityImage)
- [FriendlyName](#BKMK_FriendlyName)
- [PublisherId](#BKMK_PublisherId)
- [SupportingWebsiteUrl](#BKMK_SupportingWebsiteUrl)
- [UniqueName](#BKMK_UniqueName)

### <a name="BKMK_Address1_AddressId"></a> Address1_AddressId

|Property|Value|
|---|---|
|Description|**Unique identifier for address 1.**|
|DisplayName|**Address 1: ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`address1_addressid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Address1_AddressTypeCode"></a> Address1_AddressTypeCode

|Property|Value|
|---|---|
|Description|**Type of address for address 1, such as billing, shipping, or primary address.**|
|DisplayName|**Address 1: Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`publisher_address1_addresstypecode`|

#### Address1_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address1_City"></a> Address1_City

|Property|Value|
|---|---|
|Description|**City name for address 1.**|
|DisplayName|**City**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_city`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Address1_Country"></a> Address1_Country

|Property|Value|
|---|---|
|Description|**Country/region name for address 1.**|
|DisplayName|**Country/Region**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_country`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Address1_County"></a> Address1_County

|Property|Value|
|---|---|
|Description|**County name for address 1.**|
|DisplayName|**Address 1: County**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_county`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Fax"></a> Address1_Fax

|Property|Value|
|---|---|
|Description|**Fax number for address 1.**|
|DisplayName|**Address 1: Fax**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_fax`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Latitude"></a> Address1_Latitude

|Property|Value|
|---|---|
|Description|**Latitude for address 1.**|
|DisplayName|**Address 1: Latitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_latitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|90|
|MinValue|-90|
|Precision|5|

### <a name="BKMK_Address1_Line1"></a> Address1_Line1

|Property|Value|
|---|---|
|Description|**First line for entering address 1 information.**|
|DisplayName|**Street 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_line1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Line2"></a> Address1_Line2

|Property|Value|
|---|---|
|Description|**Second line for entering address 1 information.**|
|DisplayName|**Street 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_line2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Line3"></a> Address1_Line3

|Property|Value|
|---|---|
|Description|**Third line for entering address 1 information.**|
|DisplayName|**Street 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_line3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Longitude"></a> Address1_Longitude

|Property|Value|
|---|---|
|Description|**Longitude for address 1.**|
|DisplayName|**Address 1: Longitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_longitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|180|
|MinValue|-180|
|Precision|5|

### <a name="BKMK_Address1_Name"></a> Address1_Name

|Property|Value|
|---|---|
|Description|**Name to enter for address 1.**|
|DisplayName|**Address 1: Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Address1_PostalCode"></a> Address1_PostalCode

|Property|Value|
|---|---|
|Description|**ZIP Code or postal code for address 1.**|
|DisplayName|**ZIP/Postal Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_postalcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_Address1_PostOfficeBox"></a> Address1_PostOfficeBox

|Property|Value|
|---|---|
|Description|**Post office box number for address 1.**|
|DisplayName|**Address 1: Post Office Box**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_postofficebox`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_Address1_ShippingMethodCode"></a> Address1_ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Method of shipment for address 1.**|
|DisplayName|**Address 1: Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`publisher_address1_shippingmethodcode`|

#### Address1_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

|Property|Value|
|---|---|
|Description|**State or province for address 1.**|
|DisplayName|**State/Province**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_stateorprovince`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Telephone1"></a> Address1_Telephone1

|Property|Value|
|---|---|
|Description|**First telephone number associated with address 1.**|
|DisplayName|**Phone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Telephone2"></a> Address1_Telephone2

|Property|Value|
|---|---|
|Description|**Second telephone number associated with address 1.**|
|DisplayName|**Address 1: Telephone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_Telephone3"></a> Address1_Telephone3

|Property|Value|
|---|---|
|Description|**Third telephone number associated with address 1.**|
|DisplayName|**Address 1: Telephone 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address1_UPSZone"></a> Address1_UPSZone

|Property|Value|
|---|---|
|Description|**United Parcel Service (UPS) zone for address 1.**|
|DisplayName|**Address 1: UPS Zone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_upszone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4|

### <a name="BKMK_Address1_UTCOffset"></a> Address1_UTCOffset

|Property|Value|
|---|---|
|Description|**UTC offset for address 1. This is the difference between local time and standard Coordinated Universal Time.**|
|DisplayName|**Address 1: UTC Offset**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_utcoffset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_Address2_AddressId"></a> Address2_AddressId

|Property|Value|
|---|---|
|Description|**Unique identifier for address 2.**|
|DisplayName|**Address 2: ID**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`address2_addressid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_Address2_AddressTypeCode"></a> Address2_AddressTypeCode

|Property|Value|
|---|---|
|Description|**Type of address for address 2. such as billing, shipping, or primary address.**|
|DisplayName|**Address 2: Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`publisher_address2_addresstypecode`|

#### Address2_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_City"></a> Address2_City

|Property|Value|
|---|---|
|Description|**City name for address 2.**|
|DisplayName|**Address 2: City**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_city`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Address2_Country"></a> Address2_Country

|Property|Value|
|---|---|
|Description|**Country/region name for address 2.**|
|DisplayName|**Address 2: Country/Region**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_country`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_Address2_County"></a> Address2_County

|Property|Value|
|---|---|
|Description|**County name for address 2.**|
|DisplayName|**Address 2: County**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_county`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Fax"></a> Address2_Fax

|Property|Value|
|---|---|
|Description|**Fax number for address 2.**|
|DisplayName|**Address 2: Fax**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_fax`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Latitude"></a> Address2_Latitude

|Property|Value|
|---|---|
|Description|**Latitude for address 2.**|
|DisplayName|**Address 2: Latitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_latitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|90|
|MinValue|-90|
|Precision|5|

### <a name="BKMK_Address2_Line1"></a> Address2_Line1

|Property|Value|
|---|---|
|Description|**First line for entering address 2 information.**|
|DisplayName|**Address 2: Street 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_line1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Line2"></a> Address2_Line2

|Property|Value|
|---|---|
|Description|**Second line for entering address 2 information.**|
|DisplayName|**Address 2: Street 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_line2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Line3"></a> Address2_Line3

|Property|Value|
|---|---|
|Description|**Third line for entering address 2 information.**|
|DisplayName|**Address 2: Street 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_line3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Longitude"></a> Address2_Longitude

|Property|Value|
|---|---|
|Description|**Longitude for address 2.**|
|DisplayName|**Address 2: Longitude**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_longitude`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|180|
|MinValue|-180|
|Precision|5|

### <a name="BKMK_Address2_Name"></a> Address2_Name

|Property|Value|
|---|---|
|Description|**Name to enter for address 2.**|
|DisplayName|**Address 2: Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_name`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_Address2_PostalCode"></a> Address2_PostalCode

|Property|Value|
|---|---|
|Description|**ZIP Code or postal code for address 2.**|
|DisplayName|**Address 2: ZIP/Postal Code**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_postalcode`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_Address2_PostOfficeBox"></a> Address2_PostOfficeBox

|Property|Value|
|---|---|
|Description|**Post office box number for address 2.**|
|DisplayName|**Address 2: Post Office Box**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_postofficebox`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_Address2_ShippingMethodCode"></a> Address2_ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Method of shipment for address 2.**|
|DisplayName|**Address 2: Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`publisher_address2_shippingmethodcode`|

#### Address2_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

|Property|Value|
|---|---|
|Description|**State or province for address 2.**|
|DisplayName|**Address 2: State/Province**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_stateorprovince`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Telephone1"></a> Address2_Telephone1

|Property|Value|
|---|---|
|Description|**First telephone number associated with address 2.**|
|DisplayName|**Address 2: Telephone 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_telephone1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Telephone2"></a> Address2_Telephone2

|Property|Value|
|---|---|
|Description|**Second telephone number associated with address 2.**|
|DisplayName|**Address 2: Telephone 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_telephone2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_Telephone3"></a> Address2_Telephone3

|Property|Value|
|---|---|
|Description|**Third telephone number associated with address 2.**|
|DisplayName|**Address 2: Telephone 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_telephone3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|50|

### <a name="BKMK_Address2_UPSZone"></a> Address2_UPSZone

|Property|Value|
|---|---|
|Description|**United Parcel Service (UPS) zone for address 2.**|
|DisplayName|**Address 2: UPS Zone**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_upszone`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|4|

### <a name="BKMK_Address2_UTCOffset"></a> Address2_UTCOffset

|Property|Value|
|---|---|
|Description|**UTC offset for address 2. This is the difference between local time and standard Coordinated Universal Time.**|
|DisplayName|**Address 2: UTC Offset**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_utcoffset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_CustomizationOptionValuePrefix"></a> CustomizationOptionValuePrefix

|Property|Value|
|---|---|
|Description|**Default option value prefix used for newly created options for solutions associated with this publisher.**|
|DisplayName|**Option Value Prefix**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`customizationoptionvalueprefix`|
|RequiredLevel|SystemRequired|
|Type|Integer|
|MaxValue|99999|
|MinValue|10000|

### <a name="BKMK_CustomizationPrefix"></a> CustomizationPrefix

|Property|Value|
|---|---|
|Description|**Prefix used for new entities, attributes, and entity relationships for solutions associated with this publisher.**|
|DisplayName|**Prefix**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`customizationprefix`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|8|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the solution.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|String|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|2000|

### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|---|---|
|Description|**Email address for the publisher.**|
|DisplayName|**Email**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`emailaddress`|
|RequiredLevel|None|
|Type|String|
|Format|Email|
|FormatName|Email|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EntityImage"></a> EntityImage

|Property|Value|
|---|---|
|Description|**Shows the default image for the record.**|
|DisplayName|**Entity Image**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage`|
|RequiredLevel|None|
|Type|Image|
|CanStoreFullImage|False|
|IsPrimaryImage|True|
|MaxHeight|144|
|MaxSizeInKB|10240|
|MaxWidth|144|

### <a name="BKMK_FriendlyName"></a> FriendlyName

|Property|Value|
|---|---|
|Description|**User display name for this publisher.**|
|DisplayName|**Display Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`friendlyname`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|True|
|MaxLength|256|

### <a name="BKMK_PublisherId"></a> PublisherId

|Property|Value|
|---|---|
|Description|**Unique identifier of the publisher.**|
|DisplayName|**Publisher Identifier**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publisherid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_SupportingWebsiteUrl"></a> SupportingWebsiteUrl

|Property|Value|
|---|---|
|Description|**URL for the supporting website of this publisher.**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`supportingwebsiteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_UniqueName"></a> UniqueName

|Property|Value|
|---|---|
|Description|**The unique name of this publisher.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`uniquename`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|256|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [EntityImage_Timestamp](#BKMK_EntityImage_Timestamp)
- [EntityImage_URL](#BKMK_EntityImage_URL)
- [EntityImageId](#BKMK_EntityImageId)
- [IsReadonly](#BKMK_IsReadonly)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [PinpointPublisherDefaultLocale](#BKMK_PinpointPublisherDefaultLocale)
- [PinpointPublisherId](#BKMK_PinpointPublisherId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the publisher.**|
|DisplayName|**Created By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`createdby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_CreatedOn"></a> CreatedOn

|Property|Value|
|---|---|
|Description|**Date and time when the publisher was created.**|
|DisplayName|**Created On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who created the publisher.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_EntityImage_Timestamp"></a> EntityImage_Timestamp

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_timestamp`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_EntityImage_URL"></a> EntityImage_URL

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimage_url`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Disabled|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_EntityImageId"></a> EntityImageId

|Property|Value|
|---|---|
|Description|**For internal use only.**|
|DisplayName|**Entity Image Id**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`entityimageid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_IsReadonly"></a> IsReadonly

|Property|Value|
|---|---|
|Description|**Indicates whether the publisher was created as part of a managed solution installation.**|
|DisplayName|**Is Read-Only Publisher**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`isreadonly`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`publisher_isreadonly`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the publisher.**|
|DisplayName|**Modified By**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`modifiedby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedOn"></a> ModifiedOn

|Property|Value|
|---|---|
|Description|**Date and time when the publisher was last modified.**|
|DisplayName|**Modified On**|
|IsValidForForm|False|
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
|Description|**Unique identifier of the delegate user who modified the publisher.**|
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
|Description|**Unique identifier of the organization associated with the publisher.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_PinpointPublisherDefaultLocale"></a> PinpointPublisherDefaultLocale

|Property|Value|
|---|---|
|Description|**Default locale of the publisher in Microsoft Pinpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointpublisherdefaultlocale`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|16|

### <a name="BKMK_PinpointPublisherId"></a> PinpointPublisherId

|Property|Value|
|---|---|
|Description|**Identifier of the publisher in Microsoft Pinpoint.**|
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`pinpointpublisherid`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [lk_publisher_createdby](#BKMK_lk_publisher_createdby)
- [lk_publisher_modifiedby](#BKMK_lk_publisher_modifiedby)
- [lk_publisherbase_createdonbehalfby](#BKMK_lk_publisherbase_createdonbehalfby)
- [lk_publisherbase_modifiedonbehalfby](#BKMK_lk_publisherbase_modifiedonbehalfby)
- [organization_publisher](#BKMK_organization_publisher)

### <a name="BKMK_lk_publisher_createdby"></a> lk_publisher_createdby

One-To-Many Relationship: [systemuser lk_publisher_createdby](systemuser.md#BKMK_lk_publisher_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_publisher_modifiedby"></a> lk_publisher_modifiedby

One-To-Many Relationship: [systemuser lk_publisher_modifiedby](systemuser.md#BKMK_lk_publisher_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_publisherbase_createdonbehalfby"></a> lk_publisherbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_publisherbase_createdonbehalfby](systemuser.md#BKMK_lk_publisherbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_publisherbase_modifiedonbehalfby"></a> lk_publisherbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_publisherbase_modifiedonbehalfby](systemuser.md#BKMK_lk_publisherbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_publisher"></a> organization_publisher

One-To-Many Relationship: [organization organization_publisher](organization.md#BKMK_organization_publisher)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|


## One-to-Many relationships

These relationships are one-to-many. Listed by **SchemaName**.

- [publisher_appmodule](#BKMK_publisher_appmodule)
- [Publisher_DuplicateBaseRecord](#BKMK_Publisher_DuplicateBaseRecord)
- [Publisher_DuplicateMatchingRecord](#BKMK_Publisher_DuplicateMatchingRecord)
- [Publisher_PublisherAddress](#BKMK_Publisher_PublisherAddress)
- [publisher_solution](#BKMK_publisher_solution)
- [Publisher_SyncErrors](#BKMK_Publisher_SyncErrors)

### <a name="BKMK_publisher_appmodule"></a> publisher_appmodule

Many-To-One Relationship: [appmodule publisher_appmodule](appmodule.md#BKMK_publisher_appmodule)

|Property|Value|
|---|---|
|ReferencingEntity|`appmodule`|
|ReferencingAttribute|`publisherid`|
|ReferencedEntityNavigationPropertyName|`publisher_appmodule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Publisher_DuplicateBaseRecord"></a> Publisher_DuplicateBaseRecord

Many-To-One Relationship: [duplicaterecord Publisher_DuplicateBaseRecord](duplicaterecord.md#BKMK_Publisher_DuplicateBaseRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`baserecordid`|
|ReferencedEntityNavigationPropertyName|`Publisher_DuplicateBaseRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Publisher_DuplicateMatchingRecord"></a> Publisher_DuplicateMatchingRecord

Many-To-One Relationship: [duplicaterecord Publisher_DuplicateMatchingRecord](duplicaterecord.md#BKMK_Publisher_DuplicateMatchingRecord)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterecord`|
|ReferencingAttribute|`duplicaterecordid`|
|ReferencedEntityNavigationPropertyName|`Publisher_DuplicateMatchingRecord`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Publisher_PublisherAddress"></a> Publisher_PublisherAddress

Many-To-One Relationship: [publisheraddress Publisher_PublisherAddress](publisheraddress.md#BKMK_Publisher_PublisherAddress)

|Property|Value|
|---|---|
|ReferencingEntity|`publisheraddress`|
|ReferencingAttribute|`parentid`|
|ReferencedEntityNavigationPropertyName|`Publisher_PublisherAddress`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_publisher_solution"></a> publisher_solution

Many-To-One Relationship: [solution publisher_solution](solution.md#BKMK_publisher_solution)

|Property|Value|
|---|---|
|ReferencingEntity|`solution`|
|ReferencingAttribute|`publisherid`|
|ReferencedEntityNavigationPropertyName|`publisher_solution`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Publisher_SyncErrors"></a> Publisher_SyncErrors

Many-To-One Relationship: [syncerror Publisher_SyncErrors](syncerror.md#BKMK_Publisher_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`Publisher_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.publisher?displayProperty=fullName>
