---
title: "Business Unit (BusinessUnit) table/entity reference (Microsoft Dataverse)"
description: "Includes schema information and supported messages for the Business Unit (BusinessUnit) table/entity with Microsoft Dataverse."
ms.topic: generated-reference
author: phecke
ms.author: pehecke
search.audienceType: 
  - developer
---

# Business Unit (BusinessUnit) table/entity reference (Microsoft Dataverse)

Business, division, or department in the Microsoft Dynamics 365 database.

## Messages

The following table lists the messages for the Business Unit (BusinessUnit) table.
Messages represent operations that can be performed on the table. They may also be events.

| Name <br />Is Event? |Web API Operation |SDK for .NET |
| ---- | ----- |----- |
| `Associate`<br />Event: True |[Associate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Associate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-associate-method-or-associaterequest)|
| `Create`<br />Event: True |`POST` /businessunits<br />See [Create](/powerapps/developer/data-platform/webapi/create-entity-web-api) |[Create records](/power-apps/developer/data-platform/org-service/entity-operations-create#basic-create)|
| `Delete`<br />Event: True |`DELETE` /businessunits(*businessunitid*)<br />See [Delete](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-delete) |[Delete records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-delete)|
| `Disassociate`<br />Event: True |[Disassociate records](/power-apps/developer/data-platform/webapi/associate-disassociate-entities-using-web-api) |[Disassociate records](/power-apps/developer/data-platform/org-service/entity-operations-associate-disassociate#use-the-disassociate-method-or-disassociaterequest)|
| `Retrieve`<br />Event: False |`GET` /businessunits(*businessunitid*)<br />See [Retrieve](/powerapps/developer/data-platform/webapi/retrieve-entity-using-web-api) |[Retrieve records](/power-apps/developer/data-platform/org-service/entity-operations-retrieve)|
| `RetrieveBusinessHierarchyBusinessUnit`<br />Event: False |<xref:Microsoft.Dynamics.CRM.RetrieveBusinessHierarchyBusinessUnit?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.RetrieveBusinessHierarchyBusinessUnitRequest>|
| `RetrieveMultiple`<br />Event: False |`GET` /businessunits<br />See [Query data](/power-apps/developer/data-platform/webapi/query-data-web-api) |[Query data](/power-apps/developer/data-platform/org-service/entity-operations-query-data)|
| `RetrieveSubsidiaryTeamsBusinessUnit`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSubsidiaryTeamsBusinessUnitRequest>|
| `RetrieveSubsidiaryUsersBusinessUnit`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.RetrieveSubsidiaryUsersBusinessUnitRequest>|
| `SetParentBusinessUnit`<br />Event: False | |<xref:Microsoft.Crm.Sdk.Messages.SetParentBusinessUnitRequest>|
| `SetParentSystemUser`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SetParentSystemUser?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SetParentSystemUserRequest>|
| `SetParentTeam`<br />Event: False |<xref:Microsoft.Dynamics.CRM.SetParentTeam?displayProperty=nameWithType /> |<xref:Microsoft.Crm.Sdk.Messages.SetParentTeamRequest>|
| `SetState`<br />Event: True |`PATCH` /businessunits(*businessunitid*)<br />[Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) the `statecode` and `statuscode` properties. |<xref:Microsoft.Crm.Sdk.Messages.SetStateRequest>|
| `Update`<br />Event: True |`PATCH` /businessunits(*businessunitid*)<br />See [Update](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#basic-update) |[Update records](/power-apps/developer/data-platform/org-service/entity-operations-update-delete#basic-update)|
| `Upsert`<br />Event: False |`PATCH` /businessunits(*businessunitid*)<br />See [Upsert a table row](/powerapps/developer/data-platform/webapi/update-delete-entities-using-web-api#upsert-a-table-row) |<xref:Microsoft.Xrm.Sdk.Messages.UpsertRequest>|

## Properties

The following table lists selected properties for the Business Unit (BusinessUnit) table.

|Property|Value|
| --- | --- |
| **DisplayName** | **Business Unit** |
| **DisplayCollectionName** | **Business Units** |
| **SchemaName** | `BusinessUnit` |
| **CollectionSchemaName** | `BusinessUnits` |
| **EntitySetName** | `businessunits`|
| **LogicalName** | `businessunit` |
| **LogicalCollectionName** | `businessunits` |
| **PrimaryIdAttribute** | `businessunitid` |
| **PrimaryNameAttribute** |`name` |
| **TableType** | `Standard` |
| **OwnershipType** | `BusinessOwned` |

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
|GlobalChoiceName|`businessunit_address1_addresstypecode`|

#### Address1_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address1_City"></a> Address1_City

|Property|Value|
|---|---|
|Description|**City name for address 1.**|
|DisplayName|**Bill To City**|
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
|DisplayName|**Bill To Country/Region**|
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
|DisplayName|**Bill To Street 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_line1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address1_Line2"></a> Address1_Line2

|Property|Value|
|---|---|
|Description|**Second line for entering address 1 information.**|
|DisplayName|**Bill To Street 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_line2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address1_Line3"></a> Address1_Line3

|Property|Value|
|---|---|
|Description|**Third line for entering address 1 information.**|
|DisplayName|**Bill To Street 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address1_line3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

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
|DisplayName|**Bill To ZIP/Postal Code**|
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
|GlobalChoiceName|`businessunit_address1_shippingmethodcode`|

#### Address1_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address1_StateOrProvince"></a> Address1_StateOrProvince

|Property|Value|
|---|---|
|Description|**State or province for address 1.**|
|DisplayName|**Bill To State/Province**|
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
|DisplayName|**Main Phone**|
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
|DisplayName|**Other Phone**|
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
|Description|**Type of address for address 2, such as billing, shipping, or primary address.**|
|DisplayName|**Address 2: Address Type**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_addresstypecode`|
|RequiredLevel|None|
|Type|Picklist|
|DefaultFormValue|1|
|GlobalChoiceName|`businessunit_address2_addresstypecode`|

#### Address2_AddressTypeCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_City"></a> Address2_City

|Property|Value|
|---|---|
|Description|**City name for address 2.**|
|DisplayName|**Ship To City**|
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
|DisplayName|**Ship To Country/Region**|
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
|DisplayName|**Ship To Street 1**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_line1`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address2_Line2"></a> Address2_Line2

|Property|Value|
|---|---|
|Description|**Second line for entering address 2 information.**|
|DisplayName|**Ship To Street 2**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_line2`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

### <a name="BKMK_Address2_Line3"></a> Address2_Line3

|Property|Value|
|---|---|
|Description|**Third line for entering address 2 information.**|
|DisplayName|**Ship To Street 3**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`address2_line3`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Active|
|IsLocalizable|False|
|MaxLength|250|

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
|DisplayName|**Ship To ZIP/Postal Code**|
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
|GlobalChoiceName|`businessunit_address2_shippingmethodcode`|

#### Address2_ShippingMethodCode Choices/Options

|Value|Label|
|---|---|
|1|**Default Value**|

### <a name="BKMK_Address2_StateOrProvince"></a> Address2_StateOrProvince

|Property|Value|
|---|---|
|Description|**State or province for address 2.**|
|DisplayName|**Ship To State/Province**|
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

### <a name="BKMK_BusinessUnitId"></a> BusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier of the business unit.**|
|DisplayName|**Business Unit**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`businessunitid`|
|RequiredLevel|SystemRequired|
|Type|Uniqueidentifier|

### <a name="BKMK_CalendarId"></a> CalendarId

|Property|Value|
|---|---|
|Description|**Fiscal calendar associated with the business unit.**|
|DisplayName|**Calendar**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`calendarid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|calendar|

### <a name="BKMK_CostCenter"></a> CostCenter

|Property|Value|
|---|---|
|Description|**Name of the business unit cost center.**|
|DisplayName|**Cost Center**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`costcenter`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_CreditLimit"></a> CreditLimit

|Property|Value|
|---|---|
|Description|**Credit limit for the business unit.**|
|DisplayName|**Credit Limit**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`creditlimit`|
|RequiredLevel|None|
|Type|Double|
|ImeMode|Disabled|
|MaxValue|1000000000|
|MinValue|0|
|Precision|2|

### <a name="BKMK_Description"></a> Description

|Property|Value|
|---|---|
|Description|**Description of the business unit.**|
|DisplayName|**Description**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`description`|
|RequiredLevel|None|
|Type|Memo|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|2000|

### <a name="BKMK_DivisionName"></a> DivisionName

|Property|Value|
|---|---|
|Description|**Name of the division to which the business unit belongs.**|
|DisplayName|**Division**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`divisionname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_EMailAddress"></a> EMailAddress

|Property|Value|
|---|---|
|Description|**Email address for the business unit.**|
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

### <a name="BKMK_FileAsName"></a> FileAsName

|Property|Value|
|---|---|
|Description|**Alternative name under which the business unit can be filed.**|
|DisplayName|**File as Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`fileasname`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|100|

### <a name="BKMK_FtpSiteUrl"></a> FtpSiteUrl

|Property|Value|
|---|---|
|Description|**FTP site URL for the business unit.**|
|DisplayName|**FTP Site**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`ftpsiteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|200|

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

### <a name="BKMK_InheritanceMask"></a> InheritanceMask

|Property|Value|
|---|---|
|Description|**Inheritance mask for the business unit.**|
|DisplayName|**Inheritance Mask**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`inheritancemask`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1000000000|
|MinValue|0|

### <a name="BKMK_IsDisabled"></a> IsDisabled

|Property|Value|
|---|---|
|Description|**Information about whether the business unit is enabled or disabled.**|
|DisplayName|**Is Disabled**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`isdisabled`|
|RequiredLevel|SystemRequired|
|Type|Boolean|
|GlobalChoiceName|`businessunit_isdisabled`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|

### <a name="BKMK_Name"></a> Name

|Property|Value|
|---|---|
|Description|**Name of the business unit.**|
|DisplayName|**Name**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`name`|
|RequiredLevel|SystemRequired|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|160|

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

### <a name="BKMK_ParentBusinessUnitId"></a> ParentBusinessUnitId

|Property|Value|
|---|---|
|Description|**Unique identifier for the parent business unit.**|
|DisplayName|**Parent Business**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`parentbusinessunitid`|
|RequiredLevel|ApplicationRequired|
|Type|Lookup|
|Targets|businessunit|

### <a name="BKMK_Picture"></a> Picture

|Property|Value|
|---|---|
|Description|**Picture or diagram of the business unit.**|
|DisplayName|**Picture**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`picture`|
|RequiredLevel|None|
|Type|Memo|
|Format|TextArea|
|FormatName|TextArea|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|1073741823|

### <a name="BKMK_StockExchange"></a> StockExchange

|Property|Value|
|---|---|
|Description|**Stock exchange on which the business is listed.**|
|DisplayName|**Stock Exchange**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`stockexchange`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|20|

### <a name="BKMK_TickerSymbol"></a> TickerSymbol

|Property|Value|
|---|---|
|Description|**Stock exchange ticker symbol for the business unit.**|
|DisplayName|**Ticker Symbol**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`tickersymbol`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|10|

### <a name="BKMK_TransactionCurrencyId"></a> TransactionCurrencyId

|Property|Value|
|---|---|
|Description|**Unique identifier of the currency associated with the businessunit.**|
|DisplayName|**Currency**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`transactioncurrencyid`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|transactioncurrency|

### <a name="BKMK_UTCOffset"></a> UTCOffset

|Property|Value|
|---|---|
|Description|**UTC offset for the business unit. This is the difference between local time and standard Coordinated Universal Time.**|
|DisplayName|**UTC Offset**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`utcoffset`|
|RequiredLevel|None|
|Type|Integer|
|MaxValue|1500|
|MinValue|-1500|

### <a name="BKMK_WebSiteUrl"></a> WebSiteUrl

|Property|Value|
|---|---|
|Description|**Website URL for the business unit.**|
|DisplayName|**Website**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`websiteurl`|
|RequiredLevel|None|
|Type|String|
|Format|Url|
|FormatName|Url|
|ImeMode|Inactive|
|IsLocalizable|False|
|MaxLength|200|

### <a name="BKMK_WorkflowSuspended"></a> WorkflowSuspended

|Property|Value|
|---|---|
|Description|**Information about whether workflow or sales process rules have been suspended.**|
|DisplayName|**Workflow Suspended**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`workflowsuspended`|
|RequiredLevel|None|
|Type|Boolean|
|GlobalChoiceName|`businessunit_workflowsuspended`|
|DefaultValue|False|
|True Label|Yes|
|False Label|No|


## Read-only columns/attributes

These columns/attributes return false for both **IsValidForCreate** and **IsValidForUpdate**. Listed by **SchemaName**.

- [CreatedBy](#BKMK_CreatedBy)
- [CreatedOn](#BKMK_CreatedOn)
- [CreatedOnBehalfBy](#BKMK_CreatedOnBehalfBy)
- [DisabledReason](#BKMK_DisabledReason)
- [ExchangeRate](#BKMK_ExchangeRate)
- [ModifiedBy](#BKMK_ModifiedBy)
- [ModifiedOn](#BKMK_ModifiedOn)
- [ModifiedOnBehalfBy](#BKMK_ModifiedOnBehalfBy)
- [OrganizationId](#BKMK_OrganizationId)
- [UserGroupId](#BKMK_UserGroupId)
- [VersionNumber](#BKMK_VersionNumber)

### <a name="BKMK_CreatedBy"></a> CreatedBy

|Property|Value|
|---|---|
|Description|**Unique identifier of the user who created the business unit.**|
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
|Description|**Date and time when the business unit was created.**|
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
|Description|**Unique identifier of the delegate user who created the businessunit.**|
|DisplayName|**Created By (Delegate)**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`createdonbehalfby`|
|RequiredLevel|None|
|Type|Lookup|
|Targets|systemuser|

### <a name="BKMK_DisabledReason"></a> DisabledReason

|Property|Value|
|---|---|
|Description|**Reason for disabling the business unit.**|
|DisplayName|**Disable Reason**|
|IsValidForForm|True|
|IsValidForRead|True|
|LogicalName|`disabledreason`|
|RequiredLevel|None|
|Type|String|
|Format|Text|
|FormatName|Text|
|ImeMode|Auto|
|IsLocalizable|False|
|MaxLength|500|

### <a name="BKMK_ExchangeRate"></a> ExchangeRate

|Property|Value|
|---|---|
|Description|**Exchange rate for the currency associated with the businessunit with respect to the base currency.**|
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
|Description|**Unique identifier of the user who last modified the business unit.**|
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
|Description|**Date and time when the business unit was last modified.**|
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
|Description|**Unique identifier of the delegate user who last modified the businessunit.**|
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
|Description|**Unique identifier of the organization associated with the business unit.**|
|DisplayName|**Organization**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`organizationid`|
|RequiredLevel|SystemRequired|
|Type|Lookup|
|Targets|organization|

### <a name="BKMK_UserGroupId"></a> UserGroupId

|Property|Value|
|---|---|
|Description||
|DisplayName||
|IsValidForForm|False|
|IsValidForRead|False|
|LogicalName|`usergroupid`|
|RequiredLevel|None|
|Type|Uniqueidentifier|

### <a name="BKMK_VersionNumber"></a> VersionNumber

|Property|Value|
|---|---|
|Description|**Version number of the business unit.**|
|DisplayName|**Version number**|
|IsValidForForm|False|
|IsValidForRead|True|
|LogicalName|`versionnumber`|
|RequiredLevel|None|
|Type|BigInt|
|MaxValue|9223372036854775807|
|MinValue|-9223372036854775808|

## Many-to-One relationships

These relationships are many-to-one. Listed by **SchemaName**.

- [business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit-many-to-one)
- [BusinessUnit_Calendar](#BKMK_BusinessUnit_Calendar)
- [lk_businessunit_createdonbehalfby](#BKMK_lk_businessunit_createdonbehalfby)
- [lk_businessunit_modifiedonbehalfby](#BKMK_lk_businessunit_modifiedonbehalfby)
- [lk_businessunitbase_createdby](#BKMK_lk_businessunitbase_createdby)
- [lk_businessunitbase_modifiedby](#BKMK_lk_businessunitbase_modifiedby)
- [organization_business_units](#BKMK_organization_business_units)
- [TransactionCurrency_BusinessUnit](#BKMK_TransactionCurrency_BusinessUnit)

### <a name="BKMK_business_unit_parent_business_unit-many-to-one"></a> business_unit_parent_business_unit

One-To-Many Relationship: [businessunit business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit-one-to-many)

|Property|Value|
|---|---|
|ReferencedEntity|`businessunit`|
|ReferencedAttribute|`businessunitid`|
|ReferencingAttribute|`parentbusinessunitid`|
|ReferencingEntityNavigationPropertyName|`parentbusinessunitid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `Restrict`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_BusinessUnit_Calendar"></a> BusinessUnit_Calendar

One-To-Many Relationship: [calendar BusinessUnit_Calendar](calendar.md#BKMK_BusinessUnit_Calendar)

|Property|Value|
|---|---|
|ReferencedEntity|`calendar`|
|ReferencedAttribute|`calendarid`|
|ReferencingAttribute|`calendarid`|
|ReferencingEntityNavigationPropertyName|`calendarid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `RemoveLink`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_businessunit_createdonbehalfby"></a> lk_businessunit_createdonbehalfby

One-To-Many Relationship: [systemuser lk_businessunit_createdonbehalfby](systemuser.md#BKMK_lk_businessunit_createdonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdonbehalfby`|
|ReferencingEntityNavigationPropertyName|`createdonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_businessunit_modifiedonbehalfby"></a> lk_businessunit_modifiedonbehalfby

One-To-Many Relationship: [systemuser lk_businessunit_modifiedonbehalfby](systemuser.md#BKMK_lk_businessunit_modifiedonbehalfby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedonbehalfby`|
|ReferencingEntityNavigationPropertyName|`modifiedonbehalfby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_businessunitbase_createdby"></a> lk_businessunitbase_createdby

One-To-Many Relationship: [systemuser lk_businessunitbase_createdby](systemuser.md#BKMK_lk_businessunitbase_createdby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`createdby`|
|ReferencingEntityNavigationPropertyName|`createdby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_lk_businessunitbase_modifiedby"></a> lk_businessunitbase_modifiedby

One-To-Many Relationship: [systemuser lk_businessunitbase_modifiedby](systemuser.md#BKMK_lk_businessunitbase_modifiedby)

|Property|Value|
|---|---|
|ReferencedEntity|`systemuser`|
|ReferencedAttribute|`systemuserid`|
|ReferencingAttribute|`modifiedby`|
|ReferencingEntityNavigationPropertyName|`modifiedby`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_organization_business_units"></a> organization_business_units

One-To-Many Relationship: [organization organization_business_units](organization.md#BKMK_organization_business_units)

|Property|Value|
|---|---|
|ReferencedEntity|`organization`|
|ReferencedAttribute|`organizationid`|
|ReferencingAttribute|`organizationid`|
|ReferencingEntityNavigationPropertyName|`organizationid`|
|IsHierarchical||
|CascadeConfiguration|Archive: `NoCascade`<br />Assign: `NoCascade`<br />Delete: `NoCascade`<br />Merge: `NoCascade`<br />Reparent: `NoCascade`<br />RollupView: `NoCascade`<br />Share: `NoCascade`<br />Unshare: `NoCascade`|

### <a name="BKMK_TransactionCurrency_BusinessUnit"></a> TransactionCurrency_BusinessUnit

One-To-Many Relationship: [transactioncurrency TransactionCurrency_BusinessUnit](transactioncurrency.md#BKMK_TransactionCurrency_BusinessUnit)

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

- [adx_inviteredemption_businessunit_owningbusinessunit](#BKMK_adx_inviteredemption_businessunit_owningbusinessunit)
- [adx_portalcomment_businessunit_owningbusinessunit](#BKMK_adx_portalcomment_businessunit_owningbusinessunit)
- [BulkDeleteOperation_BusinessUnit](#BKMK_BulkDeleteOperation_BusinessUnit)
- [business_unit_accounts](#BKMK_business_unit_accounts)
- [business_unit_actioncards](#BKMK_business_unit_actioncards)
- [business_unit_activityfileattachment](#BKMK_business_unit_activityfileattachment)
- [business_unit_activitypointer](#BKMK_business_unit_activitypointer)
- [business_unit_adx_invitation](#BKMK_business_unit_adx_invitation)
- [business_unit_adx_setting](#BKMK_business_unit_adx_setting)
- [business_unit_aiplugin](#BKMK_business_unit_aiplugin)
- [business_unit_aipluginauth](#BKMK_business_unit_aipluginauth)
- [business_unit_aipluginconversationstarter](#BKMK_business_unit_aipluginconversationstarter)
- [business_unit_aipluginconversationstartermapping](#BKMK_business_unit_aipluginconversationstartermapping)
- [business_unit_aipluginexternalschema](#BKMK_business_unit_aipluginexternalschema)
- [business_unit_aipluginexternalschemaproperty](#BKMK_business_unit_aipluginexternalschemaproperty)
- [business_unit_aiplugingovernance](#BKMK_business_unit_aiplugingovernance)
- [business_unit_aiplugingovernanceext](#BKMK_business_unit_aiplugingovernanceext)
- [business_unit_aiplugininstance](#BKMK_business_unit_aiplugininstance)
- [business_unit_aipluginoperation](#BKMK_business_unit_aipluginoperation)
- [business_unit_aipluginoperationparameter](#BKMK_business_unit_aipluginoperationparameter)
- [business_unit_aipluginoperationresponsetemplate](#BKMK_business_unit_aipluginoperationresponsetemplate)
- [business_unit_aipluginusersetting](#BKMK_business_unit_aipluginusersetting)
- [business_unit_annotations](#BKMK_business_unit_annotations)
- [business_unit_applicationuser](#BKMK_business_unit_applicationuser)
- [business_unit_appnotification](#BKMK_business_unit_appnotification)
- [business_unit_appointment_activities](#BKMK_business_unit_appointment_activities)
- [business_unit_approvalprocess](#BKMK_business_unit_approvalprocess)
- [business_unit_approvalstageapproval](#BKMK_business_unit_approvalstageapproval)
- [business_unit_approvalstagecondition](#BKMK_business_unit_approvalstagecondition)
- [business_unit_approvalstageintelligent](#BKMK_business_unit_approvalstageintelligent)
- [business_unit_approvalstageorder](#BKMK_business_unit_approvalstageorder)
- [business_unit_asyncoperation](#BKMK_business_unit_asyncoperation)
- [business_unit_bot](#BKMK_business_unit_bot)
- [business_unit_botcomponent](#BKMK_business_unit_botcomponent)
- [business_unit_botcomponentcollection](#BKMK_business_unit_botcomponentcollection)
- [business_unit_businessprocess](#BKMK_business_unit_businessprocess)
- [business_unit_calendars](#BKMK_business_unit_calendars)
- [business_unit_card](#BKMK_business_unit_card)
- [business_unit_category](#BKMK_business_unit_category)
- [business_unit_certificatecredential](#BKMK_business_unit_certificatecredential)
- [business_unit_connectioninstance](#BKMK_business_unit_connectioninstance)
- [business_unit_connectionreference](#BKMK_business_unit_connectionreference)
- [business_unit_connections](#BKMK_business_unit_connections)
- [business_unit_connector](#BKMK_business_unit_connector)
- [business_unit_contacts](#BKMK_business_unit_contacts)
- [business_unit_conversationtranscript](#BKMK_business_unit_conversationtranscript)
- [business_unit_copilotglossaryterm](#BKMK_business_unit_copilotglossaryterm)
- [business_unit_copilotsynonyms](#BKMK_business_unit_copilotsynonyms)
- [business_unit_credential](#BKMK_business_unit_credential)
- [business_unit_customapi](#BKMK_business_unit_customapi)
- [business_unit_datalakefolder](#BKMK_business_unit_datalakefolder)
- [business_unit_desktopflowbinary](#BKMK_business_unit_desktopflowbinary)
- [business_unit_desktopflowmodule](#BKMK_business_unit_desktopflowmodule)
- [business_unit_dvfilesearch](#BKMK_business_unit_dvfilesearch)
- [business_unit_dvfilesearchattribute](#BKMK_business_unit_dvfilesearchattribute)
- [business_unit_dvfilesearchentity](#BKMK_business_unit_dvfilesearchentity)
- [business_unit_dvtablesearch](#BKMK_business_unit_dvtablesearch)
- [business_unit_dvtablesearchattribute](#BKMK_business_unit_dvtablesearchattribute)
- [business_unit_dvtablesearchentity](#BKMK_business_unit_dvtablesearchentity)
- [business_unit_email_activities](#BKMK_business_unit_email_activities)
- [business_unit_emailserverprofile](#BKMK_business_unit_emailserverprofile)
- [business_unit_environmentvariabledefinition](#BKMK_business_unit_environmentvariabledefinition)
- [business_unit_exchangesyncidmapping](#BKMK_business_unit_exchangesyncidmapping)
- [business_unit_exportedexcel](#BKMK_business_unit_exportedexcel)
- [business_unit_exportsolutionupload](#BKMK_business_unit_exportsolutionupload)
- [business_unit_fabricaiskill](#BKMK_business_unit_fabricaiskill)
- [business_unit_fax_activities](#BKMK_business_unit_fax_activities)
- [business_unit_featurecontrolsetting](#BKMK_business_unit_featurecontrolsetting)
- [business_unit_federatedknowledgeconfiguration](#BKMK_business_unit_federatedknowledgeconfiguration)
- [business_unit_federatedknowledgeentityconfiguration](#BKMK_business_unit_federatedknowledgeentityconfiguration)
- [business_unit_feedback](#BKMK_business_unit_feedback)
- [business_unit_flowaggregation](#BKMK_business_unit_flowaggregation)
- [business_unit_flowcapacityassignment](#BKMK_business_unit_flowcapacityassignment)
- [business_unit_flowcredentialapplication](#BKMK_business_unit_flowcredentialapplication)
- [business_unit_flowevent](#BKMK_business_unit_flowevent)
- [business_unit_flowmachine](#BKMK_business_unit_flowmachine)
- [business_unit_flowmachinegroup](#BKMK_business_unit_flowmachinegroup)
- [business_unit_flowmachineimage](#BKMK_business_unit_flowmachineimage)
- [business_unit_flowmachineimageversion](#BKMK_business_unit_flowmachineimageversion)
- [business_unit_flowmachinenetwork](#BKMK_business_unit_flowmachinenetwork)
- [business_unit_flowrun](#BKMK_business_unit_flowrun)
- [business_unit_flowsession](#BKMK_business_unit_flowsession)
- [business_unit_fxexpression](#BKMK_business_unit_fxexpression)
- [business_unit_goal](#BKMK_business_unit_goal)
- [business_unit_goalrollupquery](#BKMK_business_unit_goalrollupquery)
- [business_unit_governanceconfiguration](#BKMK_business_unit_governanceconfiguration)
- [business_unit_indexedtrait](#BKMK_business_unit_indexedtrait)
- [business_unit_interactionforemail](#BKMK_business_unit_interactionforemail)
- [business_unit_keyvaultreference](#BKMK_business_unit_keyvaultreference)
- [business_unit_knowledgearticle](#BKMK_business_unit_knowledgearticle)
- [business_unit_knowledgefaq](#BKMK_business_unit_knowledgefaq)
- [business_unit_letter_activities](#BKMK_business_unit_letter_activities)
- [business_unit_mailbox](#BKMK_business_unit_mailbox)
- [business_unit_mailmergetemplates](#BKMK_business_unit_mailmergetemplates)
- [business_unit_managedidentity](#BKMK_business_unit_managedidentity)
- [business_unit_msdyn_aibdataset](#BKMK_business_unit_msdyn_aibdataset)
- [business_unit_msdyn_aibdatasetfile](#BKMK_business_unit_msdyn_aibdatasetfile)
- [business_unit_msdyn_aibdatasetrecord](#BKMK_business_unit_msdyn_aibdatasetrecord)
- [business_unit_msdyn_aibdatasetscontainer](#BKMK_business_unit_msdyn_aibdatasetscontainer)
- [business_unit_msdyn_aibfeedbackloop](#BKMK_business_unit_msdyn_aibfeedbackloop)
- [business_unit_msdyn_aibfile](#BKMK_business_unit_msdyn_aibfile)
- [business_unit_msdyn_aibfileattacheddata](#BKMK_business_unit_msdyn_aibfileattacheddata)
- [business_unit_msdyn_aidataprocessingevent](#BKMK_business_unit_msdyn_aidataprocessingevent)
- [business_unit_msdyn_aidocumenttemplate](#BKMK_business_unit_msdyn_aidocumenttemplate)
- [business_unit_msdyn_aievaluationconfiguration](#BKMK_business_unit_msdyn_aievaluationconfiguration)
- [business_unit_msdyn_aievaluationrun](#BKMK_business_unit_msdyn_aievaluationrun)
- [business_unit_msdyn_aievent](#BKMK_business_unit_msdyn_aievent)
- [business_unit_msdyn_aifptrainingdocument](#BKMK_business_unit_msdyn_aifptrainingdocument)
- [business_unit_msdyn_aimodel](#BKMK_business_unit_msdyn_aimodel)
- [business_unit_msdyn_aiodimage](#BKMK_business_unit_msdyn_aiodimage)
- [business_unit_msdyn_aiodlabel](#BKMK_business_unit_msdyn_aiodlabel)
- [business_unit_msdyn_aiodtrainingboundingbox](#BKMK_business_unit_msdyn_aiodtrainingboundingbox)
- [business_unit_msdyn_aiodtrainingimage](#BKMK_business_unit_msdyn_aiodtrainingimage)
- [business_unit_msdyn_aitemplate](#BKMK_business_unit_msdyn_aitemplate)
- [business_unit_msdyn_aitestcase](#BKMK_business_unit_msdyn_aitestcase)
- [business_unit_msdyn_aitestcasedocument](#BKMK_business_unit_msdyn_aitestcasedocument)
- [business_unit_msdyn_aitestcaseinput](#BKMK_business_unit_msdyn_aitestcaseinput)
- [business_unit_msdyn_aitestrun](#BKMK_business_unit_msdyn_aitestrun)
- [business_unit_msdyn_aitestrunbatch](#BKMK_business_unit_msdyn_aitestrunbatch)
- [business_unit_msdyn_analysiscomponent](#BKMK_business_unit_msdyn_analysiscomponent)
- [business_unit_msdyn_analysisjob](#BKMK_business_unit_msdyn_analysisjob)
- [business_unit_msdyn_analysisoverride](#BKMK_business_unit_msdyn_analysisoverride)
- [business_unit_msdyn_analysisresult](#BKMK_business_unit_msdyn_analysisresult)
- [business_unit_msdyn_analysisresultdetail](#BKMK_business_unit_msdyn_analysisresultdetail)
- [business_unit_msdyn_copilotinteractions](#BKMK_business_unit_msdyn_copilotinteractions)
- [business_unit_msdyn_customcontrolextendedsettings](#BKMK_business_unit_msdyn_customcontrolextendedsettings)
- [business_unit_msdyn_dataflow](#BKMK_business_unit_msdyn_dataflow)
- [business_unit_msdyn_dataflow_datalakefolder](#BKMK_business_unit_msdyn_dataflow_datalakefolder)
- [business_unit_msdyn_dataflowconnectionreference](#BKMK_business_unit_msdyn_dataflowconnectionreference)
- [business_unit_msdyn_dataflowrefreshhistory](#BKMK_business_unit_msdyn_dataflowrefreshhistory)
- [business_unit_msdyn_dataflowtemplate](#BKMK_business_unit_msdyn_dataflowtemplate)
- [business_unit_msdyn_dmsrequest](#BKMK_business_unit_msdyn_dmsrequest)
- [business_unit_msdyn_dmsrequeststatus](#BKMK_business_unit_msdyn_dmsrequeststatus)
- [business_unit_msdyn_dmssyncrequest](#BKMK_business_unit_msdyn_dmssyncrequest)
- [business_unit_msdyn_dmssyncstatus](#BKMK_business_unit_msdyn_dmssyncstatus)
- [business_unit_msdyn_entitylinkchatconfiguration](#BKMK_business_unit_msdyn_entitylinkchatconfiguration)
- [business_unit_msdyn_entityrefreshhistory](#BKMK_business_unit_msdyn_entityrefreshhistory)
- [business_unit_msdyn_favoriteknowledgearticle](#BKMK_business_unit_msdyn_favoriteknowledgearticle)
- [business_unit_msdyn_federatedarticle](#BKMK_business_unit_msdyn_federatedarticle)
- [business_unit_msdyn_fileupload](#BKMK_business_unit_msdyn_fileupload)
- [business_unit_msdyn_flow_actionapprovalmodel](#BKMK_business_unit_msdyn_flow_actionapprovalmodel)
- [business_unit_msdyn_flow_approval](#BKMK_business_unit_msdyn_flow_approval)
- [business_unit_msdyn_flow_approvalrequest](#BKMK_business_unit_msdyn_flow_approvalrequest)
- [business_unit_msdyn_flow_approvalresponse](#BKMK_business_unit_msdyn_flow_approvalresponse)
- [business_unit_msdyn_flow_approvalstep](#BKMK_business_unit_msdyn_flow_approvalstep)
- [business_unit_msdyn_flow_awaitallactionapprovalmodel](#BKMK_business_unit_msdyn_flow_awaitallactionapprovalmodel)
- [business_unit_msdyn_flow_awaitallapprovalmodel](#BKMK_business_unit_msdyn_flow_awaitallapprovalmodel)
- [business_unit_msdyn_flow_basicapprovalmodel](#BKMK_business_unit_msdyn_flow_basicapprovalmodel)
- [business_unit_msdyn_flow_flowapproval](#BKMK_business_unit_msdyn_flow_flowapproval)
- [business_unit_msdyn_formmapping](#BKMK_business_unit_msdyn_formmapping)
- [business_unit_msdyn_function](#BKMK_business_unit_msdyn_function)
- [business_unit_msdyn_historicalcaseharvestbatch](#BKMK_business_unit_msdyn_historicalcaseharvestbatch)
- [business_unit_msdyn_historicalcaseharvestrun](#BKMK_business_unit_msdyn_historicalcaseharvestrun)
- [business_unit_msdyn_integratedsearchprovider](#BKMK_business_unit_msdyn_integratedsearchprovider)
- [business_unit_msdyn_kalanguagesetting](#BKMK_business_unit_msdyn_kalanguagesetting)
- [business_unit_msdyn_kbattachment](#BKMK_business_unit_msdyn_kbattachment)
- [business_unit_msdyn_kmfederatedsearchconfig](#BKMK_business_unit_msdyn_kmfederatedsearchconfig)
- [business_unit_msdyn_knowledgearticleimage](#BKMK_business_unit_msdyn_knowledgearticleimage)
- [business_unit_msdyn_knowledgearticletemplate](#BKMK_business_unit_msdyn_knowledgearticletemplate)
- [business_unit_msdyn_knowledgeassetconfiguration](#BKMK_business_unit_msdyn_knowledgeassetconfiguration)
- [business_unit_msdyn_knowledgeharvestjobrecord](#BKMK_business_unit_msdyn_knowledgeharvestjobrecord)
- [business_unit_msdyn_knowledgeinteractioninsight](#BKMK_business_unit_msdyn_knowledgeinteractioninsight)
- [business_unit_msdyn_knowledgemanagementsetting](#BKMK_business_unit_msdyn_knowledgemanagementsetting)
- [business_unit_msdyn_knowledgepersonalfilter](#BKMK_business_unit_msdyn_knowledgepersonalfilter)
- [business_unit_msdyn_knowledgesearchfilter](#BKMK_business_unit_msdyn_knowledgesearchfilter)
- [business_unit_msdyn_knowledgesearchinsight](#BKMK_business_unit_msdyn_knowledgesearchinsight)
- [business_unit_msdyn_mobileapp](#BKMK_business_unit_msdyn_mobileapp)
- [business_unit_msdyn_pmanalysishistory](#BKMK_business_unit_msdyn_pmanalysishistory)
- [business_unit_msdyn_pmbusinessruleautomationconfig](#BKMK_business_unit_msdyn_pmbusinessruleautomationconfig)
- [business_unit_msdyn_pmcalendar](#BKMK_business_unit_msdyn_pmcalendar)
- [business_unit_msdyn_pmcalendarversion](#BKMK_business_unit_msdyn_pmcalendarversion)
- [business_unit_msdyn_pminferredtask](#BKMK_business_unit_msdyn_pminferredtask)
- [business_unit_msdyn_pmprocessextendedmetadataversion](#BKMK_business_unit_msdyn_pmprocessextendedmetadataversion)
- [business_unit_msdyn_pmprocesstemplate](#BKMK_business_unit_msdyn_pmprocesstemplate)
- [business_unit_msdyn_pmprocessusersettings](#BKMK_business_unit_msdyn_pmprocessusersettings)
- [business_unit_msdyn_pmprocessversion](#BKMK_business_unit_msdyn_pmprocessversion)
- [business_unit_msdyn_pmrecording](#BKMK_business_unit_msdyn_pmrecording)
- [business_unit_msdyn_pmsimulation](#BKMK_business_unit_msdyn_pmsimulation)
- [business_unit_msdyn_pmtemplate](#BKMK_business_unit_msdyn_pmtemplate)
- [business_unit_msdyn_pmview](#BKMK_business_unit_msdyn_pmview)
- [business_unit_msdyn_qna](#BKMK_business_unit_msdyn_qna)
- [business_unit_msdyn_richtextfile](#BKMK_business_unit_msdyn_richtextfile)
- [business_unit_msdyn_salesforcestructuredobject](#BKMK_business_unit_msdyn_salesforcestructuredobject)
- [business_unit_msdyn_salesforcestructuredqnaconfig](#BKMK_business_unit_msdyn_salesforcestructuredqnaconfig)
- [business_unit_msdyn_schedule](#BKMK_business_unit_msdyn_schedule)
- [business_unit_msdyn_serviceconfiguration](#BKMK_business_unit_msdyn_serviceconfiguration)
- [business_unit_msdyn_slakpi](#BKMK_business_unit_msdyn_slakpi)
- [business_unit_msdyn_solutionhealthrule](#BKMK_business_unit_msdyn_solutionhealthrule)
- [business_unit_msdyn_solutionhealthruleargument](#BKMK_business_unit_msdyn_solutionhealthruleargument)
- [business_unit_msdyn_virtualtablecolumncandidate](#BKMK_business_unit_msdyn_virtualtablecolumncandidate)
- [business_unit_msdynce_botcontent](#BKMK_business_unit_msdynce_botcontent)
- [business_unit_mspcat_catalogsubmissionfiles](#BKMK_business_unit_mspcat_catalogsubmissionfiles)
- [business_unit_mspcat_packagestore](#BKMK_business_unit_mspcat_packagestore)
- [business_unit_nlsqregistration](#BKMK_business_unit_nlsqregistration)
- [business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit-one-to-many)
- [business_unit_personaldocumenttemplates](#BKMK_business_unit_personaldocumenttemplates)
- [business_unit_phone_call_activities](#BKMK_business_unit_phone_call_activities)
- [business_unit_plannerbusinessscenario](#BKMK_business_unit_plannerbusinessscenario)
- [business_unit_plannersyncaction](#BKMK_business_unit_plannersyncaction)
- [business_unit_plugin](#BKMK_business_unit_plugin)
- [business_unit_postfollows](#BKMK_business_unit_postfollows)
- [business_unit_PostRegarding](#BKMK_business_unit_PostRegarding)
- [business_unit_powerbidataset](#BKMK_business_unit_powerbidataset)
- [business_unit_powerbidatasetapdx](#BKMK_business_unit_powerbidatasetapdx)
- [business_unit_powerbimashupparameter](#BKMK_business_unit_powerbimashupparameter)
- [business_unit_powerbireport](#BKMK_business_unit_powerbireport)
- [business_unit_powerbireportapdx](#BKMK_business_unit_powerbireportapdx)
- [business_unit_powerfxrule](#BKMK_business_unit_powerfxrule)
- [business_unit_powerpagecomponent](#BKMK_business_unit_powerpagecomponent)
- [business_unit_powerpagesddosalert](#BKMK_business_unit_powerpagesddosalert)
- [business_unit_powerpagesite](#BKMK_business_unit_powerpagesite)
- [business_unit_powerpagesitelanguage](#BKMK_business_unit_powerpagesitelanguage)
- [business_unit_powerpagesitepublished](#BKMK_business_unit_powerpagesitepublished)
- [business_unit_powerpageslog](#BKMK_business_unit_powerpageslog)
- [business_unit_powerpagesmanagedidentity](#BKMK_business_unit_powerpagesmanagedidentity)
- [business_unit_powerpagesscanreport](#BKMK_business_unit_powerpagesscanreport)
- [business_unit_powerpagessiteaifeedback](#BKMK_business_unit_powerpagessiteaifeedback)
- [business_unit_powerpagessourcefile](#BKMK_business_unit_powerpagessourcefile)
- [business_unit_privilegecheckerrun](#BKMK_business_unit_privilegecheckerrun)
- [business_unit_processstageparameter](#BKMK_business_unit_processstageparameter)
- [business_unit_queues](#BKMK_business_unit_queues)
- [business_unit_queues2](#BKMK_business_unit_queues2)
- [business_unit_recentlyused](#BKMK_business_unit_recentlyused)
- [business_unit_recurrencerule](#BKMK_business_unit_recurrencerule)
- [business_unit_recurringappointmentmaster_activities](#BKMK_business_unit_recurringappointmentmaster_activities)
- [business_unit_reports](#BKMK_business_unit_reports)
- [business_unit_retaineddataexcel](#BKMK_business_unit_retaineddataexcel)
- [business_unit_retentionconfig](#BKMK_business_unit_retentionconfig)
- [business_unit_retentionfailuredetail](#BKMK_business_unit_retentionfailuredetail)
- [business_unit_retentionoperation](#BKMK_business_unit_retentionoperation)
- [business_unit_retentionsuccessdetail](#BKMK_business_unit_retentionsuccessdetail)
- [business_unit_roles](#BKMK_business_unit_roles)
- [business_unit_savingrule](#BKMK_business_unit_savingrule)
- [business_unit_sharepointdocumentlocation](#BKMK_business_unit_sharepointdocumentlocation)
- [business_unit_sharepointsites](#BKMK_business_unit_sharepointsites)
- [business_unit_sideloadedaiplugin](#BKMK_business_unit_sideloadedaiplugin)
- [business_unit_signal](#BKMK_business_unit_signal)
- [business_unit_slabase](#BKMK_business_unit_slabase)
- [business_unit_slakpiinstance](#BKMK_business_unit_slakpiinstance)
- [business_unit_socialactivity](#BKMK_business_unit_socialactivity)
- [business_unit_socialprofiles](#BKMK_business_unit_socialprofiles)
- [business_unit_solutioncomponentbatchconfiguration](#BKMK_business_unit_solutioncomponentbatchconfiguration)
- [business_unit_stagesolutionupload](#BKMK_business_unit_stagesolutionupload)
- [business_unit_synapsedatabase](#BKMK_business_unit_synapsedatabase)
- [business_unit_system_users](#BKMK_business_unit_system_users)
- [business_unit_tag](#BKMK_business_unit_tag)
- [business_unit_taggedflowsession](#BKMK_business_unit_taggedflowsession)
- [business_unit_taggedprocess](#BKMK_business_unit_taggedprocess)
- [business_unit_task_activities](#BKMK_business_unit_task_activities)
- [business_unit_teams](#BKMK_business_unit_teams)
- [business_unit_templates](#BKMK_business_unit_templates)
- [business_unit_trait](#BKMK_business_unit_trait)
- [business_unit_unstructuredfilesearchentity](#BKMK_business_unit_unstructuredfilesearchentity)
- [business_unit_unstructuredfilesearchrecord](#BKMK_business_unit_unstructuredfilesearchrecord)
- [business_unit_user_settings](#BKMK_business_unit_user_settings)
- [business_unit_userform](#BKMK_business_unit_userform)
- [business_unit_userquery](#BKMK_business_unit_userquery)
- [business_unit_userqueryvisualizations](#BKMK_business_unit_userqueryvisualizations)
- [business_unit_workflow](#BKMK_business_unit_workflow)
- [business_unit_workflowbinary](#BKMK_business_unit_workflowbinary)
- [business_unit_workflowlogs](#BKMK_business_unit_workflowlogs)
- [business_unit_workflowmetadata](#BKMK_business_unit_workflowmetadata)
- [business_unit_workqueue](#BKMK_business_unit_workqueue)
- [business_unit_workqueueitem](#BKMK_business_unit_workqueueitem)
- [BusinessUnit_AsyncOperations](#BKMK_BusinessUnit_AsyncOperations)
- [BusinessUnit_BulkDeleteFailures](#BKMK_BusinessUnit_BulkDeleteFailures)
- [businessunit_callbackregistration](#BKMK_businessunit_callbackregistration)
- [businessunit_canvasapp](#BKMK_businessunit_canvasapp)
- [BusinessUnit_DuplicateRules](#BKMK_BusinessUnit_DuplicateRules)
- [BusinessUnit_ImportData](#BKMK_BusinessUnit_ImportData)
- [BusinessUnit_ImportFiles](#BKMK_BusinessUnit_ImportFiles)
- [BusinessUnit_ImportLogs](#BKMK_BusinessUnit_ImportLogs)
- [BusinessUnit_ImportMaps](#BKMK_BusinessUnit_ImportMaps)
- [BusinessUnit_Imports](#BKMK_BusinessUnit_Imports)
- [businessunit_mailboxtrackingfolder](#BKMK_businessunit_mailboxtrackingfolder)
- [businessunit_principalobjectattributeaccess](#BKMK_businessunit_principalobjectattributeaccess)
- [BusinessUnit_ProcessSessions](#BKMK_BusinessUnit_ProcessSessions)
- [BusinessUnit_SyncError](#BKMK_BusinessUnit_SyncError)
- [BusinessUnit_SyncErrors](#BKMK_BusinessUnit_SyncErrors)
- [chat_businessunit_owningbusinessunit](#BKMK_chat_businessunit_owningbusinessunit)
- [Owning_businessunit_processsessions](#BKMK_Owning_businessunit_processsessions)

### <a name="BKMK_adx_inviteredemption_businessunit_owningbusinessunit"></a> adx_inviteredemption_businessunit_owningbusinessunit

Many-To-One Relationship: [adx_inviteredemption adx_inviteredemption_businessunit_owningbusinessunit](adx_inviteredemption.md#BKMK_adx_inviteredemption_businessunit_owningbusinessunit)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_inviteredemption`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`adx_inviteredemption_businessunit_owningbusinessunit`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_adx_portalcomment_businessunit_owningbusinessunit"></a> adx_portalcomment_businessunit_owningbusinessunit

Many-To-One Relationship: [adx_portalcomment adx_portalcomment_businessunit_owningbusinessunit](adx_portalcomment.md#BKMK_adx_portalcomment_businessunit_owningbusinessunit)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_portalcomment`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`adx_portalcomment_businessunit_owningbusinessunit`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BulkDeleteOperation_BusinessUnit"></a> BulkDeleteOperation_BusinessUnit

Many-To-One Relationship: [bulkdeleteoperation BulkDeleteOperation_BusinessUnit](bulkdeleteoperation.md#BKMK_BulkDeleteOperation_BusinessUnit)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeleteoperation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BulkDeleteOperation_BusinessUnit`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_accounts"></a> business_unit_accounts

Many-To-One Relationship: [account business_unit_accounts](account.md#BKMK_business_unit_accounts)

|Property|Value|
|---|---|
|ReferencingEntity|`account`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_accounts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_actioncards"></a> business_unit_actioncards

Many-To-One Relationship: [actioncard business_unit_actioncards](actioncard.md#BKMK_business_unit_actioncards)

|Property|Value|
|---|---|
|ReferencingEntity|`actioncard`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_actioncards`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_activityfileattachment"></a> business_unit_activityfileattachment

Many-To-One Relationship: [activityfileattachment business_unit_activityfileattachment](activityfileattachment.md#BKMK_business_unit_activityfileattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`activityfileattachment`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_activityfileattachment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_activitypointer"></a> business_unit_activitypointer

Many-To-One Relationship: [activitypointer business_unit_activitypointer](activitypointer.md#BKMK_business_unit_activitypointer)

|Property|Value|
|---|---|
|ReferencingEntity|`activitypointer`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_activitypointer`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_adx_invitation"></a> business_unit_adx_invitation

Many-To-One Relationship: [adx_invitation business_unit_adx_invitation](adx_invitation.md#BKMK_business_unit_adx_invitation)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_invitation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_adx_invitation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_adx_setting"></a> business_unit_adx_setting

Many-To-One Relationship: [adx_setting business_unit_adx_setting](adx_setting.md#BKMK_business_unit_adx_setting)

|Property|Value|
|---|---|
|ReferencingEntity|`adx_setting`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_adx_setting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aiplugin"></a> business_unit_aiplugin

Many-To-One Relationship: [aiplugin business_unit_aiplugin](aiplugin.md#BKMK_business_unit_aiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugin`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aiplugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginauth"></a> business_unit_aipluginauth

Many-To-One Relationship: [aipluginauth business_unit_aipluginauth](aipluginauth.md#BKMK_business_unit_aipluginauth)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginauth`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginauth`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginconversationstarter"></a> business_unit_aipluginconversationstarter

Many-To-One Relationship: [aipluginconversationstarter business_unit_aipluginconversationstarter](aipluginconversationstarter.md#BKMK_business_unit_aipluginconversationstarter)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstarter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginconversationstarter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginconversationstartermapping"></a> business_unit_aipluginconversationstartermapping

Many-To-One Relationship: [aipluginconversationstartermapping business_unit_aipluginconversationstartermapping](aipluginconversationstartermapping.md#BKMK_business_unit_aipluginconversationstartermapping)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginconversationstartermapping`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginconversationstartermapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginexternalschema"></a> business_unit_aipluginexternalschema

Many-To-One Relationship: [aipluginexternalschema business_unit_aipluginexternalschema](aipluginexternalschema.md#BKMK_business_unit_aipluginexternalschema)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginexternalschema`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginexternalschema`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginexternalschemaproperty"></a> business_unit_aipluginexternalschemaproperty

Many-To-One Relationship: [aipluginexternalschemaproperty business_unit_aipluginexternalschemaproperty](aipluginexternalschemaproperty.md#BKMK_business_unit_aipluginexternalschemaproperty)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginexternalschemaproperty`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginexternalschemaproperty`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aiplugingovernance"></a> business_unit_aiplugingovernance

Many-To-One Relationship: [aiplugingovernance business_unit_aiplugingovernance](aiplugingovernance.md#BKMK_business_unit_aiplugingovernance)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernance`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aiplugingovernance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aiplugingovernanceext"></a> business_unit_aiplugingovernanceext

Many-To-One Relationship: [aiplugingovernanceext business_unit_aiplugingovernanceext](aiplugingovernanceext.md#BKMK_business_unit_aiplugingovernanceext)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugingovernanceext`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aiplugingovernanceext`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aiplugininstance"></a> business_unit_aiplugininstance

Many-To-One Relationship: [aiplugininstance business_unit_aiplugininstance](aiplugininstance.md#BKMK_business_unit_aiplugininstance)

|Property|Value|
|---|---|
|ReferencingEntity|`aiplugininstance`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aiplugininstance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginoperation"></a> business_unit_aipluginoperation

Many-To-One Relationship: [aipluginoperation business_unit_aipluginoperation](aipluginoperation.md#BKMK_business_unit_aipluginoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginoperation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginoperationparameter"></a> business_unit_aipluginoperationparameter

Many-To-One Relationship: [aipluginoperationparameter business_unit_aipluginoperationparameter](aipluginoperationparameter.md#BKMK_business_unit_aipluginoperationparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationparameter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginoperationparameter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginoperationresponsetemplate"></a> business_unit_aipluginoperationresponsetemplate

Many-To-One Relationship: [aipluginoperationresponsetemplate business_unit_aipluginoperationresponsetemplate](aipluginoperationresponsetemplate.md#BKMK_business_unit_aipluginoperationresponsetemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginoperationresponsetemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginoperationresponsetemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_aipluginusersetting"></a> business_unit_aipluginusersetting

Many-To-One Relationship: [aipluginusersetting business_unit_aipluginusersetting](aipluginusersetting.md#BKMK_business_unit_aipluginusersetting)

|Property|Value|
|---|---|
|ReferencingEntity|`aipluginusersetting`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_aipluginusersetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_annotations"></a> business_unit_annotations

Many-To-One Relationship: [annotation business_unit_annotations](annotation.md#BKMK_business_unit_annotations)

|Property|Value|
|---|---|
|ReferencingEntity|`annotation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_annotations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_applicationuser"></a> business_unit_applicationuser

Many-To-One Relationship: [applicationuser business_unit_applicationuser](applicationuser.md#BKMK_business_unit_applicationuser)

|Property|Value|
|---|---|
|ReferencingEntity|`applicationuser`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_applicationuser`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_appnotification"></a> business_unit_appnotification

Many-To-One Relationship: [appnotification business_unit_appnotification](appnotification.md#BKMK_business_unit_appnotification)

|Property|Value|
|---|---|
|ReferencingEntity|`appnotification`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_appnotification`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_appointment_activities"></a> business_unit_appointment_activities

Many-To-One Relationship: [appointment business_unit_appointment_activities](appointment.md#BKMK_business_unit_appointment_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`appointment`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_appointment_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_approvalprocess"></a> business_unit_approvalprocess

Many-To-One Relationship: [approvalprocess business_unit_approvalprocess](approvalprocess.md#BKMK_business_unit_approvalprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalprocess`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_approvalprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_approvalstageapproval"></a> business_unit_approvalstageapproval

Many-To-One Relationship: [approvalstageapproval business_unit_approvalstageapproval](approvalstageapproval.md#BKMK_business_unit_approvalstageapproval)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageapproval`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_approvalstageapproval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_approvalstagecondition"></a> business_unit_approvalstagecondition

Many-To-One Relationship: [approvalstagecondition business_unit_approvalstagecondition](approvalstagecondition.md#BKMK_business_unit_approvalstagecondition)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstagecondition`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_approvalstagecondition`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_approvalstageintelligent"></a> business_unit_approvalstageintelligent

Many-To-One Relationship: [approvalstageintelligent business_unit_approvalstageintelligent](approvalstageintelligent.md#BKMK_business_unit_approvalstageintelligent)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageintelligent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_approvalstageintelligent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_approvalstageorder"></a> business_unit_approvalstageorder

Many-To-One Relationship: [approvalstageorder business_unit_approvalstageorder](approvalstageorder.md#BKMK_business_unit_approvalstageorder)

|Property|Value|
|---|---|
|ReferencingEntity|`approvalstageorder`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_approvalstageorder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_asyncoperation"></a> business_unit_asyncoperation

Many-To-One Relationship: [asyncoperation business_unit_asyncoperation](asyncoperation.md#BKMK_business_unit_asyncoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_asyncoperation`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_bot"></a> business_unit_bot

Many-To-One Relationship: [bot business_unit_bot](bot.md#BKMK_business_unit_bot)

|Property|Value|
|---|---|
|ReferencingEntity|`bot`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_bot`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_botcomponent"></a> business_unit_botcomponent

Many-To-One Relationship: [botcomponent business_unit_botcomponent](botcomponent.md#BKMK_business_unit_botcomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_botcomponent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_botcomponentcollection"></a> business_unit_botcomponentcollection

Many-To-One Relationship: [botcomponentcollection business_unit_botcomponentcollection](botcomponentcollection.md#BKMK_business_unit_botcomponentcollection)

|Property|Value|
|---|---|
|ReferencingEntity|`botcomponentcollection`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_botcomponentcollection`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_businessprocess"></a> business_unit_businessprocess

Many-To-One Relationship: [businessprocess business_unit_businessprocess](businessprocess.md#BKMK_business_unit_businessprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`businessprocess`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_businessprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_calendars"></a> business_unit_calendars

Many-To-One Relationship: [calendar business_unit_calendars](calendar.md#BKMK_business_unit_calendars)

|Property|Value|
|---|---|
|ReferencingEntity|`calendar`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_calendars`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_card"></a> business_unit_card

Many-To-One Relationship: [card business_unit_card](card.md#BKMK_business_unit_card)

|Property|Value|
|---|---|
|ReferencingEntity|`card`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_card`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_category"></a> business_unit_category

Many-To-One Relationship: [category business_unit_category](category.md#BKMK_business_unit_category)

|Property|Value|
|---|---|
|ReferencingEntity|`category`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_category`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_certificatecredential"></a> business_unit_certificatecredential

Many-To-One Relationship: [certificatecredential business_unit_certificatecredential](certificatecredential.md#BKMK_business_unit_certificatecredential)

|Property|Value|
|---|---|
|ReferencingEntity|`certificatecredential`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_certificatecredential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_connectioninstance"></a> business_unit_connectioninstance

Many-To-One Relationship: [connectioninstance business_unit_connectioninstance](connectioninstance.md#BKMK_business_unit_connectioninstance)

|Property|Value|
|---|---|
|ReferencingEntity|`connectioninstance`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_connectioninstance`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_connectionreference"></a> business_unit_connectionreference

Many-To-One Relationship: [connectionreference business_unit_connectionreference](connectionreference.md#BKMK_business_unit_connectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`connectionreference`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_connectionreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_connections"></a> business_unit_connections

Many-To-One Relationship: [connection business_unit_connections](connection.md#BKMK_business_unit_connections)

|Property|Value|
|---|---|
|ReferencingEntity|`connection`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_connections`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_connector"></a> business_unit_connector

Many-To-One Relationship: [connector business_unit_connector](connector.md#BKMK_business_unit_connector)

|Property|Value|
|---|---|
|ReferencingEntity|`connector`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_connector`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_contacts"></a> business_unit_contacts

Many-To-One Relationship: [contact business_unit_contacts](contact.md#BKMK_business_unit_contacts)

|Property|Value|
|---|---|
|ReferencingEntity|`contact`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_contacts`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_conversationtranscript"></a> business_unit_conversationtranscript

Many-To-One Relationship: [conversationtranscript business_unit_conversationtranscript](conversationtranscript.md#BKMK_business_unit_conversationtranscript)

|Property|Value|
|---|---|
|ReferencingEntity|`conversationtranscript`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_conversationtranscript`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_copilotglossaryterm"></a> business_unit_copilotglossaryterm

Many-To-One Relationship: [copilotglossaryterm business_unit_copilotglossaryterm](copilotglossaryterm.md#BKMK_business_unit_copilotglossaryterm)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotglossaryterm`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_copilotglossaryterm`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_copilotsynonyms"></a> business_unit_copilotsynonyms

Many-To-One Relationship: [copilotsynonyms business_unit_copilotsynonyms](copilotsynonyms.md#BKMK_business_unit_copilotsynonyms)

|Property|Value|
|---|---|
|ReferencingEntity|`copilotsynonyms`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_copilotsynonyms`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_credential"></a> business_unit_credential

Many-To-One Relationship: [credential business_unit_credential](credential.md#BKMK_business_unit_credential)

|Property|Value|
|---|---|
|ReferencingEntity|`credential`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_credential`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_customapi"></a> business_unit_customapi

Many-To-One Relationship: [customapi business_unit_customapi](customapi.md#BKMK_business_unit_customapi)

|Property|Value|
|---|---|
|ReferencingEntity|`customapi`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_customapi`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_datalakefolder"></a> business_unit_datalakefolder

Many-To-One Relationship: [datalakefolder business_unit_datalakefolder](datalakefolder.md#BKMK_business_unit_datalakefolder)

|Property|Value|
|---|---|
|ReferencingEntity|`datalakefolder`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_datalakefolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_desktopflowbinary"></a> business_unit_desktopflowbinary

Many-To-One Relationship: [desktopflowbinary business_unit_desktopflowbinary](desktopflowbinary.md#BKMK_business_unit_desktopflowbinary)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowbinary`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_desktopflowbinary`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_desktopflowmodule"></a> business_unit_desktopflowmodule

Many-To-One Relationship: [desktopflowmodule business_unit_desktopflowmodule](desktopflowmodule.md#BKMK_business_unit_desktopflowmodule)

|Property|Value|
|---|---|
|ReferencingEntity|`desktopflowmodule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_desktopflowmodule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_dvfilesearch"></a> business_unit_dvfilesearch

Many-To-One Relationship: [dvfilesearch business_unit_dvfilesearch](dvfilesearch.md#BKMK_business_unit_dvfilesearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearch`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_dvfilesearch`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_dvfilesearchattribute"></a> business_unit_dvfilesearchattribute

Many-To-One Relationship: [dvfilesearchattribute business_unit_dvfilesearchattribute](dvfilesearchattribute.md#BKMK_business_unit_dvfilesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchattribute`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_dvfilesearchattribute`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_dvfilesearchentity"></a> business_unit_dvfilesearchentity

Many-To-One Relationship: [dvfilesearchentity business_unit_dvfilesearchentity](dvfilesearchentity.md#BKMK_business_unit_dvfilesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvfilesearchentity`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_dvfilesearchentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_dvtablesearch"></a> business_unit_dvtablesearch

Many-To-One Relationship: [dvtablesearch business_unit_dvtablesearch](dvtablesearch.md#BKMK_business_unit_dvtablesearch)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearch`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_dvtablesearch`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_dvtablesearchattribute"></a> business_unit_dvtablesearchattribute

Many-To-One Relationship: [dvtablesearchattribute business_unit_dvtablesearchattribute](dvtablesearchattribute.md#BKMK_business_unit_dvtablesearchattribute)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchattribute`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_dvtablesearchattribute`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_dvtablesearchentity"></a> business_unit_dvtablesearchentity

Many-To-One Relationship: [dvtablesearchentity business_unit_dvtablesearchentity](dvtablesearchentity.md#BKMK_business_unit_dvtablesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`dvtablesearchentity`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_dvtablesearchentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_email_activities"></a> business_unit_email_activities

Many-To-One Relationship: [email business_unit_email_activities](email.md#BKMK_business_unit_email_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`email`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_email_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_emailserverprofile"></a> business_unit_emailserverprofile

Many-To-One Relationship: [emailserverprofile business_unit_emailserverprofile](emailserverprofile.md#BKMK_business_unit_emailserverprofile)

|Property|Value|
|---|---|
|ReferencingEntity|`emailserverprofile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_emailserverprofile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_environmentvariabledefinition"></a> business_unit_environmentvariabledefinition

Many-To-One Relationship: [environmentvariabledefinition business_unit_environmentvariabledefinition](environmentvariabledefinition.md#BKMK_business_unit_environmentvariabledefinition)

|Property|Value|
|---|---|
|ReferencingEntity|`environmentvariabledefinition`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_environmentvariabledefinition`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_exchangesyncidmapping"></a> business_unit_exchangesyncidmapping

Many-To-One Relationship: [exchangesyncidmapping business_unit_exchangesyncidmapping](exchangesyncidmapping.md#BKMK_business_unit_exchangesyncidmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`exchangesyncidmapping`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_exchangesyncidmapping`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_exportedexcel"></a> business_unit_exportedexcel

Many-To-One Relationship: [exportedexcel business_unit_exportedexcel](exportedexcel.md#BKMK_business_unit_exportedexcel)

|Property|Value|
|---|---|
|ReferencingEntity|`exportedexcel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_exportedexcel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_exportsolutionupload"></a> business_unit_exportsolutionupload

Many-To-One Relationship: [exportsolutionupload business_unit_exportsolutionupload](exportsolutionupload.md#BKMK_business_unit_exportsolutionupload)

|Property|Value|
|---|---|
|ReferencingEntity|`exportsolutionupload`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_exportsolutionupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_fabricaiskill"></a> business_unit_fabricaiskill

Many-To-One Relationship: [fabricaiskill business_unit_fabricaiskill](fabricaiskill.md#BKMK_business_unit_fabricaiskill)

|Property|Value|
|---|---|
|ReferencingEntity|`fabricaiskill`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_fabricaiskill`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_fax_activities"></a> business_unit_fax_activities

Many-To-One Relationship: [fax business_unit_fax_activities](fax.md#BKMK_business_unit_fax_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`fax`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_fax_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_featurecontrolsetting"></a> business_unit_featurecontrolsetting

Many-To-One Relationship: [featurecontrolsetting business_unit_featurecontrolsetting](featurecontrolsetting.md#BKMK_business_unit_featurecontrolsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`featurecontrolsetting`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_featurecontrolsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_federatedknowledgeconfiguration"></a> business_unit_federatedknowledgeconfiguration

Many-To-One Relationship: [federatedknowledgeconfiguration business_unit_federatedknowledgeconfiguration](federatedknowledgeconfiguration.md#BKMK_business_unit_federatedknowledgeconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_federatedknowledgeconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_federatedknowledgeentityconfiguration"></a> business_unit_federatedknowledgeentityconfiguration

Many-To-One Relationship: [federatedknowledgeentityconfiguration business_unit_federatedknowledgeentityconfiguration](federatedknowledgeentityconfiguration.md#BKMK_business_unit_federatedknowledgeentityconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`federatedknowledgeentityconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_federatedknowledgeentityconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_feedback"></a> business_unit_feedback

Many-To-One Relationship: [feedback business_unit_feedback](feedback.md#BKMK_business_unit_feedback)

|Property|Value|
|---|---|
|ReferencingEntity|`feedback`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_feedback`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowaggregation"></a> business_unit_flowaggregation

Many-To-One Relationship: [flowaggregation business_unit_flowaggregation](flowaggregation.md#BKMK_business_unit_flowaggregation)

|Property|Value|
|---|---|
|ReferencingEntity|`flowaggregation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowaggregation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowcapacityassignment"></a> business_unit_flowcapacityassignment

Many-To-One Relationship: [flowcapacityassignment business_unit_flowcapacityassignment](flowcapacityassignment.md#BKMK_business_unit_flowcapacityassignment)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcapacityassignment`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowcapacityassignment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowcredentialapplication"></a> business_unit_flowcredentialapplication

Many-To-One Relationship: [flowcredentialapplication business_unit_flowcredentialapplication](flowcredentialapplication.md#BKMK_business_unit_flowcredentialapplication)

|Property|Value|
|---|---|
|ReferencingEntity|`flowcredentialapplication`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowcredentialapplication`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowevent"></a> business_unit_flowevent

Many-To-One Relationship: [flowevent business_unit_flowevent](flowevent.md#BKMK_business_unit_flowevent)

|Property|Value|
|---|---|
|ReferencingEntity|`flowevent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowevent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowmachine"></a> business_unit_flowmachine

Many-To-One Relationship: [flowmachine business_unit_flowmachine](flowmachine.md#BKMK_business_unit_flowmachine)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachine`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowmachine`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowmachinegroup"></a> business_unit_flowmachinegroup

Many-To-One Relationship: [flowmachinegroup business_unit_flowmachinegroup](flowmachinegroup.md#BKMK_business_unit_flowmachinegroup)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinegroup`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowmachinegroup`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowmachineimage"></a> business_unit_flowmachineimage

Many-To-One Relationship: [flowmachineimage business_unit_flowmachineimage](flowmachineimage.md#BKMK_business_unit_flowmachineimage)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimage`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowmachineimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowmachineimageversion"></a> business_unit_flowmachineimageversion

Many-To-One Relationship: [flowmachineimageversion business_unit_flowmachineimageversion](flowmachineimageversion.md#BKMK_business_unit_flowmachineimageversion)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachineimageversion`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowmachineimageversion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowmachinenetwork"></a> business_unit_flowmachinenetwork

Many-To-One Relationship: [flowmachinenetwork business_unit_flowmachinenetwork](flowmachinenetwork.md#BKMK_business_unit_flowmachinenetwork)

|Property|Value|
|---|---|
|ReferencingEntity|`flowmachinenetwork`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowmachinenetwork`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowrun"></a> business_unit_flowrun

Many-To-One Relationship: [flowrun business_unit_flowrun](flowrun.md#BKMK_business_unit_flowrun)

|Property|Value|
|---|---|
|ReferencingEntity|`flowrun`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_flowsession"></a> business_unit_flowsession

Many-To-One Relationship: [flowsession business_unit_flowsession](flowsession.md#BKMK_business_unit_flowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`flowsession`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_flowsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_fxexpression"></a> business_unit_fxexpression

Many-To-One Relationship: [fxexpression business_unit_fxexpression](fxexpression.md#BKMK_business_unit_fxexpression)

|Property|Value|
|---|---|
|ReferencingEntity|`fxexpression`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_fxexpression`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_goal"></a> business_unit_goal

Many-To-One Relationship: [goal business_unit_goal](goal.md#BKMK_business_unit_goal)

|Property|Value|
|---|---|
|ReferencingEntity|`goal`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_goal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_goalrollupquery"></a> business_unit_goalrollupquery

Many-To-One Relationship: [goalrollupquery business_unit_goalrollupquery](goalrollupquery.md#BKMK_business_unit_goalrollupquery)

|Property|Value|
|---|---|
|ReferencingEntity|`goalrollupquery`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_goalrollupquery`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_governanceconfiguration"></a> business_unit_governanceconfiguration

Many-To-One Relationship: [governanceconfiguration business_unit_governanceconfiguration](governanceconfiguration.md#BKMK_business_unit_governanceconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`governanceconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_governanceconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_indexedtrait"></a> business_unit_indexedtrait

Many-To-One Relationship: [indexedtrait business_unit_indexedtrait](indexedtrait.md#BKMK_business_unit_indexedtrait)

|Property|Value|
|---|---|
|ReferencingEntity|`indexedtrait`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_indexedtrait`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_interactionforemail"></a> business_unit_interactionforemail

Many-To-One Relationship: [interactionforemail business_unit_interactionforemail](interactionforemail.md#BKMK_business_unit_interactionforemail)

|Property|Value|
|---|---|
|ReferencingEntity|`interactionforemail`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_new_interactionforemail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_keyvaultreference"></a> business_unit_keyvaultreference

Many-To-One Relationship: [keyvaultreference business_unit_keyvaultreference](keyvaultreference.md#BKMK_business_unit_keyvaultreference)

|Property|Value|
|---|---|
|ReferencingEntity|`keyvaultreference`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_keyvaultreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_knowledgearticle"></a> business_unit_knowledgearticle

Many-To-One Relationship: [knowledgearticle business_unit_knowledgearticle](knowledgearticle.md#BKMK_business_unit_knowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgearticle`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_knowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_knowledgefaq"></a> business_unit_knowledgefaq

Many-To-One Relationship: [knowledgefaq business_unit_knowledgefaq](knowledgefaq.md#BKMK_business_unit_knowledgefaq)

|Property|Value|
|---|---|
|ReferencingEntity|`knowledgefaq`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_knowledgefaq`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_letter_activities"></a> business_unit_letter_activities

Many-To-One Relationship: [letter business_unit_letter_activities](letter.md#BKMK_business_unit_letter_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`letter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_letter_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_mailbox"></a> business_unit_mailbox

Many-To-One Relationship: [mailbox business_unit_mailbox](mailbox.md#BKMK_business_unit_mailbox)

|Property|Value|
|---|---|
|ReferencingEntity|`mailbox`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_mailbox`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_mailmergetemplates"></a> business_unit_mailmergetemplates

Many-To-One Relationship: [mailmergetemplate business_unit_mailmergetemplates](mailmergetemplate.md#BKMK_business_unit_mailmergetemplates)

|Property|Value|
|---|---|
|ReferencingEntity|`mailmergetemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_mailmergetemplates`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_managedidentity"></a> business_unit_managedidentity

Many-To-One Relationship: [managedidentity business_unit_managedidentity](managedidentity.md#BKMK_business_unit_managedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`managedidentity`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_managedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibdataset"></a> business_unit_msdyn_aibdataset

Many-To-One Relationship: [msdyn_aibdataset business_unit_msdyn_aibdataset](msdyn_aibdataset.md#BKMK_business_unit_msdyn_aibdataset)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdataset`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibdataset`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibdatasetfile"></a> business_unit_msdyn_aibdatasetfile

Many-To-One Relationship: [msdyn_aibdatasetfile business_unit_msdyn_aibdatasetfile](msdyn_aibdatasetfile.md#BKMK_business_unit_msdyn_aibdatasetfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetfile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibdatasetfile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibdatasetrecord"></a> business_unit_msdyn_aibdatasetrecord

Many-To-One Relationship: [msdyn_aibdatasetrecord business_unit_msdyn_aibdatasetrecord](msdyn_aibdatasetrecord.md#BKMK_business_unit_msdyn_aibdatasetrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetrecord`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibdatasetrecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibdatasetscontainer"></a> business_unit_msdyn_aibdatasetscontainer

Many-To-One Relationship: [msdyn_aibdatasetscontainer business_unit_msdyn_aibdatasetscontainer](msdyn_aibdatasetscontainer.md#BKMK_business_unit_msdyn_aibdatasetscontainer)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibdatasetscontainer`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibdatasetscontainer`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibfeedbackloop"></a> business_unit_msdyn_aibfeedbackloop

Many-To-One Relationship: [msdyn_aibfeedbackloop business_unit_msdyn_aibfeedbackloop](msdyn_aibfeedbackloop.md#BKMK_business_unit_msdyn_aibfeedbackloop)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfeedbackloop`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibfeedbackloop`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibfile"></a> business_unit_msdyn_aibfile

Many-To-One Relationship: [msdyn_aibfile business_unit_msdyn_aibfile](msdyn_aibfile.md#BKMK_business_unit_msdyn_aibfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibfile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aibfileattacheddata"></a> business_unit_msdyn_aibfileattacheddata

Many-To-One Relationship: [msdyn_aibfileattacheddata business_unit_msdyn_aibfileattacheddata](msdyn_aibfileattacheddata.md#BKMK_business_unit_msdyn_aibfileattacheddata)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aibfileattacheddata`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aibfileattacheddata`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aidataprocessingevent"></a> business_unit_msdyn_aidataprocessingevent

Many-To-One Relationship: [msdyn_aidataprocessingevent business_unit_msdyn_aidataprocessingevent](msdyn_aidataprocessingevent.md#BKMK_business_unit_msdyn_aidataprocessingevent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aidataprocessingevent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aidataprocessingevent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aidocumenttemplate"></a> business_unit_msdyn_aidocumenttemplate

Many-To-One Relationship: [msdyn_aidocumenttemplate business_unit_msdyn_aidocumenttemplate](msdyn_aidocumenttemplate.md#BKMK_business_unit_msdyn_aidocumenttemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aidocumenttemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aidocumenttemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aievaluationconfiguration"></a> business_unit_msdyn_aievaluationconfiguration

Many-To-One Relationship: [msdyn_aievaluationconfiguration business_unit_msdyn_aievaluationconfiguration](msdyn_aievaluationconfiguration.md#BKMK_business_unit_msdyn_aievaluationconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievaluationconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aievaluationconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aievaluationrun"></a> business_unit_msdyn_aievaluationrun

Many-To-One Relationship: [msdyn_aievaluationrun business_unit_msdyn_aievaluationrun](msdyn_aievaluationrun.md#BKMK_business_unit_msdyn_aievaluationrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievaluationrun`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aievaluationrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aievent"></a> business_unit_msdyn_aievent

Many-To-One Relationship: [msdyn_aievent business_unit_msdyn_aievent](msdyn_aievent.md#BKMK_business_unit_msdyn_aievent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aievent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aievent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aifptrainingdocument"></a> business_unit_msdyn_aifptrainingdocument

Many-To-One Relationship: [msdyn_aifptrainingdocument business_unit_msdyn_aifptrainingdocument](msdyn_aifptrainingdocument.md#BKMK_business_unit_msdyn_aifptrainingdocument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aifptrainingdocument`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aifptrainingdocument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aimodel"></a> business_unit_msdyn_aimodel

Many-To-One Relationship: [msdyn_aimodel business_unit_msdyn_aimodel](msdyn_aimodel.md#BKMK_business_unit_msdyn_aimodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aimodel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aimodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aiodimage"></a> business_unit_msdyn_aiodimage

Many-To-One Relationship: [msdyn_aiodimage business_unit_msdyn_aiodimage](msdyn_aiodimage.md#BKMK_business_unit_msdyn_aiodimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodimage`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aiodimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aiodlabel"></a> business_unit_msdyn_aiodlabel

Many-To-One Relationship: [msdyn_aiodlabel business_unit_msdyn_aiodlabel](msdyn_aiodlabel.md#BKMK_business_unit_msdyn_aiodlabel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodlabel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aiodlabel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aiodtrainingboundingbox"></a> business_unit_msdyn_aiodtrainingboundingbox

Many-To-One Relationship: [msdyn_aiodtrainingboundingbox business_unit_msdyn_aiodtrainingboundingbox](msdyn_aiodtrainingboundingbox.md#BKMK_business_unit_msdyn_aiodtrainingboundingbox)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingboundingbox`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aiodtrainingboundingbox`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aiodtrainingimage"></a> business_unit_msdyn_aiodtrainingimage

Many-To-One Relationship: [msdyn_aiodtrainingimage business_unit_msdyn_aiodtrainingimage](msdyn_aiodtrainingimage.md#BKMK_business_unit_msdyn_aiodtrainingimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aiodtrainingimage`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aiodtrainingimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aitemplate"></a> business_unit_msdyn_aitemplate

Many-To-One Relationship: [msdyn_aitemplate business_unit_msdyn_aitemplate](msdyn_aitemplate.md#BKMK_business_unit_msdyn_aitemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aitemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aitestcase"></a> business_unit_msdyn_aitestcase

Many-To-One Relationship: [msdyn_aitestcase business_unit_msdyn_aitestcase](msdyn_aitestcase.md#BKMK_business_unit_msdyn_aitestcase)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcase`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aitestcase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aitestcasedocument"></a> business_unit_msdyn_aitestcasedocument

Many-To-One Relationship: [msdyn_aitestcasedocument business_unit_msdyn_aitestcasedocument](msdyn_aitestcasedocument.md#BKMK_business_unit_msdyn_aitestcasedocument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcasedocument`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aitestcasedocument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aitestcaseinput"></a> business_unit_msdyn_aitestcaseinput

Many-To-One Relationship: [msdyn_aitestcaseinput business_unit_msdyn_aitestcaseinput](msdyn_aitestcaseinput.md#BKMK_business_unit_msdyn_aitestcaseinput)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestcaseinput`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aitestcaseinput`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aitestrun"></a> business_unit_msdyn_aitestrun

Many-To-One Relationship: [msdyn_aitestrun business_unit_msdyn_aitestrun](msdyn_aitestrun.md#BKMK_business_unit_msdyn_aitestrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestrun`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aitestrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_aitestrunbatch"></a> business_unit_msdyn_aitestrunbatch

Many-To-One Relationship: [msdyn_aitestrunbatch business_unit_msdyn_aitestrunbatch](msdyn_aitestrunbatch.md#BKMK_business_unit_msdyn_aitestrunbatch)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_aitestrunbatch`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_aitestrunbatch`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_analysiscomponent"></a> business_unit_msdyn_analysiscomponent

Many-To-One Relationship: [msdyn_analysiscomponent business_unit_msdyn_analysiscomponent](msdyn_analysiscomponent.md#BKMK_business_unit_msdyn_analysiscomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysiscomponent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_analysiscomponent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_analysisjob"></a> business_unit_msdyn_analysisjob

Many-To-One Relationship: [msdyn_analysisjob business_unit_msdyn_analysisjob](msdyn_analysisjob.md#BKMK_business_unit_msdyn_analysisjob)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisjob`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_analysisjob`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_analysisoverride"></a> business_unit_msdyn_analysisoverride

Many-To-One Relationship: [msdyn_analysisoverride business_unit_msdyn_analysisoverride](msdyn_analysisoverride.md#BKMK_business_unit_msdyn_analysisoverride)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisoverride`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_analysisoverride`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_analysisresult"></a> business_unit_msdyn_analysisresult

Many-To-One Relationship: [msdyn_analysisresult business_unit_msdyn_analysisresult](msdyn_analysisresult.md#BKMK_business_unit_msdyn_analysisresult)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresult`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_analysisresult`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_analysisresultdetail"></a> business_unit_msdyn_analysisresultdetail

Many-To-One Relationship: [msdyn_analysisresultdetail business_unit_msdyn_analysisresultdetail](msdyn_analysisresultdetail.md#BKMK_business_unit_msdyn_analysisresultdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_analysisresultdetail`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_analysisresultdetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_copilotinteractions"></a> business_unit_msdyn_copilotinteractions

Many-To-One Relationship: [msdyn_copilotinteractions business_unit_msdyn_copilotinteractions](msdyn_copilotinteractions.md#BKMK_business_unit_msdyn_copilotinteractions)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_copilotinteractions`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_copilotinteractions`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_customcontrolextendedsettings"></a> business_unit_msdyn_customcontrolextendedsettings

Many-To-One Relationship: [msdyn_customcontrolextendedsettings business_unit_msdyn_customcontrolextendedsettings](msdyn_customcontrolextendedsettings.md#BKMK_business_unit_msdyn_customcontrolextendedsettings)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_customcontrolextendedsettings`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_customcontrolextendedsettings`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dataflow"></a> business_unit_msdyn_dataflow

Many-To-One Relationship: [msdyn_dataflow business_unit_msdyn_dataflow](msdyn_dataflow.md#BKMK_business_unit_msdyn_dataflow)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dataflow`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dataflow_datalakefolder"></a> business_unit_msdyn_dataflow_datalakefolder

Many-To-One Relationship: [msdyn_dataflow_datalakefolder business_unit_msdyn_dataflow_datalakefolder](msdyn_dataflow_datalakefolder.md#BKMK_business_unit_msdyn_dataflow_datalakefolder)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflow_datalakefolder`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dataflow_datalakefolder`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dataflowconnectionreference"></a> business_unit_msdyn_dataflowconnectionreference

Many-To-One Relationship: [msdyn_dataflowconnectionreference business_unit_msdyn_dataflowconnectionreference](msdyn_dataflowconnectionreference.md#BKMK_business_unit_msdyn_dataflowconnectionreference)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowconnectionreference`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dataflowconnectionreference`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dataflowrefreshhistory"></a> business_unit_msdyn_dataflowrefreshhistory

Many-To-One Relationship: [msdyn_dataflowrefreshhistory business_unit_msdyn_dataflowrefreshhistory](msdyn_dataflowrefreshhistory.md#BKMK_business_unit_msdyn_dataflowrefreshhistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowrefreshhistory`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dataflowrefreshhistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dataflowtemplate"></a> business_unit_msdyn_dataflowtemplate

Many-To-One Relationship: [msdyn_dataflowtemplate business_unit_msdyn_dataflowtemplate](msdyn_dataflowtemplate.md#BKMK_business_unit_msdyn_dataflowtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dataflowtemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dataflowtemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dmsrequest"></a> business_unit_msdyn_dmsrequest

Many-To-One Relationship: [msdyn_dmsrequest business_unit_msdyn_dmsrequest](msdyn_dmsrequest.md#BKMK_business_unit_msdyn_dmsrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmsrequest`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dmsrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dmsrequeststatus"></a> business_unit_msdyn_dmsrequeststatus

Many-To-One Relationship: [msdyn_dmsrequeststatus business_unit_msdyn_dmsrequeststatus](msdyn_dmsrequeststatus.md#BKMK_business_unit_msdyn_dmsrequeststatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmsrequeststatus`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dmsrequeststatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dmssyncrequest"></a> business_unit_msdyn_dmssyncrequest

Many-To-One Relationship: [msdyn_dmssyncrequest business_unit_msdyn_dmssyncrequest](msdyn_dmssyncrequest.md#BKMK_business_unit_msdyn_dmssyncrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmssyncrequest`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dmssyncrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_dmssyncstatus"></a> business_unit_msdyn_dmssyncstatus

Many-To-One Relationship: [msdyn_dmssyncstatus business_unit_msdyn_dmssyncstatus](msdyn_dmssyncstatus.md#BKMK_business_unit_msdyn_dmssyncstatus)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_dmssyncstatus`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_dmssyncstatus`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_entitylinkchatconfiguration"></a> business_unit_msdyn_entitylinkchatconfiguration

Many-To-One Relationship: [msdyn_entitylinkchatconfiguration business_unit_msdyn_entitylinkchatconfiguration](msdyn_entitylinkchatconfiguration.md#BKMK_business_unit_msdyn_entitylinkchatconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entitylinkchatconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_entitylinkchatconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_entityrefreshhistory"></a> business_unit_msdyn_entityrefreshhistory

Many-To-One Relationship: [msdyn_entityrefreshhistory business_unit_msdyn_entityrefreshhistory](msdyn_entityrefreshhistory.md#BKMK_business_unit_msdyn_entityrefreshhistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_entityrefreshhistory`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_entityrefreshhistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_favoriteknowledgearticle"></a> business_unit_msdyn_favoriteknowledgearticle

Many-To-One Relationship: [msdyn_favoriteknowledgearticle business_unit_msdyn_favoriteknowledgearticle](msdyn_favoriteknowledgearticle.md#BKMK_business_unit_msdyn_favoriteknowledgearticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_favoriteknowledgearticle`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_favoriteknowledgearticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_federatedarticle"></a> business_unit_msdyn_federatedarticle

Many-To-One Relationship: [msdyn_federatedarticle business_unit_msdyn_federatedarticle](msdyn_federatedarticle.md#BKMK_business_unit_msdyn_federatedarticle)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_federatedarticle`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_federatedarticle`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_fileupload"></a> business_unit_msdyn_fileupload

Many-To-One Relationship: [msdyn_fileupload business_unit_msdyn_fileupload](msdyn_fileupload.md#BKMK_business_unit_msdyn_fileupload)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_fileupload`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_fileupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_actionapprovalmodel"></a> business_unit_msdyn_flow_actionapprovalmodel

Many-To-One Relationship: [msdyn_flow_actionapprovalmodel business_unit_msdyn_flow_actionapprovalmodel](msdyn_flow_actionapprovalmodel.md#BKMK_business_unit_msdyn_flow_actionapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_actionapprovalmodel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_actionapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_approval"></a> business_unit_msdyn_flow_approval

Many-To-One Relationship: [msdyn_flow_approval business_unit_msdyn_flow_approval](msdyn_flow_approval.md#BKMK_business_unit_msdyn_flow_approval)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approval`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_approval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_approvalrequest"></a> business_unit_msdyn_flow_approvalrequest

Many-To-One Relationship: [msdyn_flow_approvalrequest business_unit_msdyn_flow_approvalrequest](msdyn_flow_approvalrequest.md#BKMK_business_unit_msdyn_flow_approvalrequest)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalrequest`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_approvalrequest`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_approvalresponse"></a> business_unit_msdyn_flow_approvalresponse

Many-To-One Relationship: [msdyn_flow_approvalresponse business_unit_msdyn_flow_approvalresponse](msdyn_flow_approvalresponse.md#BKMK_business_unit_msdyn_flow_approvalresponse)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalresponse`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_approvalresponse`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_approvalstep"></a> business_unit_msdyn_flow_approvalstep

Many-To-One Relationship: [msdyn_flow_approvalstep business_unit_msdyn_flow_approvalstep](msdyn_flow_approvalstep.md#BKMK_business_unit_msdyn_flow_approvalstep)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_approvalstep`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_approvalstep`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_awaitallactionapprovalmodel"></a> business_unit_msdyn_flow_awaitallactionapprovalmodel

Many-To-One Relationship: [msdyn_flow_awaitallactionapprovalmodel business_unit_msdyn_flow_awaitallactionapprovalmodel](msdyn_flow_awaitallactionapprovalmodel.md#BKMK_business_unit_msdyn_flow_awaitallactionapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_awaitallactionapprovalmodel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_awaitallactionapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_awaitallapprovalmodel"></a> business_unit_msdyn_flow_awaitallapprovalmodel

Many-To-One Relationship: [msdyn_flow_awaitallapprovalmodel business_unit_msdyn_flow_awaitallapprovalmodel](msdyn_flow_awaitallapprovalmodel.md#BKMK_business_unit_msdyn_flow_awaitallapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_awaitallapprovalmodel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_awaitallapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_basicapprovalmodel"></a> business_unit_msdyn_flow_basicapprovalmodel

Many-To-One Relationship: [msdyn_flow_basicapprovalmodel business_unit_msdyn_flow_basicapprovalmodel](msdyn_flow_basicapprovalmodel.md#BKMK_business_unit_msdyn_flow_basicapprovalmodel)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_basicapprovalmodel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_basicapprovalmodel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_flow_flowapproval"></a> business_unit_msdyn_flow_flowapproval

Many-To-One Relationship: [msdyn_flow_flowapproval business_unit_msdyn_flow_flowapproval](msdyn_flow_flowapproval.md#BKMK_business_unit_msdyn_flow_flowapproval)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_flow_flowapproval`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_flow_flowapproval`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_formmapping"></a> business_unit_msdyn_formmapping

Many-To-One Relationship: [msdyn_formmapping business_unit_msdyn_formmapping](msdyn_formmapping.md#BKMK_business_unit_msdyn_formmapping)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_formmapping`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_formmapping`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_function"></a> business_unit_msdyn_function

Many-To-One Relationship: [msdyn_function business_unit_msdyn_function](msdyn_function.md#BKMK_business_unit_msdyn_function)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_function`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_function`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_historicalcaseharvestbatch"></a> business_unit_msdyn_historicalcaseharvestbatch

Many-To-One Relationship: [msdyn_historicalcaseharvestbatch business_unit_msdyn_historicalcaseharvestbatch](msdyn_historicalcaseharvestbatch.md#BKMK_business_unit_msdyn_historicalcaseharvestbatch)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_historicalcaseharvestbatch`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_historicalcaseharvestbatch`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_historicalcaseharvestrun"></a> business_unit_msdyn_historicalcaseharvestrun

Many-To-One Relationship: [msdyn_historicalcaseharvestrun business_unit_msdyn_historicalcaseharvestrun](msdyn_historicalcaseharvestrun.md#BKMK_business_unit_msdyn_historicalcaseharvestrun)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_historicalcaseharvestrun`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_historicalcaseharvestrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_integratedsearchprovider"></a> business_unit_msdyn_integratedsearchprovider

Many-To-One Relationship: [msdyn_integratedsearchprovider business_unit_msdyn_integratedsearchprovider](msdyn_integratedsearchprovider.md#BKMK_business_unit_msdyn_integratedsearchprovider)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_integratedsearchprovider`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_integratedsearchprovider`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_kalanguagesetting"></a> business_unit_msdyn_kalanguagesetting

Many-To-One Relationship: [msdyn_kalanguagesetting business_unit_msdyn_kalanguagesetting](msdyn_kalanguagesetting.md#BKMK_business_unit_msdyn_kalanguagesetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kalanguagesetting`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_kalanguagesetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_kbattachment"></a> business_unit_msdyn_kbattachment

Many-To-One Relationship: [msdyn_kbattachment business_unit_msdyn_kbattachment](msdyn_kbattachment.md#BKMK_business_unit_msdyn_kbattachment)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kbattachment`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_kbattachment`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_kmfederatedsearchconfig"></a> business_unit_msdyn_kmfederatedsearchconfig

Many-To-One Relationship: [msdyn_kmfederatedsearchconfig business_unit_msdyn_kmfederatedsearchconfig](msdyn_kmfederatedsearchconfig.md#BKMK_business_unit_msdyn_kmfederatedsearchconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_kmfederatedsearchconfig`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_kmfederatedsearchconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgearticleimage"></a> business_unit_msdyn_knowledgearticleimage

Many-To-One Relationship: [msdyn_knowledgearticleimage business_unit_msdyn_knowledgearticleimage](msdyn_knowledgearticleimage.md#BKMK_business_unit_msdyn_knowledgearticleimage)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticleimage`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgearticleimage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgearticletemplate"></a> business_unit_msdyn_knowledgearticletemplate

Many-To-One Relationship: [msdyn_knowledgearticletemplate business_unit_msdyn_knowledgearticletemplate](msdyn_knowledgearticletemplate.md#BKMK_business_unit_msdyn_knowledgearticletemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgearticletemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgearticletemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgeassetconfiguration"></a> business_unit_msdyn_knowledgeassetconfiguration

Many-To-One Relationship: [msdyn_knowledgeassetconfiguration business_unit_msdyn_knowledgeassetconfiguration](msdyn_knowledgeassetconfiguration.md#BKMK_business_unit_msdyn_knowledgeassetconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeassetconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgeassetconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgeharvestjobrecord"></a> business_unit_msdyn_knowledgeharvestjobrecord

Many-To-One Relationship: [msdyn_knowledgeharvestjobrecord business_unit_msdyn_knowledgeharvestjobrecord](msdyn_knowledgeharvestjobrecord.md#BKMK_business_unit_msdyn_knowledgeharvestjobrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeharvestjobrecord`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgeharvestjobrecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgeinteractioninsight"></a> business_unit_msdyn_knowledgeinteractioninsight

Many-To-One Relationship: [msdyn_knowledgeinteractioninsight business_unit_msdyn_knowledgeinteractioninsight](msdyn_knowledgeinteractioninsight.md#BKMK_business_unit_msdyn_knowledgeinteractioninsight)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgeinteractioninsight`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgeinteractioninsight`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgemanagementsetting"></a> business_unit_msdyn_knowledgemanagementsetting

Many-To-One Relationship: [msdyn_knowledgemanagementsetting business_unit_msdyn_knowledgemanagementsetting](msdyn_knowledgemanagementsetting.md#BKMK_business_unit_msdyn_knowledgemanagementsetting)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgemanagementsetting`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgemanagementsetting`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgepersonalfilter"></a> business_unit_msdyn_knowledgepersonalfilter

Many-To-One Relationship: [msdyn_knowledgepersonalfilter business_unit_msdyn_knowledgepersonalfilter](msdyn_knowledgepersonalfilter.md#BKMK_business_unit_msdyn_knowledgepersonalfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgepersonalfilter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgepersonalfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgesearchfilter"></a> business_unit_msdyn_knowledgesearchfilter

Many-To-One Relationship: [msdyn_knowledgesearchfilter business_unit_msdyn_knowledgesearchfilter](msdyn_knowledgesearchfilter.md#BKMK_business_unit_msdyn_knowledgesearchfilter)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgesearchfilter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgesearchfilter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_knowledgesearchinsight"></a> business_unit_msdyn_knowledgesearchinsight

Many-To-One Relationship: [msdyn_knowledgesearchinsight business_unit_msdyn_knowledgesearchinsight](msdyn_knowledgesearchinsight.md#BKMK_business_unit_msdyn_knowledgesearchinsight)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_knowledgesearchinsight`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_knowledgesearchinsight`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_mobileapp"></a> business_unit_msdyn_mobileapp

Many-To-One Relationship: [msdyn_mobileapp business_unit_msdyn_mobileapp](msdyn_mobileapp.md#BKMK_business_unit_msdyn_mobileapp)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_mobileapp`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_mobileapp`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmanalysishistory"></a> business_unit_msdyn_pmanalysishistory

Many-To-One Relationship: [msdyn_pmanalysishistory business_unit_msdyn_pmanalysishistory](msdyn_pmanalysishistory.md#BKMK_business_unit_msdyn_pmanalysishistory)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmanalysishistory`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmanalysishistory`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmbusinessruleautomationconfig"></a> business_unit_msdyn_pmbusinessruleautomationconfig

Many-To-One Relationship: [msdyn_pmbusinessruleautomationconfig business_unit_msdyn_pmbusinessruleautomationconfig](msdyn_pmbusinessruleautomationconfig.md#BKMK_business_unit_msdyn_pmbusinessruleautomationconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmbusinessruleautomationconfig`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmbusinessruleautomationconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmcalendar"></a> business_unit_msdyn_pmcalendar

Many-To-One Relationship: [msdyn_pmcalendar business_unit_msdyn_pmcalendar](msdyn_pmcalendar.md#BKMK_business_unit_msdyn_pmcalendar)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmcalendar`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmcalendar`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmcalendarversion"></a> business_unit_msdyn_pmcalendarversion

Many-To-One Relationship: [msdyn_pmcalendarversion business_unit_msdyn_pmcalendarversion](msdyn_pmcalendarversion.md#BKMK_business_unit_msdyn_pmcalendarversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmcalendarversion`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmcalendarversion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pminferredtask"></a> business_unit_msdyn_pminferredtask

Many-To-One Relationship: [msdyn_pminferredtask business_unit_msdyn_pminferredtask](msdyn_pminferredtask.md#BKMK_business_unit_msdyn_pminferredtask)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pminferredtask`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pminferredtask`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmprocessextendedmetadataversion"></a> business_unit_msdyn_pmprocessextendedmetadataversion

Many-To-One Relationship: [msdyn_pmprocessextendedmetadataversion business_unit_msdyn_pmprocessextendedmetadataversion](msdyn_pmprocessextendedmetadataversion.md#BKMK_business_unit_msdyn_pmprocessextendedmetadataversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessextendedmetadataversion`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmprocessextendedmetadataversion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmprocesstemplate"></a> business_unit_msdyn_pmprocesstemplate

Many-To-One Relationship: [msdyn_pmprocesstemplate business_unit_msdyn_pmprocesstemplate](msdyn_pmprocesstemplate.md#BKMK_business_unit_msdyn_pmprocesstemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocesstemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmprocesstemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmprocessusersettings"></a> business_unit_msdyn_pmprocessusersettings

Many-To-One Relationship: [msdyn_pmprocessusersettings business_unit_msdyn_pmprocessusersettings](msdyn_pmprocessusersettings.md#BKMK_business_unit_msdyn_pmprocessusersettings)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessusersettings`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmprocessusersettings`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmprocessversion"></a> business_unit_msdyn_pmprocessversion

Many-To-One Relationship: [msdyn_pmprocessversion business_unit_msdyn_pmprocessversion](msdyn_pmprocessversion.md#BKMK_business_unit_msdyn_pmprocessversion)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmprocessversion`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmprocessversion`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmrecording"></a> business_unit_msdyn_pmrecording

Many-To-One Relationship: [msdyn_pmrecording business_unit_msdyn_pmrecording](msdyn_pmrecording.md#BKMK_business_unit_msdyn_pmrecording)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmrecording`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmrecording`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmsimulation"></a> business_unit_msdyn_pmsimulation

Many-To-One Relationship: [msdyn_pmsimulation business_unit_msdyn_pmsimulation](msdyn_pmsimulation.md#BKMK_business_unit_msdyn_pmsimulation)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmsimulation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmsimulation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmtemplate"></a> business_unit_msdyn_pmtemplate

Many-To-One Relationship: [msdyn_pmtemplate business_unit_msdyn_pmtemplate](msdyn_pmtemplate.md#BKMK_business_unit_msdyn_pmtemplate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmtemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmtemplate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_pmview"></a> business_unit_msdyn_pmview

Many-To-One Relationship: [msdyn_pmview business_unit_msdyn_pmview](msdyn_pmview.md#BKMK_business_unit_msdyn_pmview)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_pmview`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_pmview`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_qna"></a> business_unit_msdyn_qna

Many-To-One Relationship: [msdyn_qna business_unit_msdyn_qna](msdyn_qna.md#BKMK_business_unit_msdyn_qna)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_qna`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_qna`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_richtextfile"></a> business_unit_msdyn_richtextfile

Many-To-One Relationship: [msdyn_richtextfile business_unit_msdyn_richtextfile](msdyn_richtextfile.md#BKMK_business_unit_msdyn_richtextfile)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_richtextfile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_richtextfile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_salesforcestructuredobject"></a> business_unit_msdyn_salesforcestructuredobject

Many-To-One Relationship: [msdyn_salesforcestructuredobject business_unit_msdyn_salesforcestructuredobject](msdyn_salesforcestructuredobject.md#BKMK_business_unit_msdyn_salesforcestructuredobject)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_salesforcestructuredobject`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_salesforcestructuredobject`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_salesforcestructuredqnaconfig"></a> business_unit_msdyn_salesforcestructuredqnaconfig

Many-To-One Relationship: [msdyn_salesforcestructuredqnaconfig business_unit_msdyn_salesforcestructuredqnaconfig](msdyn_salesforcestructuredqnaconfig.md#BKMK_business_unit_msdyn_salesforcestructuredqnaconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_salesforcestructuredqnaconfig`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_salesforcestructuredqnaconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_schedule"></a> business_unit_msdyn_schedule

Many-To-One Relationship: [msdyn_schedule business_unit_msdyn_schedule](msdyn_schedule.md#BKMK_business_unit_msdyn_schedule)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_schedule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_schedule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_serviceconfiguration"></a> business_unit_msdyn_serviceconfiguration

Many-To-One Relationship: [msdyn_serviceconfiguration business_unit_msdyn_serviceconfiguration](msdyn_serviceconfiguration.md#BKMK_business_unit_msdyn_serviceconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_serviceconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_serviceconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_slakpi"></a> business_unit_msdyn_slakpi

Many-To-One Relationship: [msdyn_slakpi business_unit_msdyn_slakpi](msdyn_slakpi.md#BKMK_business_unit_msdyn_slakpi)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_slakpi`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_slakpi`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_solutionhealthrule"></a> business_unit_msdyn_solutionhealthrule

Many-To-One Relationship: [msdyn_solutionhealthrule business_unit_msdyn_solutionhealthrule](msdyn_solutionhealthrule.md#BKMK_business_unit_msdyn_solutionhealthrule)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthrule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_solutionhealthrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_solutionhealthruleargument"></a> business_unit_msdyn_solutionhealthruleargument

Many-To-One Relationship: [msdyn_solutionhealthruleargument business_unit_msdyn_solutionhealthruleargument](msdyn_solutionhealthruleargument.md#BKMK_business_unit_msdyn_solutionhealthruleargument)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_solutionhealthruleargument`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_solutionhealthruleargument`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdyn_virtualtablecolumncandidate"></a> business_unit_msdyn_virtualtablecolumncandidate

Many-To-One Relationship: [msdyn_virtualtablecolumncandidate business_unit_msdyn_virtualtablecolumncandidate](msdyn_virtualtablecolumncandidate.md#BKMK_business_unit_msdyn_virtualtablecolumncandidate)

|Property|Value|
|---|---|
|ReferencingEntity|`msdyn_virtualtablecolumncandidate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdyn_virtualtablecolumncandidate`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_msdynce_botcontent"></a> business_unit_msdynce_botcontent

Many-To-One Relationship: [msdynce_botcontent business_unit_msdynce_botcontent](msdynce_botcontent.md#BKMK_business_unit_msdynce_botcontent)

|Property|Value|
|---|---|
|ReferencingEntity|`msdynce_botcontent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_msdynce_botcontent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_mspcat_catalogsubmissionfiles"></a> business_unit_mspcat_catalogsubmissionfiles

Many-To-One Relationship: [mspcat_catalogsubmissionfiles business_unit_mspcat_catalogsubmissionfiles](mspcat_catalogsubmissionfiles.md#BKMK_business_unit_mspcat_catalogsubmissionfiles)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_catalogsubmissionfiles`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_mspcat_catalogsubmissionfiles`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_mspcat_packagestore"></a> business_unit_mspcat_packagestore

Many-To-One Relationship: [mspcat_packagestore business_unit_mspcat_packagestore](mspcat_packagestore.md#BKMK_business_unit_mspcat_packagestore)

|Property|Value|
|---|---|
|ReferencingEntity|`mspcat_packagestore`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_mspcat_packagestore`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_nlsqregistration"></a> business_unit_nlsqregistration

Many-To-One Relationship: [nlsqregistration business_unit_nlsqregistration](nlsqregistration.md#BKMK_business_unit_nlsqregistration)

|Property|Value|
|---|---|
|ReferencingEntity|`nlsqregistration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_nlsqregistration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_parent_business_unit-one-to-many"></a> business_unit_parent_business_unit

Many-To-One Relationship: [businessunit business_unit_parent_business_unit](#BKMK_business_unit_parent_business_unit-many-to-one)

|Property|Value|
|---|---|
|ReferencingEntity|`businessunit`|
|ReferencingAttribute|`parentbusinessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_parent_business_unit`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_personaldocumenttemplates"></a> business_unit_personaldocumenttemplates

Many-To-One Relationship: [personaldocumenttemplate business_unit_personaldocumenttemplates](personaldocumenttemplate.md#BKMK_business_unit_personaldocumenttemplates)

|Property|Value|
|---|---|
|ReferencingEntity|`personaldocumenttemplate`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_personaldocumenttemplates`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_phone_call_activities"></a> business_unit_phone_call_activities

Many-To-One Relationship: [phonecall business_unit_phone_call_activities](phonecall.md#BKMK_business_unit_phone_call_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`phonecall`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_phone_call_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_plannerbusinessscenario"></a> business_unit_plannerbusinessscenario

Many-To-One Relationship: [plannerbusinessscenario business_unit_plannerbusinessscenario](plannerbusinessscenario.md#BKMK_business_unit_plannerbusinessscenario)

|Property|Value|
|---|---|
|ReferencingEntity|`plannerbusinessscenario`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_plannerbusinessscenario`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_plannersyncaction"></a> business_unit_plannersyncaction

Many-To-One Relationship: [plannersyncaction business_unit_plannersyncaction](plannersyncaction.md#BKMK_business_unit_plannersyncaction)

|Property|Value|
|---|---|
|ReferencingEntity|`plannersyncaction`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_plannersyncaction`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_plugin"></a> business_unit_plugin

Many-To-One Relationship: [plugin business_unit_plugin](plugin.md#BKMK_business_unit_plugin)

|Property|Value|
|---|---|
|ReferencingEntity|`plugin`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_plugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_postfollows"></a> business_unit_postfollows

Many-To-One Relationship: [postfollow business_unit_postfollows](postfollow.md#BKMK_business_unit_postfollows)

|Property|Value|
|---|---|
|ReferencingEntity|`postfollow`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_postfollows`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_PostRegarding"></a> business_unit_PostRegarding

Many-To-One Relationship: [postregarding business_unit_PostRegarding](postregarding.md#BKMK_business_unit_PostRegarding)

|Property|Value|
|---|---|
|ReferencingEntity|`postregarding`|
|ReferencingAttribute|`regardingobjectowningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_PostRegarding`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerbidataset"></a> business_unit_powerbidataset

Many-To-One Relationship: [powerbidataset business_unit_powerbidataset](powerbidataset.md#BKMK_business_unit_powerbidataset)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidataset`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerbidataset`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerbidatasetapdx"></a> business_unit_powerbidatasetapdx

Many-To-One Relationship: [powerbidatasetapdx business_unit_powerbidatasetapdx](powerbidatasetapdx.md#BKMK_business_unit_powerbidatasetapdx)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbidatasetapdx`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerbidatasetapdx`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerbimashupparameter"></a> business_unit_powerbimashupparameter

Many-To-One Relationship: [powerbimashupparameter business_unit_powerbimashupparameter](powerbimashupparameter.md#BKMK_business_unit_powerbimashupparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbimashupparameter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerbimashupparameter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerbireport"></a> business_unit_powerbireport

Many-To-One Relationship: [powerbireport business_unit_powerbireport](powerbireport.md#BKMK_business_unit_powerbireport)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireport`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerbireport`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerbireportapdx"></a> business_unit_powerbireportapdx

Many-To-One Relationship: [powerbireportapdx business_unit_powerbireportapdx](powerbireportapdx.md#BKMK_business_unit_powerbireportapdx)

|Property|Value|
|---|---|
|ReferencingEntity|`powerbireportapdx`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerbireportapdx`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerfxrule"></a> business_unit_powerfxrule

Many-To-One Relationship: [powerfxrule business_unit_powerfxrule](powerfxrule.md#BKMK_business_unit_powerfxrule)

|Property|Value|
|---|---|
|ReferencingEntity|`powerfxrule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerfxrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagecomponent"></a> business_unit_powerpagecomponent

Many-To-One Relationship: [powerpagecomponent business_unit_powerpagecomponent](powerpagecomponent.md#BKMK_business_unit_powerpagecomponent)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagecomponent`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagecomponent`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagesddosalert"></a> business_unit_powerpagesddosalert

Many-To-One Relationship: [powerpagesddosalert business_unit_powerpagesddosalert](powerpagesddosalert.md#BKMK_business_unit_powerpagesddosalert)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesddosalert`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagesddosalert`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagesite"></a> business_unit_powerpagesite

Many-To-One Relationship: [powerpagesite business_unit_powerpagesite](powerpagesite.md#BKMK_business_unit_powerpagesite)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesite`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagesite`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagesitelanguage"></a> business_unit_powerpagesitelanguage

Many-To-One Relationship: [powerpagesitelanguage business_unit_powerpagesitelanguage](powerpagesitelanguage.md#BKMK_business_unit_powerpagesitelanguage)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitelanguage`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagesitelanguage`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagesitepublished"></a> business_unit_powerpagesitepublished

Many-To-One Relationship: [powerpagesitepublished business_unit_powerpagesitepublished](powerpagesitepublished.md#BKMK_business_unit_powerpagesitepublished)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesitepublished`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagesitepublished`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpageslog"></a> business_unit_powerpageslog

Many-To-One Relationship: [powerpageslog business_unit_powerpageslog](powerpageslog.md#BKMK_business_unit_powerpageslog)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpageslog`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpageslog`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagesmanagedidentity"></a> business_unit_powerpagesmanagedidentity

Many-To-One Relationship: [powerpagesmanagedidentity business_unit_powerpagesmanagedidentity](powerpagesmanagedidentity.md#BKMK_business_unit_powerpagesmanagedidentity)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesmanagedidentity`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagesmanagedidentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagesscanreport"></a> business_unit_powerpagesscanreport

Many-To-One Relationship: [powerpagesscanreport business_unit_powerpagesscanreport](powerpagesscanreport.md#BKMK_business_unit_powerpagesscanreport)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagesscanreport`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagesscanreport`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagessiteaifeedback"></a> business_unit_powerpagessiteaifeedback

Many-To-One Relationship: [powerpagessiteaifeedback business_unit_powerpagessiteaifeedback](powerpagessiteaifeedback.md#BKMK_business_unit_powerpagessiteaifeedback)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagessiteaifeedback`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagessiteaifeedback`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_powerpagessourcefile"></a> business_unit_powerpagessourcefile

Many-To-One Relationship: [powerpagessourcefile business_unit_powerpagessourcefile](powerpagessourcefile.md#BKMK_business_unit_powerpagessourcefile)

|Property|Value|
|---|---|
|ReferencingEntity|`powerpagessourcefile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_powerpagessourcefile`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_privilegecheckerrun"></a> business_unit_privilegecheckerrun

Many-To-One Relationship: [privilegecheckerrun business_unit_privilegecheckerrun](privilegecheckerrun.md#BKMK_business_unit_privilegecheckerrun)

|Property|Value|
|---|---|
|ReferencingEntity|`privilegecheckerrun`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_privilegecheckerrun`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_processstageparameter"></a> business_unit_processstageparameter

Many-To-One Relationship: [processstageparameter business_unit_processstageparameter](processstageparameter.md#BKMK_business_unit_processstageparameter)

|Property|Value|
|---|---|
|ReferencingEntity|`processstageparameter`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_processstageparameter`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_queues"></a> business_unit_queues

Many-To-One Relationship: [queue business_unit_queues](queue.md#BKMK_business_unit_queues)

|Property|Value|
|---|---|
|ReferencingEntity|`queue`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_queues`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_queues2"></a> business_unit_queues2

Many-To-One Relationship: [queue business_unit_queues2](queue.md#BKMK_business_unit_queues2)

|Property|Value|
|---|---|
|ReferencingEntity|`queue`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_queues2`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_recentlyused"></a> business_unit_recentlyused

Many-To-One Relationship: [recentlyused business_unit_recentlyused](recentlyused.md#BKMK_business_unit_recentlyused)

|Property|Value|
|---|---|
|ReferencingEntity|`recentlyused`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_recentlyused`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_recurrencerule"></a> business_unit_recurrencerule

Many-To-One Relationship: [recurrencerule business_unit_recurrencerule](recurrencerule.md#BKMK_business_unit_recurrencerule)

|Property|Value|
|---|---|
|ReferencingEntity|`recurrencerule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_recurrencerule`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_recurringappointmentmaster_activities"></a> business_unit_recurringappointmentmaster_activities

Many-To-One Relationship: [recurringappointmentmaster business_unit_recurringappointmentmaster_activities](recurringappointmentmaster.md#BKMK_business_unit_recurringappointmentmaster_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`recurringappointmentmaster`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_recurringappointmentmaster_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_reports"></a> business_unit_reports

Many-To-One Relationship: [report business_unit_reports](report.md#BKMK_business_unit_reports)

|Property|Value|
|---|---|
|ReferencingEntity|`report`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_reports`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_retaineddataexcel"></a> business_unit_retaineddataexcel

Many-To-One Relationship: [retaineddataexcel business_unit_retaineddataexcel](retaineddataexcel.md#BKMK_business_unit_retaineddataexcel)

|Property|Value|
|---|---|
|ReferencingEntity|`retaineddataexcel`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_retaineddataexcel`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_retentionconfig"></a> business_unit_retentionconfig

Many-To-One Relationship: [retentionconfig business_unit_retentionconfig](retentionconfig.md#BKMK_business_unit_retentionconfig)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionconfig`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_retentionconfig`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_retentionfailuredetail"></a> business_unit_retentionfailuredetail

Many-To-One Relationship: [retentionfailuredetail business_unit_retentionfailuredetail](retentionfailuredetail.md#BKMK_business_unit_retentionfailuredetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionfailuredetail`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_retentionfailuredetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_retentionoperation"></a> business_unit_retentionoperation

Many-To-One Relationship: [retentionoperation business_unit_retentionoperation](retentionoperation.md#BKMK_business_unit_retentionoperation)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionoperation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_retentionoperation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_retentionsuccessdetail"></a> business_unit_retentionsuccessdetail

Many-To-One Relationship: [retentionsuccessdetail business_unit_retentionsuccessdetail](retentionsuccessdetail.md#BKMK_business_unit_retentionsuccessdetail)

|Property|Value|
|---|---|
|ReferencingEntity|`retentionsuccessdetail`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_retentionsuccessdetail`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_roles"></a> business_unit_roles

Many-To-One Relationship: [role business_unit_roles](role.md#BKMK_business_unit_roles)

|Property|Value|
|---|---|
|ReferencingEntity|`role`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_roles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_savingrule"></a> business_unit_savingrule

Many-To-One Relationship: [savingrule business_unit_savingrule](savingrule.md#BKMK_business_unit_savingrule)

|Property|Value|
|---|---|
|ReferencingEntity|`savingrule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_savingrule`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_sharepointdocumentlocation"></a> business_unit_sharepointdocumentlocation

Many-To-One Relationship: [sharepointdocumentlocation business_unit_sharepointdocumentlocation](sharepointdocumentlocation.md#BKMK_business_unit_sharepointdocumentlocation)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointdocumentlocation`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_sharepointdocumentlocation`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_sharepointsites"></a> business_unit_sharepointsites

Many-To-One Relationship: [sharepointsite business_unit_sharepointsites](sharepointsite.md#BKMK_business_unit_sharepointsites)

|Property|Value|
|---|---|
|ReferencingEntity|`sharepointsite`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_sharepointsites`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_sideloadedaiplugin"></a> business_unit_sideloadedaiplugin

Many-To-One Relationship: [sideloadedaiplugin business_unit_sideloadedaiplugin](sideloadedaiplugin.md#BKMK_business_unit_sideloadedaiplugin)

|Property|Value|
|---|---|
|ReferencingEntity|`sideloadedaiplugin`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_sideloadedaiplugin`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_signal"></a> business_unit_signal

Many-To-One Relationship: [signal business_unit_signal](signal.md#BKMK_business_unit_signal)

|Property|Value|
|---|---|
|ReferencingEntity|`signal`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_signal`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_slabase"></a> business_unit_slabase

Many-To-One Relationship: [sla business_unit_slabase](sla.md#BKMK_business_unit_slabase)

|Property|Value|
|---|---|
|ReferencingEntity|`sla`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_slabase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_slakpiinstance"></a> business_unit_slakpiinstance

Many-To-One Relationship: [slakpiinstance business_unit_slakpiinstance](slakpiinstance.md#BKMK_business_unit_slakpiinstance)

|Property|Value|
|---|---|
|ReferencingEntity|`slakpiinstance`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_slakpiinstance`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_socialactivity"></a> business_unit_socialactivity

Many-To-One Relationship: [socialactivity business_unit_socialactivity](socialactivity.md#BKMK_business_unit_socialactivity)

|Property|Value|
|---|---|
|ReferencingEntity|`socialactivity`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_socialactivity`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_socialprofiles"></a> business_unit_socialprofiles

Many-To-One Relationship: [socialprofile business_unit_socialprofiles](socialprofile.md#BKMK_business_unit_socialprofiles)

|Property|Value|
|---|---|
|ReferencingEntity|`socialprofile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_socialprofiles`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_solutioncomponentbatchconfiguration"></a> business_unit_solutioncomponentbatchconfiguration

Many-To-One Relationship: [solutioncomponentbatchconfiguration business_unit_solutioncomponentbatchconfiguration](solutioncomponentbatchconfiguration.md#BKMK_business_unit_solutioncomponentbatchconfiguration)

|Property|Value|
|---|---|
|ReferencingEntity|`solutioncomponentbatchconfiguration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_solutioncomponentbatchconfiguration`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_stagesolutionupload"></a> business_unit_stagesolutionupload

Many-To-One Relationship: [stagesolutionupload business_unit_stagesolutionupload](stagesolutionupload.md#BKMK_business_unit_stagesolutionupload)

|Property|Value|
|---|---|
|ReferencingEntity|`stagesolutionupload`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_stagesolutionupload`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_synapsedatabase"></a> business_unit_synapsedatabase

Many-To-One Relationship: [synapsedatabase business_unit_synapsedatabase](synapsedatabase.md#BKMK_business_unit_synapsedatabase)

|Property|Value|
|---|---|
|ReferencingEntity|`synapsedatabase`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_synapsedatabase`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_system_users"></a> business_unit_system_users

Many-To-One Relationship: [systemuser business_unit_system_users](systemuser.md#BKMK_business_unit_system_users)

|Property|Value|
|---|---|
|ReferencingEntity|`systemuser`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_system_users`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_tag"></a> business_unit_tag

Many-To-One Relationship: [tag business_unit_tag](tag.md#BKMK_business_unit_tag)

|Property|Value|
|---|---|
|ReferencingEntity|`tag`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_tag`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_taggedflowsession"></a> business_unit_taggedflowsession

Many-To-One Relationship: [taggedflowsession business_unit_taggedflowsession](taggedflowsession.md#BKMK_business_unit_taggedflowsession)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedflowsession`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_taggedflowsession`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_taggedprocess"></a> business_unit_taggedprocess

Many-To-One Relationship: [taggedprocess business_unit_taggedprocess](taggedprocess.md#BKMK_business_unit_taggedprocess)

|Property|Value|
|---|---|
|ReferencingEntity|`taggedprocess`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_taggedprocess`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_task_activities"></a> business_unit_task_activities

Many-To-One Relationship: [task business_unit_task_activities](task.md#BKMK_business_unit_task_activities)

|Property|Value|
|---|---|
|ReferencingEntity|`task`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_task_activities`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_teams"></a> business_unit_teams

Many-To-One Relationship: [team business_unit_teams](team.md#BKMK_business_unit_teams)

|Property|Value|
|---|---|
|ReferencingEntity|`team`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_teams`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_templates"></a> business_unit_templates

Many-To-One Relationship: [template business_unit_templates](template.md#BKMK_business_unit_templates)

|Property|Value|
|---|---|
|ReferencingEntity|`template`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_templates`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_trait"></a> business_unit_trait

Many-To-One Relationship: [trait business_unit_trait](trait.md#BKMK_business_unit_trait)

|Property|Value|
|---|---|
|ReferencingEntity|`trait`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_trait`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_unstructuredfilesearchentity"></a> business_unit_unstructuredfilesearchentity

Many-To-One Relationship: [unstructuredfilesearchentity business_unit_unstructuredfilesearchentity](unstructuredfilesearchentity.md#BKMK_business_unit_unstructuredfilesearchentity)

|Property|Value|
|---|---|
|ReferencingEntity|`unstructuredfilesearchentity`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_unstructuredfilesearchentity`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_unstructuredfilesearchrecord"></a> business_unit_unstructuredfilesearchrecord

Many-To-One Relationship: [unstructuredfilesearchrecord business_unit_unstructuredfilesearchrecord](unstructuredfilesearchrecord.md#BKMK_business_unit_unstructuredfilesearchrecord)

|Property|Value|
|---|---|
|ReferencingEntity|`unstructuredfilesearchrecord`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_unstructuredfilesearchrecord`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_user_settings"></a> business_unit_user_settings

Many-To-One Relationship: [usersettings business_unit_user_settings](usersettings.md#BKMK_business_unit_user_settings)

|Property|Value|
|---|---|
|ReferencingEntity|`usersettings`|
|ReferencingAttribute|`businessunitid`|
|ReferencedEntityNavigationPropertyName|`business_unit_user_settings`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_userform"></a> business_unit_userform

Many-To-One Relationship: [userform business_unit_userform](userform.md#BKMK_business_unit_userform)

|Property|Value|
|---|---|
|ReferencingEntity|`userform`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_userform`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_userquery"></a> business_unit_userquery

Many-To-One Relationship: [userquery business_unit_userquery](userquery.md#BKMK_business_unit_userquery)

|Property|Value|
|---|---|
|ReferencingEntity|`userquery`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_userquery`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_userqueryvisualizations"></a> business_unit_userqueryvisualizations

Many-To-One Relationship: [userqueryvisualization business_unit_userqueryvisualizations](userqueryvisualization.md#BKMK_business_unit_userqueryvisualizations)

|Property|Value|
|---|---|
|ReferencingEntity|`userqueryvisualization`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_userqueryvisualizations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_workflow"></a> business_unit_workflow

Many-To-One Relationship: [workflow business_unit_workflow](workflow.md#BKMK_business_unit_workflow)

|Property|Value|
|---|---|
|ReferencingEntity|`workflow`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_workflow`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_workflowbinary"></a> business_unit_workflowbinary

Many-To-One Relationship: [workflowbinary business_unit_workflowbinary](workflowbinary.md#BKMK_business_unit_workflowbinary)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowbinary`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_workflowbinary`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_workflowlogs"></a> business_unit_workflowlogs

Many-To-One Relationship: [workflowlog business_unit_workflowlogs](workflowlog.md#BKMK_business_unit_workflowlogs)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowlog`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_workflowlogs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_workflowmetadata"></a> business_unit_workflowmetadata

Many-To-One Relationship: [workflowmetadata business_unit_workflowmetadata](workflowmetadata.md#BKMK_business_unit_workflowmetadata)

|Property|Value|
|---|---|
|ReferencingEntity|`workflowmetadata`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_workflowmetadata`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_workqueue"></a> business_unit_workqueue

Many-To-One Relationship: [workqueue business_unit_workqueue](workqueue.md#BKMK_business_unit_workqueue)

|Property|Value|
|---|---|
|ReferencingEntity|`workqueue`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_workqueue`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_business_unit_workqueueitem"></a> business_unit_workqueueitem

Many-To-One Relationship: [workqueueitem business_unit_workqueueitem](workqueueitem.md#BKMK_business_unit_workqueueitem)

|Property|Value|
|---|---|
|ReferencingEntity|`workqueueitem`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`business_unit_workqueueitem`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_AsyncOperations"></a> BusinessUnit_AsyncOperations

Many-To-One Relationship: [asyncoperation BusinessUnit_AsyncOperations](asyncoperation.md#BKMK_BusinessUnit_AsyncOperations)

|Property|Value|
|---|---|
|ReferencingEntity|`asyncoperation`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_AsyncOperations`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_BulkDeleteFailures"></a> BusinessUnit_BulkDeleteFailures

Many-To-One Relationship: [bulkdeletefailure BusinessUnit_BulkDeleteFailures](bulkdeletefailure.md#BKMK_BusinessUnit_BulkDeleteFailures)

|Property|Value|
|---|---|
|ReferencingEntity|`bulkdeletefailure`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_BulkDeleteFailures`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_businessunit_callbackregistration"></a> businessunit_callbackregistration

Many-To-One Relationship: [callbackregistration businessunit_callbackregistration](callbackregistration.md#BKMK_businessunit_callbackregistration)

|Property|Value|
|---|---|
|ReferencingEntity|`callbackregistration`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`businessunit_callbackregistration`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_businessunit_canvasapp"></a> businessunit_canvasapp

Many-To-One Relationship: [canvasapp businessunit_canvasapp](canvasapp.md#BKMK_businessunit_canvasapp)

|Property|Value|
|---|---|
|ReferencingEntity|`canvasapp`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`businessunit_canvasapp`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_DuplicateRules"></a> BusinessUnit_DuplicateRules

Many-To-One Relationship: [duplicaterule BusinessUnit_DuplicateRules](duplicaterule.md#BKMK_BusinessUnit_DuplicateRules)

|Property|Value|
|---|---|
|ReferencingEntity|`duplicaterule`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_DuplicateRules`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_ImportData"></a> BusinessUnit_ImportData

Many-To-One Relationship: [importdata BusinessUnit_ImportData](importdata.md#BKMK_BusinessUnit_ImportData)

|Property|Value|
|---|---|
|ReferencingEntity|`importdata`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_ImportData`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_ImportFiles"></a> BusinessUnit_ImportFiles

Many-To-One Relationship: [importfile BusinessUnit_ImportFiles](importfile.md#BKMK_BusinessUnit_ImportFiles)

|Property|Value|
|---|---|
|ReferencingEntity|`importfile`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_ImportFiles`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_ImportLogs"></a> BusinessUnit_ImportLogs

Many-To-One Relationship: [importlog BusinessUnit_ImportLogs](importlog.md#BKMK_BusinessUnit_ImportLogs)

|Property|Value|
|---|---|
|ReferencingEntity|`importlog`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_ImportLogs`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_ImportMaps"></a> BusinessUnit_ImportMaps

Many-To-One Relationship: [importmap BusinessUnit_ImportMaps](importmap.md#BKMK_BusinessUnit_ImportMaps)

|Property|Value|
|---|---|
|ReferencingEntity|`importmap`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_ImportMaps`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_Imports"></a> BusinessUnit_Imports

Many-To-One Relationship: [import BusinessUnit_Imports](import.md#BKMK_BusinessUnit_Imports)

|Property|Value|
|---|---|
|ReferencingEntity|`import`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_Imports`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_businessunit_mailboxtrackingfolder"></a> businessunit_mailboxtrackingfolder

Many-To-One Relationship: [mailboxtrackingfolder businessunit_mailboxtrackingfolder](mailboxtrackingfolder.md#BKMK_businessunit_mailboxtrackingfolder)

|Property|Value|
|---|---|
|ReferencingEntity|`mailboxtrackingfolder`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`businessunit_mailboxtrackingfolder`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_businessunit_principalobjectattributeaccess"></a> businessunit_principalobjectattributeaccess

Many-To-One Relationship: [principalobjectattributeaccess businessunit_principalobjectattributeaccess](principalobjectattributeaccess.md#BKMK_businessunit_principalobjectattributeaccess)

|Property|Value|
|---|---|
|ReferencingEntity|`principalobjectattributeaccess`|
|ReferencingAttribute|`objectid`|
|ReferencedEntityNavigationPropertyName|`businessunit_principalobjectattributeaccess`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_ProcessSessions"></a> BusinessUnit_ProcessSessions

Many-To-One Relationship: [processsession BusinessUnit_ProcessSessions](processsession.md#BKMK_BusinessUnit_ProcessSessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_ProcessSessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `UseCollectionName`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: 110<br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_SyncError"></a> BusinessUnit_SyncError

Many-To-One Relationship: [syncerror BusinessUnit_SyncError](syncerror.md#BKMK_BusinessUnit_SyncError)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_SyncError`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_BusinessUnit_SyncErrors"></a> BusinessUnit_SyncErrors

Many-To-One Relationship: [syncerror BusinessUnit_SyncErrors](syncerror.md#BKMK_BusinessUnit_SyncErrors)

|Property|Value|
|---|---|
|ReferencingEntity|`syncerror`|
|ReferencingAttribute|`regardingobjectid`|
|ReferencedEntityNavigationPropertyName|`BusinessUnit_SyncErrors`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_chat_businessunit_owningbusinessunit"></a> chat_businessunit_owningbusinessunit

Many-To-One Relationship: [chat chat_businessunit_owningbusinessunit](chat.md#BKMK_chat_businessunit_owningbusinessunit)

|Property|Value|
|---|---|
|ReferencingEntity|`chat`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`chat_businessunit_owningbusinessunit`|
|IsCustomizable|`True`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|

### <a name="BKMK_Owning_businessunit_processsessions"></a> Owning_businessunit_processsessions

Many-To-One Relationship: [processsession Owning_businessunit_processsessions](processsession.md#BKMK_Owning_businessunit_processsessions)

|Property|Value|
|---|---|
|ReferencingEntity|`processsession`|
|ReferencingAttribute|`owningbusinessunit`|
|ReferencedEntityNavigationPropertyName|`Owning_businessunit_processsessions`|
|IsCustomizable|`False`|
|AssociatedMenuConfiguration|AvailableOffline: True<br />Behavior: `DoNotDisplay`<br />Group: `Details`<br />Label: <br />MenuId: null<br />Order: <br />QueryApi: null<br />ViewId: `00000000-0000-0000-0000-000000000000`|



### See also

[Dataverse table/entity reference](/power-apps/developer/data-platform/reference/about-entity-reference)  
[Dataverse Web API Reference](/power-apps/developer/data-platform/webapi/reference/about)   
<xref:Microsoft.Dynamics.CRM.businessunit?displayProperty=fullName>
