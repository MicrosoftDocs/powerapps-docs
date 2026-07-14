---
title: "Publisher Address (PublisherAddress) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Publisher Address (PublisherAddress) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Publisher Address (PublisherAddress) table/entity reference (Microsoft Dataverse)

Address and shipping information. Used to store additional addresses for a publisher.

## Messages

The following table lists the messages for the Publisher Address (PublisherAddress) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: False |`POST` /publisheraddresses<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /publisheraddresses(*publisheraddressid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: True |`GET` /publisheraddresses(*publisheraddressid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveMultiple`<br />Event: True |`GET` /publisheraddresses<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `Update`<br />Event: False |`PATCH` /publisheraddresses(*publisheraddressid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /publisheraddresses(*publisheraddressid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Publisher Address (PublisherAddress) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Publisher Address** |
| **DisplayCollectionName** | **Publisher Addresses** |
| **SchemaName** | `PublisherAddress` |
| **CollectionSchemaName** | `PublisherAddresses` |
| **EntitySetName** | `publisheraddresses`|
| **LogicalName** | `publisheraddress` |
| **LogicalCollectionName** | `publisheraddresses` |
| **PrimaryIdAttribute** | `publisheraddressid` |
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

|Property|Value|
|---|---|
|Description|**Specifies which publisher address is applicable.**|
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
|Description|**Type of address for the publisher, such as billing, shipping, or primary address.**|
|DisplayName|**Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`publisheraddress_addresstypecode`|

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
|Description|**City name in the publisher address.**|
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
|Description|**Country/region name in the publisher address.**|
|DisplayName|**Country**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`country`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|80|

### <a name="BKMK_County"></a> County

|Property|Value|
|---|---|
|Description|**County name in the publisher address.**|
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

### <a name="BKMK_Fax"></a> Fax

|Property|Value|
|---|---|
|Description|**Fax number for the publisher address.**|
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
|Description|**Freight terms for the publisher address.**|
|DisplayName|**Freight Terms**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`freighttermscode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`publisheraddress_freighttermscode`|

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
|Description|**Latitude for the publisher address.**|
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
|Description|**First line for entering address information.**|
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
|MaxLength|50|

### <a name="BKMK_Line2"></a> Line2

|Property|Value|
|---|---|
|Description|**Second line for entering address information.**|
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
|MaxLength|50|

### <a name="BKMK_Line3"></a> Line3

|Property|Value|
|---|---|
|Description|**Third line for entering address information.**|
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
|MaxLength|50|

### <a name="BKMK_Longitude"></a> Longitude

|Property|Value|
|---|---|
|Description|**Longitude for the publisher address.**|
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
|Description|**Name used to identify the publisher address.**|
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

### <a name="BKMK_ParentId"></a> ParentId

|Property|Value|
|---|---|
|Description|**Unique identifier of the parent object with which the publisher address is associated.**|
|DisplayName|**Parent**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|publisher|

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
|Description|**ZIP Code or postal code in the publisher address.**|
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
|Description|**Post office box number in the publisher address.**|
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
|Description|**Name of the primary contact at the publisher address.**|
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

### <a name="BKMK_PublisherAddressId"></a> PublisherAddressId

|Property|Value|
|---|---|
|Description|**Unique identifier of the publisher address.**|
|DisplayName|**Address**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`publisheraddressid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_ShippingMethodCode"></a> ShippingMethodCode

|Property|Value|
|---|---|
|Description|**Method of shipment for the publisher address.**|
|DisplayName|**Shipping Method**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`shippingmethodcode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|-1|
|GlobalChoiceName|`publisheraddress_shippingmethodcode`|

#### ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default**|

### <a name="BKMK_StateOrProvince"></a> StateOrProvince

|Property|Value|
|---|---|
|Description|**State or province in the publisher address.**|
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
|Description|**First telephone number for the publisher address.**|
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
|Description|**Second telephone number for the publisher address.**|
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
|Description|**Third telephone number for the publisher address.**|
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

### <a name="BKMK_UPSZone"></a> UPSZone

|Property|Value|
|---|---|
|Description|**United Parcel Service (UPS) zone for the address of the publisher.**|
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
|Description|**UTC offset for the address. This is the difference between local time and standard Coordinated Universal Time.**|
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

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the publisher address.**|
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
|Description|**Date and time when the publisher address was created.**|
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
|Description|**Unique identifier of the delegate user who created the publisher address.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_ModifiedBy"></a> ModifiedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who last modified the publisher address.**|
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
|Description|**Date and time when the publisher address was last modified.**|
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
|Description|**Unique identifier of the delegate user who modified the publisher address.**|
|DisplayName|**Modified By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`modifiedonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

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

- [lk_publisheraddressbase_createdby](#BKMK_lk_publisheraddressbase_createdby)
- [lk_publisheraddressbase_createdonbehalfby](#BKMK_lk_publisheraddressbase_createdonbehalfby)
- [lk_publisheraddressbase_modifiedby](#BKMK_lk_publisheraddressbase_modifiedby)
- [lk_publisheraddressbase_modifiedonbehalfby](#BKMK_lk_publisheraddressbase_modifiedonbehalfby)
- [Publisher_PublisherAddress](#BKMK_Publisher_PublisherAddress)

### <a name="BKMK_lk_publisheraddressbase_createdby"></a> lk_publisheraddressbase_createdby

One-To-Many Relationship: [systemuser lk_publisheraddressbase_createdby](systemuser.md#BKMK_lk_publisheraddressbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_publisheraddressbase_createdonbehalfby"></a> lk_publisheraddressbase_createdonbehalfby

One-To-Many Relationship: [systemuser lk_publisheraddressbase_createdonbehalfby](systemuser.md#BKMK_lk_publisheraddressbase_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_publisheraddressbase_modifiedby"></a> lk_publisheraddressbase_modifiedby

One-To-Many Relationship: [systemuser lk_publisheraddressbase_modifiedby](systemuser.md#BKMK_lk_publisheraddressbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_publisheraddressbase_modifiedonbehalfby"></a> lk_publisheraddressbase_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_publisheraddressbase_modifiedonbehalfby](systemuser.md#BKMK_lk_publisheraddressbase_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_Publisher_PublisherAddress"></a> Publisher_PublisherAddress

One-To-Many Relationship: [publisher Publisher_PublisherAddress](publisher.md#BKMK_Publisher_PublisherAddress)

|Property|Value|
|---|---|
|ReferencedEntity|`publisher`|
|ReferencedAttribute|`publisherid`|
|ReferencingAttribute|`parentid`|
|ReferencingEntityNavigationPropertyName|`parentid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Cascade`<br />Merge: `Cascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.publisheraddress?displayProperty=fullName>
